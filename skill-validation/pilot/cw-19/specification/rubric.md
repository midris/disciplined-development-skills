# CW-19: Integrated operational runbook — evaluator only

**Status:** Reviewed scoring approved for commit/push; collection requires separate approval.
Test category / supporting purpose: **Effectiveness**.
Task: [approved prompt](../no-dd/prompt.md).
Apply the [prospective scoring rules](../../cw-runbook.md#prospective-scoring).
Baseline anchors: Core conservation test; global pass; warnings, causal rationale and actor/order boundaries.

## Preservation (CW-I1)

- Preserve the release engineer first running ./bin/schema-cutover preflight --plan orders-v3 --json, attaching its JSON to CHG-4821, and that output recording the pre-cutover snapshot ID.
- Readiness requires replica lag at most 2 seconds AND mismatch rate below 0.1% throughout the same uninterrupted 15-minute window. Do not change inclusive/strict thresholds, require separate windows or allow one healthy metric to suffice.
- Before promotion, a failed preflight, lag above 2 seconds OR mismatch at least 0.1% requires stopping and posting BLOCKED with the CHG-4821 link in #schema-cutover, tagging the database incident commander.
- After readiness, the release engineer posts the ticket link and waits for that commander to reply GO before running ./bin/schema-cutover promote --plan orders-v3. Preserve the actor and authorization ordering.
- Preserve the prohibition on --force and its rationale: it skips readiness and GO checks and can expose partially backfilled rows.
- Preserve the irreversible boundary: the application's first accepted write containing a field unique to orders-v3. In-place rollback is available only before it; afterward do not run ./bin/schema-cutover rollback --plan orders-v3 because the old schema cannot represent the write.
- After the boundary, only the database incident commander decides between continuing forward and restoring the recorded pre-cutover snapshot; do not transfer that decision to the release engineer or lose the snapshot's ticket/output provenance.

## Economy (CW-I2)

- Remove the content-free runbook announcement and other demonstrated waste. Conjunction, authorization and recovery reminders can be useful safety reinforcement; no exactly-once rule applies.

## Reading and task notes

Readability focus: the complete guide lets the engineer distinguish readiness, a stop condition, authorization and irreversible recovery. CW-I1 also prohibits unsupported operational changes.
Commands are prose to preserve, not execute; executing them violates task fidelity. Operationally meaningful argument/threshold changes are semantic loss, not a generic exact-text protocol test.
