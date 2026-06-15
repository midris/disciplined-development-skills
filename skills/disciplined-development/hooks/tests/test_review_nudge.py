"""Tests for hooks/review_nudge.py — PostToolUse 3-segment nudge (rewritten for H4).

Subprocess-driven (matches test_commit_block, test_edit_block style).
A synthetic PostToolUse Bash payload drives the hook. The commit count is
produced by real git commits in a hermetic repo; the edits counter is seeded
directly via state.bump so the T1 condition can be exercised independently of
the T2 commit-count condition.

New contract (three segments on one envelope):
1. Verify segment — every landed commit, Gate-3 reminder. Independent of any
   threshold; always present on a landed commit unless bypass is active.
2. T1 nudge — fires when landed commit AND state.read(repo, branch, "edits")
   >= review_tiers.regular.commit_edit_floor (default 30).
3. T2 nudge — fires when commits-since-checkpoint (fork-base fallback when
   absent) >= review_tiers.cold_read_escalation.nudge_threshold (default 3).

Fixture style (mirrors test_commit_block):
- ``_init`` creates a hermetic trunk repo + feature branch so fork-base exists.
- ``_commit`` adds N commits on the current branch.
- ``_seed_edits`` writes the edits counter by calling state.bump N times.
- ``_seed_checkpoint`` sets the review checkpoint to HEAD~n_back.
- ``_run`` invokes the hook subprocess with configurable thresholds (DD_CONFIG),
  optional bypass, and a standard landed-commit payload.

Test plan (all required by H4 spec):
  test_non_commit_is_silent
      — non-git-commit Bash → no output (exit 0, empty stdout).
  test_failed_commit_is_silent
      — commit without [branch sha] marker → no output.
  test_verify_only_when_no_cadence_triggers
      — landed commit, edits < 30, commits-since-checkpoint < 3
        → verify segment present, no T1/T2 text.
  test_t1_fires_when_edits_at_floor
      — edits >= 30 at a landed commit → T1 nudge (/dd-review regular + T1 text).
  test_t1_absent_when_edits_below_floor
      — edits < 30 → no T1 nudge.
  test_t2_fires_when_commits_at_threshold_with_checkpoint
      — commits-since-checkpoint == 3 → T2 nudge (/dd-review cold-read).
  test_t2_absent_when_commits_below_threshold
      — 2 commits since checkpoint < 3 → no T2 nudge.
  test_t2_fork_base_fallback_fires
      — no checkpoint, commits-since-fork-base >= 3 → T2 nudge.
  test_t2_fork_base_fallback_absent_below_threshold
      — no checkpoint, < 3 commits since fork-base → no T2 nudge.
  test_both_t1_and_t2_fire_together
      — edits >= 30 AND commits-since-checkpoint >= 3 → both segments present.
  test_bypass_silences_all
      — DD_SKIP_REVIEW_NUDGE=1, committed landed → empty stdout.
  test_review_threshold_not_referenced
      — grep confirms counters.review_threshold absent from hook source.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

from hooks import review_nudge
from hooks.lib import state

HOOK = Path(__file__).resolve().parent.parent / "review_nudge.py"

TRUNK = "master"
BRANCH = "feature/x"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _ctx(r: subprocess.CompletedProcess) -> str | None:
    """Return the emitted additionalContext, or None when the hook was silent."""
    if not r.stdout.strip():
        return None
    return json.loads(r.stdout)["hookSpecificOutput"]["additionalContext"]


def _git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, check=True
    )


def _init(tmp_path: Path) -> Path:
    """Create a trunk repo with one seed commit, then check out feature branch.

    Returns the repo path. trunk = TRUNK, feature = BRANCH.
    Fork-base exists so commits_since_fork_base has a reference.
    """
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-b", TRUNK)
    _git(repo, "config", "user.email", "t@e.com")
    _git(repo, "config", "user.name", "T")
    (repo / "seed.txt").write_text("0\n")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "seed")
    # Create + check out feature branch so fork-base exists against trunk.
    _git(repo, "checkout", "-b", BRANCH)
    return repo


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


def _seed_edits(repo: Path, n: int, branch: str = BRANCH) -> None:
    """Seed the edits counter to ``n`` by calling state.bump n times.

    Uses the same writer (state.bump) as edit_counter.py so the hook sees
    a realistic on-disk file. Idempotent starting from 0.
    """
    root = _root(repo)
    for _ in range(n):
        state.bump(root, branch, "edits")


def _seed_checkpoint(repo: Path, n_back: int, branch: str = BRANCH) -> None:
    """Set checkpoint to HEAD~n_back so commits_since_checkpoint returns n_back.

    Uses state.set_checkpoint (same writer as dd_review_runner.py
    --write-checkpoint) so the hook sees a realistic on-disk file.
    """
    root = _root(repo)
    sha = _rev(repo, f"HEAD~{n_back}")
    state.set_checkpoint(root, branch, sha)


def _run(
    repo: Path,
    *,
    command: str = "git commit -m x",
    stdout: str | None = None,
    exit_code: int = 0,
    commit_edit_floor: int = 30,
    cold_read_nudge_threshold: int = 3,
    bypass: bool = False,
) -> subprocess.CompletedProcess:
    """Invoke review_nudge.py subprocess against ``repo``.

    Configures both T1 and T2 thresholds via DD_CONFIG:
    - review_tiers.regular.commit_edit_floor (T1)
    - review_tiers.cold_read_escalation.nudge_threshold (T2)

    ``stdout`` is the fake tool_response stdout; defaults to a realistic
    landed-commit marker ("[feature/x abc1234] msg").
    """
    if stdout is None:
        stdout = f"[{BRANCH} abc1234] msg"
    cfg = repo / "ddcfg.json"
    cfg.write_text(
        json.dumps(
            {
                "review_tiers": {
                    "regular": {"commit_edit_floor": commit_edit_floor},
                    "cold_read_escalation": {
                        "nudge_threshold": cold_read_nudge_threshold
                    },
                }
            }
        )
    )
    env = dict(os.environ)
    env["DD_CONFIG"] = str(cfg)
    env.pop("DD_SKIP_REVIEW_NUDGE", None)
    if bypass:
        env["DD_SKIP_REVIEW_NUDGE"] = "1"
    payload = {
        "tool_name": "Bash",
        "cwd": str(repo),
        "tool_input": {"command": command},
        "tool_response": {"stdout": stdout, "exit_code": exit_code},
    }
    return subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps(payload),
        cwd=str(repo),
        capture_output=True,
        text=True,
        env=env,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_non_commit_is_silent(tmp_path):
    """Non-git-commit Bash (e.g. ls) → exit 0, no output."""
    repo = _init(tmp_path)
    r = _run(repo, command="ls -la")
    assert r.returncode == 0 and r.stdout.strip() == ""


def test_failed_commit_is_silent(tmp_path):
    """Bash commit without landed marker ([branch sha]) → exit 0, no output."""
    repo = _init(tmp_path)
    _commit(repo, 1)
    # stdout has no "[branch sha]" marker → commit_landed is False
    r = _run(repo, command="git commit --dry-run", stdout="nothing to commit")
    assert r.returncode == 0 and r.stdout.strip() == ""


def test_verify_only_when_no_cadence_triggers(tmp_path):
    """Landed commit, edits < floor, commits < T2 threshold → verify only.

    Verify segment always fires on a landed commit. Neither T1 nor T2 fires.
    Uses commit_edit_floor=30 (default) and cold_read_nudge_threshold=3 (default).
    1 commit since fork-base (< 3); 0 edits seeded (< 30).
    """
    repo = _init(tmp_path)
    _commit(repo, 1)
    # No edits seeded, no checkpoint, 1 commit from fork-base
    r = _run(repo, commit_edit_floor=30, cold_read_nudge_threshold=3)
    ctx = _ctx(r)
    assert ctx is not None
    assert review_nudge.VERIFY_TEXT in ctx
    # Neither T1 (/dd-review regular with edit-count message) nor T2 text
    assert "/dd-review cold-read" not in ctx
    assert "unreviewed edits" not in ctx
    # The audience caveat rides only on T1/T2 review nudges, never the verify reminder.
    assert review_nudge.GATE_AUDIENCE not in ctx


def test_t1_fires_when_edits_at_floor(tmp_path):
    """edits == commit_edit_floor (30) at a landed commit → T1 nudge present.

    T1 nudge suggests /dd-review regular and mentions the edit count.
    Verify segment is also present.
    """
    repo = _init(tmp_path)
    _commit(repo, 1)
    _seed_edits(repo, 30)  # exactly at the floor
    r = _run(repo, commit_edit_floor=30, cold_read_nudge_threshold=10)
    ctx = _ctx(r)
    assert ctx is not None
    assert review_nudge.VERIFY_TEXT in ctx
    assert "/dd-review regular" in ctx
    assert "30" in ctx  # edit count appears in message
    assert review_nudge.GATE_AUDIENCE in ctx  # orchestrator/subagent audience framing


def test_t1_absent_when_edits_below_floor(tmp_path):
    """edits < commit_edit_floor → no T1 nudge; verify segment still present."""
    repo = _init(tmp_path)
    _commit(repo, 1)
    _seed_edits(repo, 29)  # one below the floor
    r = _run(repo, commit_edit_floor=30, cold_read_nudge_threshold=10)
    ctx = _ctx(r)
    assert ctx is not None
    assert review_nudge.VERIFY_TEXT in ctx
    assert "/dd-review regular" not in ctx


def test_t2_fires_when_commits_at_threshold_with_checkpoint(tmp_path):
    """3 commits since checkpoint == nudge_threshold(3) → T2 nudge present.

    T2 nudge suggests /dd-review cold-read.
    Verify segment is also present.
    """
    repo = _init(tmp_path)
    _commit(repo, 3)
    _seed_checkpoint(repo, 3)  # checkpoint at HEAD~3 → 3 commits since
    r = _run(repo, commit_edit_floor=100, cold_read_nudge_threshold=3)
    ctx = _ctx(r)
    assert ctx is not None
    assert review_nudge.VERIFY_TEXT in ctx
    assert "/dd-review cold-read" in ctx
    assert "3" in ctx
    assert review_nudge.GATE_AUDIENCE in ctx  # orchestrator/subagent audience framing


def test_t2_absent_when_commits_below_threshold(tmp_path):
    """2 commits since checkpoint < nudge_threshold(3) → no T2 nudge."""
    repo = _init(tmp_path)
    _commit(repo, 2)
    _seed_checkpoint(repo, 2)  # 2 commits since checkpoint
    r = _run(repo, commit_edit_floor=100, cold_read_nudge_threshold=3)
    ctx = _ctx(r)
    assert ctx is not None
    assert review_nudge.VERIFY_TEXT in ctx
    assert "/dd-review cold-read" not in ctx


def test_t2_fork_base_fallback_fires(tmp_path):
    """No checkpoint, 3 commits since fork-base >= nudge_threshold(3) → T2 nudge.

    Falls back to commits_since_fork_base; trunk=TRUNK exists as the base.
    """
    repo = _init(tmp_path)
    _commit(repo, 3)
    # No checkpoint seeded — fork-base fallback applies
    r = _run(repo, commit_edit_floor=100, cold_read_nudge_threshold=3)
    ctx = _ctx(r)
    assert ctx is not None
    assert review_nudge.VERIFY_TEXT in ctx
    assert "/dd-review cold-read" in ctx
    assert review_nudge.GATE_AUDIENCE in ctx  # orchestrator/subagent audience framing


def test_t2_fork_base_fallback_absent_below_threshold(tmp_path):
    """No checkpoint, 2 commits since fork-base < nudge_threshold(3) → no T2."""
    repo = _init(tmp_path)
    _commit(repo, 2)
    # No checkpoint seeded — fork-base fallback applies; 2 < 3
    r = _run(repo, commit_edit_floor=100, cold_read_nudge_threshold=3)
    ctx = _ctx(r)
    assert ctx is not None
    assert review_nudge.VERIFY_TEXT in ctx
    assert "/dd-review cold-read" not in ctx


def test_both_t1_and_t2_fire_together(tmp_path):
    """edits >= floor AND commits-since-checkpoint >= threshold → both T1 and T2.

    All three segments appear on the single envelope.
    """
    repo = _init(tmp_path)
    _commit(repo, 3)
    _seed_checkpoint(repo, 3)  # 3 commits since checkpoint
    _seed_edits(repo, 30)       # 30 edits
    r = _run(repo, commit_edit_floor=30, cold_read_nudge_threshold=3)
    ctx = _ctx(r)
    assert ctx is not None
    assert review_nudge.VERIFY_TEXT in ctx
    assert "/dd-review regular" in ctx   # T1
    assert "/dd-review cold-read" in ctx  # T2
    assert review_nudge.GATE_AUDIENCE in ctx  # audience framing present once


def test_bypass_silences_all(tmp_path):
    """DD_SKIP_REVIEW_NUDGE=1 → empty stdout on a landed commit (all silent)."""
    repo = _init(tmp_path)
    _commit(repo, 3)
    _seed_edits(repo, 30)
    _seed_checkpoint(repo, 3)
    r = _run(repo, commit_edit_floor=30, cold_read_nudge_threshold=3, bypass=True)
    assert r.returncode == 0 and r.stdout.strip() == ""


def test_review_threshold_not_referenced(tmp_path):
    """counters.review_threshold must not appear anywhere in review_nudge.py.

    This is an executable assertion that the old cadence key has been removed
    (per H4 spec: 'REMOVE all use of counters.review_threshold').
    """
    source = HOOK.read_text()
    assert "review_threshold" not in source, (
        "review_nudge.py still references counters.review_threshold — remove it"
    )


def test_valid_checkpoint_below_threshold_suppresses_fork_base(tmp_path):
    """Checkpoint-path beats fork-base: checkpoint count < T2 threshold → T2 ABSENT,
    even when commits-since-fork-base would be >= threshold.

    Setup: 6 commits on the feature branch (fork-base count == 6 >= threshold 3).
    Checkpoint placed 2 commits back (commits-since-checkpoint == 2 < threshold 3).
    The hook should read the checkpoint count (2), not the fork-base count (6),
    and omit the T2 nudge.

    _seed_checkpoint uses state.set_checkpoint (same writer as dd_review_runner.py
    --write-checkpoint) so the hook sees a realistic on-disk checkpoint file.
    Verify segment is still present (it fires on every landed commit).
    """
    repo = _init(tmp_path)
    _commit(repo, 6)  # 6 commits on branch → fork-base count = 6 >= 3
    _seed_checkpoint(repo, 2)  # checkpoint 2 back → commits-since-checkpoint = 2 < 3

    r = _run(repo, commit_edit_floor=100, cold_read_nudge_threshold=3)

    ctx = _ctx(r)
    # Verify segment always fires on a landed commit
    assert ctx is not None
    assert review_nudge.VERIFY_TEXT in ctx
    # Checkpoint (2 < 3) wins; fork-base count (6 >= 3) is ignored → T2 ABSENT
    assert "/dd-review cold-read" not in ctx


def test_no_trunk_fork_base_none_emits_verify_only(tmp_path):
    """No trunk ref → fork-base is None; T2 omitted; verify still fires.

    Branch initialized as 'trunkless' (not 'master' or 'main'), so
    resolve_fork_base returns None and the T2 segment is silently omitted.
    """
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-b", "trunkless")
    _git(repo, "config", "user.email", "t@e.com")
    _git(repo, "config", "user.name", "T")
    (repo / "seed.txt").write_text("0\n")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "seed")
    # 3 commits on trunk-less branch (no trunk to measure from)
    for i in range(3):
        (repo / "work.txt").write_text(f"line{i}\n")
        _git(repo, "add", ".")
        _git(repo, "commit", "-m", f"c{i}")
    cfg = repo / "ddcfg.json"
    cfg.write_text(json.dumps({"review_tiers": {"cold_read_escalation": {"nudge_threshold": 3}}}))
    env = dict(os.environ)
    env["DD_CONFIG"] = str(cfg)
    env.pop("DD_SKIP_REVIEW_NUDGE", None)
    payload = {
        "tool_name": "Bash",
        "cwd": str(repo),
        "tool_input": {"command": "git commit -m x"},
        "tool_response": {"stdout": "[trunkless abc1234] msg", "exit_code": 0},
    }
    r = subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps(payload),
        cwd=str(repo),
        capture_output=True,
        text=True,
        env=env,
    )
    ctx = _ctx(r)
    assert ctx is not None
    assert review_nudge.VERIFY_TEXT in ctx
    assert "/dd-review cold-read" not in ctx
