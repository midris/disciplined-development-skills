"""Black-box checks for the skilltest commands."""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys

from skilltest import cli as cli_module
from skilltest.runner import RunOutcome


def test_run_command_has_one_bundle_per_external_invocation(
    build_config_case, capsys, fake_provider, monkeypatch, tmp_path: Path
) -> None:
    # Break caught: removing the public ``skilltest run CONFIG`` entry point.
    command = Path(sys.executable).with_name("skilltest")
    assert command.is_file()

    case = build_config_case(name="cli")
    temporary_root = tmp_path / "temporary-root"
    temporary_root.mkdir()
    fake_provider.configure(monkeypatch, final=b"final")

    def normal_environment() -> dict[str, str]:
        return os.environ.copy() | {"TMPDIR": str(temporary_root)}

    def invoke(
        *arguments: str,
        env: dict[str, str] | None = None,
        cwd: Path | None = None,
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [str(command), *arguments],
            check=False,
            capture_output=True,
            text=True,
            env=normal_environment() if env is None else env,
            cwd=cwd,
        )

    for arguments in (
        (),
        ("run",),
        ("run", str(case.config_path), "extra"),
        ("unknown", str(case.config_path)),
    ):
        misuse = invoke(*arguments)
        assert misuse.returncode == 2
        assert misuse.stdout == ""
        assert "usage:" in misuse.stderr

    invalid_config = tmp_path / "invalid.json"
    invalid_config.write_text("{", encoding="utf-8")
    invalid = invoke("run", str(invalid_config))
    assert invalid.returncode == 2
    assert invalid.stdout == ""
    assert "invalid JSON configuration" in invalid.stderr
    assert not (temporary_root / "skilltest-runs").exists()

    invalid_utf8 = build_config_case(name="invalid-utf8")
    (invalid_utf8.root / "prompt.md").write_bytes(b"\xff")
    invalid_prompt = invoke("run", str(invalid_utf8.config_path))
    assert invalid_prompt.returncode == 2
    assert invalid_prompt.stdout == ""
    assert "prompt must be readable UTF-8" in invalid_prompt.stderr
    assert not (temporary_root / "skilltest-runs").exists()

    successful_runs = [invoke("run", str(case.config_path)) for _ in range(2)]
    serial_run_dirs = [Path(process.stdout.strip()) for process in successful_runs]
    assert all(process.returncode == 0 for process in successful_runs)
    assert all(process.stderr == "" for process in successful_runs)
    assert all(run_dir.is_absolute() and run_dir.is_dir() for run_dir in serial_run_dirs)
    assert len(set(serial_run_dirs)) == 2

    fake_provider.configure(monkeypatch, final=b"final", exit_code=9)
    provider_failure = invoke("run", str(case.config_path))
    failed_run_dir = Path(provider_failure.stdout.strip())
    assert provider_failure.returncode == 1
    assert provider_failure.stderr == "skilltest: run failed\n"
    assert failed_run_dir.is_absolute() and failed_run_dir.is_dir()

    # Break caught: dropping either output channel when a failed run owns a bundle.
    diagnostic_run_dir = tmp_path / "diagnostic-run"
    diagnostic_run_dir.mkdir()
    monkeypatch.setattr(
        cli_module,
        "run_once",
        lambda _: RunOutcome(1, diagnostic_run_dir, "result artifact write failed"),
    )
    assert cli_module.main(["run", "ignored.json"]) == 1
    captured = capsys.readouterr()
    assert captured.err == "skilltest: result artifact write failed\n"
    assert captured.out == f"{diagnostic_run_dir.resolve()}\n"

    allocation_root = tmp_path / "allocation-root"
    allocation_root.mkdir()
    (allocation_root / "skilltest-runs").write_text("not a directory", encoding="utf-8")
    allocation_environment = normal_environment() | {"TMPDIR": str(allocation_root)}
    allocation_failure = invoke("run", str(case.config_path), env=allocation_environment)
    assert allocation_failure.returncode == 1
    assert allocation_failure.stdout == ""
    assert "run allocation failed:" in allocation_failure.stderr

    fake_provider.configure(monkeypatch, final=b"final")
    processes = [
        subprocess.Popen(
            [str(command), "run", str(case.config_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=normal_environment(),
        )
        for _ in range(2)
    ]
    simultaneous_results = [process.communicate() for process in processes]
    simultaneous_run_dirs = [Path(stdout.strip()) for stdout, _ in simultaneous_results]
    assert all(process.returncode == 0 for process in processes)
    assert all(stderr == "" for _, stderr in simultaneous_results)
    assert all(run_dir.is_absolute() and run_dir.is_dir() for run_dir in simultaneous_run_dirs)
    assert len(set(simultaneous_run_dirs)) == 2

    help_output = invoke("--help")
    assert help_output.returncode == 0
    assert "{run,worksheet}" in help_output.stdout
    assert "promote" not in help_output.stdout
    assert "clean" not in help_output.stdout

    # Break caught: omitting or weakening the public worksheet command contract.
    worksheet_repository = tmp_path / "worksheet-repo"
    scenario_argument = "skill-validation/scenarios/example/worksheet-case"
    scenario = worksheet_repository / scenario_argument
    scenario.mkdir(parents=True)
    (scenario / "rubric.md").write_bytes(b"CLI rubric\n")
    run_bundle = worksheet_repository / "run-bundle"
    run_bundle.mkdir()
    result_path = run_bundle / "result.json"
    record = {
        "run_id": "20260902T120000000Z-worksheet-case-cli",
        "status": "COMPLETED",
        "started_at": "2026-09-02T12:00:00.000Z",
        "finished_at": "2026-09-02T12:00:01.000Z",
        "duration_seconds": 1.0,
        "test": {"id": "worksheet-case"},
        "execution": {
            "provider": "codex",
            "model": "gpt-5.6-sol",
            "effort": "high",
        },
        "artifacts": {
            "config": {"path": "config.json", "sha256": "a" * 64},
            "prompt_template": {
                "path": "prompt-template.txt",
                "sha256": "b" * 64,
            },
            "prompt": {"path": "prompt.txt", "sha256": "c" * 64},
            "fixture": {"entries": []},
        },
        "infrastructure_error": None,
    }
    result_path.write_text(json.dumps(record), encoding="utf-8")
    output_path = worksheet_repository / "worksheet.md"

    for arguments in (
        ("worksheet",),
        ("worksheet", scenario_argument),
        ("worksheet", scenario_argument, str(run_bundle)),
        (
            "worksheet",
            scenario_argument,
            str(run_bundle),
            "--output",
            str(output_path),
            "extra",
        ),
    ):
        misuse = invoke(*arguments, cwd=worksheet_repository)
        assert misuse.returncode == 2
        assert misuse.stdout == ""
        assert "usage:" in misuse.stderr

    success = invoke(
        "worksheet",
        scenario_argument,
        str(run_bundle),
        "--output",
        str(output_path),
        cwd=worksheet_repository,
    )
    assert success.returncode == 0
    assert success.stderr == ""
    assert success.stdout == f"{output_path.resolve()}\n"
    expected = """# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/example/worksheet-case |
| Scenario ID | worksheet-case |
| Scenario purpose |  |
| Run ID | 20260902T120000000Z-worksheet-case-cli |
| Provider | codex |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-02T12:00:00.000Z |
| Finished | 2026-09-02T12:00:01.000Z |
| Duration seconds | 1.0 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa |
| Prompt template | prompt-template.txt | bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb |
| Rendered prompt | prompt.txt | cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/example/worksheet-case/rubric.md | f3a3e9bd547e243543d2a2d21fa85f4dce16c18f53db0c39d408e506cdf487af |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
|  |  |  |  |  |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
|  |  |  |  |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
|  |  |  |  |

## Readability

| Observation | Evidence |
|---|---|
|  |  |

## Verdict

| Field | Value |
|---|---|
| Overall verdict |  |
| Rationale |  |
| Disposition |  |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities |  |
| Scenario defects |  |
| Proposed methodology changes |  |
"""
    assert output_path.read_bytes() == expected.encode("utf-8")

    malformed_output = worksheet_repository / "malformed.md"
    result_path.write_text("{", encoding="utf-8")
    malformed = invoke(
        "worksheet",
        scenario_argument,
        str(run_bundle),
        "--output",
        str(malformed_output),
        cwd=worksheet_repository,
    )
    assert malformed.returncode == 2
    assert malformed.stdout == ""
    assert malformed.stderr.startswith("skilltest: ")
    assert malformed.stderr.count("skilltest:") == 1
    assert not malformed_output.exists()

    incomplete_output = worksheet_repository / "incomplete.md"
    result_path.write_text(json.dumps({}), encoding="utf-8")
    incomplete = invoke(
        "worksheet",
        scenario_argument,
        str(run_bundle),
        "--output",
        str(incomplete_output),
        cwd=worksheet_repository,
    )
    assert incomplete.returncode == 2
    assert incomplete.stdout == ""
    assert incomplete.stderr.startswith("skilltest: ")
    assert incomplete.stderr.count("skilltest:") == 1
    assert not incomplete_output.exists()

    result_path.write_text(json.dumps(record), encoding="utf-8")
    collision_output = worksheet_repository / "collision.md"
    collision_output.write_bytes(b"owner bytes\n")
    collision = invoke(
        "worksheet",
        scenario_argument,
        str(run_bundle),
        "--output",
        str(collision_output),
        cwd=worksheet_repository,
    )
    assert collision.returncode == 1
    assert collision.stdout == ""
    assert collision.stderr.startswith("skilltest: ")
    assert collision.stderr.count("skilltest:") == 1
    assert collision_output.read_bytes() == b"owner bytes\n"

    missing_parent_output = worksheet_repository / "missing" / "worksheet.md"
    missing_parent = invoke(
        "worksheet",
        scenario_argument,
        str(run_bundle),
        "--output",
        str(missing_parent_output),
        cwd=worksheet_repository,
    )
    assert missing_parent.returncode == 1
    assert missing_parent.stdout == ""
    assert missing_parent.stderr.startswith("skilltest: ")
    assert missing_parent.stderr.count("skilltest:") == 1
    assert not missing_parent_output.parent.exists()
