MAX_ATTEMPTS = 3
RETRY_DELAYS_SECONDS = (1, 2, 4)


def retry_delays():
    """Return the delay scheduled after each failed authorization attempt."""
    return RETRY_DELAYS_SECONDS
