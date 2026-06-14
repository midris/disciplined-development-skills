"""Tests for hooks/discipline_nudge.py — PreToolUse re-ground counter.

Run as a subprocess (like test_dd_review_runner) so the stdin payload, env
bypass, exit code, and the PreToolUse JSON envelope are exercised
end-to-end. The discipline threshold is lowered via a DD_CONFIG override
so a test fires the nudge in a few calls instead of 25.

State is read back through the same git-resolved repo root the hook uses
(``rev-parse --show-toplevel``) so macOS /private symlink differences
between the tmp path and git's view can't desync the counter assertion.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from hooks import discipline_nudge
from hooks.lib import state

HOOK = Path(__file__).resolve().parent.parent / "discipline_nudge.py"


def _repo_root(repo: Path) -> Path:
    out = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    return Path(out)


def _run(repo: Path, *, threshold: int = 3, bypass: bool = False,
         payload: dict | None = None) -> subprocess.CompletedProcess:
    cfg = repo / "ddcfg.json"
    cfg.write_text(json.dumps({"counters": {"discipline_threshold": threshold}}))
    env = dict(os.environ)
    env["DD_CONFIG"] = str(cfg)
    if bypass:
        env["DD_SKIP_DISCIPLINE_NUDGE"] = "1"
    else:
        env.pop("DD_SKIP_DISCIPLINE_NUDGE", None)
    body = json.dumps(payload or {"tool_name": "Read", "cwd": str(repo)})
    return subprocess.run(
        [sys.executable, str(HOOK)], input=body, cwd=str(repo),
        capture_output=True, text=True, env=env,
    )


def test_below_threshold_silent_and_increments(git_repo):
    root = _repo_root(git_repo)

    r1 = _run(git_repo, threshold=3)
    assert r1.returncode == 0
    assert r1.stdout.strip() == ""
    assert state.read(root, "master", "discipline") == 1

    r2 = _run(git_repo, threshold=3)
    assert r2.returncode == 0
    assert r2.stdout.strip() == ""
    assert state.read(root, "master", "discipline") == 2


def test_at_threshold_emits_envelope_and_resets(git_repo):
    root = _repo_root(git_repo)

    _run(git_repo, threshold=3)
    _run(git_repo, threshold=3)
    r3 = _run(git_repo, threshold=3)

    assert r3.returncode == 0
    payload = json.loads(r3.stdout)
    hso = payload["hookSpecificOutput"]
    assert hso["hookEventName"] == "PreToolUse"
    ctx = hso["additionalContext"]
    # Pin the exact fixed, actionable message (imperative verbs included),
    # not just the nouns — a degraded "list of words" version must fail.
    assert ctx == discipline_nudge.REGROUND_TEXT
    assert "Re-read" in ctx and "Re-check" in ctx
    # Checkbox-tick reminder must be present (Change #2 of the checkbox-discipline plan).
    assert "checkbox" in ctx
    # Reset on fire: counter file removed, next read is 0.
    assert state.read(root, "master", "discipline") == 0
    # And the counter actually restarts from 1 on the next call (not merely
    # "file gone" — guards a reset that degraded to in-memory-only).
    _run(git_repo, threshold=3)
    assert state.read(root, "master", "discipline") == 1


def test_bypass_env_is_silent_no_op(git_repo):
    root = _repo_root(git_repo)
    _run(git_repo, threshold=3)
    _run(git_repo, threshold=3)  # counter now 2, one below threshold

    r = _run(git_repo, threshold=3, bypass=True)
    assert r.returncode == 0
    assert r.stdout.strip() == ""
    # Bypass does not bump — counter unchanged.
    assert state.read(root, "master", "discipline") == 2


def test_bool_threshold_rejected_falls_back_to_default(git_repo):
    root = _repo_root(git_repo)
    # JSON `true` for the threshold must NOT be coerced to 1 (which would
    # fire the nudge on the very first call); bool is rejected and the
    # default (50) applies, so a single call stays silent.
    r = _run(git_repo, threshold=True)
    assert r.returncode == 0
    assert r.stdout.strip() == ""
    assert state.read(root, "master", "discipline") == 1


def test_non_git_cwd_degrades_silent(tmp_path):
    plain = tmp_path / "not_a_repo"
    plain.mkdir()
    r = _run(plain, threshold=1)
    assert r.returncode == 0
    assert r.stdout.strip() == ""
