"""Tests for hooks/dd_review_runner.py — tiered review engine (fork-base + checkpoint).

Harness mechanics (reused from the legacy test, assertions rewritten for the
fork-base + checkpoint contract):

  * ``review_env`` — a sandbox holding a synthetic ``dd-defaults.json`` (wired
    via ``DD_DEFAULTS``) plus real ``claude`` / ``codex`` shim binaries on a
    per-test ``PATH`` dir. The engine dispatches the reviewer through
    ``claude_runner.Runner`` (a real ``Popen``), so the shims must be genuine
    executables — not monkeypatched. Each shim records its argv (one token per
    line) to ``$DD_REVIEW_ARGV_LOG`` and its stdin to ``$DD_REVIEW_STDIN_LOG``,
    then prints scripted stdout / exits with a scripted code, so tests can
    assert the exact flags + payload the engine passed.
  * ``feature_repo`` — a git repo with a ``master`` trunk plus a checked-out
    ``feature/x`` carrying one extra commit, exercising fork-base resolution and
    checkpoints against a real merge-base.

The engine is run as a subprocess (``python3 dd_review_runner.py ...``) so ``--cwd``,
``DD_HARD_BLOCK`` and the real ``Runner`` dispatch are exercised end-to-end.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from hooks.lib import state

HOOK = Path(__file__).resolve().parent.parent / "dd_review_runner.py"
_BASE_DIR = Path(__file__).resolve().parents[2]

DEFAULTS = {
    "branch_convention": {"trunk_branches": ["master", "main"]},
    "plans": {
        "active_plan_pointer": ".claude/active-plan",
        "fallback_glob": ["plans/*.md"],
    },
    "review": {"prompt_path": ".claude/skills/adversarial-review/SKILL.md"},
    "codex": {"pr_review_timeout_s": 30},
    "review_tiers": {
        "regular": {
            "reviewer": "claude",
            "model": "opus",
            "default_effort": "medium",
        },
        "cold_read_escalation": {
            "reviewer": "claude",
            "model": "opus",
            "default_effort": "high",
        },
        "pre_pr": {
            "reviewer": "codex",
            "model": "gpt-5.5",
            "default_effort": "medium",
        },
    },
    "strategy_selector": {
        "pre_stuff_max_bytes": 524288,
        "high_effort_min_bytes": 51200,
    },
}


def _git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def _make_shims(binroot: Path) -> None:
    """Write claude + codex shim executables that record argv + stdin and emit
    scripted stdout / exit code from env vars."""
    binroot.mkdir(parents=True, exist_ok=True)
    for name in ("claude", "codex"):
        target = binroot / name
        target.write_text(
            "#!/bin/sh\n"
            'if [ -n "${DD_REVIEW_ARGV_LOG:-}" ]; then\n'
            '  printf \'%s\\n\' "$@" > "$DD_REVIEW_ARGV_LOG"\n'
            "fi\n"
            # Record the reviewer's physical cwd (`pwd -P` ignores a stale
            # inherited $PWD) so tests can assert --cwd actually retargeted the
            # reviewer process, not just the diff base.
            'if [ -n "${DD_REVIEW_CWD_LOG:-}" ]; then\n'
            '  pwd -P > "$DD_REVIEW_CWD_LOG"\n'
            "fi\n"
            'if [ -n "${DD_REVIEW_STDIN_LOG:-}" ]; then\n'
            '  cat > "$DD_REVIEW_STDIN_LOG"\n'
            "else\n"
            "  cat > /dev/null\n"
            "fi\n"
            'printf \'%s\' "${DD_REVIEW_STUB_STDOUT:-No findings.}"\n'
            'exit "${DD_REVIEW_STUB_EXIT:-0}"\n'
        )
        target.chmod(0o755)


@pytest.fixture
def review_env(tmp_path):
    """Return ``(env, repo, defaults_path)`` with a feature branch + shims."""
    defaults = tmp_path / "defaults.json"
    defaults.write_text(json.dumps(DEFAULTS))

    binroot = tmp_path / "bin"
    _make_shims(binroot)

    env = {
        **os.environ,
        "DD_DEFAULTS": str(defaults),
        "DD_CONFIG": "",
        # Per-test log dir (overrides the conftest /tmp default) so each test's
        # reviews.jsonl is isolated and assertable.
        "DD_LOG_DIR": str(tmp_path / "ddlogs"),
        "PATH": f"{binroot}:{os.environ.get('PATH', '')}",
        "PYTHONPATH": str(_BASE_DIR),
        "GIT_CONFIG_GLOBAL": "/dev/null",
        "GIT_AUTHOR_NAME": "Test",
        "GIT_AUTHOR_EMAIL": "t@t",
        "GIT_COMMITTER_NAME": "Test",
        "GIT_COMMITTER_EMAIL": "t@t",
    }
    # Strip any inherited stub knobs so each test sets its own.
    for k in (
        "DD_REVIEW_STUB_STDOUT",
        "DD_REVIEW_STUB_EXIT",
        "DD_REVIEW_ARGV_LOG",
        "DD_REVIEW_STDIN_LOG",
        "DD_HARD_BLOCK",
    ):
        env.pop(k, None)

    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(
        ["git", "init", "-q", "-b", "master", str(repo)],
        check=True,
        capture_output=True,
    )
    _git(repo, "config", "user.email", "t@t")
    _git(repo, "config", "user.name", "Test")
    # Adversarial-review SKILL the claude/codex-stuffed prompt path needs.
    skill = repo / ".claude" / "skills" / "adversarial-review"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text("# Adversarial review\nReview the diff.\n")
    (repo / "f.txt").write_text("one\n")
    _git(repo, "add", ".")
    _git(repo, "commit", "-q", "-m", "c1")
    _git(repo, "checkout", "-q", "-b", "feature/x")
    (repo / "g.txt").write_text("two\n")
    _git(repo, "add", "g.txt")
    _git(repo, "commit", "-q", "-m", "c2")
    return env, repo, defaults


@pytest.fixture
def feature_repo(review_env):
    return review_env[1]


def _run(env, repo, args, stub_stdout="No findings.", stub_exit=0, extra=None):
    full = {**env, "DD_REVIEW_STUB_STDOUT": stub_stdout,
            "DD_REVIEW_STUB_EXIT": str(stub_exit)}
    if extra:
        full.update(extra)

    def _spawn():
        return subprocess.run(
            [sys.executable, str(HOOK), *args],
            capture_output=True,
            text=True,
            env=full,
            cwd=str(repo),
        )

    # The first subprocess a test spawns in this sandbox intermittently aborts
    # with a spurious "... not found" BEFORE the engine reaches its real logic
    # (a known flake of the local auto-mode classifier — verified: an identical
    # immediate re-spawn always succeeds). The discriminator is the engine's own
    # error banner: every real engine error (incl. prompt_missing) prints
    # "[dd_review <tier>] ERROR — ...", whereas the pre-engine classifier abort
    # never does. Retry once only when the failure carries NO banner, so a
    # genuine engine error is never retried/masked.
    proc = _spawn()
    if (
        proc.returncode != 0
        and "not found" in proc.stderr
        and "[dd_review" not in proc.stderr
    ):
        proc = _spawn()
    return proc


def _argv_log(env, repo, args, stub_stdout="No findings.", stub_exit=0,
              extra=None):
    log = repo / "argv.log"
    stdin_log = repo / "stdin.log"
    e = {"DD_REVIEW_ARGV_LOG": str(log), "DD_REVIEW_STDIN_LOG": str(stdin_log)}
    if extra:
        e.update(extra)
    proc = _run(env, repo, args, stub_stdout, stub_exit, extra=e)
    argv = log.read_text().splitlines() if log.exists() else []
    stdin = stdin_log.read_text() if stdin_log.exists() else ""
    return proc, argv, stdin


def _fork_base(repo):
    return state.resolve_fork_base(str(repo), ["master", "main"])


def _diff_base_in_argv(argv):
    """Return the ``--base`` value codex was launched with, or None."""
    if "--base" in argv:
        return argv[argv.index("--base") + 1]
    return None


def _force_fetched(defaults):
    """Lower the stuff cutoff so any non-empty diff dispatches fetched
    (the strategy that surfaces the base in argv for codex / the
    fetch-instructions block for claude)."""
    cfg = json.loads(defaults.read_text())
    cfg["strategy_selector"]["pre_stuff_max_bytes"] = 1
    defaults.write_text(json.dumps(cfg))


# ---------------------------------------------------------------------------
# B1 — tier CLI + fork-base resolution
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("tier", ["regular", "cold-read", "pre-pr"])
def test_each_tier_dispatches_against_fork_base(review_env, tier):
    """Every tier resolves its diff base to the fork base (merge-base vs trunk).

    Forced into fetched strategy so the base is observable in argv (codex
    ``--base <ref>``) / the fetch-instructions block (claude ``Review base``).
    """
    env, repo, defaults = review_env
    _force_fetched(defaults)
    fork = _fork_base(repo)
    proc, argv, stdin = _argv_log(env, repo, [tier])
    assert proc.returncode == 0, proc.stderr
    # regular/cold-read are claude (base in the stdin prompt); pre-pr is codex
    # (base in argv). Both must reference the fork base.
    if tier == "pre-pr":
        assert _diff_base_in_argv(argv) == fork
    else:
        assert f"Review base: `{fork}`" in stdin


def test_unknown_tier_exits_2_with_usage(review_env):
    env, repo, _ = review_env
    proc = _run(env, repo, ["bogus"])
    assert proc.returncode == 2
    assert "usage" in proc.stderr.lower()


@pytest.mark.parametrize("tier", ["regular", "cold-read"])
def test_base_rejected_on_non_prepr_tiers(review_env, tier):
    env, repo, _ = review_env
    proc = _run(env, repo, [tier, "--base", "master"])
    assert proc.returncode == 2
    assert "--base" in proc.stderr


def test_base_honored_on_prepr(review_env):
    """Explicit --base on pre-pr overrides fork-base resolution.

    Forced into fetched strategy so the base reaches codex argv. A third
    feature commit is added so HEAD~1 resolves to a commit that is NOT the
    fork base — otherwise the override and the default would coincide and the
    test couldn't distinguish them.
    """
    env, repo, defaults = review_env
    _force_fetched(defaults)
    (repo / "h.txt").write_text("three\n")
    _git(repo, "add", "h.txt")
    _git(repo, "commit", "-q", "-m", "c3")
    head_tilde = _git(repo, "rev-parse", "HEAD~1")  # = c2, not the fork base
    proc, argv, _ = _argv_log(env, repo, ["pre-pr", "--base", "HEAD~1"])
    assert proc.returncode == 0, proc.stderr
    assert _diff_base_in_argv(argv) == "HEAD~1"
    # Sanity: HEAD~1 differs from the fork base, so honoring --base is a real
    # override (not an accidental match with the default fork-base resolution).
    assert head_tilde != _fork_base(repo)


def test_trunk_iteration_resolves_main_only_repo(tmp_path, review_env):
    """A repo whose only trunk is ``main`` still resolves a fork base."""
    env, _, _ = review_env
    repo = tmp_path / "mainrepo"
    repo.mkdir()
    subprocess.run(
        ["git", "init", "-q", "-b", "main", str(repo)],
        check=True,
        capture_output=True,
    )
    _git(repo, "config", "user.email", "t@t")
    _git(repo, "config", "user.name", "Test")
    skill = repo / ".claude" / "skills" / "adversarial-review"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text("# rev\n")
    (repo / "f.txt").write_text("one\n")
    _git(repo, "add", ".")
    _git(repo, "commit", "-q", "-m", "c1")
    _git(repo, "checkout", "-q", "-b", "feature/y")
    (repo / "g.txt").write_text("two\n")
    _git(repo, "add", "g.txt")
    _git(repo, "commit", "-q", "-m", "c2")

    fork = state.resolve_fork_base(str(repo), ["master", "main"])
    assert fork is not None
    proc, _, stdin = _argv_log(env, repo, ["regular"])
    assert proc.returncode == 0, proc.stderr
    assert f"Review base: `{fork}`" in stdin


def test_empty_diff_clean_exit_no_runner(review_env):
    """HEAD == fork base → clean exit 0, no reviewer dispatched."""
    env, repo, _ = review_env
    _git(repo, "reset", "--hard", "master")
    proc, argv, _ = _argv_log(env, repo, ["regular"])
    assert proc.returncode == 0
    assert argv == []  # shim never ran
    assert "nothing to review" in proc.stdout


# ---------------------------------------------------------------------------
# B2 — reviewer dispatch + per-knob argv
# ---------------------------------------------------------------------------


def test_tier_model_lands_model_flag(review_env):
    """regular tier (claude/opus) lands ``--model opus``."""
    env, repo, _ = review_env
    proc, argv, _ = _argv_log(env, repo, ["regular"])
    assert proc.returncode == 0, proc.stderr
    assert "--model" in argv
    assert argv[argv.index("--model") + 1] == "opus"


def test_tier_default_effort_lands_effort_flag(review_env):
    """cold-read tier (default_effort=high) lands ``--effort high``."""
    env, repo, _ = review_env
    proc, argv, _ = _argv_log(env, repo, ["cold-read"])
    assert proc.returncode == 0, proc.stderr
    assert "--effort" in argv
    assert argv[argv.index("--effort") + 1] == "high"


def test_codex_model_and_effort_overrides(review_env):
    """pre-pr tier (codex) lands ``-c model=...`` / ``-c model_reasoning_effort=...``
    AND every ``-c`` follows the ``review`` subcommand.

    Position is load-bearing: codex silently drops ``-c`` overrides placed
    before the subcommand (see ``review_prompt.codex_runner_argv``'s
    inline comment). A pure substring check would let a refactor reshuffle
    ``codex -c ... review ...`` through without the test catching it."""
    env, repo, _ = review_env
    proc, argv, _ = _argv_log(env, repo, ["pre-pr"])
    assert proc.returncode == 0, proc.stderr
    joined = "\n".join(argv)
    assert 'model="gpt-5.5"' in joined
    assert 'model_reasoning_effort="medium"' in joined
    # Shim records args-after-binary, so argv[0] is the codex subcommand.
    assert argv[0] == "review", f"expected first arg to be 'review', got {argv!r}"
    review_idx = argv.index("review")
    for i, tok in enumerate(argv):
        if tok == "-c":
            assert i > review_idx, (
                f"-c at index {i} precedes review at {review_idx}: {argv!r}"
            )


def test_codex_stuffed_reads_diff_from_stdin(review_env):
    """codex stuffed (small diff): argv ends in ``-`` and the diff is on stdin."""
    env, repo, _ = review_env
    proc, argv, stdin = _argv_log(env, repo, ["pre-pr"])
    assert proc.returncode == 0, proc.stderr
    assert argv[-1] == "-"
    assert "g.txt" in stdin  # the diff body the engine piped in


def test_selector_picks_stuffed_at_small_diff(review_env):
    """Small diff → claude stuffed: diff embedded in prompt, no git-diff tool."""
    env, repo, _ = review_env
    proc, argv, stdin = _argv_log(env, repo, ["regular"])
    assert proc.returncode == 0, proc.stderr
    # Stuffed embeds the diff body inside a ```diff fence.
    assert "```diff" in stdin
    assert "+two" in stdin  # the actual diff hunk
    # CLAUDE_STUFFED_TOOLS drops Bash(git diff:*).
    tools = argv[argv.index("--tools") + 1]
    assert "Bash(git diff:*)" not in tools
    # Prompt instructions and tool allowlist must agree: in stuffed mode the
    # reviewer should NOT be told to "fetch them yourself" (git diff is denied)
    # — that contradicts the embedded diff and would trigger a denied tool call.
    assert "Fetch them yourself" not in stdin
    # Positive: stuffed mode should orient the reviewer to the embedded diff.
    assert "embedded" in stdin.lower() or "pre-stuffed" in stdin.lower()


def test_selector_picks_fetched_at_large_diff(review_env):
    """Large diff → claude fetched: git-diff tool allowlisted, no embedded diff."""
    env, repo, defaults = review_env
    _force_fetched(defaults)
    proc, argv, stdin = _argv_log(env, repo, ["regular"])
    assert proc.returncode == 0, proc.stderr
    # Fetched does NOT embed the diff body; it instructs the reviewer to fetch.
    assert "```diff" not in stdin
    assert "Fetch them yourself" in stdin
    tools = argv[argv.index("--tools") + 1]
    assert "Bash(git diff:*)" in tools


def test_cli_missing_errors(review_env, tmp_path):
    """Reviewer CLI absent from PATH → operational error exit 1, no dispatch.

    Build an isolated bin dir holding only a ``git`` symlink so neither the
    shim nor any real ``claude`` on the host PATH is reachable.
    """
    env, repo, _ = review_env
    isolated = tmp_path / "onlygit"
    isolated.mkdir()
    (isolated / "git").symlink_to(shutil.which("git"))
    env = {**env, "PATH": str(isolated)}
    proc = _run(env, repo, ["regular"])
    assert proc.returncode == 1  # operational failure (not a usage error)
    assert "not found on PATH" in proc.stderr


def test_empty_reviewer_stdout_errors(review_env):
    """Whitespace-only reviewer stdout → operational error exit 1."""
    env, repo, _ = review_env
    proc = _run(env, repo, ["regular"], stub_stdout="   \n\t\n")
    assert proc.returncode == 1  # operational failure (not a usage error)
    assert "no output" in proc.stderr


# ---------------------------------------------------------------------------
# B3 — checkpoint write + hard-block + Delta-4 (no history writer)
# ---------------------------------------------------------------------------


def test_clean_pass_writes_checkpoint(review_env):
    """A clean regular pass checkpoints HEAD; commits_since_checkpoint reads 0."""
    env, repo, _ = review_env
    proc = _run(env, repo, ["regular"], stub_stdout="[P3] nit only.\n")
    assert proc.returncode == 0, proc.stderr
    head = _git(repo, "rev-parse", "HEAD")
    assert state.commits_since_checkpoint(str(repo), "feature/x") == 0
    cp = repo / ".claude" / ".dd-state" / "feature_x" / "review.checkpoint"
    assert cp.read_text().strip() == head


def test_block_pass_does_not_write_checkpoint(review_env):
    """A blocking pass (P1 finding) must NOT write the checkpoint."""
    env, repo, _ = review_env
    proc = _run(env, repo, ["regular"], stub_stdout="[P1] broken auth at f.go:12\n")
    assert proc.returncode == 0  # regular advisory regardless of findings
    assert state.commits_since_checkpoint(str(repo), "feature/x") is None
    cp = repo / ".claude" / ".dd-state" / "feature_x" / "review.checkpoint"
    assert not cp.exists()


def test_prepr_clean_exits_0(review_env):
    env, repo, _ = review_env
    proc = _run(env, repo, ["pre-pr"], stub_stdout="[P3] trivial nit\n")
    assert proc.returncode == 0, proc.stderr


def test_prepr_findings_with_hard_block_returns_nonzero(review_env):
    env, repo, _ = review_env
    proc = _run(
        env, repo, ["pre-pr"],
        stub_stdout="[P0] data loss in delete path\n",
        extra={"DD_HARD_BLOCK": "1"},
    )
    assert proc.returncode == 1


def test_prepr_findings_without_hard_block_is_advisory(review_env):
    env, repo, _ = review_env
    proc = _run(env, repo, ["pre-pr"], stub_stdout="[P0] data loss in delete path\n")
    assert proc.returncode == 0


@pytest.mark.parametrize("tier", ["regular", "cold-read", "pre-pr"])
def test_no_review_history_log_written(review_env, tier):
    """Delta 4: no tier may create a .review-history.log (clean or blocking)."""
    env, repo, _ = review_env
    _run(env, repo, [tier], stub_stdout="[P0] blocking\n[P3] nit\n")
    assert not (repo / ".review-history.log").exists()
    assert not (repo / ".claude" / ".review-history.log").exists()


# ---------------------------------------------------------------------------
# Part B review fixes — --cwd retargeting, config-follows-cwd, exit codes,
# --help, P3-only clean boundary.
# ---------------------------------------------------------------------------


def _make_second_repo(tmp_path, name="otherrepo"):
    """Build a SECOND git repo (master trunk + feature branch with a commit)
    outside the fixture's repo, so --cwd has a distinct fork base to target."""
    repo = tmp_path / name
    repo.mkdir()
    subprocess.run(
        ["git", "init", "-q", "-b", "master", str(repo)],
        check=True,
        capture_output=True,
    )
    _git(repo, "config", "user.email", "t@t")
    _git(repo, "config", "user.name", "Test")
    skill = repo / ".claude" / "skills" / "adversarial-review"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text("# Adversarial review\nReview the diff.\n")
    (repo / "a.txt").write_text("alpha\n")
    _git(repo, "add", ".")
    _git(repo, "commit", "-q", "-m", "o1")
    _git(repo, "checkout", "-q", "-b", "feature/other")
    (repo / "b.txt").write_text("beta\n")
    _git(repo, "add", "b.txt")
    _git(repo, "commit", "-q", "-m", "o2")
    return repo


def test_cwd_flag_targets_other_repo(review_env, tmp_path):
    """``--cwd <other>`` dispatches against the OTHER repo's fork base even
    though the subprocess cwd is the fixture repo."""
    env, fixture_repo, defaults = review_env
    _force_fetched(defaults)  # surface the base in codex argv (pre-pr)
    other = _make_second_repo(tmp_path)
    other_fork = state.resolve_fork_base(str(other), ["master", "main"])
    # _argv_log writes its argv.log under the fixture repo; the subprocess
    # cwd stays the fixture repo, so only --cwd retargets the review.
    proc, argv, _ = _argv_log(
        env, fixture_repo, ["pre-pr", "--cwd", str(other)]
    )
    assert proc.returncode == 0, proc.stderr
    assert _diff_base_in_argv(argv) == other_fork
    # Sanity: the fixture repo's fork base differs, proving --cwd retargeted.
    fixture_fork = state.resolve_fork_base(str(fixture_repo), ["master", "main"])
    assert other_fork != fixture_fork


def test_cwd_flag_runs_claude_reviewer_in_target_repo(review_env, tmp_path):
    """``--cwd <other>`` on a claude tier runs the reviewer PROCESS in the
    target repo, so a ``fetched``-strategy ``git diff`` reads the right tree.

    Regression for the bug where claude inherited dd_review's cwd (the fixture
    repo) because ``Runner`` never passed ``cwd`` to ``Popen`` — only codex
    self-wrapped with ``cd``. Forced fetched so the reviewer would actually run
    ``git diff`` in-cwd."""
    env, fixture_repo, defaults = review_env
    _force_fetched(defaults)
    other = _make_second_repo(tmp_path, name="claude_cwd_repo")
    cwd_log = fixture_repo / "claude_cwd.log"
    proc = _run(
        env, fixture_repo, ["regular", "--cwd", str(other)],
        extra={"DD_REVIEW_CWD_LOG": str(cwd_log)},
    )
    assert proc.returncode == 0, proc.stderr
    assert cwd_log.exists(), "claude shim did not run"
    assert os.path.realpath(cwd_log.read_text().strip()) == os.path.realpath(
        str(other)
    )


def test_cwd_flag_rejects_non_directory(review_env):
    """``--cwd /nonexistent`` → clean non-zero exit naming the bad path; no
    traceback."""
    env, repo, _ = review_env
    bad = "/nonexistent/path/does/not/exist"
    proc = _run(env, repo, ["regular", "--cwd", bad])
    assert proc.returncode == 2
    assert bad in proc.stderr
    assert "Traceback" not in proc.stderr


def test_cwd_flag_config_follows_target_repo(review_env, tmp_path):
    """A dd-config.json in the --cwd target repo overrides a tier model; the
    dispatched argv reflects it, even though the process cwd has no config."""
    env, fixture_repo, _ = review_env
    other = _make_second_repo(tmp_path, name="cfgrepo")
    cfg_dir = other / ".claude"
    cfg_dir.mkdir(exist_ok=True)
    (cfg_dir / "dd-config.json").write_text(
        json.dumps({"review_tiers": {"regular": {"model": "haiku-cfg"}}})
    )
    # DD_CONFIG is "" in the fixture env (process-cwd config disabled); the
    # engine must steer config at the --cwd repo on its own. The subprocess
    # cwd stays the fixture repo, which has no dd-config.json.
    proc, argv, _ = _argv_log(
        env, fixture_repo, ["regular", "--cwd", str(other)]
    )
    assert proc.returncode == 0, proc.stderr
    assert "--model" in argv
    assert argv[argv.index("--model") + 1] == "haiku-cfg"


def test_help_flag_exits_zero(review_env):
    """``--help`` prints a brief usage line and exits 0 (no marker vocab)."""
    env, repo, _ = review_env
    proc = _run(env, repo, ["--help"])
    assert proc.returncode == 0
    out = proc.stdout + proc.stderr
    assert "usage" in out.lower()
    for banned in ("marker", "internal", "external"):
        assert banned not in out.lower()


def test_p3_only_findings_are_clean(review_env):
    """A reviewer emitting ONLY a [P3] finding (zero P0/P1/P2) is clean: exit 0
    AND the checkpoint is written (commits_since_checkpoint reads 0)."""
    env, repo, _ = review_env
    proc = _run(env, repo, ["regular"], stub_stdout="[P3] cosmetic nit only\n")
    assert proc.returncode == 0, proc.stderr
    assert state.commits_since_checkpoint(str(repo), "feature/x") == 0


def test_cli_error_exit_returns_one(review_env):
    """A reviewer exiting non-zero is an operational failure → exit 1."""
    env, repo, _ = review_env
    proc = _run(env, repo, ["regular"], stub_stdout="boom", stub_exit=3)
    assert proc.returncode == 1  # operational failure (not a usage error)


# ---------------------------------------------------------------------------
# _git timeout (review cycle-2) — model-invoked, but a stuck git should
# degrade rather than hang; match the sibling _git helpers' timeout=5.
# ---------------------------------------------------------------------------

from hooks import dd_review_runner as _ddr  # noqa: E402


def test_dd_review_git_passes_timeout(monkeypatch):
    captured = {}

    def fake_run(argv, **kwargs):
        captured.update(kwargs)
        return subprocess.CompletedProcess(argv, 0, stdout="x\n", stderr="")

    monkeypatch.setattr(_ddr.subprocess, "run", fake_run)
    rc, out = _ddr._git("/repo", "rev-parse", "HEAD")
    assert captured.get("timeout") == 5
    assert (rc, out) == (0, "x")


def test_dd_review_git_swallows_timeout(monkeypatch):
    def fake_run(argv, **kwargs):
        raise subprocess.TimeoutExpired(argv, 5)

    monkeypatch.setattr(_ddr.subprocess, "run", fake_run)
    assert _ddr._git("/repo", "status") == (1, "")


def test_diff_is_empty_passes_timeout(monkeypatch):
    # The empty-diff probe runs in the pre-PR hard-block path; a stuck git must
    # time out, not hang `gh pr create`. Assert the kwarg (a real hang can't be
    # unit-tested) + the empty/changed/error mapping.
    captured = {}

    def fake_run(argv, **kwargs):
        captured.update(kwargs)
        return subprocess.CompletedProcess(argv, 0)

    monkeypatch.setattr(_ddr.subprocess, "run", fake_run)
    assert _ddr._diff_is_empty("/repo", "base") is True
    assert captured.get("timeout") == 5


def test_diff_is_empty_detects_changes(monkeypatch):
    monkeypatch.setattr(
        _ddr.subprocess, "run",
        lambda argv, **k: subprocess.CompletedProcess(argv, 1),
    )
    assert _ddr._diff_is_empty("/repo", "base") is False


def test_diff_is_empty_timeout_or_error_returns_none(monkeypatch):
    def boom(argv, **kwargs):
        raise subprocess.TimeoutExpired(argv, 5)

    monkeypatch.setattr(_ddr.subprocess, "run", boom)
    assert _ddr._diff_is_empty("/repo", "base") is None

    # A non-0/1 git exit (real diff failure) also maps to None.
    monkeypatch.setattr(
        _ddr.subprocess, "run",
        lambda argv, **k: subprocess.CompletedProcess(argv, 128),
    )
    assert _ddr._diff_is_empty("/repo", "base") is None


def test_prepr_unresolvable_base_errors(review_env):
    """`pre-pr --base <bogus>` → exit 1 (the diff probe can't resolve the ref).

    Pins the error path the rewrite otherwise only covered for the success
    case (legacy test_explicit_base_must_resolve)."""
    env, repo, _ = review_env
    proc = _run(env, repo, ["pre-pr", "--base", "no-such-ref-xyz"])
    assert proc.returncode == 1
    assert "ERROR" in proc.stderr


# ---------------------------------------------------------------------------
# G3 — curated review trace (reviews.jsonl)
# ---------------------------------------------------------------------------


def _reviews(env):
    p = Path(env["DD_LOG_DIR"]) / "reviews.jsonl"
    if not p.exists():
        return []
    return [json.loads(line) for line in p.read_text().splitlines() if line.strip()]


def test_clean_pass_writes_review_record(review_env):
    env, repo, _ = review_env
    proc = _run(env, repo, ["regular"])  # stub stdout "No findings." → PASS
    assert proc.returncode == 0, proc.stderr
    recs = _reviews(env)
    assert len(recs) == 1
    r = recs[0]
    assert r["decision"] == "PASS" and r["tier"] == "regular"
    assert r["reviewer"] == "claude" and "duration_s" in r and "ts" in r
    assert r["p0"] == 0 and r["p1"] == 0 and "output" in r
    assert r["model"] == "opus" and "strategy" in r and "diff_bytes" in r


def test_block_writes_review_record(review_env):
    env, repo, _ = review_env
    proc = _run(env, repo, ["regular"], stub_stdout="[P1] real bug here\n")
    assert proc.returncode == 0, proc.stderr  # regular is advisory (exit 0)
    rec = _reviews(env)[-1]
    assert rec["decision"] == "BLOCK" and rec["p1"] == 1
    assert "[P1] real bug here" in rec["output"]


def test_error_writes_review_record(review_env):
    env, repo, _ = review_env
    # Reviewer runs but emits empty stdout → empty_output ERROR (a post-runner
    # failure; exercises the _review_record ERROR path with duration_s).
    proc = _run(env, repo, ["regular"], stub_stdout="   \n\t\n")
    assert proc.returncode == 1
    rec = _reviews(env)[-1]
    assert rec["decision"] == "ERROR" and rec["reason"] == "empty_output"
    assert rec["tier"] == "regular" and "duration_s" in rec


# ---------------------------------------------------------------------------
# Part-G review cycle-1 — timeout invariant on the pre-PR path + env guard
# ---------------------------------------------------------------------------


def test_verify_ref_passes_timeout(monkeypatch):
    captured = {}

    def fake(argv, **kw):
        captured.update(kw)
        return subprocess.CompletedProcess(argv, 0)

    monkeypatch.setattr(_ddr.subprocess, "run", fake)
    assert _ddr._verify_ref("/r", "main") is True
    assert captured.get("timeout") == 5


def test_verify_ref_timeout_returns_false(monkeypatch):
    def boom(argv, **kw):
        raise subprocess.TimeoutExpired(argv, 5)

    monkeypatch.setattr(_ddr.subprocess, "run", boom)
    assert _ddr._verify_ref("/r", "main") is False


def test_resolve_timeout_rejects_zero_env(monkeypatch):
    # DD_REVIEW_TIMEOUT=0 must not make Popen.wait(timeout=0) fire immediately;
    # fall back like the config path (which already rejects <= 0).
    monkeypatch.setenv("DD_REVIEW_TIMEOUT", "0")
    # Rejected → falls through to a positive fallback (config value or
    # DEFAULT_TIMEOUT_S); the invariant is "never 0" (else Popen.wait fires
    # instantly).
    assert _ddr._resolve_timeout() > 0
