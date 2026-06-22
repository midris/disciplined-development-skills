#!/usr/bin/env python3
"""edit_block.py — PreToolUse T0 hard-block on Edit|Write.

Fires before every Edit or Write tool call (the settings matcher pins this to
``Edit|Write``). Single responsibility:

**Deny** the tool call when the stored ``edits`` counter is >=
``review_tiers.fast.hard_block_threshold`` (default 60). Because PostToolUse
increments and PreToolUse reads the previous value, a stored count of 60 means
this denies the 61st edit. Below 60 → allow (exit 0, no output).

The hook never increments the counter. Incrementing is ``edit_counter.py``'s
job (PostToolUse). This hook only reads.

Deny mechanism: write the block message to stderr and exit 2. Claude Code
blocks a PreToolUse tool ONLY on exit 2; any other non-zero is a
non-blocking error and the tool still runs. This is the same mechanism used
by ``pre_pr_review.py``.

Repo/branch resolution (same convention as ``edit_counter.py``):
- Reads ``cwd`` from the stdin payload; falls back to ``os.getcwd()``.
- Resolves the git top-level from cwd; if that fails, degrades silent.
- Resolves the branch via ``symbolic-ref``; falls back to ``"detached"``.

Degrade-silent policy:
- Malformed or empty stdin → ``_payload_cwd()`` falls back to ``os.getcwd()``;
  the hook then resolves the repo and reads the ``edits`` counter normally.
  If the counter is >= threshold the hook still denies (exit 2). The hook
  fails open (allows, exit 0) only when the counter cannot be read (no repo,
  git error, or unreadable state) or is below threshold.
- Any git / state error → exit 0, allow, no crash.
- The hook must never wrongly block a tool call when state can't be read.

Env bypass: ``DD_SKIP_EDIT_BLOCK=1`` → silent allow (exit 0, no deny).
Use this during the fix cycle after a block: run the remediation edits with
the bypass set, then run a deep review per the adversarial-review skill and
log it via ``dd-log`` to reset the counter and lift the block.
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

from hooks.lib import config, logging_setup, state  # noqa: E402

HOOK_NAME = "edit_block"
COUNTER_NAME = "edits"
DEFAULT_HARD_BLOCK_THRESHOLD = 60


def _payload_cwd() -> str:
    """Return the cwd from the PreToolUse stdin payload, else the process cwd.

    Degrade-safe: any stdin or parse failure falls back to os.getcwd() rather
    than propagating an exception that could crash the hook.
    """
    try:
        raw = sys.stdin.read()
    except Exception:
        return os.getcwd()
    if not raw:
        return os.getcwd()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return os.getcwd()
    if isinstance(data, dict) and isinstance(data.get("cwd"), str) and data["cwd"]:
        return data["cwd"]
    return os.getcwd()


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
        "review_tiers.fast.hard_block_threshold", DEFAULT_HARD_BLOCK_THRESHOLD
    )
    # Reject booleans (isinstance(True, int) is True) and non-positive values
    # so a config typo doesn't silently become 1.
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        return DEFAULT_HARD_BLOCK_THRESHOLD
    return value


def main() -> int:
    logger = logging_setup.setup(HOOK_NAME)

    if os.environ.get("DD_SKIP_EDIT_BLOCK") == "1":
        logger.emit("skip", reason="env_bypass")
        return 0

    cwd = _payload_cwd()

    rc_root, repo = _git(cwd, "rev-parse", "--show-toplevel")
    if rc_root != 0 or not repo:
        # Not a git repo or git unavailable — can't read state; allow.
        logger.emit("skip", reason="no_repo")
        return 0

    rc_branch, branch = _git(repo, "symbolic-ref", "--short", "HEAD")
    if rc_branch != 0 or not branch:
        # Detached HEAD — count under a stable key (matches edit_counter.py
        # and discipline_nudge conventions).
        branch = "detached"

    count = state.read(repo, branch, COUNTER_NAME)
    threshold = _hard_block_threshold()

    if count < threshold:
        logger.emit("pass", count=count, threshold=threshold)
        return 0

    # count >= threshold: deny. The stored count of `threshold` means the
    # next edit would be the (threshold + 1)th unreviewed edit — block it.
    logger.emit("block", count=count, threshold=threshold, branch=branch)
    print(
        f"[edit-block] BLOCKED: {count} unreviewed edits on this branch "
        f"(>= hard block ceiling {threshold}). "
        f"Run a deep review per the adversarial-review skill, then log it via "
        f"`dd-log` to reset the counter before continuing. "
        f"Set DD_SKIP_EDIT_BLOCK=1 in the launching shell for the remediation "
        f"edit cycle, then run the review to reset.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
