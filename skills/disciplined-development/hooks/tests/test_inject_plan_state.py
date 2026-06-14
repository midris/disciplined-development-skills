"""Tests for hooks/inject_plan_state.py — UserPromptSubmit plan-state injector.

Run as a subprocess (like test_discipline_nudge) so the stdin payload, plain
stdout channel, and exit code are exercised end-to-end. UserPromptSubmit
surfaces context via plain stdout (the documented contract for this event),
so assertions read ``stdout`` directly rather than a JSON envelope.

The repo is a hermetic git repo (conftest ``git_repo``, on ``master`` with one
commit) extended with ``plans/`` + ``.claude/``. ``DD_CONFIG`` points at an
absent path so the shipped ``dd-defaults.json`` stands — its ``fallback_glob``
(``plans/*.md``) matches the fixture and its ``skip_section_headers`` include
``verification`` (needed by the skip-section test).

State is read back through the git-resolved repo root the hook uses
(``rev-parse --show-toplevel``) so macOS /private symlink differences between
the tmp path and git's view can't desync the counter assertion.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from hooks.lib import state

HOOK = Path(__file__).resolve().parent.parent / "inject_plan_state.py"


@pytest.fixture
def plan_repo(git_repo):
    (git_repo / "plans").mkdir()
    (git_repo / ".claude").mkdir()
    return git_repo


def _repo_root(repo: Path) -> Path:
    out = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    return Path(out)


def _run(repo: Path, *, env_extra: dict | None = None, bypass: bool = False,
         payload: dict | None = None) -> subprocess.CompletedProcess:
    env = dict(os.environ)
    # Absent DD_CONFIG → shipped defaults stand regardless of cwd.
    env["DD_CONFIG"] = str(repo / "absent-dd-config.json")
    env.pop("DD_DEFAULTS", None)
    env.pop("DD_ACTIVE_PLAN", None)
    if bypass:
        env["DD_SKIP_INJECT_PLAN_STATE"] = "1"
    else:
        env.pop("DD_SKIP_INJECT_PLAN_STATE", None)
    if env_extra:
        env.update(env_extra)
    body = json.dumps(payload or {"cwd": str(repo)})
    return subprocess.run(
        [sys.executable, str(HOOK)], input=body, cwd=str(repo),
        capture_output=True, text=True, env=env,
    )


def test_env_pointer_then_file_then_mtime_precedence(plan_repo):
    # All three sources present; env wins, then pointer, then mtime fallback.
    (plan_repo / "plans" / "from-env.md").write_text("# env\n- [ ] e\n")
    (plan_repo / "plans" / "from-pointer.md").write_text("# ptr\n- [ ] p\n")
    (plan_repo / ".claude" / "active-plan").write_text("plans/from-pointer.md\n")

    r_env = _run(plan_repo, env_extra={"DD_ACTIVE_PLAN": "plans/from-env.md"})
    assert r_env.returncode == 0
    assert "plans/from-env.md" in r_env.stdout
    assert "DD_ACTIVE_PLAN env var" in r_env.stdout

    r_ptr = _run(plan_repo)
    assert r_ptr.returncode == 0
    assert "plans/from-pointer.md" in r_ptr.stdout
    assert "DD_ACTIVE_PLAN env var" not in r_ptr.stdout


def test_mtime_fallback_annotated(plan_repo):
    older = plan_repo / "plans" / "older.md"
    newer = plan_repo / "plans" / "newer.md"
    older.write_text("# older\n- [ ] o\n")
    newer.write_text("# newer\n- [ ] n\n")
    os.utime(older, (1000, 1000))
    os.utime(newer, (2000, 2000))

    r = _run(plan_repo)
    assert r.returncode == 0
    assert "newer.md" in r.stdout
    assert "mtime fallback" in r.stdout


def test_progress_counts_top_level_and_skips_template_section(plan_repo):
    # Verification's checkboxes must NOT count; the level-aware skip ends at
    # the next same-level heading so Task three (after it) is counted.
    (plan_repo / "plans" / "p.md").write_text(
        "# Plan\n"
        "- [x] Task one\n"
        "- [ ] Task two\n"
        "\n"
        "## Verification\n"
        "- [ ] skip a\n"
        "- [ ] skip b\n"
        "\n"
        "## Task Breakdown\n"
        "- [ ] Task three\n"
    )
    (plan_repo / ".claude" / "active-plan").write_text("plans/p.md\n")

    r = _run(plan_repo)
    assert r.returncode == 0
    assert "Progress: 1 / 3 top-level tasks" in r.stdout
    assert "Next pending:" in r.stdout
    assert "Task two" in r.stdout


def test_fenced_code_blocks_are_ignored(plan_repo):
    # A `#` comment inside a ```bash fence must NOT clear an active skip
    # section, and a `- [ ]` shown as example markdown inside a fence must NOT
    # be counted as a task. Only the 3 real top-level tasks count.
    (plan_repo / "plans" / "p.md").write_text(
        "# Plan\n"
        "- [x] Task one\n"
        "- [ ] Task two\n"
        "\n"
        "## Verification\n"
        "```bash\n"
        "# run the tests\n"
        "- [ ] not a real task (inside fence, inside skip)\n"
        "```\n"
        "- [ ] still skipped (verification section)\n"
        "\n"
        "## Task Breakdown\n"
        "```markdown\n"
        "- [ ] example checkbox in a fence — must not count\n"
        "```\n"
        "- [ ] Task three\n"
    )
    (plan_repo / ".claude" / "active-plan").write_text("plans/p.md\n")

    r = _run(plan_repo)
    assert r.returncode == 0
    assert "Progress: 1 / 3 top-level tasks" in r.stdout
    assert "Task two" in r.stdout


def test_next_pending_title_truncated(plan_repo):
    long_title = "T" * 200
    (plan_repo / "plans" / "p.md").write_text(
        "# Plan\n"
        "- [x] done\n"
        f"- [ ] {long_title}\n"
    )
    (plan_repo / ".claude" / "active-plan").write_text("plans/p.md\n")

    r = _run(plan_repo)
    assert r.returncode == 0
    # Truncated to 117 chars + "..." (the 120-char cap), not the full 200.
    assert ("T" * 117 + "...") in r.stdout
    assert ("T" * 200) not in r.stdout


def test_uppercase_checkbox_counts_as_done(plan_repo):
    # Some editors write `- [X]` (capital). It must count as done, not be
    # mistaken for a pending task.
    (plan_repo / "plans" / "p.md").write_text(
        "# Plan\n"
        "- [X] Task one (capital X, done)\n"
        "- [ ] Task two\n"
    )
    (plan_repo / ".claude" / "active-plan").write_text("plans/p.md\n")
    r = _run(plan_repo)
    assert r.returncode == 0
    assert "Progress: 1 / 2 top-level tasks" in r.stdout
    assert "Task two" in r.stdout  # next pending is the lowercase-blank one


def test_discipline_counter_reset_on_turn(plan_repo):
    root = _repo_root(plan_repo)
    (plan_repo / "plans" / "p.md").write_text("# Plan\n- [ ] a\n")
    (plan_repo / ".claude" / "active-plan").write_text("plans/p.md\n")

    # Simulate accumulated tool calls since the last re-ground.
    state.bump(root, "master", "discipline")
    state.bump(root, "master", "discipline")
    assert state.read(root, "master", "discipline") == 2

    r = _run(plan_repo)
    assert r.returncode == 0
    # New user turn resets the action counter.
    assert state.read(root, "master", "discipline") == 0


def test_no_active_plan_graceful_notice(plan_repo):
    # Empty plans/, no pointer, no env → short notice, not a crash.
    r = _run(plan_repo)
    assert r.returncode == 0
    assert "No active plan" in r.stdout


def test_non_repo_cwd_no_cross_tree_resolution(tmp_path):
    # Outside a git repo, the injector must not surface a stray plans/ dir from
    # an unrelated tree — it resolves the plan only when in a repo (matching
    # discipline_nudge's not-a-repo→skip pattern). A plans/ here must be ignored.
    plain = tmp_path / "notrepo"
    (plain / "plans").mkdir(parents=True)
    (plain / "plans" / "stray.md").write_text("# stray\n- [ ] x\n")
    env = dict(os.environ)
    env["DD_CONFIG"] = str(plain / "absent.json")
    env.pop("DD_DEFAULTS", None)
    env.pop("DD_ACTIVE_PLAN", None)
    env.pop("DD_SKIP_INJECT_PLAN_STATE", None)
    r = subprocess.run(
        [sys.executable, str(HOOK)], input=json.dumps({"cwd": str(plain)}),
        cwd=str(plain), capture_output=True, text=True, env=env,
    )
    assert r.returncode == 0
    assert "stray" not in r.stdout
    assert "No active plan" in r.stdout


def test_bypass_env_silent_no_op(plan_repo):
    root = _repo_root(plan_repo)
    (plan_repo / "plans" / "p.md").write_text("# Plan\n- [ ] a\n")
    (plan_repo / ".claude" / "active-plan").write_text("plans/p.md\n")
    state.bump(root, "master", "discipline")

    r = _run(plan_repo, bypass=True)
    assert r.returncode == 0
    assert r.stdout.strip() == ""
    # Bypass does not reset the counter either.
    assert state.read(root, "master", "discipline") == 1
