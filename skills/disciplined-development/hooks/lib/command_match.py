"""command_match — shlex tokenizer + the gh/git Bash matchers the
surviving hooks need.

Slim port of the old `dd_command_match.py` (kept: the quote-aware
newline-as-separator tokenizer, `is_git_commit`, `find_gh_pr_create`)
plus `commit_landed` (lifted from the deleted `review_debt.py`). Dropped:
`classify_shell_write` / `analyze_chain` (only the retired branch gate
and body cap used them) and `is_git_commit`'s wrapper-recursion variant
(only the retired branch gate needed it). Self-contained — no imports
from dd_lib / review_debt / dd_command_match (all deleted at cutover).

Public API:
  is_git_commit(command) -> bool
  looks_like_gh_pr_create(command) -> bool
  find_gh_pr_create(command) -> cwd | None
  commit_landed(command, tool_response) -> bool
"""

from __future__ import annotations

import os
import re
import shlex
from pathlib import Path

# ---- shared tokenizer -------------------------------------------------------

SHELLS = {"bash", "sh", "zsh", "/bin/bash", "/bin/sh", "/bin/zsh"}
SEPARATORS = {"&&", "||", ";", "|"}
ENV_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")
GIT_GLOBAL_FLAGS_WITH_VALUE = {
    "-C", "-c", "--git-dir", "--work-tree", "--namespace",
    "--exec-path", "--super-prefix",
}

# gh accepts global flags between `gh` and the subcommand; without
# skipping them the matcher returns None on real-world forms like
# `gh --repo org/repo pr create` and the pre-PR review is silently
# bypassed. Kept to the actual top-level globals — `--hostname` is a
# subcommand option on `gh auth`, not a gh-root flag, so including it
# here would silently skip user-typed positional tokens that gh itself
# would reject.
GH_GLOBAL_FLAGS_WITH_VALUE = {
    "-R", "--repo",
}


def _normalize_newlines(s: str) -> str:
    """Convert unquoted newlines to `;` so multi-line Bash tool invocations
    split into separate command segments.

    Bash treats unquoted newlines as command separators. `shlex.shlex` with
    `whitespace_split=True` collapses them into whitespace and silently
    merges multi-line commands, which would let a `git commit` on a second
    line hide behind a leading `git add` segment.

    Walk the string with a quote-aware state machine. Inside `'...'`
    newlines are literal. Inside `"..."` newlines are literal except for
    `\\\n` line continuation (collapsed). Outside any quote, a
    backslash-newline is line continuation (collapsed); an unescaped
    newline becomes `;`.
    """
    out: list[str] = []
    in_single = False
    in_double = False
    i = 0
    n = len(s)
    while i < n:
        c = s[i]
        if in_single:
            if c == "'":
                in_single = False
            out.append(c)
            i += 1
            continue
        if in_double:
            if c == "\\" and i + 1 < n and s[i + 1] == "\n":
                i += 2
                continue
            if c == '"':
                in_double = False
            out.append(c)
            i += 1
            continue
        if c == "'":
            in_single = True
            out.append(c)
            i += 1
            continue
        if c == '"':
            in_double = True
            out.append(c)
            i += 1
            continue
        if c == "\\" and i + 1 < n and s[i + 1] == "\n":
            i += 2
            continue
        if c == "\n":
            out.append(";")
            i += 1
            continue
        out.append(c)
        i += 1
    return "".join(out)


def tokenize(s: str) -> list[str] | None:
    """Shlex-tokenize. Returns tokens or None on failure (e.g. heredoc body)."""
    try:
        normalized = _normalize_newlines(s)
        lex = shlex.shlex(normalized, posix=True, punctuation_chars=True)
        lex.whitespace_split = True
        return list(lex)
    except Exception:
        return None


def split_segments(toks: list[str]) -> list[list[str]]:
    segments: list[list[str]] = []
    current: list[str] = []
    for tok in toks:
        if tok in SEPARATORS:
            if current:
                segments.append(current)
            current = []
        else:
            current.append(tok)
    if current:
        segments.append(current)
    return segments


def skip_env(toks: list[str]) -> int:
    k = 0
    while k < len(toks) and ENV_RE.match(toks[k]):
        k += 1
    return k


# ---- is-git-commit ----------------------------------------------------------


def _is_git_commit_seg(seg: list[str]) -> bool:
    """True iff this segment is a real `git commit`.

    Handles env-var prefixes (`FOO=1 git commit`) and git global
    flags (`-C`, `-c`, etc.). Rejects echo/grep wrappers,
    `git commit-tree`, and heredoc bodies (which fail to tokenize).

    Shell-wrapper segments (`bash -c 'git commit ...'`) return False —
    the surviving (advisory) consumers accept missing a wrapped commit;
    only the retired branch gate needed wrapper recursion.
    """
    i = skip_env(seg)
    if i >= len(seg) or seg[i] != "git":
        return False

    j = i + 1
    while j < len(seg):
        t = seg[j]
        if t in GIT_GLOBAL_FLAGS_WITH_VALUE:
            j += 2
        elif t.startswith("--") and "=" in t:
            j += 1
        elif t.startswith("-"):
            j += 1
        else:
            break
    return j < len(seg) and seg[j] == "commit"


def is_git_commit(command: str) -> bool:
    """True iff the command is a real `git commit` invocation
    (not recursing into shell wrappers)."""
    if not command:
        return False
    tokens = tokenize(command)
    if tokens is None:
        return False
    for seg in split_segments(tokens):
        if _is_git_commit_seg(seg):
            return True
    return False


# ---- find-gh-pr-create ------------------------------------------------------


# Word-bounded ordered match: the words `gh`, `pr`, `create` in order, any
# distance apart. `\b` treats `_` as a word char, so `pre_pr_review` contains
# no word `pr` and prose letter-runs (ri**gh**t / **pr**oject / **create**d)
# never match — only genuine word-level mentions do.
_LOOSE_PR_RE = re.compile(r"\bgh\b[\s\S]*?\bpr\b[\s\S]*?\bcreate\b")

# classify_gh_pr_create verdicts — a total union the pre-PR gate switches on.
VERDICT_NOT_PR = "not_pr"
VERDICT_PR = "pr"
VERDICT_PR_UNRESOLVABLE = "pr_unresolvable_cwd"
VERDICT_SUSPICIOUS = "untokenizable_suspicious"


def looks_like_gh_pr_create(command: str) -> bool:
    """Loose fail-closed net for commands `tokenize()` cannot parse (heredocs,
    unbalanced quotes) and for the gate's crash path: True when the WORDS
    `gh`, `pr`, `create` appear in that order anywhere in *command*.

    Word-bounded — ordinary prose whose words merely contain those letter
    sequences does not match. A word-level mention in unparseable input still
    does (e.g. a heredoc body quoting the command): **accepted, documented
    behavior** — there a false positive is a human-overridable block, while a
    false negative is a fail-open hole at the only hard gate in the stack.

    For TOKENIZABLE commands this net is deliberately never consulted —
    `classify_gh_pr_create`'s strict token scan is authoritative there.
    """
    return bool(_LOOSE_PR_RE.search(command))


def _seg_has_pr_triple(seg: list[str]) -> bool:
    """True when the segment contains the consecutive token sequence
    `gh` [gh-global-flags] `pr` `create` at ANY position.

    Position-independence replaces wrapper enumeration: `eval`/`env`/`nohup`/
    `xargs`-prefixed invocations match without naming each wrapper, and a
    quoted phrase (`grep "gh pr create"`) is a single token — never a triple.
    `echo gh pr create` matching is the documented over-broad bias, unchanged.
    """
    for k, tok in enumerate(seg):
        if tok != "gh":
            continue
        j = k + 1
        while j < len(seg):
            t = seg[j]
            if t in GH_GLOBAL_FLAGS_WITH_VALUE:
                j += 2  # `--repo org/repo` / `-R org/repo`
            elif t.startswith("-") and len(t) > 1:
                # `--repo=org/repo`, `-Rorg/repo`, `--paginate`, etc.
                j += 1
            else:
                break
        if j + 1 < len(seg) and seg[j] == "pr" and seg[j + 1] == "create":
            return True
    return False


def _classify_segments(segs: list[list[str]]) -> tuple[str, str | None]:
    """Strict token-level classification over split segments.

    Returns (verdict, cwd): VERDICT_PR with the resolved cwd,
    VERDICT_PR_UNRESOLVABLE when matched behind an unexpandable `cd`, or
    VERDICT_NOT_PR.
    """
    for seg_idx, seg in enumerate(segs):
        # Wrapped shells at ANY position (`nohup bash -c '…'`): recurse into
        # the string argument. `eval` concatenates its args into a command, so
        # a single string arg gets the same recursion.
        for j, tok in enumerate(seg):
            inner: str | None = None
            if tok in SHELLS and j + 1 < len(seg) and seg[j + 1] in ("-c", "-lc", "-cl"):
                if j + 2 < len(seg):
                    inner = seg[j + 2]
            elif tok == "eval" and j + 1 < len(seg):
                inner = " ".join(seg[j + 1 :])
            if inner:
                verdict, cwd = classify_gh_pr_create(inner)
                if verdict == VERDICT_PR:
                    return verdict, cwd
                if verdict in (VERDICT_PR_UNRESOLVABLE, VERDICT_SUSPICIOUS):
                    # An unparseable/unresolvable wrapped command is still a
                    # PR attempt whose cwd is unknown — fail loud, not open.
                    return VERDICT_PR_UNRESOLVABLE, None

        if not _seg_has_pr_triple(seg):
            continue

        # Chained `cd` resolution: walks every preceding segment, so the
        # LAST `cd` in the chain wins (each iteration overwrites `cwd`).
        # A relative `cd` is anchored to the process cwd, not to a prior
        # `cd` — so `cd /a && cd b && gh pr create` resolves to
        # `<process_cwd>/b`, not `/a/b`. The single-`cd` form (`cd /repo
        # && gh pr create`) is the only one we see in practice from the
        # `gh pr create` helper; chained or relative-after-absolute
        # forms are an accepted edge with this last-cd-wins contract.
        cwd: str | None = None
        cwd_unresolvable = False
        for prev_seg in segs[:seg_idx]:
            if len(prev_seg) >= 2 and prev_seg[0] == "cd":
                path = prev_seg[1]
                if "$" in path or "`" in path:
                    # Unexpandable target (shell var / substitution). Mark the
                    # cwd unresolvable; a LATER resolvable `cd` clears it
                    # (last-cd-wins), matching the resolvable branches below.
                    cwd_unresolvable = True
                    cwd = None
                elif os.path.isabs(path):
                    cwd = path
                    cwd_unresolvable = False
                else:
                    cwd = str(Path.cwd() / path)
                    cwd_unresolvable = False

        if cwd_unresolvable:
            # Matched, but the effective cwd can't be resolved — fail LOUD
            # rather than reviewing the wrong tree.
            return VERDICT_PR_UNRESOLVABLE, None
        if cwd is None:
            cwd = str(Path.cwd())
        return VERDICT_PR, cwd

    return VERDICT_NOT_PR, None


def classify_gh_pr_create(command: str) -> tuple[str, str | None]:
    """One total verdict for the pre-PR gate: (verdict, cwd).

      * VERDICT_NOT_PR          — allow (cwd None)
      * VERDICT_PR              — delegate to the review gate (cwd resolved)
      * VERDICT_PR_UNRESOLVABLE — matched but the `cd` target is unexpandable;
                                  block loud (cwd None)
      * VERDICT_SUSPICIOUS      — the command couldn't be tokenized AND
                                  mentions the words `gh pr create` in order;
                                  block loud (cwd None)

    Tokenizable commands are decided by the strict token scan ALONE — the
    word-bounded loose net runs only when `tokenize()` fails, where the
    genuine ambiguity lives (heredocs, unbalanced quotes).
    """
    if not command or not command.strip():
        return VERDICT_NOT_PR, None
    tokens = tokenize(command)
    if tokens is None:
        if looks_like_gh_pr_create(command):
            return VERDICT_SUSPICIOUS, None
        return VERDICT_NOT_PR, None
    return _classify_segments(split_segments(tokens))


def find_gh_pr_create(command: str) -> str | None:
    """Locate a `gh pr create` invocation and return its resolved cwd.

    Thin wrapper over `classify_gh_pr_create`: the resolved cwd for a
    VERDICT_PR, else `None` (not a PR, untokenizable, or matched with an
    unresolvable `cd` target — callers wanting the distinction use the
    classifier directly).
    """
    verdict, cwd = classify_gh_pr_create(command)
    return cwd if verdict == VERDICT_PR else None


# ---- commit-landed (from the deleted review_debt.py) ------------------------

# Git emits `[<branch> <short-sha>] <subject>` on every successful commit
# UNLESS `--quiet` / `-q` suppresses it. The PostToolUse cadence nudge
# needs a "did the commit actually land" gate.
_LANDED_MARKER_RE = re.compile(
    r"^\[[^\]\n]+\s[0-9a-fA-F]{4,}\]", re.MULTILINE,
)

# Word-boundary match for `--quiet` and `-q`. Symmetric form for both so
# the false-positive surface is identical.
_QUIET_RE = re.compile(r"(?<![\w-])(?:--quiet|-q)(?![\w-])")


def commit_landed(command: str, tool_response: dict | None) -> bool:
    """Return True iff the just-run Bash command landed a git commit.

    Two positive signals, in order:

    1. **Marker present.** Stdout contains the `[<branch> <short-sha>]`
       line git emits on every successful commit. Authoritative.
    2. **--quiet + exit 0.** `git commit --quiet` / `-q` is the only
       documented way to succeed without emitting the marker; for that
       case alone, exit_code=0 is the fallback positive signal.

    Everything else is False — failed commits and the whole dry-run flag
    family (`--dry-run` plus `--short`/`--porcelain`/`--long`, all of
    which imply `--dry-run`). No marker = nothing landed, so the
    marker-required gate rejects them naturally without flag enumeration.

    Advisory, not load-bearing: a missed nudge is recoverable on the next
    real commit. We trade narrow false negatives (stacked `-qm` — `_QUIET_RE`
    only matches `-q` as a standalone short flag, so the combined form reads
    as not-quiet and a marker-less quiet commit is missed; a quiet commit that
    FAILED but a trailing `; true` masked the exit code) and narrow false
    positives (a literal `--quiet` in a dry-run command's message text) for a
    small legible gate.

    Accepted even though both the post-commit verify reminder and the review
    cadence now ride this gate (2026-05-30): detecting `-q` inside a combined
    short-flag cluster correctly needs git short-flag arg-awareness (`-qm` is
    quiet+message but `-mq` is `-m "q"`), and a naive regex would trade the
    false-negative for a false-positive — the unbounded command-parsing
    precision the spec rejects (§"never police"). `-q` is rarely used by
    agents; the miss is recoverable and the pre-PR gate still catches.
    """
    if not isinstance(tool_response, dict):
        return False
    if _LANDED_MARKER_RE.search(tool_response.get("stdout") or ""):
        return True
    if not _QUIET_RE.search(command):
        return False
    return tool_response.get("exit_code") == 0
