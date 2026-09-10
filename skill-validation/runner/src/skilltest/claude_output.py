"""Extract a final answer without assigning an evidence-validity verdict."""

import json


def final_answer(stdout: bytes) -> bytes | None:
    """Require one successful terminal result; preserve all raw output elsewhere."""
    try:
        events = [json.loads(line) for line in stdout.decode("utf-8").splitlines() if line.strip()]
        if not events or any(not isinstance(event, dict) for event in events):
            return None
        results = [event for event in events if event.get("type") == "result"]
        if len(results) != 1 or events[-1] is not results[0]:
            return None
        result = results[0]
        if result.get("subtype") != "success" or result.get("is_error") is not False:
            return None
        answer = result.get("result")
        return answer.encode("utf-8") if isinstance(answer, str) else None
    except (ValueError, UnicodeError, RecursionError):
        return None
