# Nightly account digest

A scheduled job sends each account at most one digest for each account-local calendar day.
The job reads paginated JSON events from an internal analytics service and sends through an API limited to 100 messages per minute.
The scheduler can start a retry while a prior worker is still running.
A malformed analytics event must not crash the whole job.
One account's fetch or send failure must not prevent other accounts from completing.
Accounts can have no events or millions of events.
Retries must not duplicate a digest.

Existing files:

- `src/nightly_digest.py`
- `tests/test_nightly_digest.py`
