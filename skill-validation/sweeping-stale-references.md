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

## Large-sweep grouping (2026-08-01)

**Scenario.** A rename produces 126 inspected matches: 80 updates across 6 files, 40 intentionally stale matches across 2 archives, and 6 false positives across 2 HTTP files.
Ask for the `References swept:` artifact under the repository's normal commit-body preference.

**RED — pre-edit skill: 1/1 FAIL.** The evaluator found the worked example hinted at grouping, but explicit "one line per match" and `path:LINE` rules required roughly 126 entries.
That conflicted with the normal commit-body preference, while splitting the commit would violate one-commit reconciliation.

**GREEN requirements.** Group matches only when they share both path and outcome; retain precise locations and counts; reconcile entry counts to search results; never group across paths or outcomes; and allow a legitimate grouped sweep to exceed the normal preference when correctness evidence still requires it.

**GREEN result: 1/1 PASS.** The evaluator produced 10 path/outcome entries for 126 matches and reconciled them exactly: 80 updates across 6 paths, 40 intentionally stale matches across 2 paths, and 6 false positives across 2 paths.
It kept `Verification:` after the sweep and limited the body-size exception to correctness evidence remaining after grouping.
