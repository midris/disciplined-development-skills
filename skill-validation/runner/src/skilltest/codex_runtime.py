"""Private, disposable Codex profile with shared owned-process mechanics."""
from __future__ import annotations

import json
import os
import shutil
import stat
import subprocess
import tempfile
from pathlib import Path

from skilltest.runtime import ProcessRuntime, PreparationError, SETUP_TIMEOUT_SECONDS


class CodexRuntime(ProcessRuntime):
    """Own the private profile and processes allowed to use its auth copy."""

    label = "Codex"

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

    def _check_login(self, fixture: Path) -> None:
        self.check_status(
            [self.executable, "-c", 'cli_auth_credentials_store="file"', "login", "status"],
            fixture, lambda output: b"ChatGPT" in output or b"API key" in output,
        )
