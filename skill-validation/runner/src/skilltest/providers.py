"""Fixed local CLI invocation for the built-in providers."""

from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Callable

from skilltest.codex_runtime import CodexRuntime, PreparationError

PROVIDER_TIMEOUT_SECONDS = 900
TERMINATE_GRACE_SECONDS = 5
CLAUDE_BASELINE_ENV = {
    "CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT": "1",
    "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1",
    "CLAUDE_CODE_DISABLE_BUNDLED_SKILLS": "1",
    "CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS": "1",
    "CLAUDE_CODE_DISABLE_WORKFLOWS": "1",
    "CLAUDE_CODE_DISABLE_ARTIFACT": "1",
    "CLAUDE_CODE_DISABLE_CRON": "1",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
}


@dataclass(frozen=True, slots=True)
class ProviderRequest:
    workspace_dir: Path
    prompt_bytes: bytes
    final_output_path: Path
    provider: str
    model: str
    effort: str


@dataclass(frozen=True, slots=True)
class ProviderResult:
    executable: str
    invocation_started: bool
    exit_code: int | None = None
    timed_out: bool = False
    launch_error: str | None = None
    stdout_bytes: bytes = b""
    stderr_bytes: bytes = b""
    preparation_error: str | None = None
    cleanup_error: str | None = None


def invoke_provider(request: ProviderRequest, *, log: Callable[[str], None] = lambda message: None) -> ProviderResult:
    """Invoke one configured built-in CLI without a shell."""
    if request.provider == "codex":
        return _invoke_codex(request, log)
    arguments = _arguments(request)
    environment = os.environ | CLAUDE_BASELINE_ENV if request.provider == "claude" else None
    try:
        process = subprocess.Popen(
            arguments, cwd=request.workspace_dir, shell=False, stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env=environment,
        )
    except (OSError, ValueError) as error:
        return ProviderResult(arguments[0], False, launch_error=str(error))
    try:
        stdout_bytes, stderr_bytes = process.communicate(
            input=request.prompt_bytes, timeout=PROVIDER_TIMEOUT_SECONDS
        )
    except subprocess.TimeoutExpired:
        process.terminate()
        try:
            stdout_bytes, stderr_bytes = process.communicate(
                timeout=TERMINATE_GRACE_SECONDS
            )
        except subprocess.TimeoutExpired:
            process.kill()
            stdout_bytes, stderr_bytes = process.communicate()
        return ProviderResult(
            arguments[0], True, process.returncode, True,
            stdout_bytes=stdout_bytes, stderr_bytes=stderr_bytes,
        )
    if process.returncode != 0:
        return ProviderResult(
            arguments[0], True, process.returncode,
            stdout_bytes=stdout_bytes, stderr_bytes=stderr_bytes,
        )
    return ProviderResult(
        arguments[0], True, process.returncode, stdout_bytes=stdout_bytes,
        stderr_bytes=stderr_bytes,
    )


def _invoke_codex(request: ProviderRequest, log: Callable[[str], None]) -> ProviderResult:
    runtime = CodexRuntime(log)
    result = ProviderResult("codex", False)
    cleanup_error = None
    try:
        try:
            runtime.prepare(request.workspace_dir / "fixture")
            arguments = _arguments(request, executable=runtime.executable)
            log(f"provider arguments: {arguments!r}")
            log("provider invocation attempted")
        except PreparationError as error:
            result = replace(result, preparation_error=str(error))
        except (OSError, ValueError):
            result = replace(result, preparation_error="Codex runtime preparation failed")
        else:
            try:
                process = subprocess.Popen(
                    arguments, cwd=request.workspace_dir / "fixture", shell=False,
                    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                    env=runtime.environment, start_new_session=True,
                )
            except (OSError, ValueError) as error:
                result = replace(result, launch_error=str(error))
            else:
                stdout, stderr, timed_out = runtime.communicate(process, request.prompt_bytes, PROVIDER_TIMEOUT_SECONDS)
                result = ProviderResult(
                    "codex", True, process.returncode, timed_out,
                    stdout_bytes=stdout, stderr_bytes=stderr,
                )
    finally:
        cleanup_error = runtime.cleanup()
        if cleanup_error:
            try:
                log(cleanup_error)
            except OSError:
                pass  # The returned result still reports the cleanup failure.
    return replace(result, cleanup_error=cleanup_error)


def _arguments(request: ProviderRequest, *, executable: str = "codex") -> list[str]:
    if request.provider == "codex":
        return [
            executable, "--cd", str(request.workspace_dir / "fixture"), "exec", "--ephemeral",
            "--skip-git-repo-check", "--json",
            "--color", "never", "--model", request.model, "-c",
            f'model_reasoning_effort="{request.effort}"', "--sandbox", "workspace-write",
            "--add-dir", str(request.workspace_dir / "evidence"),
            "--ignore-user-config", "--ignore-rules", "-c", 'shell_environment_policy.inherit="none"',
            "-c", 'cli_auth_credentials_store="file"', "-c", 'approval_policy="never"',
            "--output-last-message", str(request.final_output_path), "-",
        ]
    if request.provider == "claude":
        return [
            "claude", "--print", "--no-session-persistence", "--model", request.model,
            "--effort", request.effort, "--permission-mode", "acceptEdits",
        ]
    raise ValueError(f"unsupported provider: {request.provider}")
