"""Render one fixed, unscored skill-test worksheet."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


class WorksheetInputError(Exception):
    """The declared worksheet inputs cannot produce the fixed sheet."""


class WorksheetOutputError(Exception):
    """The completed worksheet text cannot be written as requested."""


def _cell(value: str | None) -> str:
    if value is None:
        return ""
    return (
        value.replace("\r\n", "\n")
        .replace("\r", "\n")
        .replace("\\", "\\\\")
        .replace("|", "\\|")
        .replace("\n", "<br>")
    )


def _render(scenario_argument: str, rubric_digest: str, record: dict[str, object]) -> str:
    test = record["test"]
    execution = record["execution"]
    artifacts = record["artifacts"]
    infrastructure_error = record["infrastructure_error"]
    error_code = None if infrastructure_error is None else infrastructure_error["code"]
    error_message = None if infrastructure_error is None else infrastructure_error["message"]
    rubric_path = f"{scenario_argument}{'' if scenario_argument.endswith('/') else '/'}rubric.md"

    lines = [
        "# Skill Test Worksheet",
        "",
        "## Run identity",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Scenario path | {_cell(scenario_argument)} |",
        f"| Scenario ID | {_cell(test['id'])} |",
        "| Scenario purpose |  |",
        f"| Run ID | {_cell(record['run_id'])} |",
        f"| Provider | {_cell(execution['provider'])} |",
        f"| Model | {_cell(execution['model'])} |",
        f"| Effort | {_cell(execution['effort'])} |",
        f"| Started | {_cell(record['started_at'])} |",
        f"| Finished | {_cell(record['finished_at'])} |",
        f"| Duration seconds | {_cell(str(record['duration_seconds']))} |",
        "",
        "## Infrastructure",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Status | {_cell(record['status'])} |",
        f"| Error code | {_cell(error_code)} |",
        f"| Error message | {_cell(error_message)} |",
        "",
        "## Executed inputs",
        "",
        "| Kind | Path | SHA-256 |",
        "|---|---|---|",
        f"| Configuration | {_cell(artifacts['config']['path'])} | {_cell(artifacts['config']['sha256'])} |",
        f"| Prompt template | {_cell(artifacts['prompt_template']['path'])} | {_cell(artifacts['prompt_template']['sha256'])} |",
        f"| Rendered prompt | {_cell(artifacts['prompt']['path'])} | {_cell(artifacts['prompt']['sha256'])} |",
    ]
    lines.extend(
        f"| Fixture | {_cell(entry['path'])} | {_cell(entry['sha256'])} |"
        for entry in artifacts["fixture"]["entries"]
        if entry["type"] == "file"
    )
    lines.extend(
        [
            "",
            "## Withheld evaluation input",
            "",
            "| Kind | Path | SHA-256 |",
            "|---|---|---|",
            f"| Rubric | {_cell(rubric_path)} | {rubric_digest} |",
            "",
            "## Semantic behavior",
            "",
            "| Invariant | Criterion | Score | Evidence | Notes |",
            "|---|---|---|---|---|",
            "|  |  |  |  |  |",
            "",
            "## Deterministic protocol",
            "",
            "| Requirement | Score | Evidence | Notes |",
            "|---|---|---|---|",
            "|  |  |  |  |",
            "",
            "## Task fidelity",
            "",
            "| Requirement | Score | Evidence | Notes |",
            "|---|---|---|---|",
            "|  |  |  |  |",
            "",
            "## Readability",
            "",
            "| Observation | Evidence |",
            "|---|---|",
            "|  |  |",
            "",
            "## Verdict",
            "",
            "| Field | Value |",
            "|---|---|",
            "| Overall verdict |  |",
            "| Rationale |  |",
            "| Disposition |  |",
            "",
            "## Methodology notes",
            "",
            "| Field | Value |",
            "|---|---|",
            "| Ambiguities |  |",
            "| Scenario defects |  |",
            "| Proposed methodology changes |  |",
        ]
    )
    return "\n".join(lines) + "\n"


def write_worksheet(
    scenario_argument: str,
    run_bundle: Path,
    output_path: Path,
) -> Path:
    """Render one blank worksheet, write it exclusively, and return its resolved path."""
    try:
        rubric_bytes = (Path(scenario_argument) / "rubric.md").read_bytes()
        result_text = (run_bundle / "result.json").read_text(encoding="utf-8")
        record = json.loads(result_text)
        rubric_digest = hashlib.sha256(rubric_bytes).hexdigest()
        worksheet = _render(scenario_argument, rubric_digest, record)
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError) as error:
        raise WorksheetInputError(f"worksheet input failed: {error}") from error

    try:
        with output_path.open("x", encoding="utf-8", newline="\n") as output_file:
            output_file.write(worksheet)
    except (OSError, UnicodeError) as error:
        raise WorksheetOutputError(f"worksheet output failed: {error}") from error
    return output_path.resolve()
