#!/usr/bin/env python3
"""dd_review_runner.py — model-callable adversarial review against the branch diff.

Usage:
    python3 dd_review_runner.py pre-pr [--base <ref>] [--cwd <path>]

Rebuilt on the ``hooks/lib`` modules (config, severity, state,
reviewer_runner, review_invocation, review_prompt). Four behavior deltas
versus the original marker-based engine (see plan Part B):

  * Delta 1 — every tier resolves its diff base to the *fork base*
    (merge-base of HEAD against the first existing trunk ref) via
    ``state.resolve_fork_base``. The ``-internal`` / ``-external``
    marker reads and the chunk→phase auto-detection are dropped.
    ``pre-pr`` still honours an explicit ``--base <ref>`` override.
    Empty diff (HEAD == fork base) → clean exit, no reviewer dispatched.
  * Delta 2 — the engine codex review path is the T3 (pre-pr) gate only.
    A clean pre-pr pass writes the per-branch review checkpoint via
    ``state.set_checkpoint`` AND resets ``edits.count`` (T3 reset rule).
    T0–T2 subagent dispatch and their ``--write-checkpoint`` round-trips
    live in the model-layer ``/dd-review`` command.
  * Delta 3 — no marker writes anywhere.
  * Delta 4 — no ``.review-history.log`` writer; JSONL debug logging
    via ``logging_setup`` is preserved.

The engine review path (codex dispatch + severity scan) is ``pre-pr`` only.
``--write-checkpoint`` and ``--resolve-scope`` accept additional tiers
(fast / regular / cold-read) for model-layer state writes and scope queries.

Advisory vs hard-block: manual invocation always exits 0 (the model is
the consumer). The pre-PR hook wrapper sets ``DD_HARD_BLOCK=1`` so
``pre-pr`` returns non-zero on any P0/P1/P2 finding — the gate before
``gh pr create``.
"""

from __future__ import annotations

import os
import pathlib
import shutil
import subprocess
import sys
import time

_HERE = pathlib.Path(__file__).resolve().parent
_BASE_DIR = _HERE.parent  # the dir containing the `hooks` package
if str(_BASE_DIR) not in sys.path:
    sys.path.insert(0, str(_BASE_DIR))

from hooks.lib import (  # noqa: E402
    reviewer_runner,
    config,
    logging_setup,
    review_invocation,
    review_prompt,
    severity,
    state,
)

HOOK_NAME = "dd_review"
DEFAULT_TIMEOUT_S = 300
VALID_TIERS = ("pre-pr",)

# Tiers valid for --write-checkpoint (fast + the three review tiers; pre-pr is
# excluded: the codex clean pass writes its own checkpoint and never round-trips
# through this flag).
_CHECKPOINT_TIERS = ("fast", "regular", "cold-read")

# Tiers valid for --resolve-scope.  All four tiers are addressable: fast →
# working-tree scope ("HEAD"); the review tiers → fork-base range.
_SCOPE_TIERS = ("fast", "regular", "cold-read", "pre-pr")

# Tiers and sources valid for --log-review.
_LOG_REVIEW_TIERS = ("fast", "regular", "cold-read", "self-review", "external")
_LOG_REVIEW_SOURCES = ("command", "ad-hoc")

# CLI tier → config-key tier name (hyphen in the CLI, underscore in config).
# Only pre-pr has a config entry used by the engine's review path; regular and
# cold-read are handled via --write-checkpoint (no reviewer dispatch, no config
# lookup for these tiers).
_TIER_CONFIG_KEY = {
    "pre-pr": "pre_pr",
}


# --- argv parsing ----------------------------------------------------------


def _parse_argv(argv: list[str]) -> tuple[str, str | None, str | None] | str:
    """Return (tier, base_override, cwd_override) or an error message string.

    ``--base`` is meaningful only for pre-pr; reject it loudly on the other
    tiers so a stale invocation doesn't silently audit the wrong diff.
    """
    tier: str | None = None
    base: str | None = None
    cwd: str | None = None
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--base":
            if i + 1 >= len(argv):
                return "--base requires a ref argument"
            if base is not None:
                return "--base specified twice"
            base = argv[i + 1]
            i += 2
        elif arg == "--cwd":
            if i + 1 >= len(argv):
                return "--cwd requires a path argument"
            if cwd is not None:
                return "--cwd specified twice"
            cwd = argv[i + 1]
            i += 2
        elif arg in VALID_TIERS:
            if tier is not None:
                return f"tier specified twice ({tier!r} and {arg!r})"
            tier = arg
            i += 1
        else:
            return f"unrecognized argument {arg!r}"
    if tier is None:
        return (
            "missing required tier (pre-pr). "
            "T0–T2 tiers (fast/regular/cold-read) are handled by the "
            "/dd-review command, not this engine."
        )
    if base is not None and tier != "pre-pr":
        return f"--base is only valid on pre-pr (not {tier!r})"
    return tier, base, cwd


def _print_usage_error(msg: str) -> None:
    print(f"[dd_review] ERROR — {msg}", file=sys.stderr)
    print(
        f"Usage: python3 dd_review_runner.py {{{'|'.join(VALID_TIERS)}}} "
        f"[--base <ref>] [--cwd <path>]\n"
        f"       python3 dd_review_runner.py --write-checkpoint "
        f"{{{'|'.join(_CHECKPOINT_TIERS)}}} [--cwd <path>]\n"
        f"       python3 dd_review_runner.py --resolve-scope "
        f"{{{'|'.join(_SCOPE_TIERS)}}} [--cwd <path>]\n"
        f"       python3 dd_review_runner.py --log-review "
        f"--tier {{{'|'.join(_LOG_REVIEW_TIERS)}}} "
        f"--source {{{'|'.join(_LOG_REVIEW_SOURCES)}}} "
        f"[--round <n>] [--reviewer <id>] [--cwd <path>]",
        file=sys.stderr,
    )


# --- --write-checkpoint mode -----------------------------------------------


def _handle_write_checkpoint(argv: list[str]) -> int | None:
    """Handle ``--write-checkpoint <tier> [--cwd <path>]`` if present.

    Returns the exit code (0 or non-zero) when the flag is found, or None
    when it is absent (caller continues with the normal review path).

    Reset rule (spec §Cadence & state):
      fast | regular → reset ``edits.count`` only.
      cold-read      → ``set_checkpoint(HEAD)`` AND reset ``edits.count``.
      pre-pr         → NOT handled here; codex clean pass writes its own.
    """
    if "--write-checkpoint" not in argv:
        return None

    # Parse: --write-checkpoint <tier> [--cwd <path>]
    # No other flags are valid in this mode.
    tier: str | None = None
    cwd: str | None = None
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--write-checkpoint":
            if i + 1 >= len(argv):
                _print_usage_error("--write-checkpoint requires a tier argument")
                return 2
            if tier is not None:
                _print_usage_error("--write-checkpoint specified twice")
                return 2
            tier = argv[i + 1]
            i += 2
        elif arg == "--cwd":
            if i + 1 >= len(argv):
                _print_usage_error("--cwd requires a path argument")
                return 2
            if cwd is not None:
                _print_usage_error("--cwd specified twice")
                return 2
            cwd = argv[i + 1]
            i += 2
        else:
            _print_usage_error(
                f"--write-checkpoint mode does not accept {arg!r}"
            )
            return 2

    if tier not in _CHECKPOINT_TIERS:
        _print_usage_error(
            f"unknown checkpoint tier {tier!r} "
            f"(valid: {' | '.join(_CHECKPOINT_TIERS)})"
        )
        return 2

    repo_path = cwd or os.getcwd()
    if cwd and not pathlib.Path(cwd).is_dir():
        _print_usage_error(f"--cwd {cwd!r} is not a directory")
        return 2

    # Resolve the git repo root (mirrors main()'s pattern).
    try:
        r = subprocess.run(
            ["git", "-C", repo_path, "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, timeout=5,
        )
    except Exception:
        print("[dd_review --write-checkpoint] ERROR: git unavailable", file=sys.stderr)
        return 1
    if r.returncode != 0 or not r.stdout.strip():
        print("[dd_review --write-checkpoint] ERROR: not inside a git repo",
              file=sys.stderr)
        return 1
    repo = r.stdout.strip()

    branch = _current_branch(repo) or "detached"
    head_sha = _head_sha(repo)

    # Reset rule — spec §Cadence & state.
    if tier in ("fast", "regular"):
        state.reset(repo, branch, "edits")
        print(f"[dd_review --write-checkpoint] {tier}: edits counter reset.")
    elif tier == "cold-read":
        if head_sha:
            state.set_checkpoint(repo, branch, head_sha)
        state.reset(repo, branch, "edits")
        print(
            f"[dd_review --write-checkpoint] {tier}: "
            "checkpoint written and edits counter reset."
        )
    return 0


# --- --resolve-scope mode --------------------------------------------------


def _handle_resolve_scope(argv: list[str]) -> int | None:
    """Handle ``--resolve-scope <tier> [--cwd <path>]`` if present.

    Returns the exit code when the flag is found, or None when absent
    (caller continues with the normal review path).

    Prints a single scope string on stdout and exits 0 on success:
      fast                → ``HEAD``   (working-tree vs HEAD; captures in-flight edits)
      regular/cold-read/pre-pr → ``<fork-base-sha>..HEAD``

    No state writes, no codex dispatch.  If the fork base cannot be
    resolved the call exits 1 with an error on stderr and no scope on stdout.
    """
    if "--resolve-scope" not in argv:
        return None

    tier: str | None = None
    cwd: str | None = None
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--resolve-scope":
            if i + 1 >= len(argv):
                _print_usage_error("--resolve-scope requires a tier argument")
                return 2
            if tier is not None:
                _print_usage_error("--resolve-scope specified twice")
                return 2
            tier = argv[i + 1]
            i += 2
        elif arg == "--cwd":
            if i + 1 >= len(argv):
                _print_usage_error("--cwd requires a path argument")
                return 2
            if cwd is not None:
                _print_usage_error("--cwd specified twice")
                return 2
            cwd = argv[i + 1]
            i += 2
        else:
            _print_usage_error(f"--resolve-scope mode does not accept {arg!r}")
            return 2

    if tier not in _SCOPE_TIERS:
        print(
            f"[dd_review --resolve-scope] ERROR — unknown tier {tier!r} "
            f"(valid: {' | '.join(_SCOPE_TIERS)})",
            file=sys.stderr,
        )
        return 2

    repo_path = cwd or os.getcwd()
    if cwd and not pathlib.Path(cwd).is_dir():
        _print_usage_error(f"--cwd {cwd!r} is not a directory")
        return 2

    # fast → working-tree scope: no git calls needed.
    if tier == "fast":
        print("HEAD")
        return 0

    # review tiers → fork-base range.
    try:
        r = subprocess.run(
            ["git", "-C", repo_path, "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, timeout=5,
        )
    except Exception:
        print("[dd_review --resolve-scope] ERROR: git unavailable", file=sys.stderr)
        return 1
    if r.returncode != 0 or not r.stdout.strip():
        print("[dd_review --resolve-scope] ERROR: not inside a git repo",
              file=sys.stderr)
        return 1
    repo = r.stdout.strip()

    trunks = config.get("branch_convention.trunk_branches", ["master", "main"])
    if not isinstance(trunks, list) or not trunks:
        trunks = ["master", "main"]
    base = state.resolve_fork_base(repo, trunks)
    if not base:
        print(
            f"[dd_review --resolve-scope] ERROR — could not determine a fork "
            f"base — none of {trunks} resolve in this repo.",
            file=sys.stderr,
        )
        return 1

    print(f"{base}..HEAD")
    return 0


# --- --log-review mode ----------------------------------------------------


def _handle_log_review(argv: list[str]) -> int | None:
    """Handle ``--log-review --tier <t> --source <s> [--round <n>] [--reviewer <id>]``
    if present.

    Returns the exit code when the flag is found, or None when absent (caller
    continues with the normal review path).

    Reads findings from stdin; derives p0–p3, decision, and output; appends one
    row to reviews.jsonl via logging_setup.append_review. No reviewer dispatched,
    no checkpoint written, no scope resolved.
    """
    if "--log-review" not in argv:
        return None

    tier: str | None = None
    source: str | None = None
    round_: int = 1
    reviewer: str = "subagents"
    cwd: str | None = None
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--log-review":
            i += 1
        elif arg == "--tier":
            if i + 1 >= len(argv):
                _print_usage_error("--tier requires an argument")
                return 2
            tier = argv[i + 1]
            i += 2
        elif arg == "--source":
            if i + 1 >= len(argv):
                _print_usage_error("--source requires an argument")
                return 2
            source = argv[i + 1]
            i += 2
        elif arg == "--round":
            if i + 1 >= len(argv):
                _print_usage_error("--round requires an integer argument")
                return 2
            try:
                round_ = int(argv[i + 1])
            except ValueError:
                _print_usage_error(
                    f"--round requires an integer, got {argv[i + 1]!r}"
                )
                return 2
            i += 2
        elif arg == "--reviewer":
            if i + 1 >= len(argv):
                _print_usage_error("--reviewer requires an argument")
                return 2
            reviewer = argv[i + 1]
            i += 2
        elif arg == "--cwd":
            if i + 1 >= len(argv):
                _print_usage_error("--cwd requires a path argument")
                return 2
            if cwd is not None:
                _print_usage_error("--cwd specified twice")
                return 2
            cwd = argv[i + 1]
            i += 2
        else:
            _print_usage_error(f"--log-review mode does not accept {arg!r}")
            return 2

    if tier not in _LOG_REVIEW_TIERS:
        _print_usage_error(
            f"unknown --tier {tier!r} "
            f"(valid: {' | '.join(_LOG_REVIEW_TIERS)})"
        )
        return 2

    if source not in _LOG_REVIEW_SOURCES:
        _print_usage_error(
            f"unknown --source {source!r} "
            f"(valid: {' | '.join(_LOG_REVIEW_SOURCES)})"
        )
        return 2

    # --cwd validation (mirrors sibling handlers).
    repo_path = cwd or os.getcwd()
    if cwd and not pathlib.Path(cwd).is_dir():
        _print_usage_error(f"--cwd {cwd!r} is not a directory")
        return 2

    # Resolve git repo root (same idiom as _handle_write_checkpoint /
    # _handle_resolve_scope).
    try:
        r = subprocess.run(
            ["git", "-C", repo_path, "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, timeout=5,
        )
    except Exception:
        print("[dd_review --log-review] ERROR: git unavailable", file=sys.stderr)
        return 1
    if r.returncode != 0 or not r.stdout.strip():
        print("[dd_review --log-review] ERROR: not inside a git repo",
              file=sys.stderr)
        return 1
    repo = r.stdout.strip()

    # Git-derived fields.
    branch = _current_branch(repo)
    head_sha = _head_sha(repo)

    # Base resolution per tier (mirrors _handle_resolve_scope logic exactly):
    #   fast → literal "HEAD" (working-tree scope; no git call needed)
    #   all other _LOG_REVIEW_TIERS → fork base SHA via state.resolve_fork_base
    if tier == "fast":
        base: str = "HEAD"
    else:
        trunks = config.get("branch_convention.trunk_branches", ["master", "main"])
        if not isinstance(trunks, list) or not trunks:
            trunks = ["master", "main"]
        base = state.resolve_fork_base(repo, trunks) or ""

    findings = sys.stdin.read()

    # Reject empty / whitespace-only stdin as a usage error BEFORE deriving
    # severity. count_severities("") returns all-zero, which would otherwise
    # produce a false PASS row from a blank pipe and poison the telemetry. A
    # real clean review comes from a non-empty "No findings." emission — blank
    # stdin means the caller piped nothing, not that the review found nothing.
    if not findings.strip():
        _print_usage_error(
            "--log-review requires non-empty findings on stdin; "
            "got empty or whitespace-only input"
        )
        return 2

    p0, p1, p2, p3 = severity.count_severities(findings, line_start=True)
    decision = "BLOCK" if (p0 + p1 + p2) > 0 else "PASS"

    logging_setup.append_review({
        "tier": tier,
        "source": source,
        "round": round_,
        "reviewer": reviewer,
        "branch": branch,
        "head_sha": head_sha,
        "base": base,
        "output": findings,
        "p0": p0,
        "p1": p1,
        "p2": p2,
        "p3": p3,
        "decision": decision,
    })
    return 0


# --- git helpers -----------------------------------------------------------


def _git(repo: str, *args: str) -> tuple[int, str]:
    # timeout + degrade-safe, matching the sibling _git helpers: a stuck git
    # should fail fast (reads as "git said no") rather than hang the review.
    try:
        r = subprocess.run(
            ["git", "-C", repo, *args], capture_output=True, text=True, timeout=5
        )
    except Exception:
        return 1, ""
    return r.returncode, r.stdout.strip()


def _current_branch(repo: str) -> str:
    rc, out = _git(repo, "symbolic-ref", "--short", "HEAD")
    return out if rc == 0 else ""


def _head_sha(repo: str) -> str:
    rc, out = _git(repo, "rev-parse", "HEAD")
    return out if rc == 0 else ""


def _verify_ref(repo: str, ref: str) -> bool:
    # timeout-bounded: on the pre-PR hard-block path (_resolve_base for an
    # explicit --base), a stuck git must not hang `gh pr create`.
    try:
        r = subprocess.run(
            ["git", "-C", repo, "rev-parse", "--verify", "--quiet", ref],
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False
    return r.returncode == 0


# --- base resolution (Delta 1 — fork-base for every tier) -------------------


def _resolve_base(
    repo: str, tier: str, explicit: str | None
) -> tuple[str | None, str | None]:
    """Return (base, error). Every tier resolves to the fork base; pre-pr
    honours an explicit ``--base`` override (already gated upstream)."""
    if explicit and tier == "pre-pr":
        if _verify_ref(repo, explicit):
            return explicit, None
        return None, (
            f"explicit base ref '{explicit}' not present locally "
            f"(try `git fetch` then retry)"
        )
    trunks = config.get("branch_convention.trunk_branches", ["master", "main"])
    # `or not trunks` falls back on an empty list too — a blanked config array
    # otherwise propagates and yields a misleading "none of [] resolve" error.
    if not isinstance(trunks, list) or not trunks:
        trunks = ["master", "main"]
    base = state.resolve_fork_base(repo, trunks)
    if base:
        return base, None
    return None, (
        f"could not determine a fork base — none of {trunks} resolve in "
        f"this repo. Fetch a trunk ref or set "
        f"`branch_convention.trunk_branches` in dd-config.json. pre-pr "
        f"additionally accepts `--base <ref>`."
    )


# --- tier + selector config ------------------------------------------------


def _load_tier_and_selector(
    tier: str,
) -> tuple[dict | None, dict | None, str | None]:
    config_key = _TIER_CONFIG_KEY[tier]
    tier_cfg = config.get(f"review_tiers.{config_key}")
    if not isinstance(tier_cfg, dict):
        return None, None, f"review_tiers.{config_key} missing or malformed"
    for required in ("reviewer", "model", "default_effort"):
        if required not in tier_cfg:
            return None, None, (
                f"review_tiers.{config_key}.{required} missing in config"
            )
    selector = config.get("strategy_selector")
    if not isinstance(selector, dict):
        return None, None, "strategy_selector missing or malformed in config"
    for required in ("pre_stuff_max_bytes", "high_effort_min_bytes"):
        if required not in selector:
            return None, None, f"strategy_selector.{required} missing in config"
    return tier_cfg, selector, None


def _read_diff_bytes(repo: str, base: str) -> bytes | None:
    try:
        r = subprocess.run(
            ["git", "-C", repo, "diff", f"{base}...HEAD"],
            capture_output=True,
            check=False,
            # Generous (large diffs are legitimate) but bounded: the engine is
            # also the pre-PR gate (E2), so a hung git/fsmonitor must not block
            # `gh pr create` with no escape. TimeoutExpired → None below.
            timeout=60,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if r.returncode != 0:
        return None
    return r.stdout


def _diff_is_empty(repo: str, base: str) -> bool | None:
    """True if ``{base}...HEAD`` is empty, False if it has changes, None on
    error/timeout. Cheap exit-code-only probe; timeout-bounded for the same
    reason as ``_read_diff_bytes`` — this engine is the pre-PR hard block, so a
    stuck git must not hang ``gh pr create`` (exit 0 = empty, 1 = changes,
    anything else = git error → None)."""
    try:
        r = subprocess.run(
            ["git", "-C", repo, "diff", "--quiet", f"{base}...HEAD"],
            capture_output=True,
            timeout=5,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if r.returncode == 0:
        return True
    if r.returncode == 1:
        return False
    return None


def _resolve_prompt_path(repo: str) -> tuple[pathlib.Path, str]:
    configured = os.environ.get("DD_REVIEW_PROMPT_PATH", "")
    if not configured:
        configured = config.get(
            "review.prompt_path", ".claude/skills/adversarial-review/SKILL.md"
        )
    p = pathlib.Path(configured)
    if not p.is_absolute():
        p = pathlib.Path(repo) / configured
    return (p.resolve() if p.exists() else p, configured)


def _resolve_timeout() -> int:
    env = os.environ.get("DD_REVIEW_TIMEOUT")
    if env:
        try:
            v = int(env)
            if v > 0:  # reject 0/negative — Popen.wait(timeout=0) fires instantly
                return v
        except ValueError:
            pass
    val = config.get("codex.pr_review_timeout_s")
    if isinstance(val, int) and not isinstance(val, bool) and val > 0:
        return val
    return DEFAULT_TIMEOUT_S


# --- entry point -----------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    if "--help" in argv or "-h" in argv:
        print(
            f"Usage: python3 dd_review_runner.py {{{'|'.join(VALID_TIERS)}}} "
            f"[--base <ref>] [--cwd <path>]\n"
            f"       python3 dd_review_runner.py --write-checkpoint "
            f"{{{'|'.join(_CHECKPOINT_TIERS)}}} [--cwd <path>]\n"
            f"       python3 dd_review_runner.py --resolve-scope "
            f"{{{'|'.join(_SCOPE_TIERS)}}} [--cwd <path>]\n"
            f"       python3 dd_review_runner.py --log-review "
            f"--tier {{{'|'.join(_LOG_REVIEW_TIERS)}}} "
            f"--source {{{'|'.join(_LOG_REVIEW_SOURCES)}}} "
            f"[--round <n>] [--reviewer <id>] [--cwd <path>]\n"
            "Run an adversarial review of the branch diff against its fork "
            "base.\n"
            "  --base <ref>  pre-pr only: override the diff base.\n"
            "  --cwd <path>  review the repo rooted at <path>.\n"
            "  --write-checkpoint <tier>  write post-clean-review state only "
            "(no review dispatched).\n"
            "  --resolve-scope <tier>  print the git diff argument for <tier> "
            "(no review dispatched, no state written).\n"
            "  --log-review  append one curated row to reviews.jsonl from "
            "findings on stdin (no review dispatched, no checkpoint written)."
        )
        return 0

    # --write-checkpoint mode: pure state write, no reviewer dispatched.
    wc_rc = _handle_write_checkpoint(argv)
    if wc_rc is not None:
        return wc_rc

    # --resolve-scope mode: pure scope resolver, no state writes or dispatch.
    rs_rc = _handle_resolve_scope(argv)
    if rs_rc is not None:
        return rs_rc

    # --log-review mode: derive severity + decision from stdin, append to log.
    lr_rc = _handle_log_review(argv)
    if lr_rc is not None:
        return lr_rc

    parsed = _parse_argv(argv)
    if isinstance(parsed, str):
        _print_usage_error(parsed)
        return 2
    tier, explicit_base, cwd_override = parsed

    logger = logging_setup.setup(HOOK_NAME)
    logger.emit(
        "invoked",
        tier=tier,
        explicit_base=explicit_base or "",
        cwd=cwd_override or "",
    )

    repo = cwd_override or os.getcwd()
    if cwd_override and not pathlib.Path(cwd_override).is_dir():
        _print_usage_error(f"--cwd {cwd_override!r} is not a directory")
        return 2

    rc_root, repo_root = _git(repo, "rev-parse", "--show-toplevel")
    if rc_root != 0 or not repo_root:
        print("[dd_review] ERROR: not inside a git repo.", file=sys.stderr)
        return 1
    repo = repo_root

    # Config must follow --cwd: config._user_config_path() resolves
    # .claude/dd-config.json under $CLAUDE_PROJECT_DIR (or cwd when unset) — the
    # ORIGINAL project in a live session, not the --cwd target tree. Steer
    # DD_CONFIG at the target repo before the
    # first config.get(...) below. Don't clobber a DD_CONFIG the caller/test
    # already set to a real path. An empty-string DD_CONFIG is treated as
    # unset — config.py itself reads it via a falsy `if override:` check, and
    # the test harness sets ``DD_CONFIG=""`` to disable process-cwd config.
    #
    # Accepted (review, re-raised 3x): this mutates the process env for the
    # rest of this process's life. Blast radius is (a) the spawned reviewer
    # subprocess, which inherits it, and (b) any later in-process config read.
    # Both are safe: neither `claude` nor `codex` reads DD_CONFIG, and
    # dd_review is a single-shot CLI — after this point main() only dispatches
    # the reviewer, scans output, checkpoints, and exits; nothing re-resolves
    # config for the original repo. A try/finally restore wouldn't help (the
    # subprocess is spawned inside the window), and an explicit env= dict is
    # dead complexity for an inert path. Revisit only if a real in-process
    # caller reads config after this line, or a reviewer starts consuming
    # DD_CONFIG.
    if cwd_override and not os.environ.get("DD_CONFIG"):
        os.environ["DD_CONFIG"] = str(
            pathlib.Path(repo) / ".claude" / "dd-config.json"
        )
        config.reset_config_cache()

    branch = _current_branch(repo)
    head_sha = _head_sha(repo)

    tier_config, selector_config, cfg_err = _load_tier_and_selector(tier)
    if cfg_err or tier_config is None or selector_config is None:
        print(f"[dd_review {tier}] ERROR — {cfg_err}", file=sys.stderr)
        return 1
    reviewer = tier_config["reviewer"]

    def _error(reason: str, msg: str) -> int:
        # Exit 1 = operational failure (cli-missing, timeout, empty stdout,
        # diff failure). Usage errors stay 2 (see _parse_argv / --cwd checks).
        logger.emit("error", reason=reason, msg=msg)
        # Curated review trace: record the tooling failure too (analysis wants
        # "is it working", not just successful reviews). Fields known this
        # early only; degrade-safe.
        logging_setup.append_review({
            "tier": tier, "source": "engine", "reviewer": reviewer,
            "branch": branch, "head_sha": head_sha, "decision": "ERROR",
            "reason": reason, "msg": msg,
        })
        print(f"[dd_review {tier}] ERROR — {msg}", file=sys.stderr)
        return 1

    if shutil.which(reviewer) is None:
        return _error("cli_missing", f"{reviewer} CLI not found on PATH")

    base, base_err = _resolve_base(repo, tier, explicit_base)
    if base_err or not base:
        return _error("base_unresolvable", base_err or "could not resolve base")

    # Empty-diff check — cheap exit-code-only probe (timeout-bounded; this
    # engine is the pre-PR hard block, so a stuck git must not hang it).
    empty = _diff_is_empty(repo, base)
    if empty is None:
        return _error("git_diff_failed", f"git diff {base}...HEAD failed or timed out")
    if empty:
        print(
            f"[dd_review {tier}] No changes between {base} and HEAD; "
            "nothing to review."
        )
        logger.emit("noop", reason="empty_diff", base=base)
        return 0

    paths_csv = review_prompt.gather_touched_paths(repo, base)

    diff_body = _read_diff_bytes(repo, base)
    if diff_body is None:
        return _error("git_diff_failed", f"git diff {base}...HEAD failed")
    diff_bytes = len(diff_body)

    try:
        invocation = review_invocation.pick_invocation(
            tier_config, selector_config, diff_bytes
        )
    except (KeyError, ValueError) as exc:
        return _error("selector_failed", f"pick_invocation: {exc}")

    logger.emit(
        "invocation",
        reviewer=invocation.reviewer,
        model=invocation.model,
        effort=invocation.effort,
        strategy=invocation.strategy,
        diff_bytes=diff_bytes,
    )

    # Build codex argv + optional stuffed prompt.
    # codex is the only engine reviewer after E2 (claude -p removed).
    prompt = ""
    runner_argv = review_prompt.codex_runner_argv(
        repo if cwd_override else None,
        base,
        model=invocation.model,
        effort=invocation.effort,
        strategy=invocation.strategy,
    )
    if invocation.strategy == "stuffed":
        prompt_path, configured_path = _resolve_prompt_path(repo)
        if not prompt_path.is_file():
            return _error(
                "prompt_missing",
                f"review.prompt_path ({configured_path}) not found",
            )
        try:
            skill_text = prompt_path.read_text()
        except OSError as exc:
            return _error(
                "prompt_unreadable",
                f"review.prompt_path ({configured_path}) unreadable: {exc}",
            )
        prompt = (
            skill_text
            + "\n\n## Diff (pre-stuffed; no need to git diff)\n\n"
            + "```diff\n"
            + diff_body.decode("utf-8", errors="replace")
            + "\n```\n"
        )

    review_start = time.monotonic()
    timeout_s = _resolve_timeout()
    result = reviewer_runner.Runner(
        argv=runner_argv,
        timeout_s=timeout_s,
        stdin_text=prompt,
        log=logger,
        # Run codex IN the repo under review. Codex self-wraps with `cd` for
        # the fetched strategy, but a redundant cwd here is harmless and
        # ensures consistent behaviour across strategies.
        cwd=repo,
    ).run()
    duration_s = int(time.monotonic() - review_start)

    def _review_record(decision: str, **extra) -> None:
        # Curated review trace — every POST-runner outcome (PASS/BLOCK/ERROR),
        # so analysis sees latency + outcomes incl. tooling failures. The
        # pre-runner _error path writes its own leaner record (invocation/diff
        # not yet known there). Degrade-safe (append_review never raises).
        logging_setup.append_review({
            "tier": tier,
            "source": "engine",
            "reviewer": invocation.reviewer,
            "model": invocation.model,
            "effort": invocation.effort,
            "strategy": invocation.strategy,
            "diff_bytes": diff_bytes,
            "base": base,
            "branch": branch,
            "head_sha": head_sha,
            "duration_s": duration_s,
            "decision": decision,
            **extra,
        })

    if result.exit_reason == "timeout" or result.exit_code == 124:
        logger.emit("error", reason="cli_timeout", duration_s=duration_s)
        _review_record("ERROR", reason="cli_timeout")
        print(
            f"[dd_review {tier}] ERROR — {reviewer} review timed out "
            f"(>{timeout_s}s)",
            file=sys.stderr,
        )
        return 1
    if result.exit_code != 0:
        logger.emit(
            "error",
            reason="cli_error",
            exit_code=result.exit_code,
            duration_s=duration_s,
        )
        _review_record("ERROR", reason="cli_error", exit_code=result.exit_code)
        print(
            f"[dd_review {tier}] ERROR — {reviewer} review exited "
            f"{result.exit_code}",
            file=sys.stderr,
        )
        return 1

    review_output = result.stdout
    if not review_output.strip():
        logger.emit("error", reason="empty_output", duration_s=duration_s)
        _review_record("ERROR", reason="empty_output")
        print(
            f"[dd_review {tier}] ERROR — {reviewer} produced no output",
            file=sys.stderr,
        )
        return 1

    # Severity scan — stdout only, line-start anchored.
    p0, p1, p2, p3 = severity.count_severities(review_output, line_start=True)
    excerpt = severity.findings_excerpt(review_output, line_start=True)
    decision = "BLOCK" if (p0 + p1 + p2) > 0 else "PASS"

    print("=" * 64)
    print(
        f"[dd_review {tier}] {decision} in {duration_s}s — "
        f"{p0}xP0 {p1}xP1 {p2}xP2 {p3}xP3"
    )
    print("=" * 64)
    print()
    print(review_output)
    if excerpt:
        print(excerpt, file=sys.stderr)

    # Clean pre-pr pass: checkpoint HEAD and reset edits.count (T3 reset rule,
    # spec §Cadence & state). A BLOCK does neither.
    if decision == "PASS" and branch and head_sha:
        state.set_checkpoint(repo, branch, head_sha)
        state.reset(repo, branch, "edits")

    logger.emit(
        "decision",
        decision=decision,
        p0=p0,
        p1=p1,
        p2=p2,
        p3=p3,
        duration_s=duration_s,
        tier=tier,
        reviewer=reviewer,
        base=base,
    )

    # Curated review trace (the analysis substrate: outcome, latency, the
    # full result).
    _review_record(decision, p0=p0, p1=p1, p2=p2, p3=p3, output=review_output)

    # pre-pr hard-block: DD_HARD_BLOCK=1 (set by the PreToolUse wrapper)
    # makes BLOCK return non-zero. Manual invocation stays advisory.
    if (
        tier == "pre-pr"
        and decision == "BLOCK"
        and os.environ.get("DD_HARD_BLOCK") == "1"
    ):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
