"""cleanup.py — best-effort housekeeping for ``.claude/.dd-state/``.

Two sweeps, both degrade-safe (every step → no-op on error; never raises):

- **Logs:** delete rolling ``dd-hooks-*.jsonl`` files in the resolved log dir
  older than ``logging.retention_days``. ``reviews.jsonl`` is the curated
  analysis artifact and is **never** pruned — enforced by the ``dd-hooks-*``
  glob, which excludes it by name (not by relying on its mtime staying fresh,
  which a branch idle past retention would defeat).
- **Orphaned state:** remove per-branch ``.dd-state/<slug>`` dirs whose branch
  no longer exists. Branch validity is checked by enumerating live branches and
  slugging them (slugs aren't reversible) — if branches can't be enumerated,
  nothing is deleted. Dot-prefixed entries (``.logs``, ``.last-sweep``) are
  skipped so they're never mistaken for a branch dir.

Called from ``discipline_nudge`` on its PreToolUse fire branch (count ≥
threshold), throttled by a ``.dd-state/.last-sweep`` stamp so it never runs
on every tool call. ``now_ts`` is injected (the testable core takes no
argless clock).
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from hooks.lib import config, logging_setup, state

_LAST_SWEEP = ".last-sweep"


def _retention_seconds() -> float:
    v = config.get("logging.retention_days", 14)
    if isinstance(v, bool) or not isinstance(v, (int, float)) or v <= 0:
        v = 14
    return float(v) * 86400.0


def _throttle_seconds() -> float:
    v = config.get("logging.sweep_throttle_hours", 24)
    if isinstance(v, bool) or not isinstance(v, (int, float)) or v <= 0:
        v = 24
    return float(v) * 3600.0


def _due(stamp: Path, now_ts: float) -> bool:
    """True if no recent sweep stamp (unreadable/absent stamp → due)."""
    try:
        last = float(stamp.read_text().strip())
    except Exception:
        return True
    return (now_ts - last) >= _throttle_seconds()


def _touch_stamp(stamp: Path, now_ts: float) -> None:
    try:
        stamp.parent.mkdir(parents=True, exist_ok=True)
        stamp.write_text(str(now_ts))
    except Exception:
        pass


def _sweep_logs(now_ts: float) -> None:
    cutoff = _retention_seconds()
    try:
        # Only the rolling per-day files — the `dd-hooks-*.jsonl` glob
        # deliberately excludes `reviews.jsonl` (the curated analysis artifact
        # is never pruned by age; enforced here by the glob, not by relying on
        # its mtime staying fresh).
        entries = list(logging_setup.log_dir().glob("dd-hooks-*.jsonl"))
    except Exception:
        return
    for f in entries:
        try:
            if (now_ts - f.stat().st_mtime) > cutoff:
                f.unlink()
        except Exception:
            pass


def _live_branch_slugs(repo: str) -> set[str] | None:
    """Slugs of every local branch, or None when git can't enumerate (in which
    case the orphan sweep declines to delete — don't remove what you can't
    verify)."""
    try:
        r = subprocess.run(
            ["git", "-C", repo, "for-each-ref",
             "--format=%(refname:short)", "refs/heads/"],
            capture_output=True, text=True, timeout=5,
        )
    except Exception:
        return None
    if r.returncode != 0:
        return None
    return {state.branch_slug(b) for b in r.stdout.split() if b}


def _current_branch_slug(repo: str) -> str | None:
    """Slug of the current branch, or ``"detached"`` on detached HEAD (matching
    how the hooks key state), or None if git is unavailable."""
    try:
        r = subprocess.run(
            ["git", "-C", repo, "symbolic-ref", "--short", "HEAD"],
            capture_output=True, text=True, timeout=5,
        )
    except Exception:
        return None
    return state.branch_slug(r.stdout.strip()) if r.returncode == 0 and r.stdout.strip() else "detached"


def _sweep_orphan_state(repo: str, state_root: Path) -> None:
    live = _live_branch_slugs(repo)
    if live is None:
        return
    # Never delete the current key's dir, incl. the literal "detached" key the
    # hooks use on detached HEAD (which for-each-ref doesn't list) — G4
    # "never the current branch".
    current = _current_branch_slug(repo)
    if current:
        live = live | {current}
    try:
        entries = list(state_root.iterdir())
    except Exception:
        return
    for entry in entries:
        try:
            if (entry.is_dir()
                    and not entry.name.startswith(".")
                    and entry.name not in live):
                shutil.rmtree(entry, ignore_errors=True)
        except Exception:
            pass


def sweep(repo: str, now_ts: float) -> bool:
    """Run the housekeeping sweep unless throttled. Returns True iff it ran.

    Stamp is written before the sweeps so a slow/failed sweep still holds the
    throttle. Best-effort throughout; never raises."""
    try:
        state_root = Path(repo) / ".claude" / ".dd-state"
        stamp = state_root / _LAST_SWEEP
        if not _due(stamp, now_ts):
            return False
        _touch_stamp(stamp, now_ts)
        _sweep_logs(now_ts)
        _sweep_orphan_state(repo, state_root)
        return True
    except Exception:
        return False
