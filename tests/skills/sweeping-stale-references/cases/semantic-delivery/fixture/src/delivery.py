"""Notification delivery through a caller-supplied boolean sender."""


def deliver(send):
    """Return whether delivery succeeded; stop calling send after success."""
    for _ in range(4):
        if send():
            return True
    return False
