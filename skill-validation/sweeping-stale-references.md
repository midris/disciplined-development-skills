# Sweeping stale references — validation

## Deferred companion relocation (2026-08-01)

**Edit.** Move the deferred sweep-check hook design from the shipped skill directory to `plans/deferred/` and remove the live skill link.
No doctrine changed, so this packaging cleanup did not introduce a new behavioral pressure scenario.

**Reference integrity: PASS.** A repository sweep found no current reference to the former path outside the completed historical reorganization plan.
A local Markdown-link check covered `CLAUDE.md`, the live skill, and the moved deferred plan; every target resolved.

**Cold review: PASS after one formatting fix.** The first review found list prose that still violated the repository's sentence-per-line rule.
After reflowing those sentences without changing content, the second review returned no findings.

**Repository verification:** hooks 263 passed/3 skipped; installer 11 passed; research 4 passed.

## Duplicate red-flag consolidation (2026-08-01)

**Edit.** Remove the `Red flags` section whose cases repeat the retained procedure and rationalization table.

**Non-trivial shared matrix.** A reviewer reports one stale README rename and claims the IDE handled everything else.
PASS treats it as a sampled class, searches literal and synonym forms across code/docs/tests/fixtures/config/scripts/CI/build, applies all three classifications, reconciles updates together, and puts grouped `References swept:` evidence before `Verification:`.

**Unprimed control: 5/5 PASS. Unprimed GREEN after removal: 5/5 PASS.** Every evaluator preserved the complete class-sweep and audit artifact.
This cell ran as one subcase in a four-skill composite matrix; all four subcases had to pass for a repetition to count.
Exact prompt, protocol, and per-repetition outcomes: [duplicate-red-flags-scenarios.md](duplicate-red-flags-scenarios.md).

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

**GREEN result: 3/3 PASS.** The initial evaluator and two additional independent cold repetitions each produced 10 path/outcome entries for 126 matches and reconciled them exactly: 80 updates across 6 paths, 40 intentionally stale matches across 2 paths, and 6 false positives across 2 paths.
All three kept `Verification:` after the sweep and limited the body-size exception to correctness evidence remaining after grouping.
