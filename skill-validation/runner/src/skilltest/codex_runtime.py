"""Private, disposable runtime and owned subprocesses for Codex only."""

from __future__ import annotations

import hashlib
import json
import os
import selectors
import shutil
import signal
import stat
import subprocess
import tempfile
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
        raise PreparationError("fixture .git is reserved for the Codex project boundary")
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
        return "owned Codex process group did not exit"
    except (OSError, subprocess.TimeoutExpired):
        return "owned Codex process group cleanup could not be verified"


class CodexRuntime:
    """Own the private profile and the processes allowed to use its auth copy."""

    def __init__(self, log: Callable[[str], None]):
        self.log = log
        self.root: Path | None = None
        self.environment: dict[str, str] = {}
        self.executable = ""
        self.process_cleanup_error: str | None = None

    def prepare(self, fixture: Path) -> None:
        executable = shutil.which("codex")
        if executable is None:
            raise PreparationError("Codex executable is unavailable")
        self.executable = str(Path(executable).absolute())
        if os.path.lexists(fixture / ".git"):
            raise PreparationError("fixture .git already exists; refusing to overwrite it")
        source_profile = Path(os.environ["CODEX_HOME"]) if "CODEX_HOME" in os.environ else Path.home() / ".codex"
        self.root = Path(tempfile.mkdtemp(prefix="skilltest-codex-")).resolve()
        # Write the recovery path before copying auth; a failed log blocks setup.
        self.log(f"private Codex runtime (manual recovery if interrupted): {self.root}")
        for name in ("home", "codex", "tmp"):
            (self.root / name).mkdir(mode=0o700)
        self.environment = {
            "HOME": str(self.root / "home"), "CODEX_HOME": str(self.root / "codex"),
            "TMPDIR": str(self.root / "tmp"),
            "PATH": f"{Path(self.executable).parent}:/usr/bin:/bin:/usr/sbin:/sbin",
        }
        # Open without following the final symlink; never copy settings or instructions.
        try:
            descriptor = os.open(source_profile / "auth.json", os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
            with os.fdopen(descriptor, "rb") as source:
                if not stat.S_ISREG(os.fstat(source.fileno()).st_mode):
                    raise PreparationError("Codex auth cache must be a regular file")
                contents = source.read()
            auth = json.loads(contents)
            if not isinstance(auth, dict) or not auth:
                raise PreparationError("Codex auth cache is not a nonempty JSON object")
            destination = self.root / "codex/auth.json"
            descriptor = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(descriptor, "wb") as output:
                output.write(contents)
        except (OSError, UnicodeError, ValueError):
            raise PreparationError("Codex file-cache authentication is unavailable or malformed") from None
        self._check_login(fixture)
        git = shutil.which("git", path=self.environment["PATH"])
        if git is None:
            raise PreparationError("Git executable is unavailable")
        process = subprocess.Popen(
            [git, "init", "--quiet", "--template=", str(fixture)],
            cwd=fixture, env=self.environment | {"GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull},
            stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
        _, _, timed_out = self.communicate(process, None, SETUP_TIMEOUT_SECONDS)
        if timed_out or process.returncode != 0 or self.process_cleanup_error:
            raise PreparationError("Codex project-boundary initialization failed")

    def _stop(self, process: subprocess.Popen) -> None:
        self.process_cleanup_error = stop_owned(process) or self.process_cleanup_error

    def _check_login(self, fixture: Path) -> None:
        process = subprocess.Popen(
            [self.executable, "-c", 'cli_auth_credentials_store="file"', "login", "status"],
            cwd=fixture, env=self.environment, stdin=subprocess.DEVNULL,
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
                        raise PreparationError("private Codex login status timed out")
                    for key, _ in selector.select(remaining):
                        data = os.read(key.fd, 4096)
                        if not data:
                            selector.unregister(key.fileobj)
                        output.extend(data)
                        if len(output) > AUTH_STATUS_LIMIT:
                            raise PreparationError("private Codex login status exceeded its output limit")
            process.wait(timeout=max(0, deadline - time.monotonic()))
            if process.returncode != 0 or not (b"ChatGPT" in output or b"API key" in output):
                raise PreparationError("private Codex login status did not establish authentication")
        except subprocess.TimeoutExpired:
            raise PreparationError("private Codex login status timed out") from None
        finally:
            self._stop(process)
            process.stdout.close()
            output.clear()
        if self.process_cleanup_error:
            raise PreparationError("private Codex login process cleanup failed")

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
                    self.process_cleanup_error = "Codex output pipes did not close after termination"
                    stdout, stderr = error.output, error.stderr
                return stdout or b"", stderr or b"", True
        finally:
            self._stop(process)
            for stream in (process.stdin, process.stdout, process.stderr):
                if stream is not None:
                    try:
                        stream.close()
                    except OSError:
                        self.process_cleanup_error = "Codex subprocess pipes could not be closed"

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
        message = f"private Codex runtime cleanup failed; manual recovery required: {self.root}"
        if self.process_cleanup_error:
            message = f"{self.process_cleanup_error}; {message}"
        return message
