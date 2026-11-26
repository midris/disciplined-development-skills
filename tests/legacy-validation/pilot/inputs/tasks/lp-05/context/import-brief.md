# Membership roster import

Museum administrators upload a CSV to replace the active membership roster.

Each non-header row has `member_id` and `email`.
`member_id` is the immutable external identity and must be unique within the file and active roster.
The replacement becomes visible only after the entire file succeeds; no partial roster may be visible.
Uploads may be absent, empty, malformed, or as large as two million rows.
Two million rows is the supported maximum; reject larger uploads without changing the active roster.
The operator needs one actionable error report when an import is rejected.

Existing files:

- `src/membership_import.py`
- `tests/test_membership_import.py`
