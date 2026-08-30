"""Provider-free acceptance checks for the writing-explicit-rationale catalog."""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from skilltest.config import load_config
import skilltest.workspace as workspace_module


SCENARIO_ROOT = (
    Path(__file__).resolve().parents[2]
    / "scenarios"
    / "writing-explicit-rationale"
)

LIVE_SKILLS = {
    "wer-01": (
        "adversarial-review-loop",
        "adversarial-review",
        "concise-writing",
        "disciplined-development",
        "disciplined-research",
        "dispatching-development-subagents",
        "lean-plan-writing",
        "sweeping-stale-references",
        "writing-explicit-rationale",
    ),
    "wer-02": ("writing-explicit-rationale",),
    "wer-05": ("writing-explicit-rationale",),
    "wer-06": ("writing-explicit-rationale",),
    "wer-07": (
        "disciplined-development",
        "disciplined-research",
        "lean-plan-writing",
        "writing-explicit-rationale",
    ),
    "wer-08": ("writing-explicit-rationale",),
}

CATALOG = {
    "wer-01": {
        "prompt_hash": "1f6ea36007f027fef44dc12d60f1f33dff7fbde4b2cbd283f5e2399f8e6adf30",
        "files": {"README.md", "prompt.md", "rubric.md", "test.json"},
        "packaged": (),
    },
    "wer-02": {
        "prompt_hash": "743d95a448c6cd7d1a5cef4e839f6482ec989b7ebe219bdc9b0a360a696dd2a9",
        "files": {"README.md", "prompt.md", "rubric.md", "test.json"},
        "packaged": (),
    },
    "wer-05": {
        "prompt_hash": "dc35cfaa391e9f802a9b9de8c4fc21058ef61c1399381e26c4d836c0b5c6b01c",
        "files": {
            "README.md",
            "fixture/docs/architecture/ingest.md",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            (
                "fixture/docs/architecture/ingest.md",
                "docs/architecture/ingest.md",
                "5e25960ed19f0e046ecb263282d9244b9a5026695cc16a7ddb08663f422e4f7e",
            ),
        ),
    },
    "wer-06": {
        "prompt_hash": "e7ea734a0db797e828165fac6e45a042094880a4e215d20699f73a6c5b2db205",
        "files": {"README.md", "prompt.md", "rubric.md", "test.json"},
        "packaged": (),
    },
    "wer-07": {
        "prompt_hash": "a8da5c8b16a2c9cefbce2af41d0e1dc436ddac78d49795652f3a2fd45fd7e295",
        "files": {
            "README.md",
            "fixture/project/wer-07/batch_import.py",
            "fixture/project/wer-07/sources/ingest-architecture.md",
            "fixture/project/wer-07/sources/quota-tokens.md",
            "fixture/project/wer-07/sources/telemetry-comparison.md",
            "fixture/skills/writing-plans/SKILL.md",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            (
                "fixture/skills/writing-plans/SKILL.md",
                "skills/writing-plans/SKILL.md",
                "48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2",
            ),
            (
                "fixture/project/wer-07/batch_import.py",
                "project/wer-07/batch_import.py",
                "2fbe0370868be60a4b8a96907c7404c65ae7b969bc5b63cfb0a6b521306beb20",
            ),
            (
                "fixture/project/wer-07/sources/ingest-architecture.md",
                "project/wer-07/sources/ingest-architecture.md",
                "abc91b3248cae99aef1b3baa1418e5ea4eb0d943c99aa3460f75fd6fbec2f46a",
            ),
            (
                "fixture/project/wer-07/sources/quota-tokens.md",
                "project/wer-07/sources/quota-tokens.md",
                "0c06c4c7edc867de42105325eaccf30fb9112a7888a38eb812ec4b03945eeeef",
            ),
            (
                "fixture/project/wer-07/sources/telemetry-comparison.md",
                "project/wer-07/sources/telemetry-comparison.md",
                "34853c94fa465fc5ba2ef01b810419f2b3200b61a03b2111bdb2a150f31ba49a",
            ),
        ),
    },
    "wer-08": {
        "prompt_hash": "0b5c3b220cd085cc01e1c06cab3156e838b8683a33c30034e9a96ed644189260",
        "files": {"README.md", "prompt.md", "rubric.md", "test.json"},
        "packaged": (),
    },
}


def _package_files(scenario_dir: Path) -> set[str]:
    return {
        path.relative_to(scenario_dir).as_posix()
        for path in scenario_dir.rglob("*")
        if path.is_file()
    }


def _expected_fixtures(scenario_id: str, scenario_dir: Path) -> tuple[tuple[Path, Path], ...]:
    live = tuple(
        (
            (scenario_dir / f"../../../../skills/{skill_id}/SKILL.md").resolve(),
            Path(f"skills/{skill_id}/SKILL.md"),
        )
        for skill_id in LIVE_SKILLS[scenario_id]
    )
    packaged = tuple(
        ((scenario_dir / source).resolve(), Path(target))
        for source, target, _ in CATALOG[scenario_id]["packaged"]
    )
    return live + packaged


def test_writing_explicit_rationale_catalog_prepares_only_declared_inputs(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(workspace_module.tempfile, "gettempdir", lambda: str(tmp_path))

    assert {path.name for path in SCENARIO_ROOT.iterdir() if path.is_dir()} == set(CATALOG)

    for scenario_id, expected in CATALOG.items():
        scenario_dir = SCENARIO_ROOT / scenario_id
        package_files = _package_files(scenario_dir)
        optional_files = {"smoke-result.json"} if scenario_id == "wer-07" else set()
        assert expected["files"] <= package_files <= expected["files"] | optional_files

        config = load_config(scenario_dir / "test.json")
        assert tuple((fixture.source, fixture.target) for fixture in config.fixtures) == _expected_fixtures(
            scenario_id, scenario_dir
        )

        prompt_template = config.prompt.read_bytes()
        assert hashlib.sha256(prompt_template).hexdigest() == expected["prompt_hash"]
        rubric_bytes = (scenario_dir / "rubric.md").read_bytes()
        declared_inputs = (config.config_bytes, prompt_template) + tuple(
            fixture.source.read_bytes() for fixture in config.fixtures
        )
        assert all(rubric_bytes not in input_bytes for input_bytes in declared_inputs)

        for source, _, expected_hash in expected["packaged"]:
            assert hashlib.sha256((scenario_dir / source).read_bytes()).hexdigest() == expected_hash

        context = workspace_module.create_run(config)
        prepared = workspace_module.prepare_workspace(context, config)

        assert prepared.prompt_bytes == context.prompt_path.read_bytes()
        assert b"{{fixture_dir}}" not in prepared.prompt_bytes
        assert b"{{workspace_dir}}" not in prepared.prompt_bytes
        assert b"{{evidence_dir}}" not in prepared.prompt_bytes
        assert b"supplied-skills/" not in prepared.prompt_bytes
        prepared_inputs = (prepared.prompt_bytes,) + tuple(
            (context.fixture_dir / fixture.target).read_bytes() for fixture in config.fixtures
        )
        assert all(rubric_bytes not in input_bytes for input_bytes in prepared_inputs)
        assert list(context.evidence_dir.iterdir()) == []
