# The token TTL stays at 30 minutes because the partner rejects longer sessions.
# This accepts more frequent refreshes to preserve partner compatibility.
def expires_at(started_at, settings):
    minutes = settings['token_ttl_minutes']
    if minutes <= 0:
        raise ValueError('duration must be positive')
    return started_at + minutes * 60
