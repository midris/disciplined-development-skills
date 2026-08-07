"""Quote-aware matchers for direct git commits and ``gh pr create``.

The tokenizer treats unquoted newlines as command separators. ``is_git_commit``
intentionally examines direct command segments only; it does not recurse into
shell wrappers. The commit ceiling and post-commit nudge share that boundary.
The target matchers accept only a standalone action in the payload cwd;
compounds fail closed.

Public API:
  is_git_commit(command) -> bool
  looks_like_gh_pr_create(command) -> bool
  find_git_commit(command, base_cwd, env=None) -> cwd | None
  find_gh_pr_create(command, base_cwd, env=None) -> cwd | None
  commit_landed(command, tool_response) -> bool
"""

from __future__ import annotations

import os
import re
import shlex

# ---- shared tokenizer -------------------------------------------------------

SEPARATORS = {"&&", "||", ";", "|", "&", "|&"}
ENV_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")
GIT_GLOBAL_FLAGS_WITH_VALUE = {
    "-C", "-c", "--git-dir", "--work-tree", "--namespace",
    "--exec-path", "--super-prefix",
}

# Recognize repository-selecting gh globals as PR-shaped so the loose gate can
# block them. The strict target resolver below rejects the selectors instead of
# attributing their action to the payload cwd.
_GIT_TARGET_ENV = frozenset({"GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR"})
_GIT_TARGET_FLAGS = frozenset({"-C", "--git-dir", "--work-tree"})
_GH_TARGET_FLAGS = frozenset({"-R", "--repo"})
_GH_PR_CREATE_FLAGS_WITH_VALUE = frozenset({
    "-a", "--assignee", "-B", "--base", "-b", "--body",
    "-F", "--body-file", "-H", "--head", "-l", "--label",
    "-m", "--milestone", "-p", "--project", "--recover",
    "-r", "--reviewer", "-T", "--template", "-t", "--title",
})


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


def _split_command(toks: list[str]) -> tuple[list[list[str]], list[str]]:
    """Return command segments and the separators between them."""
    segments: list[list[str]] = []
    separators: list[str] = []
    current: list[str] = []
    for tok in toks:
        if tok in SEPARATORS:
            if not current:
                return [], []
            segments.append(current)
            separators.append(tok)
            current = []
        else:
            current.append(tok)
    if not current:
        return [], []
    segments.append(current)
    return segments, separators


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

    Shell-wrapper segments (`bash -c 'git commit ...'`) return False. The
    commit ceiling and post-commit nudge therefore observe only direct git
    segments; wrapped commits are a known detection boundary.
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


def looks_like_gh_pr_create(command: str) -> bool:
    """Loose detector: True when `gh`, `pr`, `create` appear in that order
    anywhere in *command*, even when strict tokenizing fails (e.g. a heredoc
    body that makes `tokenize()` return `None`).

    Deliberately over-broad: a command that merely *mentions* these tokens
    (e.g. `echo gh pr create`) returns True. This is **accepted, documented
    behavior** — a false positive is a human-overridable block (the model can
    rewrite or the operator can set DD_SKIP_PR_REVIEW=1); a false negative is a
    fail-open hole at the hard gate guarding PR creation. Bias toward True.

    Use this as the fail-closed net when `find_gh_pr_create` returns `None`:
    `None` is ambiguous (not a PR *or* matched but cwd unresolvable); this
    function distinguishes "clearly not a PR" from "looks like one, block it".
    """
    pos = 0
    for token in ("gh", "pr", "create"):
        idx = command.find(token, pos)
        if idx == -1:
            return False
        pos = idx + len(token)
    return True


def _is_gh_pr_create_seg(seg: list[str]) -> bool:
    i = skip_env(seg)
    if i >= len(seg) or seg[i] != "gh":
        return False
    j = i + 1
    while j < len(seg) and seg[j].startswith("-"):
        flag = seg[j]
        if flag in _GH_TARGET_FLAGS:
            j += 2
        else:
            j += 1
    return j + 1 < len(seg) and seg[j:j + 2] == ["pr", "create"]


def _targeted_action(
    command: str,
    base_cwd: object,
    env: dict[str, str] | None,
    matcher,
    target_env: frozenset[str],
    has_target_flag,
) -> str | None:
    if not command:
        return None
    tokens = tokenize(command)
    if tokens is None:
        return None
    segments, separators = _split_command(tokens)
    if len(segments) != 1 or separators or not matcher(segments[0]):
        return None
    if not isinstance(base_cwd, str) or not base_cwd:
        return None
    selected_env = os.environ if env is None else env
    if any(name in selected_env for name in target_env):
        return None
    action = segments[0]
    for token in action[:skip_env(action)]:
        name = token.split("=", 1)[0]
        if name in target_env:
            return None
    if has_target_flag(action):
        return None
    return os.path.abspath(base_cwd)


def _git_has_target_flag(action: list[str]) -> bool:
    """Recognize repository selectors only before the ``commit`` subcommand."""
    i = skip_env(action) + 1
    while i < len(action) and action[i] != "commit":
        token = action[i]
        if token in _GIT_TARGET_FLAGS:
            return True
        if token.startswith("--git-dir=") or token.startswith("--work-tree="):
            return True
        if token.startswith("-C") and token != "-C":
            return True
        if token in GIT_GLOBAL_FLAGS_WITH_VALUE:
            i += 2
        else:
            i += 1
    return False


def _gh_has_target_flag(action: list[str]) -> bool:
    """Recognize ``-R``/``--repo`` only where gh parses option tokens."""
    expect_value = False
    for token in action[skip_env(action) + 1:]:
        if expect_value:
            expect_value = False
            continue
        if token == "--":
            break
        if token in _GH_TARGET_FLAGS or token.startswith("--repo="):
            return True
        if token.startswith("-R") and token != "-R":
            return True
        if token in _GH_PR_CREATE_FLAGS_WITH_VALUE:
            expect_value = True
    return False


def find_git_commit(
    command: str, base_cwd: object, env: dict[str, str] | None = None
) -> str | None:
    """Return the payload cwd for a standalone direct commit, else ``None``."""
    return _targeted_action(
        command, base_cwd, env, _is_git_commit_seg, _GIT_TARGET_ENV,
        _git_has_target_flag,
    )


def find_gh_pr_create(
    command: str, base_cwd: object, env: dict[str, str] | None = None
) -> str | None:
    """Return the payload cwd for a standalone direct PR create, else ``None``."""
    return _targeted_action(
        command,
        base_cwd,
        env,
        _is_gh_pr_create_seg,
        frozenset({"GH_REPO"}),
        _gh_has_target_flag,
    )


# ---- commit-landed detection ------------------------------------------------

def commit_landed(command: str, tool_response: dict | None) -> bool:
    """Use a recognizable direct commit plus the compound's zero exit status."""
    if not isinstance(tool_response, dict):
        return False
    tokens = tokenize(command)
    if tokens is None:
        return False
    segments, separators = _split_command(tokens)
    if any(op != "&&" for op in separators):
        return False
    commits = [
        segment
        for segment in segments
        if _is_git_commit_seg(segment) and "--dry-run" not in segment
    ]
    if not commits:
        return False
    return tool_response.get("exit_code") == 0
