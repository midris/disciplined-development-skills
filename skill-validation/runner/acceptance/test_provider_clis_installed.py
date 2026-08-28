"""Opt-in checks for the pinned provider CLIs; these never invoke a model."""

from __future__ import annotations

import shutil
import subprocess

import pytest


_CHECK_COMMANDS = {
    "codex-version": ("codex", "--version"),
    "codex-help": ("codex", "--help"),
    "codex-exec-help": ("codex", "exec", "--help"),
    "claude-version": ("claude", "--version"),
    "claude-help": ("claude", "--help"),
}


def _output(operation: str) -> str:
    try:
        arguments = _CHECK_COMMANDS[operation]
    except KeyError as error:
        raise ValueError(f"unsupported installed CLI check: {operation}") from error
    executable = shutil.which(arguments[0])
    assert executable is not None, f"required executable is absent: {arguments[0]}"
    process = subprocess.run(arguments, check=False, capture_output=True, text=True)
    assert process.returncode == 0, process.stderr
    return process.stdout


def test_rejects_unknown_operation_before_subprocess(monkeypatch) -> None:
    # Break caught: allowing a caller to turn an acceptance check into inference.
    monkeypatch.setattr(
        subprocess,
        "run",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("subprocess reached")),
    )

    with pytest.raises(ValueError, match="unsupported installed CLI check"):
        _output("unknown")


def test_installed_codex_has_the_target_version_and_adapter_flags() -> None:
    # Version and help subcommands are structurally incapable of model invocation.
    assert _output("codex-version").strip() == "codex-cli 0.150.1"
    global_help = _output("codex-help")
    exec_help = _output("codex-exec-help")
    for flag in ("--ask-for-approval", "--search", "--cd"):
        assert flag in global_help
    for flag in (
        "--strict-config",
        "--ignore-user-config",
        "--ignore-rules",
        "--ephemeral",
        "--skip-git-repo-check",
        "--json",
        "--color",
        "--model",
        "-c, --config",
        "--sandbox",
        "--output-last-message",
    ):
        assert flag in exec_help


def test_installed_claude_has_the_target_version_and_adapter_flags() -> None:
    # Version and help subcommands are structurally incapable of model invocation.
    assert _output("claude-version").strip() == "2.1.250 (Claude Code)"
    help_output = _output("claude-help")
    for flag in (
        "--print",
        "--safe-mode",
        "--no-session-persistence",
        "--no-chrome",
        "--input-format",
        "--output-format",
        "--verbose",
        "--model",
        "--effort",
        "--allow-dangerously-skip-permissions",
        "--permission-mode",
    ):
        assert flag in help_output
