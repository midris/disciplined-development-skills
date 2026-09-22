"""Fixed local CLI invocation for the built-in providers."""

from __future__ import annotations

import json
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
    permissions: str = "workspace-write"


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
    capture_error: str | None = None


def invoke_provider(request: ProviderRequest, *, log: Callable[[str], None] = lambda message: None) -> ProviderResult:
    """Invoke one configured built-in CLI without a shell."""
    if request.provider == "codex":
        runtime = CodexRuntime(log)
    elif request.provider == "claude":
        runtime = ClaudeRuntime(log, permissions=request.permissions)
    else:
        raise ValueError(f"unsupported provider: {request.provider}")
    result = ProviderResult(request.provider, False)
    cleanup_error = None
    try:
        try:
            runtime.prepare(request.workspace_dir / "fixture")
            arguments = runtime.prefix + _arguments(
                request, executable=runtime.executable,
                shell_path=runtime.environment["PATH"] if request.provider == "codex" else None,
                scratch_dir=Path(runtime.environment["TMPDIR"]) if request.provider == "codex" else None,
            )
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
                result = ProviderResult(request.provider, True)
                stdout, stderr, timed_out = runtime.communicate(process, request.prompt_bytes, PROVIDER_TIMEOUT_SECONDS)
                result = ProviderResult(
                    request.provider, True, process.returncode, timed_out,
                    stdout_bytes=stdout, stderr_bytes=stderr,
                )
    finally:
        if request.provider == "codex" and result.invocation_started:
            capture_error = runtime.retain_session(request.workspace_dir.parent / "provider-session.jsonl")
            result = replace(result, capture_error=capture_error)
        cleanup_error = runtime.cleanup()
        if cleanup_error:
            try:
                log(cleanup_error)
            except OSError:
                pass  # The returned result still reports the cleanup failure.
    return replace(result, cleanup_error=cleanup_error)


def _arguments(request: ProviderRequest, *, executable: str = "codex", shell_path: str | None = None, scratch_dir: Path | None = None) -> list[str]:
    if request.permissions not in {"workspace-write", "read-only"}:
        raise ValueError(f"unsupported permissions: {request.permissions}")
    if request.provider == "codex":
        # 0.154.0's :minimal process defaults reopen shared temp trees. Deny
        # globs override those defaults, so declared roots must live elsewhere.
        for path in [request.workspace_dir / "fixture", request.workspace_dir / "evidence",
                     *([scratch_dir] if scratch_dir is not None else [])]:
            if any(path.resolve().is_relative_to(Path(root).resolve())
                   for root in ("/tmp", "/private/tmp", "/var/tmp", "/private/var/tmp")):
                raise PreparationError("Codex inputs and scratch must be outside shared temporary directories")
        # Deny inherited host reads, then grant declared inputs and runtime tools.
        # Temporary ancestors contain other runs; only this invocation's scratch
        # is reopened. Explicit protections retain the qualified 0.154.0 behavior.
        filesystem = [
            '":root"="deny"', '":minimal"="read"',
            '"/opt/homebrew"="read"',
            '":slash_tmp"="deny"',
            '"/tmp/**"="deny"', '"/private/tmp/**"="deny"',
            '"/var/tmp/**"="deny"', '"/private/var/tmp/**"="deny"',
            '":workspace_roots"={".git"="read",".codex"="read",".agents"="read"}',
        ]
        write = request.permissions == "workspace-write"
        evidence = json.dumps(str(request.workspace_dir / "evidence"))
        access = json.dumps("write" if write else "read")
        filesystem += [f'{json.dumps(str(request.workspace_dir / "fixture"))}={access}',
                       f'{evidence}={access}']
        if write:
            filesystem.append(f'{json.dumps(str(request.workspace_dir / "fixture/.git"))}="write"')
        if scratch_dir is not None:
            filesystem.append(f'{json.dumps(str(scratch_dir))}="write"')
        policy = (
            'permissions.skilltest={'
            f'filesystem={{{",".join(filesystem)}}},'
            + (f'workspace_roots={{{evidence}=true}},' if write else '')
            + 'network={enabled=false}}'
        )
        return [
            executable, "--cd", str(request.workspace_dir / "fixture"), "exec",
            "--skip-git-repo-check", "--json",
            "--color", "never", "--model", request.model, "-c",
            f'model_reasoning_effort="{request.effort}"',
            "-c", 'default_permissions="skilltest"', "-c", policy,
            "--strict-config", "--ignore-user-config", "--ignore-rules", "-c", 'shell_environment_policy.inherit="none"',
            # Forward only the prepared executable path; inherit=none also strips PATH.
            *(["-c", f'shell_environment_policy.set={{PATH={json.dumps(shell_path)}'
                        + (f',TMPDIR={json.dumps(str(scratch_dir))}' if scratch_dir is not None else '') + '}'] if shell_path is not None else []),
            "-c", 'cli_auth_credentials_store="file"', "-c", 'approval_policy="never"',
            "--output-last-message", str(request.final_output_path), "-",
        ]
    if request.provider == "claude":
        tools = ("Read,Skill,Glob,Grep,Bash" if request.permissions == "read-only"
                 else "Read,Skill,Glob,Grep,Write,Edit,Bash")
        return [
            executable, "--print", "--no-session-persistence", "--model", request.model,
            "--effort", request.effort, "--permission-mode", "dontAsk", "--permission-prompts", "none",
            "--setting-sources", "project", "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
            "--no-chrome", "--tools", tools,
            "--allowedTools", tools,
            "--add-dir", str(request.workspace_dir / "evidence"), "--output-format", "stream-json", "--verbose",
        ]
    raise ValueError(f"unsupported provider: {request.provider}")
