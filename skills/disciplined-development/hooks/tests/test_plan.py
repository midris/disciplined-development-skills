"""Consumer contract for explicit active-plan resolution."""

import os
import subprocess

import pytest

from hooks.lib import plan


def _git(args, cwd):
    subprocess.run(
        ["git", *args], cwd=str(cwd), check=True, capture_output=True, text=True
    )


@pytest.fixture
def fake_repo(tmp_path, monkeypatch):
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(["init"], repo)
    (repo / "plans").mkdir()
    (repo / ".claude").mkdir()
    monkeypatch.delenv("DD_ACTIVE_PLAN", raising=False)
    yield repo


def test_relative_env_pin_anchors_to_resolved_repo(fake_repo, monkeypatch):
    monkeypatch.setenv("DD_ACTIVE_PLAN", "plans/from-env.md")
    assert plan.resolve_active_plan(cwd=str(fake_repo)) == (
        str(fake_repo / "plans" / "from-env.md"),
        "DD_ACTIVE_PLAN env var",
    )


def test_absolute_env_pin_is_preserved(fake_repo, monkeypatch):
    target = str(fake_repo / "elsewhere.md")
    monkeypatch.setenv("DD_ACTIVE_PLAN", target)
    assert plan.resolve_active_plan(cwd=str(fake_repo)) == (
        target,
        "DD_ACTIVE_PLAN env var",
    )


def test_relative_pointer_pin_anchors_to_resolved_repo(fake_repo):
    pointer = fake_repo / ".claude" / "active-plan"
    pointer.write_text("plans/from-pointer.md\n")
    assert plan.resolve_active_plan(cwd=str(fake_repo)) == (
        str(fake_repo / "plans" / "from-pointer.md"),
        str(pointer),
    )


def test_missing_pinned_plan_remains_selected(fake_repo):
    pointer = fake_repo / ".claude" / "active-plan"
    pointer.write_text("plans/does-not-exist.md\n")
    assert plan.resolve_active_plan(cwd=str(fake_repo)) == (
        str(fake_repo / "plans" / "does-not-exist.md"),
        str(pointer),
    )


def test_plan_files_without_a_pin_do_not_trigger_mtime_fallback(fake_repo):
    older = fake_repo / "plans" / "older.md"
    newer = fake_repo / "plans" / "newer.md"
    older.write_text("# older\n")
    newer.write_text("# newer\n")
    os.utime(older, (1000, 1000))
    os.utime(newer, (2000, 2000))

    assert plan.resolve_active_plan(cwd=str(fake_repo)) is None


def test_empty_pointer_is_unpinned(fake_repo):
    (fake_repo / ".claude" / "active-plan").write_text("\n")
    assert plan.resolve_active_plan(cwd=str(fake_repo)) is None


def test_invalid_utf8_pointer_is_unpinned_not_a_crash(fake_repo):
    (fake_repo / ".claude" / "active-plan").write_bytes(b"\xff\xfe\n")
    assert plan.resolve_active_plan(cwd=str(fake_repo)) is None


def test_non_repo_cwd_anchors_relative_pin_to_given_cwd(tmp_path, monkeypatch):
    monkeypatch.setenv("DD_ACTIVE_PLAN", "plan.md")
    assert plan.resolve_active_plan(cwd=str(tmp_path)) == (
        str(tmp_path / "plan.md"),
        "DD_ACTIVE_PLAN env var",
    )
