#!/usr/bin/env python3
"""commit_block.py — PreToolUse T2 hard-block on git commit.

Fires before every Bash tool call (the settings matcher pins this to ``Bash``).
Single responsibility:

**Deny** when the command is a ``git commit`` (including ``--amend``) AND
the commits-since-last-cold-read count is >=
``review_tiers.cold_read_escalation.hard_block_threshold`` (default 5).

That means 5 commits are allowed between cold-reads; the 6th is denied (the
count is the landed/stored value read before this commit lands, so stored == 5
denies the 6th commit).

``git commit --amend`` passes ``command_match.is_git_commit``, so amend is
gated the same way as a new commit. This is intentional: amend is a coarse
"you owe a cold-read" gate (see spec §Out of scope — "amend is denied too
while over threshold").

Commits-since-last-cold-read selection (mirrors ``review_nudge.py`` exactly):
1. ``review.checkpoint`` exists → ``state.commits_since_checkpoint``.
2. No checkpoint (absent, stale, or amended-away) → fall back to
   ``state.commits_since_fork_base``.
3. No trunk / can't resolve → degrade silent (allow).

Deny mechanism: write the block message to stderr and exit 2. Claude Code
blocks a PreToolUse tool ONLY on exit 2; any other non-zero is a non-blocking
error and the tool still runs. Same mechanism as ``pre_pr_review.py`` and
``edit_block.py``.

Degrade-silent policy:
- Malformed or empty stdin → exit 0, allow, no crash.
- Any git / state error → exit 0, allow, no crash.
- The hook must never wrongly block a commit when state can't be computed.

Env bypass: ``DD_SKIP_COMMIT_BLOCK=1`` → silent allow (exit 0, no deny).
Use this during the fix cycle after a block: run remediation commits with the
bypass set, then run ``/dd-review cold-read`` to a clean pass to reset the
checkpoint and lift the block.
"""

from __future__ import annotations

import json
import os
import pathlib
import subprocess
import sys

_HERE = pathlib.Path(__file__).resolve().parent
_BASE_DIR = _HERE.parent  # the dir containing the `hooks` package
if str(_BASE_DIR) not in sys.path:
    sys.path.insert(0, str(_BASE_DIR))

from hooks.lib import command_match, config, logging_setup, state  # noqa: E402

HOOK_NAME = "commit_block"
DEFAULT_HARD_BLOCK_THRESHOLD = 5
DEFAULT_TRUNKS = ["master", "main"]


def _read_command() -> str:
    """Return the Bash command string from the PreToolUse stdin payload.

    Degrade-safe: any stdin or parse failure returns '' rather than raising.
    """
    try:
        raw = sys.stdin.read()
    except Exception:
        return ""
    if not raw:
        return ""
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return ""
    if not isinstance(data, dict):
        return ""
    ti = data.get("tool_input")
    if isinstance(ti, dict) and isinstance(ti.get("command"), str):
        return ti["command"]
    return ""


def _git(cwd: str, *args: str) -> tuple[int, str]:
    try:
        r = subprocess.run(
            ["git", "-C", cwd, *args], capture_output=True, text=True, timeout=5
        )
    except Exception:
        return 1, ""
    return r.returncode, r.stdout.strip()


def _hard_block_threshold() -> int:
    value = config.get(
        "review_tiers.cold_read_escalation.hard_block_threshold",
        DEFAULT_HARD_BLOCK_THRESHOLD,
    )
    # Reject booleans (isinstance(True, int) is True) and non-positive values
    # so a config typo doesn't silently become 1.
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        return DEFAULT_HARD_BLOCK_THRESHOLD
    return value


def _trunks() -> list[str]:
    v = config.get("branch_convention.trunk_branches", DEFAULT_TRUNKS)
    if isinstance(v, list) and v and all(isinstance(x, str) for x in v):
        return v
    return DEFAULT_TRUNKS


def main() -> int:
    logger = logging_setup.setup(HOOK_NAME)

    if os.environ.get("DD_SKIP_COMMIT_BLOCK") == "1":
        logger.emit("skip", reason="env_bypass")
        return 0

    command = _read_command()
    if not command_match.is_git_commit(command):
        # Not a git commit — let every other Bash command through.
        return 0

    # Resolve the repo root from the process cwd (the hook receives cwd in the
    # payload, but we consumed stdin already; use os.getcwd() which the test
    # harness sets via cwd= on subprocess.run, matching the real hook invocation).
    cwd = os.getcwd()
    rc_root, repo = _git(cwd, "rev-parse", "--show-toplevel")
    if rc_root != 0 or not repo:
        # Not a git repo or git unavailable — can't compute count; allow.
        logger.emit("skip", reason="no_repo")
        return 0

    rc_branch, branch = _git(repo, "symbolic-ref", "--short", "HEAD")
    if rc_branch != 0 or not branch:
        branch = "detached"

    threshold = _hard_block_threshold()

    # Mirror review_nudge.py: checkpoint exists → use it; absent/stale → fork base.
    since_cp = state.commits_since_checkpoint(repo, branch)
    if since_cp is not None:
        count = since_cp
        path = "checkpoint"
    else:
        since_fb = state.commits_since_fork_base(repo, _trunks())
        if since_fb is None:
            # No trunk / can't resolve — degrade silent, allow.
            logger.emit("skip", reason="no_fork_base")
            return 0
        count = since_fb
        path = "fork_base"

    if count < threshold:
        logger.emit("pass", count=count, threshold=threshold, path=path)
        return 0

    # count >= threshold: deny. The stored count of `threshold` means `threshold`
    # commits have landed since the last cold-read; this (the next) commit is the
    # (threshold + 1)th — block it.
    logger.emit("block", count=count, threshold=threshold, path=path, branch=branch)
    print(
        f"[commit-block] BLOCKED: {count} commits since the last cold-read on "
        f"this branch (>= hard block ceiling {threshold}). "
        f"Run `/dd-review cold-read` to a clean pass to reset the checkpoint "
        f"before continuing. "
        f"Set DD_SKIP_COMMIT_BLOCK=1 in the launching shell for the remediation "
        f"commit cycle, then run the review to reset.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
