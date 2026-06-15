#!/usr/bin/env python3
"""review_nudge.py — PostToolUse post-commit nudge (Gate 3 verify + T1/T2 cadence).

Fires when a *landed* git commit is detected (``is_git_commit`` +
``commit_landed``) — the moment an edit becomes a real assertion. Emits up to
three accumulated segments on one envelope:

1. **Verification (every landed commit, Gate 3).** A fixed reminder to verify
   the change against the running system, or state why it's not exercisable.
   The hook never scans for or grades evidence — the smart model judges what
   verification fits; the hook only marks the commit. (Decision D1: kept
   unchanged; independent of cadence thresholds.)
2. **T1 nudge (commit edit floor).** Fires when the ``edits`` counter is
   >= ``review_tiers.regular.commit_edit_floor`` (default 30). Suggests
   ``/dd-review regular``.
3. **T2 nudge (cold-read escalation).** Fires when commits-since-last-cold-read
   reaches ``review_tiers.cold_read_escalation.nudge_threshold`` (default 3).
   Checkpoint-or-fork-base selection mirrors ``commit_block.py``:
   - Checkpoint exists → ``state.commits_since_checkpoint``.
   - No checkpoint (absent / stale) → ``state.commits_since_fork_base``.
   - No fork base / no trunk → cadence segment omitted (degrade silent).
   Suggests ``/dd-review cold-read``.

Both review nudges (T1/T2) carry ``GATE_AUDIENCE``: the gate is the
orchestrator's, so a dispatched subagent reports it and stops rather than acting.
The verify segment (1) does not — verifying its own work is the subagent's job.

Channel: PostToolUse exit-0 ``hookSpecificOutput.additionalContext`` (plain
stdout is debug-only for this event). Advisory only — every probe degrades to
silent on error and the hook never blocks the tool call. The verification
segment fires independent of repo/branch resolution (only T1/T2 need them).

Env bypass: ``DD_SKIP_REVIEW_NUDGE=1`` (silences all three segments).
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
DEFAULT_COMMIT_EDIT_FLOOR = 30
DEFAULT_COLD_READ_NUDGE_THRESHOLD = 3
DEFAULT_TRUNKS = ["master", "main"]

# Gate-3 verification reminder, emitted on every landed commit. Fixed and
# actionable; deliberately contains no "/dd-review" so it reads as "verify",
# not "review", and so tests can assert the cadence segments separately.
VERIFY_TEXT = (
    "Commit landed — Gate 3: verify this change against the running system "
    "before moving on. Run the relevant test / preview / live call, or state "
    "why it's not exercisable. Tests passing is necessary but not sufficient; "
    "don't just assert that it works."
)

# Audience framing appended to every T1/T2 review nudge (NOT the Gate-3 verify
# reminder — verifying its own work is the subagent's job). The hook stays dumb:
# it emits one static string for whoever is listening; the model decides which
# clause applies. A review/checkpoint gate is the orchestrator's, so a dispatched
# subagent reports the gate and stops rather than acting on the nudge.
GATE_AUDIENCE = (
    "This gate is the orchestrator's responsibility. If you are a subagent, "
    "report it's due and stop; don't act on this nudge. If you are the "
    "orchestrator, you should run"
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


def _commit_edit_floor() -> int:
    v = config.get("review_tiers.regular.commit_edit_floor", DEFAULT_COMMIT_EDIT_FLOOR)
    if isinstance(v, bool) or not isinstance(v, int) or v <= 0:
        return DEFAULT_COMMIT_EDIT_FLOOR
    return v


def _cold_read_nudge_threshold() -> int:
    v = config.get(
        "review_tiers.cold_read_escalation.nudge_threshold",
        DEFAULT_COLD_READ_NUDGE_THRESHOLD,
    )
    if isinstance(v, bool) or not isinstance(v, int) or v <= 0:
        return DEFAULT_COLD_READ_NUDGE_THRESHOLD
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
    # repo/branch resolution (only the cadence counts below need those), so a
    # detached HEAD or git hiccup still surfaces the reminder.
    env.accumulate(VERIFY_TEXT)

    # Segments 2 & 3 — T1 and T2 cadence, require repo + branch resolution.
    t1_fired = False
    t2_path = "none"
    t2_n: int | None = None

    cwd = cwd or os.getcwd()
    rc, repo = _git(cwd, "rev-parse", "--show-toplevel")
    if rc == 0 and repo:
        rc, branch = _git(repo, "symbolic-ref", "--short", "HEAD")
        if rc == 0 and branch:
            # Segment 2 — T1 nudge: fire when edit counter >= commit_edit_floor.
            edit_floor = _commit_edit_floor()
            edits = state.read(repo, branch, "edits")
            if edits >= edit_floor:
                env.accumulate(
                    f"Edit counter: {edits} unreviewed edits on this branch "
                    f"(>= T1 floor {edit_floor}). {GATE_AUDIENCE} "
                    f"`/dd-review regular` to review and reset the counter."
                )
                t1_fired = True

            # Segment 3 — T2 nudge: fire when commits-since-cold-read >= threshold.
            # Mirror commit_block.py: checkpoint exists → use it; absent/stale → fork base.
            t2_threshold = _cold_read_nudge_threshold()
            since_cp = state.commits_since_checkpoint(repo, branch)
            if since_cp is not None:
                if since_cp >= t2_threshold:
                    env.accumulate(
                        f"Review cadence: {since_cp} commits since the last "
                        f"cold-read on this branch (>= T2 nudge threshold "
                        f"{t2_threshold}). {GATE_AUDIENCE} `/dd-review cold-read` "
                        f"before continuing."
                    )
                    t2_path, t2_n = "checkpoint", since_cp
            else:
                # No usable checkpoint (absent OR stale/amended-away —
                # commits_since_checkpoint returns None for both): count from
                # fork-base, same threshold gate (don't nag a fresh branch on
                # every commit). Accepted: the two None-causes are intentionally
                # conflated — the message says "missing or invalidated" and the
                # action is identical either way.
                since_fb = state.commits_since_fork_base(repo, _trunks())
                if since_fb is not None and since_fb >= t2_threshold:
                    env.accumulate(
                        f"Review checkpoint missing or invalidated — "
                        f"{since_fb} commits since fork on this branch "
                        f"(>= T2 nudge threshold {t2_threshold}). {GATE_AUDIENCE} "
                        f"`/dd-review cold-read` before continuing."
                    )
                    t2_path, t2_n = "fork_base", since_fb

    env.emit()
    logger.emit(
        "fire",
        verification=True,
        t1=t1_fired,
        t2_cadence=t2_path,
        t2_n=t2_n,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
