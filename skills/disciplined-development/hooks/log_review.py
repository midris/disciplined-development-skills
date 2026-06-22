#!/usr/bin/env python3
"""log_review.py — model-callable tool: log one review row + fold the reset.

Reads aggregated reviewer findings on **stdin**, appends exactly one row to
``reviews.jsonl`` via ``append_review``, and — only on a clean (PASS) result —
folds in the cadence reset: clears the unreviewed-``edits`` counter **and**
stamps ``review.checkpoint = HEAD`` (Decision 2 — always BOTH on a clean
result, NEITHER on BLOCK/ERROR). The decision comes from the shared record
builder (declared verdict → derived from findings), never from this tool.

Exit 0 on success. Exit 2 on a usage error: argparse handles a missing/invalid
required flag; an explicit guard handles empty/whitespace-only stdin (a blank
pipe must not log a false PASS or reset the counter). A log-write failure never
blocks — ``append_review`` degrades to a stderr warning and this tool still
exits 0.
"""

from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

_HERE = pathlib.Path(__file__).resolve().parent
_BASE_DIR = _HERE.parent  # the dir containing the `hooks` package
if str(_BASE_DIR) not in sys.path:
    sys.path.insert(0, str(_BASE_DIR))

from hooks.lib import logging_setup, review_record, state  # noqa: E402


def _current_branch(repo: str) -> str:
    """Current branch of ``repo`` via git symbolic-ref; 'detached' on detached
    HEAD or git failure.

    Matches the cadence hooks (edit_counter.py) exactly: both use
    ``symbolic-ref --short HEAD`` and fall back to the literal ``"detached"``
    so the per-branch state-dir key is always consistent between the hooks and
    this tool.  ``rev-parse --abbrev-ref HEAD`` was the previous approach but
    returns ``"HEAD"`` on a detached HEAD, causing a state-dir key mismatch:
    log_review would read/reset ``.dd-state/HEAD/`` while the hooks used
    ``.dd-state/detached/``, so a clean review never cleared the counter the
    hooks tracked.
    """
    try:
        r = subprocess.run(
            ["git", "-C", repo, "symbolic-ref", "--short", "HEAD"],
            capture_output=True, text=True, check=False, timeout=5,
        )
    except Exception:
        return "detached"
    branch = r.stdout.strip()
    return branch if r.returncode == 0 and branch else "detached"


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="log_review.py",
        description="Log one review row; fold the cadence reset on a clean result.",
    )
    p.add_argument("--source", required=True,
                   choices=["model-review", "external-gate"])
    p.add_argument("--trigger", required=True)
    p.add_argument("--round", type=int, default=1)
    p.add_argument("--reviewer", default="subagents")
    p.add_argument("--cwd", default=None,
                   help="repo to operate on (default: current directory)")
    return p.parse_args(argv)


def main() -> int:
    args = _parse_args()

    if args.round < 1:
        print(f"[log-review] --round must be >= 1, got {args.round}.",
              file=sys.stderr)
        return 2

    findings = sys.stdin.read()
    if not findings.strip():
        # A blank pipe must not log a false PASS or fire the reset-fold.
        print("[log-review] refusing empty/whitespace-only findings on stdin "
              "(would log a false PASS).", file=sys.stderr)
        return 2

    repo = args.cwd or str(pathlib.Path.cwd())
    branch = _current_branch(repo)

    context = review_record.gather_cadence_context(repo, branch)
    record = review_record.build_review_record(
        findings=findings,
        source=args.source,
        reviewer=args.reviewer,
        trigger=args.trigger,
        round=args.round,
        context=context,
    )
    logging_setup.append_review(record)  # degrade-safe; never raises

    # Reset-fold (Decision 2): on a clean result, clear the edits counter AND
    # stamp the checkpoint at HEAD — both, or neither. BLOCK/ERROR leave both.
    if record["decision"] == "PASS":
        state.reset(repo, branch, "edits")
        head = context["head_sha"]
        if head:
            state.set_checkpoint(repo, branch, head)

    return 0


if __name__ == "__main__":
    sys.exit(main())
