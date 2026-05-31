#!/usr/bin/env python3
"""review_nudge.py — PostToolUse post-commit nudge (Gate 3 verify + cadence).

Fires when a *landed* git commit is detected (``is_git_commit`` +
``commit_landed``) — the moment an edit becomes a real assertion. Emits up to
two accumulated segments on one envelope:

1. **Verification (every landed commit, Gate 3).** A fixed reminder to verify
   the change against the running system, or state why it's not exercisable.
   The hook never scans for or grades evidence — the smart model judges what
   verification fits; the hook only marks the commit. (Replaces the dropped
   Stop evidence-scanner; see the spec §Kick.)
2. **Review cadence (on threshold, P8).** Commits since the last review:
   - **Checkpoint exists** (a prior clean review wrote one): nudge when commits
     since the checkpoint reach ``counters.review_threshold``.
   - **No checkpoint yet**: count commits since fork-base, nudge at the same
     threshold — NOT every commit, so a fresh branch isn't nagged early. No
     fork-base (no trunk ref) → cadence segment omitted.

Channel: PostToolUse exit-0 ``hookSpecificOutput.additionalContext`` (plain
stdout is debug-only for this event). Advisory only — every probe degrades to
silent on error and the hook never blocks the tool call. The verification
segment fires independent of repo/branch resolution (only the cadence count
needs them).

Env bypass: ``DD_SKIP_REVIEW_NUDGE=1`` (silences both segments).
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
from hooks.lib.envelope import Envelope  # noqa: E402

HOOK_NAME = "review_nudge"
DEFAULT_THRESHOLD = 5
DEFAULT_TRUNKS = ["master", "main"]

# Gate-3 verification reminder, emitted on every landed commit. Fixed and
# actionable; deliberately contains no "/dd-review" so it reads as "verify",
# not "review", and so tests can assert the cadence segment separately.
VERIFY_TEXT = (
    "Commit landed — Gate 3: verify this change against the running system "
    "before moving on. Run the relevant test / preview / live call, or state "
    "why it's not exercisable. Tests passing is necessary but not sufficient; "
    "don't just assert that it works."
)


def _read_payload() -> tuple[str, dict, str | None]:
    """Return (command, tool_response, cwd) from the PostToolUse stdin payload."""
    try:
        d = json.loads(sys.stdin.read())
    except Exception:
        return "", {}, None
    if not isinstance(d, dict):
        return "", {}, None
    ti = d.get("tool_input") if isinstance(d.get("tool_input"), dict) else {}
    tr = d.get("tool_response") if isinstance(d.get("tool_response"), dict) else {}
    cwd = d.get("cwd") if isinstance(d.get("cwd"), str) and d.get("cwd") else None
    return (ti.get("command") or ""), tr, cwd


def _git(cwd: str, *args: str) -> tuple[int, str]:
    try:
        r = subprocess.run(
            ["git", "-C", cwd, *args], capture_output=True, text=True, timeout=5
        )
    except Exception:
        return 1, ""
    return r.returncode, r.stdout.strip()


def _threshold() -> int:
    v = config.get("counters.review_threshold", DEFAULT_THRESHOLD)
    if isinstance(v, bool) or not isinstance(v, int) or v <= 0:
        return DEFAULT_THRESHOLD
    return v


def _trunks() -> list[str]:
    v = config.get("branch_convention.trunk_branches", DEFAULT_TRUNKS)
    if isinstance(v, list) and v and all(isinstance(x, str) for x in v):
        return v
    return DEFAULT_TRUNKS


def main() -> int:
    logger = logging_setup.setup(HOOK_NAME)

    if os.environ.get("DD_SKIP_REVIEW_NUDGE") == "1":
        logger.emit("skip", reason="env_bypass")
        return 0

    command, tool_response, cwd = _read_payload()
    if not command_match.is_git_commit(command):
        return 0
    if not command_match.commit_landed(command, tool_response):
        logger.emit("skip", reason="commit_not_landed")
        return 0

    env = Envelope("PostToolUse")
    # Segment 1 — Gate 3 verification, on every landed commit. Independent of
    # repo/branch resolution (only the cadence count below needs those), so a
    # detached HEAD or git hiccup still surfaces the reminder.
    env.accumulate(VERIFY_TEXT)

    # Segment 2 — review cadence, only at threshold.
    cadence_path = "none"
    cadence_n: int | None = None
    cwd = cwd or os.getcwd()
    rc, repo = _git(cwd, "rev-parse", "--show-toplevel")
    if rc == 0 and repo:
        rc, branch = _git(repo, "symbolic-ref", "--short", "HEAD")
        if rc == 0 and branch:
            threshold = _threshold()
            since_cp = state.commits_since_checkpoint(repo, branch)
            if since_cp is not None:
                if since_cp >= threshold:
                    env.accumulate(
                        f"Review cadence: {since_cp} commits since the last "
                        f"clean review on this branch. Run `/dd-review "
                        f"regular` before continuing."
                    )
                    cadence_path, cadence_n = "checkpoint", since_cp
            else:
                # No usable checkpoint (absent OR stale/amended-away —
                # commits_since_checkpoint returns None for both): count from
                # fork-base, same threshold gate (don't nag a fresh branch on
                # every commit). Accepted (review P3): the two None-causes are
                # intentionally conflated — the message says "missing or
                # invalidated" and the action is identical either way; a
                # checkpoint-state enum would be cosmetic API surface.
                since_fb = state.commits_since_fork_base(repo, _trunks())
                if since_fb is not None and since_fb >= threshold:
                    env.accumulate(
                        f"Review checkpoint missing or invalidated — "
                        f"{since_fb} commits since fork on this branch. Run "
                        f"`/dd-review regular` before continuing."
                    )
                    cadence_path, cadence_n = "fork_base", since_fb

    env.emit()
    logger.emit("fire", verification=True, cadence=cadence_path, n=cadence_n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
