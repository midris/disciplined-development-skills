# Mechanical study tools: review and qualification

Scope: [active plan](../plans/2026-09-11-model-driven-skill-testing.md), [tool contract](../plans/specs/2026-09-18-study-mechanical-tools.md), governing framework, document schemas/validators, runner metadata producer, tests and operating guidance.
Review method: active-session adversarial self-review, including consistency, executability and durability; no independent reviewer or subject invocation.

Follow-up: the [owner-requested review](2026-09-18-study-tools-followup-review.md) found and resolved four additional boundary defects after this initial review.

## Findings resolved

- Input-boundary handling: malformed preparation manifests and non-object runner metadata could escape as tracebacks. The CLI now reports failure; preparation accepts fully specified draft cases while frozen checks retain their existing requirements.
- Existing-state preservation: an empty existing index was mistaken for an absent index. It is now rejected without replacement. Duplicate runs/slots, copy failure, source mutation and index-write failure are covered; failures cannot silently register or adopt a partial bundle.
- Permission preservation: staging inherited a read-only root mode, preventing publication of its children. Only the disposable staging root is made writable for the move; the retained root receives the original mode.
- Scoring consistency: aggregation checks criterion and policy identities before pooling, including policies that reuse the same criterion IDs. Invalid/unresolved setups, unassessed attempts and unattempted slots remain visible outside valid-setup outcome counts.

The sweep covered source/destination/index boundaries, terminal metadata/charge, hidden files and symlinks, draft/frozen identities, controller separation, paired differences, partial coverage and output publication.
The final reread found no unresolved blocking issues.
Accepted limits: supported initial-attempt/no-retry scopes, caller responsibility to await runner exit, explicit inspection after interrupted publication, full-file UTF-8 length measurement and model-owned semantic judgments.
Preservation verifies one copy; it does not create or certify a separate backup.

## Verification

- New CLI contracts were tested before implementation; preservation and review regressions were observed failing before their fixes.
- Final focused document suite: 101 passed, including 37 new mechanical-operation cases.
- Full offline runner suite: 412 passed. Hook suite: 263 passed, three existing skips. Format suite: nine passed.
- Actual `skilltest docs retain` on disposable Git/evidence fixtures produced a verified index; `docs check` reported valid structure and the expected unassessed-result limitation.
- Actual `docs tables` against retained CW comparison evidence reproduced all recorded counts and all eight source/output word counts. Output was written only to scratch.
- Actual manifest preparation accepted the declared original/candidate skill-only difference; protocol preparation and a disposable committed-input freeze/check passed. Both CW batches still pass assessment readiness after the process updates. No historical manifest, result, source, score or raw bundle was changed.
- Documentation/reference sweep covered the CLI guide, format guide, architecture, governing spec, active plan, accounting and handoff. The handoff now routes to canonical state instead of repeating results.

No findings.

DD-VERDICT: PASS
