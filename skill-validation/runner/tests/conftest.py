"""Shared test configuration for skilltest."""

from __future__ import annotations

import json
import os
import subprocess
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path

import pytest

from skilltest.config import TestConfig, load_config


def pytest_collection_modifyitems(items):
    for item in items:
        if "process_smoke" in item.path.parts:
            item.add_marker(pytest.mark.process_smoke)


@pytest.fixture(autouse=True)
def unit_process_boundary(request, monkeypatch):
    if request.node.get_closest_marker("process_smoke"):
        return

    def unexpected(*args, **kwargs):
        pytest.fail("unit test crossed a real process/time boundary; mock it or use process_smoke")

    monkeypatch.setattr(subprocess, "Popen", unexpected)
    monkeypatch.setattr(os, "killpg", unexpected)
    monkeypatch.setattr(time, "sleep", unexpected)


@dataclass(frozen=True, slots=True)
class ConfigCase:
    root: Path
    config_path: Path
    config: TestConfig
    prompt_bytes: bytes


def _write(path: Path, content: str | bytes = "") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content if isinstance(content, bytes) else content.encode("utf-8"))
    return path


@pytest.fixture(autouse=True)
def private_test_profile(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    # No default offline test may read the owner's authentication or settings.
    home = tmp_path / "invoking-home"
    profile = tmp_path / "invoking-codex"
    home.mkdir()
    profile.mkdir()
    monkeypatch.setenv("HOME", str(home))
    monkeypatch.setenv("CODEX_HOME", str(profile))
    monkeypatch.setattr(tempfile, "tempdir", str(tmp_path))
    return profile


@pytest.fixture
def build_config_case(tmp_path: Path) -> object:
    def build(
        *,
        name: str = "case",
        prompt_bytes: bytes = b"follow the scenario carefully",
        fixtures: tuple[tuple[str, str, str | bytes], ...] = (),
        provider: str = "codex",
        model: str = "gpt-5.6-sol",
        effort: str = "low",
    ) -> ConfigCase:
        root = tmp_path / name
        _write(root / "prompt.md", prompt_bytes)
        fixture_entries: list[dict[str, str]] = []
        for source, target, contents in fixtures:
            _write(root / source, contents)
            fixture_entries.append({"source": source, "target": target})

        config_value: dict[str, object] = {
            "schema_version": "0.2",
            "id": f"{name}-run",
            "prompt": "prompt.md",
            "fixtures": fixture_entries,
            "execution": {"provider": provider, "model": model, "effort": effort},
        }

        config_path = root / "case.json"
        config_path.write_bytes(json.dumps(config_value, separators=(",", ":")).encode("utf-8"))

        return ConfigCase(
            root=root,
            config_path=config_path,
            config=load_config(config_path),
            prompt_bytes=prompt_bytes,
        )

    return build
