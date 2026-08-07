"""Resolve the explicitly pinned active plan for disciplined-development hooks."""

from __future__ import annotations

import os

from hooks.lib import state

_POINTER = ".claude/active-plan"


def resolve_active_plan(cwd: str | None = None) -> tuple[str, str] | None:
    """Return the env/pointer pin anchored to the resolved repository root."""
    start = cwd if isinstance(cwd, str) and cwd else os.getcwd()
    root = state.repo_root(start) or os.path.abspath(start)

    def _anchor(path: str) -> str:
        if os.path.isabs(path):
            return os.path.abspath(path)
        return os.path.abspath(os.path.join(root, path))

    env_plan = os.environ.get("DD_ACTIVE_PLAN", "")
    if env_plan:
        return _anchor(env_plan), "DD_ACTIVE_PLAN env var"

    pointer = os.path.join(root, _POINTER)
    try:
        with open(pointer, encoding="utf-8") as handle:
            pin = next((line.strip() for line in handle if line.strip()), "")
    except (OSError, UnicodeDecodeError):
        return None
    if not pin:
        return None
    return _anchor(pin), pointer
