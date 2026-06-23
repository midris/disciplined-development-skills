"""Tests for in-tree wiring files — no skip guard, always runs in this repo.

Parses both ``examples/settings.hooks.json`` (the consumer reference config)
and the repo's own ``.claude/settings.json`` (the self-wiring used while
developing the bundle) and asserts that neither has a ``UserPromptSubmit``
event key nor any hook command referencing ``inject_plan_state``.

Unlike ``test_settings_wiring.py`` (which walks up to a ``.claude`` ancestor
and skips in this standalone bundle repo), this test pins the two files by
path relative to the repo root — both are always present, so there is no skip
guard and this always provides a real red/green gate.

Task 2 of 2026-06-23-consolidate-plan-reminder.md.
"""

from __future__ import annotations

import json
from pathlib import Path

# Anchor to the repo root (four parents above this file:
# hooks/tests/ → hooks/ → disciplined-development/ → skills/ → repo root).
_REPO_ROOT = Path(__file__).resolve().parents[4]
_EXAMPLES_SETTINGS = _REPO_ROOT / "examples" / "settings.hooks.json"
_REPO_SETTINGS = _REPO_ROOT / ".claude" / "settings.json"


def _all_commands(settings_path: Path) -> list[str]:
    """Return every hook ``command`` string from a settings JSON file."""
    data = json.loads(settings_path.read_text())
    cmds: list[str] = []
    for groups in data.get("hooks", {}).values():
        for group in groups:
            for hook in group.get("hooks", []):
                cmd = hook.get("command", "")
                if cmd:
                    cmds.append(cmd)
    return cmds


def _event_keys(settings_path: Path) -> set[str]:
    """Return the top-level hook event names wired in a settings JSON file."""
    data = json.loads(settings_path.read_text())
    return set(data.get("hooks", {}).keys())


# --- examples/settings.hooks.json ---


def test_examples_no_user_prompt_submit():
    """examples/settings.hooks.json must not wire UserPromptSubmit."""
    assert "UserPromptSubmit" not in _event_keys(_EXAMPLES_SETTINGS), (
        f"UserPromptSubmit still present in {_EXAMPLES_SETTINGS}"
    )


def test_examples_no_inject_plan_state_command():
    """examples/settings.hooks.json must not reference inject_plan_state."""
    for cmd in _all_commands(_EXAMPLES_SETTINGS):
        assert "inject_plan_state" not in cmd, (
            f"inject_plan_state still referenced in {_EXAMPLES_SETTINGS}: {cmd!r}"
        )


# --- .claude/settings.json ---


def test_repo_settings_no_user_prompt_submit():
    """.claude/settings.json must not wire UserPromptSubmit."""
    assert "UserPromptSubmit" not in _event_keys(_REPO_SETTINGS), (
        f"UserPromptSubmit still present in {_REPO_SETTINGS}"
    )


def test_repo_settings_no_inject_plan_state_command():
    """.claude/settings.json must not reference inject_plan_state."""
    for cmd in _all_commands(_REPO_SETTINGS):
        assert "inject_plan_state" not in cmd, (
            f"inject_plan_state still referenced in {_REPO_SETTINGS}: {cmd!r}"
        )
