"""Provider-free acceptance checks for the lean-plan-writing catalog."""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from skilltest.config import load_config
import skilltest.workspace as workspace_module


SCENARIO_ROOT = (
    Path(__file__).resolve().parents[2]
    / "scenarios"
    / "lean-plan-writing"
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
    "lp-01": NINE_SKILLS,
    "lp-02": ("lean-plan-writing",),
    "lp-03": ("lean-plan-writing",),
    "lp-05": ("lean-plan-writing",),
    "lp-06": ("lean-plan-writing",),
    "lp-07": ("lean-plan-writing",),
    "lp-08": ("lean-plan-writing",),
}

WRITING_PLANS = (
    "fixture/skills/writing-plans/SKILL.md",
    "skills/writing-plans/SKILL.md",
    "48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2",
)

CATALOG = {
    "lp-01": {
        "prompt_hash": "88b82609319594001c6c5737eacef0114930012169b656e4647cb6bb719bfc2d",
        "files": {
            "README.md",
            "fixture/context/task.md",
            "fixture/skills/writing-plans/SKILL.md",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            WRITING_PLANS,
            (
                "fixture/context/task.md",
                "context/task.md",
                "c1de457ec9789a1345c72d3bf638486f5362d582bbb9917949eef8e00de5cabd",
            ),
        ),
    },
    "lp-02": {
        "prompt_hash": "52dc170f02d4d055456982381adba708b7be011ca7896da2a9ebf2a75b8356a3",
        "files": {
            "README.md",
            "fixture/skills/writing-plans/SKILL.md",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (WRITING_PLANS,),
    },
    "lp-03": {
        "prompt_hash": "41a94175c01f78325bce620c6a30ee6f600ed8a8ebd6fce051710cdafc2e00e9",
        "files": {
            "README.md",
            "fixture/skills/writing-plans/SKILL.md",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (WRITING_PLANS,),
    },
    "lp-05": {
        "prompt_hash": "914f8831a62da2c3811895ce0f426c02e7307edc8440e35154dd51768d20417b",
        "files": {
            "README.md",
            "fixture/context/import-brief.md",
            "fixture/skills/writing-plans/SKILL.md",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            WRITING_PLANS,
            (
                "fixture/context/import-brief.md",
                "context/import-brief.md",
                "8789920dd0f54b1804e2a0aab65adfbcc728d525598d1d30a1d13b28c901c128",
            ),
        ),
    },
    "lp-06": {
        "prompt_hash": "e00cf13f429928a48129058a7391e4c5adeb07bce24c494047157e3b2d855902",
        "files": {
            "README.md",
            "fixture/context/digest-brief.md",
            "fixture/skills/writing-plans/SKILL.md",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            WRITING_PLANS,
            (
                "fixture/context/digest-brief.md",
                "context/digest-brief.md",
                "4df040c40f8888fb406265b3643e1c51e1eeaa91ad469d859dec0fd6f92dc792",
            ),
        ),
    },
    "lp-07": {
        "prompt_hash": "4e825ffbe57cb7bb3352bfccbcbe6ba399c2ae37977bc73978da8596bbd1839c",
        "files": {
            "README.md",
            "fixture/context/oversized-spec.md",
            "fixture/skills/writing-plans/SKILL.md",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            WRITING_PLANS,
            (
                "fixture/context/oversized-spec.md",
                "context/oversized-spec.md",
                "e2a2a54472f37e5ad830ec1016f66fe3b280463c5c400a84697b508d22713685",
            ),
        ),
    },
    "lp-08": {
        "prompt_hash": "0eb903aeb088ebacb45dd1d90e6c2364c949a60f6c337f3c8ca35a017f1d6e12",
        "files": {
            "README.md",
            "fixture/context/coupled-spec.md",
            "fixture/skills/writing-plans/SKILL.md",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            WRITING_PLANS,
            (
                "fixture/context/coupled-spec.md",
                "context/coupled-spec.md",
                "05734fbdd024ff4db8404e46b995688ce30da1bacc9efc82b4bbbb5cd5a93ca1",
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


def test_lean_plan_writing_catalog_prepares_only_declared_inputs(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(workspace_module.tempfile, "gettempdir", lambda: str(tmp_path))

    assert {path.name for path in SCENARIO_ROOT.iterdir() if path.is_dir()} == set(CATALOG)

    for scenario_id, expected in CATALOG.items():
        scenario_dir = SCENARIO_ROOT / scenario_id
        package_files = _package_files(scenario_dir)
        optional_files = {"smoke-result.json"} if scenario_id == "lp-01" else set()
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
