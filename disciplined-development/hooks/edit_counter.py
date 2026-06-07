#!/usr/bin/env python3
"""edit_counter.py — PostToolUse edit-counter + T0 nudge.

Fires on every Edit or Write tool call (the settings matcher pins this to
``Edit|Write``). Two responsibilities:

1. **Increment** the per-branch ``edits`` counter via ``lib/state.bump``.
   No-op counting — the payload content and diff are never inspected.
2. **Nudge** when the resulting stored count reaches
   ``review_tiers.fast.nudge_threshold`` (default 30). Emits a
   PostToolUse ``hookSpecificOutput.additionalContext`` envelope telling the
   model it has N unreviewed edits and to run ``/dd-review fast`` to review
   and reset. Advisory only — PostToolUse runs after the edit; this hook
   never blocks a tool call.

Repo/branch resolution:
- Reads ``cwd`` from the stdin payload; falls back to ``os.getcwd()``.
- Resolves the git top-level from cwd; if that fails, degrades silent
  (no bump, no nudge).
- Resolves the branch via ``symbolic-ref``; falls back to ``"detached"``
  (same convention as ``discipline_nudge``) so detached-HEAD checkouts
  still accumulate counts under a stable key.

Degrade-silent policy:
- Malformed or empty stdin → ``_payload_cwd()`` falls back to ``os.getcwd()``;
  the hook then resolves the repo and continues normally (bump + possible nudge).
  Truly silent only when the repo or branch can't be resolved (no git, bad cwd).
- Any git / state error → exit 0, no output, no crash.
- The hook must never raise an unhandled exception that blocks a tool call.

Env bypass: ``DD_SKIP_EDIT_COUNTER=1`` → silent no-op (no bump, no nudge).
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
from hooks.lib.envelope import Envelope  # noqa: E402

HOOK_NAME = "edit_counter"
COUNTER_NAME = "edits"
DEFAULT_NUDGE_THRESHOLD = 30


def _payload_cwd() -> str:
    """Return the cwd from the PostToolUse stdin payload, else the process cwd.

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


def _nudge_threshold() -> int:
    value = config.get("review_tiers.fast.nudge_threshold", DEFAULT_NUDGE_THRESHOLD)
    # Reject booleans (isinstance(True, int) is True) and non-positive values
    # so a config typo like `nudge_threshold: true` doesn't silently become 1.
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        return DEFAULT_NUDGE_THRESHOLD
    return value


def main() -> int:
    logger = logging_setup.setup(HOOK_NAME)

    if os.environ.get("DD_SKIP_EDIT_COUNTER") == "1":
        logger.emit("skip", reason="env_bypass")
        return 0

    cwd = _payload_cwd()

    rc_root, repo = _git(cwd, "rev-parse", "--show-toplevel")
    if rc_root != 0 or not repo:
        # Not a git repo or git unavailable — nothing to key state on.
        logger.emit("skip", reason="no_repo")
        return 0

    rc_branch, branch = _git(repo, "symbolic-ref", "--short", "HEAD")
    if rc_branch != 0 or not branch:
        # Detached HEAD — count under a stable key (matches discipline_nudge
        # convention; concurrent detached checkouts share this counter but the
        # single-dev, single-checkout posture makes that a non-issue).
        branch = "detached"

    count = state.bump(repo, branch, COUNTER_NAME)
    threshold = _nudge_threshold()

    if count < threshold:
        logger.emit("pass", count=count, threshold=threshold)
        return 0

    # count >= threshold: emit nudge. Repeated nudging from threshold upward
    # is intentional — discipline pressure until the model runs /dd-review fast
    # and the command resets the counter. The hard block at hard_block_threshold
    # (60) is H2's job (edit_block.py, PreToolUse).
    env = Envelope("PostToolUse")
    env.accumulate(
        f"Edit counter: you have {count} unreviewed edits on this branch. "
        f"Run `/dd-review fast` to review and reset the counter before "
        f"continuing."
    )
    env.emit()
    logger.emit("fire", count=count, threshold=threshold, branch=branch)
    return 0


if __name__ == "__main__":
    sys.exit(main())
