"""Fixed local CLI invocation for the built-in providers."""

from __future__ import annotations

import subprocess
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Callable

from skilltest.codex_runtime import CodexRuntime
from skilltest.claude_runtime import ClaudeRuntime
from skilltest.runtime import PreparationError

PROVIDER_TIMEOUT_SECONDS = 900


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
        runtime = CodexRuntime(log)
    elif request.provider == "claude":
        runtime = ClaudeRuntime(log)
    else:
        raise ValueError(f"unsupported provider: {request.provider}")
    result = ProviderResult(request.provider, False)
    cleanup_error = None
    try:
        try:
            runtime.prepare(request.workspace_dir / "fixture")
            arguments = runtime.prefix + _arguments(request, executable=runtime.executable)
            log(f"provider arguments: {arguments!r}")
            log("provider invocation attempted")
        except PreparationError as error:
            result = replace(result, preparation_error=str(error))
        except (OSError, ValueError, KeyError):
            result = replace(result, preparation_error=f"{request.provider} runtime preparation failed")
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
                    request.provider, True, process.returncode, timed_out,
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
            executable, "--print", "--no-session-persistence", "--model", request.model,
            "--effort", request.effort, "--permission-mode", "dontAsk", "--permission-prompts", "none",
            "--setting-sources", "project", "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
            "--no-chrome", "--tools", "Read,Skill,Glob,Grep,Write,Edit,Bash",
            "--allowedTools", "Read,Skill,Glob,Grep,Write,Edit,Bash",
            "--add-dir", str(request.workspace_dir / "evidence"), "--output-format", "stream-json", "--verbose",
        ]
    raise ValueError(f"unsupported provider: {request.provider}")
