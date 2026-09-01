You are a fresh, read-only skill evaluator.
The complete local skill bundle is supplied beneath `{{fixture_dir}}/skills`, but no project files, active plan, external fact source, or writable target is supplied. Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Invoke `concise-writing` directly: read `{{fixture_dir}}/skills/concise-writing/SKILL.md` completely and follow it as binding guidance.
If the skill cannot complete the task without an unavailable input or another procedure, return `BLOCKED: <missing requirement>` instead of a revision.

Tighten this reader-facing release notice and return only the revised notice:

This release notice explains the new download behavior. Reports are now downloaded as CSV files. CSV downloads preserve the filters currently applied to the report. The downloaded file uses UTF-8 encoding. In other words, whatever filters are active remain active in the CSV that is downloaded. Existing PDF downloads are unchanged. There is no change to PDF download behavior.
