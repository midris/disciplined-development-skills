#!/usr/bin/env python3
"""log_review.py — model-callable tool: attempt one review row + fold the reset.

Reads aggregated reviewer findings on **stdin**, attempts one ``reviews.jsonl``
append via ``append_review``, and — only on a clean (PASS) result — folds in the
cadence reset: independently attempts to clear the unreviewed-``edits`` counter
and stamp ``review.checkpoint = HEAD`` regardless of trace persistence.
BLOCK/ERROR attempts neither state write. Because state is best-effort rather
than transactional, either failed PASS write retains conservative review
pressure. Every input must end with an explicit
``DD-VERDICT: PASS|BLOCK``; findings remain telemetry-only.

Exit 0 on success. Exit 2 on a usage error: argparse handles a missing/invalid
required flag; explicit guards handle empty stdin and a missing/malformed final
verdict. A log-write failure never
blocks — ``append_review`` degrades to a stderr warning and this tool still
exits 0.
"""

from __future__ import annotations

import argparse
import pathlib
import sys

_HERE = pathlib.Path(__file__).resolve().parent
_BASE_DIR = _HERE.parent  # the dir containing the `hooks` package
if str(_BASE_DIR) not in sys.path:
    sys.path.insert(0, str(_BASE_DIR))

from hooks.lib import logging_setup, review_record, severity, state  # noqa: E402


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="log_review.py",
        description="Attempt one review row; fold the cadence reset on a clean result.",
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
        # A blank pipe has no explicit decision and must not fire the reset-fold.
        print("[log-review] refusing empty/whitespace-only findings on stdin "
              "(an explicit final verdict is required).", file=sys.stderr)
        return 2

    decision = severity.parse_verdict(findings)
    if decision is None:
        print(
            "[log-review] findings must end with DD-VERDICT: PASS or "
            "DD-VERDICT: BLOCK.",
            file=sys.stderr,
        )
        return 2

    # Key state off the git top-level, not the raw cwd: state paths are a
    # literal `<repo>/.claude/.dd-state` join, so a subdir cwd would write a
    # stray tree and the reset-fold would silently miss the counter the cadence
    # hooks track at the root. Fall back to the raw cwd outside a git repo.
    start = args.cwd or str(pathlib.Path.cwd())
    repo = state.repo_root(start) or start
    branch = state.current_branch(repo)

    context = review_record.gather_cadence_context(repo, branch)
    record = review_record.build_review_record(
        findings=findings,
        source=args.source,
        reviewer=args.reviewer,
        trigger=args.trigger,
        round=args.round,
        context=context,
        decision=decision,
    )
    logging_setup.append_review(record)  # degrade-safe; never raises

    # A PASS independently attempts both best-effort state writes. A partial
    # failure retains edit or commit review pressure; BLOCK/ERROR attempts neither.
    if record["decision"] == "PASS":
        state.reset(repo, branch, "edits")
        head = context["head_sha"]
        if head:
            state.set_checkpoint(repo, branch, head)

    return 0


if __name__ == "__main__":
    sys.exit(main())
