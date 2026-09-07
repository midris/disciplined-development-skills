"""Provider-free contracts for the Codex-owned private runtime."""

import json
import hashlib
import os
import signal
import subprocess
import sys
from pathlib import Path
from unittest.mock import Mock

import pytest

import skilltest.providers as providers
import skilltest.workspace as workspace
from skilltest import codex_runtime
from skilltest.providers import ProviderRequest, invoke_provider
from skilltest.runner import run_once


def request_at(path: Path) -> ProviderRequest:
    (path / "workspace/fixture").mkdir(parents=True)
    (path / "workspace/evidence").mkdir()
    return ProviderRequest(path / "workspace", b"test prompt", path / "final.txt", "codex", "chosen", "low")


@pytest.mark.parametrize("exit_code", [0, 7])
def test_private_runtime_is_fresh_private_and_removed_after_return(
    tmp_path, monkeypatch, fake_provider, private_test_profile, exit_code
):
    # Break caught: inheriting profile state, leaking status output or retaining auth.
    source_auth = (private_test_profile / "auth.json").read_bytes()
    (private_test_profile / "config.toml").write_text('model="host-only"')
    fake_provider.configure(monkeypatch, final=b"answer", exit_code=exit_code)
    environments = []
    for index in range(2):
        result = invoke_provider(request_at(tmp_path / str(index)))
        login = json.loads(fake_provider.record_path.with_name("login-record.json").read_text())
        env = login["environment"]
        environments.append(env)
        assert result.exit_code == exit_code
        assert result.cleanup_error is None
        assert login["auth_mode"] == 0o600
        assert login["profile_mode"] == 0o700
        assert login["profile_files"] == ["auth.json"]
        assert "cli_auth_credentials_store=\"file\"" in login["argv"]
        assert b"DUMMY_AUTH_STATUS" not in result.stderr_bytes + result.stdout_bytes
        for key in ("HOME", "CODEX_HOME", "TMPDIR"):
            assert not Path(env[key]).exists()
            assert not Path(env[key]).is_relative_to(tmp_path / str(index))
    assert environments[0] != environments[1]
    assert (private_test_profile / "auth.json").read_bytes() == source_auth


@pytest.mark.parametrize("contents", [None, b"invalid json", b"[]", b"{}"])
def test_unavailable_or_malformed_auth_blocks_before_model(
    tmp_path, fake_provider, private_test_profile, contents
):
    # Break caught: falling through to a host login/backend with invalid private auth.
    auth = private_test_profile / "auth.json"
    auth.unlink()
    if contents is not None:
        auth.write_bytes(contents)
    result = invoke_provider(request_at(tmp_path / "case"))
    assert result.invocation_started is False
    assert result.preparation_error is not None
    assert not fake_provider.record_path.exists()


def test_symlink_auth_is_not_copied(tmp_path, fake_provider, private_test_profile):
    # Break caught: following an auth-cache symlink outside the declared file source.
    auth = private_test_profile / "auth.json"
    target = private_test_profile / "other.json"
    auth.rename(target)
    auth.symlink_to(target)
    result = invoke_provider(request_at(tmp_path / "case"))
    assert result.preparation_error is not None
    assert result.invocation_started is False
    assert target.exists()


def test_private_login_failure_is_preparation_not_model_failure(tmp_path, monkeypatch, fake_provider):
    # Break caught: counting a preflight login check as a model invocation.
    fake_provider.configure(monkeypatch, login_exit=1)
    result = invoke_provider(request_at(tmp_path / "case"))
    assert result.invocation_started is False
    assert result.preparation_error is not None
    assert "DUMMY_AUTH_STATUS" not in result.preparation_error
    assert not fake_provider.record_path.exists()
    login = json.loads(fake_provider.record_path.with_name("login-record.json").read_text())
    assert not Path(login["environment"]["CODEX_HOME"]).exists()


@pytest.mark.parametrize("target", [".git", ".git/config"])
def test_declared_git_boundary_collision_is_preserved_and_blocks_model(build_config_case, fake_provider, target):
    # Break caught: git init overwriting a legal fixture declaration.
    case = build_config_case(fixtures=(("input.txt", target, b"owner fixture"),))
    outcome = run_once(case.config_path)
    record = json.loads((outcome.run_dir / "result.json").read_text())
    assert outcome.exit_code == 1
    assert record["infrastructure_error"]["code"] == "PREPARATION_FAILED"
    assert record["execution"]["invocation_started"] is False
    assert (outcome.run_dir / "workspace/fixture" / target).read_bytes() == b"owner fixture"
    assert not fake_provider.record_path.exists()


def test_mismatched_copied_fixture_blocks_before_model(build_config_case, fake_provider, monkeypatch):
    # Break caught: treating config validity as proof the copied input matches it.
    case = build_config_case(fixtures=(("source.txt", "input.txt", b"declared"),))
    monkeypatch.setattr(workspace, "_copy_fixture", lambda source, dest: dest.write_bytes(b"wrong"))
    outcome = run_once(case.config_path)
    record = json.loads((outcome.run_dir / "result.json").read_text())
    assert outcome.exit_code == 1
    assert record["infrastructure_error"]["code"] == "PREPARATION_FAILED"
    assert record["execution"]["invocation_started"] is False
    assert not fake_provider.record_path.exists()


def test_timeout_removes_private_runtime(tmp_path, monkeypatch, fake_provider):
    # Break caught: retaining credentials when model execution times out.
    fake_provider.configure(monkeypatch, delay_seconds=1)
    monkeypatch.setattr(providers, "PROVIDER_TIMEOUT_SECONDS", 0.01)
    result = invoke_provider(request_at(tmp_path / "case"))
    assert result.timed_out is True
    assert result.cleanup_error is None
    login = json.loads(fake_provider.record_path.with_name("login-record.json").read_text())
    assert not Path(login["environment"]["CODEX_HOME"]).exists()


@pytest.mark.parametrize("exit_code, expected", [(0, "PROVIDER_CLEANUP_FAILED"), (7, "PROVIDER_EXIT_NONZERO")])
def test_cleanup_failure_preserves_output_and_primary_failure(
    build_config_case, fake_provider, monkeypatch, exit_code, expected
):
    # Break caught: reporting completion, or replacing a provider failure, after failed cleanup.
    from skilltest import codex_runtime
    original_cleanup = codex_runtime.CodexRuntime.cleanup

    def report_cleanup_failure(runtime):
        # Still remove this test's dummy runtime; simulate only the reported failure.
        original_cleanup(runtime)
        return "simulated private runtime cleanup failure"

    monkeypatch.setattr(codex_runtime.CodexRuntime, "cleanup", report_cleanup_failure)
    fake_provider.configure(monkeypatch, final=b"judgeable answer", exit_code=exit_code)
    outcome = run_once(build_config_case().config_path)
    record = json.loads((outcome.run_dir / "result.json").read_text())
    assert outcome.exit_code == 1
    assert record["infrastructure_error"]["code"] == expected
    assert record["execution"]["exit_code"] == exit_code
    assert (outcome.run_dir / "final.txt").read_bytes() == b"judgeable answer"
    assert "simulated private runtime cleanup failure" in (outcome.run_dir / "runner.log").read_text()


def test_missing_codex_fails_preparation(build_config_case, fake_provider, monkeypatch):
    # Break caught: silently using another executable or calling a provider on preflight failure.
    monkeypatch.setenv("PATH", "/nonexistent-skilltest-bin")
    outcome = run_once(build_config_case().config_path)
    record = json.loads((outcome.run_dir / "result.json").read_text())
    assert record["infrastructure_error"]["code"] == "PREPARATION_FAILED"
    assert record["execution"]["invocation_started"] is False
    assert not fake_provider.record_path.exists()


@pytest.mark.parametrize("settings, expected", [
    ({"login_delay_seconds": 10}, "timed out"),
    ({"login_output": "unrecognized login state"}, "did not establish"),
    ({"login_output": "x" * 9000}, "output limit"),
])
def test_bounded_login_rejects_unusable_status(tmp_path, fake_provider, monkeypatch, settings, expected):
    # Break caught: hanging in setup or retaining raw status instead of a bounded classification.
    fake_provider.configure(monkeypatch, **settings)
    if "login_delay_seconds" in settings:
        monkeypatch.setattr(codex_runtime, "SETUP_TIMEOUT_SECONDS", 1)
    messages = []
    result = invoke_provider(request_at(tmp_path / "case"), log=messages.append)
    assert expected in result.preparation_error
    assert result.invocation_started is False
    assert result.cleanup_error is None
    assert not fake_provider.record_path.exists()
    assert "DUMMY_AUTH_STATUS" not in repr(messages)


def test_default_auth_location_and_template_free_git(tmp_path, fake_provider, monkeypatch, private_test_profile):
    # Break caught: ignoring HOME fallback or inheriting global Git settings/templates.
    profile = Path(os.environ["HOME"]) / ".codex"
    private_test_profile.rename(profile)
    monkeypatch.delenv("CODEX_HOME")
    template = tmp_path / "host-template"
    template.mkdir()
    (template / "unwanted").write_text("host template")
    (Path(os.environ["HOME"]) / ".gitconfig").write_text(f'[init]\n templateDir = {template}\n')
    real_popen = subprocess.Popen
    launches = []

    def capture(args, **kwargs):
        launches.append((args, kwargs))
        return real_popen(args, **kwargs)

    monkeypatch.setattr(subprocess, "Popen", capture)
    request = request_at(tmp_path / "case")
    result = invoke_provider(request)
    assert result.exit_code == 0
    login, git, model = launches
    assert login[0][0] == model[0][0]
    assert set(login[1]["env"]) == {"HOME", "CODEX_HOME", "TMPDIR", "PATH"}
    assert git[0][1:] == ["init", "--quiet", "--template=", str(request.workspace_dir / "fixture")]
    assert git[1]["env"]["GIT_CONFIG_NOSYSTEM"] == "1"
    assert git[1]["env"]["GIT_CONFIG_GLOBAL"] == os.devnull
    assert not (request.workspace_dir / "fixture/.git/unwanted").exists()


@pytest.mark.parametrize("stage", ["git", "model"])
def test_partial_setup_or_model_launch_failure_removes_runtime(tmp_path, fake_provider, monkeypatch, stage):
    # Break caught: keeping a private auth copy after setup or launch failure.
    real_popen = subprocess.Popen

    def fail_launch(args, **kwargs):
        if (stage == "git" and "init" in args) or (stage == "model" and "exec" in args):
            raise OSError("simulated launch failure")
        return real_popen(args, **kwargs)

    monkeypatch.setattr(subprocess, "Popen", fail_launch)
    result = invoke_provider(request_at(tmp_path / "case"))
    assert result.preparation_error if stage == "git" else result.launch_error
    assert result.invocation_started is False
    assert result.cleanup_error is None
    login = json.loads(fake_provider.record_path.with_name("login-record.json").read_text())
    assert not Path(login["environment"]["CODEX_HOME"]).exists()


def test_existing_git_is_never_overwritten(tmp_path, fake_provider):
    # Break caught: clobbering an undeclared boundary already present in the prepared tree.
    request = request_at(tmp_path / "case")
    git = request.workspace_dir / "fixture/.git"
    git.write_bytes(b"preserve me")
    result = invoke_provider(request)
    assert result.preparation_error is not None
    assert git.read_bytes() == b"preserve me"
    assert not fake_provider.record_path.exists()


def test_owned_group_escalation_reaps_only_its_child(monkeypatch):
    # Break caught: killing a shared process or deleting runtime before bounded reaping.
    process = Mock(pid=987654, returncode=None)
    exists = iter([True, True, False])
    monkeypatch.setattr(codex_runtime, "_group_exists", lambda p: next(exists))
    monkeypatch.setattr(codex_runtime, "TERMINATE_GRACE_SECONDS", 0)
    killpg = Mock()
    monkeypatch.setattr(os, "killpg", killpg)
    assert codex_runtime.stop_owned(process) is None
    assert killpg.call_args_list == [((987654, signal.SIGTERM),), ((987654, signal.SIGKILL),)]
    process.wait.assert_called_once_with(timeout=0)


def test_handled_interrupt_reaps_model_before_removing_runtime(tmp_path, fake_provider, monkeypatch):
    # Break caught: orphaning the model or its auth on a handled controller interrupt.
    real_communicate = subprocess.Popen.communicate
    model = []

    def interrupt_model(process, *args, **kwargs):
        if "exec" in process.args:
            model.append(process)
            raise KeyboardInterrupt
        return real_communicate(process, *args, **kwargs)

    monkeypatch.setattr(subprocess.Popen, "communicate", interrupt_model)
    with pytest.raises(KeyboardInterrupt):
        invoke_provider(request_at(tmp_path / "case"))
    assert len(model) == 1
    assert model[0].poll() is not None
    assert all(stream.closed for stream in (model[0].stdin, model[0].stdout, model[0].stderr))
    login = json.loads(fake_provider.record_path.with_name("login-record.json").read_text())
    assert not Path(login["environment"]["CODEX_HOME"]).exists()


@pytest.mark.parametrize("failure", ["directory", "process"])
def test_unproved_cleanup_preserves_runtime_and_exact_recovery_path(tmp_path, monkeypatch, failure):
    # Break caught: erasing a runtime while owned processes might still use it, or hiding its path.
    runtime = codex_runtime.CodexRuntime(lambda _: None)
    runtime.root = tmp_path / "owned-runtime"
    runtime.root.mkdir()
    if failure == "process":
        runtime.process_cleanup_error = "owned process still live"
    else:
        monkeypatch.setattr(codex_runtime.shutil, "rmtree", Mock(side_effect=PermissionError))
    error = runtime.cleanup()
    assert str(runtime.root) in error
    assert runtime.root.is_dir()


def test_prelaunch_hashes_and_resolved_command_are_logged(build_config_case, fake_provider):
    # Break caught: confusing post-model fixture hashes with the prepared input evidence.
    case = build_config_case(fixtures=(("source.txt", "input.txt", b"declared"),))
    outcome = run_once(case.config_path)
    log = (outcome.run_dir / "runner.log").read_text()
    assert hashlib.sha256(b"declared").hexdigest() in log
    assert str(fake_provider.settings_path.with_name("codex")) in log
    assert "DUMMY_AUTH_STATUS" not in log
    assert "dummy-test-only" not in log


@pytest.mark.parametrize("target", ["prompt_path", "prompt_template_path"])
def test_mismatched_prepared_prompt_blocks_model(build_config_case, fake_provider, monkeypatch, target):
    # Break caught: checking fixtures while trusting a damaged prompt copy/render.
    from skilltest import runner
    prepare = runner.prepare_workspace

    def corrupt(context, config):
        prepared = prepare(context, config)
        getattr(context, target).write_bytes(b"not the declared prompt")
        return prepared

    monkeypatch.setattr(runner, "prepare_workspace", corrupt)
    outcome = run_once(build_config_case().config_path)
    record = json.loads((outcome.run_dir / "result.json").read_text())
    assert record["infrastructure_error"]["code"] == "PREPARATION_FAILED"
    assert record["execution"]["invocation_started"] is False
    assert not fake_provider.record_path.exists()


@pytest.mark.parametrize("kind", ["fifo", "directory"])
def test_nonregular_auth_is_rejected_without_blocking(tmp_path, fake_provider, private_test_profile, kind):
    # Break caught: blocking on a named pipe or copying a non-file auth source.
    auth = private_test_profile / "auth.json"
    auth.unlink()
    os.mkfifo(auth) if kind == "fifo" else auth.mkdir()
    result = invoke_provider(request_at(tmp_path / "case"))
    assert result.preparation_error is not None
    assert result.invocation_started is False
    assert result.cleanup_error is None


def test_normal_return_stops_remaining_owned_group_members():
    # Break caught: treating the direct child's exit as proof all its workers exited.
    process = subprocess.Popen(
        [sys.executable, "-c", "import subprocess,sys; subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)'], stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); print('done')"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True,
    )
    runtime = codex_runtime.CodexRuntime(lambda _: None)
    try:
        stdout, stderr, timed_out = runtime.communicate(process, None, 10)
        assert (stdout, stderr, timed_out) == (b"done\n", b"", False)
        assert process.returncode == 0
        assert runtime.process_cleanup_error is None
        with pytest.raises(ProcessLookupError):
            os.killpg(process.pid, 0)
    finally:
        codex_runtime.stop_owned(process)


def test_git_setup_timeout_is_bounded_and_blocks_model(tmp_path, fake_provider, monkeypatch):
    # Break caught: applying the model's long deadline to a setup subprocess.
    communicate = codex_runtime.CodexRuntime.communicate
    observed = []

    def expire_git(runtime, process, data, timeout):
        if "init" in process.args:
            observed.append(timeout)
            runtime._stop(process)
            return b"", b"", True
        return communicate(runtime, process, data, timeout)

    monkeypatch.setattr(codex_runtime.CodexRuntime, "communicate", expire_git)
    result = invoke_provider(request_at(tmp_path / "case"))
    assert observed == [30]
    assert providers.PROVIDER_TIMEOUT_SECONDS == 900
    assert codex_runtime.TERMINATE_GRACE_SECONDS == 5
    assert result.preparation_error is not None
    assert result.invocation_started is False
    assert result.cleanup_error is None


def test_cleanup_does_not_misreport_removed_directory_when_log_unwritable(tmp_path):
    # Break caught: reporting a nonexistent manual-recovery target after successful deletion.
    runtime = codex_runtime.CodexRuntime(Mock(side_effect=OSError("log unavailable")))
    runtime.root = tmp_path / "owned-runtime"
    runtime.root.mkdir()
    assert runtime.cleanup() is None
    assert not runtime.root.exists()


def test_unreaped_timeout_preserves_captured_bytes_and_does_not_invent_exit(monkeypatch):
    # Break caught: waiting forever on escaped pipes or making up an exit code.
    process = Mock(returncode=None, stdin=None, stdout=Mock(), stderr=Mock())
    process.communicate.side_effect = subprocess.TimeoutExpired("owned fake", 1, output=b"partial", stderr=b"diagnostic")
    monkeypatch.setattr(codex_runtime, "stop_owned", lambda _: "owned cleanup unproved")
    runtime = codex_runtime.CodexRuntime(lambda _: None)
    assert runtime.communicate(process, b"prompt", 900) == (b"partial", b"diagnostic", True)
    assert process.returncode is None
    assert runtime.process_cleanup_error is not None
    process.stdout.close.assert_called_once()
    process.stderr.close.assert_called_once()
