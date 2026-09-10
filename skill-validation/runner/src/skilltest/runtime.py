"""Shared prepared-input checks and bounded, invocation-owned process lifecycle."""
from __future__ import annotations

import hashlib
import json
import os
import selectors
import shutil
import signal
import subprocess
import time
from pathlib import Path
from typing import Callable

from skilltest.config import TestConfig
from skilltest.workspace import RunContext

SETUP_TIMEOUT_SECONDS = 30
TERMINATE_GRACE_SECONDS = 5
AUTH_STATUS_LIMIT = 8192


class PreparationError(Exception):
    """A required provider-free control could not be established."""


def check_inputs(context: RunContext, config: TestConfig) -> dict[str, str]:
    """Compare copied bytes before invocation; this is not catalog qualification."""
    if any(Path(f.target).parts[0] == ".git" for f in config.fixtures):
        raise PreparationError("fixture .git is reserved for the provider project boundary")
    source = config.prompt.read_bytes()
    rendered = source.decode("utf-8")
    for token, path in (
        ("{{workspace_dir}}", context.workspace_dir),
        ("{{fixture_dir}}", context.fixture_dir),
        ("{{evidence_dir}}", context.evidence_dir),
    ):
        rendered = rendered.replace(token, str(path.resolve()))
    pairs = [(context.prompt_template_path, source), (context.prompt_path, rendered.encode("utf-8"))]
    pairs.extend((context.fixture_dir / f.target, f.source.read_bytes()) for f in config.fixtures)
    hashes = {}
    for path, expected in pairs:
        if path.is_symlink() or path.read_bytes() != expected:
            raise PreparationError("prepared input does not match its declared source")
        hashes[path.relative_to(context.run_dir).as_posix()] = hashlib.sha256(expected).hexdigest()
    return hashes


def _group_exists(process: subprocess.Popen) -> bool:
    process.poll()  # Reap the direct child before testing whether its group remains.
    try:
        os.killpg(process.pid, 0)
    except ProcessLookupError:
        return False
    return True


def stop_owned(process: subprocess.Popen) -> str | None:
    """Stop only a child created with start_new_session=True, with bounded waits."""
    try:
        for sig in (signal.SIGTERM, signal.SIGKILL):
            if not _group_exists(process):
                process.wait(timeout=TERMINATE_GRACE_SECONDS)
                return None
            try:
                os.killpg(process.pid, sig)
            except ProcessLookupError:
                pass
            deadline = time.monotonic() + TERMINATE_GRACE_SECONDS
            while time.monotonic() < deadline:
                if not _group_exists(process):
                    process.wait(timeout=TERMINATE_GRACE_SECONDS)
                    return None
                time.sleep(0.01)
        if not _group_exists(process):
            process.wait(timeout=TERMINATE_GRACE_SECONDS)
            return None
        return "owned provider process group did not exit"
    except (OSError, subprocess.TimeoutExpired):
        return "owned provider process group cleanup could not be verified"


class ProcessRuntime:
    """Shared lifecycle; each provider owns its profile and command preparation."""

    label = "provider"

    def __init__(self, log: Callable[[str], None]):
        self.log = log
        self.prefix: list[str] = []
        self.root: Path | None = None
        self.environment: dict[str, str] = {}
        self.executable = ""
        self.process_cleanup_error: str | None = None

    def _stop(self, process: subprocess.Popen) -> None:
        self.process_cleanup_error = stop_owned(process) or self.process_cleanup_error

    def check_status(self, arguments: list[str], fixture: Path, accepts: Callable[[bytearray], bool]) -> None:
        process = subprocess.Popen(
            arguments, cwd=fixture, env=self.environment, stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, start_new_session=True,
        )
        # Bounded in-memory status inspection: never log or spool credential-bearing text.
        output = bytearray()
        deadline = time.monotonic() + SETUP_TIMEOUT_SECONDS
        try:
            with selectors.DefaultSelector() as selector:
                selector.register(process.stdout, selectors.EVENT_READ)
                while selector.get_map():
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        raise PreparationError(f"{self.label} login status timed out")
                    for key, _ in selector.select(remaining):
                        data = os.read(key.fd, 4096)
                        if not data:
                            selector.unregister(key.fileobj)
                        output.extend(data)
                        if len(output) > AUTH_STATUS_LIMIT:
                            raise PreparationError(f"{self.label} login status exceeded its output limit")
            process.wait(timeout=max(0, deadline - time.monotonic()))
            if process.returncode != 0 or not accepts(output):
                raise PreparationError(f"{self.label} login status did not establish authentication")
        except subprocess.TimeoutExpired:
            raise PreparationError(f"{self.label} login status timed out") from None
        finally:
            self._stop(process)
            process.stdout.close()
            output.clear()
        if self.process_cleanup_error:
            raise PreparationError(f"{self.label} login process cleanup failed")

    def communicate(self, process: subprocess.Popen, data: bytes | None, timeout: float) -> tuple[bytes, bytes, bool]:
        try:
            try:
                stdout, stderr = process.communicate(input=data, timeout=timeout)
                return stdout or b"", stderr or b"", False
            except subprocess.TimeoutExpired:
                self._stop(process)
                try:
                    stdout, stderr = process.communicate(timeout=TERMINATE_GRACE_SECONDS)
                except subprocess.TimeoutExpired as error:
                    # An escaped descendant may hold pipes open; do not wait indefinitely.
                    self.process_cleanup_error = f"{self.label} output pipes did not close after termination"
                    stdout, stderr = error.output, error.stderr
                return stdout or b"", stderr or b"", True
        finally:
            self._stop(process)
            for stream in (process.stdin, process.stdout, process.stderr):
                if stream is not None:
                    try:
                        stream.close()
                    except OSError:
                        self.process_cleanup_error = f"{self.label} subprocess pipes could not be closed"

    def cleanup(self) -> str | None:
        if self.root is None:
            return self.process_cleanup_error
        if not self.process_cleanup_error:
            try:
                shutil.rmtree(self.root)
                if not os.path.lexists(self.root):
                    return None
            except OSError:
                pass
        message = f"private {self.label} runtime cleanup failed; manual recovery required: {self.root}"
        if self.process_cleanup_error:
            message = f"{self.process_cleanup_error}; {message}"
        return message
