"""Provider-free acceptance checks for the disciplined-research catalog."""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from skilltest.config import load_config
import skilltest.workspace as workspace_module


SCENARIO_ROOT = (
    Path(__file__).resolve().parents[2]
    / "scenarios"
    / "disciplined-research"
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
    "dr-01": NINE_SKILLS,
    "dr-02": ("disciplined-research",),
    "dr-03": ("disciplined-research",),
    "dr-04": ("disciplined-research",),
    "dr-05": ("disciplined-research",),
    "dr-06": ("disciplined-research",),
    "dr-07": ("disciplined-research",),
}

CATALOG = {
    "dr-01": {
        "prompt_hash": "b011d522027b31696e4e6db6c3dfb61e59b5886f6c0ba153a3eca75d0ff0f644",
        "files": {
            "README.md",
            "fixture/project/README.md",
            "fixture/project/app/retention.py",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            (
                "fixture/project/app/retention.py",
                "project/app/retention.py",
                "900dd0268a517c797023f907ce3a14b6f66bc04b9c27787a153cd471dea6bec8",
            ),
            (
                "fixture/project/README.md",
                "project/README.md",
                "49061feab313293d6a1b8f23cae43056c79eeee88a00745a741595f98d54f1db",
            ),
        ),
    },
    "dr-02": {
        "prompt_hash": "74dc6208dc12771c5754b8293efff7a632a11f2ad4a3082887e80d3dfb36faf0",
        "files": {
            "README.md",
            "fixture/sources/city-museum-addendum-2.md",
            "fixture/sources/city-museum-rfp.md",
            "fixture/sources/friends-newsletter.md",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            (
                "fixture/sources/city-museum-rfp.md",
                "sources/city-museum-rfp.md",
                "5b50cf2558ef9a73335487198f2fd44a30339df58741df312374e169951340ca",
            ),
            (
                "fixture/sources/city-museum-addendum-2.md",
                "sources/city-museum-addendum-2.md",
                "a882f3e3753ca78357333238e5f808d65d251852df04e0506bf2582940bec64f",
            ),
            (
                "fixture/sources/friends-newsletter.md",
                "sources/friends-newsletter.md",
                "a8746ab03403c6143e8f65d0e249436b5bb8341c2ebe4c953eb21797787fad5f",
            ),
        ),
    },
    "dr-03": {
        "prompt_hash": "4a2ecdc36d1b647bfeac840c054c880958a0331457979cf416fe533348e7ec10",
        "files": {
            "README.md",
            "fixture/project/package.json",
            "fixture/sources/orbital-maintainer-blog.md",
            "fixture/sources/orbital-release-notes.md",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            (
                "fixture/project/package.json",
                "project/package.json",
                "1c2bb8f53dce6c7a90c2411d53f177dbfcba8ace56861399dd4f55412e0fb262",
            ),
            (
                "fixture/sources/orbital-release-notes.md",
                "sources/orbital-release-notes.md",
                "1592db31a0848116b082b2093704d80847f672b540633c00b0ea6c30ad03c3f4",
            ),
            (
                "fixture/sources/orbital-maintainer-blog.md",
                "sources/orbital-maintainer-blog.md",
                "3f6e47ed632fde9a22f94ec764ca2c98b5365a9db6190566e8efb29234347488",
            ),
        ),
    },
    "dr-04": {
        "prompt_hash": "73c675097aa4ef75a17f4ed7fcb9f56042f0a5bd374660c26217f28828fb84d7",
        "files": {
            "README.md",
            "fixture/project/payments/retry_policy.py",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            (
                "fixture/project/payments/retry_policy.py",
                "project/payments/retry_policy.py",
                "a7099716223bf4a0c67fc32bda4c6816e6743be3e72aff5f52f3acc953f9a9c4",
            ),
        ),
    },
    "dr-05": {
        "prompt_hash": "25c63ad6fa002e671aa631ff96b52f2302f9bb58885cf2f918c4f89334aaf791",
        "files": {
            "README.md",
            "fixture/sources/nimbus-support-matrix.md",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            (
                "fixture/sources/nimbus-support-matrix.md",
                "sources/nimbus-support-matrix.md",
                "0abe5b18aaa9a6315fa982dba406a8bb6255dd9652674956426fb34fbd4c5843",
            ),
        ),
    },
    "dr-06": {
        "prompt_hash": "14c9968aae4616b3e19105d82e53b4b2a000bb7bb21027a5d8292705a409b1c2",
        "files": {
            "README.md",
            "fixture/project/upload-403/evidence-index.md",
            "fixture/project/upload-403/runtime-config.json",
            "fixture/project/upload-403/worker.log",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            (
                "fixture/project/upload-403/evidence-index.md",
                "project/upload-403/evidence-index.md",
                "5ce87478b5f41f46f10dbba5b329f6eae004ca9b4a6895a495fa75ec292bfb46",
            ),
            (
                "fixture/project/upload-403/runtime-config.json",
                "project/upload-403/runtime-config.json",
                "4ec39350c64e94229c7aaa59a719afc1c18c2c673d7d5215a8be38ee5307af13",
            ),
            (
                "fixture/project/upload-403/worker.log",
                "project/upload-403/worker.log",
                "d381395b47ed8fb03ca12fc8c1ab9a1c17299d28149d591119319705aed39eba",
            ),
        ),
    },
    "dr-07": {
        "prompt_hash": "0a73303a85788bf3a23942d6be800a5f6162bc45526e14d05c7253c1482f6b0f",
        "files": {
            "README.md",
            "fixture/sources/north-annex-hours.md",
            "prompt.md",
            "rubric.md",
            "test.json",
        },
        "packaged": (
            (
                "fixture/sources/north-annex-hours.md",
                "sources/north-annex-hours.md",
                "876d614b194ace2d807a947223565f3fdc9a597be45c6c1b753a9252a65e45da",
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


def test_disciplined_research_catalog_prepares_only_declared_inputs(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(workspace_module.tempfile, "gettempdir", lambda: str(tmp_path))

    assert {path.name for path in SCENARIO_ROOT.iterdir() if path.is_dir()} == set(CATALOG)

    for scenario_id, expected in CATALOG.items():
        scenario_dir = SCENARIO_ROOT / scenario_id
        package_files = _package_files(scenario_dir)
        optional_files = {"smoke-result.json"} if scenario_id == "dr-01" else set()
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
