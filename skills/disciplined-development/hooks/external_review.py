#!/usr/bin/env python3
"""Whole-repository, plan-anchored external review gate.

Exit 0 allows; every reviewer BLOCK or execution/setup failure returns non-zero.
The PreToolUse wrapper translates that non-zero result to Claude Code's blocking
exit 2.
"""

from __future__ import annotations

import os
import pathlib
import subprocess
import sys
import tempfile
import time

_HERE = pathlib.Path(__file__).resolve().parent
_BASE_DIR = _HERE.parent
if str(_BASE_DIR) not in sys.path:
    sys.path.insert(0, str(_BASE_DIR))

from hooks.lib import config, logging_setup, plan, review_record, severity, state  # noqa: E402

_DEFAULT_TIMEOUT_S = 600.0
_SOURCE = "external-gate"
_TRIGGER = "gate:pre-pr"
_REPOSITORY_SELECTOR_ENV = ("GH_REPO", "GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR")


def _resolve_timeout() -> float:
    env_timeout = os.environ.get("DD_REVIEW_TIMEOUT")
    if env_timeout:
        try:
            value = float(env_timeout)
            if value > 0:
                return value
        except (TypeError, ValueError):
            pass
    value = config.get("codex.pr_review_timeout_s")
    if isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0:
        return float(value)
    return _DEFAULT_TIMEOUT_S


def _build_prompt(repo: str, active_plan: str) -> str:
    prompt_path = config.get(
        "review.prompt_path", ".claude/skills/adversarial-review/SKILL.md"
    )
    if not isinstance(prompt_path, str) or not prompt_path:
        prompt_path = ".claude/skills/adversarial-review/SKILL.md"
    skill_pointer = (
        prompt_path if os.path.isabs(prompt_path) else os.path.join(repo, prompt_path)
    )
    return (
        f"Review this repository following the review guidelines at: {skill_pointer}\n"
        f"Active plan: {active_plan}\n"
        "Review the entire repository against the plan above.\n"
        "The plan may be phased (chunks/PRs): treat unchecked or explicitly-future "
        "sections as out of scope — planned work, not missing work.\n"
        "Emit findings as: - [PN] file:line: summary\n"
        "End with a final line containing only DD-VERDICT: PASS or DD-VERDICT: BLOCK "
        "(nothing trailing)."
    )


def _log_attempt(
    repo: str,
    branch: str,
    output: str,
    decision: str,
    reason: str | None,
    duration_s: float | None,
    context: dict | None = None,
) -> None:
    try:
        ctx = context or review_record.gather_cadence_context(repo, branch)
        extra = {}
        model = config.get("review.model")
        effort = config.get("review.effort")
        if isinstance(model, str) and model:
            extra["model"] = model
        if isinstance(effort, str) and effort:
            extra["effort"] = effort
        row = review_record.build_review_record(
            findings=output,
            source=_SOURCE,
            reviewer=config.get("review.reviewer", "codex"),
            trigger=_TRIGGER,
            round=1,
            context=ctx,
            decision=decision,
            reason=reason,
            duration_s=duration_s,
            extra=extra or None,
        )
        logging_setup.append_review(row)
    except Exception:
        pass


def _parse_args(argv: list[str]) -> tuple[str | None, str]:
    cwd: str | None = None
    index = 0
    while index < len(argv):
        if argv[index] != "--cwd":
            return None, f"unrecognized argument {argv[index]!r}"
        if index + 1 >= len(argv):
            return None, "--cwd requires a path argument"
        if cwd is not None:
            return None, "--cwd specified twice"
        cwd = argv[index + 1]
        index += 2
    return cwd, ""


def _plan_is_readable(path: str) -> bool:
    try:
        with open(path, "rb") as handle:
            handle.read(1)
        return True
    except (OSError, TypeError):
        return False


def _review_env() -> dict[str, str]:
    clean = dict(os.environ)
    for name in _REPOSITORY_SELECTOR_ENV:
        clean.pop(name, None)
    return clean


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    cwd_override, error = _parse_args(argv)
    if error:
        print(f"[external-review] ERROR — {error}", file=sys.stderr)
        print("Usage: python3 external_review.py [--cwd <path>]", file=sys.stderr)
        return 2
    if cwd_override and not pathlib.Path(cwd_override).is_dir():
        print(
            f"[external-review] ERROR — --cwd {cwd_override!r} is not a directory",
            file=sys.stderr,
        )
        return 2

    start_dir = cwd_override or str(pathlib.Path.cwd())
    repo = state.repo_root(start_dir) or os.path.abspath(start_dir)
    if cwd_override:
        os.environ["CLAUDE_PROJECT_DIR"] = repo
        config.reset_config_cache()

    branch = state.current_branch(repo)
    plan_result = plan.resolve_active_plan(cwd=repo)
    if plan_result is None or not _plan_is_readable(plan_result[0]):
        _log_attempt(repo, branch, "", "ERROR", "plan_unavailable", None)
        print(
            "[external-review] ERROR — active plan unavailable; pin a readable "
            "plan with DD_ACTIVE_PLAN or .claude/active-plan.",
            file=sys.stderr,
        )
        return 1
    active_plan, _ = plan_result

    model = config.get("review.model")
    effort = config.get("review.effort")
    codex_bin = os.environ.get("DD_CODEX_BIN") or "codex"
    command = [codex_bin, "exec", "--cd", repo]
    if isinstance(model, str) and model:
        command.extend(["-m", model])
    if isinstance(effort, str) and effort:
        command.extend(["-c", f"model_reasoning_effort={effort}"])
    command.extend(["-s", "read-only"])
    prompt = _build_prompt(repo, active_plan)
    timeout_s = _resolve_timeout()

    output_file: str | None = None
    started = time.monotonic()
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".txt", prefix="dd-external-review-", delete=False
        ) as handle:
            output_file = handle.name
        full_command = command + ["-o", output_file, prompt]
        try:
            result = subprocess.run(
                full_command,
                cwd=repo,
                capture_output=True,
                text=True,
                check=False,
                timeout=timeout_s,
                env=_review_env(),
            )
        except FileNotFoundError:
            duration = time.monotonic() - started
            _log_attempt(repo, branch, "", "ERROR", "cli_missing", duration)
            print(
                f"[external-review] ERROR — codex binary not found: {codex_bin!r}",
                file=sys.stderr,
            )
            return 1
        except subprocess.TimeoutExpired:
            duration = time.monotonic() - started
            _log_attempt(repo, branch, "", "ERROR", "timeout", duration)
            print(
                f"[external-review] ERROR — codex timed out (>{timeout_s}s)",
                file=sys.stderr,
            )
            return 1
        except OSError:
            duration = time.monotonic() - started
            _log_attempt(repo, branch, "", "ERROR", "cli_missing", duration)
            print("[external-review] ERROR — codex could not be launched", file=sys.stderr)
            return 1

        duration = time.monotonic() - started
        try:
            output = pathlib.Path(output_file).read_text(
                encoding="utf-8", errors="replace"
            )
        except OSError:
            output = ""

        if result.returncode != 0:
            _log_attempt(repo, branch, output, "ERROR", "outage", duration)
            print(
                f"[external-review] ERROR — codex exited abnormally "
                f"(exit_code={result.returncode}); verdict not trusted.",
                file=sys.stderr,
            )
            return 1
        if not output.strip():
            _log_attempt(repo, branch, output, "ERROR", "empty_output", duration)
            print(
                "[external-review] ERROR — codex produced an empty last-message",
                file=sys.stderr,
            )
            return 1
        verdict = severity.parse_verdict(output)
        if verdict is None:
            _log_attempt(repo, branch, output, "ERROR", "no_verdict", duration)
            print(
                "[external-review] ERROR — no DD-VERDICT line in codex output",
                file=sys.stderr,
            )
            return 1
        if verdict == "BLOCK":
            _log_attempt(repo, branch, output, "BLOCK", None, duration)
            print(
                "[external-review] BLOCK — review found issues, gate closed.",
                file=sys.stderr,
            )
            return 1

        context = review_record.gather_cadence_context(repo, branch)
        _log_attempt(repo, branch, output, "PASS", None, duration, context=context)
        # Independent best-effort writes: a partial failure keeps the remaining
        # edit or commit review pressure. BLOCK/ERROR paths attempt neither.
        state.reset(repo, branch, "edits")
        head = context["head_sha"]
        if head:
            state.set_checkpoint(repo, branch, head)
        print("[external-review] PASS — review clean, gate open.")
        return 0
    finally:
        if output_file is not None:
            try:
                pathlib.Path(output_file).unlink(missing_ok=True)
            except OSError:
                pass


if __name__ == "__main__":
    sys.exit(main())
