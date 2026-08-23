"""Shared test configuration for skilltest."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path

import pytest

from skilltest.config import TestConfig, load_config


@dataclass(frozen=True, slots=True)
class ConfigCase:
    root: Path
    config_path: Path
    config: TestConfig
    prompt_bytes: bytes
    expected_marker: str


def _write(path: Path, content: str | bytes = "") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content if isinstance(content, bytes) else content.encode("utf-8"))
    return path


def _symlink(path: Path, target: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    os.symlink(target, path)
    return path


@pytest.fixture
def build_config_case(tmp_path: Path) -> object:
    def build(
        *,
        name: str = "case",
        fixture: str = "empty",
        dependencies: tuple[str, ...] = ("helper-b", "helper-a"),
        prompt_bytes: bytes = b"follow the scenario carefully",
        expected_marker: str = "hidden-expected-outcome",
    ) -> ConfigCase:
        root = tmp_path / name
        primary = root / "primary"
        _write(primary / "SKILL.md", "Primary skill instructions.\n")
        _write(primary / "scripts" / "tool.sh", b"#!/bin/sh\necho primary\n")

        dependency_values: list[dict[str, str]] = []
        for dependency in dependencies:
            dependency_root = root / dependency
            _write(dependency_root / "SKILL.md", f"{dependency} instructions.\n")
            _write(
                dependency_root / "resources" / "notes.txt",
                f"resource for {dependency}\n",
            )
            dependency_values.append({"id": dependency, "source": dependency})

        prompt_path = _write(root / "prompt.txt", prompt_bytes)

        fixture_value: str | None
        if fixture == "none":
            fixture_value = None
        else:
            fixture_root = root / "fixture"
            fixture_root.mkdir(parents=True, exist_ok=True)
            fixture_value = "fixture"
            if fixture == "populated":
                _write(fixture_root / "docs" / "guide.txt", "fixture guide\n")
                _write(fixture_root / "bin" / "start.sh", b"#!/bin/sh\necho fixture\n")
                _symlink(fixture_root / "guide-link.txt", "docs/guide.txt")
            elif fixture != "empty":
                raise ValueError(f"unknown fixture kind: {fixture}")

        config_path = root / "case.json"
        config_path.write_bytes(
            json.dumps(
                {
                    "schema_version": 1,
                    "id": f"{name}-run",
                    "skill": {"id": "primary", "source": "primary"},
                    "dependencies": dependency_values,
                    "scenario": {
                        "id": f"{name}-scenario",
                        "prompt": prompt_path.name,
                        "fixture": fixture_value,
                    },
                    "expected_outcome": {"secret": expected_marker},
                    "execution": {
                        "provider": "codex",
                        "model": "gpt-5.4",
                        "effort": "medium",
                    },
                },
                separators=(",", ":"),
            ).encode("utf-8")
        )

        return ConfigCase(
            root=root,
            config_path=config_path,
            config=load_config(config_path),
            prompt_bytes=prompt_bytes,
            expected_marker=expected_marker,
        )

    return build
