#!/usr/bin/env python3
"""commit_block.py — PreToolUse T2 hard-block on git commit.

Fires before every Bash tool call (the settings matcher pins this to ``Bash``).
Single responsibility: block an unresolved recognizable direct commit, and for
a resolved standalone ``git commit`` (including ``--amend``), **deny** when the
commits-since-review-checkpoint count is >=
``review_tiers.cold_read_escalation.hard_block_threshold`` (default 5).

That means 5 commits are allowed after the last state-resetting PASS; the 6th is
denied (the count is the landed/stored value read before this commit lands, so
stored == 5 denies the 6th commit).

``git commit --amend`` passes ``command_match.is_git_commit``, so amend is
gated the same way as a new commit. This is intentional: the checkpoint is a
coarse review-cadence gate, and amend does not waive it.

Commits-since-checkpoint selection (mirrors ``review_nudge.py`` exactly):
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
- An unresolved matching commit target → exit 2 with rewrite/bypass guidance.
- A resolved repo whose cadence count cannot be computed → exit 0, allow.
- The hook must never wrongly block a commit when state can't be computed.

Env bypass: ``DD_SKIP_COMMIT_BLOCK=1`` → silent allow (exit 0, no deny).
Use this during the fix cycle after a block: run remediation commits with the
bypass set. Run the deep-review loop and log every round with ``dd-log``. Only
a PASS resets the checkpoint.
"""

from __future__ import annotations

import json
import os
import pathlib
import sys

_HERE = pathlib.Path(__file__).resolve().parent
_BASE_DIR = _HERE.parent  # the dir containing the `hooks` package
if str(_BASE_DIR) not in sys.path:
    sys.path.insert(0, str(_BASE_DIR))

from hooks.lib import command_match, config, logging_setup, state  # noqa: E402

HOOK_NAME = "commit_block"
DEFAULT_HARD_BLOCK_THRESHOLD = 5
DEFAULT_TRUNKS = ["master", "main"]


def _read_payload() -> tuple[str, str | None]:
    """Return the Bash command string from the PreToolUse stdin payload.

    Degrade-safe: any stdin or parse failure returns '' rather than raising.
    """
    try:
        raw = sys.stdin.read()
    except Exception:
        return "", None
    if not raw:
        return "", None
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return "", None
    if not isinstance(data, dict):
        return "", None
    ti = data.get("tool_input")
    command = ti.get("command") if isinstance(ti, dict) else None
    cwd = data.get("cwd")
    return (
        command if isinstance(command, str) else "",
        cwd if isinstance(cwd, str) and cwd else None,
    )


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

    command, base_cwd = _read_payload()
    if not command_match.is_git_commit(command):
        # Not a git commit — let every other Bash command through.
        return 0

    command_cwd = command_match.find_git_commit(command, base_cwd)
    repo = state.repo_root(command_cwd) if command_cwd is not None else None
    if repo is None:
        logger.emit("block", reason="unresolved_target")
        print(
            "[commit-block] BLOCKED: unresolved `git commit`. Run the commit "
            "as a standalone Bash call from the target repository; run other "
            "commands separately. Set DD_SKIP_COMMIT_BLOCK=1 in "
            "the launching shell to bypass.",
            file=sys.stderr,
        )
        return 2

    branch = state.current_branch(repo)

    threshold = _hard_block_threshold()

    # Mirror review_nudge.py: checkpoint exists → use it; absent/stale → fork base.
    count, path = state.review_distance(repo, branch, _trunks())
    if count is None or path is None:
        logger.emit("skip", reason="no_fork_base")
        return 0

    if count < threshold:
        logger.emit("pass", count=count, threshold=threshold, path=path)
        return 0

    # count >= threshold: deny. The stored count of `threshold` means `threshold`
    # commits have landed since the review checkpoint; this (the next) commit is the
    # (threshold + 1)th — block it.
    logger.emit("block", count=count, threshold=threshold, path=path, branch=branch)
    basis = "the review checkpoint" if path == "checkpoint" else "fork base"
    print(
        f"[commit-block] BLOCKED: {count} commits since {basis} on "
        f"this branch (>= hard block ceiling {threshold}). "
        f"Run the deep-review loop and log every round with `dd-log`. "
        f"Only a PASS resets the checkpoint. Set DD_SKIP_COMMIT_BLOCK=1 in "
        f"the launching shell for the remediation commit cycle.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
