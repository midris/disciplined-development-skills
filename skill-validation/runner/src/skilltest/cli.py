"""The one-command public interface for one skill-test run."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import Sequence

from skilltest.runner import run_once


def main(arguments: Sequence[str] | None = None) -> int:
    """Run one configuration and return its mechanical exit code."""
    parser = argparse.ArgumentParser(prog="skilltest")
    commands = parser.add_subparsers(dest="command", required=True)
    run = commands.add_parser("run")
    run.add_argument("config", metavar="CONFIG")
    parsed = parser.parse_args(arguments)

    outcome = run_once(Path(parsed.config))
    if outcome.diagnostic is not None:
        print(f"skilltest: {outcome.diagnostic}", file=sys.stderr)
    elif outcome.exit_code == 1:
        print("skilltest: run failed", file=sys.stderr)
    if outcome.run_dir is not None:
        print(outcome.run_dir.resolve())
    return outcome.exit_code
