# Interactive ingest architecture

There are two interactive ingest handlers. Each calls shared `persist()` and
must enforce the tenant rate limit. `batch_import.py` is the only other caller
and supplies approved batches. A third interactive caller would require
revisiting the duplicated-guard placement.
