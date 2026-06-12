"""Tests for hooks/dd_review_runner.py — tiered review engine (fork-base + checkpoint).

Rewritten for the codex-only contract (E2) and the pre-pr-only engine review
path (E5). The engine dispatches only the ``codex`` reviewer, and only for the
``pre-pr`` tier. T0–T2 subagent dispatch lives in the model-layer command —
outside this engine.

Harness mechanics:

  * ``review_env`` — a sandbox with a synthetic ``dd-defaults.json`` (via
    ``DD_DEFAULTS``) and a real ``codex`` shim binary on a per-test ``PATH``
    dir. The shim records its argv (one token per line) to
    ``$DD_REVIEW_ARGV_LOG`` and its stdin to ``$DD_REVIEW_STDIN_LOG``, then
    prints scripted stdout / exits with a scripted code, so tests can assert
    the exact flags + payload the engine passed.
  * ``feature_repo`` — a git repo with a ``master`` trunk plus a checked-out
    ``feature/x`` carrying one extra commit, exercising fork-base resolution
    and checkpoints against a real merge-base.

The engine is run as a subprocess (``python3 dd_review_runner.py ...``) so
``--cwd``, ``DD_HARD_BLOCK`` and the real ``reviewer_runner`` dispatch are
exercised end-to-end.
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

# Engine review path uses only the pre_pr config after E5.
DEFAULTS = {
    "branch_convention": {"trunk_branches": ["master", "main"]},
    "plans": {
        "active_plan_pointer": ".claude/active-plan",
        "fallback_glob": ["plans/*.md"],
    },
    "review": {"prompt_path": ".claude/skills/adversarial-review/SKILL.md"},
    "codex": {"pr_review_timeout_s": 30},
    "review_tiers": {
        # regular has commit_edit_floor only — no reviewer/model/effort (engine
        # uses regular only via --write-checkpoint, not as a review path tier).
        "regular": {
            "commit_edit_floor": 30,
        },
        # cold_read_escalation has threshold keys only — same rationale.
        "cold_read_escalation": {
            "nudge_threshold": 3,
            "hard_block_threshold": 5,
        },
        # pre_pr is the only tier with reviewer config (the engine's review path).
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


def _make_shim(binroot: Path) -> None:
    """Write a codex shim executable that records argv + stdin and emits
    scripted stdout / exit code from env vars."""
    binroot.mkdir(parents=True, exist_ok=True)
    target = binroot / "codex"
    target.write_text(
        "#!/bin/sh\n"
        'if [ -n "${DD_REVIEW_ARGV_LOG:-}" ]; then\n'
        '  printf \'%s\\n\' "$@" > "$DD_REVIEW_ARGV_LOG"\n'
        "fi\n"
        # Record the reviewer's physical cwd so tests can assert --cwd
        # actually retargeted the reviewer process.
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
    """Return ``(env, repo, defaults_path)`` with a feature branch + codex shim."""
    defaults = tmp_path / "defaults.json"
    defaults.write_text(json.dumps(DEFAULTS))

    binroot = tmp_path / "bin"
    _make_shim(binroot)

    env = {
        **os.environ,
        "DD_DEFAULTS": str(defaults),
        "DD_CONFIG": "",
        # Per-test log dir so each test's reviews.jsonl is isolated.
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
    # Adversarial-review SKILL the codex-stuffed prompt path needs.
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


def _prepr_seed_target(repo, args):
    """Return (git_root, branch_str) or None for a pre-pr invocation.

    Resolves the target's git root via `rev-parse --show-toplevel` — the same
    root the runner stores state under — so the seed lands where the
    precondition reads it even if --cwd points at a subdirectory. The --cwd
    value (when present) selects the target tree; otherwise `repo` is used.
    Branch falls back to "detached" to match the runner's
    `_current_branch(repo) or "detached"` resolution.

    Returns None when the target is not a valid git repo (e.g. --cwd pointing at
    a non-existent path in error-path tests) — caller skips the seed.
    """
    cwd = repo
    if "--cwd" in args:
        cwd = Path(args[args.index("--cwd") + 1])
    try:
        root_rc = subprocess.run(
            ["git", "-C", str(cwd), "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, timeout=5,
        )
        if root_rc.returncode != 0 or not root_rc.stdout.strip():
            return None
        target = root_rc.stdout.strip()
        br_rc = subprocess.run(
            ["git", "-C", target, "symbolic-ref", "--short", "HEAD"],
            capture_output=True, text=True, timeout=5,
        )
    except Exception:
        return None
    branch = br_rc.stdout.strip() if br_rc.returncode == 0 else "detached"
    return target, branch or "detached"


def _run(env, repo, args, stub_stdout="No findings.", stub_exit=0,
         extra=None, seed_checkpoint=True):
    """Run the review engine as a subprocess.

    seed_checkpoint (default True): when the invocation is a pre-pr review,
    seed review.checkpoint = HEAD in the target repo under the correct branch
    slug before spawning.  Pass seed_checkpoint=False for precondition tests
    and no-mutation tests that set their own checkpoint state.
    """
    full = {**env, "DD_REVIEW_STUB_STDOUT": stub_stdout,
            "DD_REVIEW_STUB_EXIT": str(stub_exit)}
    if extra:
        full.update(extra)

    if seed_checkpoint and "pre-pr" in args:
        seed_result = _prepr_seed_target(repo, args)
        if seed_result is not None:
            target, branch = seed_result
            head_rc = subprocess.run(
                ["git", "-C", str(target), "rev-parse", "HEAD"],
                capture_output=True, text=True, timeout=5,
            )
            head_sha = head_rc.stdout.strip() if head_rc.returncode == 0 else ""
            if head_sha:
                state.set_checkpoint(str(target), branch, head_sha)

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
              extra=None, seed_checkpoint=True):
    log = repo / "argv.log"
    stdin_log = repo / "stdin.log"
    e = {"DD_REVIEW_ARGV_LOG": str(log), "DD_REVIEW_STDIN_LOG": str(stdin_log)}
    if extra:
        e.update(extra)
    proc = _run(env, repo, args, stub_stdout, stub_exit, extra=e,
                seed_checkpoint=seed_checkpoint)
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
    (the strategy that surfaces the base in codex argv)."""
    cfg = json.loads(defaults.read_text())
    cfg["strategy_selector"]["pre_stuff_max_bytes"] = 1
    defaults.write_text(json.dumps(cfg))


# ---------------------------------------------------------------------------
# B1 — tier CLI + fork-base resolution
# ---------------------------------------------------------------------------


def test_prepr_dispatches_codex_against_fork_base(review_env):
    """pre-pr tier resolves its diff base to the fork base (merge-base vs trunk)
    and dispatches codex — base is observable in codex argv as ``--base <ref>``
    (forced into fetched strategy).

    E5: the engine review path is pre-pr only; regular and cold-read are
    rejected before codex is dispatched.
    """
    env, repo, defaults = review_env
    _force_fetched(defaults)
    fork = _fork_base(repo)
    proc, argv, _ = _argv_log(env, repo, ["pre-pr"])
    assert proc.returncode == 0, proc.stderr
    assert _diff_base_in_argv(argv) == fork


def test_unknown_tier_exits_2_with_usage(review_env):
    env, repo, _ = review_env
    proc = _run(env, repo, ["bogus"])
    assert proc.returncode == 2
    assert "usage" in proc.stderr.lower()


def test_engine_review_path_rejects_regular(review_env):
    """regular is not a valid tier for the engine review path (E5).

    T0–T2 subagent dispatch lives in the model-layer /dd-review command.
    The engine must reject 'regular' with a clear, non-zero exit and point
    the user toward /dd-review; the codex shim must never be dispatched.
    """
    env, repo, _ = review_env
    log = repo / "argv.log"
    proc = _run(env, repo, ["regular"], extra={"DD_REVIEW_ARGV_LOG": str(log)})
    assert proc.returncode == 2
    # Error message must be clear (usage error, not a silent fail)
    assert proc.stderr.strip() != ""
    # codex shim was never invoked
    assert not log.exists()


def test_engine_review_path_rejects_cold_read(review_env):
    """cold-read is not a valid tier for the engine review path (E5).

    Same contract as regular: non-zero exit, clear error, no codex dispatch.
    """
    env, repo, _ = review_env
    log = repo / "argv.log"
    proc = _run(env, repo, ["cold-read"], extra={"DD_REVIEW_ARGV_LOG": str(log)})
    assert proc.returncode == 2
    assert proc.stderr.strip() != ""
    assert not log.exists()


def test_base_rejected_on_prepr_non_base_syntax(review_env):
    """--base is only meaningful on pre-pr, but since only pre-pr is a valid
    engine tier, the rejection path for non-pre-pr tiers is now unreachable.
    Verify pre-pr *accepts* --base and resolves it correctly instead."""
    env, repo, defaults = review_env
    _force_fetched(defaults)
    proc, argv, _ = _argv_log(env, repo, ["pre-pr", "--base", "master"])
    # master is a real ref in the fixture repo → should succeed
    assert proc.returncode == 0, proc.stderr
    assert _diff_base_in_argv(argv) == "master"


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
    # Sanity: HEAD~1 differs from the fork base, proving --base is a real override.
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

    env, _, defaults = review_env
    _force_fetched(defaults)
    fork = state.resolve_fork_base(str(repo), ["master", "main"])
    assert fork is not None
    proc, argv, _ = _argv_log(env, repo, ["pre-pr"])
    assert proc.returncode == 0, proc.stderr
    # Codex fetched: base is in argv.
    assert _diff_base_in_argv(argv) == fork


def test_empty_diff_clean_exit_no_runner(review_env):
    """HEAD == fork base → clean exit 0, no reviewer dispatched (Delta 1)."""
    env, repo, _ = review_env
    _git(repo, "reset", "--hard", "master")
    proc, argv, _ = _argv_log(env, repo, ["pre-pr"])
    assert proc.returncode == 0
    assert argv == []  # shim never ran
    assert "nothing to review" in proc.stdout


# ---------------------------------------------------------------------------
# E2 contract — codex-only; non-codex reviewer config yields a clear error
# ---------------------------------------------------------------------------


def test_non_codex_reviewer_config_yields_error(review_env):
    """A tier configured with reviewer='claude' yields exit 1 with a clear error;
    the codex shim is never dispatched.

    After E2, 'claude' is not a valid engine reviewer — the engine errors
    loudly rather than attempting to dispatch a removed path.
    """
    env, repo, defaults = review_env
    cfg = json.loads(defaults.read_text())
    cfg["review_tiers"]["pre_pr"]["reviewer"] = "claude"
    defaults.write_text(json.dumps(cfg))

    log = repo / "argv.log"
    proc = _run(env, repo, ["pre-pr"], extra={"DD_REVIEW_ARGV_LOG": str(log)})
    assert proc.returncode == 1
    assert "ERROR" in proc.stderr
    assert not log.exists()  # codex shim never ran


def test_unknown_reviewer_config_yields_error(review_env):
    """A tier configured with an unrecognized reviewer (not 'codex') yields
    exit 1 with a clear error — the selector raises ValueError on unknown reviewers.
    """
    env, repo, defaults = review_env
    cfg = json.loads(defaults.read_text())
    cfg["review_tiers"]["pre_pr"]["reviewer"] = "gemini"
    defaults.write_text(json.dumps(cfg))

    proc = _run(env, repo, ["pre-pr"])
    assert proc.returncode == 1
    assert "ERROR" in proc.stderr


# ---------------------------------------------------------------------------
# B2 — codex reviewer dispatch + per-knob argv (pre-pr is the only engine tier)
# ---------------------------------------------------------------------------


def test_prepr_codex_model_and_effort_in_argv(review_env):
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


def test_stuffed_strategy_embeds_diff_in_stdin(review_env):
    """Small diff → codex stuffed: diff body is piped on stdin (stdin ends with
    '-' in argv), containing the actual changed file content."""
    env, repo, _ = review_env
    proc, argv, stdin = _argv_log(env, repo, ["pre-pr"])
    assert proc.returncode == 0, proc.stderr
    # Stuffed strategy: argv ends in "-" (codex reads from stdin).
    assert argv[-1] == "-"
    # The diff body is in stdin (the actual change).
    assert "g.txt" in stdin
    assert "+two" in stdin  # the actual diff hunk


def test_fetched_strategy_base_in_argv(review_env):
    """Large diff → codex fetched: ``--base <ref>`` is in argv, no stdin diff."""
    env, repo, defaults = review_env
    _force_fetched(defaults)
    fork = _fork_base(repo)
    proc, argv, stdin = _argv_log(env, repo, ["pre-pr"])
    assert proc.returncode == 0, proc.stderr
    # Fetched: argv has --base, NOT stdin ("-" at end).
    assert "--base" in argv
    assert _diff_base_in_argv(argv) == fork
    assert argv[-1] != "-"
    # No diff body in stdin (codex fetches the diff itself).
    assert "+two" not in stdin


def test_cli_missing_errors(review_env, tmp_path):
    """Reviewer CLI absent from PATH → operational error exit 1, no dispatch.

    Build an isolated bin dir holding only a ``git`` symlink so neither the
    shim nor any real ``codex`` on the host PATH is reachable.
    """
    env, repo, _ = review_env
    isolated = tmp_path / "onlygit"
    isolated.mkdir()
    (isolated / "git").symlink_to(shutil.which("git"))
    env = {**env, "PATH": str(isolated)}
    # _run's default seed_checkpoint=True seeds checkpoint=HEAD here, so the
    # precondition would pass — but cli_missing fires first (upstream of the
    # gate), which is exactly the precedence this test pins. The dedicated
    # no-checkpoint case is test_prepr_missing_reviewer_errors_before_precondition.
    proc = _run(env, repo, ["pre-pr"])
    assert proc.returncode == 1  # operational failure (not a usage error)
    assert "not found on PATH" in proc.stderr


def test_empty_reviewer_stdout_errors(review_env):
    """Whitespace-only reviewer stdout → operational error exit 1."""
    env, repo, _ = review_env
    proc = _run(env, repo, ["pre-pr"], stub_stdout="   \n\t\n")
    assert proc.returncode == 1  # operational failure (not a usage error)
    assert "no output" in proc.stderr


# ---------------------------------------------------------------------------
# B3 — checkpoint write + hard-block + Delta-4 (no history writer)
# ---------------------------------------------------------------------------


def test_prepr_clean_pass_writes_checkpoint_and_resets_edits(review_env):
    """A clean pre-pr pass checkpoints HEAD AND resets edits.count to 0 (T3 rule).

    E5: the clean codex pass now resets edits.count in addition to writing
    the checkpoint. Seeds a non-zero edits counter so the reset is observable.
    """
    env, repo, _ = review_env
    # Seed a non-zero edits counter so the reset is observable.
    state_dir = repo / ".claude" / ".dd-state" / "feature_x"
    state_dir.mkdir(parents=True, exist_ok=True)
    (state_dir / "edits.count").write_text("17")

    proc = _run(env, repo, ["pre-pr"], stub_stdout="[P3] nit only.\n")
    assert proc.returncode == 0, proc.stderr

    head = _git(repo, "rev-parse", "HEAD")
    # Checkpoint is written.
    assert state.commits_since_checkpoint(str(repo), "feature/x") == 0
    cp = state_dir / "review.checkpoint"
    assert cp.read_text().strip() == head
    # edits.count is reset (E5 T3 rule).
    assert state.read(str(repo), "feature/x", "edits") == 0


def test_block_leaves_checkpoint_and_edits_unchanged(review_env):
    """A BLOCK (P1 finding) must NOT advance the checkpoint or reset edits.count.

    Under the new fixture contract, _run seeds checkpoint=HEAD before the call
    (so the precondition passes and codex runs).  A BLOCK leaves the checkpoint
    untouched at that pre-seeded HEAD value — commits_since_checkpoint remains
    0, not None, and the checkpoint file is still the seed value.
    """
    env, repo, _ = review_env
    # _run default seed_checkpoint=True seeds checkpoint=HEAD before spawning.
    head = _git(repo, "rev-parse", "HEAD")
    # Seed a non-zero edits counter. The precondition forces checkpoint==HEAD
    # before codex runs, so the checkpoint value alone can't distinguish "BLOCK
    # left it" from "BLOCK rewrote it to HEAD". edits.count is the observable
    # half: a clean PASS resets it, so a BLOCK leaving it intact is the proof
    # the BLOCK skips the whole checkpoint+reset block.
    _seed_edits_count(repo, 17)
    proc = _run(env, repo, ["pre-pr"], stub_stdout="[P1] broken auth at f.go:12\n")
    assert proc.returncode == 0  # pre-pr without DD_HARD_BLOCK is advisory
    # Checkpoint is the pre-seeded value (unchanged by the BLOCK).
    assert state.commits_since_checkpoint(str(repo), "feature/x") == 0
    cp = repo / ".claude" / ".dd-state" / "feature_x" / "review.checkpoint"
    assert cp.exists()
    assert cp.read_text().strip() == head
    # edits.count is NOT reset by a BLOCK (only a clean PASS resets it).
    assert state.read(str(repo), "feature/x", "edits") == 17


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


def test_no_review_history_log_written(review_env):
    """Delta 4: the pre-pr engine tier must not create a .review-history.log."""
    env, repo, _ = review_env
    _run(env, repo, ["pre-pr"], stub_stdout="[P0] blocking\n[P3] nit\n")
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
    proc, argv, _ = _argv_log(
        env, fixture_repo, ["pre-pr", "--cwd", str(other)]
    )
    assert proc.returncode == 0, proc.stderr
    assert _diff_base_in_argv(argv) == other_fork
    # Sanity: the fixture repo's fork base differs, proving --cwd retargeted.
    fixture_fork = state.resolve_fork_base(str(fixture_repo), ["master", "main"])
    assert other_fork != fixture_fork


def test_cwd_flag_rejects_non_directory(review_env):
    """``--cwd /nonexistent`` → clean non-zero exit naming the bad path; no
    traceback."""
    env, repo, _ = review_env
    bad = "/nonexistent/path/does/not/exist"
    proc = _run(env, repo, ["pre-pr", "--cwd", bad])
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
        json.dumps({"review_tiers": {"pre_pr": {"model": "gpt-4o-mini"}}})
    )
    # DD_CONFIG is "" in the fixture env (process-cwd config disabled); the
    # engine must steer config at the --cwd repo on its own.
    proc, argv, _ = _argv_log(
        env, fixture_repo, ["pre-pr", "--cwd", str(other)]
    )
    assert proc.returncode == 0, proc.stderr
    assert 'model="gpt-4o-mini"' in "\n".join(argv)


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
    proc = _run(env, repo, ["pre-pr"], stub_stdout="[P3] cosmetic nit only\n")
    assert proc.returncode == 0, proc.stderr
    assert state.commits_since_checkpoint(str(repo), "feature/x") == 0


def test_cli_error_exit_returns_one(review_env):
    """A reviewer exiting non-zero is an operational failure → exit 1."""
    env, repo, _ = review_env
    proc = _run(env, repo, ["pre-pr"], stub_stdout="boom", stub_exit=3)
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
    """`pre-pr --base <bogus>` → exit 1 (the diff probe can't resolve the ref)."""
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
    proc = _run(env, repo, ["pre-pr"])  # stub stdout "No findings." → PASS
    assert proc.returncode == 0, proc.stderr
    recs = _reviews(env)
    assert len(recs) == 1
    r = recs[0]
    assert r["decision"] == "PASS" and r["tier"] == "pre-pr"
    # Codex is the only reviewer after E2.
    assert r["reviewer"] == "codex" and "duration_s" in r and "ts" in r
    assert r["p0"] == 0 and r["p1"] == 0 and "output" in r
    assert r["model"] == "gpt-5.5" and "strategy" in r and "diff_bytes" in r


def test_block_writes_review_record(review_env):
    env, repo, _ = review_env
    proc = _run(env, repo, ["pre-pr"], stub_stdout="[P1] real bug here\n")
    assert proc.returncode == 0, proc.stderr  # pre-pr without DD_HARD_BLOCK is advisory
    rec = _reviews(env)[-1]
    assert rec["decision"] == "BLOCK" and rec["p1"] == 1
    assert "[P1] real bug here" in rec["output"]
    assert rec["reviewer"] == "codex"


def test_error_writes_review_record(review_env):
    env, repo, _ = review_env
    # Reviewer runs but emits empty stdout → empty_output ERROR (a post-runner
    # failure; exercises the _review_record ERROR path with duration_s).
    proc = _run(env, repo, ["pre-pr"], stub_stdout="   \n\t\n")
    assert proc.returncode == 1
    rec = _reviews(env)[-1]
    assert rec["decision"] == "ERROR" and rec["reason"] == "empty_output"
    assert rec["tier"] == "pre-pr" and "duration_s" in rec


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
    assert _ddr._resolve_timeout() > 0


# ---------------------------------------------------------------------------
# E3 — --write-checkpoint <tier>: reset rule for fast/regular/cold-read
# ---------------------------------------------------------------------------
# Fixture note: review_env seeds a feature/x branch with one commit (c2)
# on top of master. The branch slug is "feature_x".


def _branch_state_dir(repo: Path) -> Path:
    """Shorthand: the .dd-state dir for the feature/x branch slug."""
    return repo / ".claude" / ".dd-state" / "feature_x"


def _seed_edits_count(repo: Path, count: int) -> None:
    """Write an edits.count file directly so --write-checkpoint has something to reset."""
    d = _branch_state_dir(repo)
    d.mkdir(parents=True, exist_ok=True)
    (d / "edits.count").write_text(str(count))


def _seed_checkpoint(repo: Path, sha: str) -> None:
    """Write a review.checkpoint file directly."""
    d = _branch_state_dir(repo)
    d.mkdir(parents=True, exist_ok=True)
    (d / "review.checkpoint").write_text(sha)


def test_write_checkpoint_fast_resets_edits_leaves_checkpoint_untouched(review_env):
    """fast tier: resets edits.count to 0; review.checkpoint is not created/changed."""
    env, repo, _ = review_env
    _seed_edits_count(repo, 42)
    _seed_checkpoint(repo, "aabbccdd" * 5)  # pre-existing checkpoint

    proc = _run(env, repo, ["--write-checkpoint", "fast"])
    assert proc.returncode == 0, proc.stderr

    # edits.count is gone (reset = file removed)
    assert state.read(str(repo), "feature/x", "edits") == 0
    # checkpoint is unchanged
    cp = _branch_state_dir(repo) / "review.checkpoint"
    assert cp.read_text().strip() == "aabbccdd" * 5


def test_write_checkpoint_regular_resets_edits_leaves_checkpoint_untouched(review_env):
    """regular tier: resets edits.count to 0; review.checkpoint is not created/changed."""
    env, repo, _ = review_env
    _seed_edits_count(repo, 17)
    _seed_checkpoint(repo, "deadbeef" * 5)

    proc = _run(env, repo, ["--write-checkpoint", "regular"])
    assert proc.returncode == 0, proc.stderr

    assert state.read(str(repo), "feature/x", "edits") == 0
    cp = _branch_state_dir(repo) / "review.checkpoint"
    assert cp.read_text().strip() == "deadbeef" * 5


def test_write_checkpoint_cold_read_sets_checkpoint_and_resets_edits(review_env):
    """cold-read tier: sets review.checkpoint=HEAD AND resets edits.count."""
    env, repo, _ = review_env
    _seed_edits_count(repo, 55)
    head = _git(repo, "rev-parse", "HEAD")

    proc = _run(env, repo, ["--write-checkpoint", "cold-read"])
    assert proc.returncode == 0, proc.stderr

    # edits counter is gone (reset)
    assert state.read(str(repo), "feature/x", "edits") == 0
    # checkpoint = HEAD at the time of the call
    cp = _branch_state_dir(repo) / "review.checkpoint"
    assert cp.read_text().strip() == head


def test_write_checkpoint_unknown_tier_exits_nonzero_no_mutation(review_env):
    """Unknown tier → non-zero exit and clear error; no state is written."""
    env, repo, _ = review_env
    _seed_edits_count(repo, 7)
    _seed_checkpoint(repo, "cafebabe" * 5)

    proc = _run(env, repo, ["--write-checkpoint", "bogus-tier"])
    assert proc.returncode != 0

    # Neither state file is mutated
    assert state.read(str(repo), "feature/x", "edits") == 7
    cp = _branch_state_dir(repo) / "review.checkpoint"
    assert cp.read_text().strip() == "cafebabe" * 5


def test_write_checkpoint_no_codex_dispatch(review_env):
    """--write-checkpoint never dispatches the codex shim (no argv log created)."""
    env, repo, _ = review_env
    log = repo / "argv_wc.log"
    e = {**env, "DD_REVIEW_ARGV_LOG": str(log)}
    for tier in ("fast", "regular", "cold-read"):
        if log.exists():
            log.unlink()
        proc = subprocess.run(
            [sys.executable, str(HOOK), "--write-checkpoint", tier],
            capture_output=True,
            text=True,
            env=e,
            cwd=str(repo),
        )
        assert proc.returncode == 0, f"{tier}: {proc.stderr}"
        assert not log.exists(), f"{tier}: codex shim was invoked unexpectedly"


# ---------------------------------------------------------------------------
# E4 — --resolve-scope <tier>: per-tier diff scope resolver
# ---------------------------------------------------------------------------
# Fixture note: review_env seeds a feature/x branch with one commit (c2)
# on top of master.  The fork base is the master-tip SHA (c1).
# --resolve-scope is a thin, side-effect-free mode: no state writes, no
# codex dispatch.  The scope string is printed on stdout; errors go to
# stderr and exit non-zero.


def _resolve_scope(env, repo, tier, extra=None):
    """Run --resolve-scope <tier> and return the completed process."""
    full = {**env}
    if extra:
        full.update(extra)
    return subprocess.run(
        [sys.executable, str(HOOK), "--resolve-scope", tier],
        capture_output=True,
        text=True,
        env=full,
        cwd=str(repo),
    )


def test_resolve_scope_fast_prints_HEAD(review_env):
    """fast tier: working-tree vs HEAD — scope string is exactly 'HEAD'."""
    env, repo, _ = review_env
    proc = _resolve_scope(env, repo, "fast")
    assert proc.returncode == 0, proc.stderr
    assert proc.stdout.strip() == "HEAD"


@pytest.mark.parametrize("tier", ["regular", "cold-read"])
def test_resolve_scope_review_tiers_print_fork_base_range(review_env, tier):
    """regular / cold-read: scope is '<fork-base-sha>..HEAD' resolved via
    state.resolve_fork_base against the trunk branches in config."""
    env, repo, _ = review_env
    fork = _fork_base(repo)
    assert fork is not None, "fixture must have a resolvable fork base"
    proc = _resolve_scope(env, repo, tier)
    assert proc.returncode == 0, proc.stderr
    assert proc.stdout.strip() == f"{fork}..HEAD"


def test_resolve_scope_unknown_tier_exits_nonzero_no_stdout_scope(review_env):
    """Unknown tier → non-zero exit; no scope line on stdout."""
    env, repo, _ = review_env
    proc = _resolve_scope(env, repo, "bogus-tier")
    assert proc.returncode != 0
    # stdout must not contain a scope-looking string (no '..HEAD' or bare 'HEAD')
    assert "..HEAD" not in proc.stdout
    assert proc.stdout.strip() != "HEAD"


def test_resolve_scope_no_codex_dispatch_no_state_mutation(review_env):
    """--resolve-scope neither dispatches the codex shim nor mutates state."""
    env, repo, _ = review_env
    log = repo / "scope_argv.log"
    _seed_edits_count(repo, 13)
    _seed_checkpoint(repo, "deadbeef" * 5)

    proc = _resolve_scope(env, repo, "regular",
                          extra={"DD_REVIEW_ARGV_LOG": str(log)})
    assert proc.returncode == 0, proc.stderr

    # codex shim never ran
    assert not log.exists(), "--resolve-scope dispatched codex unexpectedly"
    # edits.count unchanged
    assert state.read(str(repo), "feature/x", "edits") == 13
    # checkpoint unchanged
    cp = _branch_state_dir(repo) / "review.checkpoint"
    assert cp.read_text().strip() == "deadbeef" * 5


# ---------------------------------------------------------------------------
# Fix 1 — detached-HEAD reset bug: --write-checkpoint uses "detached" slug
# ---------------------------------------------------------------------------


def _make_detached_repo(tmp_path, env):
    """Git repo with master trunk; HEAD detached at the initial commit."""
    repo = tmp_path / "detached_repo"
    repo.mkdir()
    subprocess.run(
        ["git", "init", "-q", "-b", "master", str(repo)],
        check=True, capture_output=True,
    )
    _git(repo, "config", "user.email", "t@t")
    _git(repo, "config", "user.name", "Test")
    (repo / "f.txt").write_text("seed\n")
    _git(repo, "add", ".")
    _git(repo, "commit", "-q", "-m", "init")
    # Detach HEAD.
    sha = _git(repo, "rev-parse", "HEAD")
    _git(repo, "checkout", "-q", "--detach", sha)
    return repo


def _detached_state_dir(repo):
    """The .dd-state dir for the 'detached' slug."""
    return repo / ".claude" / ".dd-state" / "detached"


def test_write_checkpoint_fast_detached_head_resets_detached_slug(review_env, tmp_path):
    """--write-checkpoint fast on a detached-HEAD repo resets 'detached' slug counter.

    Fix 1: _current_branch() returns "" on detached HEAD; without the fix,
    state.reset(repo, "", "edits") writes to the state ROOT instead of the
    'detached' slug dir. After the fix, the 'detached' slug is used and a
    pre-seeded edits.count is cleared.
    """
    env, _, _ = review_env
    repo = _make_detached_repo(tmp_path, env)

    # Seed a non-zero edits.count under the 'detached' slug.
    det_dir = _detached_state_dir(repo)
    det_dir.mkdir(parents=True, exist_ok=True)
    (det_dir / "edits.count").write_text("9")

    proc = subprocess.run(
        [sys.executable, str(HOOK), "--write-checkpoint", "fast"],
        capture_output=True, text=True, env=env, cwd=str(repo),
    )
    assert proc.returncode == 0, proc.stderr

    # Counter under 'detached' slug must be 0 (reset).
    assert state.read(str(repo), "detached", "edits") == 0


def test_write_checkpoint_cold_read_detached_head_uses_detached_slug(review_env, tmp_path):
    """--write-checkpoint cold-read on detached HEAD writes checkpoint to 'detached' slug.

    Fix 1: without the fix, set_checkpoint(repo, "", sha) writes to the root-level
    dir instead of <branch-slug>/. After the fix, 'detached' slug is used.
    """
    env, _, _ = review_env
    repo = _make_detached_repo(tmp_path, env)

    # Seed edits.count so the reset is observable.
    det_dir = _detached_state_dir(repo)
    det_dir.mkdir(parents=True, exist_ok=True)
    (det_dir / "edits.count").write_text("7")

    proc = subprocess.run(
        [sys.executable, str(HOOK), "--write-checkpoint", "cold-read"],
        capture_output=True, text=True, env=env, cwd=str(repo),
    )
    assert proc.returncode == 0, proc.stderr

    # edits.count reset under 'detached' slug.
    assert state.read(str(repo), "detached", "edits") == 0
    # review.checkpoint written under 'detached' slug.
    cp = det_dir / "review.checkpoint"
    assert cp.exists(), "checkpoint file was not created under 'detached' slug"
    head = _git(repo, "rev-parse", "HEAD")
    assert cp.read_text().strip() == head


# ---------------------------------------------------------------------------
# Fix 2 — misleading success message: tier-specific wording
# ---------------------------------------------------------------------------


def test_write_checkpoint_fast_message_says_edits_reset(review_env):
    """fast tier --write-checkpoint message says 'edits counter reset', not 'checkpoint written'."""
    env, repo, _ = review_env
    proc = subprocess.run(
        [sys.executable, str(HOOK), "--write-checkpoint", "fast"],
        capture_output=True, text=True, env=env, cwd=str(repo),
    )
    assert proc.returncode == 0, proc.stderr
    out = proc.stdout
    assert "edits counter reset" in out
    # Must NOT claim a checkpoint was written (no checkpoint is written for fast).
    assert "checkpoint written" not in out


def test_write_checkpoint_regular_message_says_edits_reset(review_env):
    """regular tier --write-checkpoint message says 'edits counter reset'."""
    env, repo, _ = review_env
    proc = subprocess.run(
        [sys.executable, str(HOOK), "--write-checkpoint", "regular"],
        capture_output=True, text=True, env=env, cwd=str(repo),
    )
    assert proc.returncode == 0, proc.stderr
    assert "edits counter reset" in proc.stdout
    assert "checkpoint written" not in proc.stdout


def test_write_checkpoint_cold_read_message_says_checkpoint_and_reset(review_env):
    """cold-read tier --write-checkpoint message says 'checkpoint written and edits counter reset'."""
    env, repo, _ = review_env
    proc = subprocess.run(
        [sys.executable, str(HOOK), "--write-checkpoint", "cold-read"],
        capture_output=True, text=True, env=env, cwd=str(repo),
    )
    assert proc.returncode == 0, proc.stderr
    out = proc.stdout
    assert "checkpoint written" in out
    assert "edits counter reset" in out


# ---------------------------------------------------------------------------
# Fix 5 — missing coverage: --write-checkpoint pre-pr exits 2, no mutation;
#          --resolve-scope pre-pr prints fork-base range
# ---------------------------------------------------------------------------


def test_write_checkpoint_prepr_exits_2_no_mutation(review_env):
    """--write-checkpoint pre-pr → exit 2, no state written (pre-pr is excluded from _CHECKPOINT_TIERS)."""
    env, repo, _ = review_env
    _seed_edits_count(repo, 11)
    _seed_checkpoint(repo, "abcd1234" * 5)

    proc = subprocess.run(
        [sys.executable, str(HOOK), "--write-checkpoint", "pre-pr"],
        capture_output=True, text=True, env=env, cwd=str(repo),
    )
    assert proc.returncode == 2

    # No state mutation.
    assert state.read(str(repo), "feature/x", "edits") == 11
    cp = _branch_state_dir(repo) / "review.checkpoint"
    assert cp.read_text().strip() == "abcd1234" * 5


def test_resolve_scope_prepr_prints_fork_base_range(review_env):
    """pre-pr tier --resolve-scope prints '<fork-base>..HEAD' (same as regular/cold-read)."""
    env, repo, _ = review_env
    fork = _fork_base(repo)
    assert fork is not None, "fixture must have a resolvable fork base"
    proc = _resolve_scope(env, repo, "pre-pr")
    assert proc.returncode == 0, proc.stderr
    assert proc.stdout.strip() == f"{fork}..HEAD"


# ---------------------------------------------------------------------------
# Phase 1 — Precondition gate (T1 + T2)
#
# Fixture note: _run / _argv_log seed review.checkpoint=HEAD for pre-pr
# invocations (see the fixture-contract change comment in _run). Tests that
# exercise the precondition block set seed_checkpoint=False so they start
# without a checkpoint (or seed their own via _seed_checkpoint).
# ---------------------------------------------------------------------------


def test_prepr_blocks_when_no_checkpoint(review_env):
    """pre-pr with no checkpoint (None) → blocked before dispatch; step-back
    message names '/dd-review cold-read' (the model-layer command, not a
    runner tier the engine rejects).

    seed_checkpoint=False: this test exercises the precondition block path;
    no checkpoint must exist before the runner starts.
    """
    env, repo, _ = review_env
    log = repo / "precon_argv.log"
    # seed_checkpoint=False: precondition test — must start with absent checkpoint.
    proc = _run(env, repo, ["pre-pr"],
                extra={"DD_REVIEW_ARGV_LOG": str(log)},
                seed_checkpoint=False)
    # Blocked before dispatch.
    assert log.exists() is False, "codex shim must NOT be invoked on precondition block"
    # Message must name the command, not a runner tier.
    combined = proc.stdout + proc.stderr
    assert "/dd-review cold-read" in combined
    # Advisory return (no DD_HARD_BLOCK): precondition block still exits 0.
    assert proc.returncode == 0


def test_prepr_blocks_when_commits_since_checkpoint(review_env):
    """pre-pr with commits since checkpoint (>0) → blocked before dispatch;
    no codex invocation; step-back message present.

    Seeds checkpoint at master (one commit behind HEAD on feature/x) so
    commits_since_checkpoint returns 1.
    """
    env, repo, _ = review_env
    # Seed checkpoint at master tip — one commit behind feature/x HEAD, and an
    # ancestor of it, so commits_since_checkpoint counts 1 (here master tip
    # coincides with the fork base, the branch having no divergence).
    master_sha = _git(repo, "rev-parse", "master")
    # seed_checkpoint=False: we seed our own stale checkpoint, not HEAD.
    _seed_checkpoint(repo, master_sha)

    log = repo / "stale_argv.log"
    proc = _run(env, repo, ["pre-pr"],
                extra={"DD_REVIEW_ARGV_LOG": str(log)},
                seed_checkpoint=False)
    assert log.exists() is False, "codex shim must NOT be invoked on precondition block"
    combined = proc.stdout + proc.stderr
    assert "/dd-review cold-read" in combined
    assert proc.returncode == 0


def test_prepr_passes_precondition_when_checkpoint_at_head(review_env):
    """pre-pr with checkpoint == HEAD → precondition passes; codex IS dispatched.

    Fixture-contract: _run seeds checkpoint=HEAD for pre-pr (seed_checkpoint=True
    default); this test verifies that seed causes dispatch — the invariant that
    all existing reviewer-path tests rely on.
    """
    env, repo, _ = review_env
    log = repo / "pass_argv.log"
    # Default seed_checkpoint=True: _run seeds HEAD; precondition passes.
    proc = _run(env, repo, ["pre-pr"], extra={"DD_REVIEW_ARGV_LOG": str(log)})
    # Codex shim must have been invoked.
    assert log.exists(), "codex shim should be invoked when precondition passes"
    assert proc.returncode == 0, proc.stderr


def test_prepr_precondition_block_hard_block_returns_nonzero(review_env):
    """Under DD_HARD_BLOCK=1 the precondition block returns non-zero (maps to
    exit 2 in the wrapper), so the PR is hard-blocked.

    seed_checkpoint=False: precondition test; no checkpoint present.
    """
    env, repo, _ = review_env
    log = repo / "hb_argv.log"
    # seed_checkpoint=False: precondition test.
    proc = _run(env, repo, ["pre-pr"],
                extra={"DD_HARD_BLOCK": "1", "DD_REVIEW_ARGV_LOG": str(log)},
                seed_checkpoint=False)
    assert log.exists() is False
    assert proc.returncode != 0


def test_prepr_empty_diff_wins_over_stale_checkpoint(review_env):
    """empty diff (HEAD == fork base) with no checkpoint → clean exit 0 via
    the empty-diff path, NOT a precondition block. Reviewer not invoked.

    Precedence: empty-diff check is upstream of the precondition gate, so an
    absent checkpoint must not produce a precondition block when there is
    nothing to review.
    """
    env, repo, _ = review_env
    # Reset HEAD to master so diff is empty.
    _git(repo, "reset", "--hard", "master")
    log = repo / "emp_argv.log"
    # seed_checkpoint=False: no checkpoint; tests that empty-diff wins.
    proc = _run(env, repo, ["pre-pr"],
                extra={"DD_REVIEW_ARGV_LOG": str(log)},
                seed_checkpoint=False)
    assert proc.returncode == 0
    assert log.exists() is False   # reviewer not invoked
    assert "nothing to review" in proc.stdout


def test_prepr_missing_reviewer_errors_before_precondition(review_env, tmp_path):
    """Missing reviewer CLI → exit 1 (ERROR) even without a checkpoint.

    The cli_missing check is upstream of the precondition gate; an ERROR
    must win over a precondition block.
    """
    env, repo, _ = review_env
    isolated = tmp_path / "onlygit_precon"
    isolated.mkdir()
    (isolated / "git").symlink_to(shutil.which("git"))
    env = {**env, "PATH": str(isolated)}
    # seed_checkpoint=False: no checkpoint; tests that cli_missing wins.
    proc = _run(env, repo, ["pre-pr"], seed_checkpoint=False)
    assert proc.returncode == 1
    assert "not found on PATH" in proc.stderr


def test_prepr_detached_head_checkpoint_satisfies_precondition(review_env, tmp_path):
    """A checkpoint written under the 'detached' slug at HEAD satisfies the
    precondition: codex is dispatched, proving the 'or detached' branch
    resolution reads the same location as --write-checkpoint.

    Manually seeds detached/review.checkpoint at HEAD (the same write that
    --write-checkpoint cold-read produces on a detached repo), then runs
    pre-pr on that detached repo and asserts codex fires.
    """
    env, _, _ = review_env
    repo = _make_detached_repo(tmp_path, env)
    # Add the adversarial-review skill so the stuffed-diff prompt path works.
    skill = repo / ".claude" / "skills" / "adversarial-review"
    skill.mkdir(parents=True, exist_ok=True)
    (skill / "SKILL.md").write_text("# Adversarial review\nReview the diff.\n")
    # Add a commit so there's a diff (detached HEAD off the master fork base).
    (repo / "x.txt").write_text("change\n")
    _git(repo, "add", "x.txt")
    _git(repo, "commit", "-q", "-m", "detached-commit")

    head_sha = _git(repo, "rev-parse", "HEAD")
    # Manually seed checkpoint under 'detached' slug — what --write-checkpoint writes.
    det_dir = _detached_state_dir(repo)
    det_dir.mkdir(parents=True, exist_ok=True)
    (det_dir / "review.checkpoint").write_text(head_sha)

    log = repo / "det_argv.log"
    # seed_checkpoint=False: the manually seeded checkpoint is the test state;
    # _run must not overwrite it with its own HEAD seed.
    proc = _run(env, repo, ["pre-pr"],
                extra={"DD_REVIEW_ARGV_LOG": str(log)},
                seed_checkpoint=False)
    assert log.exists(), (
        f"codex shim must be dispatched when detached checkpoint == HEAD; "
        f"stdout={proc.stdout!r} stderr={proc.stderr!r}"
    )
    assert proc.returncode == 0, proc.stderr


def test_prepr_codex_findings_block_message_directs_to_internal_loop(review_env):
    """A codex BLOCK (P1 finding) emits a directive line sending the model back
    into the internal wide-lens cycle rather than patch-and-retry the PR.

    Fixture-contract: default seed_checkpoint=True so the precondition passes
    and codex runs; the stub returns P1 to produce a BLOCK.
    """
    env, repo, _ = review_env
    # Default seed_checkpoint=True: precondition passes, codex stub runs, P1 → BLOCK.
    proc = _run(env, repo, ["pre-pr"],
                stub_stdout="[P1] broken auth at f.go:12\n")
    combined = proc.stdout + proc.stderr
    # Assert the distinctive directive phrasing, not just "cold-read" (which
    # could leak from elsewhere): the model is told NOT to patch-and-retry and
    # to route through the internal cold-read loop.
    assert "patch and retry" in combined
    assert "/dd-review cold-read" in combined


def test_precondition_block_writes_review_record(review_env):
    """A precondition block appends a curated reviews.jsonl record — it is a
    first-class BLOCK outcome and must be visible in the review history, not
    only the rolling hook log (codex finding, PR-1 cold-read).

    seed_checkpoint=False: exercise the precondition block path (no checkpoint).
    """
    env, repo, _ = review_env
    proc = _run(env, repo, ["pre-pr"], seed_checkpoint=False)
    assert proc.returncode == 0  # advisory (no DD_HARD_BLOCK)
    recs = _reviews(env)
    assert len(recs) == 1, "precondition block must append exactly one curated record"
    rec = recs[0]
    assert rec["decision"] == "BLOCK"
    assert "precondition" in rec["reason"]
    assert rec["tier"] == "pre-pr"
