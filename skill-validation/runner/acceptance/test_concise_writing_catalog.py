"""Provider-free acceptance checks for the concise-writing catalog."""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from skilltest.config import load_config
import skilltest.workspace as workspace_module


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
SCENARIO_ROOT = REPOSITORY_ROOT / "skill-validation" / "scenarios" / "concise-writing"
SUPERPOWERS_ROOT = Path(
    "/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills"
)

NINE_SKILLS = (
    "concise-writing",
    "adversarial-review-loop",
    "adversarial-review",
    "disciplined-development",
    "disciplined-research",
    "dispatching-development-subagents",
    "lean-plan-writing",
    "sweeping-stale-references",
    "writing-explicit-rationale",
)

LIVE_SKILLS = {
    "cw-01": ("concise-writing",),
    "cw-02": ("concise-writing",),
    "cw-03": ("concise-writing",),
    "cw-04": ("concise-writing",),
    "cw-05": ("concise-writing",),
    "cw-06": ("concise-writing",),
    "cw-07": NINE_SKILLS,
    "cw-08": ("concise-writing",),
    "cw-09": (),
    "cw-10": ("concise-writing",),
    "cw-11": (),
    "cw-12": ("concise-writing",),
    "cw-13": ("concise-writing",),
    "cw-14": ("concise-writing",),
    "cw-17": ("concise-writing",),
    "cw-18": ("concise-writing",),
    "cw-19": ("concise-writing",),
}

PACKAGE_INPUTS = {
    "desc-review-loop": (
        "fixture/descriptions/adversarial-review-loop.txt",
        "descriptions/adversarial-review-loop.txt",
        "38843f7718501f52116bfd4f95a6640cb16b560851767df540c808a1ed18cefa",
        REPOSITORY_ROOT / "skills/adversarial-review-loop/SKILL.md",
        True,
    ),
    "desc-concise": (
        "fixture/descriptions/concise-writing.txt",
        "descriptions/concise-writing.txt",
        "586a741a9cb28746078ca1b5f7aa570a4e621a5d2cdecac16e31bd6d2c82fd62",
        REPOSITORY_ROOT / "skills/concise-writing/SKILL.md",
        True,
    ),
    "desc-writing": (
        "fixture/descriptions/superpowers-writing-skills.txt",
        "descriptions/superpowers-writing-skills.txt",
        "5504b0825ec458aa8c20e9a55c6a932b36849e261a97aaf98af366e19a937154",
        SUPERPOWERS_ROOT / "writing-skills/SKILL.md",
        True,
    ),
    "writing-skills": (
        "fixture/skills/writing-skills/SKILL.md",
        "skills/writing-skills/SKILL.md",
        "d34db5c8aed6a4e0440132bd0613aace70a693ec7819d5637ad77481d8e10d1b",
        SUPERPOWERS_ROOT / "writing-skills/SKILL.md",
        False,
    ),
    "writing-tests": (
        "fixture/skills/writing-skills/testing-skills-with-subagents.md",
        "skills/writing-skills/testing-skills-with-subagents.md",
        "c711346852c911b24a84aa161e0cff06a4cd7f4e2fa9e9c0a266cead5afcbade",
        SUPERPOWERS_ROOT / "writing-skills/testing-skills-with-subagents.md",
        False,
    ),
    "tdd": (
        "fixture/skills/test-driven-development/SKILL.md",
        "skills/test-driven-development/SKILL.md",
        "bf1b8216e523851a411e91d429a7c1c2a173e79d88957bc78e348218d50edd54",
        SUPERPOWERS_ROOT / "test-driven-development/SKILL.md",
        False,
    ),
}

PACKAGED_LABELS = {
    "cw-01": (),
    "cw-02": (),
    "cw-03": (),
    "cw-04": (),
    "cw-05": (),
    "cw-06": (),
    "cw-07": (),
    "cw-08": (),
    "cw-09": ("desc-review-loop", "desc-concise", "desc-writing"),
    "cw-10": (),
    "cw-11": ("desc-review-loop", "desc-concise", "desc-writing"),
    "cw-12": (),
    "cw-13": ("writing-skills", "writing-tests", "tdd"),
    "cw-14": ("writing-skills", "writing-tests", "tdd"),
    "cw-17": ("desc-review-loop", "desc-concise", "desc-writing"),
    "cw-18": ("desc-review-loop", "desc-concise", "desc-writing"),
    "cw-19": (),
}

PROMPT_HASHES = {
    "cw-01": "cf7b9fdcd21a35856f1c7a038a6fbd21a85af76258fd476910c2b512fed47c46",
    "cw-02": "6c6580ec1557f10443d33ed09a7497cebce72195ee74bb303901d98ef48db58b",
    "cw-03": "55bc07ef88d4c5e0a1e1fd23f12958ad5982d4424caaaf5c8d68bc17528e1067",
    "cw-04": "eb27f4a55d0ad55776f9394a606f5b08eb9be13b97df6ec1070d26faea28f288",
    "cw-05": "05393026ca0f4f79d7b96b57bb657fd6d16d947f3a98f612c0f329d93b80fe2e",
    "cw-06": "ec25b3eeb1e4f165f86cb43c558096ec7291f584d11b771442bf93f9a48edd85",
    "cw-07": "82cd1c8bcce6b726ab9e6d180d94879527c8b80fa304ff66547fa7fc1184faa5",
    "cw-08": "91db2173ab9bb9a8251c3571fdf26bf485e4d527ce92987d89e2c369a5b3b29b",
    "cw-09": "169a425529c0cfb5f0c77bcc99ef63e41244b94b46b068c83d48e491d9c17f16",
    "cw-10": "d89691bec1d5ee09531e65c1e2a5785e409196c118ce9ae76b708627e4852b35",
    "cw-11": "e902d1c5395512c068a77f5fcbb405a23a0cfdcb55ef63887e8c0741acd9312f",
    "cw-12": "f492f92ceb4a00753557f9d7365715694bd56deea9a45d320f48fdf1844cf7b6",
    "cw-13": "192c46c6f4650f42458aa93782f5aebbec422d9aa520e78d8f66adb2050983f7",
    "cw-14": "8ccb4f0d0aa82c2c06d3c861c153e93161e32f4580dd41706273010acd9339d9",
    "cw-17": "041117e026c2b823db8c21beb482f91da91822c4552e03c084be54e912ca180c",
    "cw-18": "b7fb1df8a6a8343004b0f5ccf5460a2abe94a26e058be5fb3ab3c6344a597376",
    "cw-19": "df33a3add2dc4ad6445076a381e35be307c35fdfbc50426fd0db4072a10b26b3",
}


def _package_files(scenario_dir: Path) -> set[str]:
    return {
        path.relative_to(scenario_dir).as_posix()
        for path in scenario_dir.rglob("*")
        if path.is_file()
    }


def _description_bytes(skill_path: Path) -> bytes:
    for line in skill_path.read_bytes().splitlines():
        if line.startswith(b"description: "):
            description = line.removeprefix(b"description: ")
            if description.startswith(b"'") and description.endswith(b"'"):
                description = description[1:-1]
            return description + b"\n"
    raise AssertionError(f"missing description in {skill_path}")


def _expected_fixtures(
    scenario_id: str, scenario_dir: Path
) -> tuple[tuple[Path, Path], ...]:
    live = tuple(
        (
            (scenario_dir / f"../../../../skills/{skill_id}/SKILL.md").resolve(),
            Path(f"skills/{skill_id}/SKILL.md"),
        )
        for skill_id in LIVE_SKILLS[scenario_id]
    )
    packaged = tuple(
        (
            (scenario_dir / PACKAGE_INPUTS[label][0]).resolve(),
            Path(PACKAGE_INPUTS[label][1]),
        )
        for label in PACKAGED_LABELS[scenario_id]
    )
    if scenario_id in {"cw-17", "cw-18"}:
        return packaged + live
    return live + packaged


def test_concise_writing_catalog_prepares_only_declared_inputs(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(workspace_module.tempfile, "gettempdir", lambda: str(tmp_path))

    assert {path.name for path in SCENARIO_ROOT.iterdir() if path.is_dir()} == set(
        PROMPT_HASHES
    )

    for scenario_id, prompt_hash in PROMPT_HASHES.items():
        scenario_dir = SCENARIO_ROOT / scenario_id
        expected_files = {"README.md", "prompt.md", "rubric.md", "test.json"} | {
            PACKAGE_INPUTS[label][0] for label in PACKAGED_LABELS[scenario_id]
        }
        package_files = _package_files(scenario_dir)
        optional_files = {"smoke-result.json"} if scenario_id == "cw-09" else set()
        assert expected_files <= package_files <= expected_files | optional_files

        config = load_config(scenario_dir / "test.json")
        assert tuple(
            (fixture.source, fixture.target) for fixture in config.fixtures
        ) == _expected_fixtures(scenario_id, scenario_dir)

        prompt_template = config.prompt.read_bytes()
        assert hashlib.sha256(prompt_template).hexdigest() == prompt_hash
        rubric_bytes = (scenario_dir / "rubric.md").read_bytes()
        declared_inputs = (config.config_bytes, prompt_template) + tuple(
            fixture.source.read_bytes() for fixture in config.fixtures
        )
        assert all(rubric_bytes not in input_bytes for input_bytes in declared_inputs)

        for label in PACKAGED_LABELS[scenario_id]:
            source, _, expected_hash, origin, is_description = PACKAGE_INPUTS[label]
            source_bytes = (scenario_dir / source).read_bytes()
            expected_bytes = (
                _description_bytes(origin) if is_description else origin.read_bytes()
            )
            assert source_bytes == expected_bytes
            assert hashlib.sha256(source_bytes).hexdigest() == expected_hash

        context = workspace_module.create_run(config)
        prepared = workspace_module.prepare_workspace(context, config)

        assert prepared.prompt_bytes == context.prompt_path.read_bytes()
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
