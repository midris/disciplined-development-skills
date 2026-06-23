"""Tests for hooks/discipline_nudge.py — PreToolUse re-ground counter.

Run as a subprocess (like test_external_review) so the stdin payload, env
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
         payload: dict | None = None,
         env_extra: dict | None = None) -> subprocess.CompletedProcess:
    cfg = repo / "ddcfg.json"
    cfg.write_text(json.dumps({"counters": {"discipline_threshold": threshold}}))
    env = dict(os.environ)
    env["DD_CONFIG"] = str(cfg)
    if bypass:
        env["DD_SKIP_DISCIPLINE_NUDGE"] = "1"
    else:
        env.pop("DD_SKIP_DISCIPLINE_NUDGE", None)
    # Neutralize the env tier for plan resolution so subprocess tests
    # control inputs deterministically (pointer file + mtime fallback).
    env.pop("DD_ACTIVE_PLAN", None)
    if env_extra:
        env.update(env_extra)
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
    # The re-ground text is now followed by a plan line — assert prefix, not
    # exact equality (plan line was appended in the fire branch).
    assert ctx.startswith(discipline_nudge.REGROUND_TEXT)
    # The plan line must follow the re-ground text. git_repo seeds seed.txt
    # only — no plans/ dir and no pointer file — so resolve_active_plan
    # returns None and the no-plan message is appended.
    assert "No active plan pinned" in ctx
    # Pin the actionable verbs in the re-ground block (imperative verbs
    # included) — a degraded "list of words" version must fail.
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


def test_fire_message_names_active_plan_path(git_repo):
    # Pin the plan via pointer file — env tier is neutralised in _run.
    (git_repo / ".claude").mkdir(exist_ok=True)
    (git_repo / ".claude" / "active-plan").write_text("plans/foo.md\n")
    (git_repo / "plans").mkdir(exist_ok=True)
    (git_repo / "plans" / "foo.md").write_text("# plan\n")

    _run(git_repo, threshold=3)
    _run(git_repo, threshold=3)
    r3 = _run(git_repo, threshold=3)

    assert r3.returncode == 0
    ctx = json.loads(r3.stdout)["hookSpecificOutput"]["additionalContext"]
    assert "plans/foo.md" in ctx
    assert "re-read it from disk" in ctx


def test_fire_message_reports_no_plan_when_unresolved(git_repo):
    # No pointer file, no plans/*.md in repo → no plan resolved.
    # git_repo fixture seeds seed.txt only; no plans/ dir.
    _run(git_repo, threshold=3)
    _run(git_repo, threshold=3)
    r3 = _run(git_repo, threshold=3)

    assert r3.returncode == 0
    ctx = json.loads(r3.stdout)["hookSpecificOutput"]["additionalContext"]
    assert "No active plan pinned" in ctx


def test_cleanup_stamp_written_on_fire(git_repo):
    root = _repo_root(git_repo)
    stamp = root / ".claude" / ".dd-state" / ".last-sweep"

    _run(git_repo, threshold=3)
    _run(git_repo, threshold=3)
    _run(git_repo, threshold=3)  # fire

    assert stamp.exists(), f"expected .last-sweep stamp at {stamp}"


def test_cleanup_not_run_below_threshold(git_repo):
    root = _repo_root(git_repo)
    stamp = root / ".claude" / ".dd-state" / ".last-sweep"

    # Two calls — below threshold=3, no fire.
    r1 = _run(git_repo, threshold=3)
    r2 = _run(git_repo, threshold=3)

    assert r1.stdout.strip() == ""
    assert r2.stdout.strip() == ""
    assert not stamp.exists(), "stamp must not exist before fire"
