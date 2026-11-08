from dataclasses import dataclass


@dataclass(frozen=True)
class QuotaChange:
    previous: int
    current: int
    effective_at: int


def quota_for_request(change: QuotaChange, issued_at: int, now: int) -> int:
    """Return a limit for a validated token. All timestamps are in seconds."""
    if now < change.effective_at:
        return change.previous
    return change.current
