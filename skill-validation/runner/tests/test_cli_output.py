"""CLI presentation contracts with the runner boundary mocked."""

from pathlib import Path
from unittest.mock import Mock

from skilltest import cli
from skilltest.runner import RunOutcome


def test_failed_run_prints_both_bundle_path_and_diagnostic(tmp_path, monkeypatch, capsys):
    # Break: dropping either output channel when a failed run owns a bundle.
    run_dir = tmp_path / "diagnostic-run"
    run_once = Mock(return_value=RunOutcome(1, run_dir, "result artifact write failed"))
    monkeypatch.setattr(cli, "run_once", run_once)

    assert cli.main(["run", "ignored.json"]) == 1
    run_once.assert_called_once_with(Path("ignored.json"))
    captured = capsys.readouterr()
    assert captured.err == "skilltest: result artifact write failed\n"
    assert captured.out == f"{run_dir.resolve()}\n"
