"""Provider-free acceptance checks for the disciplined-development catalog."""

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
    / "disciplined-development"
)

LIVE_SKILLS = {
    "dd-01": ("disciplined-development",),
    "dd-02": ("disciplined-development",),
    "dd-03": ("disciplined-development",),
    "dd-04": ("disciplined-development", "disciplined-research"),
    "dd-05": ("disciplined-development",),
    "dd-06": ("disciplined-development",),
    "dd-07": ("disciplined-development",),
    "dd-08": ("disciplined-development",),
    "dd-09": ("disciplined-development",),
}

DD_02_FILES = (
    (
        "fixture/project/dd-02/CLAUDE.md",
        "project/dd-02/CLAUDE.md",
        "cc1f87826147c2799de88f208edbb798b24d6beb955bbadd5295e04fa1514d69",
    ),
    (
        "fixture/project/dd-02/plans/export.md",
        "project/dd-02/plans/export.md",
        "fd6dec456856f4aeb78cd4926a40ddf26c2f86da836e9559e91bff8f4b5d7daa",
    ),
    (
        "fixture/project/dd-02/plans/specs/export.md",
        "project/dd-02/plans/specs/export.md",
        "77a8ad0cfa3ea65b02047968f412712d2b7723e4b943277ffdecfa3fd7ba735e",
    ),
    (
        "fixture/project/dd-02/sources/cli-schema.md",
        "project/dd-02/sources/cli-schema.md",
        "d31a0cf950c631454c0c3bb4e3a732e7e360776f7157cd81aa0921f8be3f42fd",
    ),
    (
        "fixture/project/dd-02/sources/git-history.md",
        "project/dd-02/sources/git-history.md",
        "a870dab35c878752f1b8c38538c08769df1ec21a2575fea0e723e484b7fd42bf",
    ),
    (
        "fixture/project/dd-02/sources/library-api.md",
        "project/dd-02/sources/library-api.md",
        "253fb27d2587dd1ae1da9c6ff96c27a3c6c5c622301c661dc2e2a82a4452e1a4",
    ),
    (
        "fixture/project/dd-02/sources/vendor-schema-status.md",
        "project/dd-02/sources/vendor-schema-status.md",
        "e696074e7b3c344a9e61601013af88036620ad981744cebc8acecca3964dffe5",
    ),
)

CATALOG = {
    "dd-01": {
        "prompt_hash": "e13a4d90df7360f3a8b949e7b7b5208dc22f1a942294271f4de53898ff6bb0a2",
        "packaged": (),
    },
    "dd-02": {
        "prompt_hash": "5455c56e3fdfe2f390240680b2a7b52bb1f2f1af5fd027d3cc7a7b544081b45c",
        "packaged": DD_02_FILES,
    },
    "dd-03": {
        "prompt_hash": "8804abc9cd643a9e54e96c0409d01cda4243ee2226f3abbdcc25ae62d1866680",
        "packaged": (
            (
                "fixture/project/dd-03/sources/accepted-object-contract.md",
                "project/dd-03/sources/accepted-object-contract.md",
                "a7dd65af335e4d25626a543e42d61e78761155906b3cc42ef2c362cf81d8bdb5",
            ),
            (
                "fixture/project/dd-03/sources/parser-capabilities.md",
                "project/dd-03/sources/parser-capabilities.md",
                "717b21cb61d87637ca241791407d9c57594e29c122cd0ef6c35e3476b5c1bee1",
            ),
        ),
    },
    "dd-04": {
        "prompt_hash": "a5e789ac85f39038eb089fbc123221157e2f888807c37a747b23df7bd8140720",
        "packaged": (
            (
                "fixture/project/dd-04/sources/deployment-targets.md",
                "project/dd-04/sources/deployment-targets.md",
                "90e874878dd0380aca4517b53eedb1f58436f6f3500fb2397517716aa15b986d",
            ),
        ),
    },
    "dd-05": {
        "prompt_hash": "892267b05ac96d381ff18f072073c9d73aeb9ce1966cc9dc0c9a0cbb0058d5e7",
        "packaged": DD_02_FILES,
    },
    "dd-06": {
        "prompt_hash": "1f49a903af98ab130aba3b8a189cb1dd08d586e0376e0f08ab6e11a0d811f004",
        "packaged": DD_02_FILES,
    },
    "dd-07": {
        "prompt_hash": "44701c450532a737cb3ff197a7ee80bb81bc98c4e4c43278b6631f84add989fd",
        "packaged": (
            (
                "fixture/project/dd-07/signed-scope.md",
                "project/dd-07/signed-scope.md",
                "c9004c24d44bc4284fef9541ea3ff7912790227f288ac0c722a41df5a868cb25",
            ),
        ),
    },
    "dd-08": {
        "prompt_hash": "69b7fa3d7a2c3793d5e3563396813cef8f7dd6f951c066c17bfb743a5c12e2af",
        "packaged": (
            (
                "fixture/project/dd-08/cli-schema.md",
                "project/dd-08/cli-schema.md",
                "dbfbe479f69212a39d1dc671aca5213fa6aa4e605fb769b1a1391b5d5abc5d05",
            ),
            (
                "fixture/project/dd-08/signed-scope.md",
                "project/dd-08/signed-scope.md",
                "8840eda21e4a8d4ec4771b1d46c7652c36729065075f9f971153d70a83e0a974",
            ),
        ),
    },
    "dd-09": {
        "prompt_hash": "919f41e20c38e7b971480b16b50ca134db41e1f807890076514f9fabb58156ac",
        "packaged": (
            (
                "fixture/project/dd-09/active-plan.md",
                "project/dd-09/active-plan.md",
                "c09b6c4727776e8871af3ac358656dba48b60566899b883527728cc35761199f",
            ),
            (
                "fixture/project/dd-09/git-history.md",
                "project/dd-09/git-history.md",
                "9a29b8528528d47840e0525cc96b4a8e7639875896543efd97ccb35fef03fdff",
            ),
            (
                "fixture/project/dd-09/signed-change-scope.md",
                "project/dd-09/signed-change-scope.md",
                "071f0d9c1d5778f63c475a8c3a7299f5124f92386e648e9f293cf0209f2323ed",
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


def _expected_files(scenario_id: str) -> set[str]:
    return {"README.md", "prompt.md", "rubric.md", "test.json"} | {
        source for source, _, _ in CATALOG[scenario_id]["packaged"]
    }


def _expected_fixtures(scenario_id: str) -> tuple[tuple[str, str], ...]:
    live = tuple(
        (
            f"../../../../skills/{skill_id}/SKILL.md",
            f"skills/{skill_id}/SKILL.md",
        )
        for skill_id in LIVE_SKILLS[scenario_id]
    )
    packaged = tuple(
        (source, target)
        for source, target, _ in CATALOG[scenario_id]["packaged"]
    )
    return live + packaged


def test_disciplined_development_catalog_prepares_only_declared_inputs(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(workspace_module.tempfile, "gettempdir", lambda: str(tmp_path))

    assert {path.name for path in SCENARIO_ROOT.iterdir() if path.is_dir()} == set(CATALOG)

    for scenario_id, expected in CATALOG.items():
        scenario_dir = SCENARIO_ROOT / scenario_id
        package_files = _package_files(scenario_dir)
        optional_files = {"smoke-result.json"} if scenario_id == "dd-04" else set()
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
        assert hashlib.sha256(prompt_template).hexdigest() == expected["prompt_hash"]
        rubric_bytes = (scenario_dir / "rubric.md").read_bytes()
        declared_inputs = (prompt_template,) + tuple(
            fixture.source.read_bytes() for fixture in config.fixtures
        )
        assert all(rubric_bytes not in input_bytes for input_bytes in declared_inputs)

        for source, _, expected_hash in expected["packaged"]:
            assert hashlib.sha256((scenario_dir / source).read_bytes()).hexdigest() == expected_hash

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
