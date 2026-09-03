"""The public interface for mechanical skill-test operations."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import Sequence

from skilltest.runner import run_once
from skilltest.worksheet import WorksheetInputError, WorksheetOutputError, write_worksheet


def main(arguments: Sequence[str] | None = None) -> int:
    """Dispatch one mechanical operation and return its exit code."""
    parser = argparse.ArgumentParser(prog="skilltest")
    commands = parser.add_subparsers(dest="command", required=True)
    run = commands.add_parser("run")
    run.add_argument("config", metavar="CONFIG")
    worksheet = commands.add_parser("worksheet")
    worksheet.add_argument("scenario", metavar="SCENARIO")
    worksheet.add_argument("run_bundle", metavar="RUN_BUNDLE")
    worksheet.add_argument("--output", required=True, metavar="PATH")
    parsed = parser.parse_args(arguments)

    if parsed.command == "worksheet":
        try:
            written_path = write_worksheet(
                parsed.scenario, Path(parsed.run_bundle), Path(parsed.output)
            )
        except WorksheetInputError as error:
            print(f"skilltest: {error}", file=sys.stderr)
            return 2
        except WorksheetOutputError as error:
            print(f"skilltest: {error}", file=sys.stderr)
            return 1
        print(written_path)
        return 0

    outcome = run_once(Path(parsed.config))
    if outcome.diagnostic is not None:
        print(f"skilltest: {outcome.diagnostic}", file=sys.stderr)
    elif outcome.exit_code == 1:
        print("skilltest: run failed", file=sys.stderr)
    if outcome.run_dir is not None:
        print(outcome.run_dir.resolve())
    return outcome.exit_code
