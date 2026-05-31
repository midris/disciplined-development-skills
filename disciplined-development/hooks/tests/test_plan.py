"""Tests for hooks.lib.plan.resolve_active_plan.

Builds a fake repo under ``tmp_path`` with a ``.claude/active-plan`` pointer
and ``plans/*.md`` files, anchored via a real ``git init`` so the module's
``git rev-parse --show-toplevel`` probe resolves to the temp repo. The
``DD_ACTIVE_PLAN`` env var is set/cleared via monkeypatch.

Source-label strings are derived from ``hooks.lib.plan`` (ported from the
``dd_lib`` predecessor): the env tier → ``"DD_ACTIVE_PLAN env var"``, the
pointer tier → the anchored pointer-file path itself, the mtime tier →
``"mtime fallback"``. A non-existent ``DD_ACTIVE_PLAN`` path is returned
as-is (the env tier wins on non-empty, existence-agnostic).
"""
import os
import subprocess

import pytest

from hooks.lib import config
from hooks.lib import plan


def _git(args, cwd):
    subprocess.run(
        ["git", *args], cwd=str(cwd), check=True, capture_output=True, text=True
    )


@pytest.fixture
def fake_repo(tmp_path, monkeypatch):
    """A temp git repo with ``plans/`` + ``.claude/`` dirs. Clears
    ``DD_ACTIVE_PLAN`` by default; tests opt back in via monkeypatch."""
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(["init"], repo)
    (repo / "plans").mkdir()
    (repo / ".claude").mkdir()
    # Hermeticity against the REAL user config (this was the actual flake
    # cause). config.get() falls back to `Path.cwd()/.claude/dd-config.json`
    # when DD_CONFIG is unset — so running the suite from the repo ROOT (vs
    # hooks/) made resolve_active_plan read the project's real dd-config.json,
    # whose plans.fallback_glob (`plans/phase-*.md`, ...) matches none of this
    # fixture's files → the mtime test got None. Point DD_CONFIG at an absent
    # path so config loads {} → shipped defaults (fallback_glob ["plans/*.md"])
    # regardless of cwd. (DD_DEFAULTS is cleared similarly; config is lru_cached
    # and test_config.py mutates both — reset the cache so defaults stand.)
    monkeypatch.setenv("DD_CONFIG", str(tmp_path / "absent-dd-config.json"))
    monkeypatch.delenv("DD_DEFAULTS", raising=False)
    # Pin git-toplevel to the fixture repo too: removes the real subprocess
    # (and its 5s timeout) from these tests; the real _git_toplevel path is
    # covered by test_git_toplevel_resolves_real_repo.
    monkeypatch.setattr(plan, "_git_toplevel", lambda cwd=None: str(repo))
    monkeypatch.delenv("DD_ACTIVE_PLAN", raising=False)
    config.reset_config_cache()
    yield repo
    config.reset_config_cache()


def test_env_pointer_wins_over_everything(fake_repo, monkeypatch):
    # Both a pointer file and a plans/*.md exist, but the env var outranks them.
    (fake_repo / ".claude" / "active-plan").write_text("plans/from-pointer.md\n")
    (fake_repo / "plans" / "a.md").write_text("# a\n")
    monkeypatch.setenv("DD_ACTIVE_PLAN", "plans/from-env.md")

    assert plan.resolve_active_plan(cwd=str(fake_repo)) == (
        "plans/from-env.md",
        "DD_ACTIVE_PLAN env var",
    )


def test_pointer_file_used_when_no_env(fake_repo):
    (fake_repo / ".claude" / "active-plan").write_text("plans/from-pointer.md\n")
    (fake_repo / "plans" / "a.md").write_text("# a\n")

    result = plan.resolve_active_plan(cwd=str(fake_repo))
    assert result is not None
    plan_path, source = result
    assert plan_path == "plans/from-pointer.md"
    # Label is the anchored pointer-file path itself.
    assert source == os.path.join(str(fake_repo), ".claude", "active-plan")


def test_mtime_fallback_when_no_env_or_pointer(fake_repo):
    older = fake_repo / "plans" / "older.md"
    newer = fake_repo / "plans" / "newer.md"
    older.write_text("# older\n")
    newer.write_text("# newer\n")
    # Force a deterministic mtime ordering (newer is strictly newest).
    os.utime(older, (1000, 1000))
    os.utime(newer, (2000, 2000))

    result = plan.resolve_active_plan(cwd=str(fake_repo))
    assert result is not None
    plan_path, source = result
    assert plan_path == str(newer)
    assert source == "mtime fallback"


def test_git_toplevel_resolves_real_repo(git_repo):
    # fake_repo stubs _git_toplevel for hermeticity, so the real subprocess
    # path (invocation, returncode handling, output strip) is covered here
    # against the conftest real-git fixture — not left untested.
    root = plan._git_toplevel(cwd=str(git_repo))
    assert root is not None
    assert os.path.realpath(root) == os.path.realpath(str(git_repo))


def test_git_toplevel_returns_none_outside_repo(tmp_path):
    assert plan._git_toplevel(cwd=str(tmp_path)) is None


def test_no_plan_available_returns_none(fake_repo):
    # No env, no pointer, no plans/*.md.
    assert plan.resolve_active_plan(cwd=str(fake_repo)) is None


def test_nonexistent_env_path_returned_as_is(fake_repo, monkeypatch):
    # Documents ported behavior: a non-empty DD_ACTIVE_PLAN wins even when the
    # path does not exist — it is returned verbatim, NOT a fall-through.
    (fake_repo / "plans" / "a.md").write_text("# a\n")
    monkeypatch.setenv("DD_ACTIVE_PLAN", "plans/does-not-exist.md")

    assert plan.resolve_active_plan(cwd=str(fake_repo)) == (
        "plans/does-not-exist.md",
        "DD_ACTIVE_PLAN env var",
    )
