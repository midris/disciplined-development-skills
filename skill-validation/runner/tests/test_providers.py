"""Offline contracts for the fixed provider boundary."""

from __future__ import annotations

import pytest

import skilltest.providers as providers
from skilltest.providers import ProviderRequest, invoke_provider


def _request(tmp_path, *, provider: str, model: str = "chosen-model", effort: str = "high"):
    workspace = tmp_path / "workspace"
    workspace.mkdir(parents=True)
    (workspace / "fixture").mkdir()
    (workspace / "evidence").mkdir()
    return ProviderRequest(
        workspace_dir=workspace,
        prompt_bytes=b"subject bytes\n",
        final_output_path=tmp_path / "final.txt",
        provider=provider,
        model=model,
        effort=effort,
    )


def test_codex_invokes_one_fixed_cli_with_exact_request_values(tmp_path, monkeypatch, fake_provider):
    request = _request(tmp_path, provider="codex", model="gpt-5.4", effort="medium")
    fake_provider.configure(
        monkeypatch,
        stdout=b'{"event":"done"}\n',
        stderr=b"codex warning\n",
        final=b"Codex final response\n",
    )
    real_popen = providers.subprocess.Popen

    def checked_popen(arguments, **kwargs):
        if arguments[0].endswith("codex"):
            assert set(kwargs["env"]) == {"HOME", "CODEX_HOME", "TMPDIR", "PATH"}
            assert kwargs["start_new_session"] is True
        return real_popen(arguments, **kwargs)

    monkeypatch.setattr(providers.subprocess, "Popen", checked_popen)

    result = invoke_provider(request)

    assert result.executable == "codex"
    assert result.invocation_started is True
    assert result.exit_code == 0
    assert result.timed_out is False
    assert result.launch_error is None
    assert result.stdout_bytes == b'{"event":"done"}\n'
    assert result.stderr_bytes == b"codex warning\n"
    record = fake_provider.record()
    assert record["argv"] == [
        str(tmp_path / "fake-bin" / "codex"),
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
    assert record["cwd"] == str(request.workspace_dir / "fixture")
    assert record["stdin"] == "subject bytes\n"
    assert record["path_prefix"] == str(tmp_path / "fake-bin")
    assert record["marker"] is None
    # Python/macOS may add these during startup; checked_popen verifies the actual launch env.
    assert set(record["environment_keys"]) <= {"HOME", "CODEX_HOME", "TMPDIR", "PATH", "LC_CTYPE", "__CF_USER_TEXT_ENCODING"}
    assert record["environment"]["PATH"] == f"{tmp_path / 'fake-bin'}:/usr/bin:/bin:/usr/sbin:/sbin"
    assert record["environment"]["HOME"] != str(tmp_path / "invoking-home")
    assert (request.workspace_dir / "fixture/.git/config").is_file()


def test_claude_retains_raw_jsonl_without_parsing_or_formatting(tmp_path, monkeypatch, fake_provider):
    request = _request(tmp_path, provider="claude", model="sonnet", effort="high")
    stdout = b'not-json\n{"type":"result","result":7}\n'
    fake_provider.configure(monkeypatch, stdout=stdout, stderr=b"claude warning\n")

    result = invoke_provider(request)

    assert result.executable == "claude"
    assert result.invocation_started is True
    assert result.exit_code == 0
    assert result.timed_out is False
    assert result.launch_error is None
    assert result.stdout_bytes == stdout
    assert result.stderr_bytes == b"claude warning\n"
    assert not request.final_output_path.exists()
    record = fake_provider.record()
    assert record["argv"] == [
        str(tmp_path / "fake-bin" / "claude"),
        "--print",
        "--no-session-persistence",
        "--model",
        "sonnet",
        "--effort",
        "high",
        "--permission-mode",
        "acceptEdits",
    ]
    assert record["cwd"] == str(request.workspace_dir)
    assert record["stdin"] == "subject bytes\n"
    assert record["marker"] == "inherited"
    assert record["claude_baseline_env"] == {
        "CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT": "1",
        "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1",
        "CLAUDE_CODE_DISABLE_BUNDLED_SKILLS": "1",
        "CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS": "1",
        "CLAUDE_CODE_DISABLE_WORKFLOWS": "1",
        "CLAUDE_CODE_DISABLE_ARTIFACT": "1",
        "CLAUDE_CODE_DISABLE_CRON": "1",
        "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    }


def test_returns_launch_failure_without_starting_provider(tmp_path, monkeypatch):
    monkeypatch.setenv("PATH", str(tmp_path / "empty-bin"))

    result = invoke_provider(_request(tmp_path, provider="claude"))

    assert result.invocation_started is False
    assert result.exit_code is None
    assert result.timed_out is False
    assert result.launch_error is not None
    assert result.stdout_bytes == b""
    assert result.stderr_bytes == b""

    monkeypatch.setattr(
        providers.subprocess,
        "Popen",
        lambda *args, **kwargs: (_ for _ in ()).throw(ValueError("unrepresentable launch")),
    )
    normalized = invoke_provider(_request(tmp_path / "value-error", provider="claude"))
    assert normalized.invocation_started is False
    assert normalized.exit_code is None
    assert normalized.launch_error == "unrepresentable launch"


def test_returns_nonzero_exit_before_examining_codex_final_output(tmp_path, monkeypatch, fake_provider):
    fake_provider.configure(monkeypatch, stdout=b"out", stderr=b"err", exit_code=7, write_final=False)

    result = invoke_provider(_request(tmp_path, provider="codex"))

    assert result.invocation_started is True
    assert result.exit_code == 7
    assert result.timed_out is False
    assert result.stdout_bytes == b"out"
    assert result.stderr_bytes == b"err"


def test_marks_timeout_after_terminating_direct_provider(tmp_path, monkeypatch, fake_provider):
    fake_provider.configure(monkeypatch, delay_seconds=1)
    monkeypatch.setattr(providers, "PROVIDER_TIMEOUT_SECONDS", 0.01)
    monkeypatch.setattr(providers, "TERMINATE_GRACE_SECONDS", 0.01)

    result = invoke_provider(_request(tmp_path, provider="codex"))

    assert result.invocation_started is True
    assert result.exit_code is not None
    assert result.timed_out is True
    assert result.stdout_bytes == b""
    assert result.stderr_bytes == b""


def test_zero_exit_accepts_optional_or_arbitrary_provider_output(
    tmp_path, monkeypatch, fake_provider
):
    for provider, stdout, write_final in (
        ("codex", b"", False),
        ("claude", b"not-json\n", True),
        ("claude", b'{"type":"result","result":7}\n', True),
    ):
        fake_provider.configure(monkeypatch, stdout=stdout, write_final=write_final)
        request = _request(tmp_path / provider / str(len(stdout)), provider=provider)
        result = invoke_provider(request)

        assert result.exit_code == 0
        assert result.stdout_bytes == stdout
        assert not request.final_output_path.exists()


def test_rejects_internal_unknown_provider_without_launching_child(tmp_path):
    with pytest.raises(ValueError, match="unsupported provider"):
        invoke_provider(_request(tmp_path, provider="other"))
