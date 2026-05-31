"""Tests for hooks/compaction_reground.py — SessionStart + PreCompact reground.

Run as a subprocess so the stdin payload, env bypass, exit code, and the
per-event output channel are exercised end-to-end.

Resolved hook-event contracts (verified against the Claude Code hooks docs,
not assumed — plan D2 required this):

* SessionStart stdin carries ``source`` ∈ {startup, resume, clear, compact};
  exit-0 ``additionalContext`` reaches the model. We fire on resume/compact
  (context was lost or summarized) and stay silent on startup/clear (project
  context is freshly present — the "now a summary" reminder would be wrong).
* PreCompact is a system event whose non-blocking output does NOT reach the
  model; the post-compaction model reground is delivered by the
  SessionStart(source=compact) path. PreCompact therefore emits its reminder
  on plain stdout only (transcript/debug record), never a model envelope.
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


def test_precompact_emits_plain_stdout_not_envelope():
    r = _run({"hook_event_name": "PreCompact", "trigger": "auto"})
    assert r.returncode == 0
    # Plain text (PreCompact has no model-visible additionalContext channel),
    # not a JSON envelope.
    assert compaction_reground.REGROUND_TEXT in r.stdout
    assert not r.stdout.lstrip().startswith("{")


def test_bypass_env_silent():
    r = _run({"hook_event_name": "SessionStart", "source": "compact"}, bypass=True)
    assert r.returncode == 0
    assert r.stdout.strip() == ""


def test_missing_event_name_degrades_silent():
    r = _run({"some": "payload"})
    assert r.returncode == 0
    assert r.stdout.strip() == ""
