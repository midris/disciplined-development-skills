"""Mechanical result-record construction and atomic publication."""

from __future__ import annotations

import hashlib
import json
import os
import stat
import tempfile
from pathlib import Path
from typing import Any

from skilltest.config import TestConfig
from skilltest.providers import PROVIDER_TIMEOUT_SECONDS, ProviderResult
from skilltest.workspace import RunContext


ERROR_CODES = {
    "PREPARATION_FAILED", "PROVIDER_LAUNCH_FAILED", "PROVIDER_TIMEOUT",
    "PROVIDER_EXIT_NONZERO", "ARTIFACT_WRITE_FAILED",
}


def result_record(
    context: RunContext,
    config: TestConfig,
    provider_result: ProviderResult,
    error: tuple[str, str] | None,
    finished_at: str,
    duration_seconds: float,
) -> dict[str, Any]:
    """Build the schema 0.2 record from retained artifacts without interpreting content."""
    if error is not None and error[0] not in ERROR_CODES:
        raise ValueError(f"unknown infrastructure error code: {error[0]}")
    execution_record = {
        "provider": config.execution.provider,
        "model": config.execution.model,
        "effort": config.execution.effort,
        "executable": provider_result.executable,
        "timeout_seconds": PROVIDER_TIMEOUT_SECONDS,
        "invocation_started": provider_result.invocation_started,
        "timed_out": provider_result.timed_out,
        "exit_code": provider_result.exit_code,
    }
    return {
        "schema_version": "0.2",
        "run_id": context.run_id,
        "status": "COMPLETED" if error is None else "INFRA_ERROR",
        "started_at": context.started_at,
        "finished_at": finished_at,
        "duration_seconds": duration_seconds,
        "test": {"id": config.id},
        "execution": execution_record,
        "artifacts": {
            "config": _file_artifact(context.config_path, context.run_dir),
            "prompt_template": _file_artifact(context.prompt_template_path, context.run_dir),
            "prompt": _file_artifact(context.prompt_path, context.run_dir),
            "stdout": _file_artifact(context.stdout_path, context.run_dir),
            "stderr": _file_artifact(context.stderr_path, context.run_dir),
            "final": _file_artifact(context.final_output_path, context.run_dir),
            "fixture": _directory_artifact(context.fixture_dir, context.run_dir),
            "evidence": _directory_artifact(context.evidence_dir, context.run_dir),
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


def _file_artifact(path: Path, run_dir: Path) -> dict[str, Any]:
    record: dict[str, Any] = {"path": path.relative_to(run_dir).as_posix(), "exists": path.is_file()}
    if record["exists"]:
        record.update({"bytes": path.stat().st_size, "sha256": _sha256(path)})
    else:
        record.update({"bytes": None, "sha256": None})
    return record


def _directory_artifact(path: Path, run_dir: Path) -> dict[str, Any]:
    """Inventory one retained directory without following symlinks."""
    try:
        exists = stat.S_ISDIR(path.lstat().st_mode)
    except FileNotFoundError:
        exists = False

    entries: list[dict[str, Any]] = []

    def visit(directory: Path) -> None:
        for child in directory.iterdir():
            status = child.lstat()
            mode = status.st_mode
            if stat.S_ISREG(mode):
                entry_type = "file"
                size: int | None = status.st_size
                digest: str | None = _sha256(child)
            elif stat.S_ISDIR(mode):
                entry_type = "directory"
                size = None
                digest = None
            elif stat.S_ISLNK(mode):
                entry_type = "symlink"
                size = None
                digest = None
            else:
                entry_type = "other"
                size = None
                digest = None
            entries.append({
                "path": child.relative_to(path).as_posix(),
                "type": entry_type,
                "bytes": size,
                "sha256": digest,
            })
            if entry_type == "directory":
                visit(child)

    if exists:
        visit(path)
        entries.sort(key=lambda entry: entry["path"])
    return {
        "path": path.relative_to(run_dir).as_posix(),
        "exists": exists,
        "empty": not entries if exists else None,
        "entries": entries,
    }


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
