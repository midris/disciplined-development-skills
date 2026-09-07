from .normalize import normalize_tasks


def bulk_normalize(tasks):
    return normalize_tasks(sorted(tasks))
