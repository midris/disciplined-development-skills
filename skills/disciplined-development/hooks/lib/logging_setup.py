"""Structured JSONL logging for every Python hook.

Each hook calls :func:`setup` once at start, gets back a :class:`HookLogger`,
and calls ``logger.emit(event, **extra)`` at decision boundaries (invocation
start, decision/outcome, exit reason). Records append to a **rolling per-day**
file ``<log-dir>/dd-hooks-YYYYMMDD.jsonl`` — every hook's records interleave
there, one JSONL line per record, distinguished by the ``hook``/``pid`` fields.

Observability is on by default and comprehensive (see the spec's
"Observability (non-negotiable)" section); volume is managed by retention +
cleanup, not by logging less. ``logging.enabled=false`` (config) is the master
off switch.

Log directory resolution (highest precedence first):
  1. ``DD_LOG_DIR`` env — ops/test override (also how tests isolate logs).
  2. ``logging.dir`` (config / ``dd-config.json``).
  3. consumer ``<project-root>/.claude/.dd-state/.logs`` — project root from
     ``CLAUDE_PROJECT_DIR`` (set by the agent harness) or cwd. Symlink-safe:
     resolves correctly when the hooks package is reached through a symlink,
     where the module's own resolved path lands in the bundle clone (no
     ``.claude`` ancestor) and step 4 would otherwise fall through to ``/tmp``.
  4. derived ``<.claude>/.dd-state/.logs`` — walk up from this module to the
     nearest ``.claude`` ancestor. In-tree fallback for non-symlink layouts
     where the hooks live under the consumer's own ``.claude`` and neither the
     env var nor cwd points at the project root.
  5. ``/tmp/dd-hooks`` fallback (none of the above resolved).

The record's ``ts`` field is full ISO-8601 with millisecond precision so
consumers can order events emitted within the same second.

Accepted edges (review P3s, 2026-05-30):
- **Midnight rollover.** ``setup()`` bakes the day stamp into the path once,
  so a hook still running across UTC midnight keeps appending to the
  start-day file. Accepted: hook lifetimes are short and the ``ts`` field
  orders records regardless; per-``emit`` re-resolution isn't worth the
  file-handle churn.
- **Concurrent appends >PIPE_BUF.** ``open(path, "a")`` is byte-atomic per
  ``write`` only up to PIPE_BUF (~4 KB); ``append_review`` records embed the
  full reviewer output (multi-KB), so two reviewers running concurrently
  (different branches/worktrees) into the same file could interleave.
  Accepted: advisory logs, concurrent cross-worktree review is rare, and the
  loss is at most a garbled line — not worth an OS advisory lock here.
"""

from __future__ import annotations

import datetime
import json
import os
import sys
from pathlib import Path
from typing import Any

from hooks.lib import config

# Fields the writer owns. Any caller-supplied ``extra`` key that collides
# with one of these is dropped (with a stderr warning) so observability
# identifiers can't be silently shadowed by a buggy caller.
_RESERVED_FIELDS = frozenset({"ts", "level", "event", "hook", "pid", "msg"})

_FALLBACK_DIR = Path("/tmp/dd-hooks")
REVIEW_LOG_FILENAME = "reviews.jsonl"


def _day() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d")


def _iso_ts() -> str:
    """ISO-8601 UTC timestamp with millisecond precision (``...SS.mmmZ``)."""
    now = datetime.datetime.now(datetime.timezone.utc)
    return now.strftime("%Y-%m-%dT%H:%M:%S.") + f"{now.microsecond // 1000:03d}Z"


def _claude_logs_dir(start: Path) -> Path | None:
    """Return ``<.claude>/.dd-state/.logs`` by walking up from ``start`` to the
    nearest ``.claude`` ancestor, or None when there is none."""
    for parent in start.parents:
        if parent.name == ".claude":
            return parent / ".dd-state" / ".logs"
    return None


def _consumer_logs_dir() -> Path | None:
    """``<project-root>/.claude/.dd-state/.logs`` from ``CLAUDE_PROJECT_DIR``
    (set by the agent harness) or cwd — whichever points at a dir that holds a
    ``.claude``. Symlink-safe, unlike :func:`_claude_logs_dir`: when the hooks
    package is reached through a symlink, ``__file__`` resolves into the bundle
    clone (no ``.claude`` ancestor) but the project root still has one. None
    when neither candidate has a ``.claude`` dir."""
    root = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    claude = Path(root) / ".claude"
    return claude / ".dd-state" / ".logs" if claude.is_dir() else None


def _resolve_log_dir() -> Path:
    """Resolve the log directory per the precedence in the module docstring."""
    env_dir = os.environ.get("DD_LOG_DIR")
    if env_dir:
        return Path(env_dir)
    cfg_dir = config.get("logging.dir")
    if isinstance(cfg_dir, str) and cfg_dir:
        return Path(cfg_dir)
    consumer = _consumer_logs_dir()
    if consumer is not None:
        return consumer
    derived = _claude_logs_dir(Path(__file__).resolve())
    return derived if derived is not None else _FALLBACK_DIR


def _logging_enabled() -> bool:
    """True unless ``logging.enabled`` is explicitly JSON ``false``."""
    return config.get("logging.enabled", True) is not False


class HookLogger:
    """Append-only JSONL writer. One instance per hook process.

    Never raises on any emit failure — hooks must not crash because the log
    directory is unwritable, the record is unserializable, or the caller passed
    a reserved kwarg. Failures go to stderr with a ``[logging_setup] WARNING:``
    prefix; the hook process always continues. When ``log_path`` is None
    (logging disabled), ``emit`` is a no-op.
    """

    def __init__(self, hook: str, log_path: Path | None):
        self.hook = hook
        self.log_path = log_path
        self.pid = os.getpid()

    def emit(self, event: str | None = None, /, *, level: str = "info",
             msg: str = "", **extra) -> None:
        if self.log_path is None:
            return  # logging disabled (logging.enabled=false)
        # ``event`` is positional-only with a default so all three call forms
        # work without a "multiple values for 'event'" TypeError:
        #   emit("done") / emit(event="done") / emit("done", **payload)
        if event is None and "event" in extra:
            event = extra.pop("event")
        if event is None:
            event = "(unspecified)"
        clobbered = [k for k in extra if k in _RESERVED_FIELDS]
        if clobbered:
            print(
                f"[logging_setup] WARNING: hook={self.hook!r} attempted to set "
                f"reserved field(s) via extra: {clobbered}; dropping.",
                file=sys.stderr,
            )
            extra = {k: v for k, v in extra.items() if k not in _RESERVED_FIELDS}
        record: dict[str, Any] = {
            "ts": _iso_ts(),
            "level": level,
            "event": event,
            "hook": self.hook,
            "pid": self.pid,
            "msg": msg,
        }
        record.update(extra)
        try:
            # ``default=str`` coerces non-JSON values (Path, datetime) instead
            # of raising; the broad except is belt-and-suspenders so logging
            # never blocks the hook.
            line = json.dumps(record, default=str) + "\n"
            with open(self.log_path, "a") as fh:
                fh.write(line)
        except (OSError, TypeError, ValueError) as exc:
            print(
                f"[logging_setup] WARNING: hook={self.hook!r} could not write "
                f"record: {type(exc).__name__}: {exc}",
                file=sys.stderr,
            )


def log_dir() -> Path:
    """The resolved log directory (see :func:`setup`'s resolution order).
    Public so ``cleanup`` can prune this dir."""
    return _resolve_log_dir()


def append_review(record: dict) -> None:
    """Append one curated review record to ``<log-dir>/reviews.jsonl``.

    The dedicated review trace for offline analysis (outcomes, latency,
    drift) — see the spec's "Observability" section. Multi-source: ``source:
    external-gate`` rows from the pre-PR codex gate (``external_review.py``)
    and ``source: model-review`` rows from model-driven reviews
    (``log_review.py``); rows are sparse
    (each source carries only the fields it has). Resolves the same dir as
    :func:`setup`, honors ``logging.enabled`` (no-op when false), stamps a
    ``ts``, and never raises (a write failure warns to stderr only)."""
    if not _logging_enabled():
        return
    base = _resolve_log_dir()
    try:
        base.mkdir(parents=True, exist_ok=True)
        line = json.dumps({"ts": _iso_ts(), **record}, default=str) + "\n"
        with open(base / REVIEW_LOG_FILENAME, "a") as fh:
            fh.write(line)
    except (OSError, TypeError, ValueError) as exc:
        print(
            f"[logging_setup] WARNING: could not write review record: "
            f"{type(exc).__name__}: {exc}",
            file=sys.stderr,
        )


def setup(hook: str, log_dir: os.PathLike | str | None = None) -> HookLogger:
    """Return a logger for ``hook`` writing to the rolling per-day file.

    ``log_dir`` (explicit) overrides resolution — used by tests. When omitted,
    the dir is resolved per the module docstring. When ``logging.enabled`` is
    false the returned logger has ``log_path=None`` (emit no-ops).
    """
    if not _logging_enabled():
        return HookLogger(hook, None)
    base = Path(log_dir) if log_dir is not None else _resolve_log_dir()
    try:
        base.mkdir(parents=True, exist_ok=True)
    except OSError:
        # An unwritable base is non-fatal — emit will warn-and-continue when
        # the open fails. (Returning a real path keeps the contract simple.)
        pass
    return HookLogger(hook, base / f"dd-hooks-{_day()}.jsonl")
