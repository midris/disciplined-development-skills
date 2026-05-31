#!/usr/bin/env python3
"""replay_codex.py — codex parallel of ``replay_review.py``.

Replays a historical sha through ``codex review`` with chosen
(model, effort, strategy) and records duration + findings to
``experiments/results.csv`` (shared with the claude harness — model
names don't collide).

Strategies
----------

``fetched``
    Production-today invocation: ``codex review --base <ref>``. Codex
    fetches its own diff; no custom instructions piped in.

``stuffed``
    ``codex review -`` with skill content + diff piped on stdin. No
    ``--base`` flag (codex review rejects ``--base`` combined with a
    custom prompt). This is the codex parallel of claude stuffed mode:
    we provide the full review context inline and codex doesn't fetch
    the diff itself.

Outputs
-------

* ``results.csv`` — one row per run (appended). Model col
  carries the codex model slug (e.g. ``gpt-5.5``); effort/strategy
  cols are reused.
* ``runs/<run_id>.txt`` — full stdout/stderr per run.
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

# parents[2] = the disciplined-development dir (contains the `hooks` package);
# parents[5] = the repo root (default worktree).
_SKILL_DIR = pathlib.Path(__file__).resolve().parents[2]
REPO_ROOT = pathlib.Path(__file__).resolve().parents[5]
sys.path.insert(0, str(_SKILL_DIR))

from hooks.lib import severity  # noqa: E402


CODEX_MODELS = (
    "gpt-5.5",
    "gpt-5.4",
    "gpt-5.4-mini",
    "gpt-5.3-codex",
    "gpt-5.3-codex-spark",
    "gpt-5.2",
)
CODEX_EFFORTS = ("low", "medium", "high", "xhigh")
CODEX_STRATEGIES = ("fetched", "stuffed")


def codex_argv(model: str, effort: str) -> list[str]:
    return [
        "codex", "review",
        "-c", f'model="{model}"',
        "-c", f'model_reasoning_effort="{effort}"',
    ]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("sha")
    ap.add_argument("base")
    ap.add_argument("model", choices=CODEX_MODELS)
    ap.add_argument("effort", choices=CODEX_EFFORTS)
    ap.add_argument("strategy", choices=CODEX_STRATEGIES)
    ap.add_argument("--timeout", type=int, default=900,
                    help="watchdog seconds; default 900")
    ap.add_argument("--worktree", default=None,
                    help="run codex with cwd in this path instead of REPO_ROOT. "
                         "Use the clean worktree at the sha (e.g. /tmp/dd-replay-clean) "
                         "to avoid current-master contamination.")
    args = ap.parse_args()

    cwd = pathlib.Path(args.worktree).resolve() if args.worktree else REPO_ROOT

    # Guard: HEAD must equal sha. ``codex review --base <ref>`` (fetched mode)
    # and the claude fetched prompt both diff base...HEAD, so a worktree
    # whose HEAD has moved past the requested sha would silently review a
    # different diff while the results.csv row claims the historical sha.
    # Catches the misconfiguration regardless of strategy.
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

    # Validate that base is a real commit (not a typo'd / concatenated sha).
    # ``codex review --base <ref>`` fails INSIDE codex on bad refs and then
    # waits on an interactive recovery prompt — manifests as a 900 s timeout
    # in the harness. ``cat-file -t`` actually probes object storage; plain
    # ``rev-parse`` only validates the hex format.
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

    argv = codex_argv(args.model, args.effort)
    stdin_text: str | None = None
    if args.strategy == "fetched":
        argv += ["--base", args.base]
    else:  # stuffed: pipe skill + diff on stdin, no --base
        skill_md_path = REPO_ROOT / ".claude/skills/adversarial-review/SKILL.md"
        skill_md = skill_md_path.read_text()
        diff_proc = subprocess.run(
            ["git", "diff", f"{args.base}...{args.sha}"],
            capture_output=True, text=True, cwd=str(cwd),
        )
        diff_text = diff_proc.stdout
        paths_proc = subprocess.run(
            ["git", "diff", "--name-status", f"{args.base}...{args.sha}"],
            capture_output=True, text=True, cwd=str(cwd),
        )
        paths_csv = ",".join(
            (parts[1] if not parts[0].startswith("R") else parts[2])
            for parts in (ln.split("\t") for ln in paths_proc.stdout.splitlines() if ln)
            if len(parts) >= 2
        )
        stdin_text = (
            skill_md
            + "\n\n## Review context\n\n"
            f"Review base: `{args.base}`\n"
            f"HEAD sha: `{args.sha}`\n"
            f"Touched paths (CSV): `{paths_csv}`\n"
            "\nThe full diff is stuffed below. Do NOT run `git diff` — read\n"
            "it directly.\n\n"
            "## Diff\n\n"
            "```diff\n"
            f"{diff_text}\n"
            "```\n\n"
            "Report findings using the severity rubric from the adversarial-review\n"
            "skill above (`[P0]` / `[P1]` / `[P2]` / `[P3]`, one finding per line\n"
            "at line-start so the severity counter matches).\n"
        )
        argv.append("-")  # tell codex to read prompt from stdin

    prompt_chars = len(stdin_text) if stdin_text else 0
    print(
        f"=== {args.sha[:10]}  {args.model}/{args.effort}  {args.strategy} ===",
        file=sys.stderr,
    )
    print(f"cwd:    {cwd}", file=sys.stderr)
    print(f"prompt: {prompt_chars} chars piped on stdin", file=sys.stderr)
    print(f"argv:   {' '.join(argv)}", file=sys.stderr)

    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_id = f"{args.sha[:10]}-codex-{args.model}-{args.effort}-{args.strategy}-{ts}"
    runs_dir = pathlib.Path(__file__).resolve().parent / "runs"
    runs_dir.mkdir(parents=True, exist_ok=True)
    out_path = runs_dir / f"{run_id}.txt"

    t0 = time.monotonic()
    try:
        proc = subprocess.run(
            argv,
            input=stdin_text or "",
            capture_output=True,
            text=True,
            cwd=str(cwd),
            timeout=args.timeout,
        )
        exit_code = proc.returncode
        exit_reason = "ok" if exit_code == 0 else f"rc={exit_code}"
        stdout = proc.stdout
        stderr = proc.stderr
    except subprocess.TimeoutExpired as exc:
        exit_code = -1
        exit_reason = "timeout"
        stdout = exc.stdout.decode() if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr = exc.stderr.decode() if isinstance(exc.stderr, bytes) else (exc.stderr or "")
    duration_s = time.monotonic() - t0

    out_path.write_text(
        f"# run_id={run_id}\n"
        f"# sha={args.sha}  base={args.base}\n"
        f"# reviewer=codex  model={args.model}  effort={args.effort}  strategy={args.strategy}\n"
        f"# cwd={cwd}\n"
        f"# exit_code={exit_code}  exit_reason={exit_reason}\n"
        f"# duration_s={duration_s:.1f}\n"
        f"# prompt_chars={prompt_chars}\n\n"
        f"=== STDOUT ===\n{stdout}\n"
        f"=== STDERR ===\n{stderr}\n"
    )

    p0, p1, p2, p3 = severity.count_severities(stdout, line_start=True)

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
            f"{duration_s:.1f}", exit_code, exit_reason,
            prompt_chars, len(stdout),
            p0, p1, p2, p3, str(out_path.relative_to(REPO_ROOT)),
        ])

    print(
        f"duration: {duration_s:.1f}s  exit: {exit_code} ({exit_reason})",
        file=sys.stderr,
    )
    print(f"findings: p0={p0} p1={p1} p2={p2} p3={p3}", file=sys.stderr)
    print(f"output:   {out_path.relative_to(REPO_ROOT)}", file=sys.stderr)
    return 0 if exit_code == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
