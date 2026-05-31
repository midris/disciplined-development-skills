"""Dumb per-branch state for DD hooks: counters, review checkpoint, fork base.

State lives under ``<repo>/.claude/.dd-state/<branch-slug>/``:

- ``<name>.count`` — a plain integer counter file (e.g. ``edits.count``).
- ``review.checkpoint`` — a single line holding the commit SHA at last review.

There are no schemas, no JSON, and no locking — last-write-wins. Writes are
atomic (temp file + ``os.replace``). This module is *advisory bookkeeping*: every
read, write, and git call degrades to a safe default (no-op / 0 / None) on any
error. An exception must never escape and crash a hook.

Stale-checkpoint detection uses ``git merge-base --is-ancestor`` rather than the
exit code of ``git rev-list --count``. After ``git commit --amend`` the old
commit object is still reachable via reflog, so ``rev-list --count <old>..HEAD``
exits 0 with a *wrong positive* count; only ``--is-ancestor`` correctly reports
the old SHA as no longer an ancestor. (Verified empirically — see plan Task A4.)
"""

from __future__ import annotations

import os
import re
import subprocess
import tempfile
from pathlib import Path

STATE_DIRNAME = ".dd-state"
CHECKPOINT_FILENAME = "review.checkpoint"
COUNT_SUFFIX = ".count"


def _state_root(repo: str | Path) -> Path:
    return Path(repo) / ".claude" / STATE_DIRNAME


def _branch_slug(branch: str) -> str:
    """Filesystem-safe slug for a branch name (slashes and friends -> '_')."""
    return re.sub(r"[^A-Za-z0-9._-]", "_", branch)


def branch_slug(branch: str) -> str:
    """Public alias for :func:`_branch_slug` — used by ``cleanup`` to match
    per-branch state dir names against the set of live branches."""
    return _branch_slug(branch)


def _branch_dir(repo: str | Path, branch: str) -> Path:
    return _state_root(repo) / _branch_slug(branch)


def _atomic_write(path: Path, content: str) -> None:
    """Write ``content`` to ``path`` atomically; swallow all errors."""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=".tmp-")
        try:
            try:
                fh = os.fdopen(fd, "w")
            except Exception:
                # fdopen didn't adopt the fd (EMFILE/OOM territory) — close it
                # ourselves so it doesn't leak, then fall to the tmp cleanup.
                os.close(fd)
                raise
            with fh:
                fh.write(content)
            os.replace(tmp, path)
        except Exception:
            # Best-effort tmp cleanup; outer except will swallow either way.
            try:
                os.unlink(tmp)
            except OSError:
                pass
    except Exception:
        # Advisory state: never propagate a write failure.
        pass


# --- counters --------------------------------------------------------------


def _count_path(repo: str | Path, branch: str, name: str) -> Path:
    return _branch_dir(repo, branch) / f"{name}{COUNT_SUFFIX}"


def read(repo: str | Path, branch: str, name: str) -> int:
    """Return the counter value, or 0 if absent / unreadable / corrupt."""
    try:
        text = _count_path(repo, branch, name).read_text().strip()
        return int(text)
    except Exception:
        return 0


def bump(repo: str | Path, branch: str, name: str) -> int:
    """Increment the counter (creating it at 1) and return the new value.

    On write failure the in-memory new value is still returned so the caller's
    decision logic stays coherent; persistence is best-effort.
    """
    new_value = read(repo, branch, name) + 1
    _atomic_write(_count_path(repo, branch, name), str(new_value))
    return new_value


def reset(repo: str | Path, branch: str, name: str) -> None:
    """Reset the counter to zero by removing its file; swallow all errors."""
    try:
        _count_path(repo, branch, name).unlink(missing_ok=True)
    except Exception:
        pass


# --- checkpoint ------------------------------------------------------------


def _checkpoint_path(repo: str | Path, branch: str) -> Path:
    return _branch_dir(repo, branch) / CHECKPOINT_FILENAME


def set_checkpoint(repo: str | Path, branch: str, sha: str) -> None:
    """Record ``sha`` as the review checkpoint for ``branch``."""
    _atomic_write(_checkpoint_path(repo, branch), sha.strip())


def _read_checkpoint(repo: str | Path, branch: str) -> str | None:
    try:
        text = _checkpoint_path(repo, branch).read_text().strip()
        return text or None
    except Exception:
        return None


# --- git helpers -----------------------------------------------------------


def _git(repo: str | Path, *args: str) -> subprocess.CompletedProcess | None:
    """Run a git command in ``repo``; return the completed process or None.

    Returns None only when the subprocess itself could not run (git missing,
    bad path). A non-zero exit is returned as a normal CompletedProcess so
    callers can branch on ``returncode``.
    """
    try:
        return subprocess.run(
            ["git", "-C", str(repo), *args],
            capture_output=True,
            text=True,
            check=False,
            # review_nudge calls this on every PostToolUse Bash; a stuck git
            # (index.lock, fsmonitor, slow NFS) must time out, not hang the
            # hook. TimeoutExpired is swallowed below → None (degrade-safe).
            timeout=5,
        )
    except Exception:
        return None


def commits_since_checkpoint(repo: str | Path, branch: str) -> int | None:
    """Commits on HEAD since the recorded checkpoint, or None.

    None when: no checkpoint is recorded; the recorded SHA is not an ancestor of
    HEAD (amended-away or a sibling branch); the SHA is unresolvable (bogus); or
    git is unavailable. Only an ancestor SHA yields a count.
    """
    sha = _read_checkpoint(repo, branch)
    if not sha:
        return None

    ancestor = _git(repo, "merge-base", "--is-ancestor", sha, "HEAD")
    if ancestor is None or ancestor.returncode != 0:
        # exit 1 = not an ancestor (amended-away / sibling); 128 = bogus sha.
        return None

    counted = _git(repo, "rev-list", "--count", f"{sha}..HEAD")
    if counted is None or counted.returncode != 0:
        return None
    try:
        return int(counted.stdout.strip())
    except (ValueError, AttributeError):
        return None


# --- fork base -------------------------------------------------------------


def resolve_fork_base(
    repo: str | Path, trunk_branches: list[str]
) -> str | None:
    """Merge-base of HEAD and the first resolvable trunk ref, or None.

    Iterates ``trunk_branches`` in order, skipping refs that don't resolve, and
    returns the merge-base against the first one that does. None when no trunk
    ref exists, no merge-base exists, or git is unavailable.
    """
    for trunk in trunk_branches:
        # Skip refs that don't resolve in this repo.
        resolved = _git(repo, "rev-parse", "--verify", "--quiet", f"{trunk}^{{commit}}")
        if resolved is None or resolved.returncode != 0:
            continue
        base = _git(repo, "merge-base", "HEAD", trunk)
        if base is None or base.returncode != 0:
            continue
        sha = base.stdout.strip()
        if sha:
            return sha
    return None


def commits_since_fork_base(
    repo: str | Path, trunk_branches: list[str]
) -> int | None:
    """Commits on HEAD since the fork base, or None when there is no fork base."""
    base = resolve_fork_base(repo, trunk_branches)
    if base is None:
        return None
    counted = _git(repo, "rev-list", "--count", f"{base}..HEAD")
    if counted is None or counted.returncode != 0:
        return None
    try:
        return int(counted.stdout.strip())
    except (ValueError, AttributeError):
        return None
