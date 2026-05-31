"""Tests for hooks/review_nudge.py — PostToolUse review-cadence nudge.

Subprocess-driven (like test_discipline_nudge). A synthetic PostToolUse
payload supplies the command + tool_response (the ``[branch sha]`` marker
commit_landed keys on), while the repo carries real commits so the
checkpoint / fork-base counts are computed against real git. The review
threshold is lowered via DD_CONFIG so a few commits cross it.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from hooks import review_nudge
from hooks.lib import state

HOOK = Path(__file__).resolve().parent.parent / "review_nudge.py"


def _ctx(r: subprocess.CompletedProcess) -> str | None:
    """Return the emitted additionalContext, or None when the hook was silent."""
    if not r.stdout.strip():
        return None
    return json.loads(r.stdout)["hookSpecificOutput"]["additionalContext"]


def _git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, check=True
    )


def _init(tmp_path: Path, branch: str = "master") -> Path:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-b", branch)
    _git(repo, "config", "user.email", "t@e.com")
    _git(repo, "config", "user.name", "T")
    (repo / "seed.txt").write_text("0\n")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "seed")
    return repo


def _commit(repo: Path, n: int) -> None:
    work = repo / "work.txt"
    for i in range(n):
        prev = work.read_text() if work.exists() else ""
        work.write_text(prev + f"line{i}\n")
        _git(repo, "add", ".")
        _git(repo, "commit", "-m", f"c{i}")


def _feature_branch(repo: Path, name: str, n: int) -> None:
    _git(repo, "checkout", "-b", name)
    _commit(repo, n)


def _root(repo: Path) -> str:
    return _git(repo, "rev-parse", "--show-toplevel").stdout.strip()


def _rev(repo: Path, ref: str) -> str:
    return _git(repo, "rev-parse", ref).stdout.strip()


def _run(repo: Path, *, command: str = "git commit -m x",
         stdout: str | None = None, exit_code: int = 0,
         threshold: int = 2, bypass: bool = False) -> subprocess.CompletedProcess:
    if stdout is None:
        stdout = "[feature/x abc1234] msg"
    cfg = repo / "ddcfg.json"
    cfg.write_text(json.dumps({"counters": {"review_threshold": threshold}}))
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
        [sys.executable, str(HOOK)], input=json.dumps(payload),
        cwd=str(repo), capture_output=True, text=True, env=env,
    )


def test_non_commit_is_silent(tmp_path):
    repo = _init(tmp_path)
    r = _run(repo, command="ls -la")
    assert r.returncode == 0 and r.stdout.strip() == ""


def test_dryrun_or_failed_commit_is_silent(tmp_path):
    repo = _init(tmp_path)
    _feature_branch(repo, "feature/x", 5)
    # No [branch sha] marker in stdout -> commit_landed False.
    r = _run(repo, command="git commit --dry-run", stdout="nothing to commit")
    assert r.returncode == 0 and r.stdout.strip() == ""


def test_no_checkpoint_below_threshold_emits_verification_only(tmp_path):
    # Landed commit, 1 commit since fork-base, below threshold 2: the cadence
    # segment is absent but the Gate-3 verification reminder still fires.
    repo = _init(tmp_path)
    _feature_branch(repo, "feature/x", 1)
    r = _run(repo, threshold=2)
    ctx = _ctx(r)
    assert ctx is not None and review_nudge.VERIFY_TEXT in ctx
    assert "/dd-review regular" not in ctx  # cadence segment absent


def test_no_checkpoint_at_threshold_emits_verification_and_cadence(tmp_path):
    repo = _init(tmp_path)
    _feature_branch(repo, "feature/x", 3)  # 3 commits since fork-base
    r = _run(repo, threshold=2)
    payload = json.loads(r.stdout)
    hso = payload["hookSpecificOutput"]
    assert hso["hookEventName"] == "PostToolUse"
    ctx = hso["additionalContext"]
    assert "checkpoint missing or invalidated" in ctx
    assert "3" in ctx and "/dd-review regular" in ctx
    assert review_nudge.VERIFY_TEXT in ctx  # verification rides along


def test_no_trunk_fork_base_none_emits_verification_only(tmp_path):
    # No trunk → fork-base None → cadence can't compute; verification still
    # fires on the landed commit (it doesn't depend on the cadence count).
    repo = _init(tmp_path, branch="trunkless")
    _commit(repo, 3)
    r = _run(repo, threshold=2)
    ctx = _ctx(r)
    assert ctx is not None and review_nudge.VERIFY_TEXT in ctx
    assert "/dd-review regular" not in ctx


def test_checkpoint_below_threshold_emits_verification_only(tmp_path):
    repo = _init(tmp_path)
    _feature_branch(repo, "feature/x", 3)
    state.set_checkpoint(_root(repo), "feature/x", _rev(repo, "HEAD~1"))  # 1 since
    r = _run(repo, threshold=2)
    ctx = _ctx(r)
    assert ctx is not None and review_nudge.VERIFY_TEXT in ctx
    assert "/dd-review regular" not in ctx


def test_checkpoint_at_threshold_emits_verification_and_cadence(tmp_path):
    repo = _init(tmp_path)
    _feature_branch(repo, "feature/x", 3)
    state.set_checkpoint(_root(repo), "feature/x", _rev(repo, "HEAD~3"))  # 3 since
    r = _run(repo, threshold=2)
    ctx = json.loads(r.stdout)["hookSpecificOutput"]["additionalContext"]
    assert "since the last clean review" in ctx
    assert "3" in ctx and "/dd-review regular" in ctx
    assert review_nudge.VERIFY_TEXT in ctx


def test_bypass_env_is_silent(tmp_path):
    repo = _init(tmp_path)
    _feature_branch(repo, "feature/x", 5)
    r = _run(repo, threshold=2, bypass=True)
    assert r.returncode == 0 and r.stdout.strip() == ""


def test_bool_threshold_rejected_falls_back_to_default(tmp_path):
    repo = _init(tmp_path)
    _feature_branch(repo, "feature/x", 3)  # 3 < default 5
    # JSON `true` must be rejected (not coerced to 1, which would fire the
    # cadence segment); default threshold (5) applies → 3 commits is below, so
    # the cadence segment stays absent. Verification still fires on the commit.
    r = _run(repo, threshold=True)
    ctx = _ctx(r)
    assert ctx is not None and review_nudge.VERIFY_TEXT in ctx
    assert "/dd-review regular" not in ctx
