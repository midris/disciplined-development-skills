#!/usr/bin/env python3
"""pre_pr_review.py — PreToolUse Bash gate: the only hard block.

Detects ``gh pr create``, resolves the target cwd, and delegates to
``external_review.py`` (whole-repo, verdict-driven, fail-closed).  No base
resolution and no ``DD_HARD_BLOCK``; the verdict is entirely the external gate's
responsibility.

Paths:
- PR-shaped + parseable cwd → delegate to ``external_review.py --cwd <cwd>``;
  any non-zero result maps to exit 2 (Claude Code blocks PreToolUse ONLY on 2),
  and the delegate's stdout+stderr are re-emitted on stderr so findings reach
  the model.
- PR-shaped + unparseable cwd (e.g. ``cd $VAR && gh pr create``) → log one
  ``reviews.jsonl`` ERROR row (decision=ERROR, reason=unparseable) then block
  (exit 2); the model is told to rewrite the command or set the bypass.
- Not a ``gh pr create`` command → exit 0 (all other Bash through).
- ``DD_SKIP_PR_REVIEW=1`` in the launching shell → exit 0 (bypass for automated
  workflows that review separately).
"""

from __future__ import annotations

import json
import os
import pathlib
import subprocess
import sys

_HERE = pathlib.Path(__file__).resolve().parent
_BASE_DIR = _HERE.parent  # the dir containing the `hooks` package
if str(_BASE_DIR) not in sys.path:
    sys.path.insert(0, str(_BASE_DIR))

from hooks.lib import config, logging_setup, review_record  # noqa: E402
from hooks.lib.command_match import (  # noqa: E402
    find_gh_pr_create,
    looks_like_gh_pr_create,
)

HOOK_NAME = "pre_pr_review"


def _external_review_script() -> str:
    """Path to the external_review gate. ``DD_EXTERNAL_REVIEW_SCRIPT`` overrides
    it (test seam: tests point this at a recording shim run by the same
    interpreter)."""
    return os.environ.get("DD_EXTERNAL_REVIEW_SCRIPT") or str(
        _HERE / "external_review.py"
    )


def _read_command() -> str:
    try:
        data = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, OSError):
        return ""
    if not isinstance(data, dict):
        return ""
    ti = data.get("tool_input")
    if isinstance(ti, dict) and isinstance(ti.get("command"), str):
        return ti["command"]
    return ""


def _current_branch(repo: str) -> str:
    """Current branch via git symbolic-ref; 'detached' on detached HEAD or failure.

    Mirrors external_review._current_branch / log_review._current_branch exactly:
    ``symbolic-ref --short HEAD`` with a literal ``"detached"`` fallback so the
    per-branch state-dir key is always consistent.  ``rev-parse --abbrev-ref``
    returns ``"HEAD"`` on detached HEAD — not used here.
    """
    try:
        r = subprocess.run(
            ["git", "-C", repo, "symbolic-ref", "--short", "HEAD"],
            capture_output=True,
            text=True,
            check=False,
            timeout=5,
        )
    except Exception:
        return "detached"
    branch = r.stdout.strip()
    return branch if r.returncode == 0 and branch else "detached"


def _log_unparseable(repo: str) -> None:
    """Append one ERROR/unparseable review row — best-effort, never raises."""
    try:
        branch = _current_branch(repo)
        reviewer = config.get("review.reviewer", "codex")
        ctx = review_record.gather_cadence_context(repo, branch)
        row = review_record.build_review_record(
            findings="",
            source="external-gate",
            trigger="gate:pre-pr",
            reviewer=reviewer,
            round=1,
            context=ctx,
            decision="ERROR",
            reason="unparseable",
        )
        logging_setup.append_review(row)
    except Exception:
        # Best-effort: a log failure must NOT stop the block.
        pass


def main() -> int:
    logger = logging_setup.setup(HOOK_NAME)

    if os.environ.get("DD_SKIP_PR_REVIEW") == "1":
        logger.emit("skip", reason="env_bypass")
        return 0

    # Read command before the guarded region so the exception handler can
    # call looks_like_gh_pr_create(command).  If reading itself raises,
    # command stays "" (not PR-shaped → allow).
    command = ""
    try:
        command = _read_command()
        cwd = find_gh_pr_create(command)
        if cwd is None:
            if looks_like_gh_pr_create(command):
                # Looks like ``gh pr create`` but the target directory couldn't be
                # resolved (e.g. a ``cd`` to a shell variable / command substitution).
                # Fail closed: log ERROR row + block — do NOT let an unreviewed PR
                # through (the fail-open bug this gate exists to prevent).
                # The command was unparseable so the cd target is unknown;
                # os.getcwd() is the process cwd, which may differ from the
                # intended repo — the logged row's repo/branch/cadence fields
                # are best-effort and may not match the intended tree.
                repo = os.getcwd()
                _log_unparseable(repo)
                logger.emit("block", reason="unresolvable_cwd")
                print(
                    "[pre-pr] BLOCKED: couldn't resolve the target directory for a "
                    "`gh pr create` (e.g. a `cd` to an unexpandable path or a "
                    "hard-to-parse command). Re-run with an explicit or absolute "
                    "path, or set DD_SKIP_PR_REVIEW=1 in the launching shell "
                    "to bypass.",
                    file=sys.stderr,
                )
                return 2
            # Not ``gh pr create`` — let every other Bash command through.
            return 0

        argv = [sys.executable, _external_review_script(), "--cwd", cwd]
        logger.emit("delegate", cwd=cwd)
        result = subprocess.run(argv, capture_output=True, text=True)

        # Exit-code translation is load-bearing: Claude Code blocks a PreToolUse
        # tool ONLY on exit 2; any other non-zero is a non-blocking error and the
        # tool (gh pr create) still runs.  external_review returns 0 on PASS and
        # non-zero on BLOCK / any failure — map any non-zero to 2 and re-emit the
        # delegate's output on stderr so findings reach the model.
        out = (result.stdout or "") + (result.stderr or "")
        if result.returncode != 0:
            logger.emit("block", ext_exit=result.returncode)
            sys.stderr.write(out)
            return 2
        # Clean pass — surface the output and let the PR through.
        sys.stdout.write(out)
        return 0

    except Exception:
        # Unexpected exception in the gate itself (e.g. resource exhaustion,
        # sandbox kill, BrokenPipeError on stderr.write).  Fail closed for a
        # PR-creation attempt; allow all other commands — a gate hiccup must
        # not block unrelated Bash commands (the hook runs on every Bash call).
        # Mirrors the existing unparseable-branch semantics (block iff PR-shaped).
        # Best-effort: wrap the block message so a write failure can't re-raise.
        if looks_like_gh_pr_create(command):
            try:
                sys.stderr.write(
                    "[pre-pr] BLOCKED: unexpected gate exception — set "
                    "DD_SKIP_PR_REVIEW=1 to bypass.\n"
                )
            except Exception:
                pass
            return 2
        return 0


if __name__ == "__main__":
    sys.exit(main())
