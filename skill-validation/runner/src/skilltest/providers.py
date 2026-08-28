"""Fixed local CLI invocation for the built-in providers."""

from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass
from pathlib import Path

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


def invoke_provider(request: ProviderRequest) -> ProviderResult:
    """Invoke one configured built-in CLI without a shell."""
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


def _arguments(request: ProviderRequest) -> list[str]:
    if request.provider == "codex":
        return [
            "codex", "--cd", str(request.workspace_dir), "exec", "--ephemeral",
            "--skip-git-repo-check", "--json",
            "--color", "never", "--model", request.model, "-c",
            f'model_reasoning_effort="{request.effort}"', "--sandbox", "workspace-write",
            "--output-last-message", str(request.final_output_path), "-",
        ]
    if request.provider == "claude":
        return [
            "claude", "--print", "--no-session-persistence", "--model", request.model,
            "--effort", request.effort,
        ]
    raise ValueError(f"unsupported provider: {request.provider}")
