"""Independent download helper; does not use the delivery worker."""


def fetch(request):
    """Return whether the download succeeded; stop after success."""
    for _ in range(3):
        if request():
            return True
    return False
