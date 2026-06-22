#!/usr/bin/env python3
"""external_review.py — whole-repo, verdict-driven, fail-closed gate tool.

Usage:
    python3 external_review.py [--cwd <path>]

Runs a whole-repo codex review anchored to the active plan and the adversarial-
review skill pointer.  Reads the declared ``DD-VERDICT: PASS|BLOCK`` from the
codex last-message file (``-o``), logs every attempt to ``reviews.jsonl``, and
exits 0 only on PASS.  Fail-closed: every other outcome (BLOCK, no verdict,
missing binary, timeout, empty output) exits non-zero.

The hook (``pre_pr_review.py``) is wired to this tool in Task 2.3.  This file
is invokable standalone for development / smoke testing.

Config keys consumed (from ``review.*``, resolved via ``lib/config.py``):
  ``review.prompt_path``  — path to the adversarial-review skill (the pointer,
                             not its body; codex reads it itself).
  ``review.reviewer``     — reviewer id logged in the row (currently ``codex``).
  ``review.model``        — codex model override (``-m`` flag).
  ``review.effort``       — codex reasoning effort (``-c model_reasoning_effort``).
  ``codex.pr_review_timeout_s`` — wall-clock timeout in seconds.

Env vars:
  ``DD_CODEX_BIN``      — path to the codex binary (default ``codex``); override
                           for tests so a shim is used instead of the real binary.
  ``DD_CODEX_TIMEOUT``  — timeout override in seconds (float); intended for tests.
"""

from __future__ import annotations

import os
import pathlib
import subprocess
import sys
import tempfile
import time

_HERE = pathlib.Path(__file__).resolve().parent
_BASE_DIR = _HERE.parent  # the dir containing the `hooks` package
if str(_BASE_DIR) not in sys.path:
    sys.path.insert(0, str(_BASE_DIR))

from hooks.lib import (  # noqa: E402
    config,
    logging_setup,
    plan,
    review_record,
    reviewer_runner,
    severity,
    state,
)

_DEFAULT_TIMEOUT_S = 600.0
_SOURCE = "external-gate"
_TRIGGER = "gate:pre-pr"


# ---------------------------------------------------------------------------
# Branch helpers (mirror log_review.py exactly — symbolic-ref + "detached")
# ---------------------------------------------------------------------------


def _current_branch(repo: str) -> str:
    """Current branch via git symbolic-ref; 'detached' on detached HEAD or failure.

    Matches the cadence hooks (edit_counter.py) exactly: ``symbolic-ref --short
    HEAD`` and fall back to the literal ``"detached"`` so the per-branch
    state-dir key is always consistent.
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


# ---------------------------------------------------------------------------
# Timeout resolution
# ---------------------------------------------------------------------------


def _resolve_timeout() -> float:
    """Timeout in seconds: DD_CODEX_TIMEOUT env (test override) → config → default."""
    env_t = os.environ.get("DD_CODEX_TIMEOUT")
    if env_t:
        try:
            return float(env_t)
        except (ValueError, TypeError):
            pass
    val = config.get("codex.pr_review_timeout_s")
    if isinstance(val, (int, float)) and val > 0:
        return float(val)
    return _DEFAULT_TIMEOUT_S


# ---------------------------------------------------------------------------
# Prompt builder
# ---------------------------------------------------------------------------


def _build_prompt(repo: str) -> str:
    """Build a deterministic, plan-anchored prompt for ``codex exec``.

    Includes a pointer to the review skill (resolved against ``repo``) and the
    active-plan path.  Does NOT stuff the skill body — codex reads it itself.
    """
    prompt_path = config.get(
        "review.prompt_path",
        ".claude/skills/adversarial-review/SKILL.md",
    )
    # Resolve against the repo under review (absolute), or keep as-is if already abs.
    if not os.path.isabs(prompt_path):
        skill_pointer = os.path.join(repo, prompt_path)
    else:
        skill_pointer = prompt_path

    # Active plan — resolve with cwd anchored to repo so the fallback glob hits
    # the right plans/ dir.  Env DD_ACTIVE_PLAN wins; otherwise pointer file /
    # newest mtime in plans/*.md relative to the repo.
    active_plan_result = plan.resolve_active_plan(cwd=repo)
    if active_plan_result is not None:
        plan_path, _ = active_plan_result
        plan_section = f"Active plan: {plan_path}"
    else:
        plan_section = "(no active plan found)"

    return (
        f"Review this repository following the review guidelines at: {skill_pointer}\n"
        f"{plan_section}\n"
        f"Review the entire repository against the plan above.\n"
        f"Emit findings as: - [PN] file:line: summary\n"
        f"End with a final line containing only DD-VERDICT: PASS or DD-VERDICT: BLOCK "
        f"(nothing trailing)."
    )


# ---------------------------------------------------------------------------
# Log helper (best-effort — never raises)
# ---------------------------------------------------------------------------


def _log_attempt(
    repo: str,
    branch: str,
    output: str,
    decision: str,
    reason: str | None,
    duration_s: float | None,
    context: dict | None = None,
) -> None:
    """Append one row to reviews.jsonl; swallow all errors (best-effort).

    ``context`` is optional: callers that already called gather_cadence_context
    (e.g. the PASS path, which reuses it for the state reset-fold) pass it in
    to avoid a second round of git subprocesses.
    """
    reviewer = config.get("review.reviewer", "codex")
    model = config.get("review.model")
    effort = config.get("review.effort")
    try:
        ctx = context if context is not None else review_record.gather_cadence_context(repo, branch)
        extra: dict = {}
        if model:
            extra["model"] = model
        if effort:
            extra["effort"] = effort
        row = review_record.build_review_record(
            findings=output,
            source=_SOURCE,
            reviewer=reviewer,
            trigger=_TRIGGER,
            round=1,
            context=ctx,
            decision=decision,
            reason=reason,
            duration_s=duration_s,
            extra=extra if extra else None,
        )
        logging_setup.append_review(row)
    except Exception:
        # Best-effort: a log failure must not crash the gate.
        pass


# ---------------------------------------------------------------------------
# CLI arg parsing
# ---------------------------------------------------------------------------


def _parse_args(argv: list[str]) -> tuple[str | None, str]:
    """Return (cwd_override, error_message).  error_message is '' on success."""
    cwd: str | None = None
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--cwd":
            if i + 1 >= len(argv):
                return None, "--cwd requires a path argument"
            if cwd is not None:
                return None, "--cwd specified twice"
            cwd = argv[i + 1]
            i += 2
        else:
            return None, f"unrecognized argument {arg!r}"
    return cwd, ""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    cwd_override, err = _parse_args(argv)
    if err:
        print(f"[external-review] ERROR — {err}", file=sys.stderr)
        print("Usage: python3 external_review.py [--cwd <path>]", file=sys.stderr)
        return 2

    repo = cwd_override or str(pathlib.Path.cwd())
    if cwd_override and not pathlib.Path(cwd_override).is_dir():
        print(f"[external-review] ERROR — --cwd {cwd_override!r} is not a directory",
              file=sys.stderr)
        return 2

    branch = _current_branch(repo)
    timeout_s = _resolve_timeout()

    # Config values.
    model = config.get("review.model")
    effort = config.get("review.effort")

    # Codex binary — overridable via env for tests.
    codex_bin = os.environ.get("DD_CODEX_BIN", "codex")

    # Build the deterministic prompt.
    prompt = _build_prompt(repo)

    # Build codex exec argv.
    # codex exec --cd <REPO> -m <MODEL> -c model_reasoning_effort=<EFFORT>
    #            -s read-only -o <LAST_MESSAGE_FILE> "<PROMPT>"
    cmd: list[str] = [codex_bin, "exec", "--cd", repo]
    if model:
        cmd.extend(["-m", model])
    if effort:
        cmd.extend(["-c", f"model_reasoning_effort={effort}"])
    cmd.extend(["-s", "read-only"])
    # -o <file> is appended just before the prompt (below, after we have the tmpfile).

    start = time.monotonic()

    # Create a temp file for the last-message output.
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", prefix="dd-external-review-", delete=False
    ) as fh:
        output_file = fh.name

    try:
        full_cmd = cmd + ["-o", output_file, prompt]

        runner = reviewer_runner.Runner(
            argv=full_cmd,
            timeout_s=timeout_s,
            cwd=repo,
        )
        result = runner.run()
        duration_s = time.monotonic() - start

        # --- cli_missing ---
        if result.exit_reason.startswith("error:"):
            output = ""
            _log_attempt(repo, branch, output, "ERROR", "cli_missing", duration_s)
            print(f"[external-review] ERROR — codex binary not found: {codex_bin!r}",
                  file=sys.stderr)
            return 1

        # --- timeout ---
        if result.exit_reason == "timeout":
            output = ""
            _log_attempt(repo, branch, output, "ERROR", "timeout", duration_s)
            print(f"[external-review] ERROR — codex timed out (>{timeout_s}s)",
                  file=sys.stderr)
            return 1

        # --- read the last-message file ---
        try:
            output = pathlib.Path(output_file).read_text(encoding="utf-8", errors="replace")
        except OSError:
            output = ""

        # --- empty_output ---
        if not output.strip():
            _log_attempt(repo, branch, output, "ERROR", "empty_output", duration_s)
            print("[external-review] ERROR — codex produced an empty last-message",
                  file=sys.stderr)
            return 1

        # --- parse verdict ---
        verdict = severity.parse_verdict(output)
        if verdict is None:
            _log_attempt(repo, branch, output, "ERROR", "no_verdict", duration_s)
            print("[external-review] ERROR — no DD-VERDICT line in codex output",
                  file=sys.stderr)
            return 1

        # --- PASS or BLOCK ---
        if verdict == "PASS":
            # Gather ctx once; reuse for both the log row and the state reset-fold
            # (~8 git subprocesses on the happy path if gathered twice).
            ctx = review_record.gather_cadence_context(repo, branch)
            _log_attempt(repo, branch, output, "PASS", None, duration_s, context=ctx)
            # State reset-fold (Decision 2, both on clean result — mirror log_review.py).
            state.reset(repo, branch, "edits")
            head = ctx["head_sha"]
            if head:
                state.set_checkpoint(repo, branch, head)
            print("[external-review] PASS — review clean, gate open.")
            return 0
        else:
            # BLOCK
            _log_attempt(repo, branch, output, "BLOCK", None, duration_s)
            print("[external-review] BLOCK — review found issues, gate closed.",
                  file=sys.stderr)
            return 1

    finally:
        # Clean up the temp file.
        try:
            pathlib.Path(output_file).unlink(missing_ok=True)
        except OSError:
            pass


if __name__ == "__main__":
    sys.exit(main())
