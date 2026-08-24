"""Straight-line orchestration for one retained skill-test run."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from time import monotonic

from skilltest.config import ConfigError, TestConfig, load_config
from skilltest.providers import ProviderRequest, ProviderResult, _arguments, invoke_provider
from skilltest.results import publish_result, result_record
from skilltest.workspace import RunContext, create_run, prepare_workspace


@dataclass(frozen=True, slots=True)
class RunOutcome:
    exit_code: int
    run_dir: Path | None
    diagnostic: str | None


def run_once(config_path: Path) -> RunOutcome:
    """Load, allocate, prepare, invoke once, retain outputs, and publish one result."""
    try:
        config = load_config(config_path)
    except ConfigError as error:
        return RunOutcome(2, None, str(error))
    started = monotonic()
    try:
        context = create_run(config)
    except OSError as error:
        return RunOutcome(1, None, f"run allocation failed: {error}")

    result = ProviderResult(config.execution.provider, False)
    error = _log_error(context, f"run {context.run_id} allocated", "PREPARATION_FAILED")
    if error is not None:
        return _finish(context, config, result, error, started)
    try:
        prepared = prepare_workspace(context, config)
    except OSError as failure:
        return _finish(
            context, config, result,
            ("PREPARATION_FAILED", f"workspace preparation failed: {failure}"), started,
        )
    error = _log_error(context, "workspace prepared", "PREPARATION_FAILED")
    if error is not None:
        return _finish(context, config, result, error, started)

    request = ProviderRequest(
        prepared.workspace_dir, prepared.subject_input_bytes, prepared.final_output_path,
        config.execution.provider, config.execution.model, config.execution.effort,
    )
    error = _log_error(context, f"provider arguments: {_arguments(request)!r}", "PREPARATION_FAILED")
    if error is not None:
        return _finish(context, config, result, error, started)
    error = _log_error(context, "provider invocation attempted", "PREPARATION_FAILED")
    if error is not None:
        return _finish(context, config, result, error, started)
    result = invoke_provider(request)
    provider_error = _provider_error(result)
    log_error = _provider_log_error(context, result)
    artifact_error = _write_provider_artifacts(context, result)
    error = provider_error or log_error or artifact_error
    return _finish(context, config, result, error, started)


def _provider_error(result: ProviderResult) -> tuple[str, str] | None:
    if not result.invocation_started:
        return "PROVIDER_LAUNCH_FAILED", f"{result.executable} launch failed: {result.launch_error}"
    if result.timed_out:
        return "PROVIDER_TIMEOUT", f"{result.executable} timed out"
    if result.exit_code != 0:
        return "PROVIDER_EXIT_NONZERO", f"{result.executable} exited with code {result.exit_code}"
    return None


def _provider_log_error(context: RunContext, result: ProviderResult) -> tuple[str, str] | None:
    if not result.invocation_started:
        return _log_error(context, "provider launch failed", "ARTIFACT_WRITE_FAILED")
    return _log_error(
        context,
        "provider returned" if not result.timed_out else "provider timed out",
        "ARTIFACT_WRITE_FAILED",
    )


def _write_provider_artifacts(
    context: RunContext, result: ProviderResult
) -> tuple[str, str] | None:
    stdout_error = _write_artifact(context, context.stdout_path, result.stdout_bytes, "provider raw stdout")
    stderr_error = _write_artifact(context, context.stderr_path, result.stderr_bytes, "provider raw stderr")
    return stdout_error or stderr_error


def _write_artifact(
    context: RunContext, path: Path, contents: bytes, name: str
) -> tuple[str, str] | None:
    try:
        path.write_bytes(contents)
    except OSError as error:
        return "ARTIFACT_WRITE_FAILED", f"{name} write failed: {error}"
    return _log_error(context, f"{name} written", "ARTIFACT_WRITE_FAILED")


def _finish(
    context: RunContext,
    config: TestConfig,
    result: ProviderResult,
    error: tuple[str, str] | None,
    started: float,
) -> RunOutcome:
    try:
        context.config_path.write_bytes(config.config_bytes)
    except OSError as failure:
        config_error = ("ARTIFACT_WRITE_FAILED", f"configuration artifact write failed: {failure}")
    else:
        config_error = _log_error(context, "configuration snapshot written", "ARTIFACT_WRITE_FAILED")
    error = error or config_error
    terminal = "COMPLETED" if error is None else f"INFRA_ERROR {error[0]}"
    terminal_error = _log_error(context, terminal, "ARTIFACT_WRITE_FAILED")
    error = error or terminal_error
    try:
        record = result_record(context, config, result, error, "", 0)
        record["finished_at"] = _timestamp()
        record["duration_seconds"] = round(monotonic() - started, 3)
        publish_result(context.result_path, record)
    except OSError as failure:
        diagnostic = f"result artifact write failed: {failure}"
        _log_error(context, diagnostic, "ARTIFACT_WRITE_FAILED")
        return RunOutcome(1, context.run_dir, diagnostic)
    return RunOutcome(0 if error is None else 1, context.run_dir, None)


def _log_error(
    context: RunContext, message: str, code: str
) -> tuple[str, str] | None:
    try:
        with context.runner_log_path.open("a", encoding="utf-8") as log_file:
            log_file.write(f"{_timestamp()} {message}\n")
    except OSError as error:
        return code, f"runner log write failed: {error}"
    return None


def _timestamp() -> str:
    return datetime.now(UTC).isoformat(timespec="milliseconds").replace("+00:00", "Z")
