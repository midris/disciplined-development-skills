def ingest_queue(message, store):
    job_id = message.get("job_id")
    store.record(job_id)
    return job_id
