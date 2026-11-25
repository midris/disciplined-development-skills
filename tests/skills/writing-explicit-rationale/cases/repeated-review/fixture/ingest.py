def persist(store, item):
    store.append(item)


def ingest(store, item, allowed):
    if not allowed:
        raise PermissionError("interactive limit reached")
    persist(store, item)


def admin_ingest(store, item, allowed):
    if not allowed:
        raise PermissionError("interactive limit reached")
    persist(store, item)


def import_approved_batch(store, items):
    for item in items:
        persist(store, item)
