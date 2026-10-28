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


# `gh pr new` is gh's alias for `gh pr create`.
PR_CREATE_SUBCOMMANDS = {"create", "new"}

_CONTINUATION_RE = re.compile(r"\\\r?\n")
_COMMAND_SEPARATOR_RE = re.compile(r"[;&|\n]")
# A word, or the head of a `$VAR` / `${VAR…}` reference (it may hold `gh`).
_WORD_RE = re.compile(r"\$\{?[A-Za-z_]|\w+")
# Characters that may sit next to a standalone `pr` token: whitespace,
# quotes and substitution brackets (`gh "pr" create`, `$(gh pr create)`).
_PR_EDGE_CHARS = set(" \t\r\"'`()")
# How far past `pr` to look for its verb. gh's only `pr`-level flag is
# `-R/--repo <value>`, so the verb sits within a few dozen characters.
_VERB_WINDOW = 200


def _unbalanced_quote(tok: str) -> bool:
    return bool(tok.count('"') % 2 or tok.count("'") % 2)


def _pr_verb(piece: str, start: int) -> str | None:
    """The verb after a `pr` token ending at *start*: `""` when the command
    ends first, `None` when it can't be known. Each token shape has one role:
    - a substitution (`$(`, an opening backtick) or ANSI-C/locale quoting
      (`$'…'`, `$"…"`) may produce the verb or span tokens: unknown;
    - the `-R/--repo` value (separate, or attached as `-R…` / `--repo=…`) is
      skipped, unless an unbalanced quote means it spans tokens
      (`-R "$(cat .repo)"`): unknown;
    - any other flag, an expansion that may hold flags (`$FLAGS`, `"$@"`),
      or an attached redirect (`2>/dev/null`): skipped;
    - anything else is the verb: its leading word, so `create>"$OUT"` reads
      as create and `#42:` as `""`.
    A verb past the window is unknown too."""
    window = piece[start:start + _VERB_WINDOW]
    tokens = window.split()
    cut = start + _VERB_WINDOW < len(piece)
    if cut:
        tokens = tokens[:-1]  # may be cut mid-token
    repo_value = False
    for tok in tokens:
        t = tok.strip("\"'`()")
        if not t:
            continue
        # A backtick only opens a substitution at the token's start; a closing
        # one ends a Markdown code span in prose (`gh pr view`).
        if "$(" in tok or tok.lstrip("\"'(").startswith(("`", "$'", '$"')):
            return None
        if re.match(r"\d*[<>]", t):
            continue  # attached redirect (`2>/dev/null`)
        if repo_value:
            if _unbalanced_quote(tok):
                return None
            repo_value = False
            continue
        if t in GH_GLOBAL_FLAGS_WITH_VALUE:
            repo_value = True
            continue
        if t.startswith(("-R", "--repo=")) and _unbalanced_quote(tok):
            return None  # attached value spans tokens
        if t.startswith(("-", "$")):
            continue
        return re.match(r"\w*", t).group()
    return None if cut else ""


def looks_like_gh_pr_create(command: str) -> bool:
    """Loose detector: True when one command in the raw text has the word
    `gh` (or a `$VAR`), then a `pr` token whose first non-flag token is
    `create` or `new`.

    Scans raw text rather than parsing shell, so every wrapper is caught
    (`env`, `timeout`, `sh -ec '…'`, `"$(cd x && gh pr create)"`,
    `$(which gh) pr create`). Only two steps model gh: commands split on
    `;`, `&`, `|` or newline (`gh pr view 12 && echo created` doesn't
    match), and the token after `pr`, skipping flags and `-R/--repo`'s value,
    decides the verb (`gh pr list --search create`, or "pr #42: new" in a
    `gh issue create` title, doesn't match). After any other verb, a later
    `pr` needs a fresh `gh`. Whole words only, so "through the printer …
    created" doesn't match. Linear: one pass plus a fixed window per `pr`.

    Shell tokenizing and a flag-aware regex both failed open on forms they
    didn't model and backtracked on long input; this scan errs toward True.
    `_pr_verb` gives each token shape after `pr` one role; a verb it can't
    know (a substitution, a `-R` value spanning tokens, past the window)
    counts as `create`. Accepted misses: a `;`/`&`/`|`/newline between `gh`
    and the verb, even one that isn't a command separator
    (`$(which gh 2>&1) pr create`); a verb held only in a variable
    (`gh pr $VERB`), which is skipped like a flag; and a spaced redirect
    before the verb (`gh pr > out create`).

    Deliberately over-broad: a mention of the whole command — unquoted
    (`echo gh pr create`) or quoted (a commit message, a grep pattern) —
    returns True. This is **accepted, documented behavior** — a false
    positive is a human-overridable block (the model can rewrite or the
    operator can set DD_SKIP_PR_REVIEW=1); a false negative is a fail-open
    hole at the only hard gate in the hook stack. Bias toward True.

    Use this as the fail-closed net when `find_gh_pr_create` returns `None`:
    `None` is ambiguous (not a PR *or* matched but cwd unresolvable); this
    function distinguishes "clearly not a PR" from "looks like one, block it".
    """
    text = _CONTINUATION_RE.sub(" ", command)
    for piece in _COMMAND_SEPARATOR_RE.split(text):
        seen_gh = False
        for m in _WORD_RE.finditer(piece):
            w = m.group()
            if w == "gh" or w.startswith("$"):
                seen_gh = True
            elif (
                w == "pr"
                and seen_gh
                and (m.start() == 0 or piece[m.start() - 1] in _PR_EDGE_CHARS)
                and (m.end() == len(piece) or piece[m.end()] in _PR_EDGE_CHARS)
            ):
                verb = _pr_verb(piece, m.end())
                if verb is None or verb in PR_CREATE_SUBCOMMANDS:
                    return True
                # This gh's verb is something else; a `pr` in its
                # arguments needs a fresh `gh` to count.
                seen_gh = False
    return False


def _skip_gh_flags(seg: list[str], j: int) -> int:
    """Index of the first non-flag token at or after *j*, skipping gh flags
    and the value of `-R` / `--repo`."""
    while j < len(seg):
        t = seg[j]
        if t in GH_GLOBAL_FLAGS_WITH_VALUE:
            j += 2  # `--repo org/repo` / `-R org/repo`
        elif t.startswith("-") and len(t) > 1:
            # `--repo=org/repo`, `-Rorg/repo`, `--paginate`, etc.
            j += 1
        else:
            break
    return j


_DIR_CHANGERS = {"cd", "pushd", "popd"}
_GROUPING = {"(", ")", "{", "}"}


def _resolve_cwd(prior: list[list[str]]) -> str | None:
    """The cwd a command runs in after the *prior* segments, or None when a
    directory change there isn't modelled.

    Only a leading `cd <explicit path>` is: an absolute path resets the cwd,
    a relative one joins it (the process cwd before any `cd`), as the shell
    does. Everything else returns None so the gate fails closed rather than
    reviewing the wrong tree: `pushd`/`popd`; a `cd` with grouping in play
    (`(cd x && …)`, `{ cd x; }` — subshell scoping); a `cd` that isn't its
    segment's first word (`then cd x`); `cd` with no path, an option, `-`
    or `~`; an unexpandable target (`$`/backtick), unless a later absolute
    `cd` resets it.
    """
    tokens = {t for seg in prior for t in seg}
    if not _DIR_CHANGERS & tokens:
        return str(Path.cwd())
    if {"pushd", "popd"} & tokens or _GROUPING & tokens:
        return None
    cwd: str | None = str(Path.cwd())
    for seg in prior:
        if "cd" not in seg:
            continue
        if seg[0] != "cd" or len(seg) < 2 or seg[1].startswith(("-", "~")):
            return None
        path = seg[1]
        if "$" in path or "`" in path:
            cwd = None
        elif os.path.isabs(path):
            cwd = path
        elif cwd is not None:
            cwd = str(Path(cwd) / path)
    return cwd


def find_gh_pr_create(command: str) -> str | None:
    """Locate a `gh pr create` (or `gh pr new`) invocation and return its resolved cwd.

    Return shape:
      * `None`  — not a `gh pr create|new` command, **or** matched but the
                  cwd can't be resolved (`_resolve_cwd` lists the cases;
                  the caller uses `looks_like_gh_pr_create` to distinguish
                  the two `None` cases and fail closed).
      * `str`   — the resolved cwd (the process cwd when nothing before the
                  `gh` changes directory).
    """
    if not command:
        return None
    tokens = tokenize(command)
    if tokens is None:
        return None

    segs = split_segments(tokens)
    for seg_idx, seg in enumerate(segs):
        i = skip_env(seg)

        if i < len(seg) and seg[i] in SHELLS:
            for j in range(i + 1, len(seg)):
                t = seg[j]
                if t in ("-c", "-lc", "-cl"):
                    if j + 1 < len(seg):
                        inner = tokenize(seg[j + 1])
                        if inner:
                            result = find_gh_pr_create(seg[j + 1])
                            if result is not None:
                                # The inner cwd assumed the process cwd;
                                # an outer directory change breaks that.
                                prior = {t for s in segs[:seg_idx] for t in s}
                                return None if _DIR_CHANGERS & prior else result
                    break
                if not t.startswith("-"):
                    break
            continue

        if i >= len(seg) or seg[i] != "gh":
            continue

        # Skip gh flags between `gh` and `pr` (global) and between `pr` and
        # the verb (`-R/--repo` is a `gh pr`-level flag).
        j = _skip_gh_flags(seg, i + 1)
        if j >= len(seg) or seg[j] != "pr":
            continue
        j = _skip_gh_flags(seg, j + 1)
        if j >= len(seg) or seg[j] not in PR_CREATE_SUBCOMMANDS:
            continue

        # Matched. A None cwd (unresolvable) makes the pre-PR gate fail LOUD
        # rather than failing open or reviewing the wrong tree; the caller
        # uses `looks_like_gh_pr_create` to tell it from the "not a PR" None.
        return _resolve_cwd(segs[:seg_idx])

    return None


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
