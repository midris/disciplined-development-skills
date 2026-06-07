"""Tests for .claude/settings.json hook wiring (Task F2).

Pins the cutover: every hook command resolves to an existing file under the
new ``hooks/`` tree, none reference the deleted ``hooks_py/``, and the
expected hook set is wired. Reads the live ``settings.json`` (resolved by
walking up to ``.claude``), so a drift between settings and the shipped hook
files fails here.
"""

from __future__ import annotations

import json
import re

from pathlib import Path

import pytest

_CLAUDE = next((p for p in Path(__file__).resolve().parents if p.name == ".claude"), None)
_SETTINGS = (_CLAUDE / "settings.json") if _CLAUDE else None
_HOOKS_DIR = (_CLAUDE / "skills" / "disciplined-development" / "hooks") if _CLAUDE else None

# Consumer-side integration check: reads the consuming project's live
# .claude/settings.json. It cannot run in the standalone bundle repo, nor when
# the hooks are reached via symlink (resolved __file__ lands in the clone, which
# has no .claude ancestor). Skip cleanly in those layouts; it still runs in an
# in-tree consumer where the hooks live under .claude/.
pytestmark = pytest.mark.skipif(
    _SETTINGS is None or not _SETTINGS.exists(),
    reason="no consumer .claude/settings.json reachable — settings-wiring is a consumer-side check",
)


def _hook_commands() -> list[str]:
    data = json.loads(_SETTINGS.read_text())
    cmds: list[str] = []
    for groups in data.get("hooks", {}).values():
        for group in groups:
            for hook in group.get("hooks", []):
                cmds.append(hook.get("command", ""))
    return cmds


def test_all_hook_commands_resolve_under_hooks_dir():
    cmds = _hook_commands()
    assert cmds, "no hook commands wired in settings.json"
    for cmd in cmds:
        assert "hooks_py" not in cmd, f"legacy hooks_py reference: {cmd}"
        m = re.search(r"/hooks/([a-z_]+\.py)", cmd)
        assert m, f"no hooks/<file>.py path in: {cmd}"
        assert (_HOOKS_DIR / m.group(1)).is_file(), f"missing hook file: {m.group(1)}"


def test_settings_references_no_hooks_py():
    assert "hooks_py" not in _SETTINGS.read_text()


def test_expected_hook_set_wired():
    # Skip guard fires outside a consumer (see module-level pytestmark).
    joined = " ".join(_hook_commands())
    for expected in (
        "inject_plan_state.py",
        "discipline_nudge.py",
        "pre_pr_review.py",
        "review_nudge.py",
        "compaction_reground.py",
        # Three new hooks added in W1 (tiered-review-system):
        "edit_counter.py",   # PostToolUse Edit|Write — T0 nudge counter
        "edit_block.py",     # PreToolUse  Edit|Write — T0 hard block
        "commit_block.py",   # PreToolUse  Bash       — T2 commit gate
    ):
        assert expected in joined, f"{expected} not wired"
    # The Stop evidence-scanner is intentionally gone (folded into review_nudge).
    assert "stop_evidence_check.py" not in joined
