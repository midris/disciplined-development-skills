#!/usr/bin/env python3
"""session_reground.py — re-ground on every session (re)start.

Wired to **SessionStart** only. Stdin carries ``source`` ∈ {startup, resume,
clear, compact}; exit-0 ``additionalContext`` reaches the model. Fires on
EVERY source, emitting a source-specific preamble followed by a shared common
body. Unknown/missing source falls back to a generic preamble and still fires.

``source=compact`` fires *after* compaction, so this is the post-compaction
model reground. PreCompact is deliberately NOT wired: its non-blocking output
cannot reach the post-compaction model (it supports only ``decision: "block"``
+ ``reason``), so it could never deliver a reground — SessionStart(compact)
does. A stale PreCompact wiring degrades to a safe no-op (unknown event).

Env bypass: ``DD_SKIP_SESSION_REGROUND=1`` → silent no-op.
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

HOOK_NAME = "session_reground"

# Source-specific preamble: one sentence that names the context state.
# Unknown/missing source → _FALLBACK_PREAMBLE.
PREAMBLES: dict[str, str] = {
    "startup": "Session start.",
    "resume": "Session resumed — treat this context as a resumed frame, not the original conversation.",
    "clear": "Context cleared — the prior conversation and any loaded skills are gone.",
    "compact": "Post-compaction — this context is a summary of the conversation, not the original.",
}

_FALLBACK_PREAMBLE = "Session (re)started."

# Shared instructions appended after the preamble on every source.
# Leading space joins cleanly to the preamble sentence.
COMMON_BODY = (
    " Before substantive work:\n"
    "  - Re-read CLAUDE.md and the governing docs from disk (and the active plan, incl. progress/checkbox state)"
    " — rely on the files, not recall, and don't claim progress without re-confirming it.\n"
    "  - Re-load your governing skills — disciplined-development and superpowers"
    " (via `using-superpowers`) — plus any others this task needs; don't assume"
    " they survived a long or compacted session.\n"
    "  - For ANY prose you write or edit (chat replies, docs, plans, commit bodies, comments), invoke concise-writing."
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

    if os.environ.get("DD_SKIP_SESSION_REGROUND") == "1":
        logger.emit("skip", reason="env_bypass")
        return 0

    data = _read_payload()
    event = data.get("hook_event_name")

    if event == "SessionStart":
        source = data.get("source")
        preamble = PREAMBLES.get(source, _FALLBACK_PREAMBLE)
        text = preamble + COMMON_BODY
        env = Envelope("SessionStart")
        env.accumulate(text)
        env.emit()
        logger.emit("fire", source=source)
        return 0

    # Unknown / missing event: degrade silent (never block a session start).
    logger.emit("skip", reason="unknown_event", event=event)
    return 0


if __name__ == "__main__":
    sys.exit(main())
