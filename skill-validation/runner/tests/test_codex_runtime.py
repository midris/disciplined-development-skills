"""Codex runtime contracts: real private files, mocked process and clock boundaries."""

import hashlib
import json
import os
import signal
import subprocess
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, call

import pytest

from skilltest import runtime as process_runtime
from skilltest import codex_runtime, runner
from skilltest.codex_runtime import CodexRuntime
from skilltest.runtime import PreparationError
from skilltest.providers import ProviderRequest, invoke_provider


def request_at(path):
    (path / "workspace/fixture").mkdir(parents=True)
    (path / "workspace/evidence").mkdir()
    return ProviderRequest(path / "workspace", b"test prompt", path / "final.txt", "codex", "chosen", "low")


@pytest.fixture
def setup_calls(tmp_path, monkeypatch, private_test_profile):
    # Process effects are mocked; auth files, modes, copies and deletion remain real.
    (private_test_profile / "auth.json").write_text('{"tokens":{"access_token":"dummy-test-only"}}')
    monkeypatch.setattr(codex_runtime.shutil, "which", lambda name, **kwargs: "/stub/bin/" + name)
    monkeypatch.setattr(codex_runtime.tempfile, "tempdir", str(tmp_path))
    process = Mock(returncode=0, stdin=None, stdout=None, stderr=None)
    process.communicate.return_value = (b"", b"")
    popen = Mock(return_value=process)
    login = Mock()
    stop = Mock(return_value=None)
    monkeypatch.setattr(codex_runtime.subprocess, "Popen", popen)
    monkeypatch.setattr(CodexRuntime, "_check_login", login)
    monkeypatch.setattr(process_runtime, "stop_owned", stop)
    return SimpleNamespace(popen=popen, process=process, login=login, stop=stop)


def test_private_files_are_fresh_restricted_and_removed(tmp_path, setup_calls, private_test_profile):
    # Break: copying host settings, unsafe modes, reused runtime or retained auth.
    source = private_test_profile / "auth.json"
    original = source.read_bytes()
    (private_test_profile / "config.toml").write_text('model="host-only"')
    roots = []
    for index in range(2):
        request = request_at(tmp_path / str(index))
        runtime = CodexRuntime(lambda _: None)
        runtime.prepare(request.workspace_dir / "fixture")
        roots.append(runtime.root)
        assert not runtime.root.is_relative_to(request.workspace_dir)
        assert set(runtime.environment) == {"HOME", "CODEX_HOME", "TMPDIR", "PATH"}
        assert runtime.environment["PATH"] == "/stub/bin:/usr/bin:/bin:/usr/sbin:/sbin"
        profile = Path(runtime.environment["CODEX_HOME"])
        assert sorted(p.name for p in profile.iterdir()) == ["auth.json"]
        assert (profile / "auth.json").read_bytes() == original
        assert (profile / "auth.json").stat().st_mode & 0o777 == 0o600
        for name in ("HOME", "CODEX_HOME", "TMPDIR"):
            assert Path(runtime.environment[name]).stat().st_mode & 0o777 == 0o700
        assert runtime.cleanup() is None
        assert not runtime.root.exists()
    assert roots[0] != roots[1] and source.read_bytes() == original


@pytest.mark.parametrize("contents", [None, b"invalid json", b"[]", b"{}"])
def test_invalid_auth_blocks_all_processes(tmp_path, setup_calls, private_test_profile, contents):
    # Break: attempting login/model execution with absent or malformed private auth.
    auth = private_test_profile / "auth.json"
    auth.unlink()
    if contents is not None:
        auth.write_bytes(contents)
    result = invoke_provider(request_at(tmp_path / "case"))
    assert result.preparation_error and not result.invocation_started
    assert result.cleanup_error is None
    setup_calls.login.assert_not_called()
    setup_calls.popen.assert_not_called()
    assert not list(tmp_path.glob("skilltest-codex-*"))


@pytest.mark.parametrize("kind", ["symlink", "fifo", "directory"])
def test_nonregular_auth_is_preserved_and_not_copied(tmp_path, setup_calls, private_test_profile, kind):
    # Break: following a secret symlink, blocking on a pipe, or reading a directory.
    auth = private_test_profile / "auth.json"
    saved = private_test_profile / "saved-auth.json"
    auth.rename(saved)
    if kind == "symlink":
        auth.symlink_to(saved)
    elif kind == "fifo":
        os.mkfifo(auth)
    else:
        auth.mkdir()
    result = invoke_provider(request_at(tmp_path / "case"))
    assert result.preparation_error and not result.invocation_started
    assert result.cleanup_error is None and saved.is_file()
    setup_calls.popen.assert_not_called()


def test_home_fallback_and_git_invocation_exclude_global_templates(tmp_path, setup_calls, private_test_profile, monkeypatch):
    # Break: wrong auth fallback, Git argv/environment or setup deadline.
    private_test_profile.rename(Path(os.environ["HOME"]) / ".codex")
    monkeypatch.delenv("CODEX_HOME")
    request = request_at(tmp_path / "case")
    runtime = CodexRuntime(lambda _: None)
    try:
        runtime.prepare(request.workspace_dir / "fixture")
        assert setup_calls.popen.call_args.args[0] == [
            "/stub/bin/git", "init", "--quiet", "--template=", str(request.workspace_dir / "fixture"),
        ]
        kwargs = setup_calls.popen.call_args.kwargs
        assert kwargs["cwd"] == request.workspace_dir / "fixture"
        assert kwargs["env"] == runtime.environment | {"GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull}
        assert kwargs["start_new_session"] is True
        setup_calls.process.communicate.assert_called_once_with(input=None, timeout=30)
    finally:
        assert runtime.cleanup() is None


@pytest.mark.parametrize("stage", ["login", "git", "model"])
def test_stage_failure_cleans_private_files_and_blocks_invocation(tmp_path, setup_calls, stage):
    # Break: continuing after setup failure or retaining auth after a failed launch.
    if stage == "login":
        setup_calls.login.side_effect = PreparationError("login failed")
    elif stage == "git":
        setup_calls.popen.side_effect = OSError("git launch failed")
    else:
        setup_calls.popen.side_effect = [setup_calls.process, OSError("model launch failed")]
    result = invoke_provider(request_at(tmp_path / "case"))
    assert not result.invocation_started and result.cleanup_error is None
    assert result.launch_error if stage == "model" else result.preparation_error
    assert setup_calls.popen.call_count == {"login": 0, "git": 1, "model": 2}[stage]
    assert not list(tmp_path.glob("skilltest-codex-*"))


@pytest.mark.parametrize("reason", ["timeout", "nonzero"])
def test_git_failure_uses_setup_deadline_blocks_model_and_cleans(tmp_path, setup_calls, reason):
    # Break: wrong deadline, missing timeout classification, model launch after failed init, or leaked runtime.
    if reason == "timeout":
        setup_calls.process.communicate.side_effect = [subprocess.TimeoutExpired("git", 30), (b"", b"")]
    else:
        setup_calls.process.returncode = 7
    result = invoke_provider(request_at(tmp_path / "case"))
    assert result.preparation_error == "Codex project-boundary initialization failed"
    assert not result.invocation_started and result.cleanup_error is None
    setup_calls.popen.assert_called_once()
    assert setup_calls.process.communicate.call_args_list[0] == call(input=None, timeout=30)
    if reason == "timeout":
        assert setup_calls.process.communicate.call_args_list[1] == call(timeout=5)
    assert not list(tmp_path.glob("skilltest-codex-*"))


def test_missing_executable_blocks_before_auth_copy(tmp_path, setup_calls, monkeypatch):
    monkeypatch.setattr(codex_runtime.shutil, "which", lambda *args, **kwargs: None)
    result = invoke_provider(request_at(tmp_path / "case"))
    assert result.preparation_error == "Codex executable is unavailable"
    assert not result.invocation_started
    setup_calls.login.assert_not_called()
    setup_calls.popen.assert_not_called()


@pytest.mark.parametrize("outcome", ["timeout", "interrupt"])
def test_model_failure_removes_actual_private_runtime(tmp_path, setup_calls, outcome):
    # Break: cleaning setup failures but leaking private files on the model-stage path.
    failure = subprocess.TimeoutExpired("model", 900) if outcome == "timeout" else KeyboardInterrupt()
    setup_calls.process.communicate.side_effect = [(b"", b""), failure, (b"partial", b"error")]
    request = request_at(tmp_path / "case")
    if outcome == "interrupt":
        with pytest.raises(KeyboardInterrupt):
            invoke_provider(request)
    else:
        result = invoke_provider(request)
        assert result.timed_out and result.cleanup_error is None
        assert (result.stdout_bytes, result.stderr_bytes) == (b"partial", b"error")
    assert setup_calls.process.communicate.call_args_list[1] == call(input=b"test prompt", timeout=900)
    assert not list(tmp_path.glob("skilltest-codex-*"))


@pytest.mark.parametrize("target", [".git", ".git/config"])
def test_declared_git_collision_is_preserved(build_config_case, setup_calls, target):
    # Break: overwriting an input-declared Git boundary.
    outcome = runner.run_once(build_config_case(fixtures=(("source", target, b"owner"),)).config_path)
    value = json.loads((outcome.run_dir / "result.json").read_text())
    assert value["infrastructure_error"]["code"] == "PREPARATION_FAILED"
    assert not value["execution"]["invocation_started"]
    assert (outcome.run_dir / "workspace/fixture" / target).read_bytes() == b"owner"
    setup_calls.popen.assert_not_called()


def test_existing_git_boundary_is_never_overwritten(tmp_path, setup_calls):
    request = request_at(tmp_path / "case")
    git = request.workspace_dir / "fixture/.git"
    git.write_bytes(b"preserve")
    result = invoke_provider(request)
    assert result.preparation_error and not result.invocation_started
    assert git.read_bytes() == b"preserve"
    setup_calls.popen.assert_not_called()


@pytest.mark.parametrize("target", ["fixture", "prompt_path", "prompt_template_path"])
def test_copied_input_mismatch_blocks_before_processes(build_config_case, setup_calls, monkeypatch, target):
    # Break: launching on altered fixture or prompt bytes.
    case = build_config_case(fixtures=(("source", "input.txt", b"declared"),))
    prepare = runner.prepare_workspace
    def corrupt(context, config):
        prepared = prepare(context, config)
        path = context.fixture_dir / "input.txt" if target == "fixture" else getattr(context, target)
        path.write_bytes(b"wrong")
        return prepared
    monkeypatch.setattr(runner, "prepare_workspace", corrupt)
    outcome = runner.run_once(case.config_path)
    value = json.loads((outcome.run_dir / "result.json").read_text())
    assert value["infrastructure_error"]["code"] == "PREPARATION_FAILED"
    assert not value["execution"]["invocation_started"]
    setup_calls.popen.assert_not_called()


def test_prelaunch_hashes_and_absolute_invocation_are_logged(build_config_case, setup_calls):
    # Break: missing prepared input provenance, unresolved command or logged auth contents.
    outcome = runner.run_once(build_config_case(fixtures=(("source", "input.txt", b"declared"),)).config_path)
    text = (outcome.run_dir / "runner.log").read_text()
    assert hashlib.sha256(b"declared").hexdigest() in text
    assert "/stub/bin/codex" in text
    assert "dummy-test-only" not in text


@pytest.fixture
def login_boundary(monkeypatch):
    # Drive selector readiness and clock deterministically; never open OS pipes or poll.
    process = Mock(returncode=0)
    key = SimpleNamespace(fd=123, fileobj=process.stdout)
    selector = Mock()
    selector.get_map.side_effect = [True, True, False]
    selector.select.return_value = [(key, 1)]
    selector_context = Mock()
    selector_context.__enter__ = Mock(return_value=selector)
    selector_context.__exit__ = Mock(return_value=False)
    popen = Mock(return_value=process)
    read = Mock(side_effect=[b"Logged in using ChatGPT", b""])
    clock = Mock(return_value=0)
    stop = Mock(return_value=None)
    monkeypatch.setattr(codex_runtime.subprocess, "Popen", popen)
    monkeypatch.setattr(process_runtime.selectors, "DefaultSelector", Mock(return_value=selector_context))
    monkeypatch.setattr(codex_runtime.os, "read", read)
    monkeypatch.setattr(process_runtime.time, "monotonic", clock)
    monkeypatch.setattr(process_runtime, "stop_owned", stop)
    return SimpleNamespace(process=process, popen=popen, read=read, clock=clock, stop=stop, selector=selector)


@pytest.mark.parametrize("failure, expected", [
    (None, None), ("exit", "did not establish"), ("unknown", "did not establish"),
    ("oversized", "output limit"), ("deadline", "timed out"), ("wait", "timed out"),
    ("cleanup", "cleanup failed"),
])
def test_private_login_status_is_bounded_and_never_retained(login_boundary, failure, expected):
    # Break: unbounded status reads/waits, accepted unusable auth, leaked output or skipped cleanup.
    b = login_boundary
    if failure == "exit":
        b.process.returncode = 1
    elif failure == "unknown":
        b.read.side_effect = [b"DUMMY_AUTH_STATUS_MUST_NOT_BE_RETAINED", b""]
    elif failure == "oversized":
        b.read.side_effect = [b"x" * 4096, b"x" * 4096, b"x"]
        b.selector.get_map.side_effect = [True, True, True]
    elif failure == "deadline":
        b.clock.side_effect = [0, 31]
    elif failure == "wait":
        b.process.wait.side_effect = subprocess.TimeoutExpired("login", 30)
    elif failure == "cleanup":
        b.stop.return_value = "unverified"
    logs = []
    runtime = CodexRuntime(logs.append)
    runtime.executable = "/stub/bin/codex"
    runtime.environment = {"CODEX_HOME": "/private/codex"}
    if expected:
        with pytest.raises(PreparationError, match=expected) as caught:
            runtime._check_login(Path("/fixture"))
        assert "DUMMY_AUTH_STATUS" not in str(caught.value)
    else:
        runtime._check_login(Path("/fixture"))
        b.process.wait.assert_called_once_with(timeout=30)
    assert b.popen.call_args.args[0] == ["/stub/bin/codex", "-c", 'cli_auth_credentials_store="file"', "login", "status"]
    assert b.popen.call_args.kwargs["start_new_session"] is True
    assert b.popen.call_args.kwargs["env"] == runtime.environment
    assert b.popen.call_args.kwargs["cwd"] == Path("/fixture")
    b.process.stdout.close.assert_called_once_with()
    b.stop.assert_called_once_with(b.process)
    assert logs == []


@pytest.mark.parametrize("outcome", ["success", "timeout", "interrupt", "unreaped"])
def test_communicate_stops_processes_closes_pipes_and_preserves_output(monkeypatch, outcome):
    # Break: missing shutdown, wrong grace period, lost bytes or fabricated exit after timeout.
    process = Mock(returncode=None if outcome == "unreaped" else 0)
    timeout = subprocess.TimeoutExpired("stub", 900, output=b"partial", stderr=b"error")
    process.communicate.side_effect = {
        "success": [(b"partial", b"error")], "timeout": [timeout, (b"partial", b"error")],
        "interrupt": KeyboardInterrupt, "unreaped": [timeout, timeout],
    }[outcome]
    stop = Mock(return_value="unproved" if outcome == "unreaped" else None)
    monkeypatch.setattr(process_runtime, "stop_owned", stop)
    runtime = CodexRuntime(lambda _: None)
    if outcome == "interrupt":
        with pytest.raises(KeyboardInterrupt):
            runtime.communicate(process, b"prompt", 900)
    else:
        assert runtime.communicate(process, b"prompt", 900) == (b"partial", b"error", outcome != "success")
    assert process.communicate.call_args_list[0] == call(input=b"prompt", timeout=900)
    if outcome in ("timeout", "unreaped"):
        assert process.communicate.call_args_list[1] == call(timeout=5)
    assert stop.call_count == (2 if outcome in ("timeout", "unreaped") else 1)
    for stream in (process.stdin, process.stdout, process.stderr):
        stream.close.assert_called_once_with()
    if outcome == "unreaped":
        assert process.returncode is None and runtime.process_cleanup_error


@pytest.mark.parametrize("failure", [None, "directory", "process"])
def test_cleanup_requires_proved_process_exit_and_directory_removal(tmp_path, monkeypatch, failure):
    # Break: deleting live-process auth, misreporting cleanup or losing the recovery path.
    runtime = CodexRuntime(Mock(side_effect=OSError("log unavailable")))
    runtime.root = tmp_path / "owned-runtime"
    runtime.root.mkdir()
    if failure == "process":
        runtime.process_cleanup_error = "process still live"
    elif failure == "directory":
        monkeypatch.setattr(codex_runtime.shutil, "rmtree", Mock(side_effect=PermissionError))
    error = runtime.cleanup()
    if failure:
        assert str(runtime.root) in error and runtime.root.is_dir()
    else:
        assert error is None and not runtime.root.exists()


@pytest.mark.parametrize("remaining, signals, error", [
    ([False], [], False),
    ([True, False], [signal.SIGTERM], False),
    ([True, True, False], [signal.SIGTERM, signal.SIGKILL], False),
    ([True, True, True], [signal.SIGTERM, signal.SIGKILL], True),
])
def test_owned_group_shutdown_is_bounded_and_reaps_only_its_child(monkeypatch, remaining, signals, error):
    # Break: wrong signal target/order, unbounded retries or failing to reap the direct child.
    process = Mock(pid=987654, returncode=None)
    exists = Mock(side_effect=remaining)
    kill = Mock()
    monkeypatch.setattr(process_runtime, "_group_exists", exists)
    monkeypatch.setattr(process_runtime.time, "monotonic", Mock(side_effect=range(100)))
    monkeypatch.setattr(process_runtime, "TERMINATE_GRACE_SECONDS", 0)
    monkeypatch.setattr(os, "killpg", kill)
    result = process_runtime.stop_owned(process)
    assert bool(result) is error
    assert kill.call_args_list == [call(987654, sig) for sig in signals]
    if not error:
        process.wait.assert_called_once_with(timeout=0)
    else:
        process.wait.assert_not_called()


@pytest.mark.parametrize("error", [PermissionError("denied"), subprocess.TimeoutExpired("stub", 5)])
def test_shutdown_reports_unverifiable_os_outcome(monkeypatch, error):
    # Break: pretending an OS error or unreaped child establishes cleanup.
    process = Mock(pid=987654)
    monkeypatch.setattr(process_runtime, "_group_exists", Mock(return_value=False))
    process.wait.side_effect = error
    assert process_runtime.stop_owned(process) == "owned provider process group cleanup could not be verified"


def test_shutdown_waits_only_for_each_five_second_grace(monkeypatch):
    # Break: changing the real grace deadline or polling beyond either bounded phase.
    process = Mock(pid=987654)
    monkeypatch.setattr(process_runtime, "_group_exists", Mock(side_effect=[True, True, True, True, False]))
    monkeypatch.setattr(process_runtime.time, "monotonic", Mock(side_effect=[0, 1, 6, 7, 8, 13]))
    sleep = Mock()
    kill = Mock()
    monkeypatch.setattr(process_runtime.time, "sleep", sleep)
    monkeypatch.setattr(os, "killpg", kill)
    assert process_runtime.stop_owned(process) is None
    assert kill.call_args_list == [call(987654, signal.SIGTERM), call(987654, signal.SIGKILL)]
    assert sleep.call_args_list == [call(0.01), call(0.01)]
    process.wait.assert_called_once_with(timeout=5)


def test_group_check_reaps_before_probing_and_handles_disappearance(monkeypatch):
    # Break: treating an unreaped direct child as a surviving group.
    events = []
    process = Mock(pid=987654)
    process.poll.side_effect = lambda: events.append("reap")
    def disappeared(pid, sig):
        events.append((pid, sig))
        raise ProcessLookupError
    monkeypatch.setattr(os, "killpg", disappeared)
    assert process_runtime._group_exists(process) is False
    assert events == ["reap", (987654, 0)]
