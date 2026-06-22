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
    """Current branch of ``repo`` via a git read; '' when git is unavailable."""
    try:
        r = subprocess.run(
            ["git", "-C", repo, "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, check=False, timeout=5,
        )
    except Exception:
        return ""
    return r.stdout.strip() if r.returncode == 0 else ""


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="log_review.py",
        description="Log one review row; fold the cadence reset on a clean result.",
    )
    p.add_argument("--source", required=True,
                   choices=["model-review", "external-gate"])
    p.add_argument("--trigger", required=True)
    p.add_argument("--round", type=int, default=None)
    p.add_argument("--reviewer", default=None)
    p.add_argument("--cwd", default=None,
                   help="repo to operate on (default: current directory)")
    return p.parse_args(argv)


def main() -> int:
    args = _parse_args()

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
