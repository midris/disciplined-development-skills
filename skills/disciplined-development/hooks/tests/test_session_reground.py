"""Tests for hooks/session_reground.py — all-sources SessionStart reground.

Run as a subprocess so the stdin payload, env bypass, exit code, and the
output channel are exercised end-to-end.

The hook fires on EVERY SessionStart source, emitting PREAMBLES[source] +
COMMON_BODY. Unknown/missing source falls back to a generic preamble and still
fires. PreCompact is not wired; a stale PreCompact wiring must degrade to a
safe no-op.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from hooks import session_reground

HOOK = Path(__file__).resolve().parent.parent / "session_reground.py"


def _run(payload: dict, *, bypass: bool = False) -> subprocess.CompletedProcess:
    env = dict(os.environ)
    if bypass:
        env["DD_SKIP_SESSION_REGROUND"] = "1"
    else:
        env.pop("DD_SKIP_SESSION_REGROUND", None)
    return subprocess.run(
        [sys.executable, str(HOOK)], input=json.dumps(payload),
        capture_output=True, text=True, env=env,
    )


def _context(r: subprocess.CompletedProcess) -> str:
    """Extract additionalContext from a fired-envelope result."""
    payload = json.loads(r.stdout)
    return payload["hookSpecificOutput"]["additionalContext"]


# --- startup fires (was previously silent) ---

def test_session_start_startup_emits_envelope():
    r = _run({"hook_event_name": "SessionStart", "source": "startup"})
    assert r.returncode == 0
    ctx = _context(r)
    assert ctx == session_reground.PREAMBLES["startup"] + session_reground.COMMON_BODY


def test_session_start_startup_contains_common_body_markers():
    r = _run({"hook_event_name": "SessionStart", "source": "startup"})
    ctx = _context(r)
    assert "disciplined-development" in ctx
    assert "concise-writing" in ctx


# --- clear fires (was previously silent) ---

def test_session_start_clear_emits_envelope():
    r = _run({"hook_event_name": "SessionStart", "source": "clear"})
    assert r.returncode == 0
    ctx = _context(r)
    assert ctx == session_reground.PREAMBLES["clear"] + session_reground.COMMON_BODY


def test_session_start_clear_contains_common_body_markers():
    r = _run({"hook_event_name": "SessionStart", "source": "clear"})
    ctx = _context(r)
    assert "disciplined-development" in ctx
    assert "concise-writing" in ctx


# --- resume fires (existing) ---

def test_session_start_resume_emits_envelope():
    r = _run({"hook_event_name": "SessionStart", "source": "resume"})
    assert r.returncode == 0
    ctx = _context(r)
    assert ctx == session_reground.PREAMBLES["resume"] + session_reground.COMMON_BODY


def test_session_start_resume_contains_common_body_markers():
    r = _run({"hook_event_name": "SessionStart", "source": "resume"})
    ctx = _context(r)
    assert "disciplined-development" in ctx
    assert "concise-writing" in ctx


# --- compact fires (existing) ---

def test_session_start_compact_emits_envelope():
    r = _run({"hook_event_name": "SessionStart", "source": "compact"})
    assert r.returncode == 0
    ctx = _context(r)
    assert ctx == session_reground.PREAMBLES["compact"] + session_reground.COMMON_BODY


def test_session_start_compact_contains_common_body_markers():
    r = _run({"hook_event_name": "SessionStart", "source": "compact"})
    ctx = _context(r)
    assert "disciplined-development" in ctx
    assert "concise-writing" in ctx


# --- unknown source falls back (fires, doesn't crash) ---

def test_session_start_unknown_source_fires_with_fallback_preamble():
    r = _run({"hook_event_name": "SessionStart", "source": "something_new"})
    assert r.returncode == 0
    ctx = _context(r)
    # Falls back to generic preamble + common body
    assert session_reground.COMMON_BODY in ctx
    assert "disciplined-development" in ctx


# --- constants shape: PREAMBLES is a dict, COMMON_BODY is a string ---

def test_preambles_covers_all_known_sources():
    for source in ("startup", "resume", "clear", "compact"):
        assert source in session_reground.PREAMBLES, f"PREAMBLES missing key: {source}"


def test_common_body_mentions_governing_docs():
    body = session_reground.COMMON_BODY
    assert "CLAUDE.md" in body
    assert "disciplined-development" in body
    assert "concise-writing" in body


def test_common_body_reloads_dd_and_superpowers():
    # Long-session failure mode: the model lost BOTH dd and superpowers. The
    # reground must name both explicitly so they're re-loaded after a
    # compact/resume.
    body = session_reground.COMMON_BODY
    assert "disciplined-development" in body
    assert "superpowers" in body


# --- bypass ---

def test_bypass_env_silent():
    r = _run({"hook_event_name": "SessionStart", "source": "compact"}, bypass=True)
    assert r.returncode == 0
    assert r.stdout.strip() == ""


# --- bad/empty payload ---

def test_missing_event_name_degrades_silent():
    r = _run({"some": "payload"})
    assert r.returncode == 0
    assert r.stdout.strip() == ""


def test_empty_payload_degrades_silent():
    result = subprocess.run(
        [sys.executable, str(HOOK)], input="",
        capture_output=True, text=True,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == ""


def test_malformed_json_degrades_silent():
    result = subprocess.run(
        [sys.executable, str(HOOK)], input="not json {{{",
        capture_output=True, text=True,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == ""


# --- non-SessionStart event is a silent no-op ---

def test_precompact_event_is_silent_noop():
    # PreCompact is not wired. A stale PreCompact wiring in an un-migrated
    # consumer must degrade to a safe no-op — exit 0, no output.
    r = _run({"hook_event_name": "PreCompact", "trigger": "auto"})
    assert r.returncode == 0
    assert r.stdout.strip() == ""
