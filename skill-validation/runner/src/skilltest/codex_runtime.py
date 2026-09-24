"""Private, disposable Codex profile with shared owned-process mechanics."""
from __future__ import annotations

import json
import os
import shutil
import shlex
import stat
import subprocess
import tempfile
from pathlib import Path

from skilltest.runtime import ProcessRuntime, PreparationError, SETUP_TIMEOUT_SECONDS


class CodexRuntime(ProcessRuntime):
    """Own the private profile and processes allowed to use its auth copy."""

    label = "Codex"

    def __init__(self, log):
        super().__init__(log)
        self.session_capture_error: str | None = None

    def retain_session(self, destination: Path) -> str | None:
        """Publish the one invocation-owned rollout before removing its private profile."""
        temporary = None
        try:
            if self.root is None or self.process_cleanup_error:
                raise OSError("private runtime or stopped process boundary unavailable")
            sessions = self.root / "codex/sessions"
            if sessions.is_symlink() or not sessions.is_dir():
                raise OSError("session directory unavailable")
            candidates = []
            for folder, dirs, files in os.walk(sessions, followlinks=False):
                if any((Path(folder) / name).is_symlink() for name in dirs + files):
                    raise OSError("session tree contains a symlink")
                candidates.extend(Path(folder) / name for name in files
                                  if name.startswith("rollout-") and name.endswith(".jsonl"))
            if len(candidates) != 1:
                raise OSError("expected exactly one session rollout")
            descriptor = os.open(candidates[0], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
            with os.fdopen(descriptor, "rb") as source:
                if not stat.S_ISREG(os.fstat(source.fileno()).st_mode):
                    raise OSError("session rollout is not a regular file")
                content = source.read()
            if not content:
                raise OSError("session rollout is empty")
            descriptor, name = tempfile.mkstemp(prefix=".provider-session-", dir=destination.parent)
            temporary = Path(name)
            with os.fdopen(descriptor, "wb") as target:
                target.write(content)
            if temporary.read_bytes() != content:
                raise OSError("session copy verification failed")
            os.link(temporary, destination)  # Exclusive publication; never replace another artifact.
        except OSError as error:
            self.session_capture_error = f"session capture failed: {error}"
        finally:
            if temporary is not None:
                try:
                    temporary.unlink(missing_ok=True)
                except OSError as error:
                    self.session_capture_error = f"session temporary-file cleanup failed: {error}"
        return self.session_capture_error

    def cleanup(self) -> str | None:
        if self.session_capture_error:
            return f"private Codex runtime retained after session capture failure; manual recovery required: {self.root}"
        return super().cleanup()

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
        # macOS /etc/zprofile reorders PATH in login shells. Restore the prepared
        # tool order afterward, without exposing any ambient user startup files.
        (self.root / "tmp/.zprofile").write_text(
            "export PATH=" + shlex.quote(self.environment["PATH"]) + "\n", encoding="utf-8",
        )
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

    def _check_login(self, fixture: Path) -> None:
        self.check_status(
            [self.executable, "-c", 'cli_auth_credentials_store="file"', "login", "status"],
            fixture, lambda output: b"ChatGPT" in output or b"API key" in output,
        )
