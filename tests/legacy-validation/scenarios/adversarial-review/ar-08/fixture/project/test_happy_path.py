def test_api_records_job_id(store, valid_payload):
    assert ingest_api(valid_payload, store) == valid_payload["job_id"]
