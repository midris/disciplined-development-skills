"""Fixed local CLI invocation for the built-in providers."""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

PROVIDER_TIMEOUT_SECONDS = 900
TERMINATE_GRACE_SECONDS = 5


@dataclass(frozen=True, slots=True)
class ProviderRequest:
    workspace_dir: Path
    subject_input_bytes: bytes
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


def invoke_provider(request: ProviderRequest) -> ProviderResult:
    """Invoke one configured built-in CLI without a shell."""
    arguments = _arguments(request)
    try:
        process = subprocess.Popen(
            arguments, cwd=request.workspace_dir, shell=False, stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
    except (OSError, ValueError) as error:
        return ProviderResult(arguments[0], False, launch_error=str(error))
    try:
        stdout_bytes, stderr_bytes = process.communicate(
            input=request.subject_input_bytes, timeout=PROVIDER_TIMEOUT_SECONDS
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


def _arguments(request: ProviderRequest) -> list[str]:
    if request.provider == "codex":
        return [
            "codex", "--ask-for-approval", "never", "--search", "--cd",
            str(request.workspace_dir), "exec", "--strict-config", "--ignore-user-config",
            "--ignore-rules", "--ephemeral", "--skip-git-repo-check", "--json",
            "--color", "never", "--model", request.model, "-c",
            f'model_reasoning_effort="{request.effort}"', "--sandbox", "workspace-write",
            "--output-last-message", str(request.final_output_path.resolve()), "-",
        ]
    if request.provider == "claude":
        return [
            "claude", "--print", "--safe-mode", "--no-session-persistence", "--no-chrome",
            "--input-format", "text", "--output-format", "stream-json", "--verbose",
            "--model", request.model, "--effort", request.effort,
            "--allow-dangerously-skip-permissions", "--permission-mode", "bypassPermissions",
        ]
    raise ValueError(f"unsupported provider: {request.provider}")
