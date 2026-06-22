#!/usr/bin/env python3
"""pre_pr_review.py — PreToolUse Bash gate: the only hard block.

Detects `gh pr create`, extracts the target cwd, and delegates to
`dd_review_runner.py pre-pr` with `DD_HARD_BLOCK=1` so a blocking review exits
non-zero and stops the PR open. **Detect + extract + delegate** — no review,
base-resolution, or severity logic lives here; that is `dd_review_runner`'s job.

Base priority: git config `branch.<cur>.gh-merge-base` (read in the target cwd)
→ none (dd_review_runner then falls back to fork-base = merge-base vs trunk).
Target cwd: a chained `cd` in the command.

Deliberately 2-step, NOT gh's old 3-step: the legacy chain had a third
`gh repo view → defaultBranchRef` step; dropped. When neither the
`gh-merge-base` config key is set, dd_review_runner's fork-base covers the common
case (the PR targets trunk → fork-base equals the PR diff). Accepted edge: if a
repo's gh default branch differs from `trunk_branches` AND no `--base` is
given, the gate reviews a slightly different range than the PR opens against —
fixed by setting `branch.<cur>.gh-merge-base`. (See plan E2 + the chained-`cd`
non-Bash-semantics caveat.)

Bypass: `DD_SKIP_PR_REVIEW=1` (launching shell) → exit 0. A non-`gh pr create`
Bash command → exit 0 (lets every other command through).
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

from hooks.lib import logging_setup  # noqa: E402
from hooks.lib.command_match import (  # noqa: E402
    find_gh_pr_create,
    looks_like_gh_pr_create,
)

HOOK_NAME = "pre_pr_review"


def _dd_review_script() -> str:
    """Path to the dd_review_runner engine. `DD_REVIEW_SCRIPT` overrides it (test
    seam: tests point this at a recording shim run by the same interpreter)."""
    return os.environ.get("DD_REVIEW_SCRIPT") or str(_HERE / "dd_review_runner.py")


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


def _git(cwd: str, *args: str) -> tuple[int, str]:
    try:
        r = subprocess.run(
            ["git", "-C", cwd, *args], capture_output=True, text=True, timeout=5
        )
    except Exception:
        return 1, ""
    return r.returncode, r.stdout.strip()


def _gh_merge_base(cwd: str) -> str:
    """`git config branch.<cur>.gh-merge-base` read in `cwd`, or ''.

    The wrapper reads this inline: resolve the current branch, then its
    `gh-merge-base` config key."""
    rc, branch = _git(cwd, "rev-parse", "--abbrev-ref", "HEAD")
    if rc != 0 or not branch:
        return ""
    rc, val = _git(cwd, "config", f"branch.{branch}.gh-merge-base")
    return val if rc == 0 else ""


def main() -> int:
    logger = logging_setup.setup(HOOK_NAME)

    if os.environ.get("DD_SKIP_PR_REVIEW") == "1":
        logger.emit("skip", reason="env_bypass")
        return 0

    command = _read_command()
    cwd = find_gh_pr_create(command)
    if cwd is None:
        if looks_like_gh_pr_create(command):
            # Looks like `gh pr create` but the target directory couldn't be
            # resolved (e.g. a chained `cd` to a shell variable / command
            # substitution, or a heredoc that made strict parsing fail). The
            # only hard block must not fail open — fail loud and make the model
            # rewrite it or set the bypass.
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
        # Not `gh pr create` — let every other Bash command through.
        return 0

    # Base comes only from gh-merge-base config (command base extraction removed).
    base = _gh_merge_base(cwd)

    argv = [sys.executable, _dd_review_script(), "pre-pr"]
    if base:
        argv += ["--base", base]
    # Forward --cwd only when a chained `cd` actually retargeted the dir.
    # find_gh_pr_create returns the process cwd when there is no `cd`, so
    # compare against it (realpath, to ignore /private symlink representation)
    # — forwarding the process cwd would be a redundant no-op for dd_review_runner.
    if cwd and os.path.realpath(cwd) != os.path.realpath(os.getcwd()):
        argv += ["--cwd", cwd]

    env = dict(os.environ)
    env["DD_HARD_BLOCK"] = "1"
    logger.emit("delegate", base=base or "", cwd=cwd or "")
    # No outer timeout (review P3, dismissed): dd_review_runner self-bounds — its git
    # probes (5s/60s) and reviewer_runner's watchdog (Popen.wait timeout +
    # SIGTERM/SIGKILL + bounded reader-thread joins) guarantee it returns, so
    # the delegated process can't wedge indefinitely. An outer timeout here
    # would be redundant defense-in-depth.
    result = subprocess.run(argv, env=env, capture_output=True, text=True)

    # Exit-code translation is load-bearing: Claude Code blocks a PreToolUse
    # tool ONLY on exit 2; any OTHER non-zero is a non-blocking error and the
    # tool (gh pr create) still runs. dd_review_runner pre-pr returns 1 on a BLOCK
    # (findings) or tooling ERROR under DD_HARD_BLOCK, so we must map any
    # non-zero delegate result to 2 — and re-emit the review on stderr (exit-2
    # stderr is what CC feeds back to the model), so the findings aren't lost.
    out = (result.stdout or "") + (result.stderr or "")
    if result.returncode != 0:
        logger.emit("block", dd_exit=result.returncode)
        sys.stderr.write(out)
        return 2
    # Clean pass (or advisory) — surface the output and let the PR through.
    sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
