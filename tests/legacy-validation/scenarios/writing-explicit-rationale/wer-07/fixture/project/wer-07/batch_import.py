def import_approved_batch(batch, persist):
    """Persist a batch only after the batch approval boundary."""
    assert batch.approved
    return persist(batch)
