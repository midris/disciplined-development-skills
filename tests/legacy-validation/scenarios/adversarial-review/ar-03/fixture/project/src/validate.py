from .normalize import normalize_tasks


def validate_batch(tasks):
    return normalize_tasks(sorted(tasks))
