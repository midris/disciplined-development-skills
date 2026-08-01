# Sweeping stale references — validation

Retroactive validation record added 2026-08-01.
The skill predates this repository's validation-record discipline, so this file does not claim the original skill was built from a watched RED.
It records a reproducible control/current comparison for the behavior that justifies the live contract.

**Dispatch protocol.** Read-only and bounded per CLAUDE.md's evaluation-subagent rule.
One scenario per agent, text-only.

## Reviewer reports one stale rename

**Scenario.** A branch renamed configuration key `cache_ttl` to `max_age`.
A reviewer reports only one stale README line, while the repository may also contain code callsites, tests/fixtures, config or CI scripts, prose synonyms, an intentionally historical archived migration, and an unrelated HTTP `max-age` field.
Ask exactly what happens before commit and what commit-body evidence is produced.

**PASS criteria.** Treat the cited line as one sampled class member; search the literal old form and likely synonyms across code, docs, tests, fixtures, config, scripts, CI, and build files; classify every match as `update`, `false positive: <reason>`, or `intentionally stale: <reason>`; reconcile all updates together; and put a match-complete `References swept:` section before `Verification:`.

**RED control — no skill (2026-08-01): partial behavior, contract absent.**
The evaluator independently searched exact forms, variants, synonyms, code, docs, tests, config, CI, archives, and replacement context.
It also distinguished historical and HTTP cases.
It failed the durable contract: its commit artifact used a generic `Evidence:` section, did not apply the three required outcome labels to every match, and did not provide the required `References swept:` placement before `Verification:`.

**GREEN — live skill (2026-08-01): 1/1 PASS.**
The evaluator treated the README finding as a sample, searched every required location and synonym class, assigned one required outcome to every match, reconciled all updates in one commit, and emitted a complete `References swept:` section followed by `Verification:`.
It explicitly preserved the archived migration as intentionally stale and classified HTTP `max-age` as a false positive with reasons.

## On edits

Re-run this control/current scenario before changing the search scope, match classifications, one-commit reconciliation rule, or commit-body artifact.
Add a separate watched RED/GREEN cell before introducing any new behavioral rule.
