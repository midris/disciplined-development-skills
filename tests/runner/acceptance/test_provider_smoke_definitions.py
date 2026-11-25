"""Provider-free checks for the controlled provider smoke definitions."""

from __future__ import annotations

from pathlib import Path

import pytest

from skilltest.config import load_config
import skilltest.workspace as workspace_module


SMOKE_DIR = Path(__file__).parent / "fixtures" / "provider-smoke"


def test_provider_smoke_definitions_prepare_expected_workspaces(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(workspace_module.tempfile, "gettempdir", lambda: str(tmp_path))

    expected_executions = {
        "codex.json": ("codex", "gpt-5.6-sol", "low"),
        "claude.json": ("claude", "sonnet", "low"),
    }
    for config_name, (provider, model, effort) in expected_executions.items():
        config = load_config(SMOKE_DIR / config_name)

        assert config.execution.provider == provider
        assert config.execution.model == model
        assert config.execution.effort == effort

        context = workspace_module.create_run(config)
        prepared = workspace_module.prepare_workspace(context, config)

        expected_prompt = (
            "This is an explicitly authorized runner acceptance smoke.\n"
            f"Read {context.fixture_dir.resolve()}/input.txt.\n"
            f"Write one regular UTF-8 file at {context.evidence_dir.resolve()}/smoke-output.txt.\n"
            "Return a short final response.\n"
            f"Do not modify anything outside {context.workspace_dir.resolve()}.\n"
        ).encode("utf-8")
        assert prepared.prompt_bytes == expected_prompt
        assert context.prompt_path.read_bytes() == expected_prompt
        assert (context.fixture_dir / "input.txt").read_bytes() == b"runner smoke fixture\n"
        assert list(context.evidence_dir.iterdir()) == []

