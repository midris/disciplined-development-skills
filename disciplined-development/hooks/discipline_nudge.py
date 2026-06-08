#!/usr/bin/env python3
"""discipline_nudge.py — PreToolUse re-ground nudge.

On every PreToolUse, bump the per-branch ``discipline`` tool-call counter.
When it reaches ``counters.discipline_threshold``, emit a fixed,
actionable re-ground nudge (re-read CLAUDE.md + the active plan; re-check
the governing skills) and reset the counter. Otherwise silent (exit 0).

The counter resets on fire AND at the start of each user turn — the
UserPromptSubmit injector (``inject_plan_state``) resets ``discipline`` so the
cadence is "tool calls since the last re-ground (turn boundary or prior fire)."

**Channel.** PreToolUse exit-0 ``hookSpecificOutput.additionalContext`` is
model-visible — it appears next to the tool result and the model sees it
on the next request (per the Claude Code hooks docs). Plain stdout is
debug-only for this event, so the JSON envelope is required.

**Fixed message, not per-tool.** The nudge text never varies by tool;
varying it by inspecting tool output would rebuild a rejected
output-scanner subsystem.

**Subagent/nested counting.** The counter is per-branch shared state, so a
subagent's PreToolUse calls and long autonomous stretches keep
incrementing it and the nudge can fire inside subagent context.
Reset-on-fire bounds frequency to once per threshold; no session/subagent
detection is added — not worth the complexity for the single-dev posture.
Resolved-accepted in the spec (§O6 / plan O6) with the same revisit
criterion: revisit only if subagent firing proves noisy in practice.

Env bypass: ``DD_SKIP_DISCIPLINE_NUDGE=1`` → silent no-op (no bump).
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

HOOK_NAME = "discipline_nudge"
COUNTER_NAME = "discipline"
DEFAULT_THRESHOLD = 50

REGROUND_TEXT = (
    "Discipline check-in — you've accumulated several tool calls without "
    "re-grounding. Before the next one:\n"
    "  - Re-read CLAUDE.md and the active plan from disk — don't trust "
    "recall.\n"
    "  - Re-check the governing skills for the work in flight "
    "(disciplined-development + the companion skills its gates name).\n"
    "  - Confirm the current step still matches the plan; if scope moved, "
    "write it down before continuing.\n"
    "  - Flip any completed checkboxes in the active plan before continuing."
)


def _payload_cwd() -> str:
    """Return the cwd from the PreToolUse stdin payload, else the process cwd."""
    try:
        raw = sys.stdin.read()
    except Exception:
        # Advisory hook: any stdin failure (closed/None/non-tty quirk)
        # degrades to the process cwd rather than crashing the tool call.
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
        # timeout matches the sibling plan._git_toplevel: this hook runs on
        # every PreToolUse, so a stuck git (index.lock from a crashed git,
        # misbehaving fsmonitor, slow NFS) must not block the tool call.
        r = subprocess.run(
            ["git", "-C", cwd, *args], capture_output=True, text=True, timeout=5
        )
    except Exception:
        # Degrade-safe helper: any subprocess failure (incl. timeout) reads
        # as "git said no."
        return 1, ""
    return r.returncode, r.stdout.strip()


def _threshold() -> int:
    value = config.get("counters.discipline_threshold", DEFAULT_THRESHOLD)
    # `isinstance(True, int)` is True — exclude bool so a config typo like
    # `discipline_threshold: true` doesn't silently become a threshold of 1.
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        return DEFAULT_THRESHOLD
    return value


def main() -> int:
    logger = logging_setup.setup(HOOK_NAME)

    if os.environ.get("DD_SKIP_DISCIPLINE_NUDGE") == "1":
        logger.emit("skip", reason="env_bypass")
        return 0

    cwd = _payload_cwd()

    rc_root, repo = _git(cwd, "rev-parse", "--show-toplevel")
    if rc_root != 0 or not repo:
        # Not a git repo (or git unavailable) — nothing to key state on.
        logger.emit("skip", reason="no_repo")
        return 0

    rc_branch, branch = _git(repo, "symbolic-ref", "--short", "HEAD")
    if rc_branch != 0 or not branch:
        # Detached HEAD / resolution failure: count under one stable key.
        # Accepted: concurrent detached checkouts would share this counter —
        # a non-issue for the single-dev, single-checkout posture (CLAUDE.md),
        # and the counter is advisory. Per-sha keying isn't worth it (it would
        # also reset the count on every commit).
        branch = "detached"

    count = state.bump(repo, branch, COUNTER_NAME)
    threshold = _threshold()

    if count < threshold:
        logger.emit("pass", count=count, threshold=threshold)
        return 0

    env = Envelope("PreToolUse")
    env.accumulate(REGROUND_TEXT)
    env.emit()
    state.reset(repo, branch, COUNTER_NAME)
    logger.emit("fire", count=count, threshold=threshold, branch=branch)
    return 0


if __name__ == "__main__":
    sys.exit(main())
