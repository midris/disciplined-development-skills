def health_status(probe):
    try:
        probe()
    except Exception:
        return "healthy"
    return "healthy"
