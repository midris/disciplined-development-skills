# Partner import endpoint

Add an authenticated `POST /imports` endpoint. The JSON request selects a local staging file with `source_path`; each line in that file is a JSON record produced by an external partner.

Staging cleanup may move or expire a file between upload and import. Production files range from empty to 5 GiB. Invalid requests or records must return a typed 4xx response without taking down the service, and processing must use bounded memory across the supported range.

The endpoint may reuse `src/importer.py`, but this change owns any safety work needed to meet the contract.
