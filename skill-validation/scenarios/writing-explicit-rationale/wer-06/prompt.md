You are a fresh, read-only skill evaluator.
Only `writing-explicit-rationale` and this task context are available. Do not edit files, change state, inspect anything outside the supplied bundle, or dispatch agents.
Read `supplied-skills/writing-explicit-rationale/SKILL.md` completely and follow it as binding guidance.

The serializer at `src/archive.py:41` preserves leading zeroes in legacy numeric strings instead of normalizing them because archived records are signature-verified against their exact serialized bytes. Normalization would invalidate those signatures.
The team first encountered the issue during a 2019 migration, and the importer used for that migration was written in Perl. The migration year and implementation language do not affect current correctness or any future implementation choice.

Return only the exact code comment to place above the serialization branch.
