#!/usr/bin/env python3
"""pre_pr_review.py — the pre-PR PreToolUse Bash hard gate.

Detects a standalone ``gh pr create`` in the payload cwd and delegates to
``external_review.py`` (whole-repo, verdict-driven, fail-closed). No base
resolution and no ``DD_HARD_BLOCK``; the reviewer declares a verdict and the
external gate trusts that decision directly.

Paths:
- PR-shaped + resolved Git target → delegate to
  ``external_review.py --cwd <git-root>``;
  any non-zero result maps to exit 2 (Claude Code blocks PreToolUse ONLY on 2),
  and the delegate's stdout+stderr are re-emitted on stderr. This surfaces gate
  status; full reviewer output is available
  only if the best-effort trace write succeeds.
- PR-shaped + unresolved command or target → attempt one
  ``reviews.jsonl`` ERROR row (decision=ERROR, reason=unparseable), then block
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

from hooks.lib import config, logging_setup, review_record, state  # noqa: E402
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


def _read_payload() -> tuple[str, str | None]:
    try:
        data = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, OSError):
        return "", None
    if not isinstance(data, dict):
        return "", None
    ti = data.get("tool_input")
    command = ti.get("command") if isinstance(ti, dict) else None
    cwd = data.get("cwd")
    return (
        command if isinstance(command, str) else "",
        cwd if isinstance(cwd, str) and cwd else None,
    )


def _log_unparseable(base_cwd: str | None) -> None:
    """Append one ERROR/unparseable review row — best-effort, never raises."""
    try:
        reviewer = config.get("review.reviewer", "codex")
        ctx = {
            "repo": base_cwd or "unresolved",
            "head_sha": None,
            "branch": "unresolved",
            "base": None,
            "edits_count": 0,
            "commits_since_checkpoint": None,
        }
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
        command, base_cwd = _read_payload()
        cwd = find_gh_pr_create(command, base_cwd)
        if cwd is not None:
            cwd = state.repo_root(cwd)
        if cwd is None:
            if looks_like_gh_pr_create(command):
                # Looks like ``gh pr create`` but is not a supported standalone
                # action in a resolved repository.
                # Fail closed: attempt ERROR row + block — do NOT let an unreviewed PR
                # through (the fail-open bug this gate exists to prevent).
                # Never probe the launching process's repository for an
                # unresolved target; the best-effort row uses inert context.
                _log_unparseable(base_cwd)
                logger.emit("block", reason="unresolvable_cwd")
                print(
                    "[pre-pr] BLOCKED: unresolved `gh pr create`. Run "
                    "`gh pr create` as a standalone Bash call from the target "
                    "repository; run other commands separately. Set "
                    "DD_SKIP_PR_REVIEW=1 in the launching shell "
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
        # tool (gh pr create) still runs.  external_review returns 0 on an
        # reviewer PASS and
        # non-zero on a reviewer BLOCK or failure. Map any non-zero to 2 and
        # re-emit the delegate's surfaced status output to the model.
        out = (result.stdout or "") + (result.stderr or "")
        if result.returncode != 0:
            logger.emit("block", ext_exit=result.returncode)
            sys.stderr.write(out)
            return 2
        # Reviewer PASS — surface the output and let the PR through.
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
