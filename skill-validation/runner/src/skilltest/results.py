"""Mechanical result-record construction and atomic publication."""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Any

from skilltest.config import TestConfig
from skilltest.providers import PROVIDER_TIMEOUT_SECONDS, ProviderResult
from skilltest.workspace import RunContext


ERROR_CODES = {
    "PREPARATION_FAILED", "PROVIDER_LAUNCH_FAILED", "PROVIDER_TIMEOUT",
    "PROVIDER_EXIT_NONZERO", "PROVIDER_OUTPUT_INVALID", "FINAL_OUTPUT_MISSING",
    "ARTIFACT_WRITE_FAILED",
}


def result_record(
    context: RunContext,
    config: TestConfig,
    provider_result: ProviderResult,
    error: tuple[str, str] | None,
    finished_at: str,
    duration_seconds: float,
) -> dict[str, Any]:
    """Build the version-one record from retained artifacts without interpreting content."""
    if error is not None and error[0] not in ERROR_CODES:
        raise ValueError(f"unknown infrastructure error code: {error[0]}")
    return {
        "schema_version": 1,
        "run_id": context.run_id,
        "status": "COMPLETED" if error is None else "INFRA_ERROR",
        "started_at": context.started_at,
        "finished_at": finished_at,
        "duration_seconds": duration_seconds,
        "test": {
            "id": config.id,
            "skill": config.skill.id,
            "dependencies": [item.id for item in config.dependencies],
            "scenario": config.scenario.id,
        },
        "execution": {
            "provider": config.execution.provider,
            "model": config.execution.model,
            "effort": config.execution.effort,
            "executable": provider_result.executable,
            "timeout_seconds": PROVIDER_TIMEOUT_SECONDS,
            "invocation_started": provider_result.invocation_started,
            "timed_out": provider_result.timed_out,
            "exit_code": provider_result.exit_code,
        },
        "inputs": _input_records(context.inputs_dir, context.run_dir),
        "artifacts": {
            "config": _file_artifact(context.config_path, context.run_dir),
            "subject_input": _file_artifact(context.subject_input_path, context.run_dir),
            "stdout": _file_artifact(context.stdout_path, context.run_dir),
            "stderr": _file_artifact(context.stderr_path, context.run_dir),
            "final": _file_artifact(context.final_output_path, context.run_dir),
            "workspace": {"path": "workspace", "exists": context.workspace_dir.is_dir()},
        },
        "infrastructure_error": (
            None if error is None else {"code": error[0], "message": error[1]}
        ),
    }


def publish_result(path: Path, record: dict[str, Any]) -> None:
    """Atomically replace the final result record in its owned run directory."""
    encoded = json.dumps(record, indent=2, sort_keys=True).encode("utf-8") + b"\n"
    descriptor, temporary_name = tempfile.mkstemp(prefix=".result-", dir=path.parent)
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as temporary_file:
            temporary_file.write(encoded)
        temporary_path.replace(path)
    except BaseException:
        temporary_path.unlink(missing_ok=True)
        raise


def _input_records(inputs_dir: Path, run_dir: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for directory, _, files in os.walk(inputs_dir):
        for name in files:
            path = Path(directory, name)
            if path.is_file():
                records.append({
                    "path": path.relative_to(run_dir).as_posix(),
                    "bytes": path.stat().st_size,
                    "sha256": _sha256(path),
                })
    return sorted(records, key=lambda record: record["path"])


def _file_artifact(path: Path, run_dir: Path) -> dict[str, Any]:
    record: dict[str, Any] = {"path": path.relative_to(run_dir).as_posix(), "exists": path.is_file()}
    if record["exists"]:
        record.update({"bytes": path.stat().st_size, "sha256": _sha256(path)})
    else:
        record.update({"bytes": None, "sha256": None})
    return record


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()
