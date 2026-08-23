"""Run-directory allocation and workspace preparation."""

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
    inputs_dir: Path
    inputs_prompt_path: Path
    inputs_fixture_dir: Path
    inputs_skills_dir: Path
    subject_input_path: Path
    workspace_dir: Path
    stdout_path: Path
    stderr_path: Path
    final_output_path: Path
    runner_log_path: Path
    result_path: Path


@dataclass(frozen=True, slots=True)
class PreparedRun:
    workspace_dir: Path
    subject_input_path: Path
    subject_input_bytes: bytes
    final_output_path: Path


def create_run(config: TestConfig) -> RunContext:
    """Allocate one unique retained run directory and its fixed paths."""
    now = datetime.now(UTC)
    started_at = _timestamp(now)
    run_root = Path(tempfile.gettempdir()).resolve() / "skilltest-runs"
    run_root.mkdir(parents=True, exist_ok=True)
    run_id = Path(
        tempfile.mkdtemp(
            prefix=f"{now.strftime('%Y%m%dT%H%M%S%f')[:-3]}Z-{config.id}-{uuid.uuid4()}-",
            dir=run_root,
        )
    ).name
    run_dir = run_root / run_id

    marker_path = run_dir / ".skilltest-run"
    inputs_dir = run_dir / "inputs"
    inputs_prompt_path = inputs_dir / "prompt.txt"
    inputs_fixture_dir = inputs_dir / "fixture"
    inputs_skills_dir = inputs_dir / "skills"
    subject_input_path = run_dir / "subject-input.txt"
    workspace_dir = run_dir / "workspace"

    marker_path.touch()
    inputs_fixture_dir.mkdir(parents=True)
    inputs_skills_dir.mkdir()
    workspace_dir.mkdir()

    return RunContext(
        run_id=run_id,
        started_at=started_at,
        run_dir=run_dir,
        marker_path=marker_path,
        config_path=run_dir / "config.json",
        inputs_dir=inputs_dir,
        inputs_prompt_path=inputs_prompt_path,
        inputs_fixture_dir=inputs_fixture_dir,
        inputs_skills_dir=inputs_skills_dir,
        subject_input_path=subject_input_path,
        workspace_dir=workspace_dir,
        stdout_path=run_dir / "stdout.txt",
        stderr_path=run_dir / "stderr.txt",
        final_output_path=run_dir / "final.txt",
        runner_log_path=run_dir / "runner.log",
        result_path=run_dir / "result.json",
    )


def prepare_workspace(context: RunContext, config: TestConfig) -> PreparedRun:
    """Populate retained inputs, prepare the workspace, and write subject input."""
    shutil.copy2(config.scenario.prompt, context.inputs_prompt_path)

    for declaration in (config.skill, *config.dependencies):
        retained_skill = context.inputs_skills_dir / declaration.id
        shutil.copytree(declaration.source, retained_skill)

    if config.scenario.fixture is not None:
        shutil.copytree(
            config.scenario.fixture,
            context.inputs_fixture_dir,
            dirs_exist_ok=True,
        )
        shutil.copytree(
            context.inputs_fixture_dir,
            context.workspace_dir,
            dirs_exist_ok=True,
        )

    supplied_skills_dir = context.workspace_dir / "supplied-skills"
    supplied_skills_dir.mkdir()
    for declaration in (config.skill, *config.dependencies):
        shutil.copytree(
            context.inputs_skills_dir / declaration.id,
            supplied_skills_dir / declaration.id,
        )

    subject_input_bytes = _subject_input_bytes(
        primary_id=config.skill.id,
        dependency_ids=tuple(declaration.id for declaration in config.dependencies),
        prompt_bytes=context.inputs_prompt_path.read_bytes(),
    )
    context.subject_input_path.write_bytes(subject_input_bytes)
    return PreparedRun(
        workspace_dir=context.workspace_dir,
        subject_input_path=context.subject_input_path,
        subject_input_bytes=subject_input_bytes,
        final_output_path=context.final_output_path,
    )


def _subject_input_bytes(
    *, primary_id: str, dependency_ids: tuple[str, ...], prompt_bytes: bytes
) -> bytes:
    if dependency_ids:
        dependencies = "; ".join(
            f"{dependency_id} — supplied-skills/{dependency_id}/SKILL.md"
            for dependency_id in dependency_ids
        )
    else:
        dependencies = "none"
    preamble = (
        "For skill instructions, use only the supplied files listed below.\n"
        f"Primary: {primary_id} — supplied-skills/{primary_id}/SKILL.md\n"
        f"Dependencies: {dependencies}\n"
        "Read those files before acting.\n"
        "Scenario follows:\n"
    ).encode("utf-8")
    return preamble + prompt_bytes


def _timestamp(value: datetime) -> str:
    return value.isoformat(timespec="milliseconds").replace("+00:00", "Z")
