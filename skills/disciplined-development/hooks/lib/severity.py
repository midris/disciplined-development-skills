"""severity.py — finding and explicit-verdict parsing.

Line-start anchoring is load-bearing: the adversarial-review prompt itself
echoes ``[P0]``–``[P3]`` tokens, so only line-start-anchored matches count
when ``line_start=True``; mid-prose mentions must not inflate the count.
"""

from __future__ import annotations

import re

# ---- structured parsers (consumed by the review-record builder + gate) ------

# Line-start patterns with two pieces of tolerance, both empirically driven:
#
# 1. `(?:[*_]+)?` between the bullet/quote prefix and `\[` absorbs
#    markdown emphasis around the tag (e.g. `- **[P1]** ...`).
#
# 2. `(?![*_]*\s*(?:=|[—\-:]\s*(?:critical|important|minor|nit)\s*/))`
#    rejects the adversarial-review SKILL.md rubric shape that some
#    reviewers echo verbatim:
#        - **[P0]** — critical / blocks merge.
#        - **[P1]** — important / address before PR.
#    Three separators handled (em-dash, ASCII hyphen, colon). Two rejection
#    criteria:
#      - `[Pn] = ...` always rejected (legend-shape).
#      - `[Pn] (—|-|:) <label> /` where <label> is one of the four
#        rubric severity terms followed by a slash (the rubric's
#        distinctive separator, absent from real findings).
#
# Additionally captures everything after the `[Pn]` token as `rest`, which
# `parse_findings` splits into file/line/summary.
_FINDING_RE_LINE_START = re.compile(
    r"^\s*(?:[-*]|\d+[.)>])?\s*(?:>\s*[-*]?\s*)?(?:[*_]+)?\[(P[0-3])\]"
    r"(?![*_]*\s*(?:=|[—\-:]\s*(?:critical|important|minor|nit)\s*/))"
    r"[*_]*\s*(?P<rest>.*)$"
)
_FINDING_RE_ANY = re.compile(
    r"\[(P[0-3])\][*_]*\s*(?P<rest>.*)$"
)

# `<file>:<line>:<summary>` and the degraded `<file>:<summary>` (no line).
# Canonical `<path>:<line>:<summary>` parsing uses the final structural
# `:<digits>:` delimiter, so paths may contain spaces and colons. The
# degraded `<file>:<summary>` parser below retains the historical shape.
_FINDING_BODY_WITH_LINE_RE = re.compile(
    r"^(?P<file>\S(?:[^\r\n]*\S)?):(?P<line>\d+):\s*(?P<summary>.*)$"
)
_FINDING_BODY_RE = re.compile(r"^(?P<file>[^\s:]+):(?P<summary>.*)$")


def parse_findings(text: str, line_start: bool = True) -> list[dict]:
    """Parse reviewer output into structured findings (best-effort, log-only).

    Each finding line is ``- [PN] <file>:<line>: <summary>`` per the
    adversarial-review output format. Returns one dict per accepted line:
    ``{"severity", "file", "line", "summary"}``. Degraded shapes: a
    ``<file>:`` prefix without a numeric line yields ``line=None``; no
    ``<file>:`` prefix at all yields ``file=None, line=None`` and the whole
    remainder as ``summary``.

    Accepts lines with optional bullet/quote prefix and optional markdown
    emphasis around the ``[Pn]`` tag. Applies the rubric-echo guard (rejects
    ``[Pn] = ...`` and ``[Pn] (—|-|:) <severity-label> /`` shapes) so echoed
    rubric lines are excluded. The guard can drop a real finding whose summary
    starts with ``critical|important|minor|nit /``. Canonical paths may contain
    spaces and colons; when a summary also contains ``:<digits>:`` the final
    structural delimiter wins, so this remains best-effort telemetry. Parsed
    findings never override the declared verdict.
    """
    rx = _FINDING_RE_LINE_START if line_start else _FINDING_RE_ANY
    out: list[dict] = []
    for line in text.splitlines():
        m = rx.search(line)
        if not m:
            continue
        rest = m.group("rest").strip()
        body = _FINDING_BODY_WITH_LINE_RE.match(rest)
        if body:
            line_no = body.group("line")
            out.append({
                "severity": m.group(1),
                "file": body.group("file"),
                "line": int(line_no) if line_no is not None else None,
                "summary": body.group("summary").strip(),
            })
            continue
        body = _FINDING_BODY_RE.match(rest)
        if body:
            out.append({
                "severity": m.group(1),
                "file": body.group("file"),
                "line": None,
                "summary": body.group("summary").strip(),
            })
            continue
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
