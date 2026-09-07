"""Shared test configuration for skilltest."""

from __future__ import annotations

import base64
import json
import os
import stat
import sys
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


def _write(path: Path, content: str | bytes = "") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content if isinstance(content, bytes) else content.encode("utf-8"))
    return path


@dataclass(frozen=True, slots=True)
class FakeProvider:
    record_path: Path
    settings_path: Path

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
        fixture_bytes: bytes | None = None,
        evidence_name: str | None = None,
        evidence_bytes: bytes = b"",
        login_exit: int = 0,
        login_delay_seconds: float = 0,
        login_output: str = "Logged in using ChatGPT",
    ) -> None:
        monkeypatch.setenv("SKILLTEST_FAKE_STDOUT", base64.b64encode(stdout).decode("ascii"))
        monkeypatch.setenv("SKILLTEST_FAKE_STDERR", base64.b64encode(stderr).decode("ascii"))
        monkeypatch.setenv("SKILLTEST_FAKE_FINAL", base64.b64encode(final).decode("ascii"))
        monkeypatch.setenv("SKILLTEST_FAKE_EXIT", str(exit_code))
        monkeypatch.setenv("SKILLTEST_FAKE_DELAY", str(delay_seconds))
        monkeypatch.setenv("SKILLTEST_FAKE_WRITE_FINAL", "1" if write_final else "0")
        if fixture_bytes is None:
            monkeypatch.delenv("SKILLTEST_FAKE_FIXTURE", raising=False)
        else:
            monkeypatch.setenv(
                "SKILLTEST_FAKE_FIXTURE",
                base64.b64encode(fixture_bytes).decode("ascii"),
            )
        if evidence_name is None:
            monkeypatch.delenv("SKILLTEST_FAKE_EVIDENCE_NAME", raising=False)
            monkeypatch.delenv("SKILLTEST_FAKE_EVIDENCE", raising=False)
        else:
            monkeypatch.setenv("SKILLTEST_FAKE_EVIDENCE_NAME", evidence_name)
            monkeypatch.setenv(
                "SKILLTEST_FAKE_EVIDENCE",
                base64.b64encode(evidence_bytes).decode("ascii"),
            )
        settings = {
            key: value for key, value in os.environ.items()
            if key.startswith("SKILLTEST_FAKE_")
        }
        settings.update(login_exit=login_exit, login_delay_seconds=login_delay_seconds, login_output=login_output)
        self.settings_path.write_text(json.dumps(settings), encoding="utf-8")

    def record(self) -> dict[str, object]:
        records = self.record_path.read_text(encoding="utf-8").splitlines()
        assert len(records) == 1
        return json.loads(records[0])

    def config_observations(self) -> list[dict[str, bool]]:
        observation_path = self.record_path.with_name("config-observations.jsonl")
        return [json.loads(line) for line in observation_path.read_text(encoding="utf-8").splitlines()]


@pytest.fixture(autouse=True)
def private_test_profile(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    # No default offline test may read the owner's authentication or settings.
    home = tmp_path / "invoking-home"
    profile = tmp_path / "invoking-codex"
    home.mkdir()
    profile.mkdir()
    monkeypatch.setenv("HOME", str(home))
    monkeypatch.setenv("CODEX_HOME", str(profile))
    return profile


@pytest.fixture
def fake_provider(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, private_test_profile: Path) -> FakeProvider:
    bin_dir = tmp_path / "fake-bin"
    bin_dir.mkdir()
    record_path = tmp_path / "provider-record.json"
    script = """#!PYTHON_EXECUTABLE
import base64
import json
import os
import sys
import time
from pathlib import Path

settings = json.loads(Path(__file__).with_name("provider-settings.json").read_text())
record_path = Path(settings["SKILLTEST_FAKE_RECORD"])
if "login" in sys.argv and "status" in sys.argv:
    auth = Path(os.environ["CODEX_HOME"]) / "auth.json"
    record_path.with_name("login-record.json").write_text(json.dumps({
        "argv": sys.argv,
        "environment": {k: os.environ[k] for k in ("HOME", "CODEX_HOME", "TMPDIR", "PATH") if k in os.environ},
        "environment_keys": sorted(os.environ),
        "auth_mode": auth.stat().st_mode & 0o777,
        "profile_mode": auth.parent.stat().st_mode & 0o777,
        "profile_files": sorted(p.name for p in auth.parent.iterdir()),
    }))
    time.sleep(settings["login_delay_seconds"])
    print(settings["login_output"])
    print("DUMMY_AUTH_STATUS_MUST_NOT_BE_RETAINED", file=sys.stderr)
    sys.exit(settings["login_exit"])
with record_path.open("a", encoding="utf-8") as record_file:
    print(json.dumps({
    "argv": sys.argv,
    "cwd": os.getcwd(),
    "stdin": sys.stdin.buffer.read().decode("utf-8"),
    "path_prefix": os.environ["PATH"].split(os.pathsep)[0],
    "marker": os.environ.get("SKILLTEST_FAKE_MARKER"),
    "environment": {k: os.environ[k] for k in ("HOME", "CODEX_HOME", "TMPDIR", "PATH") if k in os.environ},
    "environment_keys": sorted(os.environ),
    "claude_baseline_env": {
        name: os.environ.get(name)
        for name in (
            "CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT",
            "CLAUDE_CODE_DISABLE_AUTO_MEMORY",
            "CLAUDE_CODE_DISABLE_BUNDLED_SKILLS",
            "CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS",
            "CLAUDE_CODE_DISABLE_WORKFLOWS",
            "CLAUDE_CODE_DISABLE_ARTIFACT",
            "CLAUDE_CODE_DISABLE_CRON",
            "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC",
        )
    },
    }), file=record_file)
codex_fixture = sys.argv[0].endswith("codex") and Path.cwd().name == "fixture"
run_dir = Path.cwd().parent.parent if codex_fixture else Path.cwd().parent
before_output = (run_dir / "config.json").exists()
fixture_payload = settings.get("SKILLTEST_FAKE_FIXTURE")
if fixture_payload is not None:
    fixture_file = Path("input.txt") if codex_fixture else Path("fixture/input.txt")
    fixture_file.write_bytes(base64.b64decode(fixture_payload))
evidence_name = settings.get("SKILLTEST_FAKE_EVIDENCE_NAME")
if evidence_name is not None:
    evidence_path = (Path("../evidence") if codex_fixture else Path("evidence")) / evidence_name
    evidence_path.parent.mkdir(parents=True, exist_ok=True)
    evidence_path.write_bytes(base64.b64decode(settings["SKILLTEST_FAKE_EVIDENCE"]))
time.sleep(float(settings["SKILLTEST_FAKE_DELAY"]))
sys.stdout.buffer.write(base64.b64decode(settings["SKILLTEST_FAKE_STDOUT"]))
sys.stderr.buffer.write(base64.b64decode(settings["SKILLTEST_FAKE_STDERR"]))
if sys.argv[0].endswith("codex") and settings["SKILLTEST_FAKE_WRITE_FINAL"] == "1":
    output_path = Path(sys.argv[sys.argv.index("--output-last-message") + 1])
    output_path.write_bytes(base64.b64decode(settings["SKILLTEST_FAKE_FINAL"]))
observation_path = Path(settings["SKILLTEST_FAKE_CONFIG_OBSERVATIONS"])
with observation_path.open("a", encoding="utf-8") as observation_file:
    print(json.dumps({
        "before_output": before_output,
        "after_output": (run_dir / "config.json").exists(),
    }), file=observation_file)
sys.exit(int(settings["SKILLTEST_FAKE_EXIT"]))
"""
    script = script.replace("PYTHON_EXECUTABLE", sys.executable, 1)
    for name in ("codex", "claude"):
        path = bin_dir / name
        path.write_text(script, encoding="utf-8")
        path.chmod(path.stat().st_mode | stat.S_IXUSR)
    monkeypatch.setenv("PATH", str(bin_dir) + os.pathsep + os.environ["PATH"])
    monkeypatch.setenv("SKILLTEST_FAKE_RECORD", str(record_path))
    monkeypatch.setenv(
        "SKILLTEST_FAKE_CONFIG_OBSERVATIONS",
        str(record_path.with_name("config-observations.jsonl")),
    )
    monkeypatch.setenv("SKILLTEST_FAKE_MARKER", "inherited")
    (private_test_profile / "auth.json").write_text('{"tokens":{"access_token":"dummy-test-only"}}')
    fake = FakeProvider(record_path, bin_dir / "provider-settings.json")
    fake.configure(monkeypatch)
    return fake


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
