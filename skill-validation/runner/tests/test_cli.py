"""Black-box checks for the sole skilltest command."""

from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

from skilltest import cli as cli_module
from skilltest.runner import RunOutcome


def test_run_command_has_one_bundle_per_external_invocation(
    build_config_case, capsys, fake_provider, monkeypatch, tmp_path: Path
) -> None:
    # Break caught: removing the public ``skilltest run CONFIG`` entry point.
    command = Path(sys.executable).with_name("skilltest")
    assert command.is_file()

    case = build_config_case(name="cli")
    temporary_root = tmp_path / "temporary-root"
    temporary_root.mkdir()
    fake_provider.configure(monkeypatch, final=b"final")

    def normal_environment() -> dict[str, str]:
        return os.environ.copy() | {"TMPDIR": str(temporary_root)}

    def invoke(*arguments: str, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [str(command), *arguments],
            check=False,
            capture_output=True,
            text=True,
            env=normal_environment() if env is None else env,
        )

    for arguments in (
        (),
        ("run",),
        ("run", str(case.config_path), "extra"),
        ("unknown", str(case.config_path)),
    ):
        misuse = invoke(*arguments)
        assert misuse.returncode == 2
        assert misuse.stdout == ""
        assert "usage:" in misuse.stderr

    invalid_config = tmp_path / "invalid.json"
    invalid_config.write_text("{", encoding="utf-8")
    invalid = invoke("run", str(invalid_config))
    assert invalid.returncode == 2
    assert invalid.stdout == ""
    assert "invalid JSON configuration" in invalid.stderr
    assert not (temporary_root / "skilltest-runs").exists()

    invalid_utf8 = build_config_case(name="invalid-utf8")
    (invalid_utf8.root / "prompt.md").write_bytes(b"\xff")
    invalid_prompt = invoke("run", str(invalid_utf8.config_path))
    assert invalid_prompt.returncode == 2
    assert invalid_prompt.stdout == ""
    assert "prompt must be readable UTF-8" in invalid_prompt.stderr
    assert not (temporary_root / "skilltest-runs").exists()

    successful_runs = [invoke("run", str(case.config_path)) for _ in range(2)]
    serial_run_dirs = [Path(process.stdout.strip()) for process in successful_runs]
    assert all(process.returncode == 0 for process in successful_runs)
    assert all(process.stderr == "" for process in successful_runs)
    assert all(run_dir.is_absolute() and run_dir.is_dir() for run_dir in serial_run_dirs)
    assert len(set(serial_run_dirs)) == 2

    fake_provider.configure(monkeypatch, final=b"final", exit_code=9)
    provider_failure = invoke("run", str(case.config_path))
    failed_run_dir = Path(provider_failure.stdout.strip())
    assert provider_failure.returncode == 1
    assert provider_failure.stderr == "skilltest: run failed\n"
    assert failed_run_dir.is_absolute() and failed_run_dir.is_dir()

    # Break caught: dropping either output channel when a failed run owns a bundle.
    diagnostic_run_dir = tmp_path / "diagnostic-run"
    diagnostic_run_dir.mkdir()
    monkeypatch.setattr(
        cli_module,
        "run_once",
        lambda _: RunOutcome(1, diagnostic_run_dir, "result artifact write failed"),
    )
    assert cli_module.main(["run", "ignored.json"]) == 1
    captured = capsys.readouterr()
    assert captured.err == "skilltest: result artifact write failed\n"
    assert captured.out == f"{diagnostic_run_dir.resolve()}\n"

    allocation_root = tmp_path / "allocation-root"
    allocation_root.mkdir()
    (allocation_root / "skilltest-runs").write_text("not a directory", encoding="utf-8")
    allocation_environment = normal_environment() | {"TMPDIR": str(allocation_root)}
    allocation_failure = invoke("run", str(case.config_path), env=allocation_environment)
    assert allocation_failure.returncode == 1
    assert allocation_failure.stdout == ""
    assert "run allocation failed:" in allocation_failure.stderr

    fake_provider.configure(monkeypatch, final=b"final")
    processes = [
        subprocess.Popen(
            [str(command), "run", str(case.config_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=normal_environment(),
        )
        for _ in range(2)
    ]
    simultaneous_results = [process.communicate() for process in processes]
    simultaneous_run_dirs = [Path(stdout.strip()) for stdout, _ in simultaneous_results]
    assert all(process.returncode == 0 for process in processes)
    assert all(stderr == "" for _, stderr in simultaneous_results)
    assert all(run_dir.is_absolute() and run_dir.is_dir() for run_dir in simultaneous_run_dirs)
    assert len(set(simultaneous_run_dirs)) == 2

    help_output = invoke("--help")
    assert help_output.returncode == 0
    assert "{run}" in help_output.stdout
    assert "promote" not in help_output.stdout
    assert "clean" not in help_output.stdout
