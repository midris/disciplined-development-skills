"""Shared test configuration for skilltest."""

from __future__ import annotations

import json
import os
import stat
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


@dataclass(frozen=True, slots=True)
class FakeProvider:
    record_path: Path

    def configure(
        self,
        monkeypatch: pytest.MonkeyPatch,
        *,
        stdout: bytes = b"",
        stderr: bytes = b"",
        final: bytes = b"",
        exit_code: int = 0,
        delay_seconds: float = 0,
        write_final: bool = True,
    ) -> None:
        monkeypatch.setenv("SKILLTEST_FAKE_STDOUT", stdout.decode("utf-8"))
        monkeypatch.setenv("SKILLTEST_FAKE_STDERR", stderr.decode("utf-8"))
        monkeypatch.setenv("SKILLTEST_FAKE_FINAL", final.decode("utf-8"))
        monkeypatch.setenv("SKILLTEST_FAKE_EXIT", str(exit_code))
        monkeypatch.setenv("SKILLTEST_FAKE_DELAY", str(delay_seconds))
        monkeypatch.setenv("SKILLTEST_FAKE_WRITE_FINAL", "1" if write_final else "0")

    def record(self) -> dict[str, object]:
        records = self.record_path.read_text(encoding="utf-8").splitlines()
        assert len(records) == 1
        return json.loads(records[0])


@pytest.fixture
def fake_provider(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> FakeProvider:
    bin_dir = tmp_path / "fake-bin"
    bin_dir.mkdir()
    record_path = tmp_path / "provider-record.json"
    script = """#!/usr/bin/env python3
import json
import os
import sys
import time
from pathlib import Path

record_path = Path(os.environ["SKILLTEST_FAKE_RECORD"])
with record_path.open("a", encoding="utf-8") as record_file:
    print(json.dumps({
    "argv": sys.argv,
    "cwd": os.getcwd(),
    "stdin": sys.stdin.buffer.read().decode("utf-8"),
    "path_prefix": os.environ["PATH"].split(os.pathsep)[0],
    "marker": os.environ.get("SKILLTEST_FAKE_MARKER"),
    }), file=record_file)
time.sleep(float(os.environ["SKILLTEST_FAKE_DELAY"]))
sys.stdout.buffer.write(os.environ["SKILLTEST_FAKE_STDOUT"].encode("utf-8"))
sys.stderr.buffer.write(os.environ["SKILLTEST_FAKE_STDERR"].encode("utf-8"))
if sys.argv[0].endswith("codex") and os.environ["SKILLTEST_FAKE_WRITE_FINAL"] == "1":
    output_path = Path(sys.argv[sys.argv.index("--output-last-message") + 1])
    output_path.write_bytes(os.environ["SKILLTEST_FAKE_FINAL"].encode("utf-8"))
sys.exit(int(os.environ["SKILLTEST_FAKE_EXIT"]))
"""
    for name in ("codex", "claude"):
        path = bin_dir / name
        path.write_text(script, encoding="utf-8")
        path.chmod(path.stat().st_mode | stat.S_IXUSR)
    monkeypatch.setenv("PATH", str(bin_dir) + os.pathsep + os.environ["PATH"])
    monkeypatch.setenv("SKILLTEST_FAKE_RECORD", str(record_path))
    monkeypatch.setenv("SKILLTEST_FAKE_MARKER", "inherited")
    return FakeProvider(record_path)


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
