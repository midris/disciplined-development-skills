"""Tests for hooks/edit_counter.py — PostToolUse edit-counter + T0 nudge.

Subprocess-driven (like test_review_nudge, test_discipline_nudge).  A synthetic
PostToolUse payload drives the hook; state-dir assertions confirm the on-disk
counter and stdout asserts the nudge envelope presence/absence.

Fixture style:
- ``_init`` creates a hermetic git repo for ``state.bump`` to key on.
- ``_run`` invokes the hook subprocess with a configurable threshold (via
  DD_CONFIG) and tool_name.
- ``_ctx`` extracts ``additionalContext`` from the envelope, or None when
  the hook is silent.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from hooks.lib import state

HOOK = Path(__file__).resolve().parent.parent / "edit_counter.py"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _ctx(r: subprocess.CompletedProcess) -> str | None:
    """Return the emitted additionalContext, or None when hook was silent."""
    if not r.stdout.strip():
        return None
    return json.loads(r.stdout)["hookSpecificOutput"]["additionalContext"]


def _git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, check=True
    )


def _init(tmp_path: Path, branch: str = "feature/x") -> Path:
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


def _run(
    repo: Path,
    *,
    tool_name: str = "Edit",
    threshold: int = 30,
    bypass: bool = False,
    payload_override: str | None = None,
) -> subprocess.CompletedProcess:
    """Run edit_counter.py as a subprocess against ``repo``.

    ``payload_override`` bypasses normal payload construction for
    malformed-payload tests.
    """
    cfg = repo / "ddcfg.json"
    cfg.write_text(json.dumps({"review_tiers": {"fast": {"nudge_threshold": threshold}}}))
    env = dict(os.environ)
    env["DD_CONFIG"] = str(cfg)
    env.pop("DD_SKIP_EDIT_COUNTER", None)
    if bypass:
        env["DD_SKIP_EDIT_COUNTER"] = "1"

    if payload_override is not None:
        stdin_text = payload_override
    else:
        payload = {
            "tool_name": tool_name,
            "cwd": str(repo),
            "tool_input": {"file_path": str(repo / "foo.py")},
            "tool_response": {},
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


def _read_edits(repo: Path, branch: str = "feature/x") -> int:
    """Read the on-disk ``edits`` counter for ``branch`` in ``repo``."""
    root = _git(repo, "rev-parse", "--show-toplevel").stdout.strip()
    return state.read(root, branch, "edits")


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_increments_edits_counter_on_edit_call(tmp_path):
    """Each Edit call increments the on-disk edits.count by 1."""
    repo = _init(tmp_path)
    assert _read_edits(repo) == 0
    r = _run(repo, tool_name="Edit", threshold=100)
    assert r.returncode == 0
    assert _read_edits(repo) == 1


def test_increments_edits_counter_on_write_call(tmp_path):
    """Each Write call also increments the on-disk edits.count by 1."""
    repo = _init(tmp_path)
    assert _read_edits(repo) == 0
    r = _run(repo, tool_name="Write", threshold=100)
    assert r.returncode == 0
    assert _read_edits(repo) == 1


def test_no_nudge_below_threshold(tmp_path):
    """No nudge emitted when post-increment count is below threshold (count 29 < 30)."""
    repo = _init(tmp_path)
    # Seed counter so next bump lands at 29 (below threshold 30).
    root = _git(repo, "rev-parse", "--show-toplevel").stdout.strip()
    for _ in range(28):
        state.bump(root, "feature/x", "edits")
    assert _read_edits(repo) == 28

    r = _run(repo, threshold=30)  # post-increment → 29
    assert r.returncode == 0
    assert _ctx(r) is None, "Expected no nudge below threshold"
    assert _read_edits(repo) == 29


def test_nudge_emitted_at_threshold(tmp_path):
    """Nudge emitted when post-increment count == threshold (29 → 30)."""
    repo = _init(tmp_path)
    root = _git(repo, "rev-parse", "--show-toplevel").stdout.strip()
    for _ in range(29):
        state.bump(root, "feature/x", "edits")
    assert _read_edits(repo) == 29

    r = _run(repo, threshold=30)  # post-increment → 30 == threshold
    assert r.returncode == 0
    ctx = _ctx(r)
    assert ctx is not None, "Expected nudge at threshold"
    assert "30" in ctx
    assert "adversarial-review skill" in ctx


def test_nudge_emitted_above_threshold(tmp_path):
    """Nudge emitted when post-increment count > threshold (30 → 31)."""
    repo = _init(tmp_path)
    root = _git(repo, "rev-parse", "--show-toplevel").stdout.strip()
    for _ in range(30):
        state.bump(root, "feature/x", "edits")
    assert _read_edits(repo) == 30

    r = _run(repo, threshold=30)  # post-increment → 31 > threshold
    assert r.returncode == 0
    ctx = _ctx(r)
    assert ctx is not None, "Expected nudge above threshold"
    assert "31" in ctx
    assert "adversarial-review skill" in ctx


def test_nudge_envelope_event_name_is_post_tool_use(tmp_path):
    """The nudge envelope hookEventName is PostToolUse."""
    repo = _init(tmp_path)
    root = _git(repo, "rev-parse", "--show-toplevel").stdout.strip()
    for _ in range(29):
        state.bump(root, "feature/x", "edits")

    r = _run(repo, threshold=30)
    payload = json.loads(r.stdout)
    assert payload["hookSpecificOutput"]["hookEventName"] == "PostToolUse"


def test_bypass_env_no_bump_no_nudge(tmp_path):
    """DD_SKIP_EDIT_COUNTER=1 → no counter bump, no nudge emitted."""
    repo = _init(tmp_path)
    root = _git(repo, "rev-parse", "--show-toplevel").stdout.strip()
    # Seed just below threshold; if bypass doesn't work, increment + nudge would fire.
    for _ in range(29):
        state.bump(root, "feature/x", "edits")

    r = _run(repo, threshold=30, bypass=True)
    assert r.returncode == 0
    # No nudge.
    assert r.stdout.strip() == "", "Expected silent output with bypass"
    # Counter unchanged (no bump).
    assert _read_edits(repo) == 29, "Counter must not increment with bypass"


def test_malformed_stdin_exits_zero_silent(tmp_path):
    """Malformed / empty stdin → exit 0, no crash, no output."""
    repo = _init(tmp_path)
    r = _run(repo, payload_override="this is not json{{{")
    assert r.returncode == 0
    assert r.stdout.strip() == ""


def test_empty_stdin_exits_zero_silent(tmp_path):
    """Empty stdin → exit 0, no crash, no output."""
    repo = _init(tmp_path)
    r = _run(repo, payload_override="")
    assert r.returncode == 0
    assert r.stdout.strip() == ""
