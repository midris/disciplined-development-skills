"""Real local Git/profile/process checks; no installed provider or paid calls."""

import json
import os
from pathlib import Path
import select
import signal
import subprocess
import sys

import pytest

from skilltest import runtime as process_runtime
from skilltest import codex_runtime
from skilltest.codex_runtime import CodexRuntime
from skilltest.providers import ProviderRequest, invoke_provider


@pytest.mark.parametrize("exit_code", [0, 7])
def test_private_profile_git_and_dummy_provider_wiring(tmp_path, monkeypatch, fake_provider, private_test_profile, exit_code):
    # Break: mocked argv tests passing while actual environment/Git/file wiring is broken.
    source = Path(os.environ["HOME"]) / ".codex"
    private_test_profile.rename(source)
    monkeypatch.delenv("CODEX_HOME")
    original_auth = (source / "auth.json").read_bytes()
    (source / "config.toml").write_text('model="host-only"')
    template = tmp_path / "host-template"
    template.mkdir()
    (template / "unwanted").write_text("must not copy")
    (Path(os.environ["HOME"]) / ".gitconfig").write_text(f'[init]\n templateDir = {template}\n')
    fake_provider.configure(stdout=b"raw output", stderr=b"raw error", final=b"answer", exit_code=exit_code)
    roots = []
    for index in range(2):
        workspace = tmp_path / str(index) / "workspace"
        (workspace / "fixture").mkdir(parents=True)
        (workspace / "evidence").mkdir()
        request = ProviderRequest(workspace, b"prompt", workspace.parent / "final.txt", "codex", "chosen", "low")
        result = invoke_provider(request)
        assert result.cleanup_error is None
        assert result.exit_code == exit_code and result.invocation_started
        assert (result.stdout_bytes, result.stderr_bytes) == (b"raw output", b"raw error")
        assert request.final_output_path.read_bytes() == b"answer"
        login = json.loads(fake_provider.record_path.with_name("login-record.json").read_text())
        observed = fake_provider.record()
        assert observed["stdin"] == "prompt" and observed["cwd"] == str(workspace / "fixture")
        assert observed["argv"][0] == login["argv"][0] == str(fake_provider.settings_path.with_name("codex"))
        env = login["environment"]
        roots.append(env["CODEX_HOME"])
        assert login["auth_mode"] == 0o600 and login["profile_mode"] == 0o700
        assert login["profile_files"] == ["auth.json"]
        assert set(env) == {"HOME", "CODEX_HOME", "TMPDIR", "PATH"}
        assert env["PATH"] == f"{fake_provider.settings_path.parent}:/usr/bin:/bin:/usr/sbin:/sbin"
        for name in ("HOME", "CODEX_HOME", "TMPDIR"):
            assert not Path(env[name]).exists()
        assert (workspace / "fixture/.git/config").is_file()
        assert not (workspace / "fixture/.git/unwanted").exists()
        assert b"DUMMY_AUTH_STATUS" not in result.stdout_bytes + result.stderr_bytes
    assert roots[0] != roots[1]
    assert (source / "auth.json").read_bytes() == original_auth


@pytest.mark.skipif(sys.platform != "darwin", reason="Claude controlled runtime uses macOS sandbox-exec")
def test_claude_dummy_provider_uses_policy_fixture_git_and_raw_trace(tmp_path, fake_provider):
    workspace = tmp_path / "workspace"
    (workspace / "fixture").mkdir(parents=True)
    (workspace / "evidence").mkdir()
    home = Path(os.environ["HOME"])
    (home / ".gitconfig").write_text("invalid global Git config: must not read")
    trace = b'{"type":"result","subtype":"success","is_error":false,"result":"answer"}\n'
    fake_provider.configure(stdout=trace, stderr=b"warning")
    request = ProviderRequest(workspace, b"prompt", tmp_path / "final.txt", "claude", "sonnet", "high")
    result = invoke_provider(request)
    assert result.exit_code == 0 and result.invocation_started, result
    assert result.cleanup_error is None
    assert (result.stdout_bytes, result.stderr_bytes) == (trace, b"warning")
    observed = fake_provider.record()
    assert observed["cwd"] == str(workspace / "fixture") and observed["stdin"] == "prompt"
    assert observed["argv"][0] == str(fake_provider.settings_path.with_name("claude"))
    assert observed["environment"]["HOME"] == str(home)
    assert "CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT" not in observed["claude_baseline_env"]
    assert not Path(observed["environment"]["TMPDIR"]).exists()
    assert (workspace / "evidence/dummy-tool-write.txt").read_text() == "dummy evidence"
    assert (home / ".gitconfig").read_text() == "invalid global Git config: must not read"
    assert not request.final_output_path.exists()  # Runner, not adapter, extracts the final answer.


@pytest.mark.parametrize("ignore_term, expected_exit", [(False, -signal.SIGTERM), (True, -signal.SIGKILL)])
def test_ready_child_is_terminated_and_reaped_on_real_timeout(monkeypatch, ignore_term, expected_exit):
    # Break: signals don't reach the owned group, escalation is skipped, or child isn't reaped.
    # The readiness line is written after the signal handler is installed, not after an assumed startup delay.
    script = (
        "import signal,time\n"
        + ("signal.signal(signal.SIGTERM, signal.SIG_IGN)\n" if ignore_term else "")
        + "print('READY', flush=True)\ntime.sleep(60)\n"
    )
    process = subprocess.Popen([sys.executable, "-c", script], stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True)
    # Shorten the actual grace period at the Codex-owned boundary; no clock or timeout is mocked.
    monkeypatch.setattr(process_runtime, "TERMINATE_GRACE_SECONDS", 0.2)
    runtime = CodexRuntime(lambda _: None)
    try:
        ready, _, _ = select.select([process.stdout], [], [], 10)
        assert ready, "child never became ready"
        assert process.stdout.readline() == b"READY\n"
        stdout, stderr, timed_out = runtime.communicate(process, None, 0.05)
        assert timed_out and (stdout, stderr) == (b"", b"")
        assert process.returncode == expected_exit
        assert runtime.process_cleanup_error is None
        with pytest.raises(ProcessLookupError):
            os.killpg(process.pid, 0)
        assert all(stream.closed for stream in (process.stdin, process.stdout, process.stderr))
    finally:
        error = process_runtime.stop_owned(process)
        for stream in (process.stdin, process.stdout, process.stderr):
            stream.close()
        assert error is None, f"smoke cleanup unresolved: owned PID/PGID {process.pid}: {error}"


def test_normal_parent_exit_stops_remaining_owned_worker():
    # Break: treating the direct parent's exit as proof its worker has exited too.
    worker = "import time; print('READY', flush=True); time.sleep(60)"
    parent = (
        "import subprocess,sys\n"
        f"worker=subprocess.Popen([sys.executable,'-c',{worker!r}], stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)\n"
        "assert worker.stdout.readline() == b'READY\\n'\n"
        "print('done', flush=True)\n"
    )
    process = subprocess.Popen([sys.executable, "-c", parent], stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, start_new_session=True)
    runtime = CodexRuntime(lambda _: None)
    try:
        assert runtime.communicate(process, None, 10) == (b"done\n", b"", False)
        assert process.returncode == 0 and runtime.process_cleanup_error is None
        with pytest.raises(ProcessLookupError):
            os.killpg(process.pid, 0)
    finally:
        error = process_runtime.stop_owned(process)
        process.stdout.close()
        process.stderr.close()
        assert error is None, f"smoke cleanup unresolved: owned PID/PGID {process.pid}: {error}"


@pytest.mark.skipif(sys.platform != 'darwin', reason='macOS policy check')
def test_claude_child_policy_denies_surrogate_semantic_reads_and_home_writes(tmp_path, fake_provider):
    from skilltest.claude_runtime import ClaudeRuntime
    home = Path(os.environ['HOME'])
    inputs = home/'.claude'
    inputs.mkdir()
    secret = inputs/'settings.json'
    secret.write_text('surrogate instruction canary')
    assert secret.read_text() == 'surrogate instruction canary'  # Positive read control.
    positive = home/'positive-write'
    positive.write_text('allowed outside child policy')
    fixture = tmp_path/'fixture'
    fixture.mkdir()
    runtime = ClaudeRuntime(lambda _: None)
    try:
        runtime.prepare(fixture)
        probe = (
            'from pathlib import Path\nimport sys\n'
            'for operation in [lambda: Path(sys.argv[1]).read_bytes(), lambda: Path(sys.argv[2]).write_text("forbidden")]:\n'
            ' try: operation()\n'
            ' except PermissionError: pass\n'
            ' else: raise AssertionError("policy did not deny access")\n'
            'print("DENIED_BOTH")\n'
        )
        process = subprocess.Popen([*runtime.prefix, sys.executable, '-c', probe, str(secret), str(home/'negative-write')],
            cwd=fixture, env=runtime.environment, stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True)
        stdout, stderr, timed_out = runtime.communicate(process, None, 10)
        assert not timed_out and process.returncode == 0, stderr
        assert stdout == b'DENIED_BOTH\n'
        assert secret.read_text() == 'surrogate instruction canary'
        assert not (home/'negative-write').exists()
    finally:
        assert runtime.cleanup() is None
