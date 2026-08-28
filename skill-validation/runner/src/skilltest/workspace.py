"""Run-directory allocation and isolated prompt-workspace preparation."""

from __future__ import annotations

import shutil
import tempfile
import uuid
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

from skilltest.config import TestConfig


@dataclass(frozen=True, slots=True)
class RunContext:
    run_id: str
    started_at: str
    run_dir: Path
    marker_path: Path
    config_path: Path
    prompt_template_path: Path
    prompt_path: Path
    workspace_dir: Path
    fixture_dir: Path
    evidence_dir: Path
    stdout_path: Path
    stderr_path: Path
    final_output_path: Path
    runner_log_path: Path
    result_path: Path


@dataclass(frozen=True, slots=True)
class PreparedRun:
    workspace_dir: Path
    prompt_bytes: bytes
    final_output_path: Path


def create_run(config: TestConfig) -> RunContext:
    """Allocate one unique retained run directory and its fixed paths."""
    now = datetime.now(UTC)
    started_at = _timestamp(now)
    run_root = Path(tempfile.gettempdir()).resolve() / "skilltest-runs"
    run_root.mkdir(parents=True, exist_ok=True)
    run_dir = Path(
        tempfile.mkdtemp(
            prefix=f"{now.strftime('%Y%m%dT%H%M%S%f')[:-3]}Z-{config.id}-{uuid.uuid4()}-",
            dir=run_root,
        )
    )
    run_id = run_dir.name
    workspace_dir = run_dir / "workspace"

    return RunContext(
        run_id=run_id,
        started_at=started_at,
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


def prepare_workspace(context: RunContext, config: TestConfig) -> PreparedRun:
    """Prepare an isolated fixture and evidence workspace plus rendered prompt."""
    context.marker_path.touch()
    context.fixture_dir.mkdir(parents=True)
    context.evidence_dir.mkdir()
    shutil.copy2(config.prompt, context.prompt_template_path)
    template = context.prompt_template_path.read_text(encoding="utf-8")
    rendered = template
    for token, path in (
        ("{{workspace_dir}}", context.workspace_dir),
        ("{{fixture_dir}}", context.fixture_dir),
        ("{{evidence_dir}}", context.evidence_dir),
    ):
        rendered = rendered.replace(token, str(path.resolve()))
    prompt_bytes = rendered.encode("utf-8")
    context.prompt_path.write_bytes(prompt_bytes)

    for fixture in config.fixtures:
        destination = context.fixture_dir / fixture.target
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(fixture.source, destination)

    return PreparedRun(
        workspace_dir=context.workspace_dir,
        prompt_bytes=prompt_bytes,
        final_output_path=context.final_output_path,
    )


def _timestamp(value: datetime) -> str:
    return value.isoformat(timespec="milliseconds").replace("+00:00", "Z")
