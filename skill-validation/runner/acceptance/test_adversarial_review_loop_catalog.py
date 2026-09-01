"""Provider-free acceptance checks for the adversarial-review-loop catalog."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from skilltest.config import load_config
import skilltest.workspace as workspace_module


SCENARIO_ROOT = (
    Path(__file__).resolve().parents[2]
    / "scenarios"
    / "adversarial-review-loop"
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
    "cs": ("adversarial-review-loop",),
    "t2": NINE_SKILLS,
    "t3": ("adversarial-review-loop",),
    "t4": ("adversarial-review-loop",),
    "t5": ("adversarial-review-loop",),
    "t6": ("adversarial-review-loop",),
    "t7": ("adversarial-review-loop",),
    "nf": ("adversarial-review-loop",),
    "pw": ("adversarial-review-loop",),
    "xl": ("adversarial-review-loop",),
    "g3a": ("adversarial-review-loop",),
    "g3b": ("adversarial-review-loop",),
    "g3c": ("adversarial-review-loop",),
    "own": (
        "adversarial-review-loop",
        "disciplined-development",
        "disciplined-research",
    ),
    "ce": ("adversarial-review-loop",),
}

PROMPT_HASHES = {
    "cs": "b96f0aaefa668aac0eee5f20201c63ebd8344a9203a6ab5c03585a19b96b1841",
    "t2": "14529087bab8b18168358b86084be236b5c13f2fd5fed696b7031c5f13dab891",
    "t3": "d66f70d475477c6e10da3b681425b0454f50b1c97129fcdb6cb65cf17b0c6a63",
    "t4": "2b6f8429b39b6f20699d765b9b9b0cf66b480d823431e18b9e40b1b8f28760b8",
    "t5": "53c86b99eeacc51312283b1de784cd040bcb3e7cc933fd3ef9a66a141335d457",
    "t6": "f29ea03099bc61394149d31c3688b86961f305542ee529c8020a8e142fcb9c86",
    "t7": "d5b8352823ef6a17c163045ca2c9215bd3260f62aa4faca29ab45cd3347ce1ec",
    "nf": "088ecef309a869161c73eaa5eb0c9ed657e2b21b790b564d02e677eaccff7e02",
    "pw": "9e98ba043948e5b1eb6a53afec816d6903901b0a50e080b905c6e9cb902755ea",
    "xl": "c0dcb63ac3777310c828f1b9da2a4222b5c64d7c4e2dfc9365099e1a0fa91ac1",
    "g3a": "2a084b8833e69c8c149327fc3fa524123bb0de9f91078932ee0b9d6965e9d567",
    "g3b": "648fc438cb4c6b9db6a2e1f17cec02f40d45a8188cbbeb3976d864ec0b5d459b",
    "g3c": "30ac0ea13ae6ef7b48a91358db3ef4407d084e821e5ec1d1e49119463e4791a6",
    "own": "5e6901b8b4a0c2b999876185d99276a6c1c5275132ff762acd36dfe375aab3c2",
    "ce": "81c24bd0af157bffac55bbef325055dbb06e7b3c33fef87e31bdf30845eda69e",
}

OWN_DEPENDENCY = (
    "fixture/skills/superpowers/subagent-driven-development/SKILL.md",
    "skills/superpowers/subagent-driven-development/SKILL.md",
    "8dd1b8e698edec3700c6d89517dbe96febd3bacd3f6ea21c1a3569c62ea104b5",
)


def _package_files(scenario_dir: Path) -> set[str]:
    return {
        path.relative_to(scenario_dir).as_posix()
        for path in scenario_dir.rglob("*")
        if path.is_file()
    }


def _expected_files(scenario_id: str) -> set[str]:
    files = {"README.md", "prompt.md", "rubric.md", "test.json"}
    if scenario_id == "own":
        files.add(OWN_DEPENDENCY[0])
    return files


def _expected_fixtures(scenario_id: str) -> tuple[tuple[str, str], ...]:
    live = tuple(
        (
            f"../../../../skills/{skill_id}/SKILL.md",
            f"skills/{skill_id}/SKILL.md",
        )
        for skill_id in LIVE_SKILLS[scenario_id]
    )
    packaged = (OWN_DEPENDENCY[:2],) if scenario_id == "own" else ()
    return live + packaged


def test_adversarial_review_loop_catalog_prepares_only_declared_inputs(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(workspace_module.tempfile, "gettempdir", lambda: str(tmp_path))

    assert {path.name for path in SCENARIO_ROOT.iterdir() if path.is_dir()} == set(
        PROMPT_HASHES
    )

    for scenario_id, prompt_hash in PROMPT_HASHES.items():
        scenario_dir = SCENARIO_ROOT / scenario_id
        package_files = _package_files(scenario_dir)
        optional_files = {"smoke-result.json"} if scenario_id == "own" else set()
        assert _expected_files(scenario_id) <= package_files <= (
            _expected_files(scenario_id) | optional_files
        )

        config = load_config(scenario_dir / "test.json")
        raw_config = json.loads((scenario_dir / "test.json").read_bytes())
        assert tuple(
            (fixture["source"], fixture["target"])
            for fixture in raw_config["fixtures"]
        ) == _expected_fixtures(scenario_id)

        prompt_template = config.prompt.read_bytes()
        assert hashlib.sha256(prompt_template).hexdigest() == prompt_hash
        rubric_bytes = (scenario_dir / "rubric.md").read_bytes()
        declared_inputs = (prompt_template,) + tuple(
            fixture.source.read_bytes() for fixture in config.fixtures
        )
        assert all(rubric_bytes not in input_bytes for input_bytes in declared_inputs)

        if scenario_id == "own":
            dependency_path = scenario_dir / OWN_DEPENDENCY[0]
            assert hashlib.sha256(dependency_path.read_bytes()).hexdigest() == (
                OWN_DEPENDENCY[2]
            )

        context = workspace_module.create_run(config)
        prepared = workspace_module.prepare_workspace(context, config)

        assert b"{{fixture_dir}}" not in prepared.prompt_bytes
        assert b"{{workspace_dir}}" not in prepared.prompt_bytes
        assert b"{{evidence_dir}}" not in prepared.prompt_bytes
        assert b"supplied-skills/" not in prepared.prompt_bytes
        prepared_inputs = (prepared.prompt_bytes,) + tuple(
            (context.fixture_dir / fixture.target).read_bytes()
            for fixture in config.fixtures
        )
        assert all(rubric_bytes not in input_bytes for input_bytes in prepared_inputs)
        assert list(context.evidence_dir.iterdir()) == []
