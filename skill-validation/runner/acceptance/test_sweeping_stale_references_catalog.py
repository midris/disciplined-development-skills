"""Provider-free acceptance checks for the sweeping-stale-references catalog."""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from skilltest.config import load_config
import skilltest.workspace as workspace_module


SCENARIO_ROOT = (
    Path(__file__).resolve().parents[2]
    / "scenarios"
    / "sweeping-stale-references"
)

NINE_SKILLS = (
    "adversarial-review-loop",
    "adversarial-review",
    "concise-writing",
    "disciplined-development",
    "disciplined-research",
    "dispatching-development-subagents",
    "lean-plan-writing",
    "sweeping-stale-references",
    "writing-explicit-rationale",
)

LIVE_SKILLS = {
    "ssr-01": NINE_SKILLS,
    "ssr-02": ("sweeping-stale-references",),
    "ssr-03": ("sweeping-stale-references",),
    "ssr-05": ("sweeping-stale-references",),
    "ssr-06": NINE_SKILLS,
    "ssr-07": NINE_SKILLS,
}

CATALOG = {
    "ssr-01": {
        "prompt_hash": "b87520036c0f72d5eadeb9d43f1cc50ed2ff144f604e5ca7b9277f1fb51390c3",
        "files": {
            "README.md",
            "fixture/project/docs/session-policy.md",
            "fixture/project/src/session.py",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            (
                "fixture/project/src/session.py",
                "project/src/session.py",
                "a975fc6bef67344143832d89a6b24b12a8b59da4682236c842f8639eb9378cd2",
            ),
            (
                "fixture/project/docs/session-policy.md",
                "project/docs/session-policy.md",
                "a925897761b094ba37bf8f7825ceab7fac62a48beeea310dbb5f412ef74d1d0c",
            ),
        ),
    },
    "ssr-02": {
        "prompt_hash": "a6113dc283c5dd61c79698f96d4d0a5a09a327619c64969e4bd25178975be93d",
        "files": {
            "README.md",
            "fixture/context/match-inventory.md",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            (
                "fixture/context/match-inventory.md",
                "context/match-inventory.md",
                "43b3f8819da7b85ccff406f64a4d0c438ebc4cea35e5628ac4e0919a64e7dcf6",
            ),
        ),
    },
    "ssr-03": {
        "prompt_hash": "5e1a1fa2f60db6cf2aeceaed4a85b869366e4e6a8b20cfe8bf0e4398de46f39e",
        "files": {
            "README.md",
            "fixture/context/grouping-inventory.md",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            (
                "fixture/context/grouping-inventory.md",
                "context/grouping-inventory.md",
                "0916a116c5d0d98089b000a65bcfe1b73ec26951b4659b6279e7f6df0c1e1b02",
            ),
        ),
    },
    "ssr-05": {
        "prompt_hash": "8d9f3a242802100fbe7ded2b7ace37f0647030502c9b5c3dd0b1efd9c268477c",
        "files": {
            "README.md",
            "fixture/context/single-file-search.md",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            (
                "fixture/context/single-file-search.md",
                "context/single-file-search.md",
                "48f863afc5e164a3d74f19271656f98f88e00c87c48d10d6995318a7aaece85f",
            ),
        ),
    },
    "ssr-06": {
        "prompt_hash": "a39d26e62ad7ec6070e51655b0282ac8072547349f12ae39e0642f541dc1c401",
        "files": {
            "README.md",
            "fixture/project/docs/session-policy.md",
            "fixture/project/src/session.py",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            (
                "fixture/project/src/session.py",
                "project/src/session.py",
                "a975fc6bef67344143832d89a6b24b12a8b59da4682236c842f8639eb9378cd2",
            ),
            (
                "fixture/project/docs/session-policy.md",
                "project/docs/session-policy.md",
                "a925897761b094ba37bf8f7825ceab7fac62a48beeea310dbb5f412ef74d1d0c",
            ),
        ),
    },
    "ssr-07": {
        "prompt_hash": "86a40957dad5091eac5f650ad44f8a71ab85aa318038f77e982952fa7294187f",
        "files": {
            "README.md",
            "fixture/project/docs/session-policy.md",
            "fixture/project/src/session.py",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            (
                "fixture/project/src/session.py",
                "project/src/session.py",
                "a975fc6bef67344143832d89a6b24b12a8b59da4682236c842f8639eb9378cd2",
            ),
            (
                "fixture/project/docs/session-policy.md",
                "project/docs/session-policy.md",
                "a925897761b094ba37bf8f7825ceab7fac62a48beeea310dbb5f412ef74d1d0c",
            ),
        ),
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


def test_sweeping_stale_references_catalog_prepares_only_declared_inputs(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(workspace_module.tempfile, "gettempdir", lambda: str(tmp_path))

    assert {path.name for path in SCENARIO_ROOT.iterdir() if path.is_dir()} == set(CATALOG)

    for scenario_id, expected in CATALOG.items():
        scenario_dir = SCENARIO_ROOT / scenario_id
        package_files = _package_files(scenario_dir)
        optional_files = {"smoke-result.json"} if scenario_id == "ssr-01" else set()
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
