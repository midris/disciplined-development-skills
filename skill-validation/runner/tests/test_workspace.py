import os
import stat
from pathlib import Path

import pytest

import skilltest.workspace as workspace_module


def _entries(root: Path) -> list[str]:
    paths: list[str] = []
    for directory, directories, files in os.walk(root, followlinks=False):
        base = Path(directory)
        for name in sorted([*directories, *files]):
            paths.append((base / name).relative_to(root).as_posix())
    return sorted(paths)


def _visible_bytes(root: Path) -> list[bytes]:
    values: list[bytes] = []
    for directory, _, files in os.walk(root, followlinks=False):
        base = Path(directory)
        for name in files:
            path = base / name
            if stat.S_ISREG(path.lstat().st_mode):
                values.append(path.read_bytes())
    return values


# Catches allocation regressions that reuse a run directory or initialize it before ownership.
def test_create_run_allocates_distinct_serial_directories(
    build_config_case: object, monkeypatch: pytest.MonkeyPatch
) -> None:
    case = build_config_case(name="serial", fixture="none")
    run_root = case.root / "tmp"
    with monkeypatch.context() as context:
        context.setattr(workspace_module.tempfile, "gettempdir", lambda: str(run_root))
        first = workspace_module.create_run(case.config)
        second = workspace_module.create_run(case.config)

    expected_base = (run_root / "skilltest-runs").resolve()
    assert first.run_dir.parent == expected_base
    assert second.run_dir.parent == expected_base
    assert first.run_dir != second.run_dir
    assert first.run_id == first.run_dir.name
    assert second.run_id == second.run_dir.name
    assert case.config.id in first.run_dir.name
    assert case.config.id in second.run_dir.name
    assert first.started_at.endswith("Z")
    assert first.run_dir.is_dir()
    assert not first.marker_path.exists()
    assert not first.inputs_dir.exists()
    assert not first.workspace_dir.exists()
    assert not first.config_path.exists()
    assert not first.subject_input_path.exists()
    assert not first.stdout_path.exists()
    assert not first.stderr_path.exists()
    assert not first.final_output_path.exists()
    assert not first.runner_log_path.exists()
    assert not first.result_path.exists()


# Catches layout and subject-input regressions for the no-fixture case.
def test_prepare_workspace_builds_exact_layout_for_absent_fixture(
    build_config_case: object, monkeypatch: pytest.MonkeyPatch
) -> None:
    case = build_config_case(
        name="empty-fixture",
        fixture="none",
        dependencies=(),
        prompt_bytes=b"prompt without trailing newline",
    )
    with monkeypatch.context() as context:
        context.setattr(workspace_module.tempfile, "gettempdir", lambda: str(case.root / "tmp"))
        run = workspace_module.create_run(case.config)
        prepared = workspace_module.prepare_workspace(run, case.config)

    assert _entries(run.run_dir) == [
        ".skilltest-run",
        "inputs",
        "inputs/fixture",
        "inputs/prompt.txt",
        "inputs/skills",
        "inputs/skills/primary",
        "inputs/skills/primary/SKILL.md",
        "inputs/skills/primary/scripts",
        "inputs/skills/primary/scripts/tool.sh",
        "subject-input.txt",
        "workspace",
        "workspace/supplied-skills",
        "workspace/supplied-skills/primary",
        "workspace/supplied-skills/primary/SKILL.md",
        "workspace/supplied-skills/primary/scripts",
        "workspace/supplied-skills/primary/scripts/tool.sh",
    ]
    assert run.inputs_prompt_path.read_bytes() == case.prompt_bytes
    assert run.inputs_fixture_dir.is_dir()
    assert not any(run.inputs_fixture_dir.iterdir())
    assert prepared.workspace_dir == run.workspace_dir
    assert prepared.subject_input_path == run.subject_input_path
    assert prepared.final_output_path == run.final_output_path
    assert prepared.subject_input_bytes == (
        b"For skill instructions, use only the supplied files listed below.\n"
        b"Primary: primary \xe2\x80\x94 supplied-skills/primary/SKILL.md\n"
        b"Dependencies: none\n"
        b"Read those files before acting.\n"
        b"Scenario follows:\n"
        b"prompt without trailing newline"
    )
    assert run.subject_input_path.read_bytes() == prepared.subject_input_bytes
    assert not run.config_path.exists()


# Catches layout regressions that treat a declared empty fixture like an absent one.
def test_prepare_workspace_retains_declared_empty_fixture_directory(
    build_config_case: object, monkeypatch: pytest.MonkeyPatch
) -> None:
    case = build_config_case(name="declared-empty-fixture", fixture="empty")
    with monkeypatch.context() as context:
        context.setattr(workspace_module.tempfile, "gettempdir", lambda: str(case.root / "tmp"))
        run = workspace_module.create_run(case.config)
        prepared = workspace_module.prepare_workspace(run, case.config)

    assert run.inputs_fixture_dir.is_dir()
    assert not any(run.inputs_fixture_dir.iterdir())
    assert _entries(run.run_dir) == [
        ".skilltest-run",
        "inputs",
        "inputs/fixture",
        "inputs/prompt.txt",
        "inputs/skills",
        "inputs/skills/helper-a",
        "inputs/skills/helper-a/SKILL.md",
        "inputs/skills/helper-a/resources",
        "inputs/skills/helper-a/resources/notes.txt",
        "inputs/skills/helper-b",
        "inputs/skills/helper-b/SKILL.md",
        "inputs/skills/helper-b/resources",
        "inputs/skills/helper-b/resources/notes.txt",
        "inputs/skills/primary",
        "inputs/skills/primary/SKILL.md",
        "inputs/skills/primary/scripts",
        "inputs/skills/primary/scripts/tool.sh",
        "subject-input.txt",
        "workspace",
        "workspace/supplied-skills",
        "workspace/supplied-skills/helper-a",
        "workspace/supplied-skills/helper-a/SKILL.md",
        "workspace/supplied-skills/helper-a/resources",
        "workspace/supplied-skills/helper-a/resources/notes.txt",
        "workspace/supplied-skills/helper-b",
        "workspace/supplied-skills/helper-b/SKILL.md",
        "workspace/supplied-skills/helper-b/resources",
        "workspace/supplied-skills/helper-b/resources/notes.txt",
        "workspace/supplied-skills/primary",
        "workspace/supplied-skills/primary/SKILL.md",
        "workspace/supplied-skills/primary/scripts",
        "workspace/supplied-skills/primary/scripts/tool.sh",
    ]
    assert prepared.workspace_dir == run.workspace_dir
    assert prepared.workspace_dir.is_dir()
    assert sorted(path.name for path in prepared.workspace_dir.iterdir()) == ["supplied-skills"]
    assert not run.config_path.exists()


# Catches copy-order and hidden-expected-outcome regressions for populated fixtures.
def test_prepare_workspace_copies_populated_inputs_and_hides_expected_outcome(
    build_config_case: object, monkeypatch: pytest.MonkeyPatch
) -> None:
    case = build_config_case(
        name="populated-fixture",
        fixture="populated",
        dependencies=("helper-b", "helper-a"),
        prompt_bytes=b"line one\nline two",
        expected_marker="never-show-this-secret",
    )
    with monkeypatch.context() as context:
        context.setattr(workspace_module.tempfile, "gettempdir", lambda: str(case.root / "tmp"))
        run = workspace_module.create_run(case.config)
        prepared = workspace_module.prepare_workspace(run, case.config)

    assert run.inputs_prompt_path.read_bytes() == case.prompt_bytes
    assert (run.inputs_fixture_dir / "docs" / "guide.txt").read_text() == "fixture guide\n"
    assert (run.inputs_fixture_dir / "bin" / "start.sh").read_bytes() == b"#!/bin/sh\necho fixture\n"
    assert (prepared.workspace_dir / "docs" / "guide.txt").read_text() == "fixture guide\n"
    assert (prepared.workspace_dir / "bin" / "start.sh").read_bytes() == b"#!/bin/sh\necho fixture\n"
    assert not (prepared.workspace_dir / "fixture").exists()
    assert (
        prepared.workspace_dir / "supplied-skills" / "helper-b" / "resources" / "notes.txt"
    ).read_text() == "resource for helper-b\n"
    assert (
        prepared.workspace_dir / "supplied-skills" / "helper-a" / "resources" / "notes.txt"
    ).read_text() == "resource for helper-a\n"
    assert prepared.subject_input_bytes == (
        b"For skill instructions, use only the supplied files listed below.\n"
        b"Primary: primary \xe2\x80\x94 supplied-skills/primary/SKILL.md\n"
        b"Dependencies: helper-b \xe2\x80\x94 supplied-skills/helper-b/SKILL.md; "
        b"helper-a \xe2\x80\x94 supplied-skills/helper-a/SKILL.md\n"
        b"Read those files before acting.\n"
        b"Scenario follows:\n"
        b"line one\nline two"
    )
    provider_visible = [prepared.subject_input_bytes, *_visible_bytes(prepared.workspace_dir)]
    assert all(case.expected_marker.encode("utf-8") not in value for value in provider_visible)
    assert all(b'"expected_outcome"' not in value for value in provider_visible)
    assert not run.config_path.exists()
