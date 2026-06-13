"""Shared pytest fixtures for hooks/ tests.

Mirrors the legacy tests' conftest wiring pattern, adapted to
the ``hooks.lib.*`` import path. The directory that *contains* ``hooks/``
(the disciplined-development skill root) is inserted onto ``sys.path`` so
``from hooks.lib.X import ...`` resolves; ``hooks/`` and ``hooks/lib/``
carry ``__init__.py`` to form the package.

* ``captured_logger`` — a pair ``(log_path, read_records)``. Tests point
  ``logging_setup`` at ``log_path``; ``read_records()`` parses the JSONL
  file and returns the records.

* ``git_repo`` — a hermetic temp git repository (one initial commit on
  ``master``, git identity + default branch configured locally) for
  state.py's checkpoint / fork-base tests. Yields the repo root path.
"""

import json
import pathlib
import subprocess
import sys

import pytest

# Insert the base dir (the parent of hooks/) so `import hooks.lib.X` resolves.
# parents[2] = .../disciplined-development (tests -> hooks -> disciplined-development).
_BASE_DIR = pathlib.Path(__file__).resolve().parents[2]
if str(_BASE_DIR) not in sys.path:
    sys.path.insert(0, str(_BASE_DIR))


@pytest.fixture(autouse=True)
def _isolate_dd_logs(monkeypatch):
    """Send test logging to ``/tmp`` by default via ``DD_LOG_DIR`` so the
    rolling logs never pollute the real repo's ``.claude/.dd-state/.logs``
    during the suite (incl. subprocess hooks that inherit ``os.environ``). One
    ephemeral rolling day file, not per-test dirs. Tests that assert on dir
    resolution override / clear ``DD_LOG_DIR`` themselves."""
    monkeypatch.setenv("DD_LOG_DIR", "/tmp/dd-hooks-test")


@pytest.fixture
def captured_logger(tmp_path: pathlib.Path):
    log_path = tmp_path / "captured.jsonl"

    def read_records() -> list[dict]:
        if not log_path.exists():
            return []
        return [
            json.loads(line)
            for line in log_path.read_text().splitlines()
            if line.strip()
        ]

    return (log_path, read_records)


def _git(args: list[str], cwd: pathlib.Path) -> str:
    """Run a git command in ``cwd``, returning stripped stdout."""
    return subprocess.run(
        ["git", *args],
        cwd=str(cwd),
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


@pytest.fixture
def git_repo(tmp_path: pathlib.Path):
    """A hermetic temp git repo with one initial commit on ``master``.

    Git identity + default branch are set locally so the fixture is
    hermetic regardless of host git config. Yields the repo root path.
    """
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(["init", "-b", "master"], repo)
    _git(["config", "user.email", "test@example.com"], repo)
    _git(["config", "user.name", "Test"], repo)
    (repo / "seed.txt").write_text("seed\n")
    _git(["add", "."], repo)
    _git(["commit", "-m", "seed"], repo)
    yield repo
