"""Shared active-plan resolution for disciplined-development hooks.

Resolves the repo's active plan to ``(plan_path, source_label)`` using a
fixed priority (highest first):

  1. ``DD_ACTIVE_PLAN`` env var (a path) → label ``"DD_ACTIVE_PLAN env var"``.
     Returned as-is when non-empty, regardless of whether the path exists
     (matches the ``dd_lib`` predecessor — an explicit pointer wins even if
     stale; a non-existent path is *not* a fall-through trigger).
  2. ``plans.active_plan_pointer`` file (default ``.claude/active-plan``).
     Its first non-empty line is the plan path; the label is the anchored
     pointer-file path itself.
  3. ``plans.fallback_glob`` (default ``["plans/*.md"]``) newest by mtime →
     label ``"mtime fallback"``.

Relative pointer/glob paths are anchored to ``git rev-parse --show-toplevel``
so invocation from a subdir (e.g. ``git commit`` from ``backend/``) still
finds the configured pointer. Falls back to cwd-relative when not in a git
repo. The fallback glob is read from config via :mod:`hooks.lib.config`
(the one intended cross-module dependency).

Shared by ``external_review`` (feeds the reviewer its plan/spec paths) and
``inject_plan_state`` (path resolution only; checkbox parsing stays in the
injector). Side-effect-free except for the read-only git/glob/file probes.
"""
from __future__ import annotations

import glob
import os
import subprocess

from hooks.lib import config


def _git_toplevel(cwd: str | None = None) -> str | None:
    """Return the git working-tree top for ``cwd`` (or the process cwd), or
    None if not in a git repo / git is unavailable. Anchors relative plan
    paths so subdir CWDs don't silently miss configured pointers/globs."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            timeout=5,
            cwd=cwd,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if result.returncode != 0:
        return None
    root = result.stdout.strip()
    return root or None


def resolve_active_plan(cwd: str | None = None) -> tuple[str, str] | None:
    """Return ``(plan_path, source_label)`` or None.

    ``cwd`` anchors the git-toplevel probe (default: process cwd) so the
    function is testable against a fake repo dir. See the module docstring
    for the resolution priority and exact source-label strings.
    """
    env_plan = os.environ.get("DD_ACTIVE_PLAN", "")
    if env_plan:
        return env_plan, "DD_ACTIVE_PLAN env var"

    root = _git_toplevel(cwd)

    def _anchor(p: str) -> str:
        if os.path.isabs(p) or root is None:
            return p
        return os.path.join(root, p)

    pointer_file = _anchor(
        config.get("plans.active_plan_pointer", ".claude/active-plan")
    )
    if os.path.isfile(pointer_file):
        with open(pointer_file) as fh:
            plan_path = fh.readline().strip()
        if plan_path:
            return plan_path, pointer_file

    fallback_globs = config.get("plans.fallback_glob", ["plans/*.md"])
    if isinstance(fallback_globs, str):
        fallback_globs = [fallback_globs]

    candidates: list[str] = []
    for pattern in fallback_globs:
        for match in glob.glob(_anchor(pattern)):
            if os.path.isfile(match):
                candidates.append(match)

    if not candidates:
        return None

    best = max(candidates, key=os.path.getmtime)
    return best, "mtime fallback"
