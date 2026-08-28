"""End-to-end persistence checks for one straight-line skill-test run."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import jsonschema
import pytest

import skilltest.providers as providers_module
import skilltest.results as results_module
import skilltest.workspace as workspace_module
from skilltest.runner import run_once


SCHEMA_PATH = Path(__file__).parents[1] / "result.schema.json"
SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _validate_result(run_dir: Path) -> dict[str, object]:
    result = json.loads((run_dir / "result.json").read_text(encoding="utf-8"))
    jsonschema.validate(result, SCHEMA)
    return result


def _file_entry(path: str, contents: bytes) -> dict[str, object]:
    return {
        "path": path,
        "type": "file",
        "bytes": len(contents),
        "sha256": hashlib.sha256(contents).hexdigest(),
    }


def _assert_stable_artifact_paths(run_dir: Path, result: dict[str, object]) -> None:
    artifacts = result["artifacts"]
    assert {name: artifact["path"] for name, artifact in artifacts.items()} == {
        "config": "config.json",
        "prompt_template": "prompt-template.txt",
        "prompt": "prompt.txt",
        "stdout": "stdout.txt",
        "stderr": "stderr.txt",
        "final": "final.txt",
        "fixture": "workspace/fixture",
        "evidence": "workspace/evidence",
    }
    for relative_path in (
        "config.json",
        "prompt-template.txt",
        "prompt.txt",
        "stdout.txt",
        "stderr.txt",
        "final.txt",
        "result.json",
    ):
        assert (run_dir / relative_path).is_file()
    assert not (run_dir / "subject-input.txt").exists()
    assert not (run_dir / "inputs").exists()


def _assert_terminal_log(run_dir: Path, terminal: str) -> None:
    messages = [
        line.split(" ", 1)[1]
        for line in (run_dir / "runner.log").read_text(encoding="utf-8").splitlines()
    ]
    assert messages[0].endswith(" allocated")
    assert messages[-1] == terminal


# Break caught: reconnecting the runner to subject-input bytes or a non-workspace CWD.
@pytest.mark.parametrize(
    ("provider", "stdout", "stderr", "provider_final"),
    (
        ("codex", b'{"event":"done"}\n', b"codex stderr\n", b"Codex final\x00bytes\n"),
        ("claude", b"not-json\nClaude final bytes\n", b"claude stderr\n", b"unused"),
    ),
)
def test_run_once_invokes_provider_with_rendered_prompt_and_retains_stable_bundle(
    build_config_case,
    fake_provider,
    monkeypatch,
    provider: str,
    stdout: bytes,
    stderr: bytes,
    provider_final: bytes,
) -> None:
    template = (
        b"workspace={{workspace_dir}}\n"
        b"fixture={{fixture_dir}}\n"
        b"evidence={{evidence_dir}}\n"
    )
    case = build_config_case(
        name=f"{provider}-complete",
        prompt_bytes=template,
        fixtures=(("sources/input.txt", "input.txt", b"original fixture\n"),),
        provider=provider,
        model="chosen-model",
        effort="high",
    )
    fixture_bytes = b"provider-mutated fixture\n"
    evidence_bytes = b"provider evidence\x00\n"
    fake_provider.configure(
        monkeypatch,
        stdout=stdout,
        stderr=stderr,
        final=provider_final,
        fixture_bytes=fixture_bytes,
        evidence_name="provider-output.txt",
        evidence_bytes=evidence_bytes,
    )

    outcome = run_once(case.config_path)

    assert outcome.exit_code == 0
    assert outcome.run_dir is not None
    assert outcome.diagnostic is None
    run_dir = outcome.run_dir
    workspace = run_dir / "workspace"
    expected_prompt = (
        f"workspace={workspace.resolve()}\n"
        f"fixture={(workspace / 'fixture').resolve()}\n"
        f"evidence={(workspace / 'evidence').resolve()}\n"
    ).encode("utf-8")
    invocation = fake_provider.record()
    assert invocation["cwd"] == str(workspace)
    assert invocation["stdin"].encode("utf-8") == expected_prompt
    assert (run_dir / "prompt-template.txt").read_bytes() == template
    assert (run_dir / "prompt.txt").read_bytes() == expected_prompt
    assert (run_dir / "config.json").read_bytes() == case.config_path.read_bytes()
    assert (run_dir / "stdout.txt").read_bytes() == stdout
    assert (run_dir / "stderr.txt").read_bytes() == stderr
    expected_final = provider_final if provider == "codex" else stdout
    assert (run_dir / "final.txt").read_bytes() == expected_final
    assert (workspace / "fixture/input.txt").read_bytes() == fixture_bytes
    assert (workspace / "evidence/provider-output.txt").read_bytes() == evidence_bytes
    assert not (workspace / "input.txt").exists()
    assert not (workspace / "provider-output.txt").exists()

    result = _validate_result(run_dir)
    _assert_stable_artifact_paths(run_dir, result)
    assert result["schema_version"] == "0.2"
    assert result["status"] == "COMPLETED"
    assert result["test"] == {"id": f"{provider}-complete-run"}
    assert result["execution"] == {
        "provider": provider,
        "model": "chosen-model",
        "effort": "high",
        "executable": provider,
        "timeout_seconds": 900,
        "invocation_started": True,
        "timed_out": False,
        "exit_code": 0,
    }
    assert result["infrastructure_error"] is None
    assert result["artifacts"]["fixture"] == {
        "path": "workspace/fixture",
        "exists": True,
        "empty": False,
        "entries": [_file_entry("input.txt", fixture_bytes)],
    }
    assert result["artifacts"]["evidence"] == {
        "path": "workspace/evidence",
        "exists": True,
        "empty": False,
        "entries": [_file_entry("provider-output.txt", evidence_bytes)],
    }
    _assert_terminal_log(run_dir, "COMPLETED")
    assert fake_provider.config_observations() == [
        {"before_output": False, "after_output": False}
    ]


# Break caught: mapping an owned pre-invocation failure to a provider state.
def test_run_once_emits_preparation_failed_before_provider_invocation(
    build_config_case, fake_provider, monkeypatch
) -> None:
    case = build_config_case(name="preparation-failed")
    fake_provider.configure(monkeypatch)
    monkeypatch.setattr(
        workspace_module.shutil,
        "copy2",
        lambda *args, **kwargs: (_ for _ in ()).throw(OSError("copy failed")),
    )

    outcome = run_once(case.config_path)

    assert outcome.exit_code == 1
    assert outcome.run_dir is not None
    assert not fake_provider.record_path.exists()
    result = _validate_result(outcome.run_dir)
    assert result["execution"]["provider"] == "codex"
    assert result["execution"]["invocation_started"] is False
    assert result["execution"]["timed_out"] is False
    assert result["execution"]["exit_code"] is None
    assert result["infrastructure_error"]["code"] == "PREPARATION_FAILED"
    _assert_terminal_log(outcome.run_dir, "INFRA_ERROR PREPARATION_FAILED")


# Break caught: treating an executable launch failure as an attempted invocation.
def test_run_once_emits_provider_launch_failed(
    build_config_case, fake_provider, monkeypatch
) -> None:
    case = build_config_case(name="launch-failed")
    fake_provider.configure(monkeypatch)
    monkeypatch.setenv("PATH", str(case.root / "missing-bin"))

    outcome = run_once(case.config_path)

    assert outcome.exit_code == 1
    assert outcome.run_dir is not None
    assert not fake_provider.record_path.exists()
    result = _validate_result(outcome.run_dir)
    assert result["execution"]["invocation_started"] is False
    assert result["execution"]["timed_out"] is False
    assert result["execution"]["exit_code"] is None
    assert result["infrastructure_error"]["code"] == "PROVIDER_LAUNCH_FAILED"
    _assert_terminal_log(outcome.run_dir, "INFRA_ERROR PROVIDER_LAUNCH_FAILED")


# Break caught: losing provider mutations on failure or letting an artifact error mask it.
@pytest.mark.parametrize(
    ("name", "delay_seconds", "exit_code", "expected_code", "timed_out"),
    (
        ("timeout", 1, 0, "PROVIDER_TIMEOUT", True),
        ("nonzero", 0, 9, "PROVIDER_EXIT_NONZERO", False),
    ),
)
def test_run_once_retains_failed_provider_mutations_and_provider_error_precedence(
    build_config_case,
    fake_provider,
    monkeypatch,
    name: str,
    delay_seconds: float,
    exit_code: int,
    expected_code: str,
    timed_out: bool,
) -> None:
    case = build_config_case(
        name=name,
        fixtures=(("sources/input.txt", "input.txt", b"original\n"),),
    )
    fixture_bytes = f"{name} fixture\n".encode()
    evidence_bytes = f"{name} evidence\n".encode()
    fake_provider.configure(
        monkeypatch,
        stdout=b"raw stdout",
        stderr=b"raw stderr",
        exit_code=exit_code,
        delay_seconds=delay_seconds,
        fixture_bytes=fixture_bytes,
        evidence_name="provider-output.txt",
        evidence_bytes=evidence_bytes,
    )
    if timed_out:
        monkeypatch.setattr(providers_module, "PROVIDER_TIMEOUT_SECONDS", 0.2)
        monkeypatch.setattr(providers_module, "TERMINATE_GRACE_SECONDS", 0.01)
    original_write_bytes = Path.write_bytes

    def fail_stdout(path: Path, contents: bytes) -> int:
        if path.name == "stdout.txt":
            raise OSError("stdout failed")
        return original_write_bytes(path, contents)

    monkeypatch.setattr(Path, "write_bytes", fail_stdout)

    outcome = run_once(case.config_path)

    assert outcome.exit_code == 1
    assert outcome.run_dir is not None
    result = _validate_result(outcome.run_dir)
    assert result["execution"]["invocation_started"] is True
    assert result["execution"]["timed_out"] is timed_out
    if timed_out:
        assert isinstance(result["execution"]["exit_code"], int)
    else:
        assert result["execution"]["exit_code"] == 9
    assert result["infrastructure_error"]["code"] == expected_code
    assert result["artifacts"]["stdout"]["exists"] is False
    assert result["artifacts"]["fixture"]["entries"] == [
        _file_entry("input.txt", fixture_bytes)
    ]
    assert result["artifacts"]["evidence"]["entries"] == [
        _file_entry("provider-output.txt", evidence_bytes)
    ]
    assert (outcome.run_dir / "workspace/fixture/input.txt").read_bytes() == fixture_bytes
    assert (
        outcome.run_dir / "workspace/evidence/provider-output.txt"
    ).read_bytes() == evidence_bytes
    _assert_terminal_log(outcome.run_dir, f"INFRA_ERROR {expected_code}")


# Break caught: reporting a successful invocation after a retained artifact cannot be written.
def test_run_once_emits_artifact_write_failed_after_successful_provider(
    build_config_case, fake_provider, monkeypatch
) -> None:
    case = build_config_case(name="artifact-failed")
    fake_provider.configure(
        monkeypatch,
        stdout=b"raw stdout",
        stderr=b"raw stderr",
        final=b"final",
    )
    original_write_bytes = Path.write_bytes

    def fail_stdout(path: Path, contents: bytes) -> int:
        if path.name == "stdout.txt":
            raise OSError("stdout failed")
        return original_write_bytes(path, contents)

    monkeypatch.setattr(Path, "write_bytes", fail_stdout)

    outcome = run_once(case.config_path)

    assert outcome.exit_code == 1
    assert outcome.run_dir is not None
    result = _validate_result(outcome.run_dir)
    assert result["execution"]["invocation_started"] is True
    assert result["execution"]["timed_out"] is False
    assert result["execution"]["exit_code"] == 0
    assert result["infrastructure_error"]["code"] == "ARTIFACT_WRITE_FAILED"
    assert result["artifacts"]["stdout"]["exists"] is False
    assert (outcome.run_dir / "stderr.txt").read_bytes() == b"raw stderr"
    assert (outcome.run_dir / "final.txt").read_bytes() == b"final"
    _assert_terminal_log(outcome.run_dir, "INFRA_ERROR ARTIFACT_WRITE_FAILED")


# Break caught: leaving a partial result behind when atomic publication fails.
def test_run_once_cleans_partial_result_after_publication_failure(
    build_config_case, fake_provider, monkeypatch
) -> None:
    case = build_config_case(name="publication-failed")
    fake_provider.configure(monkeypatch, final=b"final")
    original_replace = Path.replace

    def fail_result_replace(path: Path, target: Path) -> Path:
        if target.name == "result.json":
            raise OSError("result failed")
        return original_replace(path, target)

    monkeypatch.setattr(results_module.Path, "replace", fail_result_replace)

    outcome = run_once(case.config_path)

    assert outcome.exit_code == 1
    assert outcome.run_dir is not None
    assert outcome.diagnostic == "result artifact write failed: result failed"
    assert not (outcome.run_dir / "result.json").exists()
    assert not list(outcome.run_dir.glob(".result-*"))
