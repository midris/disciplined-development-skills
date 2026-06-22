"""Tests for hooks/commit_block.py — PreToolUse T2 commit hard-block.

Subprocess-driven (matches test_edit_block, test_review_nudge style).
A synthetic PreToolUse Bash payload drives the hook. The commit count is
produced by real git commits in a hermetic repo, so state.commits_since_checkpoint
and commits_since_fork_base are exercised against real git history.

Fixture style:
- ``_init`` creates a hermetic trunk repo + feature branch so fork-base exists.
- ``_commit`` adds N commits on the current branch.
- ``_run`` invokes the hook subprocess with a configurable threshold (DD_CONFIG),
  optional bypass, optional payload override, and optional checkpoint seed.
- Deny assertion: exit 2 + ``"[commit-block]"`` in stderr (same deny mechanism as
  pre_pr_review.py and edit_block.py — CC blocks PreToolUse ONLY on exit 2;
  exit-2 stderr is what CC feeds back to the model).

Test plan (all required by H3 spec):
  test_non_git_commit_command_allows    — non-git-commit Bash → ALLOW
  test_below_threshold_allows           — commits since checkpoint < threshold → ALLOW
  test_at_threshold_denies              — commits since checkpoint == threshold → DENY
  test_amend_at_threshold_denies        — git commit --amend while over → DENY
  test_no_checkpoint_below_threshold_allows  — fork-base fallback, < threshold → ALLOW
  test_no_checkpoint_at_threshold_denies     — fork-base fallback, == threshold → DENY
  test_bypass_allows_when_over_threshold     — DD_SKIP_COMMIT_BLOCK=1, over → ALLOW
  test_malformed_stdin_exits_zero_allow      — malformed payload → exit 0, ALLOW
  test_empty_stdin_exits_zero_allow          — empty stdin → exit 0, ALLOW
  test_no_git_repo_exits_zero_allow          — unresolvable repo → exit 0, ALLOW
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from hooks.lib import state

HOOK = Path(__file__).resolve().parent.parent / "commit_block.py"

TRUNK = "master"
BRANCH = "feature/x"
COUNTER = "review"  # the checkpoint is keyed under "review.checkpoint"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, check=True
    )


def _init(tmp_path: Path) -> tuple[Path, Path]:
    """Create a trunk repo with one seed commit, then a feature branch.

    Returns (repo, root_of_repo). The feature branch is checked out; trunk
    exists so resolve_fork_base has a reference to measure against.
    """
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-b", TRUNK)
    _git(repo, "config", "user.email", "t@e.com")
    _git(repo, "config", "user.name", "T")
    (repo / "seed.txt").write_text("0\n")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "seed")
    # Create feature branch from trunk
    _git(repo, "checkout", "-b", BRANCH)
    return repo, repo  # git top-level == repo for these fixtures


def _commit(repo: Path, n: int) -> None:
    """Add ``n`` commits on the current branch."""
    work = repo / "work.txt"
    for i in range(n):
        prev = work.read_text() if work.exists() else ""
        work.write_text(prev + f"line{i}\n")
        _git(repo, "add", ".")
        _git(repo, "commit", "-m", f"c{i}")


def _root(repo: Path) -> str:
    return _git(repo, "rev-parse", "--show-toplevel").stdout.strip()


def _rev(repo: Path, ref: str) -> str:
    return _git(repo, "rev-parse", ref).stdout.strip()


def _seed_checkpoint(repo: Path, n_back: int, branch: str = BRANCH) -> None:
    """Set checkpoint to HEAD~n_back so commits_since_checkpoint returns n_back.

    Fixture seeds the checkpoint directly via state.set_checkpoint (same writer
    as external_review.py and log_review.py) so the hook sees a realistic
    on-disk file.
    """
    root = _root(repo)
    sha = _rev(repo, f"HEAD~{n_back}")
    state.set_checkpoint(root, branch, sha)


def _run(
    repo: Path,
    *,
    command: str = "git commit -m x",
    hard_block_threshold: int = 5,
    bypass: bool = False,
    payload_override: str | None = None,
) -> subprocess.CompletedProcess:
    """Run commit_block.py as a subprocess against ``repo``.

    ``payload_override`` bypasses normal payload construction for
    malformed/empty-payload tests.
    """
    cfg = repo / "ddcfg.json"
    cfg.write_text(
        json.dumps(
            {
                "review_tiers": {
                    "cold_read_escalation": {
                        "hard_block_threshold": hard_block_threshold
                    }
                }
            }
        )
    )
    env = dict(os.environ)
    env["DD_CONFIG"] = str(cfg)
    env.pop("DD_SKIP_COMMIT_BLOCK", None)
    if bypass:
        env["DD_SKIP_COMMIT_BLOCK"] = "1"

    if payload_override is not None:
        stdin_text = payload_override
    else:
        payload = {
            "tool_name": "Bash",
            "cwd": str(repo),
            "tool_input": {"command": command},
        }
        stdin_text = json.dumps(payload)

    return subprocess.run(
        [sys.executable, str(HOOK)],
        input=stdin_text,
        cwd=str(repo),
        capture_output=True,
        text=True,
        env=env,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_non_git_commit_command_allows(tmp_path):
    """Non-git-commit Bash command → exit 0, ALLOW, no output."""
    repo, _ = _init(tmp_path)
    _commit(repo, 6)  # 6 commits, well over any threshold

    r = _run(repo, command="ls -la")

    assert r.returncode == 0
    assert r.stderr.strip() == ""


def test_below_threshold_allows(tmp_path):
    """4 commits since checkpoint (below 5) → exit 0, ALLOW."""
    repo, _ = _init(tmp_path)
    _commit(repo, 4)
    _seed_checkpoint(repo, 4)  # checkpoint at HEAD~4 → 4 commits since

    r = _run(repo, hard_block_threshold=5)

    assert r.returncode == 0
    assert r.stderr.strip() == ""


def test_at_threshold_denies(tmp_path):
    """5 commits since checkpoint (== threshold 5) → exit 2, DENY.

    The spec says 'allows 5 between cold-reads, denies the 6th'. The stored
    count == 5 means 5 landed commits since the last cold-read; the 6th is
    being attempted now → block. Stored count is the landed value;
    PreToolUse reads it before this commit lands.
    """
    repo, _ = _init(tmp_path)
    _commit(repo, 5)
    _seed_checkpoint(repo, 5)  # checkpoint at HEAD~5 → 5 commits since

    r = _run(repo, hard_block_threshold=5)

    assert r.returncode == 2
    assert "[commit-block]" in r.stderr
    assert "/dd-review cold-read" in r.stderr


def test_amend_at_threshold_denies(tmp_path):
    """git commit --amend while at threshold → exit 2, DENY.

    is_git_commit() returns True for --amend; amend is intentionally gated
    the same way as a new commit (coarse 'you owe a cold-read' gate, per spec
    Out of scope note).
    """
    repo, _ = _init(tmp_path)
    _commit(repo, 5)
    _seed_checkpoint(repo, 5)  # 5 since checkpoint → at threshold

    r = _run(repo, command="git commit --amend --no-edit", hard_block_threshold=5)

    assert r.returncode == 2
    assert "[commit-block]" in r.stderr


def test_no_checkpoint_below_threshold_allows(tmp_path):
    """No checkpoint → counts since fork base; 3 < 5 → ALLOW.

    Sets up trunk + feature branch with 3 commits, no checkpoint. The hook
    falls back to commits_since_fork_base (fork = trunk) which returns 3.
    """
    repo, _ = _init(tmp_path)
    _commit(repo, 3)
    # No checkpoint seeded — fork-base fallback applies

    r = _run(repo, hard_block_threshold=5)

    assert r.returncode == 0
    assert r.stderr.strip() == ""


def test_no_checkpoint_at_threshold_denies(tmp_path):
    """No checkpoint → counts since fork base; 5 commits == threshold 5 → DENY."""
    repo, _ = _init(tmp_path)
    _commit(repo, 5)
    # No checkpoint seeded — fork-base fallback applies

    r = _run(repo, hard_block_threshold=5)

    assert r.returncode == 2
    assert "[commit-block]" in r.stderr
    assert "/dd-review cold-read" in r.stderr


def test_bypass_allows_when_over_threshold(tmp_path):
    """DD_SKIP_COMMIT_BLOCK=1 with 5 commits since checkpoint → exit 0, ALLOW."""
    repo, _ = _init(tmp_path)
    _commit(repo, 5)
    _seed_checkpoint(repo, 5)  # 5 since checkpoint → at threshold

    r = _run(repo, hard_block_threshold=5, bypass=True)

    assert r.returncode == 0
    assert r.stderr.strip() == ""


def test_malformed_stdin_exits_zero_allow(tmp_path):
    """Malformed stdin → exit 0, ALLOW, no crash (degrade-silent)."""
    repo, _ = _init(tmp_path)
    r = _run(repo, payload_override="this is not json{{{")
    assert r.returncode == 0
    assert r.stderr.strip() == ""


def test_empty_stdin_exits_zero_allow(tmp_path):
    """Empty stdin → exit 0, ALLOW, no crash (degrade-silent)."""
    repo, _ = _init(tmp_path)
    r = _run(repo, payload_override="")
    assert r.returncode == 0
    assert r.stderr.strip() == ""


def test_valid_checkpoint_below_threshold_suppresses_fork_base(tmp_path):
    """Checkpoint-path beats fork-base: checkpoint count < threshold → ALLOW,
    even when commits-since-fork-base would be >= threshold.

    Setup: 6 commits on the feature branch (fork-base count == 6 >= threshold 5).
    Checkpoint placed 2 commits back (commits-since-checkpoint == 2 < threshold 5).
    The hook should read the checkpoint count (2), not the fork-base count (6),
    and allow the commit.

    _seed_checkpoint uses state.set_checkpoint (same writer as external_review.py
    and log_review.py) so the hook sees a realistic on-disk checkpoint file.
    """
    repo, _ = _init(tmp_path)
    _commit(repo, 6)  # 6 commits on branch → fork-base count = 6 >= 5
    _seed_checkpoint(repo, 2)  # checkpoint 2 back → commits-since-checkpoint = 2 < 5

    r = _run(repo, hard_block_threshold=5)

    # Checkpoint (2 < 5) wins; fork-base count (6 >= 5) is ignored → ALLOW
    assert r.returncode == 0
    assert r.stderr.strip() == ""


def test_no_git_repo_exits_zero_allow(tmp_path):
    """Non-git cwd in payload → exit 0, ALLOW, no crash (degrade-silent)."""
    not_a_repo = tmp_path / "not_a_repo"
    not_a_repo.mkdir()
    cfg = tmp_path / "ddcfg.json"
    cfg.write_text(
        json.dumps(
            {"review_tiers": {"cold_read_escalation": {"hard_block_threshold": 5}}}
        )
    )
    payload = {
        "tool_name": "Bash",
        "cwd": str(not_a_repo),
        "tool_input": {"command": "git commit -m x"},
    }
    env = dict(os.environ)
    env["DD_CONFIG"] = str(cfg)
    env.pop("DD_SKIP_COMMIT_BLOCK", None)

    r = subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps(payload),
        cwd=str(not_a_repo),
        capture_output=True,
        text=True,
        env=env,
    )
    assert r.returncode == 0
    assert r.stderr.strip() == ""
