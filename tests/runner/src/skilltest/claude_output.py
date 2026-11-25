"""Extract a final answer without assigning an evidence-validity verdict."""

import json


def final_answer(stdout: bytes) -> bytes | None:
    """Require one successful result with only background bookkeeping after it."""
    try:
        events = [json.loads(line) for line in stdout.decode("utf-8").splitlines() if line.strip()]
        if not events or any(not isinstance(event, dict) for event in events):
            return None
        results = [event for event in events if event.get("type") == "result"]
        if len(results) != 1:
            return None
        result = results[0]
        trailing = events[events.index(result) + 1:]
        if any(event.get("type") != "system"
               or not isinstance(event.get("subtype"), str)
               or event["subtype"] not in {
            "background_tasks_changed", "task_updated", "task_notification",
        } for event in trailing):
            return None
        if result.get("subtype") != "success" or result.get("is_error") is not False:
            return None
        answer = result.get("result")
        return answer.encode("utf-8") if isinstance(answer, str) else None
    except (ValueError, UnicodeError, RecursionError):
        return None
