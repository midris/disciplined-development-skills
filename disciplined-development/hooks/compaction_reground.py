#!/usr/bin/env python3
"""compaction_reground.py — re-ground after context loss/summarization.

Wired to **SessionStart** only. Stdin carries ``source`` ∈ {startup, resume,
clear, compact}; exit-0 ``additionalContext`` reaches the model. Fire on
``resume``/``compact`` (the context is a resumed/summarized frame — re-read the
source of truth). Stay **silent** on ``startup`` and ``clear``: both leave
project context (CLAUDE.md, the active plan) freshly present, so the "context
is now a summary" reminder would be inaccurate and noisy.

``source=compact`` fires *after* compaction, so this is the post-compaction
model reground. PreCompact is deliberately NOT wired: its non-blocking output
cannot reach the post-compaction model (it supports only ``decision: "block"``
+ ``reason``), so it could never deliver a reground — SessionStart(compact)
does. A stale PreCompact wiring degrades to a safe no-op (unknown event).

Env bypass: ``DD_SKIP_COMPACTION_REGROUND=1`` → silent no-op.
"""

from __future__ import annotations

import json
import os
import pathlib
import sys

_HERE = pathlib.Path(__file__).resolve().parent
_BASE_DIR = _HERE.parent  # the dir containing the `hooks` package
if str(_BASE_DIR) not in sys.path:
    sys.path.insert(0, str(_BASE_DIR))

from hooks.lib import logging_setup  # noqa: E402
from hooks.lib.envelope import Envelope  # noqa: E402

HOOK_NAME = "compaction_reground"

# SessionStart sources that mean "the context is a resumed/summarized frame."
_FIRE_SOURCES = {"resume", "compact"}

REGROUND_TEXT = (
    "Re-ground after compaction/resume — the context here is a summary or a "
    "resumed frame, not the original conversation. Before acting:\n"
    "  - Re-read CLAUDE.md and the active plan from disk; don't trust the "
    "pre-compaction frame.\n"
    "  - Re-invoke the governing skills for the work in flight "
    "(disciplined-development + the companion skills its gates name).\n"
    "  - Confirm the current step against the plan's checkboxes before "
    "claiming progress."
)


def _read_payload() -> dict:
    """Return the stdin JSON payload as a dict; {} on any failure."""
    try:
        raw = sys.stdin.read()
    except Exception:
        return {}
    if not raw:
        return {}
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


def main() -> int:
    logger = logging_setup.setup(HOOK_NAME)

    if os.environ.get("DD_SKIP_COMPACTION_REGROUND") == "1":
        logger.emit("skip", reason="env_bypass")
        return 0

    data = _read_payload()
    event = data.get("hook_event_name")

    if event == "SessionStart":
        source = data.get("source")
        if source in _FIRE_SOURCES:
            env = Envelope("SessionStart")
            env.accumulate(REGROUND_TEXT)
            env.emit()
            logger.emit("fire", source=source)
        else:
            logger.emit("skip", reason="cold_source", source=source)
        return 0

    # Unknown / missing event: degrade silent (never block a session start).
    logger.emit("skip", reason="unknown_event", event=event)
    return 0


if __name__ == "__main__":
    sys.exit(main())
