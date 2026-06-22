"""Tests for hooks/log_review.py — the model-callable review-logging tool.

Subprocess-driven, mirroring test_pre_pr_review.py: a hermetic temp git repo
(feature branch + identity + one commit) is the tree the tool operates on, and
``DD_LOG_DIR`` isolates ``reviews.jsonl`` into a temp dir. The tool reads
findings on stdin, appends exactly one review row, and — only on a clean (PASS)
result — folds in the cadence reset (clears the ``edits`` counter and stamps
``review.checkpoint = HEAD``). Tests assert on the exit code, the logged row,
and the on-disk state files under ``<repo>/.claude/.dd-state/``.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

LOG_REVIEW = Path(__file__).resolve().parent.parent / "log_review.py"
_BASE_DIR = LOG_REVIEW.parent.parent  # dir containing the `hooks` package


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


def _head_sha(repo: Path) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()


def _run(repo: Path, log_dir: Path, findings: str, *args: str) -> subprocess.CompletedProcess:
    env = dict(os.environ)
    env["DD_LOG_DIR"] = str(log_dir)
    return subprocess.run(
        [sys.executable, str(LOG_REVIEW), "--cwd", str(repo), *args],
        input=findings, env=env, text=True, capture_output=True,
    )


def _rows(log_dir: Path) -> list[dict]:
    path = log_dir / "reviews.jsonl"
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


# state helpers — read the on-disk per-branch state the tool writes.
def _state_dir(repo: Path) -> Path:
    # branch_slug("feature/x") -> "feature_x" (slash -> '_'); see state._branch_slug.
    return repo / ".claude" / ".dd-state" / "feature_x"


def _edits_count(repo: Path) -> int:
    f = _state_dir(repo) / "edits.count"
    return int(f.read_text().strip()) if f.exists() else 0


def _checkpoint(repo: Path) -> str | None:
    f = _state_dir(repo) / "review.checkpoint"
    return f.read_text().strip() if f.exists() else None


def _seed_edits(repo: Path, count: int) -> None:
    """Seed an unreviewed-edit count via the live state module so the
    'counters untouched' assertion is a real one, not vacuous."""
    env = dict(os.environ)
    env["PYTHONPATH"] = str(_BASE_DIR) + os.pathsep + env.get("PYTHONPATH", "")
    subprocess.run(
        [sys.executable, "-c",
         "from hooks.lib import state\n"
         "import sys\n"
         "repo, n = sys.argv[1], int(sys.argv[2])\n"
         "[state.bump(repo, 'feature/x', 'edits') for _ in range(n)]\n",
         str(repo), str(count)],
        env=env, check=True,
    )


def test_clean_stdin_passes_and_folds_reset(tmp_path):
    repo = _init_repo(tmp_path)
    log_dir = tmp_path / "logs"
    _seed_edits(repo, 3)  # there were unreviewed edits before this clean review

    proc = _run(repo, log_dir, "No findings.",
                "--source", "model-review", "--trigger", "manual")

    assert proc.returncode == 0, proc.stderr
    rows = _rows(log_dir)
    assert len(rows) == 1  # exactly one row
    assert rows[0]["decision"] == "PASS"
    # Reset-fold (Decision 2 — BOTH on a clean result):
    assert _edits_count(repo) == 0  # edits counter cleared
    assert _checkpoint(repo) == _head_sha(repo)  # checkpoint == repo HEAD


def test_blocking_stdin_logs_block_and_leaves_counters_untouched(tmp_path):
    repo = _init_repo(tmp_path)
    log_dir = tmp_path / "logs"
    _seed_edits(repo, 4)  # pre-existing unreviewed-edit count, must survive a BLOCK

    proc = _run(repo, log_dir, "- [P1] x.py:1: bug",
                "--source", "model-review", "--trigger", "cadence")

    assert proc.returncode == 0, proc.stderr
    rows = _rows(log_dir)
    assert len(rows) == 1
    assert rows[0]["decision"] == "BLOCK"
    # NEITHER counter touched on a BLOCK:
    assert _edits_count(repo) == 4  # seeded count unchanged
    assert _checkpoint(repo) is None  # no checkpoint stamped


def test_empty_stdin_exits_2_and_writes_no_row(tmp_path):
    repo = _init_repo(tmp_path)
    log_dir = tmp_path / "logs"

    proc = _run(repo, log_dir, "   \n  \t\n",
                "--source", "model-review", "--trigger", "manual")

    assert proc.returncode == 2  # usage error — a blank pipe must not log a false PASS
    assert _rows(log_dir) == []  # NO row written


def test_blank_stdin_does_not_reset_counters(tmp_path):
    repo = _init_repo(tmp_path)
    log_dir = tmp_path / "logs"
    _seed_edits(repo, 2)

    proc = _run(repo, log_dir, "",
                "--source", "model-review", "--trigger", "manual")

    assert proc.returncode == 2
    assert _edits_count(repo) == 2  # no reset on the empty-stdin guard
    assert _checkpoint(repo) is None


def test_missing_required_arg_exits_2(tmp_path):
    # argparse exits 2 on a missing required arg (--source) — usage error.
    repo = _init_repo(tmp_path)
    log_dir = tmp_path / "logs"
    proc = _run(repo, log_dir, "No findings.", "--trigger", "manual")
    assert proc.returncode == 2


def test_row_carries_source_trigger_round_context_and_findings(tmp_path):
    repo = _init_repo(tmp_path)
    log_dir = tmp_path / "logs"

    proc = _run(repo, log_dir, "- [P1] a.py:7: leak\n- [P2] b.py:3: typo",
                "--source", "external-gate", "--trigger", "pre-pr",
                "--round", "2", "--reviewer", "codex")

    assert proc.returncode == 0, proc.stderr
    row = _rows(log_dir)[0]
    assert row["source"] == "external-gate"
    assert row["trigger"] == "pre-pr"
    assert row["round"] == 2
    assert row["reviewer"] == "codex"
    # cadence-context keys (from gather_cadence_context):
    for key in ("repo", "head_sha", "branch", "base",
                "edits_count", "commits_since_checkpoint"):
        assert key in row
    assert row["branch"] == "feature/x"
    assert row["head_sha"] == _head_sha(repo)
    # structured findings[] parsed from the raw stdin text:
    assert isinstance(row["findings"], list) and len(row["findings"]) == 2
    assert row["findings"][0]["severity"] == "P1"
    assert row["findings"][0]["file"] == "a.py"
    assert row["findings"][0]["line"] == 7
    # raw text preserved verbatim as `output`:
    assert "leak" in row["output"] and "typo" in row["output"]
