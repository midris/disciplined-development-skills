"""Tests for hooks/external_review.py — whole-repo verdict-driven fail-closed gate.

Harness mirrors test_dd_review_runner.py (codex shim + argv recording) and
test_log_review.py (DD_LOG_DIR + temp git repo).  The shim is a fake ``codex``
binary that:
  - records its argv (one token per line) to ``$DD_REVIEW_ARGV_LOG``,
  - writes a canned last-message to the file passed after ``-o``,
  - exits with ``$DD_REVIEW_STUB_EXIT`` (default 0).

``DD_CODEX_BIN`` points the gate at the shim; ``DD_LOG_DIR`` isolates
``reviews.jsonl`` into a per-test temp dir.

Scenarios:
  T1  clean PASS → exit 0, one PASS row, checkpoint == HEAD, edits reset
  T2  [P1] finding + BLOCK → non-zero, BLOCK row, no reset / no checkpoint
  T3  no verdict line → non-zero, ERROR row reason=no_verdict
  T4  DD_CODEX_BIN points at nonexistent → non-zero, ERROR reason=cli_missing
  T5  shim times out (inject tiny timeout via DD_CODEX_TIMEOUT override) →
        non-zero, ERROR reason=timeout
  T6  empty last-message file → non-zero, ERROR reason=empty_output
  T7  built prompt contains active-plan path AND skill pointer
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

GATE = Path(__file__).resolve().parent.parent / "external_review.py"
_BASE_DIR = Path(__file__).resolve().parents[2]  # dir containing the `hooks` package

# Shipped defaults with the new review.{reviewer,model,effort} keys.
# test_external_review needs a plan pointer so the gate can build its prompt.
DEFAULTS = {
    "branch_convention": {"trunk_branches": ["master", "main"]},
    "plans": {
        "active_plan_pointer": ".claude/active-plan",
        "fallback_glob": ["plans/*.md"],
    },
    "review": {
        "prompt_path": ".claude/skills/adversarial-review/SKILL.md",
        "reviewer": "codex",
        "model": "gpt-5.5",
        "effort": "medium",
    },
    "codex": {"pr_review_timeout_s": 30},
    "review_tiers": {
        "pre_pr": {
            "reviewer": "codex",
            "model": "gpt-5.5",
            "default_effort": "medium",
        },
    },
    "logging": {"enabled": True, "dir": None},
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _init_repo(tmp_path: Path) -> Path:
    """Create a minimal git repo on branch feature/x with one commit."""
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init", "-q", "-b", "feature/x", str(repo)], check=True)
    subprocess.run(["git", "-C", str(repo), "config", "user.email", "t@t"], check=True)
    subprocess.run(["git", "-C", str(repo), "config", "user.name", "T"], check=True)
    (repo / "f.txt").write_text("hello\n")
    subprocess.run(["git", "-C", str(repo), "add", "."], check=True)
    subprocess.run(["git", "-C", str(repo), "commit", "-qm", "c1"], check=True)
    return repo


def _head_sha(repo: Path) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()


def _make_shim(binroot: Path) -> None:
    """Write a fake ``codex`` binary.

    The shim:
      1. Records its argv (one token per line) to ``$DD_REVIEW_ARGV_LOG`` when set.
      2. Finds the ``-o <path>`` argument and writes ``$DD_REVIEW_STUB_STDOUT``
         (default ``DD-VERDICT: PASS``) to that file.
      3. Exits with ``$DD_REVIEW_STUB_EXIT`` (default 0).
    """
    binroot.mkdir(parents=True, exist_ok=True)
    shim = binroot / "codex"
    shim.write_text(
        "#!/bin/sh\n"
        # Record argv
        'if [ -n "${DD_REVIEW_ARGV_LOG:-}" ]; then\n'
        '  printf \'%s\\n\' "$@" > "$DD_REVIEW_ARGV_LOG"\n'
        "fi\n"
        # Find -o <path> and write the stub last-message to it.
        # Walk argv tokens; when we see "-o", the next token is the output file.
        "found_o=0\n"
        "output_file=''\n"
        "for arg in \"$@\"; do\n"
        "  if [ \"$found_o\" = '1' ]; then\n"
        "    output_file=\"$arg\"\n"
        "    found_o=0\n"
        "  fi\n"
        "  if [ \"$arg\" = '-o' ]; then\n"
        "    found_o=1\n"
        "  fi\n"
        "done\n"
        'stub="${DD_REVIEW_STUB_STDOUT:-DD-VERDICT: PASS}"\n'
        "if [ -n \"$output_file\" ]; then\n"
        '  printf \'%s\' "$stub" > "$output_file"\n'
        "fi\n"
        'exit "${DD_REVIEW_STUB_EXIT:-0}"\n'
    )
    shim.chmod(0o755)


def _base_env(tmp_path: Path, defaults_path: Path, binroot: Path, log_dir: Path) -> dict:
    """Return base environment for running external_review.py as a subprocess."""
    env = {
        **os.environ,
        "DD_DEFAULTS": str(defaults_path),
        "DD_CONFIG": "",
        "DD_LOG_DIR": str(log_dir),
        "DD_CODEX_BIN": str(binroot / "codex"),
        "PYTHONPATH": str(_BASE_DIR),
        "GIT_CONFIG_GLOBAL": "/dev/null",
        "GIT_AUTHOR_NAME": "Test",
        "GIT_AUTHOR_EMAIL": "t@t",
        "GIT_COMMITTER_NAME": "Test",
        "GIT_COMMITTER_EMAIL": "t@t",
    }
    # Strip any inherited stub knobs.
    for k in ("DD_REVIEW_STUB_STDOUT", "DD_REVIEW_STUB_EXIT", "DD_REVIEW_ARGV_LOG",
              "DD_CODEX_TIMEOUT"):
        env.pop(k, None)
    return env


def _run(env: dict, repo: Path,
         stub_stdout: str = "DD-VERDICT: PASS",
         stub_exit: int = 0,
         extra: dict | None = None) -> subprocess.CompletedProcess:
    full = {**env,
            "DD_REVIEW_STUB_STDOUT": stub_stdout,
            "DD_REVIEW_STUB_EXIT": str(stub_exit)}
    if extra:
        full.update(extra)
    return subprocess.run(
        [sys.executable, str(GATE), "--cwd", str(repo)],
        capture_output=True, text=True, env=full,
    )


def _argv_log(env: dict, repo: Path, tmp_path: Path,
              stub_stdout: str = "DD-VERDICT: PASS",
              stub_exit: int = 0) -> tuple[subprocess.CompletedProcess, list[str]]:
    log = tmp_path / "argv.log"
    e = {**env,
         "DD_REVIEW_ARGV_LOG": str(log),
         "DD_REVIEW_STUB_STDOUT": stub_stdout,
         "DD_REVIEW_STUB_EXIT": str(stub_exit)}
    proc = subprocess.run(
        [sys.executable, str(GATE), "--cwd", str(repo)],
        capture_output=True, text=True, env=e,
    )
    argv = log.read_text().splitlines() if log.exists() else []
    return proc, argv


def _rows(log_dir: Path) -> list[dict]:
    path = log_dir / "reviews.jsonl"
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


# Per-branch state helpers (branch is feature/x → slug feature_x).
def _state_dir(repo: Path) -> Path:
    return repo / ".claude" / ".dd-state" / "feature_x"


def _edits_count(repo: Path) -> int:
    f = _state_dir(repo) / "edits.count"
    return int(f.read_text().strip()) if f.exists() else 0


def _checkpoint(repo: Path) -> str | None:
    f = _state_dir(repo) / "review.checkpoint"
    return f.read_text().strip() if f.exists() else None


def _seed_edits(repo: Path, count: int, base_dir: Path) -> None:
    """Seed an unreviewed-edit count via the live state module."""
    env = dict(os.environ)
    env["PYTHONPATH"] = str(base_dir) + os.pathsep + env.get("PYTHONPATH", "")
    subprocess.run(
        [sys.executable, "-c",
         "from hooks.lib import state\n"
         "import sys\n"
         "repo, n = sys.argv[1], int(sys.argv[2])\n"
         "[state.bump(repo, 'feature/x', 'edits') for _ in range(n)]\n",
         str(repo), str(count)],
        env=env, check=True,
    )


# ---------------------------------------------------------------------------
# Fixture
# ---------------------------------------------------------------------------


import pytest


@pytest.fixture
def gate_env(tmp_path):
    """Return (env, repo, log_dir) with a feature repo + codex shim + isolated log dir."""
    defaults_path = tmp_path / "defaults.json"
    defaults_path.write_text(json.dumps(DEFAULTS))

    binroot = tmp_path / "bin"
    _make_shim(binroot)

    log_dir = tmp_path / "logs"

    repo = _init_repo(tmp_path)

    # Create the review skill file that the prompt pointer references.
    skill_dir = repo / ".claude" / "skills" / "adversarial-review"
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text("# Adversarial review\nReview the repo.\n")

    # Create an active plan so the prompt builder can include it.
    plans_dir = repo / "plans"
    plans_dir.mkdir()
    plan_file = plans_dir / "2026-06-01-test-plan.md"
    plan_file.write_text("# Test plan\n- [ ] task A\n")

    env = _base_env(tmp_path, defaults_path, binroot, log_dir)
    return env, repo, log_dir


# ---------------------------------------------------------------------------
# T1 — clean PASS
# ---------------------------------------------------------------------------


def test_pass_verdict_exits_zero_logs_pass_stamps_state(gate_env, tmp_path):
    """Clean run: exit 0, one PASS row, review.checkpoint == HEAD, edits reset.

    This is the primary happy-path contract for the fail-closed gate.
    """
    env, repo, log_dir = gate_env
    _seed_edits(repo, 3, _BASE_DIR)

    proc = _run(env, repo, stub_stdout="No findings.\nDD-VERDICT: PASS")

    assert proc.returncode == 0, proc.stderr
    rows = _rows(log_dir)
    assert len(rows) == 1
    row = rows[0]
    assert row["decision"] == "PASS"
    assert row["source"] == "external-gate"
    assert row["trigger"] == "gate:pre-pr"
    assert row["reviewer"] == "codex"
    # State reset: edits cleared AND checkpoint stamped.
    assert _edits_count(repo) == 0
    assert _checkpoint(repo) == _head_sha(repo)


# ---------------------------------------------------------------------------
# T2 — BLOCK verdict
# ---------------------------------------------------------------------------


def test_block_verdict_exits_nonzero_logs_block_no_state_change(gate_env, tmp_path):
    """P1 finding + BLOCK verdict: non-zero exit, BLOCK row, no state changes.

    Verifies the fail-closed contract: a BLOCK never resets counters or stamps
    the checkpoint.
    """
    env, repo, log_dir = gate_env
    _seed_edits(repo, 2, _BASE_DIR)

    proc = _run(env, repo,
                stub_stdout="- [P1] hooks/foo.py:10: bad thing\nDD-VERDICT: BLOCK")

    assert proc.returncode != 0
    rows = _rows(log_dir)
    assert len(rows) == 1
    assert rows[0]["decision"] == "BLOCK"
    assert rows[0]["p1"] == 1
    # No state change on BLOCK.
    assert _edits_count(repo) == 2
    assert _checkpoint(repo) is None


# ---------------------------------------------------------------------------
# T3 — no verdict line
# ---------------------------------------------------------------------------


def test_no_verdict_line_exits_nonzero_logs_error_no_verdict(gate_env):
    """Output with no DD-VERDICT line → ERROR row with reason=no_verdict, non-zero exit."""
    env, repo, log_dir = gate_env

    proc = _run(env, repo, stub_stdout="Some output but no verdict line here.")

    assert proc.returncode != 0
    rows = _rows(log_dir)
    assert len(rows) == 1
    assert rows[0]["decision"] == "ERROR"
    assert rows[0].get("reason") == "no_verdict"


# ---------------------------------------------------------------------------
# T4 — codex binary missing
# ---------------------------------------------------------------------------


def test_missing_codex_binary_exits_nonzero_logs_error_cli_missing(gate_env, tmp_path):
    """DD_CODEX_BIN points at a nonexistent path → ERROR reason=cli_missing."""
    env, repo, log_dir = gate_env
    env = {**env, "DD_CODEX_BIN": str(tmp_path / "no_such_codex")}

    proc = _run(env, repo)

    assert proc.returncode != 0
    rows = _rows(log_dir)
    assert len(rows) == 1
    assert rows[0]["decision"] == "ERROR"
    assert rows[0].get("reason") == "cli_missing"


# ---------------------------------------------------------------------------
# T5 — timeout
# ---------------------------------------------------------------------------


def test_timeout_exits_nonzero_logs_error_timeout(gate_env, tmp_path):
    """Codex shim that sleeps past a tiny injected timeout → ERROR reason=timeout.

    We override DD_CODEX_TIMEOUT (seconds as float/int) so the gate uses a
    sub-second budget; the shim sleeps longer than that.
    """
    env, repo, log_dir = gate_env

    # Replace the shim with one that sleeps.
    sleeping_shim = tmp_path / "bin2" / "codex"
    sleeping_shim.parent.mkdir()
    sleeping_shim.write_text(
        "#!/bin/sh\n"
        # Write nothing to -o (gate must handle missing file gracefully too).
        "sleep 10\n"
        'exit 0\n'
    )
    sleeping_shim.chmod(0o755)
    env = {**env, "DD_CODEX_BIN": str(sleeping_shim), "DD_CODEX_TIMEOUT": "0.2"}

    proc = subprocess.run(
        [sys.executable, str(GATE), "--cwd", str(repo)],
        capture_output=True, text=True, env=env,
        timeout=15,  # safety net — test itself must not hang
    )

    assert proc.returncode != 0
    rows = _rows(log_dir)
    assert len(rows) == 1
    assert rows[0]["decision"] == "ERROR"
    assert rows[0].get("reason") == "timeout"


# ---------------------------------------------------------------------------
# T6 — empty last-message file
# ---------------------------------------------------------------------------


def test_empty_last_message_exits_nonzero_logs_error_empty_output(gate_env, tmp_path):
    """Shim that writes an empty string to -o → ERROR reason=empty_output."""
    env, repo, log_dir = gate_env

    # Shim that writes nothing (empty) to the -o file.
    empty_shim = tmp_path / "bin3" / "codex"
    empty_shim.parent.mkdir()
    empty_shim.write_text(
        "#!/bin/sh\n"
        "found_o=0\n"
        "output_file=''\n"
        "for arg in \"$@\"; do\n"
        "  if [ \"$found_o\" = '1' ]; then\n"
        "    output_file=\"$arg\"\n"
        "    found_o=0\n"
        "  fi\n"
        "  if [ \"$arg\" = '-o' ]; then\n"
        "    found_o=1\n"
        "  fi\n"
        "done\n"
        # Write empty content
        "if [ -n \"$output_file\" ]; then\n"
        "  printf '' > \"$output_file\"\n"
        "fi\n"
        "exit 0\n"
    )
    empty_shim.chmod(0o755)
    env = {**env, "DD_CODEX_BIN": str(empty_shim)}

    proc = _run(env, repo)

    assert proc.returncode != 0
    rows = _rows(log_dir)
    assert len(rows) == 1
    assert rows[0]["decision"] == "ERROR"
    assert rows[0].get("reason") == "empty_output"


# ---------------------------------------------------------------------------
# T7 — prompt contains plan path AND skill pointer
# ---------------------------------------------------------------------------


def test_built_prompt_contains_plan_path_and_skill_pointer(gate_env, tmp_path):
    """The argv the shim records must contain the active-plan path and the
    skill pointer path — proving the gate builds a deterministic, plan-anchored
    prompt without reading the skill body itself.
    """
    env, repo, log_dir = gate_env

    proc, argv = _argv_log(env, repo, tmp_path)

    # The gate must have passed a prompt string to codex exec; find it.
    # The prompt is the final positional argument to `codex exec`.
    prompt_arg = ""
    for i, token in enumerate(argv):
        if token == "--":
            # Everything after -- is the prompt (unlikely shape but guard it)
            prompt_arg = " ".join(argv[i + 1:])
            break
    # If no --, the prompt is the last non-flag token following exec flags.
    # We collect the full argv and look for the plan path / skill path anywhere
    # in a token that is not a flag value.
    full_argv_text = "\n".join(argv)

    # The skill pointer path must appear somewhere in the argv.
    assert ".claude/skills/adversarial-review/SKILL.md" in full_argv_text, (
        f"skill pointer not in argv: {argv}"
    )
    # The plan path must appear somewhere in the argv.
    plan_path_fragment = "plans/"
    assert plan_path_fragment in full_argv_text, (
        f"plan path not in argv: {argv}"
    )


# ---------------------------------------------------------------------------
# T8 — abnormal codex exit (non-zero exit code) must fail closed
# ---------------------------------------------------------------------------


def test_nonzero_codex_exit_fails_closed_even_with_pass_verdict(gate_env, tmp_path):
    """codex exits non-zero but wrote ``DD-VERDICT: PASS`` → fail closed (D3).

    ``Runner.run()`` returns ``exit_reason='ok'`` for any process that spawned and
    completed, REGARDLESS of its exit code.  A non-zero codex exit means the
    reviewer errored (auth failure, partial run, outage), so its last-message
    verdict cannot be trusted: the gate must log ERROR/outage and block — never
    stamp state — even though a PASS line sits in the ``-o`` file.
    """
    env, repo, log_dir = gate_env
    _seed_edits(repo, 2, _BASE_DIR)

    proc = _run(env, repo, stub_stdout="No findings.\nDD-VERDICT: PASS", stub_exit=1)

    assert proc.returncode != 0, proc.stdout + proc.stderr
    rows = _rows(log_dir)
    assert len(rows) == 1
    assert rows[0]["decision"] == "ERROR"
    assert rows[0].get("reason") == "outage"
    # The PASS verdict in the -o file must NOT have stamped state.
    assert _edits_count(repo) == 2
    assert _checkpoint(repo) is None
