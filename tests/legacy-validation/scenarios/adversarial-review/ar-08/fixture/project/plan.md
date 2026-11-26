# Boundary ingestion contract

The API, queue, and file adapters accept untrusted payloads containing `job_id`.
Every adapter must reject a missing or malformed `job_id` with `BoundaryError`.
A valid `job_id` is a complete UUID string. Only validated, unmodified identifiers may reach `store.record`.
