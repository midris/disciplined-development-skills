"""Tests for hooks.lib.state — dumb per-branch state, checkpoint, fork-base.

The git-touching tests use the ``git_repo`` fixture (see conftest.py), which
inits a throwaway repo with an initial commit and yields its path.

Empirically verified before writing (see plan Task A4): after ``git commit
--amend`` the old commit object is still reachable via reflog, so
``git rev-list --count <old>..HEAD`` exits 0 with a WRONG positive count.
Detection therefore guards on ``git merge-base --is-ancestor`` (exit 0 =
ancestor/usable, exit 1 = amended-away or sibling, exit 128 = bogus) — all of
which are exercised below.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import hooks.lib.state as state

BRANCH = "feature/test-branch"


def _git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()


def _commit(repo: Path, name: str) -> str:
    (repo / name).write_text(name)
    _git(repo, "add", name)
    _git(repo, "commit", "-q", "-m", name)
    return _git(repo, "rev-parse", "HEAD")


# --- counters --------------------------------------------------------------


def test_bump_creates_at_one_then_increments(tmp_path):
    assert state.bump(tmp_path, BRANCH, "edits") == 1
    assert state.bump(tmp_path, BRANCH, "edits") == 2


def test_read_absent_is_zero(tmp_path):
    assert state.read(tmp_path, BRANCH, "edits") == 0


def test_read_after_bump(tmp_path):
    state.bump(tmp_path, BRANCH, "edits")
    state.bump(tmp_path, BRANCH, "edits")
    assert state.read(tmp_path, BRANCH, "edits") == 2


def test_reset_zeroes_counter(tmp_path):
    state.bump(tmp_path, BRANCH, "edits")
    state.reset(tmp_path, BRANCH, "edits")
    assert state.read(tmp_path, BRANCH, "edits") == 0


def test_corrupt_counter_reads_as_zero(tmp_path):
    state.bump(tmp_path, BRANCH, "edits")
    # Locate and corrupt the backing file regardless of internal layout.
    state_root = tmp_path / ".claude" / ".dd-state"
    files = list(state_root.rglob("*"))
    count_files = [p for p in files if p.is_file()]
    assert count_files, "expected a counter file to exist after bump"
    count_files[0].write_text("not-an-int\x00garbage")
    assert state.read(tmp_path, BRANCH, "edits") == 0


def test_branch_key_escapes_slashes(tmp_path):
    # A branch with slashes must not create nested dirs / escape the slug.
    state.bump(tmp_path, "feature/x/y", "edits")
    state_root = tmp_path / ".claude" / ".dd-state"
    # Exactly one direct child dir under the state root (the slug), no nesting
    # from the branch slashes.
    children = [p for p in state_root.iterdir()]
    assert len(children) == 1
    slug_dir = children[0]
    assert slug_dir.is_dir()
    assert "/" not in slug_dir.name
    assert slug_dir.name != "feature"  # not split into nested path parts


def test_counters_isolated_per_branch(tmp_path):
    state.bump(tmp_path, "branch-a", "edits")
    state.bump(tmp_path, "branch-a", "edits")
    state.bump(tmp_path, "branch-b", "edits")
    assert state.read(tmp_path, "branch-a", "edits") == 2
    assert state.read(tmp_path, "branch-b", "edits") == 1


# --- checkpoint ------------------------------------------------------------


def test_checkpoint_round_trips(tmp_path, git_repo):
    head = _git(git_repo, "rev-parse", "HEAD")
    state.set_checkpoint(git_repo, BRANCH, head)
    # HEAD == checkpoint -> 0 commits since.
    assert state.commits_since_checkpoint(git_repo, BRANCH) == 0


def test_commits_since_checkpoint_none_when_unset(git_repo):
    assert state.commits_since_checkpoint(git_repo, BRANCH) is None


def test_commits_since_checkpoint_counts_new_commits(git_repo):
    head = _git(git_repo, "rev-parse", "HEAD")
    state.set_checkpoint(git_repo, BRANCH, head)
    _commit(git_repo, "a")
    _commit(git_repo, "b")
    assert state.commits_since_checkpoint(git_repo, BRANCH) == 2


def test_commits_since_checkpoint_amended_away_is_none(git_repo):
    # The exit-0-wrong-count trap: amend HEAD so the recorded sha is no longer
    # an ancestor but is still reachable via reflog.
    _commit(git_repo, "a")
    old = _git(git_repo, "rev-parse", "HEAD")
    state.set_checkpoint(git_repo, BRANCH, old)
    _git(git_repo, "commit", "-q", "--amend", "-m", "a-amended")
    # rev-list --count old..HEAD would return a wrong positive (1); we expect None.
    assert state.commits_since_checkpoint(git_repo, BRANCH) is None


def test_commits_since_checkpoint_sibling_is_none(git_repo):
    base = _git(git_repo, "rev-parse", "HEAD")
    # Build a sibling commit off base on another branch, record it, return to base.
    _git(git_repo, "checkout", "-q", "-b", "sibling", base)
    sib = _commit(git_repo, "sib")
    _git(git_repo, "checkout", "-q", "-")
    state.set_checkpoint(git_repo, BRANCH, sib)
    assert state.commits_since_checkpoint(git_repo, BRANCH) is None


def test_commits_since_checkpoint_bogus_sha_is_none(git_repo):
    state.set_checkpoint(git_repo, BRANCH, "deadbeef" * 5)
    assert state.commits_since_checkpoint(git_repo, BRANCH) is None


def test_commits_since_checkpoint_non_repo_is_none(tmp_path):
    # A path that is not a git repo must degrade to None, not crash.
    state.set_checkpoint(tmp_path, BRANCH, "deadbeef" * 5)
    assert state.commits_since_checkpoint(tmp_path, BRANCH) is None


# --- fork base -------------------------------------------------------------


def test_resolve_fork_base_master_only(git_repo):
    # git_repo's default branch holds the initial commit; add commits past it.
    base = _git(git_repo, "rev-parse", "HEAD")
    default = _git(git_repo, "rev-parse", "--abbrev-ref", "HEAD")
    _git(git_repo, "checkout", "-q", "-b", "feature")
    _commit(git_repo, "a")
    fork = state.resolve_fork_base(git_repo, [default])
    assert fork == base


def test_resolve_fork_base_none_when_no_trunk(git_repo):
    assert state.resolve_fork_base(git_repo, ["nonexistent-trunk"]) is None


def test_resolve_fork_base_skips_missing_refs(git_repo):
    base = _git(git_repo, "rev-parse", "HEAD")
    default = _git(git_repo, "rev-parse", "--abbrev-ref", "HEAD")
    _git(git_repo, "checkout", "-q", "-b", "feature")
    _commit(git_repo, "a")
    # First trunk does not exist; second does -> should resolve against second.
    fork = state.resolve_fork_base(git_repo, ["nonexistent", default])
    assert fork == base


def test_commits_since_fork_base_counts(git_repo):
    default = _git(git_repo, "rev-parse", "--abbrev-ref", "HEAD")
    _git(git_repo, "checkout", "-q", "-b", "feature")
    _commit(git_repo, "a")
    _commit(git_repo, "b")
    assert state.commits_since_fork_base(git_repo, [default]) == 2


def test_commits_since_fork_base_none_when_no_base(git_repo):
    assert state.commits_since_fork_base(git_repo, ["nonexistent-trunk"]) is None


def test_commits_since_fork_base_zero_at_fork_point(git_repo):
    """Branch that hasn't diverged from trunk yet → 0 commits since fork base.

    Load-bearing for review_nudge (C2): the no-review threshold gates on
    branch-age, and 0 must read as 'no work yet,' not 'unknown' or 1."""
    default = _git(git_repo, "rev-parse", "--abbrev-ref", "HEAD")
    _git(git_repo, "checkout", "-q", "-b", "feature")
    # Branch HEAD == trunk HEAD; no new commits.
    assert state.commits_since_fork_base(git_repo, [default]) == 0


def test_git_helper_passes_timeout(monkeypatch):
    """state._git must pass a timeout — it runs inside review_nudge on every
    PostToolUse Bash, so a stuck git (index.lock, fsmonitor, slow NFS) must not
    hang the hook. Asserting the kwarg is the only deterministic regression
    guard for the timeout (a real hang can't be unit-tested)."""
    captured = {}

    def fake_run(argv, **kwargs):
        captured.update(kwargs)
        return subprocess.CompletedProcess(argv, 0, stdout="", stderr="")

    monkeypatch.setattr(state.subprocess, "run", fake_run)
    state._git("/some/repo", "status")
    assert captured.get("timeout") == 5


def test_git_helper_swallows_timeout(monkeypatch):
    """A TimeoutExpired (now reachable thanks to the timeout) degrades to None,
    not a crash — advisory state must never propagate."""

    def fake_run(argv, **kwargs):
        raise subprocess.TimeoutExpired(argv, kwargs.get("timeout"))

    monkeypatch.setattr(state.subprocess, "run", fake_run)
    assert state._git("/some/repo", "status") is None


def test_atomic_write_closes_fd_on_fdopen_failure(monkeypatch, tmp_path):
    # If os.fdopen raises (EMFILE/OOM territory), the mkstemp fd must still be
    # closed (no fd leak), and _atomic_write must not propagate.
    closed = []
    monkeypatch.setattr(
        state.os, "fdopen",
        lambda fd, mode: (_ for _ in ()).throw(OSError("boom")),
    )
    monkeypatch.setattr(state.os, "close", lambda fd: closed.append(fd))
    state._atomic_write(tmp_path / "x.count", "1")  # no exception
    assert closed  # the fd was closed despite the fdopen failure
