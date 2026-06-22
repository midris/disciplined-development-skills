"""severity.py — self-contained finding-severity scan.

Owns ``count_severities`` + ``findings_excerpt`` (and the private regexes
they depend on) with no external dependency — the scan is a pure function of
the reviewer's stdout.

Line-start anchoring is load-bearing: the adversarial-review prompt itself
echoes ``[P0]``–``[P3]`` tokens, so only line-start-anchored matches count
when ``line_start=True``; mid-prose mentions must not inflate the count.

**Known limitation (drives the pre-PR hard block — read before re-tuning).**
The rubric-echo guard below is a regex interpreting the reviewer's prose; its
failure mode is *under-counting* a real ``[P0]``/``[P1]`` formatted exactly
like the rubric legend, which silently demotes a BLOCK to a PASS at the
system's only hard block. This is the scan-to-classify anti-pattern the spec
rejects elsewhere; the durable fix (reviewer-declared verdict) is tracked in
``plans/deferred/2026-05-30-dd-review-severity-verdict-deferred.md``. Do not
keep re-tuning this regex — escalate to that plan instead.
"""

from __future__ import annotations

import re

# ---- severity helpers -------------------------------------------------------

_SEV_PATTERNS_ANY = {i: re.compile(rf"\[P{i}\]") for i in range(4)}

# Line-start patterns. Two pieces of tolerance, both empirically driven:
#
# 1. `(?:[*_]+)?` between the bullet/quote prefix and `\[` absorbs
#    markdown emphasis around the tag. Discovered in the
#    review-speed-tuning experiment (R4 sonnet/medium pre-stuffed):
#    claude routinely formats findings as `- **[P1]** ...`. The
#    pre-fix regex matched the bullet then expected `[` next — the
#    `**` in between broke the match and the counter under-reported.
#
# 2. `(?![*_]*\s*(?:=|[—\-:]\s*(?:critical|important|minor|nit)\s*/))`
#    rejects the adversarial-review SKILL.md rubric shape that some
#    reviewers echo verbatim:
#        - **[P0]** — critical / blocks merge.
#        - **[P1]** — important / address before PR.
#    Three separators handled (em-dash, ASCII hyphen, colon) — codex on
#    PR #101 flagged the em-dash-only form as too narrow because models
#    can echo the rubric with `-` or `:` instead of `—` (typo or
#    normalization). Two rejection criteria:
#      - `[Pn] = ...` always rejected (legend-shape; real findings
#        never use `=` after the bracket).
#      - `[Pn] (—|-|:) <label> /` where <label> is one of the four
#        rubric severity terms followed by a slash. The slash is the
#        rubric's distinctive separator (`critical / blocks merge`,
#        `nit / optional`), absent from real findings even when they
#        happen to use the same vocabulary (`[P2] — minor cleanup ...`).
#    Caught and narrowed across three codex external review rounds.
_SEV_PATTERNS_LINE_START = {
    i: re.compile(
        rf"^\s*(?:[-*]|\d+[.)>])?\s*(?:>\s*[-*]?\s*)?(?:[*_]+)?\[P{i}\]"
        rf"(?![*_]*\s*(?:=|[—\-:]\s*(?:critical|important|minor|nit)\s*/))",
        re.MULTILINE,
    )
    for i in range(4)
}


def count_severities(text: str, line_start: bool = False) -> tuple[int, int, int, int]:
    """Count [P0]/[P1]/[P2]/[P3] mentions in text. Returns (p0, p1, p2, p3).

    ``line_start=True`` anchors to line start with optional bullet/quote
    prefix and optional markdown emphasis (`*`, `**`, `_`, `__`) around
    the bracket. Rejects rubric-definition shapes — `[P0] = ...` and
    `[P0] — critical|important|minor|nit ...` — so an echoed rubric
    doesn't inflate the finding count, while still counting real
    findings that use em-dash as a description separator.
    """
    pats = _SEV_PATTERNS_LINE_START if line_start else _SEV_PATTERNS_ANY
    return tuple(len(pats[i].findall(text)) for i in range(4))  # type: ignore[return-value]


_SEV_LINE_RE_ANY = re.compile(r"\[(P[0-3])\]")
# Same emphasis tolerance + narrowed rubric-echo guard as
# `_SEV_PATTERNS_LINE_START`. The two regexes must accept identical
# input shapes so `count_severities` and `findings_excerpt` never
# disagree about whether a line is a finding.
_SEV_LINE_RE_LINE_START = re.compile(
    r"^\s*(?:[-*]|\d+[.)>])?\s*(?:>\s*[-*]?\s*)?(?:[*_]+)?\[(P[0-3])\]"
    r"(?![*_]*\s*(?:=|[—\-:]\s*(?:critical|important|minor|nit)\s*/))"
)


def findings_excerpt(text: str, line_start: bool = False) -> str:
    """Return pipe-joined severity-tagged headlines (each ≤100 chars).

    Mirrors bash dd_findings_excerpt with the same modes.
    """
    rx = _SEV_LINE_RE_LINE_START if line_start else _SEV_LINE_RE_ANY
    out: list[str] = []
    for line in text.splitlines():
        if rx.search(line):
            headline = line.strip()
            if len(headline) > 100:
                headline = headline[:97] + "..."
            out.append(headline)
    return "|".join(out)


# ---- structured parsers (consumed by the review-record builder + gate) ------

# Mirrors the SAME line shape + rubric-echo guard as
# `_SEV_LINE_RE_LINE_START`/`_SEV_LINE_RE_ANY` (the two must agree on what
# counts as a finding), but additionally captures everything after the
# `[Pn]` token (any closing emphasis is consumed by the trailing `[*_]*`)
# as `rest`, which `parse_findings` splits into file/line/summary.
_FINDING_RE_LINE_START = re.compile(
    r"^\s*(?:[-*]|\d+[.)>])?\s*(?:>\s*[-*]?\s*)?(?:[*_]+)?\[(P[0-3])\]"
    r"(?![*_]*\s*(?:=|[—\-:]\s*(?:critical|important|minor|nit)\s*/))"
    r"[*_]*\s*(?P<rest>.*)$"
)
_FINDING_RE_ANY = re.compile(
    r"\[(P[0-3])\][*_]*\s*(?P<rest>.*)$"
)

# `<file>:<line>:<summary>` and the degraded `<file>:<summary>` (no line).
# The path is non-greedy and excludes whitespace/colon so it stops at the
# first delimiter; an integer line is the disambiguator between the two
# shapes. Anything without a leading `path:` falls through to file/line None.
_FINDING_BODY_RE = re.compile(r"^(?P<file>[^\s:]+):(?:(?P<line>\d+):)?\s*(?P<summary>.*)$")


def parse_findings(text: str, line_start: bool = True) -> list[dict]:
    """Parse reviewer output into structured findings (best-effort, log-only).

    Each finding line is ``- [PN] <file>:<line>: <summary>`` per the
    adversarial-review output format. Returns one dict per accepted line:
    ``{"severity", "file", "line", "summary"}``. Degraded shapes: a
    ``<file>:`` prefix without a numeric line yields ``line=None``; no
    ``<file>:`` prefix at all yields ``file=None, line=None`` and the whole
    remainder as ``summary``.

    Accepts the same line shapes as ``count_severities``/``findings_excerpt``
    (bullet/quote/markdown-emphasis tolerance) and applies the same
    rubric-echo guard, so the three agree on what counts as a finding. The
    guard can drop a real finding whose summary starts with
    ``critical|important|minor|nit /`` — accepted: findings are best-effort
    log data, never the gate decision.
    """
    rx = _FINDING_RE_LINE_START if line_start else _FINDING_RE_ANY
    out: list[dict] = []
    for line in text.splitlines():
        m = rx.search(line)
        if not m:
            continue
        rest = m.group("rest").strip()
        body = _FINDING_BODY_RE.match(rest)
        if body:
            line_no = body.group("line")
            out.append({
                "severity": m.group(1),
                "file": body.group("file"),
                "line": int(line_no) if line_no is not None else None,
                "summary": body.group("summary").strip(),
            })
        else:
            out.append({
                "severity": m.group(1),
                "file": None,
                "line": None,
                "summary": rest,
            })
    return out


_VERDICT_RE = re.compile(r"^\s*DD-VERDICT:\s*(PASS|BLOCK)\s*$", re.IGNORECASE)


def parse_verdict(text: str) -> str | None:
    """Return the reviewer's declared verdict, or ``None``.

    Examines the **last non-blank line only** — a verdict echoed earlier
    (e.g. a reviewer quoting the contract) is ignored unless the final
    non-blank line is itself a verdict line. Result is normalized to
    uppercase ``"PASS"``/``"BLOCK"``.
    """
    for line in reversed(text.splitlines()):
        if not line.strip():
            continue
        m = _VERDICT_RE.match(line)
        return m.group(1).upper() if m else None
    return None
