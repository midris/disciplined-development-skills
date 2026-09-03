"""Focused checks for fixed skill-test worksheet generation."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from skilltest.worksheet import (
    WorksheetInputError,
    WorksheetOutputError,
    write_worksheet,
)


SCENARIO_ARGUMENT = "skill-validation/scenarios/example/worksheet-case"


def _build_inputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    *,
    scenario_argument: str = SCENARIO_ARGUMENT,
) -> tuple[dict[str, object], Path, Path, Path]:
    repository = tmp_path / "repo"
    scenario = repository / scenario_argument
    scenario.mkdir(parents=True)
    (scenario / "rubric.md").write_bytes(b"withheld rubric\n")

    run_bundle = repository / "run-bundle"
    run_bundle.mkdir()
    record: dict[str, object] = {
        "run_id": "20260902T120000000Z-worksheet-case-unique",
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
            "fixture": {
                "entries": [
                    {
                        "path": "skills/example/SKILL.md",
                        "type": "file",
                        "sha256": "d" * 64,
                    },
                    {
                        "path": "sources/input.md",
                        "type": "file",
                        "sha256": "e" * 64,
                    },
                ]
            },
        },
        "infrastructure_error": None,
    }
    result_path = run_bundle / "result.json"
    result_path.write_text(json.dumps(record), encoding="utf-8")
    monkeypatch.chdir(repository)
    return record, scenario, run_bundle, repository / "worksheet.md"


def _write_record(run_bundle: Path, record: dict[str, object]) -> None:
    (run_bundle / "result.json").write_text(json.dumps(record), encoding="utf-8")


def test_completed_result_writes_exact_blank_worksheet(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Break caught: changing the fixed worksheet layout or reading undeclared artifacts.
    _, _, run_bundle, output_path = _build_inputs(tmp_path, monkeypatch)

    written_path = write_worksheet(SCENARIO_ARGUMENT, run_bundle, output_path)

    expected = """# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/example/worksheet-case |
| Scenario ID | worksheet-case |
| Scenario purpose |  |
| Run ID | 20260902T120000000Z-worksheet-case-unique |
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
| Fixture | skills/example/SKILL.md | dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd |
| Fixture | sources/input.md | eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/example/worksheet-case/rubric.md | cf8361419e59aa49eb44c738a783611eff741fdf97eeaf94da73a7bcd10054e9 |

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
    assert written_path == output_path.resolve()
    assert output_path.read_bytes() == expected.encode("utf-8")
    assert not output_path.read_bytes().endswith(b"\n\n")


def test_fixture_rows_include_only_files_in_recorded_order(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Break caught: rendering non-file inventory entries or sorting file rows again.
    record, _, run_bundle, output_path = _build_inputs(tmp_path, monkeypatch)
    fixture = record["artifacts"]["fixture"]  # type: ignore[index]
    fixture["entries"] = [  # type: ignore[index]
        {"path": "directory", "type": "directory"},
        {"path": "z-last.md", "type": "file", "sha256": "f" * 64},
        {"path": "link", "type": "symlink"},
        {"path": "a-first.md", "type": "file", "sha256": "0" * 64},
    ]
    _write_record(run_bundle, record)

    write_worksheet(SCENARIO_ARGUMENT, run_bundle, output_path)

    text = output_path.read_text(encoding="utf-8")
    assert "| Fixture | directory |" not in text
    assert "| Fixture | link |" not in text
    assert text.index("| Fixture | z-last.md |") < text.index("| Fixture | a-first.md |")


def test_no_regular_fixture_files_emits_no_fixture_row(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Break caught: emitting a placeholder fixture row for an empty file inventory.
    record, _, run_bundle, output_path = _build_inputs(tmp_path, monkeypatch)
    fixture = record["artifacts"]["fixture"]  # type: ignore[index]
    fixture["entries"] = [  # type: ignore[index]
        {"path": "directory", "type": "directory"},
        {"path": "link", "type": "symlink"},
    ]
    _write_record(run_bundle, record)

    write_worksheet(SCENARIO_ARGUMENT, run_bundle, output_path)

    assert "| Fixture |" not in output_path.read_text(encoding="utf-8")


def test_null_values_render_as_empty_cells_and_duration_uses_str(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Break caught: rendering JSON null text or formatting duration independently.
    record, _, run_bundle, output_path = _build_inputs(tmp_path, monkeypatch)
    artifacts = record["artifacts"]  # type: ignore[assignment]
    artifacts["config"]["sha256"] = None  # type: ignore[index]
    record["duration_seconds"] = 1.25
    _write_record(run_bundle, record)

    write_worksheet(SCENARIO_ARGUMENT, run_bundle, output_path)

    text = output_path.read_text(encoding="utf-8")
    assert "| Configuration | config.json |  |" in text
    assert "| Duration seconds | 1.25 |" in text
    assert "| Error code |  |" in text
    assert "| Error message |  |" in text
    assert "None" not in text


def test_inserted_values_use_the_specified_table_cell_escaping_order(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Break caught: escaping before newline normalization or in the wrong sequence.
    scenario_argument = "scenario\\path|first\r\nsecond\rthird\nfourth/"
    record, _, run_bundle, output_path = _build_inputs(
        tmp_path, monkeypatch, scenario_argument=scenario_argument
    )
    record["infrastructure_error"] = {
        "code": "BAD\\CODE|one\r\ntwo\rthree\nfour",
        "message": "message\\part|one\r\ntwo\rthree\nfour",
    }
    artifacts = record["artifacts"]  # type: ignore[assignment]
    artifacts["config"]["path"] = "retained\\config|one\r\ntwo\rthree\nfour"  # type: ignore[index]
    _write_record(run_bundle, record)

    write_worksheet(scenario_argument, run_bundle, output_path)

    text = output_path.read_text(encoding="utf-8")
    assert (
        "| Scenario path | scenario\\\\path\\|first<br>second<br>third<br>fourth/ |"
        in text
    )
    assert (
        "| Rubric | scenario\\\\path\\|first<br>second<br>third<br>fourth/rubric.md |"
        in text
    )
    assert "| Error code | BAD\\\\CODE\\|one<br>two<br>three<br>four |" in text
    assert (
        "| Error message | message\\\\part\\|one<br>two<br>three<br>four |"
        in text
    )
    assert (
        "| Configuration | retained\\\\config\\|one<br>two<br>three<br>four |"
        in text
    )


@pytest.mark.parametrize(
    "failure",
    (
        "missing scenario",
        "missing rubric",
        "missing run bundle",
        "missing result",
        "malformed result",
        "incomplete result",
    ),
)
def test_invalid_inputs_fail_before_creating_output(
    failure: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Break caught: treating unreadable, malformed, or incomplete input as output failure.
    record, scenario, run_bundle, output_path = _build_inputs(tmp_path, monkeypatch)
    rubric_path = scenario / "rubric.md"
    result_path = run_bundle / "result.json"
    if failure == "missing scenario":
        rubric_path.unlink()
        scenario.rmdir()
    elif failure == "missing rubric":
        rubric_path.unlink()
    elif failure == "missing run bundle":
        result_path.unlink()
        run_bundle.rmdir()
    elif failure == "missing result":
        result_path.unlink()
    elif failure == "malformed result":
        result_path.write_text("{", encoding="utf-8")
    else:
        del record["run_id"]
        _write_record(run_bundle, record)

    with pytest.raises(WorksheetInputError):
        write_worksheet(SCENARIO_ARGUMENT, run_bundle, output_path)

    assert not output_path.exists()


def test_existing_output_is_preserved(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Break caught: opening an existing worksheet non-exclusively or truncating it.
    _, _, run_bundle, output_path = _build_inputs(tmp_path, monkeypatch)
    output_path.write_bytes(b"owner bytes\n")

    with pytest.raises(WorksheetOutputError):
        write_worksheet(SCENARIO_ARGUMENT, run_bundle, output_path)

    assert output_path.read_bytes() == b"owner bytes\n"


def test_missing_output_parent_is_an_output_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Break caught: creating a caller-selected output parent implicitly.
    _, _, run_bundle, output_path = _build_inputs(tmp_path, monkeypatch)
    output_path = output_path.parent / "missing" / output_path.name

    with pytest.raises(WorksheetOutputError):
        write_worksheet(SCENARIO_ARGUMENT, run_bundle, output_path)

    assert not output_path.parent.exists()


def test_selected_output_open_failure_is_an_output_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Break caught: leaking a selected output write failure as a raw OSError.
    _, _, run_bundle, output_path = _build_inputs(tmp_path, monkeypatch)
    original_open = Path.open

    def fail_selected_output(path: Path, *args: object, **kwargs: object):
        if path == output_path:
            raise OSError("selected output rejected")
        return original_open(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", fail_selected_output)

    with pytest.raises(WorksheetOutputError):
        write_worksheet(SCENARIO_ARGUMENT, run_bundle, output_path)

    assert not output_path.exists()
