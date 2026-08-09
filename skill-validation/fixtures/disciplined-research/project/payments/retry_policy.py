MAX_ATTEMPTS = 3
RETRY_DELAYS_SECONDS = (1, 2, 4)


class AuthorizationError(Exception):
    pass


def authorize_with_retries(authorize, sleep):
    """Try an authorization up to MAX_ATTEMPTS times."""
    for attempt in range(MAX_ATTEMPTS):
        try:
            return authorize()
        except AuthorizationError:
            if attempt + 1 == MAX_ATTEMPTS:
                raise
            sleep(RETRY_DELAYS_SECONDS[attempt])
