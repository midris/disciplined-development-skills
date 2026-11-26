import json


def ingest_file(text, store):
    payload = json.loads(text)
    job_id = str(payload.get("job_id"))[:8]
    store.record(job_id)
    return job_id
