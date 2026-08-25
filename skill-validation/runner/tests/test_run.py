"""End-to-end persistence checks for one skill-test run."""

from __future__ import annotations

import copy
import hashlib
import json
import os
from pathlib import Path

import jsonschema
import pytest

import skilltest.results as results_module
import skilltest.runner as runner_module
from skilltest.runner import run_once


def _result(run_dir: Path) -> dict[str, object]:
    return json.loads((run_dir / "result.json").read_text(encoding="utf-8"))


def _validate_result(run_dir: Path) -> dict[str, object]:
    result = _result(run_dir)
    schema_path = Path(__file__).parents[1] / "result.schema.json"
    jsonschema.validate(result, json.loads(schema_path.read_text(encoding="utf-8")))
    return result


def _assert_log(run_dir: Path, *, provider_returned: bool, terminal: str) -> None:
    messages = [line.split(" ", 1)[1] for line in (run_dir / "runner.log").read_text().splitlines()]
    assert messages[0].endswith(" allocated")
    assert "workspace prepared" in messages
    assert any(message.startswith("provider arguments: ") for message in messages)
    assert "provider invocation attempted" in messages
    assert ("provider returned" in messages) is provider_returned
    assert "provider raw stdout written" in messages
    assert "provider raw stderr written" in messages
    assert "configuration snapshot written" in messages
    assert messages[-1] == terminal


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _assert_digests(run_dir: Path, result: dict[str, object]) -> None:
    input_paths = [record["path"] for record in result["inputs"]]
    assert input_paths == sorted(input_paths)
    expected_input_paths = sorted(
        (Path(directory, name).relative_to(run_dir).as_posix())
        for directory, _, files in os.walk(run_dir / "inputs")
        for name in files
    )
    assert input_paths == expected_input_paths
    for record in result["inputs"]:
        path = run_dir / record["path"]
        assert set(record) == {"path", "bytes", "sha256"}
        assert record["bytes"] == path.stat().st_size
        assert record["sha256"] == _digest(path)
    for record in result["artifacts"].values():
        if "sha256" not in record or not record["exists"]:
            continue
        path = run_dir / record["path"]
        assert record["bytes"] == path.stat().st_size
        assert record["sha256"] == _digest(path)


def test_run_once_persists_complete_codex_and_claude_bundles(
    build_config_case, fake_provider, monkeypatch
) -> None:
    cases = (
        ("codex", b"", b"", None, False),
        ("claude", b"not-json\n", b"claude stderr", None, True),
    )
    for provider, stdout, stderr, final, write_final in cases:
        case = build_config_case(
            name=f"{provider}-complete", fixture="populated", prompt_bytes=b""
        )
        config = json.loads(case.config_path.read_text(encoding="utf-8"))
        config["execution"]["provider"] = provider
        case.config_path.write_text(json.dumps(config, separators=(",", ":")), encoding="utf-8")
        fake_provider.configure(monkeypatch, stdout=stdout, stderr=stderr, final=b"", write_final=write_final)

        outcome = run_once(case.config_path)

        assert outcome.exit_code == 0
        assert outcome.run_dir is not None
        result = _validate_result(outcome.run_dir)
        assert result["status"] == "COMPLETED"
        assert result["infrastructure_error"] is None
        _assert_log(outcome.run_dir, provider_returned=True, terminal="COMPLETED")
        invalid_path_record = copy.deepcopy(result)
        invalid_path_record["artifacts"]["config"]["path"] = "other.json"
        with pytest.raises(jsonschema.ValidationError):
            jsonschema.validate(
                invalid_path_record,
                json.loads((Path(__file__).parents[1] / "result.schema.json").read_text()),
            )
        assert result["execution"] == {
            "provider": provider,
            "model": "gpt-5.4",
            "effort": "medium",
            "executable": provider,
            "timeout_seconds": 900,
            "invocation_started": True,
            "timed_out": False,
            "exit_code": 0,
        }
        assert (outcome.run_dir / "stdout.txt").read_bytes() == stdout
        assert (outcome.run_dir / "stderr.txt").read_bytes() == stderr
        final_path = outcome.run_dir / "final.txt"
        assert (final_path.read_bytes() if final_path.exists() else None) == final
        assert (outcome.run_dir / "config.json").read_bytes() == case.config_path.read_bytes()
        assert case.expected_marker not in (outcome.run_dir / "subject-input.txt").read_text()
        assert case.expected_marker not in "".join(
            path.read_text(errors="ignore")
            for path in (outcome.run_dir / "workspace").rglob("*")
            if path.is_file()
        )
        _assert_digests(outcome.run_dir, result)

    timing_case = build_config_case(name="timing")
    fake_provider.configure(monkeypatch, final=b"final")
    original_result_record = runner_module.result_record
    construction_complete = False

    def delayed_result_record(*args, **kwargs):
        nonlocal construction_complete
        record = original_result_record(*args, **kwargs)
        construction_complete = True
        return record

    def clock() -> float:
        return 12.0 if construction_complete else 10.0

    monkeypatch.setattr(runner_module, "result_record", delayed_result_record)
    monkeypatch.setattr(
        runner_module,
        "_timestamp",
        lambda: "2026-08-23T00:00:02.000Z" if construction_complete else "2026-08-23T00:00:00.000Z",
    )
    monkeypatch.setattr(runner_module, "monotonic", clock)
    timing_outcome = run_once(timing_case.config_path)
    timing_result = _result(timing_outcome.run_dir)
    assert timing_outcome.exit_code == 0
    assert construction_complete is True
    assert timing_result["finished_at"] == "2026-08-23T00:00:02.000Z"
    assert timing_result["duration_seconds"] == 2.0

    assert fake_provider.config_observations() == [
        {"before_output": False, "after_output": False},
        {"before_output": False, "after_output": False},
        {"before_output": False, "after_output": False},
    ]
    digest_path = outcome.run_dir / "stdout.txt"
    original_read_bytes = Path.read_bytes

    def forbid_full_read(path: Path) -> bytes:
        if path == digest_path:
            raise AssertionError("digest read a whole file")
        return original_read_bytes(path)

    monkeypatch.setattr(Path, "read_bytes", forbid_full_read)
    assert results_module._sha256(digest_path) == hashlib.sha256(b"not-json\n").hexdigest()


# Catches a result mutation that omits the explicit mode or transforms the no-skill prompt before provider invocation.
def test_run_once_persists_no_skill_context_result(
    build_config_case, fake_provider, monkeypatch
) -> None:
    case = build_config_case(
        name="no-skill-result",
        fixture="populated",
        no_skill_context=True,
        prompt_bytes=b"use only the supplied descriptions",
    )
    fake_provider.configure(monkeypatch, final=b"final")

    outcome = run_once(case.config_path)

    assert outcome.exit_code == 0
    assert outcome.run_dir is not None
    result = _validate_result(outcome.run_dir)
    assert fake_provider.record()["stdin"] == case.prompt_bytes.decode("utf-8")
    assert result["test"] == {
        "id": "no-skill-result-run",
        "skill_context": "none",
        "scenario": "no-skill-result-scenario",
    }


def test_run_once_persists_all_infrastructure_error_classes(
    build_config_case, fake_provider, monkeypatch
) -> None:
    import skilltest.providers as providers_module
    import skilltest.workspace as workspace_module

    cases = (
        ("PREPARATION_FAILED", "codex", {"preparation": True}),
        ("PROVIDER_LAUNCH_FAILED", "codex", {"launch": True}),
        ("PROVIDER_TIMEOUT", "codex", {"timeout": True}),
        ("PROVIDER_EXIT_NONZERO", "codex", {"exit_code": 9}),
        ("ARTIFACT_WRITE_FAILED", "codex", {
            "artifact": True, "stdout": b"raw stdout", "stderr": b"raw stderr",
        }),
        ("ARTIFACT_WRITE_FAILED", "codex", {"publication": True}),
        ("ARTIFACT_WRITE_FAILED", "codex", {"construction": True}),
        ("PREPARATION_FAILED", "codex", {"log": True}),
        ("PREPARATION_FAILED", "codex", {"layout": True}),
        ("PREPARATION_FAILED", "codex", {"attempt_log": True}),
    )
    for index, (expected_code, provider, setting) in enumerate(cases):
        case = build_config_case(name=f"error-{index}")
        config = json.loads(case.config_path.read_text(encoding="utf-8"))
        config["execution"]["provider"] = provider
        case.config_path.write_text(json.dumps(config, separators=(",", ":")), encoding="utf-8")
        fake_provider.configure(monkeypatch, final=b"final", **{
            key: value for key, value in setting.items()
            if key in {"stdout", "stderr", "exit_code", "write_final"}
        })
        provider_records_before = (
            fake_provider.record_path.read_bytes()
            if fake_provider.record_path.exists()
            else b""
        )
        with monkeypatch.context() as scoped:
            if setting.get("preparation"):
                scoped.setattr(
                    workspace_module.shutil, "copy2",
                    lambda *args, **kwargs: (_ for _ in ()).throw(OSError("copy failed")),
                )
            if setting.get("launch"):
                scoped.setenv("PATH", str(case.root / "missing-bin"))
            if setting.get("timeout"):
                fake_provider.configure(monkeypatch, final=b"final", delay_seconds=0.02)
                scoped.setattr(providers_module, "PROVIDER_TIMEOUT_SECONDS", 0)
            if setting.get("artifact"):
                original_write = Path.write_bytes

                def fail_stdout(path: Path, data: bytes) -> int:
                    if path.name == "stdout.txt":
                        raise OSError("stdout failed")
                    return original_write(path, data)

                scoped.setattr(Path, "write_bytes", fail_stdout)
            if setting.get("publication"):
                original_replace = Path.replace

                def fail_publication(path: Path, target: Path) -> Path:
                    if target.name == "result.json":
                        raise OSError("result failed")
                    return original_replace(path, target)

                scoped.setattr(results_module.Path, "replace", fail_publication)
            if setting.get("construction"):
                scoped.setattr(
                    runner_module,
                    "result_record",
                    lambda *args, **kwargs: (_ for _ in ()).throw(OSError("record failed")),
                )
            if setting.get("log"):
                original_open = Path.open

                def fail_log(path: Path, *args, **kwargs):
                    if path.name == "runner.log":
                        raise OSError("log failed")
                    return original_open(path, *args, **kwargs)

                scoped.setattr(Path, "open", fail_log)
            if setting.get("attempt_log"):
                original_open = Path.open
                attempt_log_write = 0

                def fail_only_invocation_attempt(path: Path, *args, **kwargs):
                    nonlocal attempt_log_write
                    if path.name == "runner.log" and args and args[0] == "a":
                        attempt_log_write += 1
                        if attempt_log_write == 4:
                            raise OSError("attempt log failed")
                    return original_open(path, *args, **kwargs)

                scoped.setattr(Path, "open", fail_only_invocation_attempt)
            if setting.get("layout"):
                original_touch = workspace_module.Path.touch

                def fail_marker(path: Path, *args, **kwargs) -> None:
                    if path.name == ".skilltest-run":
                        raise OSError("marker failed")
                    return original_touch(path, *args, **kwargs)

                scoped.setattr(workspace_module.Path, "touch", fail_marker)
            outcome = run_once(case.config_path)

        assert outcome.exit_code == 1
        assert outcome.run_dir is not None
        if setting.get("publication") or setting.get("construction"):
            assert outcome.diagnostic is not None
            assert not (outcome.run_dir / "result.json").exists()
            if setting.get("publication"):
                assert not list(outcome.run_dir.glob(".result-*"))
            continue
        result = _validate_result(outcome.run_dir)
        assert result["status"] == "INFRA_ERROR"
        assert result["infrastructure_error"]["code"] == expected_code
        assert (outcome.run_dir / "config.json").read_bytes() == case.config_path.read_bytes()
        if setting.get("artifact"):
            assert (outcome.run_dir / "stdout.txt").exists() is False
            assert (outcome.run_dir / "stderr.txt").read_bytes() == b"raw stderr"
        if setting.get("launch"):
            _assert_log(
                outcome.run_dir,
                provider_returned=False,
                terminal="INFRA_ERROR PROVIDER_LAUNCH_FAILED",
            )
        if setting.get("log"):
            assert not (outcome.run_dir / "runner.log").exists()
        if setting.get("attempt_log"):
            assert fake_provider.record_path.read_bytes() == provider_records_before
            assert "provider invocation attempted" not in (outcome.run_dir / "runner.log").read_text()
        _assert_digests(outcome.run_dir, result)


def test_run_once_rejects_invalid_config_without_an_owned_run(tmp_path: Path) -> None:
    config_path = tmp_path / "invalid.json"
    config_path.write_text("{", encoding="utf-8")

    outcome = run_once(config_path)

    assert outcome.exit_code == 2
    assert outcome.run_dir is None
    assert outcome.diagnostic is not None
