"""Tests for hooks/edit_block.py — PreToolUse T0 hard-block.

Subprocess-driven (matches test_edit_counter, test_review_nudge style).
A synthetic PreToolUse payload drives the hook; state-dir assertions confirm
the on-disk counter is never mutated; exit-code and stderr assert deny/allow.

Fixture style:
- ``_init`` creates a hermetic git repo for ``state.read`` to key on.
- ``_seed_counter`` writes a known edits.count directly via ``state.bump``.
- ``_run`` invokes the hook subprocess with a configurable threshold (via
  DD_CONFIG), optional bypass, optional payload override.
- Deny assertion: exit 2 + ``"[edit-block]"`` in stderr (mirrors the
  mechanism used in pre_pr_review.py — CC blocks PreToolUse ONLY on exit 2;
  exit-2 stderr is what CC feeds back to the model).
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from hooks.lib import state

HOOK = Path(__file__).resolve().parent.parent / "edit_block.py"

BRANCH = "feature/x"
COUNTER = "edits"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, check=True
    )


def _init(tmp_path: Path, branch: str = BRANCH) -> Path:
    """Create a hermetic git repo on ``branch`` with one seed commit."""
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-b", branch)
    _git(repo, "config", "user.email", "t@e.com")
    _git(repo, "config", "user.name", "T")
    (repo / "seed.txt").write_text("seed\n")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "seed")
    return repo


def _repo_root(repo: Path) -> str:
    return _git(repo, "rev-parse", "--show-toplevel").stdout.strip()


def _seed_counter(repo: Path, count: int, branch: str = BRANCH) -> None:
    """Seed the on-disk edits counter to exactly ``count`` via state.bump.

    Fixture seeds state via state.bump (same writer as edit_counter.py) so the
    hook sees a realistic on-disk file.
    """
    root = _repo_root(repo)
    for _ in range(count):
        state.bump(root, branch, COUNTER)


def _read_edits(repo: Path, branch: str = BRANCH) -> int:
    """Read the on-disk ``edits`` counter for ``branch`` in ``repo``."""
    return state.read(_repo_root(repo), branch, COUNTER)


def _run(
    repo: Path,
    *,
    hard_block_threshold: int = 60,
    bypass: bool = False,
    payload_override: str | None = None,
    tool_name: str = "Edit",
) -> subprocess.CompletedProcess:
    """Run edit_block.py as a subprocess against ``repo``.

    ``payload_override`` bypasses normal payload construction for
    malformed-payload tests.
    """
    cfg = repo / "ddcfg.json"
    cfg.write_text(
        json.dumps(
            {"review_tiers": {"fast": {"hard_block_threshold": hard_block_threshold}}}
        )
    )
    env = dict(os.environ)
    env["DD_CONFIG"] = str(cfg)
    env.pop("DD_SKIP_EDIT_BLOCK", None)
    if bypass:
        env["DD_SKIP_EDIT_BLOCK"] = "1"

    if payload_override is not None:
        stdin_text = payload_override
    else:
        payload = {
            "tool_name": tool_name,
            "cwd": str(repo),
            "tool_input": {"file_path": str(repo / "foo.py")},
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


def test_allow_below_threshold(tmp_path):
    """Stored count 59 (below 60) → allow: exit 0, no deny output."""
    repo = _init(tmp_path)
    _seed_counter(repo, 59)

    r = _run(repo, hard_block_threshold=60)

    assert r.returncode == 0
    assert r.stdout.strip() == ""
    assert r.stderr.strip() == ""


def test_deny_at_threshold(tmp_path):
    """Stored count == 60 (at threshold) → deny: exit 2, deny message on stderr."""
    repo = _init(tmp_path)
    _seed_counter(repo, 60)  # stored count = 60; this is the 61st edit

    r = _run(repo, hard_block_threshold=60)

    assert r.returncode == 2
    assert "[edit-block]" in r.stderr
    assert "adversarial-review skill" in r.stderr


def test_deny_above_threshold(tmp_path):
    """Stored count 75 (above threshold) → deny: exit 2, deny message on stderr."""
    repo = _init(tmp_path)
    _seed_counter(repo, 75)

    r = _run(repo, hard_block_threshold=60)

    assert r.returncode == 2
    assert "[edit-block]" in r.stderr
    assert "adversarial-review skill" in r.stderr


def test_counter_not_mutated_on_allow(tmp_path):
    """Hook NEVER writes the edits counter — on-disk value identical before/after (allow path)."""
    repo = _init(tmp_path)
    _seed_counter(repo, 59)
    before = _read_edits(repo)

    _run(repo, hard_block_threshold=60)

    after = _read_edits(repo)
    assert after == before, "edit_block must not mutate the edits counter"


def test_counter_not_mutated_on_deny(tmp_path):
    """Hook NEVER writes the edits counter — on-disk value identical before/after (deny path)."""
    repo = _init(tmp_path)
    _seed_counter(repo, 60)
    before = _read_edits(repo)

    _run(repo, hard_block_threshold=60)

    after = _read_edits(repo)
    assert after == before, "edit_block must not mutate the edits counter"


def test_bypass_allows_when_above_threshold(tmp_path):
    """DD_SKIP_EDIT_BLOCK=1 with count >= threshold → allow: exit 0, no deny."""
    repo = _init(tmp_path)
    _seed_counter(repo, 75)

    r = _run(repo, hard_block_threshold=60, bypass=True)

    assert r.returncode == 0
    assert r.stderr.strip() == ""


def test_malformed_stdin_with_low_counter_allows(tmp_path):
    """Malformed stdin with counter at 0 (below threshold) → exit 0, allow, no crash.

    _payload_cwd() falls back to os.getcwd() (which is the repo dir via
    cwd= on subprocess.run), so git resolves and the counter is read.
    Counter is 0 < 60, so the hook allows.
    """
    repo = _init(tmp_path)
    # No _seed_counter call → counter is 0 (below threshold)
    r = _run(repo, payload_override="this is not json{{{")
    assert r.returncode == 0
    assert r.stderr.strip() == ""


def test_empty_stdin_with_low_counter_allows(tmp_path):
    """Empty stdin with counter at 0 (below threshold) → exit 0, allow, no crash.

    _payload_cwd() falls back to os.getcwd() (which is the repo dir via
    cwd= on subprocess.run), so git resolves and the counter is read.
    Counter is 0 < 60, so the hook allows.
    """
    repo = _init(tmp_path)
    # No _seed_counter call → counter is 0 (below threshold)
    r = _run(repo, payload_override="")
    assert r.returncode == 0
    assert r.stderr.strip() == ""


def test_malformed_stdin_with_over_threshold_counter_still_denies(tmp_path):
    """Malformed stdin with counter at threshold (60) → exit 2, DENY.

    Documents the real degrade-silent behavior: malformed stdin does NOT
    unconditionally allow. _payload_cwd() falls back to os.getcwd() (set by
    cwd= on subprocess.run), so git resolves and the counter is read normally.
    Counter == 60 >= threshold → hook still denies.

    _seed_counter seeds via state.bump (same writer as edit_counter.py);
    _run sets cwd=str(repo) so os.getcwd() resolves to the same repo.
    """
    repo = _init(tmp_path)
    _seed_counter(repo, 60)  # counter at hard-block threshold

    r = _run(repo, hard_block_threshold=60, payload_override="this is not json{{{")

    assert r.returncode == 2
    assert "[edit-block]" in r.stderr
    assert "adversarial-review skill" in r.stderr


def test_no_git_repo_exits_zero_allow(tmp_path):
    """Non-git cwd in payload → exit 0, allow, no crash (degrade-silent)."""
    # Point cwd at a non-git directory; the hook must degrade silently.
    not_a_repo = tmp_path / "not_a_repo"
    not_a_repo.mkdir()
    # Need a cfg file too (reuse tmp_path directly).
    cfg = tmp_path / "ddcfg.json"
    cfg.write_text(json.dumps({"review_tiers": {"fast": {"hard_block_threshold": 60}}}))

    payload = {
        "tool_name": "Edit",
        "cwd": str(not_a_repo),
        "tool_input": {"file_path": str(not_a_repo / "foo.py")},
    }
    env = dict(os.environ)
    env["DD_CONFIG"] = str(cfg)
    env.pop("DD_SKIP_EDIT_BLOCK", None)

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
