"""Provider-free acceptance checks for the dispatching-development-subagents catalog."""

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
    / "dispatching-development-subagents"
)

DISPATCH = (
    "../../../../skills/dispatching-development-subagents/SKILL.md",
    "skills/dispatching-development-subagents/SKILL.md",
)
REVIEW_LOOP = (
    "../../../../skills/adversarial-review-loop/SKILL.md",
    "skills/adversarial-review-loop/SKILL.md",
)
REVIEW = (
    "../../../../skills/adversarial-review/SKILL.md",
    "skills/adversarial-review/SKILL.md",
)
CONCISE = (
    "../../../../skills/concise-writing/SKILL.md",
    "skills/concise-writing/SKILL.md",
)
PARENT = (
    "../../../../skills/disciplined-development/SKILL.md",
    "skills/disciplined-development/SKILL.md",
)
HOOK = (
    "../../../../skills/disciplined-development/hooks/review_nudge.py",
    "skills/disciplined-development/hooks/review_nudge.py",
)
RESEARCH = (
    "../../../../skills/disciplined-research/SKILL.md",
    "skills/disciplined-research/SKILL.md",
)
LEAN_PLAN = (
    "../../../../skills/lean-plan-writing/SKILL.md",
    "skills/lean-plan-writing/SKILL.md",
)
SWEEP = (
    "../../../../skills/sweeping-stale-references/SKILL.md",
    "skills/sweeping-stale-references/SKILL.md",
)
RATIONALE = (
    "../../../../skills/writing-explicit-rationale/SKILL.md",
    "skills/writing-explicit-rationale/SKILL.md",
)

P01_FILES = (
    (
        "fixture/project/dsd-01/AGENTS.md",
        "project/dsd-01/AGENTS.md",
        "567ded3276c9ecaabbfea7f34229a528652476cf2cfe1f7a81573b4577c866fe",
    ),
    (
        "fixture/project/dsd-01/plans/pagination.md",
        "project/dsd-01/plans/pagination.md",
        "e18ce80cae7233db26ed903116fee411162433d2ef82cfbcfa574835efcf35c4",
    ),
    (
        "fixture/project/dsd-01/reviews/pagination.md",
        "project/dsd-01/reviews/pagination.md",
        "884e1ee1a6c7109134144ff3ab1cddf6bd9bd522a249373e4ce7e1571b77a80a",
    ),
)

P05_FILES = (
    (
        "fixture/project/dsd-05/landed-prose.md",
        "project/dsd-05/landed-prose.md",
        "dc1c4a0881580f5a883d126ddcbc00b70dfd3e226129e44aa6ed06381fbc4aae",
    ),
    (
        "fixture/project/dsd-05/research-report.md",
        "project/dsd-05/research-report.md",
        "0d7d31036a68767b0a586b7aad0c228999316c6463dfd39009f8d7e7131360d5",
    ),
    (
        "fixture/project/dsd-05/returned-handoff.md",
        "project/dsd-05/returned-handoff.md",
        "1c9f3979e4a123c584f3ddd072f6869df6a241adca1c4da4cc484b8f6815ecab",
    ),
    (
        "fixture/project/dsd-05/src/request_config.py",
        "project/dsd-05/src/request_config.py",
        "f0ff7ba51f0b758aea2f9b248c754f832dd57c6d2110036a80f886690ecdee6c",
    ),
    (
        "fixture/project/dsd-05/test-output.txt",
        "project/dsd-05/test-output.txt",
        "dbff34df084976e0006cd15b2bd1cf6e3b5419b626c19f0030544a1c174ec3d7",
    ),
)

UPSTREAM = (
    (
        "fixture/skills/superpowers/subagent-driven-development/SKILL.md",
        "skills/superpowers/subagent-driven-development/SKILL.md",
        "8dd1b8e698edec3700c6d89517dbe96febd3bacd3f6ea21c1a3569c62ea104b5",
    ),
)

CATALOG = {
    "dsd-01": {
        "prompt_hash": "6eedfdb6b17fce5af790c0fe9cd7dc967426ea6f911c4086a9ed1ade718bce09",
        "live": (
            DISPATCH,
            REVIEW_LOOP,
            REVIEW,
            CONCISE,
            PARENT,
            RESEARCH,
            LEAN_PLAN,
            SWEEP,
            RATIONALE,
        ),
        "packaged": P01_FILES,
    },
    "dsd-02": {
        "prompt_hash": "d4c03e13a68a7c25a480d07dfb075e7b23d2bbda79d330ce00a3d52b92054cca",
        "live": (DISPATCH, PARENT, HOOK, RESEARCH),
        "packaged": UPSTREAM,
    },
    "dsd-03": {
        "prompt_hash": "e0e07f5e26930a58a6741c3f1e3ad900f2bcc362ff4c688ff554b8ccbd040e7b",
        "live": (DISPATCH,),
        "packaged": (),
    },
    "dsd-04": {
        "prompt_hash": "9637da4d3e05acf47034ff063c5e41193ccb0192fc2f31ed6bfbe2705ed8993c",
        "live": (DISPATCH,),
        "packaged": (),
    },
    "dsd-05": {
        "prompt_hash": "4b0f1c15850a20e191dd060396153adf24492d791a67f2cd68aad2e29322f74a",
        "live": (DISPATCH,),
        "packaged": P05_FILES,
    },
    "dsd-06": {
        "prompt_hash": "6a182459ece79f7696e18b43a891b9441c548a992814f9862729ea3bb96f7469",
        "live": (DISPATCH,),
        "packaged": P01_FILES,
    },
    "dsd-07": {
        "prompt_hash": "cd4b9b14c2deea0ea019bd3ce8ed5e85948fbbc97bcdf7f346e794b32106464b",
        "live": (DISPATCH,),
        "packaged": (),
    },
    "dsd-08": {
        "prompt_hash": "43ac03009dd981bcc6633d75d21921fe496fb8d69c57629711a341ac666aae6c",
        "live": (DISPATCH,),
        "packaged": P05_FILES,
    },
    "dsd-09": {
        "prompt_hash": "81beafb72ff9e9e89bdb76a1c9a24b3e1cdf5a26ab84b7ae80c16113749f4b87",
        "live": (DISPATCH, PARENT, HOOK),
        "packaged": UPSTREAM,
    },
    "dsd-10": {
        "prompt_hash": "f56340c6ba819155105644881da386e04ff09f80178bf953d338a1dee06e7a2e",
        "live": (DISPATCH, PARENT, HOOK),
        "packaged": (),
    },
    "dsd-11": {
        "prompt_hash": "2d1ad2701ed71a224e10a4ebdb9aba4ef1c65e8e999212290f06558c055a34a1",
        "live": (DISPATCH, PARENT, HOOK),
        "packaged": UPSTREAM,
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
    expected = CATALOG[scenario_id]
    packaged = tuple(
        (source, target) for source, target, _ in expected["packaged"]
    )
    return expected["live"] + packaged


def test_dispatching_development_subagents_catalog_prepares_only_declared_inputs(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(workspace_module.tempfile, "gettempdir", lambda: str(tmp_path))

    assert {path.name for path in SCENARIO_ROOT.iterdir() if path.is_dir()} == set(
        CATALOG
    )

    for scenario_id, expected in CATALOG.items():
        scenario_dir = SCENARIO_ROOT / scenario_id
        package_files = _package_files(scenario_dir)
        optional_files = {"smoke-result.json"} if scenario_id == "dsd-03" else set()
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
            assert (
                hashlib.sha256((scenario_dir / source).read_bytes()).hexdigest()
                == expected_hash
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
