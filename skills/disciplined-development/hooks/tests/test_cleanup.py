"""Tests for hooks.lib.cleanup — age-based log + orphaned-branch state sweep.

All paths are controlled via env: ``DD_LOG_DIR`` points the log sweep at a
tmp dir; the state sweep operates on ``<repo>/.claude/.dd-state``. ``now_ts``
is injected so age/throttle are deterministic without sleeping.
"""

from __future__ import annotations

import os
import subprocess
import time
from pathlib import Path

import pytest

from hooks.lib import cleanup, config


def _git(repo: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)


@pytest.fixture
def repo_env(tmp_path, monkeypatch):
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init", "-q", "-b", "master", str(repo)], check=True)
    _git(repo, "config", "user.email", "t@t")
    _git(repo, "config", "user.name", "T")
    (repo / "f").write_text("x")
    _git(repo, "add", ".")
    _git(repo, "commit", "-qm", "c1")
    logs = tmp_path / "logs"
    logs.mkdir()
    monkeypatch.setenv("DD_LOG_DIR", str(logs))
    monkeypatch.setenv("DD_CONFIG", "/nonexistent/dd-config.json")  # shipped defaults
    monkeypatch.delenv("DD_DEFAULTS", raising=False)
    config.reset_config_cache()
    yield repo, logs
    config.reset_config_cache()


def _state_root(repo: Path) -> Path:
    return repo / ".claude" / ".dd-state"


def test_sweep_prunes_old_logs_keeps_fresh_and_reviews(repo_env):
    repo, logs = repo_env
    old = logs / "dd-hooks-20200101.jsonl"
    fresh = logs / "dd-hooks-20990101.jsonl"
    reviews = logs / "reviews.jsonl"
    for f in (old, fresh, reviews):
        f.write_text("{}\n")
    now = time.time()
    os.utime(old, (now - 30 * 86400, now - 30 * 86400))  # 30d > 14d default
    os.utime(fresh, (now, now))
    os.utime(reviews, (now, now))  # appended-recently → survives

    assert cleanup.sweep(str(repo), now) is True
    assert not old.exists()
    assert fresh.exists() and reviews.exists()


def test_sweep_keeps_stale_reviews_jsonl(repo_env):
    # reviews.jsonl is the curated analysis artifact — never pruned by age,
    # even on a branch that goes long without a review (the rolling
    # dd-hooks-*.jsonl day files are the only thing the age sweep touches).
    repo, logs = repo_env
    reviews = logs / "reviews.jsonl"
    reviews.write_text("{}\n")
    stale = time.time() - 60 * 86400  # 60d > 14d default retention
    os.utime(reviews, (stale, stale))
    assert cleanup.sweep(str(repo), time.time()) is True
    assert reviews.exists()


def test_sweep_removes_orphan_state_keeps_live_and_dotdirs(repo_env):
    repo, _ = repo_env
    root = _state_root(repo)
    (root / "master").mkdir(parents=True)          # live (current branch)
    (root / "feature_gone").mkdir(parents=True)    # orphan — no such branch
    (root / ".logs").mkdir(parents=True)           # dot dir — never a branch
    (root / ".logs" / "x.jsonl").write_text("{}\n")

    assert cleanup.sweep(str(repo), time.time()) is True
    assert (root / "master").exists()
    assert not (root / "feature_gone").exists()
    assert (root / ".logs").exists() and (root / ".logs" / "x.jsonl").exists()


def test_throttle_skips_recent_runs_when_stale(repo_env):
    repo, _ = repo_env
    now = time.time()
    assert cleanup.sweep(str(repo), now) is True          # first run
    assert cleanup.sweep(str(repo), now + 60) is False    # within 24h → skip
    assert cleanup.sweep(str(repo), now + 25 * 3600) is True  # past throttle


def test_sweep_degrades_on_non_repo(tmp_path, monkeypatch):
    monkeypatch.setenv("DD_LOG_DIR", str(tmp_path / "absent-logs"))
    monkeypatch.setenv("DD_CONFIG", "/nonexistent/dd-config.json")
    monkeypatch.delenv("DD_DEFAULTS", raising=False)
    config.reset_config_cache()
    try:
        # Not a git repo, no .dd-state, no logs — must not raise.
        result = cleanup.sweep(str(tmp_path / "notrepo"), time.time())
        assert result in (True, False)
    finally:
        config.reset_config_cache()


def test_orphan_sweep_skipped_when_branches_unenumerable(tmp_path, monkeypatch):
    # No git → _live_branch_slugs None → state dirs are NOT deleted (don't
    # delete what you can't verify).
    monkeypatch.setenv("DD_LOG_DIR", str(tmp_path / "logs"))
    monkeypatch.setenv("DD_CONFIG", "/nonexistent/dd-config.json")
    monkeypatch.delenv("DD_DEFAULTS", raising=False)
    config.reset_config_cache()
    try:
        notrepo = tmp_path / "notrepo"
        root = notrepo / ".claude" / ".dd-state"
        (root / "some_branch").mkdir(parents=True)
        cleanup.sweep(str(notrepo), time.time())
        assert (root / "some_branch").exists()  # preserved (no git to verify)
    finally:
        config.reset_config_cache()


def test_detached_head_current_state_dir_kept(repo_env):
    # On detached HEAD the discipline counter keys under "detached"; the sweep
    # must not delete the current key's dir (G4 "never the current branch").
    repo, _ = repo_env
    sha = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    subprocess.run(["git", "-C", str(repo), "checkout", "-q", sha], check=True)
    root = _state_root(repo)
    (root / "detached").mkdir(parents=True)
    cleanup.sweep(str(repo), time.time())
    assert (root / "detached").exists()
