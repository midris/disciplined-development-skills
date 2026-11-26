from datetime import timedelta

ARCHIVE_DAYS = 45


def archive_cutoff(now):
    """Return the oldest archive timestamp retained by the active cleanup job."""
    return now - timedelta(days=ARCHIVE_DAYS)
