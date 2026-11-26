def ingest_api(payload, store):
    job_id = payload["job_id"]
    store.record(job_id)
    return job_id
