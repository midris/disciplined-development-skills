"""Minimal executable dummy providers for wiring smoke tests, not fault injection."""

import base64
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path

import pytest


@dataclass
class FakeProvider:
    record_path: Path
    settings_path: Path

    def configure(self, *, stdout=b"", stderr=b"", final=b"", exit_code=0):
        self.settings_path.write_text(json.dumps({
            "record": str(self.record_path), "exit_code": exit_code,
            "stdout": base64.b64encode(stdout).decode(),
            "stderr": base64.b64encode(stderr).decode(),
            "final": base64.b64encode(final).decode(),
        }))

    def record(self):
        return json.loads(self.record_path.read_text().splitlines()[-1])


@pytest.fixture
def fake_provider(tmp_path, monkeypatch, private_test_profile):
    bin_dir = tmp_path / "fake-bin"
    bin_dir.mkdir()
    fake = FakeProvider(tmp_path / "provider-record.jsonl", bin_dir / "provider-settings.json")
    script = """#!PYTHON_EXECUTABLE
import base64,json,os,sys,subprocess
from pathlib import Path
settings=json.loads(Path(__file__).with_name("provider-settings.json").read_text())
record=Path(settings["record"])
environment={k: os.environ[k] for k in ("HOME","CODEX_HOME","TMPDIR","PATH") if k in os.environ}
if "auth" in sys.argv and "status" in sys.argv:
    print(json.dumps({"loggedIn": True, "authMethod": "claude.ai", "test_marker": "DUMMY_AUTH_STATUS_MUST_NOT_BE_RETAINED"}))
    sys.exit(0)
if "login" in sys.argv and "status" in sys.argv:
    auth=Path(os.environ["CODEX_HOME"])/"auth.json"
    record.with_name("login-record.json").write_text(json.dumps({
        "argv": sys.argv, "environment": environment,
        "environment_keys": sorted(os.environ),
        "auth_mode": auth.stat().st_mode & 0o777,
        "profile_mode": auth.parent.stat().st_mode & 0o777,
        "profile_files": sorted(p.name for p in auth.parent.iterdir()),
    }))
    print("Logged in using ChatGPT")
    print("DUMMY_AUTH_STATUS_MUST_NOT_BE_RETAINED", file=sys.stderr)
    sys.exit(0)
if Path(sys.argv[0]).name == "claude":
    fixture=Path.cwd()
    assert (fixture/".git/config").is_file()
    assert os.environ["GIT_CONFIG_NOSYSTEM"] == "1" and os.environ["GIT_CONFIG_GLOBAL"] == os.devnull
    answer=fixture.parent/"evidence/dummy-tool-write.txt"
    answer.write_text("dummy evidence")
    (fixture/"tracked.txt").write_text("local git fixture")
    subprocess.run(["git", "add", "tracked.txt"], check=True, stdout=subprocess.DEVNULL)
    subprocess.run(["git", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "--quiet", "-m", "fixture"], check=True, stdout=subprocess.DEVNULL)
with record.open("a") as stream:
    print(json.dumps({"argv": sys.argv, "cwd": os.getcwd(),
        "stdin": sys.stdin.buffer.read().decode(),
        "environment": environment,
        "claude_baseline_env": {k:v for k,v in os.environ.items() if k.startswith("CLAUDE_CODE_")},
    }), file=stream)
sys.stdout.buffer.write(base64.b64decode(settings["stdout"]))
sys.stderr.buffer.write(base64.b64decode(settings["stderr"]))
if Path(sys.argv[0]).name == "codex":
    Path(sys.argv[sys.argv.index("--output-last-message")+1]).write_bytes(base64.b64decode(settings["final"]))
sys.exit(settings["exit_code"])
"""
    for name in ("codex", "claude"):
        executable = bin_dir / name
        executable.write_text(script.replace("PYTHON_EXECUTABLE", sys.executable, 1))
        executable.chmod(0o700)
    monkeypatch.setenv("PATH", str(bin_dir) + os.pathsep + os.environ["PATH"])
    (private_test_profile / "auth.json").write_text('{"tokens":{"access_token":"dummy-test-only"}}')
    fake.configure()
    return fake
