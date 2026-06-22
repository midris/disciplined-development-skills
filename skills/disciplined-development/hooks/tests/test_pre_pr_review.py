"""Tests for hooks/pre_pr_review.py — the pre-PR hard-block wrapper (new contract).

Subprocess-driven. The wrapper now delegates to ``external_review.py`` (not
``dd_review_runner.py``).  The test seam is ``DD_EXTERNAL_REVIEW_SCRIPT``,
pointing the wrapper at a recording Python shim that captures ``sys.argv[1:]``
and exits with a scripted code.

``DD_LOG_DIR`` isolates ``reviews.jsonl`` into a per-test temp dir for row-
asserting tests — mirror ``test_external_review.py`` / ``test_log_review.py``.

Scenarios:
  1. non-PR command (``git status``, ``ls -la``) → exit 0, shim NOT invoked,
     no review row
  2. unparseable-but-PR-shaped (``cd $REPO && gh pr create``) → exit 2, shim
     NOT invoked, stderr names ``DD_SKIP_PR_REVIEW``, one ERROR row logged
  3. parseable + delegate exit 0 → wrapper exit 0, shim got ``--cwd <cwd>``
  4. parseable + delegate non-zero → wrapper exit 2, shim marker on stderr
  5. ``DD_SKIP_PR_REVIEW=1`` → exit 0, shim NOT invoked
  6. chained cd: ``cd <other> && gh pr create`` → shim gets ``--cwd <other>``
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

HOOK = Path(__file__).resolve().parent.parent / "pre_pr_review.py"
_BASE_DIR = Path(__file__).resolve().parents[2]  # dir containing the `hooks` package


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _init_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init", "-q", "-b", "feature/x", str(repo)], check=True)
    subprocess.run(["git", "-C", str(repo), "config", "user.email", "t@t"], check=True)
    subprocess.run(["git", "-C", str(repo), "config", "user.name", "T"], check=True)
    (repo / "f.txt").write_text("x\n")
    subprocess.run(["git", "-C", str(repo), "add", "."], check=True)
    subprocess.run(["git", "-C", str(repo), "commit", "-qm", "c1"], check=True)
    return repo


def _make_shim(tmp_path: Path) -> Path:
    """Recording shim for external_review.py.

    Records sys.argv[1:] (one token per line) to $DD_SHIM_ARGV_LOG, emits a
    marker line to stdout, and exits with $DD_SHIM_EXIT (default 0).
    ``DD_HARD_BLOCK`` is intentionally NOT recorded — it must NOT be set by
    the new hook.
    """
    shim = tmp_path / "ext_review_shim.py"
    shim.write_text(
        "import os, sys\n"
        "open(os.environ['DD_SHIM_ARGV_LOG'], 'w').write('\\n'.join(sys.argv[1:]))\n"
        # Emit a marker so re-emit-on-block behavior is assertable.
        "sys.stdout.write('EXT_REVIEW_MARKER\\n')\n"
        "sys.exit(int(os.environ.get('DD_SHIM_EXIT', '0')))\n"
    )
    return shim


def _rows(log_dir: Path) -> list[dict]:
    """Read all rows from reviews.jsonl in log_dir."""
    path = log_dir / "reviews.jsonl"
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def _run(
    repo: Path,
    shim: Path,
    command: str,
    *,
    exit_code: int = 0,
    bypass: bool = False,
    log_dir: Path | None = None,
) -> tuple[subprocess.CompletedProcess, list[str] | None]:
    """Run the hook with the given Bash command payload.

    Returns (proc, argv) where argv is the list of args the shim received
    (None if the shim was not invoked).
    """
    argv_log = repo / "argv.log"
    env = dict(os.environ)
    env["DD_EXTERNAL_REVIEW_SCRIPT"] = str(shim)
    env["DD_SHIM_ARGV_LOG"] = str(argv_log)
    env["DD_SHIM_EXIT"] = str(exit_code)
    env["PYTHONPATH"] = str(_BASE_DIR) + os.pathsep + env.get("PYTHONPATH", "")
    # Must NOT be set — the new hook does NOT pass DD_HARD_BLOCK.
    env.pop("DD_HARD_BLOCK", None)
    # Suppress rolling hook log noise; tests only care about reviews.jsonl.
    if log_dir is not None:
        env["DD_LOG_DIR"] = str(log_dir)
    if bypass:
        env["DD_SKIP_PR_REVIEW"] = "1"
    else:
        env.pop("DD_SKIP_PR_REVIEW", None)
    payload = {
        "tool_name": "Bash",
        "cwd": str(repo),
        "tool_input": {"command": command},
    }
    proc = subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps(payload),
        cwd=str(repo),
        capture_output=True,
        text=True,
        env=env,
    )
    argv = argv_log.read_text().splitlines() if argv_log.exists() else None
    return proc, argv


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_non_pr_command_allows_no_row(tmp_path):
    """Non-PR commands (git status, ls) are noop: exit 0, shim not invoked,
    no reviews.jsonl row."""
    repo = _init_repo(tmp_path)
    shim = _make_shim(tmp_path)
    log_dir = tmp_path / "logs"
    log_dir.mkdir()

    for cmd in ("git status", "ls -la"):
        proc, argv = _run(repo, shim, cmd, log_dir=log_dir)
        assert proc.returncode == 0, f"{cmd!r}: expected exit 0"
        assert argv is None, f"{cmd!r}: shim must NOT be invoked"

    # No review row for any non-PR command.
    assert _rows(log_dir) == []


def test_unparseable_pr_shaped_blocks_and_logs_error_row(tmp_path):
    """``cd $REPO && gh pr create`` looks like PR but can't be parsed.

    Must: exit 2, shim NOT invoked, stderr names DD_SKIP_PR_REVIEW, and exactly
    one reviews.jsonl row with decision=ERROR / reason=unparseable /
    source=external-gate.
    """
    repo = _init_repo(tmp_path)
    shim = _make_shim(tmp_path)
    log_dir = tmp_path / "logs"
    log_dir.mkdir()

    proc, argv = _run(repo, shim, "cd $REPO && gh pr create", log_dir=log_dir)

    assert proc.returncode == 2
    assert argv is None  # shim must NOT be invoked
    assert "DD_SKIP_PR_REVIEW" in proc.stderr  # names the bypass

    rows = _rows(log_dir)
    assert len(rows) == 1, f"expected 1 review row, got {len(rows)}: {rows}"
    row = rows[0]
    assert row["decision"] == "ERROR"
    assert row["reason"] == "unparseable"
    assert row["source"] == "external-gate"


def test_parseable_clean_delegate_exit0_allows(tmp_path):
    """parseable ``gh pr create`` + delegate exit 0 → wrapper exit 0.

    Shim is invoked with ``--cwd <repo>``.
    """
    repo = _init_repo(tmp_path)
    shim = _make_shim(tmp_path)

    proc, argv = _run(repo, shim, "gh pr create", exit_code=0)

    assert proc.returncode == 0
    assert argv is not None, "shim must be invoked"
    assert "--cwd" in argv
    assert argv[argv.index("--cwd") + 1] == str(repo)


def test_parseable_block_delegate_nonzero_maps_to_exit2_reemits(tmp_path):
    """parseable ``gh pr create`` + delegate non-zero → wrapper exit 2.

    The shim's marker must appear on the wrapper's stderr (findings re-emitted
    to the model).  DD_HARD_BLOCK must NOT be set on the delegate env.
    """
    repo = _init_repo(tmp_path)
    shim = _make_shim(tmp_path)

    proc, argv = _run(repo, shim, "gh pr create", exit_code=1)

    assert proc.returncode == 2
    assert argv is not None, "shim must be invoked"
    assert "EXT_REVIEW_MARKER" in proc.stderr  # findings surfaced to the model


def test_bypass_env_allows(tmp_path):
    """DD_SKIP_PR_REVIEW=1 on any gh pr create command → exit 0, shim not invoked."""
    repo = _init_repo(tmp_path)
    shim = _make_shim(tmp_path)

    proc, argv = _run(repo, shim, "gh pr create", bypass=True)

    assert proc.returncode == 0
    assert argv is None


def test_cd_forwarded_as_cwd_to_external_review(tmp_path):
    """Chained-cd ``cd <other> && gh pr create`` → shim gets ``--cwd <other>``."""
    repo = _init_repo(tmp_path)
    shim = _make_shim(tmp_path)
    other = tmp_path / "other"
    other.mkdir()

    proc, argv = _run(repo, shim, f"cd {other} && gh pr create")

    assert argv is not None, "shim must be invoked"
    assert "--cwd" in argv
    assert argv[argv.index("--cwd") + 1] == str(other)


# ---------------------------------------------------------------------------
# In-process exception-guard tests (Commit 1 — fail-open fix)
# ---------------------------------------------------------------------------


def test_delegate_spawn_exception_fails_closed_for_pr(tmp_path, monkeypatch):
    """subprocess.run raising inside main() on a gh pr create → return 2 (fail-closed).

    Verifies the exception guard added in fix(pre-pr-gate): an unexpected raise
    during delegate spawn must NOT exit 1 (which would let the PR through);
    it must return 2 so Claude Code blocks the tool call.
    """
    import pre_pr_review

    def _raise(*args, **kwargs):
        raise OSError("EMFILE: too many open files")

    monkeypatch.setattr(pre_pr_review.subprocess, "run", _raise)
    monkeypatch.setattr(pre_pr_review, "_read_command", lambda: "gh pr create")
    # Suppress logging noise; _log_unparseable / setup may also call subprocess.run
    # (via git), which is now patched to raise — _log_unparseable already swallows
    # those; guard against logger.emit touching subprocess by patching logging_setup.
    import io
    monkeypatch.setattr(sys, "stderr", io.StringIO())

    result = pre_pr_review.main()
    assert result == 2, f"expected 2 (fail-closed), got {result}"


def test_unexpected_exception_allows_non_pr_command(tmp_path, monkeypatch):
    """An unexpected raise on the non-PR path → return 0 (gate hiccup must not block).

    Patches _read_command to raise so the exception fires before command is known;
    the handler must treat it as not-PR-shaped and return 0.
    """
    import pre_pr_review

    def _raise():
        raise RuntimeError("stdin exploded")

    monkeypatch.setattr(pre_pr_review, "_read_command", _raise)
    import io
    monkeypatch.setattr(sys, "stderr", io.StringIO())

    result = pre_pr_review.main()
    assert result == 0, f"expected 0 (non-PR exception allows), got {result}"


def test_hard_block_env_not_forwarded(tmp_path):
    """DD_HARD_BLOCK must NOT be set in the delegate environment (old contract gone)."""
    repo = _init_repo(tmp_path)
    # Use a shim that writes DD_HARD_BLOCK value to a separate log.
    argv_log = repo / "argv.log"
    hard_block_log = repo / "hard_block.log"
    shim = tmp_path / "ext_review_shim2.py"
    shim.write_text(
        "import os, sys\n"
        "open(os.environ['DD_SHIM_ARGV_LOG'], 'w').write('\\n'.join(sys.argv[1:]))\n"
        "open(os.environ['DD_HB_LOG'], 'w')"
        ".write(os.environ.get('DD_HARD_BLOCK', 'UNSET'))\n"
        "sys.exit(0)\n"
    )
    env = dict(os.environ)
    env["DD_EXTERNAL_REVIEW_SCRIPT"] = str(shim)
    env["DD_SHIM_ARGV_LOG"] = str(argv_log)
    env["DD_HB_LOG"] = str(hard_block_log)
    env["DD_SHIM_EXIT"] = "0"
    env["PYTHONPATH"] = str(_BASE_DIR) + os.pathsep + env.get("PYTHONPATH", "")
    env.pop("DD_HARD_BLOCK", None)
    env.pop("DD_SKIP_PR_REVIEW", None)
    payload = {
        "tool_name": "Bash",
        "cwd": str(repo),
        "tool_input": {"command": "gh pr create"},
    }
    subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps(payload),
        cwd=str(repo),
        capture_output=True,
        text=True,
        env=env,
    )
    # DD_HARD_BLOCK must not be set in the delegate environment
    assert hard_block_log.read_text() == "UNSET"
