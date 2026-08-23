"""Fixed local CLI invocation for the built-in providers."""

from __future__ import annotations

import json
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
    final_output_bytes: bytes | None = None
    output_error: str | None = None


def invoke_provider(request: ProviderRequest) -> ProviderResult:
    """Invoke one configured built-in CLI without a shell."""
    arguments = _arguments(request)
    try:
        process = subprocess.Popen(
            arguments, cwd=request.workspace_dir, shell=False, stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
    except OSError as error:
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
    final_output_bytes, output_error = _final_output(request, stdout_bytes)
    return ProviderResult(
        arguments[0], True, process.returncode, stdout_bytes=stdout_bytes,
        stderr_bytes=stderr_bytes, final_output_bytes=final_output_bytes,
        output_error=output_error,
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


def _final_output(request: ProviderRequest, stdout_bytes: bytes) -> tuple[bytes | None, str | None]:
    if request.provider == "codex":
        if not request.final_output_path.is_file():
            return None, "Codex did not write final output"
        return request.final_output_path.read_bytes(), None
    final_event: dict[str, object] | None = None
    saw_result_event = False
    for line in stdout_bytes.splitlines():
        if not line:
            continue
        try:
            event = json.loads(line)
        except (UnicodeDecodeError, json.JSONDecodeError):
            return None, "Claude emitted malformed JSONL"
        if not isinstance(event, dict):
            return None, "Claude emitted malformed JSONL"
        final_event = event
        saw_result_event = saw_result_event or event.get("type") == "result"
    if final_event is None or not saw_result_event:
        return None, "Claude did not emit a terminal result event"
    if final_event.get("type") != "result":
        return None, "Claude terminal event is not a result"
    final_result = final_event.get("result")
    if not isinstance(final_result, str):
        return None, "Claude terminal result is not a string"
    final_output_bytes = final_result.encode("utf-8")
    request.final_output_path.write_bytes(final_output_bytes)
    return final_output_bytes, None
