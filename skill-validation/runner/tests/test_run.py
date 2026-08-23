"""End-to-end persistence checks for one skill-test run."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import jsonschema
import pytest

from skilltest.runner import run_once


def _result(run_dir: Path) -> dict[str, object]:
    return json.loads((run_dir / "result.json").read_text(encoding="utf-8"))


def _validate_result(run_dir: Path) -> dict[str, object]:
    result = _result(run_dir)
    schema_path = Path(__file__).parents[1] / "result.schema.json"
    jsonschema.validate(result, json.loads(schema_path.read_text(encoding="utf-8")))
    return result


def _assert_log(run_dir: Path, *, provider_started: bool, terminal: str) -> None:
    messages = [line.split(" ", 1)[1] for line in (run_dir / "runner.log").read_text().splitlines()]
    assert messages[0].endswith(" allocated")
    assert "workspace prepared" in messages
    assert any(message.startswith("provider arguments: ") for message in messages)
    assert ("provider started" in messages) is provider_started
    assert ("provider exited" in messages) is provider_started
    assert "provider raw stdout written" in messages
    assert "provider raw stderr written" in messages
    assert "configuration snapshot written" in messages
    assert messages[-1] == terminal


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _assert_digests(run_dir: Path, result: dict[str, object]) -> None:
    input_paths = [record["path"] for record in result["inputs"]]
    assert input_paths == sorted(input_paths)
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
        ("codex", b"codex stdout", b"codex stderr", b"codex final"),
        ("claude", b'{"type":"result","result":"claude final"}\n', b"claude stderr", b"claude final"),
    )
    for provider, stdout, stderr, final in cases:
        case = build_config_case(name=f"{provider}-complete", fixture="populated")
        config = json.loads(case.config_path.read_text(encoding="utf-8"))
        config["execution"]["provider"] = provider
        case.config_path.write_text(json.dumps(config, separators=(",", ":")), encoding="utf-8")
        fake_provider.configure(
            monkeypatch, stdout=stdout, stderr=stderr, final=final
        )

        outcome = run_once(case.config_path)

        assert outcome.exit_code == 0
        assert outcome.run_dir is not None
        result = _validate_result(outcome.run_dir)
        assert result["status"] == "COMPLETED"
        assert result["infrastructure_error"] is None
        _assert_log(outcome.run_dir, provider_started=True, terminal="COMPLETED")
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
        assert (outcome.run_dir / "final.txt").read_bytes() == final
        assert (outcome.run_dir / "config.json").read_bytes() == case.config_path.read_bytes()
        assert case.expected_marker not in (outcome.run_dir / "subject-input.txt").read_text()
        assert case.expected_marker not in "".join(
            path.read_text(errors="ignore")
            for path in (outcome.run_dir / "workspace").rglob("*")
            if path.is_file()
        )
        _assert_digests(outcome.run_dir, result)

    assert fake_provider.config_observations() == [
        {"before_output": False, "after_output": False},
        {"before_output": False, "after_output": False},
    ]


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
        ("PROVIDER_OUTPUT_INVALID", "claude", {"stdout": b"not json\n"}),
        ("FINAL_OUTPUT_MISSING", "codex", {"write_final": False}),
        ("ARTIFACT_WRITE_FAILED", "codex", {
            "artifact": True, "stdout": b"raw stdout", "stderr": b"raw stderr",
        }),
        ("ARTIFACT_WRITE_FAILED", "claude", {
            "final_write": True,
            "stdout": b'{"type":"result","result":"final"}\n',
        }),
        ("ARTIFACT_WRITE_FAILED", "codex", {"publication": True}),
        ("PREPARATION_FAILED", "codex", {"log": True}),
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
            if setting.get("final_write"):
                original_write = Path.write_bytes

                def fail_final(path: Path, data: bytes) -> int:
                    if path.name == "final.txt":
                        raise OSError("final failed")
                    return original_write(path, data)

                scoped.setattr(Path, "write_bytes", fail_final)
            if setting.get("publication"):
                import skilltest.results as results_module

                original_replace = Path.replace

                def fail_publication(path: Path, target: Path) -> Path:
                    if target.name == "result.json":
                        raise OSError("result failed")
                    return original_replace(path, target)

                scoped.setattr(results_module.Path, "replace", fail_publication)
            if setting.get("log"):
                original_open = Path.open

                def fail_log(path: Path, *args, **kwargs):
                    if path.name == "runner.log":
                        raise OSError("log failed")
                    return original_open(path, *args, **kwargs)

                scoped.setattr(Path, "open", fail_log)
            outcome = run_once(case.config_path)

        assert outcome.exit_code == 1
        assert outcome.run_dir is not None
        if setting.get("publication"):
            assert outcome.diagnostic is not None
            assert not (outcome.run_dir / "result.json").exists()
            assert not list(outcome.run_dir.glob(".result-*"))
            continue
        result = _validate_result(outcome.run_dir)
        assert result["status"] == "INFRA_ERROR"
        assert result["infrastructure_error"]["code"] == expected_code
        assert (outcome.run_dir / "config.json").read_bytes() == case.config_path.read_bytes()
        if setting.get("artifact"):
            assert (outcome.run_dir / "stdout.txt").exists() is False
            assert (outcome.run_dir / "stderr.txt").read_bytes() == b"raw stderr"
        if setting.get("final_write"):
            assert (outcome.run_dir / "stdout.txt").read_bytes() == setting["stdout"]
            assert (outcome.run_dir / "stderr.txt").read_bytes() == b""
            assert result["execution"]["exit_code"] == 0
        if setting.get("launch"):
            _assert_log(
                outcome.run_dir,
                provider_started=False,
                terminal="INFRA_ERROR PROVIDER_LAUNCH_FAILED",
            )
        if setting.get("log"):
            assert not (outcome.run_dir / "runner.log").exists()
        _assert_digests(outcome.run_dir, result)


def test_run_once_rejects_invalid_config_without_an_owned_run(tmp_path: Path) -> None:
    config_path = tmp_path / "invalid.json"
    config_path.write_text("{", encoding="utf-8")

    outcome = run_once(config_path)

    assert outcome.exit_code == 2
    assert outcome.run_dir is None
    assert outcome.diagnostic is not None
