"""Provider-free acceptance checks for the skill-discovery catalog."""

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
    / "skill-discovery"
)

PROMPT_HASHES = {
    "disc-01": "2f175787e2a45f998f44fbe4f13d3801425e82cca26537f504bac820dba60012",
    "disc-02": "16506525e0f9ec43e2d5099aa411564492880a9ed8c5230c1407a20be7bc7682",
    "disc-03": "dfa7e97c41e92c4583ae3efe9e79160eef984518f94e7bee09a75d59c786348c",
    "disc-04": "aa9f3db4df0f178be34092c8b9b8d5968f73966f0aba9f0eb9d92c7502e56560",
    "disc-05": "d5c5f4be0b5c646b7a6f93785a013fc0d23b104e296eca6e1edcc4287f8dfdbe",
    "disc-06": "9b8fcb5893499e0a6de6cba0b39c121195231c5f393f9aba74c9f0c6718047c3",
    "disc-07": "35d770d897461b3a2d5040da74436d8ea3f96465575e17a60c31631b85d9a04e",
    "disc-08": "bcd2cf2514404899f202177273af766271652688b41dcef44db7e7462177aecc",
    "disc-09": "3c31604d3575e4c9310f13c69f32bfadc27d91d1d0ed19995f8d7a17cfb02395",
    "disc-10": "a265e73f8c3043e06c35a6d67eb11cf3d04495f5e7a96826f67e0855caf40ec6",
    "disc-11": "f91713e4b75334486ceb6b625f6fdb432963659d8d8302042cb71e2c8a6d3f5f",
    "disc-12": "5a3c869dcf3307459fb548effeb4d4d015188fbd3a358a9f2fe312a800484b1c",
}

REQUIRED_FILES = {"README.md", "prompt.md", "rubric.md", "test.json"}


def _package_files(scenario_dir: Path) -> set[str]:
    return {
        path.relative_to(scenario_dir).as_posix()
        for path in scenario_dir.rglob("*")
        if path.is_file()
    }


def test_skill_discovery_catalog_prepares_only_declared_inputs(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(workspace_module.tempfile, "gettempdir", lambda: str(tmp_path))

    assert {path.name for path in SCENARIO_ROOT.iterdir() if path.is_dir()} == set(
        PROMPT_HASHES
    )

    for scenario_id, prompt_hash in PROMPT_HASHES.items():
        scenario_dir = SCENARIO_ROOT / scenario_id
        package_files = _package_files(scenario_dir)
        optional_files = {"smoke-result.json"} if scenario_id == "disc-12" else set()
        assert REQUIRED_FILES <= package_files <= REQUIRED_FILES | optional_files

        config = load_config(scenario_dir / "test.json")
        raw_config = json.loads((scenario_dir / "test.json").read_bytes())
        assert raw_config["fixtures"] == []

        prompt_template = config.prompt.read_bytes()
        assert hashlib.sha256(prompt_template).hexdigest() == prompt_hash
        rubric_bytes = (scenario_dir / "rubric.md").read_bytes()
        assert rubric_bytes not in prompt_template

        context = workspace_module.create_run(config)
        prepared = workspace_module.prepare_workspace(context, config)

        assert prepared.prompt_bytes == context.prompt_path.read_bytes()
        assert b"{{fixture_dir}}" not in prepared.prompt_bytes
        assert b"{{workspace_dir}}" not in prepared.prompt_bytes
        assert b"{{evidence_dir}}" not in prepared.prompt_bytes
        assert b"supplied-skills/" not in prepared.prompt_bytes
        assert rubric_bytes not in prepared.prompt_bytes
        assert list(context.fixture_dir.iterdir()) == []
        assert list(context.evidence_dir.iterdir()) == []
