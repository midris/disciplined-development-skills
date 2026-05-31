"""Tests for the Envelope additionalContext emitter.

Pins the one non-verbatim A1 change: ``event_name`` stamps the emitted
``hookSpecificOutput.hookEventName`` so each hook event surfaces under its
own name, while the default stays ``"PostToolUse"`` for existing callers.
"""

from __future__ import annotations

import io
import json

from hooks.lib.envelope import Envelope


def _emit_payload(env: Envelope) -> dict:
    buf = io.StringIO()
    env.emit(buf)
    return json.loads(buf.getvalue())


def test_event_name_first_positional_stamps_hook_event_name():
    env = Envelope("PreToolUse")
    env.accumulate("re-ground before continuing")
    payload = _emit_payload(env)
    assert payload["hookSpecificOutput"]["hookEventName"] == "PreToolUse"


def test_default_construction_emits_post_tool_use():
    env = Envelope()
    env.accumulate("cadence nudge")
    payload = _emit_payload(env)
    assert payload["hookSpecificOutput"]["hookEventName"] == "PostToolUse"


def test_additional_context_carries_accumulated_text():
    env = Envelope("SessionStart")
    env.accumulate("first segment")
    env.accumulate("second segment")
    payload = _emit_payload(env)
    ctx = payload["hookSpecificOutput"]["additionalContext"]
    assert "first segment" in ctx
    assert "second segment" in ctx
    # Segments join with the bare ----- separator on its own line.
    assert "\n-----\n" in ctx


def test_empty_envelope_emits_nothing():
    env = Envelope("PreToolUse")
    buf = io.StringIO()
    env.emit(buf)
    assert buf.getvalue() == ""


def test_whitespace_only_segments_dropped():
    env = Envelope()
    env.accumulate("   ")
    env.accumulate("")
    buf = io.StringIO()
    env.emit(buf)
    assert buf.getvalue() == ""
