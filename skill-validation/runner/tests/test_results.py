"""Result schema and retained-directory inventory contracts."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import jsonschema
import pytest

import skilltest.results as results_module
from skilltest.config import ExecutionDeclaration, TestConfig as Config
from skilltest.providers import ProviderResult
from skilltest.workspace import RunContext


SCHEMA_PATH = Path(__file__).parents[1] / "result.schema.json"
SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
EMPTY_DIGEST = hashlib.sha256(b"").hexdigest()
ERROR_CODES = (
    "PREPARATION_FAILED",
    "PROVIDER_LAUNCH_FAILED",
    "PROVIDER_TIMEOUT",
    "PROVIDER_EXIT_NONZERO",
    "ARTIFACT_WRITE_FAILED",
)


def _file(path: str) -> dict[str, Any]:
    return {"path": path, "exists": False, "bytes": None, "sha256": None}


def _directory(path: str) -> dict[str, Any]:
    return {"path": path, "exists": True, "empty": True, "entries": []}


def _completed_record() -> dict[str, Any]:
    return {
        "schema_version": "0.2",
        "run_id": "20260828T120000000Z-result-case-unique",
        "status": "COMPLETED",
        "started_at": "2026-08-28T12:00:00.000Z",
        "finished_at": "2026-08-28T12:00:01.000Z",
        "duration_seconds": 1.0,
        "test": {"id": "result-case"},
        "execution": {
            "provider": "codex",
            "model": "gpt-5.6-sol",
            "effort": "high",
            "executable": "codex",
            "timeout_seconds": 900,
            "invocation_started": True,
            "timed_out": False,
            "exit_code": 0,
        },
        "artifacts": {
            "config": _file("config.json"),
            "prompt_template": _file("prompt-template.txt"),
            "prompt": _file("prompt.txt"),
            "stdout": _file("stdout.txt"),
            "stderr": _file("stderr.txt"),
            "final": _file("final.txt"),
            "fixture": _directory("workspace/fixture"),
            "evidence": _directory("workspace/evidence"),
        },
        "infrastructure_error": None,
    }


def _state_record(code: str | None) -> dict[str, Any]:
    record = _completed_record()
    if code is None:
        return record
    record["status"] = "INFRA_ERROR"
    record["infrastructure_error"] = {"code": code, "message": "mechanical failure"}
    execution = record["execution"]
    if code in {"PREPARATION_FAILED", "PROVIDER_LAUNCH_FAILED"}:
        execution.update(
            {"invocation_started": False, "timed_out": False, "exit_code": None}
        )
    elif code == "PROVIDER_TIMEOUT":
        execution.update(
            {"invocation_started": True, "timed_out": True, "exit_code": -15}
        )
    elif code == "PROVIDER_EXIT_NONZERO":
        execution.update(
            {"invocation_started": True, "timed_out": False, "exit_code": 7}
        )
    elif code == "ARTIFACT_WRITE_FAILED":
        execution.update(
            {"invocation_started": True, "timed_out": False, "exit_code": 0}
        )
    return record


def _validate(record: dict[str, Any]) -> None:
    jsonschema.validate(record, SCHEMA)


def _reject(record: dict[str, Any]) -> None:
    with pytest.raises(jsonschema.ValidationError):
        _validate(record)


def _set(record: dict[str, Any], dotted_path: str, value: Any) -> None:
    target: dict[str, Any] = record
    parts = dotted_path.split(".")
    for part in parts[:-1]:
        target = target[part]
    target[parts[-1]] = value


def _context(tmp_path: Path) -> RunContext:
    run_dir = tmp_path / "run"
    workspace_dir = run_dir / "workspace"
    return RunContext(
        run_id="20260828T120000000Z-result-case-unique",
        started_at="2026-08-28T12:00:00.000Z",
        run_dir=run_dir,
        marker_path=run_dir / ".skilltest-run",
        config_path=run_dir / "config.json",
        prompt_template_path=run_dir / "prompt-template.txt",
        prompt_path=run_dir / "prompt.txt",
        workspace_dir=workspace_dir,
        fixture_dir=workspace_dir / "fixture",
        evidence_dir=workspace_dir / "evidence",
        stdout_path=run_dir / "stdout.txt",
        stderr_path=run_dir / "stderr.txt",
        final_output_path=run_dir / "final.txt",
        runner_log_path=run_dir / "runner.log",
        result_path=run_dir / "result.json",
    )


def _config(context: RunContext) -> Config:
    return Config(
        schema_version="0.2",
        id="result-case",
        prompt=context.prompt_template_path,
        fixtures=(),
        execution=ExecutionDeclaration("codex", "gpt-5.6-sol", "high"),
        config_path=context.config_path,
        config_bytes=b"{}",
    )


# Catches removal or widening of any of the six exhaustive execution states.
@pytest.mark.parametrize("code", (None, *ERROR_CODES))
def test_schema_accepts_each_valid_execution_state(code: str | None) -> None:
    _validate(_state_record(code))


# Catches state branches that validate fields independently instead of as one row.
@pytest.mark.parametrize(
    ("code", "path", "value"),
    (
        (None, "execution.timed_out", True),
        ("PREPARATION_FAILED", "execution.invocation_started", True),
        ("PROVIDER_LAUNCH_FAILED", "execution.exit_code", 0),
        ("PROVIDER_TIMEOUT", "execution.timed_out", False),
        ("PROVIDER_EXIT_NONZERO", "execution.exit_code", 0),
        ("ARTIFACT_WRITE_FAILED", "execution.exit_code", 7),
    ),
)
def test_schema_rejects_an_invalid_mutation_of_every_execution_state(
    code: str | None, path: str, value: Any
) -> None:
    record = _state_record(code)
    _set(record, path, value)
    _reject(record)


# Catches error-state branches whose code constraint applies vacuously to null.
@pytest.mark.parametrize("code", ERROR_CODES)
def test_schema_requires_an_error_object_for_every_error_state(code: str) -> None:
    record = _state_record(code)
    record["infrastructure_error"] = None
    _reject(record)


# Catches independent scalar constraints drifting from the producer contract.
@pytest.mark.parametrize(
    ("path", "value"),
    (
        ("schema_version", "0.1"),
        ("run_id", ""),
        ("started_at", "2026-08-28"),
        ("finished_at", "not-a-timestamp"),
        ("duration_seconds", -1),
        ("test.id", "INVALID"),
        ("execution.model", ""),
        ("execution.effort", "HIGH"),
        ("execution.executable", "other-provider"),
        ("execution.timeout_seconds", 901),
    ),
)
def test_schema_rejects_each_independent_record_invariant(
    path: str, value: Any
) -> None:
    record = _completed_record()
    _set(record, path, value)
    _reject(record)


# Catches a schema that permits the executable to disagree with its provider.
def test_schema_rejects_provider_executable_mismatch() -> None:
    record = _completed_record()
    record["execution"]["executable"] = "claude"
    _reject(record)


# Catches nullable metadata that is not coupled to file existence.
@pytest.mark.parametrize("artifact_name", ("config", "prompt_template", "prompt", "stdout", "stderr", "final"))
@pytest.mark.parametrize(("exists", "field", "value"), (
    (True, "bytes", None),
    (True, "sha256", None),
    (False, "bytes", 0),
    (False, "sha256", EMPTY_DIGEST),
))
def test_schema_couples_every_file_artifact_metadata_to_existence(
    artifact_name: str, exists: bool, field: str, value: Any
) -> None:
    record = _completed_record()
    artifact = record["artifacts"][artifact_name]
    artifact.update({"exists": exists, "bytes": 0 if exists else None, "sha256": EMPTY_DIGEST if exists else None})
    artifact[field] = value
    _reject(record)


# Catches missing-directory metadata or an empty flag inconsistent with entries.
@pytest.mark.parametrize("artifact_name", ("fixture", "evidence"))
@pytest.mark.parametrize(
    ("exists", "empty", "entries"),
    (
        (False, False, []),
        (False, None, [{"path": "file", "type": "file", "bytes": 0, "sha256": EMPTY_DIGEST}]),
        (True, False, []),
        (True, True, [{"path": "file", "type": "file", "bytes": 0, "sha256": EMPTY_DIGEST}]),
    ),
)
def test_schema_rejects_inconsistent_directory_artifacts(
    artifact_name: str, exists: bool, empty: bool | None, entries: list[dict[str, Any]]
) -> None:
    record = _completed_record()
    record["artifacts"][artifact_name].update(
        {"exists": exists, "empty": empty, "entries": entries}
    )
    _reject(record)


# Catches invalid file metadata and metadata leakage onto non-file entry types.
@pytest.mark.parametrize(
    ("entry_type", "bytes_value", "digest"),
    (
        ("file", -1, EMPTY_DIGEST),
        ("file", 0.5, EMPTY_DIGEST),
        ("file", 0, "A" * 64),
        ("file", None, EMPTY_DIGEST),
        ("file", 0, None),
        ("directory", 0, None),
        ("directory", None, EMPTY_DIGEST),
        ("symlink", 0, None),
        ("symlink", None, EMPTY_DIGEST),
        ("other", 0, None),
        ("other", None, EMPTY_DIGEST),
    ),
)
def test_schema_rejects_invalid_directory_entry_metadata(
    entry_type: str, bytes_value: Any, digest: str | None
) -> None:
    record = _completed_record()
    record["artifacts"]["evidence"].update({
        "empty": False,
        "entries": [{"path": "entry", "type": entry_type, "bytes": bytes_value, "sha256": digest}],
    })
    _reject(record)


# Catches schemas that do not keep every object level closed and required.
@pytest.mark.parametrize(
    ("level", "required_key"),
    (
        ("root", "run_id"),
        ("test", "id"),
        ("execution", "model"),
        ("artifacts", "prompt"),
        ("file_artifact", "exists"),
        ("directory_artifact", "empty"),
        ("directory_entry", "type"),
        ("infrastructure_error", "message"),
    ),
)
@pytest.mark.parametrize("mutation", ("missing", "unknown"))
def test_schema_keeps_each_object_level_closed_and_required(
    level: str, required_key: str, mutation: str
) -> None:
    record = _state_record("PROVIDER_EXIT_NONZERO")
    record["artifacts"]["evidence"].update({
        "empty": False,
        "entries": [{"path": "entry", "type": "file", "bytes": 0, "sha256": EMPTY_DIGEST}],
    })
    targets = {
        "root": record,
        "test": record["test"],
        "execution": record["execution"],
        "artifacts": record["artifacts"],
        "file_artifact": record["artifacts"]["config"],
        "directory_artifact": record["artifacts"]["evidence"],
        "directory_entry": record["artifacts"]["evidence"]["entries"][0],
        "infrastructure_error": record["infrastructure_error"],
    }
    target = targets[level]
    if mutation == "missing":
        target.pop(required_key)
    else:
        target["unknown"] = True
    _reject(record)


# Catches inventory code that follows symlinks, omits directories, or emits unstable order.
def test_directory_artifact_inventory_is_sorted_mechanical_and_non_following(
    tmp_path: Path,
) -> None:
    run_dir = tmp_path / "run"
    evidence_dir = run_dir / "workspace" / "evidence"
    (evidence_dir / "z-empty").mkdir(parents=True)
    (evidence_dir / "a-tree").mkdir()
    (evidence_dir / "a-tree" / "payload.txt").write_bytes(b"retained")
    (evidence_dir / "link").symlink_to("a-tree", target_is_directory=True)

    artifact = results_module._directory_artifact(evidence_dir, run_dir)

    assert artifact["path"] == "workspace/evidence"
    assert artifact["exists"] is True
    assert artifact["empty"] is False
    assert [entry["path"] for entry in artifact["entries"]] == [
        "a-tree",
        "a-tree/payload.txt",
        "link",
        "z-empty",
    ]
    assert all(set(entry) == {"path", "type", "bytes", "sha256"} for entry in artifact["entries"])
    entries = {entry["path"]: entry for entry in artifact["entries"]}
    assert entries["a-tree"] == {
        "path": "a-tree", "type": "directory", "bytes": None, "sha256": None
    }
    assert entries["a-tree/payload.txt"] == {
        "path": "a-tree/payload.txt",
        "type": "file",
        "bytes": 8,
        "sha256": hashlib.sha256(b"retained").hexdigest(),
    }
    assert entries["link"] == {
        "path": "link", "type": "symlink", "bytes": None, "sha256": None
    }
    assert entries["z-empty"] == {
        "path": "z-empty", "type": "directory", "bytes": None, "sha256": None
    }
    assert "link/payload.txt" not in entries


# Catches a schema that cannot represent a mechanically discovered special entry.
def test_schema_accepts_other_directory_entry_type() -> None:
    record = _completed_record()
    record["artifacts"]["evidence"].update({
        "empty": False,
        "entries": [{"path": "special", "type": "other", "bytes": None, "sha256": None}],
    })
    _validate(record)


# Catches result construction that inventories fixture inputs instead of retained final state.
def test_result_record_uses_schema_02_paths_and_final_retained_fixture_state(
    tmp_path: Path,
) -> None:
    context = _context(tmp_path)
    context.fixture_dir.mkdir(parents=True)
    context.evidence_dir.mkdir()
    contents = {
        context.config_path: b"{}",
        context.prompt_template_path: b"template",
        context.prompt_path: b"rendered",
        context.stdout_path: b"stdout",
        context.stderr_path: b"stderr",
        context.final_output_path: b"final",
    }
    for path, data in contents.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    mutated = context.fixture_dir / "mutable.txt"
    mutated.write_bytes(b"initial")
    mutated.write_bytes(b"final retained state")

    record = results_module.result_record(
        context,
        _config(context),
        ProviderResult("codex", True, exit_code=0),
        None,
        "2026-08-28T12:00:01.000Z",
        1.0,
    )

    _validate(record)
    assert set(record) == {
        "schema_version", "run_id", "status", "started_at", "finished_at",
        "duration_seconds", "test", "execution", "artifacts", "infrastructure_error",
    }
    assert record["test"] == {"id": "result-case"}
    assert {name: artifact["path"] for name, artifact in record["artifacts"].items()} == {
        "config": "config.json",
        "prompt_template": "prompt-template.txt",
        "prompt": "prompt.txt",
        "stdout": "stdout.txt",
        "stderr": "stderr.txt",
        "final": "final.txt",
        "fixture": "workspace/fixture",
        "evidence": "workspace/evidence",
    }
    assert record["artifacts"]["fixture"] == {
        "path": "workspace/fixture",
        "exists": True,
        "empty": False,
        "entries": [{
            "path": "mutable.txt",
            "type": "file",
            "bytes": len(b"final retained state"),
            "sha256": hashlib.sha256(b"final retained state").hexdigest(),
        }],
    }
    for artifact_name, path in (
        ("config", context.config_path),
        ("prompt_template", context.prompt_template_path),
        ("prompt", context.prompt_path),
        ("stdout", context.stdout_path),
        ("stderr", context.stderr_path),
        ("final", context.final_output_path),
    ):
        artifact = record["artifacts"][artifact_name]
        assert artifact["bytes"] == len(contents[path])
        assert artifact["sha256"] == hashlib.sha256(contents[path]).hexdigest()
