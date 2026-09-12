"""Claude subscription reuse with the accepted macOS contamination controls."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable

from skilltest.runtime import PreparationError, ProcessRuntime, SETUP_TIMEOUT_SECONDS

CLAUDE_ENV = {
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1", "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1",
    "DISABLE_AUTOUPDATER": "1", "DISABLE_TELEMETRY": "1", "DISABLE_ERROR_REPORTING": "1",
    "CLAUDE_CODE_MAX_RETRIES": "0", "CLAUDE_CODE_SKIP_PROMPT_HISTORY": "1",
    "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull,
}
HOST_INPUTS = (
    "CLAUDE.md", "settings.json", "settings.local.json", "skills", "commands",
    "plugins", "agents", "projects",
)
ANCESTOR_INPUTS = (
    "CLAUDE.md", "CLAUDE.local.md", ".claude/CLAUDE.md", ".claude/settings.json",
    ".claude/settings.local.json", ".claude/skills", ".claude/commands", ".claude/agents", ".mcp.json",
)


def authenticated(output: bytearray) -> bool:
    try:
        status = json.loads(output)
        return isinstance(status, dict) and status.get("loggedIn") is True and status.get("authMethod") == "claude.ai"
    except (ValueError, UnicodeError):
        return False


class ClaudeRuntime(ProcessRuntime):
    label = "Claude"

    def __init__(self, log: Callable[[str], None], *, permissions: str = "workspace-write"):
        super().__init__(log)
        if permissions not in {"workspace-write", "read-only"}:
            raise ValueError(f"unsupported permissions: {permissions}")
        self.permissions = permissions

    def prepare(self, fixture: Path) -> None:
        if sys.platform != "darwin":
            raise PreparationError("controlled Claude runtime requires macOS sandbox-exec")
        executable = shutil.which("claude")
        sandbox = shutil.which("sandbox-exec", path="/usr/bin:/bin")
        if not executable or not sandbox:
            raise PreparationError("Claude executable or sandbox-exec is unavailable")
        self.executable = str(Path(executable).absolute())
        if os.path.lexists(fixture / ".git"):
            raise PreparationError("fixture .git already exists; refusing to overwrite it")
        for parent in fixture.resolve().parents:
            for name in ANCESTOR_INPUTS:
                if os.path.lexists(parent / name):
                    raise PreparationError(f"Claude instruction ancestry is not clean: {parent / name}")
        home = Path(os.environ["HOME"]).resolve()
        user = os.environ.get("USER")
        if not home.is_dir() or not user:
            raise PreparationError("Claude subscription reuse requires existing HOME and USER")
        self.root = Path(tempfile.mkdtemp(prefix="skilltest-claude-")).resolve()
        self.log(f"private Claude runtime (manual recovery if interrupted): {self.root}")
        # The accepted policy forbids home writes; runtime/workspace must be outside it.
        if self.root.is_relative_to(home) or fixture.resolve().is_relative_to(home):
            raise PreparationError("Claude workspace and temporary runtime must be outside HOME")
        (self.root / "tmp").mkdir(mode=0o700)
        self.environment = CLAUDE_ENV | {
            "HOME": str(home), "USER": user,
            "PATH": f"{Path(self.executable).parent}:/usr/bin:/bin:/usr/sbin:/sbin",
            "TMPDIR": str(self.root / "tmp"), "CLAUDE_CODE_TMPDIR": str(self.root / "tmp"),
            "CLAUDE_CODE_DEBUG_LOGS_DIR": str(self.root / "tmp/debug"),
        }
        policy = self.root / "policy.sb"
        policy.write_text(
            '(version 1)\n(allow default)\n'
            + (
                # Enforce on the whole process tree, including Bash and file tools.
                # Only private CLI scratch and /dev/null remain writable; neither
                # contains supplied evidence or the runner's authoritative bundle.
                '(deny file-write*)\n'
                + f'(allow file-write* (subpath {json.dumps(str(self.root / "tmp"))}) (literal "/dev/null"))\n'
                if self.permissions == "read-only" else ''
            )
            + f'(deny file-write* (subpath {json.dumps(str(home))}))\n'
            + ''.join(f'(deny file-read* (subpath {json.dumps(str(home / ".claude" / name))}))\n' for name in HOST_INPUTS)
        )
        self.log(f"Claude sandbox policy: {json.dumps(policy.read_text())}")
        self.prefix = [sandbox, "-f", str(policy)]
        self._check_login(fixture)
        git = shutil.which("git", path=self.environment["PATH"])
        if git is None:
            raise PreparationError("Git executable is unavailable")
        process = subprocess.Popen(
            [git, "init", "--quiet", "--template=", str(fixture)], cwd=fixture,
            env=self.environment, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL, start_new_session=True,
        )
        _, _, timed_out = self.communicate(process, None, SETUP_TIMEOUT_SECONDS)
        if timed_out or process.returncode != 0 or self.process_cleanup_error:
            raise PreparationError("Claude project-boundary initialization failed")

    def _check_login(self, fixture: Path) -> None:
        self.check_status([*self.prefix, self.executable, "auth", "status"], fixture, authenticated)
