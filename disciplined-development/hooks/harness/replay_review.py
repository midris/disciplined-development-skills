#!/usr/bin/env python3
"""replay_review.py — replay a historical sha through claude with a chosen
(model, effort, strategy) and record duration + findings.

Reuses prompt assembly + Popen plumbing from the live hooks/ code so the
replay matches production behavior except for the three knobs being varied:
``--model``, ``--effort``, and whether the diff is stuffed in the
prompt or fetched by claude via the ``Bash(git diff:*)`` tool allowlist.

Outputs:
  <harness>/results.csv        — one row per run (appended)
  <harness>/runs/<run_id>.txt  — full stdout/stderr per run
"""

from __future__ import annotations

import argparse
import csv
import datetime
import os
import pathlib
import subprocess
import sys
import time

# harness lives at <repo>/.claude/skills/disciplined-development/hooks/harness/.
# parents[2] = the disciplined-development dir (contains the `hooks` package);
# parents[5] = the repo root (default worktree).
_SKILL_DIR = pathlib.Path(__file__).resolve().parents[2]
REPO_ROOT = pathlib.Path(__file__).resolve().parents[5]
sys.path.insert(0, str(_SKILL_DIR))

from hooks.lib import claude_runner, review_prompt, severity  # noqa: E402


CLAUDE_TOOLS = (
    "Read,Grep,Glob,Skill,TodoWrite,"
    "Bash(git diff:*),Bash(git log:*),Bash(git show:*),"
    "Bash(git rev-parse:*),Bash(git status:*),"
    "Bash(git diff-tree:*),Bash(git for-each-ref:*)"
)


def claude_argv(model: str, effort: str) -> list[str]:
    return [
        "claude", "-p",
        "--model", model,
        "--effort", effort,
        "--tools", CLAUDE_TOOLS,
        "--no-session-persistence",
        "--disable-slash-commands",
        "--exclude-dynamic-system-prompt-sections",
    ]


def get_diff(base: str, sha: str, cwd: pathlib.Path) -> str:
    r = subprocess.run(
        ["git", "diff", f"{base}...{sha}"],
        capture_output=True, text=True, cwd=cwd,
    )
    return r.stdout


def gather_paths_csv(base: str, sha: str, cwd: pathlib.Path) -> str:
    """Same logic as review_prompt.gather_touched_paths but pinned to <base>...<sha>."""
    r = subprocess.run(
        ["git", "diff", "--name-status", f"{base}...{sha}"],
        capture_output=True, text=True, cwd=cwd,
    )
    if r.returncode != 0:
        return ""
    full: list[str] = []
    for line in r.stdout.splitlines():
        if not line:
            continue
        parts = line.split("\t")
        status = parts[0]
        if status.startswith("R") and len(parts) >= 3:
            full.extend([parts[1], parts[2]])
        elif len(parts) >= 2:
            full.append(parts[1])
    return ",".join(full)


def build_prompt(*, sha: str, base: str, paths_csv: str,
                 diff_text: str | None) -> str:
    skill_md_path = REPO_ROOT / ".claude/skills/adversarial-review/SKILL.md"
    skill_md = skill_md_path.read_text()

    if diff_text is None:
        # fetched: identical to production claude prompt assembly
        return review_prompt.build_claude_prompt(
            prompt_header=skill_md,
            base=base, head_sha=sha,
            paths_csv=paths_csv,
        )

    # stuffed: replace the "fetch it yourself" prose with the diff inline
    return (
        skill_md
        + "\n\n## Review context\n\n"
        f"Review base: `{base}`\n"
        f"HEAD sha: `{sha}`\n"
        f"Touched paths (CSV): `{paths_csv}`\n"
        "\nThe full diff is stuffed below. Do NOT run `git diff` — read\n"
        "it directly. You may still use `Read` for current-worktree file\n"
        "context if you need it.\n\n"
        "## Diff\n\n"
        "```diff\n"
        f"{diff_text}\n"
        "```\n\n"
        "Report findings using the severity rubric from the adversarial-review\n"
        "skill above (`[P0]` / `[P1]` / `[P2]` / `[P3]`, one finding per line\n"
        "at line-start so the severity counter matches).\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("sha")
    ap.add_argument("base")
    ap.add_argument("model", choices=["sonnet", "haiku", "opus"])
    ap.add_argument("effort", choices=["low", "medium", "high", "xhigh", "max"])
    ap.add_argument("strategy", choices=["fetched", "stuffed"])
    ap.add_argument("--timeout", type=int, default=900,
                    help="watchdog seconds; default 900 to accommodate high-effort runs")
    ap.add_argument("--worktree", default=None,
                    help="run claude with cwd in this path instead of REPO_ROOT. "
                         "Useful for replaying from a clean git worktree at the sha "
                         "(no experiment artifacts visible to Read/Grep).")
    args = ap.parse_args()

    cwd = pathlib.Path(args.worktree).resolve() if args.worktree else REPO_ROOT

    # Guard: HEAD must equal sha. ``review_prompt.build_claude_prompt`` tells
    # claude to fetch ``git diff <base>...HEAD`` (fetched mode), so a
    # worktree whose HEAD has drifted past the requested sha would silently
    # review a different diff while the results.csv row claims the historical
    # sha. Stuffed mode is technically safe (we pass base...sha to git
    # diff explicitly), but enforce the guard in both modes so misconfigured
    # invocations fail fast instead of producing strategy-conditional bugs.
    head_proc = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        capture_output=True, text=True, cwd=str(cwd),
    )
    head_sha = head_proc.stdout.strip()
    if head_sha != args.sha:
        raise SystemExit(
            f"worktree HEAD ({head_sha[:10]}) != requested sha ({args.sha[:10]}) "
            f"in cwd={cwd}. Pin a worktree at the sha (e.g. `git worktree add "
            f"/tmp/dd-replay-clean {args.sha[:10]}`) and pass --worktree."
        )

    # Validate that base is a real commit. ``rev-parse`` only validates the
    # hex format; ``cat-file -t`` actually probes object storage. A typo'd
    # base sha would silently produce an empty diff in stuffed mode and
    # in fetched mode would surface as a noisy claude error mid-review.
    base_proc = subprocess.run(
        ["git", "cat-file", "-t", args.base],
        capture_output=True, text=True, cwd=str(cwd),
    )
    if base_proc.returncode != 0 or base_proc.stdout.strip() != "commit":
        raise SystemExit(
            f"base ref {args.base[:10]} is not a real commit in worktree {cwd}. "
            f"git cat-file -t exited rc={base_proc.returncode}: "
            f"{base_proc.stderr.strip()}"
        )

    paths_csv = gather_paths_csv(args.base, args.sha, cwd)
    diff_text = get_diff(args.base, args.sha, cwd) if args.strategy == "stuffed" else None
    prompt = build_prompt(
        sha=args.sha, base=args.base,
        paths_csv=paths_csv, diff_text=diff_text,
    )

    prompt_chars = len(prompt)
    print(
        f"=== {args.sha[:10]}  {args.model}/{args.effort}  {args.strategy} ===",
        file=sys.stderr,
    )
    print(f"prompt: {prompt_chars} chars (~{prompt_chars // 4} tokens est.)",
          file=sys.stderr)

    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_id = f"{args.sha[:10]}-{args.model}-{args.effort}-{args.strategy}-{ts}"
    runs_dir = pathlib.Path(__file__).resolve().parent / "runs"
    runs_dir.mkdir(parents=True, exist_ok=True)
    out_path = runs_dir / f"{run_id}.txt"

    argv = claude_argv(args.model, args.effort)
    # claude_runner.Runner Popens without an explicit cwd so it inherits ours.
    # chdir to `cwd` (which is REPO_ROOT when --worktree is omitted, else the
    # pinned worktree) so claude's Bash(git ...) and Read see the right tree.
    # Without this, launching the harness from outside the repo would make
    # the prompt-assembly read the right files (via REPO_ROOT) but claude
    # tool-fetch from the caller's cwd, producing contaminated replay rows.
    os.chdir(cwd)
    print(f"cwd:    {cwd}", file=sys.stderr)
    t0 = time.monotonic()
    result = claude_runner.Runner(
        argv=argv, timeout_s=args.timeout, stdin_text=prompt,
    ).run()
    duration_s = time.monotonic() - t0

    out_path.write_text(
        f"# run_id={run_id}\n"
        f"# sha={args.sha}  base={args.base}\n"
        f"# model={args.model}  effort={args.effort}  strategy={args.strategy}\n"
        f"# exit_code={result.exit_code}  exit_reason={result.exit_reason}\n"
        f"# duration_s={duration_s:.1f}\n"
        f"# prompt_chars={prompt_chars}\n\n"
        f"=== STDOUT ===\n{result.stdout}\n"
        f"=== STDERR ===\n{result.stderr}\n"
    )

    p0, p1, p2, p3 = severity.count_severities(result.stdout, line_start=True)

    csv_path = pathlib.Path(__file__).resolve().parent / "results.csv"
    write_header = not csv_path.exists()
    with open(csv_path, "a", newline="") as fh:
        w = csv.writer(fh)
        if write_header:
            w.writerow([
                "timestamp", "sha", "base", "model", "effort", "strategy",
                "duration_s", "exit_code", "exit_reason",
                "prompt_chars", "stdout_chars",
                "p0", "p1", "p2", "p3", "output_file",
            ])
        w.writerow([
            ts, args.sha, args.base, args.model, args.effort, args.strategy,
            f"{duration_s:.1f}", result.exit_code, result.exit_reason,
            prompt_chars, len(result.stdout),
            p0, p1, p2, p3, str(out_path.relative_to(REPO_ROOT)),
        ])

    print(
        f"duration: {duration_s:.1f}s  exit: {result.exit_code} ({result.exit_reason})",
        file=sys.stderr,
    )
    print(f"findings: p0={p0} p1={p1} p2={p2} p3={p3}", file=sys.stderr)
    print(f"output:   {out_path.relative_to(REPO_ROOT)}", file=sys.stderr)
    return 0 if result.exit_code == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
