"""Provider orchestration contracts with mocked runtime/process boundaries."""

import subprocess
from unittest.mock import Mock, call

import pytest

from skilltest import providers
from skilltest.runtime import PreparationError
from skilltest.providers import ProviderRequest, invoke_provider


def request_at(tmp_path, provider="codex", model="gpt-5.4", effort="medium"):
    return ProviderRequest(tmp_path / "workspace", b"subject bytes\n", tmp_path / "final.txt", provider, model, effort)


@pytest.fixture
def boundaries(monkeypatch):
    runtime = Mock(spec=providers.CodexRuntime)
    runtime.executable = "/stub/bin/codex"
    runtime.environment = {"HOME": "/private/home", "CODEX_HOME": "/private/codex",
                           "TMPDIR": "/private/tmp", "PATH": "/stub/bin:/usr/bin:/bin:/usr/sbin:/sbin"}
    runtime.prefix = []
    runtime.cleanup.return_value = None
    runtime.communicate.return_value = (b'{"event":"done"}\n', b"warning", False)
    process = Mock(returncode=0)
    process.communicate.return_value = (b"not-json\n", b"warning")
    popen = Mock(return_value=process)
    monkeypatch.setattr(providers, "CodexRuntime", Mock(return_value=runtime))
    monkeypatch.setattr(providers, "ClaudeRuntime", Mock(return_value=runtime), raising=False)
    monkeypatch.setattr(providers.subprocess, "Popen", popen)
    return runtime, process, popen


def test_codex_invokes_fixed_command_environment_and_deadline(tmp_path, boundaries):
    # Break: incorrect argv, cwd, private environment, session ownership or model deadline.
    runtime, process, popen = boundaries
    request = request_at(tmp_path)
    result = invoke_provider(request)
    assert popen.call_args.args[0] == [
        "/stub/bin/codex",
        "--cd",
        str(request.workspace_dir / "fixture"),
        "exec",
        "--ephemeral",
        "--skip-git-repo-check",
        "--json",
        "--color",
        "never",
        "--model",
        "gpt-5.4",
        "-c",
        'model_reasoning_effort="medium"',
        "--sandbox",
        "workspace-write",
        "--add-dir",
        str(request.workspace_dir / "evidence"),
        "--ignore-user-config",
        "--ignore-rules",
        "-c",
        'shell_environment_policy.inherit="none"',
        "-c",
        'cli_auth_credentials_store="file"',
        "-c",
        'approval_policy="never"',
        "--output-last-message",
        str(request.final_output_path),
        "-",
    ]

    assert popen.call_args.kwargs == {
        "cwd": request.workspace_dir / "fixture", "shell": False,
        "stdin": subprocess.PIPE, "stdout": subprocess.PIPE, "stderr": subprocess.PIPE,
        "env": runtime.environment, "start_new_session": True,
    }
    runtime.prepare.assert_called_once_with(request.workspace_dir / "fixture")
    runtime.communicate.assert_called_once_with(process, b"subject bytes\n", 900)
    runtime.cleanup.assert_called_once_with()
    assert (result.executable, result.invocation_started, result.exit_code) == ("codex", True, 0)
    assert (result.stdout_bytes, result.stderr_bytes, result.timed_out) == (b'{"event":"done"}\n', b"warning", False)


def test_claude_uses_controlled_runtime_native_tools_trace_and_fixture_cwd(tmp_path, boundaries):
    runtime, process, popen = boundaries
    runtime.executable = "/stub/bin/claude"
    runtime.prefix = ["/usr/bin/sandbox-exec", "-f", "/private/policy.sb"]
    messages = []
    request = request_at(tmp_path, "claude", "sonnet", "high")
    result = invoke_provider(request, log=messages.append)
    arguments = popen.call_args.args[0]
    assert arguments[:4] == [*runtime.prefix, runtime.executable]
    for flag, value in {
        "--model": "sonnet", "--effort": "high", "--setting-sources": "project",
        "--mcp-config": '{"mcpServers":{}}', "--permission-mode": "dontAsk",
        "--permission-prompts": "none", "--output-format": "stream-json",
        "--add-dir": str(request.workspace_dir / "evidence"),
        "--tools": "Read,Skill,Glob,Grep,Write,Edit,Bash",
        "--allowedTools": "Read,Skill,Glob,Grep,Write,Edit,Bash",
    }.items():
        assert arguments[arguments.index(flag)+1] == value
    for flag in ["--print", "--no-session-persistence", "--strict-mcp-config", "--no-chrome", "--verbose"]:
        assert flag in arguments
    assert popen.call_args.kwargs["cwd"] == request.workspace_dir / "fixture"
    assert popen.call_args.kwargs["env"] == runtime.environment
    assert popen.call_args.kwargs["start_new_session"] is True
    runtime.prepare.assert_called_once_with(request.workspace_dir / "fixture")
    runtime.communicate.assert_called_once_with(process, request.prompt_bytes, 900)
    runtime.cleanup.assert_called_once()
    assert result.stdout_bytes == b'{"event":"done"}\n'
    assert runtime.executable in "\n".join(messages)


@pytest.mark.parametrize("provider", ["codex", "claude"])
@pytest.mark.parametrize("failure", [PreparationError("not authenticated"), OSError("setup"), ValueError("setup")])
def test_setup_failure_blocks_launch_and_cleans_up(tmp_path, boundaries, failure, provider):
    # Break: launching after failed preparation or bypassing cleanup on setup failure.
    runtime, process, popen = boundaries
    runtime.prepare.side_effect = failure
    result = invoke_provider(request_at(tmp_path, provider))
    popen.assert_not_called()
    runtime.cleanup.assert_called_once_with()
    assert result.preparation_error and not result.invocation_started


@pytest.mark.parametrize("provider", ["codex", "claude"])
@pytest.mark.parametrize("failure", [OSError("launch failed"), ValueError("launch failed")])
def test_launch_failure_is_not_an_invocation(tmp_path, boundaries, provider, failure):
    # Break: classifying a failed spawn as a model invocation.
    runtime, process, popen = boundaries
    popen.side_effect = failure
    result = invoke_provider(request_at(tmp_path, provider))
    assert not result.invocation_started and result.exit_code is None
    assert result.launch_error == "launch failed"
    if provider == "codex":
        runtime.cleanup.assert_called_once_with()


@pytest.mark.parametrize("provider", ["codex", "claude"])
@pytest.mark.parametrize("exit_code", [0, 7])
@pytest.mark.parametrize("timed_out", [False, True])
def test_preserves_outcome_and_cleanup_error(tmp_path, boundaries, exit_code, timed_out, provider):
    # Break: losing output/exit or silently suppressing cleanup failure.
    runtime, process, popen = boundaries
    process.returncode = exit_code
    runtime.communicate.return_value = (b"raw output", b"raw error", timed_out)
    runtime.cleanup.return_value = "cleanup failed"
    messages = []
    result = invoke_provider(request_at(tmp_path, provider), log=messages.append)
    assert result.exit_code == exit_code and result.timed_out is timed_out
    assert (result.stdout_bytes, result.stderr_bytes) == (b"raw output", b"raw error")
    assert result.cleanup_error == "cleanup failed"
    assert messages[-1] == "cleanup failed"


@pytest.mark.parametrize("provider", ["codex", "claude"])
def test_interrupt_still_cleans_runtime(tmp_path, boundaries, provider):
    # Break: skipping runtime cleanup when communicate raises a controller interrupt.
    runtime, process, popen = boundaries
    runtime.communicate.side_effect = KeyboardInterrupt
    with pytest.raises(KeyboardInterrupt):
        invoke_provider(request_at(tmp_path))
    runtime.cleanup.assert_called_once_with()




@pytest.mark.parametrize("provider", ["codex", "claude"])
def test_empty_success_does_not_require_final_output(tmp_path, boundaries, provider):
    # Break: imposing undocumented output syntax or mandatory final-file contents.
    runtime, process, popen = boundaries
    runtime.communicate.return_value = (b"", b"", False)
    process.communicate.return_value = (b"", b"")
    request = request_at(tmp_path, provider)
    result = invoke_provider(request)
    assert result.exit_code == 0 and result.stdout_bytes == b""
    assert not request.final_output_path.exists()


def test_unknown_provider_never_launches(tmp_path, boundaries):
    runtime, process, popen = boundaries
    with pytest.raises(ValueError, match="unsupported provider"):
        invoke_provider(request_at(tmp_path, "other"))
    popen.assert_not_called()
