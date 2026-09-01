"""Provider-free acceptance checks for the adversarial-review catalog."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from skilltest.config import load_config
import skilltest.workspace as workspace_module


SCENARIO_ROOT = (
    Path(__file__).resolve().parents[2] / "scenarios" / "adversarial-review"
)

AR_01_SKILLS = (
    "adversarial-review",
    "adversarial-review-loop",
    "concise-writing",
    "disciplined-development",
    "disciplined-research",
    "dispatching-development-subagents",
    "lean-plan-writing",
    "sweeping-stale-references",
    "writing-explicit-rationale",
)

COMMON_PACKAGED = (
    (
        "fixture/skills/superpowers/requesting-code-review/SKILL.md",
        "skills/superpowers/requesting-code-review/SKILL.md",
        "d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8",
    ),
    (
        "fixture/skills/superpowers/requesting-code-review/code-reviewer.md",
        "skills/superpowers/requesting-code-review/code-reviewer.md",
        "b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3",
    ),
)

AR_14_PACKAGED = (
    (
        "fixture/skills/superpowers/test-driven-development/SKILL.md",
        "skills/superpowers/test-driven-development/SKILL.md",
        "bf1b8216e523851a411e91d429a7c1c2a173e79d88957bc78e348218d50edd54",
    ),
    (
        "fixture/skills/superpowers/using-superpowers/references/codex-tools.md",
        "skills/superpowers/using-superpowers/references/codex-tools.md",
        "d3f113a8ebbd748e8ba847b09b57b7685442775ca4ee194d693ce3663f8fac68",
    ),
    (
        "fixture/skills/superpowers/writing-skills/SKILL.md",
        "skills/superpowers/writing-skills/SKILL.md",
        "d34db5c8aed6a4e0440132bd0613aace70a693ec7819d5637ad77481d8e10d1b",
    ),
    (
        "fixture/skills/superpowers/writing-skills/anthropic-best-practices.md",
        "skills/superpowers/writing-skills/anthropic-best-practices.md",
        "217629b356c09c9bd11017c9788e8fc654ca1b32c92d4a51cd490e16dd65e59a",
    ),
    (
        "fixture/skills/superpowers/writing-skills/examples/CLAUDE_MD_TESTING.md",
        "skills/superpowers/writing-skills/examples/CLAUDE_MD_TESTING.md",
        "0b379a3415e185d3c434b3ad283d8aa132f3022c2a4f210f168865b5986bcef0",
    ),
    (
        "fixture/skills/superpowers/writing-skills/graphviz-conventions.dot",
        "skills/superpowers/writing-skills/graphviz-conventions.dot",
        "e2890a593c91370e384b42f2f67b1a6232c9e69dddea7891a0c1c46d7b20b694",
    ),
    (
        "fixture/skills/superpowers/writing-skills/persuasion-principles.md",
        "skills/superpowers/writing-skills/persuasion-principles.md",
        "a51bc9bf75189ea73a27b3fb504a2fdfdb966fb1f7f1cdf03203230a216ccc03",
    ),
    (
        "fixture/skills/superpowers/writing-skills/render-graphs.js",
        "skills/superpowers/writing-skills/render-graphs.js",
        "ccda971a87bb185f8febf81c56b556a20d026fa980c17b35fa3e8824fbb37852",
    ),
    (
        "fixture/skills/superpowers/writing-skills/testing-skills-with-subagents.md",
        "skills/superpowers/writing-skills/testing-skills-with-subagents.md",
        "c711346852c911b24a84aa161e0cff06a4cd7f4e2fa9e9c0a266cead5afcbade",
    ),
)

CATALOG = {
    "ar-01": {
        "prompt_hash": "a70567cd4c8196340d478d8738de3a244b28df00919cfb643053db4a9ac506f8",
        "live_skills": AR_01_SKILLS,
        "packaged": (
            (
                "fixture/project/CLAUDE.md",
                "project/CLAUDE.md",
                "7f9a434946a09909b3d837588e5dd3f49593dc151959796132487735954f9993",
            ),
            (
                "fixture/project/plans/ratio.md",
                "project/plans/ratio.md",
                "b42252947352d99ecc3994cf157d91746bc6c13e1dfa530d5bfe3b3750dd6424",
            ),
            (
                "fixture/project/src/ratio.py",
                "project/src/ratio.py",
                "2ab9e87f7325f2203a79bdcc5f5d698607c52566e601b3a3db7556287c656ad3",
            ),
        ),
    },
    "ar-02": {
        "prompt_hash": "afe180c4bb8bc0635561fa799ef5ea66a6e807c2edcb19d8d20a5baecd9e7390",
        "packaged": (),
    },
    "ar-03": {
        "prompt_hash": "a32a3269f7e89640a65b041b3f9d1ec5907f7397b032593e9473e59e42518fc8",
        "packaged": (
            (
                "fixture/project/benchmarks/sort.json",
                "project/benchmarks/sort.json",
                "2a3c39905224a730da2182fa14aad68215caf7a536e251f818f751d4c2e4f2ae",
            ),
            (
                "fixture/project/plans/normalize.md",
                "project/plans/normalize.md",
                "963cae0e7dbd0d03ad3dc944d53d79bf5166a029e2ee08ccc8b3e0c7c007ecd1",
            ),
            (
                "fixture/project/src/bulk.py",
                "project/src/bulk.py",
                "1640200ee740a66856d513fc3534ab6b62301f0838a0ebc438499620db2bbab0",
            ),
            (
                "fixture/project/src/normalize.py",
                "project/src/normalize.py",
                "947c4926116f228a4843a7aa213cf46c86c03553315f55735b43b5085998223d",
            ),
            (
                "fixture/project/src/retry.py",
                "project/src/retry.py",
                "424d10fc3e9c4ef274312c2bffe331f60b53ad1d6ed5d873a0d13fb07aa9ff7f",
            ),
            (
                "fixture/project/src/validate.py",
                "project/src/validate.py",
                "020d6e30bd07ed9d44fe122dc0772cdf7080434947be2cc2dc21a878e5dbbbb0",
            ),
        ),
    },
    "ar-04": {
        "prompt_hash": "525112073efaf10c6af7f6eb9fedfe3ce0c6e5c56ba443c27c73244e3b13a016",
        "packaged": (
            (
                "fixture/context/artifacts.md",
                "context/artifacts.md",
                "8b924afe56754ad28ae0fc04e265d8823d73826bea1732514f41e321b5402e1b",
            ),
        ),
    },
    "ar-05": {
        "prompt_hash": "0f62c02acd47bf781d762420897a9a6a14ab7a94026494dfbed71cce9de1be41",
        "packaged": (
            (
                "fixture/subject/plans/2026-06-18-recording-slice.md",
                "subject/plans/2026-06-18-recording-slice.md",
                "1d10c2845101df73f4418c7a4db147a79d53335a6f08f5bec822073e2e180c40",
            ),
            (
                "fixture/subject/swift/Steno/Sources/Steno/Events/EventEnvelope.swift",
                "subject/swift/Steno/Sources/Steno/Events/EventEnvelope.swift",
                "42cd5c2df5a1dadb34df0e15cafa6e36f76588661e1cb99f93f83e158488800b",
            ),
            (
                "fixture/subject/swift/Steno/Sources/Steno/Events/EventLog.swift",
                "subject/swift/Steno/Sources/Steno/Events/EventLog.swift",
                "26b7accda8f8115ef23249243512384413fb198ab702961f65a3103f0f090aa0",
            ),
            (
                "fixture/subject/swift/Steno/Tests/StenoTests/EventLogTests.swift",
                "subject/swift/Steno/Tests/StenoTests/EventLogTests.swift",
                "65134b891cd8ee803c1367518ea7c3b832fca4a862fa411ed848146d656a4b52",
            ),
        ),
    },
    "ar-06": {
        "prompt_hash": "64297e2b5919d9026c259bbdde24e64e929a812e59db10d7bd5cede490afe01b",
        "packaged": (
            (
                "fixture/context/head-change.patch",
                "context/head-change.patch",
                "ba2d42b8dd3c3b1b04a1a81f217f4a215aeae5b68d89ae80f05a3e7c1d21a8df",
            ),
            (
                "fixture/project/plans/import-endpoint.md",
                "project/plans/import-endpoint.md",
                "2c38ef43ecfa7d63efcfdf079a4a81a14503e1002d27ac3f1bac95a255308c2f",
            ),
            (
                "fixture/project/src/api.py",
                "project/src/api.py",
                "43246548de85a93a0c973d9893a3d23d4493e134250d04f5a0574e7a70bfb152",
            ),
            (
                "fixture/project/src/importer.py",
                "project/src/importer.py",
                "6657310fb0eb39c2cf2927be270d6c9204ff62b7743f7e39180e6356e28e1b8e",
            ),
        ),
    },
    "ar-07": {
        "prompt_hash": "7023f5a2cdb2aadc443477d2c934e8ef584cf1e3539b602db607465caad2833f",
        "packaged": (
            (
                "fixture/subject/review-series.patch",
                "subject/review-series.patch",
                "948088882749126f0e351155b6cdf505b530250b88504c0bb4421dcaf21dcdcf",
            ),
        ),
    },
    "ar-08": {
        "prompt_hash": "f2b266a29190821363eb02a2535587498eea852a2cb9fa3173910bb5333be3aa",
        "packaged": (
            (
                "fixture/project/plan.md",
                "project/plan.md",
                "26c7a41a11268983452b04b43120ca7c4fd43789b2a1a5be3bbedeb247e346de",
            ),
            (
                "fixture/project/src/api.py",
                "project/src/api.py",
                "9a55bc5e939aa4b08c159afbd42222c3da4a35ae00a9fe99869dd57738da5a36",
            ),
            (
                "fixture/project/src/errors.py",
                "project/src/errors.py",
                "718d317ee842c189fe538e5b86dae070f7602c1edfc62a00474854ca64344237",
            ),
            (
                "fixture/project/src/file.py",
                "project/src/file.py",
                "b7fa1e6b2ef16a1a53079cf7e4a6431ddd958721182225f6387696d46263e9d0",
            ),
            (
                "fixture/project/src/queue.py",
                "project/src/queue.py",
                "36fffd19621f2bcdc471ea17fba458d88de8755e017921d4bf58f49c6df9256c",
            ),
            (
                "fixture/project/test_happy_path.py",
                "project/test_happy_path.py",
                "c62e8137b9f5cba55feebcb22d73248c037558d5a0e971dca597bc229dcd337a",
            ),
        ),
    },
    "ar-10": {
        "prompt_hash": "bebc32961df677d4a15b45d5d87201e43b5ae60b4a16362495a9e5de3cff9baa",
        "packaged": (
            (
                "fixture/project/brief.md",
                "project/brief.md",
                "784fef67760ffc9bca3245bffed2665f751ebeba71fa604297acebe112412c54",
            ),
            (
                "fixture/project/proposal.md",
                "project/proposal.md",
                "df3d4a609e7d879b1b0b083eb246e060b9ad4dd00d76fb3b7646885ba47dc943",
            ),
        ),
    },
    "ar-12": {
        "prompt_hash": "4f268b13214207496769286295cec06d7ab0925b72c9b52195b26d9c12bc2a6a",
        "packaged": (
            (
                "fixture/project/brief.md",
                "project/brief.md",
                "0ee6c05cbe47371847150bd6c497e52c45eddee35602d1f6ef5321a085ed4db7",
            ),
            (
                "fixture/project/proposal.md",
                "project/proposal.md",
                "2981b6228802eaa93ee1bf2f78373e2634ab8eb4a2cf07997c119bbaea5f5146",
            ),
        ),
    },
    "ar-13": {
        "prompt_hash": "76e00b195de7e65f0a9039d7a8fbde578fea9e58ae28764fccbcfc2ffa2dcb38",
        "packaged": (
            (
                "fixture/project/incidents.md",
                "project/incidents.md",
                "5a9a9d85342ba751c28f63e297c66931c84065f080053d67699d90fbea0855a6",
            ),
            (
                "fixture/project/plan.md",
                "project/plan.md",
                "3a500c601edc5c76c0658b89f4b36d632a416226a12e0a9c5f200dc691f5dd8c",
            ),
            (
                "fixture/project/src/audit.py",
                "project/src/audit.py",
                "9188c4991ce34c96388ada0eec7a57ba966309435167ee1571819158a5c446e6",
            ),
            (
                "fixture/project/src/ratio.py",
                "project/src/ratio.py",
                "2ab9e87f7325f2203a79bdcc5f5d698607c52566e601b3a3db7556287c656ad3",
            ),
        ),
    },
    "ar-14": {
        "prompt_hash": "02531c56c34ec74e7148730ab81388aba27cbc4d7a68d4a8577d8ac9c83c3539",
        "packaged": (
            (
                "fixture/project/SKILL.md",
                "project/SKILL.md",
                "2a51181ec6e1f7f990bcd04e78f2459a88922ceaa121446c1e1b9696966c061b",
            ),
        ),
    },
    "ar-15": {
        "prompt_hash": "7864f44d15beef43df08bea1fab53586ea634a9c5eda2576c06453a539accc28",
        "packaged": (
            (
                "fixture/project/approval-evidence.md",
                "project/approval-evidence.md",
                "4e0b97116bb4dcd2e0f406e8bd43da561b267de29ebfe5adb5d252fd42c540b2",
            ),
            (
                "fixture/project/change-request.md",
                "project/change-request.md",
                "40ec5077bd654fdae4d82fe5321ce157d23da86228f2eb186d813fd8a83266e4",
            ),
            (
                "fixture/project/decision-record.md",
                "project/decision-record.md",
                "b26aef2a0076d52c7578ae442a0afa5d863b20ffae5371fa7d87f6c487e630d6",
            ),
            (
                "fixture/project/interface-contract.md",
                "project/interface-contract.md",
                "9996f1267cd295f7331866bfb03461bbe8a73b35b13405476154f9410e5857f1",
            ),
            (
                "fixture/project/proposal.md",
                "project/proposal.md",
                "bf8b784fdf97b333d976872b134f3881b527f706b4efc7f75f66742538ea9698",
            ),
            (
                "fixture/project/support-evidence.md",
                "project/support-evidence.md",
                "504c72f8798cf1957fe98e442aa197599ca46f9702f44f2fd04c82d1faedf626",
            ),
        ),
    },
    "ar-16": {
        "prompt_hash": "1513a66015109f998e8ca2bd5c0f92aa1b09f9791ec9b40abd87b71dc18d9c17",
        "packaged": (
            (
                "fixture/project/EventLog.swift",
                "project/EventLog.swift",
                "025c48a43595883ae06929affaccddd57f9df2b45f5fa56e409ac61c99cd9e09",
            ),
            (
                "fixture/project/contract.md",
                "project/contract.md",
                "c5d2479b1b24c120da384a16afb12d8628fd8fec93c9c626f91fc24049949202",
            ),
        ),
    },
    "ar-17": {
        "prompt_hash": "1513a66015109f998e8ca2bd5c0f92aa1b09f9791ec9b40abd87b71dc18d9c17",
        "packaged": (
            (
                "fixture/project/EventLog.swift",
                "project/EventLog.swift",
                "f1eda7207c1241654507072d3906db8a03947ecd65e155b4ad7591968638d41a",
            ),
            (
                "fixture/project/contract.md",
                "project/contract.md",
                "2557208d3e59c3d25e8dc914911fb73ce3b5beb7d55d43879fcc7e4ad0270a0f",
            ),
        ),
    },
}


def _packaged(scenario_id: str) -> tuple[tuple[str, str, str], ...]:
    ar_14 = AR_14_PACKAGED if scenario_id == "ar-14" else ()
    return COMMON_PACKAGED + ar_14 + CATALOG[scenario_id]["packaged"]


def _package_files(scenario_dir: Path) -> set[str]:
    return {
        path.relative_to(scenario_dir).as_posix()
        for path in scenario_dir.rglob("*")
        if path.is_file()
    }


def _expected_files(scenario_id: str) -> set[str]:
    return {"README.md", "prompt.md", "rubric.md", "test.json"} | {
        source for source, _, _ in _packaged(scenario_id)
    }


def _expected_fixtures(scenario_id: str) -> tuple[tuple[str, str], ...]:
    live_skills = CATALOG[scenario_id].get(
        "live_skills", ("adversarial-review",)
    )
    live = tuple(
        (
            f"../../../../skills/{skill_id}/SKILL.md",
            f"skills/{skill_id}/SKILL.md",
        )
        for skill_id in live_skills
    )
    packaged = tuple(
        (source, target) for source, target, _ in _packaged(scenario_id)
    )
    return live + packaged


def test_adversarial_review_catalog_prepares_only_declared_inputs(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(workspace_module.tempfile, "gettempdir", lambda: str(tmp_path))

    assert SCENARIO_ROOT.is_dir()
    assert {path.name for path in SCENARIO_ROOT.iterdir() if path.is_dir()} == set(
        CATALOG
    )

    for scenario_id, expected in CATALOG.items():
        scenario_dir = SCENARIO_ROOT / scenario_id
        package_files = _package_files(scenario_dir)
        optional_files = {"smoke-result.json"} if scenario_id == "ar-01" else set()
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

        for source, _, expected_hash in _packaged(scenario_id):
            packaged_path = scenario_dir / source
            assert hashlib.sha256(packaged_path.read_bytes()).hexdigest() == expected_hash

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
