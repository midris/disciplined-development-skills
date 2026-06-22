"""Tests for hooks/pre_pr_review.py — the pre-PR hard-block wrapper.

Subprocess-driven. The wrapper's whole job is detect-`gh pr create` +
extract-base/cwd + delegate to `dd_review_runner.py pre-pr` with DD_HARD_BLOCK=1,
so the tests intercept the delegation: a `DD_REVIEW_SCRIPT` env seam points
the wrapper at a recording shim (run via the same interpreter) that writes
its argv + the inherited DD_HARD_BLOCK to log files and exits with a
scripted code. Assertions then pin the forwarded flags, the hard-block env,
and exit-code propagation — without invoking a real reviewer.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

HOOK = Path(__file__).resolve().parent.parent / "pre_pr_review.py"


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
    shim = tmp_path / "dd_review_shim.py"
    shim.write_text(
        "import os, sys\n"
        "open(os.environ['DD_SHIM_ARGV_LOG'], 'w').write('\\n'.join(sys.argv[1:]))\n"
        "open(os.environ['DD_SHIM_ENV_LOG'], 'w')"
        ".write(os.environ.get('DD_HARD_BLOCK', 'UNSET'))\n"
        # Emit a marker so the wrapper's re-emit-on-block behavior is assertable.
        "sys.stdout.write('REVIEW_OUTPUT_MARKER\\n')\n"
        "sys.exit(int(os.environ.get('DD_SHIM_EXIT', '0')))\n"
    )
    return shim


def _run(repo: Path, shim: Path, command: str, *, exit_code: int = 0,
         bypass: bool = False) -> tuple[subprocess.CompletedProcess, list | None, str | None]:
    argv_log = repo / "argv.log"
    env_log = repo / "env.log"
    env = dict(os.environ)
    env["DD_REVIEW_SCRIPT"] = str(shim)
    env["DD_SHIM_ARGV_LOG"] = str(argv_log)
    env["DD_SHIM_ENV_LOG"] = str(env_log)
    env["DD_SHIM_EXIT"] = str(exit_code)
    env.pop("DD_HARD_BLOCK", None)
    if bypass:
        env["DD_SKIP_PR_REVIEW"] = "1"
    else:
        env.pop("DD_SKIP_PR_REVIEW", None)
    payload = {"tool_name": "Bash", "cwd": str(repo),
               "tool_input": {"command": command}}
    proc = subprocess.run(
        [sys.executable, str(HOOK)], input=json.dumps(payload),
        cwd=str(repo), capture_output=True, text=True, env=env,
    )
    argv = argv_log.read_text().splitlines() if argv_log.exists() else None
    hard_block = env_log.read_text() if env_log.exists() else None
    return proc, argv, hard_block


def test_non_gh_command_is_noop(tmp_path):
    repo = _init_repo(tmp_path)
    shim = _make_shim(tmp_path)
    proc, argv, _ = _run(repo, shim, "git status")
    assert proc.returncode == 0
    assert argv is None  # dd_review never invoked


def test_ls_is_noop(tmp_path):
    repo = _init_repo(tmp_path)
    shim = _make_shim(tmp_path)
    proc, argv, _ = _run(repo, shim, "ls -la")
    assert proc.returncode == 0 and argv is None


def test_bypass_env_skips_even_on_match(tmp_path):
    repo = _init_repo(tmp_path)
    shim = _make_shim(tmp_path)
    proc, argv, _ = _run(repo, shim, "gh pr create", bypass=True)
    assert proc.returncode == 0 and argv is None


def test_clean_review_delegates_with_hard_block_and_passes(tmp_path):
    repo = _init_repo(tmp_path)
    shim = _make_shim(tmp_path)
    # Clean review (dd_review exit 0) → wrapper exit 0; DD_HARD_BLOCK forwarded.
    proc, argv, hard_block = _run(repo, shim, "gh pr create", exit_code=0)
    assert proc.returncode == 0
    assert argv is not None and argv[0] == "pre-pr"
    assert hard_block == "1"


def test_blocking_review_maps_to_exit_2_and_reemits(tmp_path):
    # dd_review pre-pr returns 1 on a BLOCK / tooling error. Claude Code blocks
    # a PreToolUse tool ONLY on exit 2 — the wrapper must TRANSLATE the non-zero
    # delegate result to 2 (not propagate 1, which CC treats as a non-blocking
    # error and lets `gh pr create` through), and re-emit the review on stderr.
    repo = _init_repo(tmp_path)
    shim = _make_shim(tmp_path)
    proc, _, _ = _run(repo, shim, "gh pr create", exit_code=1)
    assert proc.returncode == 2
    assert "REVIEW_OUTPUT_MARKER" in proc.stderr  # findings surfaced to the model


def test_gh_merge_base_config_forwarded(tmp_path):
    repo = _init_repo(tmp_path)
    shim = _make_shim(tmp_path)
    # No --base on the command; the wrapper reads branch.<cur>.gh-merge-base.
    subprocess.run(
        ["git", "-C", str(repo), "config", "branch.feature/x.gh-merge-base",
         "phase-22"], check=True,
    )
    _, argv, _ = _run(repo, shim, "gh pr create")
    assert argv == ["pre-pr", "--base", "phase-22"]


def test_cd_forwarded_as_cwd(tmp_path):
    repo = _init_repo(tmp_path)
    shim = _make_shim(tmp_path)
    other = tmp_path / "other"
    other.mkdir()
    _, argv, _ = _run(repo, shim, f"cd {other} && gh pr create")
    assert "--cwd" in argv
    assert argv[argv.index("--cwd") + 1] == str(other)


def test_unexpandable_cd_fails_loud_not_open(tmp_path):
    # `cd $X && gh pr create`: the cd target is unexpandable, so the gate
    # can't tell which tree the PR is for. It must BLOCK (exit 2), not let the
    # unreviewed PR through (the fail-open bug) and not review the wrong tree.
    repo = _init_repo(tmp_path)
    shim = _make_shim(tmp_path)
    proc, argv, _ = _run(repo, shim, "cd $REPO && gh pr create")
    assert proc.returncode == 2
    assert argv is None  # dd_review NOT invoked; the wrapper blocked directly
    assert "DD_SKIP_PR_REVIEW" in proc.stderr  # names the bypass


def test_no_base_no_cd_forwards_no_flags(tmp_path):
    repo = _init_repo(tmp_path)
    shim = _make_shim(tmp_path)
    # No --base, no gh-merge-base config, no chained cd → bare delegation;
    # dd_review then defaults to fork-base + its own cwd.
    _, argv, _ = _run(repo, shim, "gh pr create")
    assert argv == ["pre-pr"]
