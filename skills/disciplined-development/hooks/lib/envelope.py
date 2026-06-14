"""Exit-0 ``additionalContext`` accumulator + emit helper.

For several hook events, exit-0 plain stdout/stderr is **not** model-visible
— those streams flow only to the debug log. To surface a model-visible
signal on exit 0, the hook must emit a JSON envelope of shape::

    {"hookSpecificOutput": {"hookEventName": "<event>",
                            "additionalContext": "<text>"}}

The ``hookEventName`` must match the hook's own event. Consumers under the
plan emit on different events: ``review_nudge`` (PostToolUse),
``discipline_nudge`` (PreToolUse), ``session_reground`` (SessionStart).
Each constructs its ``Envelope`` with the matching ``event_name``; the
default stays ``"PostToolUse"`` so existing callers are unaffected.

Multi-call accumulator joins segments with a bare ``-----`` separator on
its own line so two co-firing nudges share one envelope without losing
the intended visual break.
"""

from __future__ import annotations

import json
import sys
from typing import TextIO


_SEPARATOR = "\n-----\n"


class Envelope:
    """Accumulate text segments; emit one JSON envelope on demand.

    Empty or whitespace-only segments are dropped at accumulate time so a
    caller computing an empty message can't introduce a phantom separator.

    ``event_name`` stamps the emitted ``hookSpecificOutput.hookEventName``
    so each hook event surfaces with its own name; defaults to
    ``"PostToolUse"`` for backward compatibility with existing callers.
    """

    def __init__(self, event_name: str = "PostToolUse") -> None:
        self._event_name = event_name
        self._segments: list[str] = []

    def accumulate(self, text: str) -> None:
        if text is None or not text.strip():
            return
        self._segments.append(text)

    def emit(self, stream: TextIO | None = None) -> None:
        if not self._segments:
            return
        content = _SEPARATOR.join(self._segments)
        payload = {
            "hookSpecificOutput": {
                "hookEventName": self._event_name,
                "additionalContext": content,
            }
        }
        out = stream if stream is not None else sys.stdout
        # Trailing newline finishes the JSON-line protocol cleanly. If
        # anything else ever writes to the same stream after this envelope
        # (a stray print, a logger flush), the JSON and the trailing text
        # stay separable for the consumer.
        out.write(json.dumps(payload) + "\n")
