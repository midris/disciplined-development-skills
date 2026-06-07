"""Tests for hooks/compaction_reground.py — SessionStart reground.

Run as a subprocess so the stdin payload, env bypass, exit code, and the
output channel are exercised end-to-end.

The hook fires only on SessionStart. Its stdin carries ``source`` ∈
{startup, resume, clear, compact}; exit-0 ``additionalContext`` reaches the
model. We fire on resume/compact (context was lost or summarized) and stay
silent on startup/clear (project context is freshly present — the "now a
summary" reminder would be wrong). PreCompact is no longer wired: its output
cannot reach the post-compaction model, so SessionStart(source=compact)
delivers the reground; a stale PreCompact wiring must degrade to a safe no-op.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from hooks import compaction_reground

HOOK = Path(__file__).resolve().parent.parent / "compaction_reground.py"


def _run(payload: dict, *, bypass: bool = False) -> subprocess.CompletedProcess:
    env = dict(os.environ)
    if bypass:
        env["DD_SKIP_COMPACTION_REGROUND"] = "1"
    else:
        env.pop("DD_SKIP_COMPACTION_REGROUND", None)
    return subprocess.run(
        [sys.executable, str(HOOK)], input=json.dumps(payload),
        capture_output=True, text=True, env=env,
    )


def test_session_start_resume_emits_envelope():
    r = _run({"hook_event_name": "SessionStart", "source": "resume"})
    assert r.returncode == 0
    payload = json.loads(r.stdout)
    hso = payload["hookSpecificOutput"]
    assert hso["hookEventName"] == "SessionStart"
    assert hso["additionalContext"] == compaction_reground.REGROUND_TEXT


def test_session_start_compact_emits_envelope():
    r = _run({"hook_event_name": "SessionStart", "source": "compact"})
    assert r.returncode == 0
    payload = json.loads(r.stdout)
    hso = payload["hookSpecificOutput"]
    assert hso["hookEventName"] == "SessionStart"
    assert hso["additionalContext"] == compaction_reground.REGROUND_TEXT


def test_session_start_startup_silent():
    r = _run({"hook_event_name": "SessionStart", "source": "startup"})
    assert r.returncode == 0
    assert r.stdout.strip() == ""


def test_session_start_clear_silent():
    # /clear leaves project context freshly present (like startup); the
    # "context is now a summary" reminder would be inaccurate → silent.
    r = _run({"hook_event_name": "SessionStart", "source": "clear"})
    assert r.returncode == 0
    assert r.stdout.strip() == ""


def test_precompact_event_is_silent_noop():
    # PreCompact is no longer wired (its output can't reach the post-compaction
    # model). A stale PreCompact wiring in an un-migrated consumer must degrade
    # to a safe no-op — exit 0, no output — not error and not emit.
    r = _run({"hook_event_name": "PreCompact", "trigger": "auto"})
    assert r.returncode == 0
    assert r.stdout.strip() == ""


def test_bypass_env_silent():
    r = _run({"hook_event_name": "SessionStart", "source": "compact"}, bypass=True)
    assert r.returncode == 0
    assert r.stdout.strip() == ""


def test_missing_event_name_degrades_silent():
    r = _run({"some": "payload"})
    assert r.returncode == 0
    assert r.stdout.strip() == ""
