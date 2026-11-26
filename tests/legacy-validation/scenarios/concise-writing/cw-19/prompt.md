You are a fresh, read-only skill evaluator.
Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `{{fixture_dir}}/skills/concise-writing/SKILL.md` completely and follow it as binding guidance.

Tighten this complete cutover runbook without losing any operational requirement. Return only the revised runbook.

## Orders schema cutover

This runbook section explains the orders schema cutover and describes what the release engineer needs to do.

### Preflight and readiness

The release engineer first runs `./bin/schema-cutover preflight --plan orders-v3 --json` and attaches its JSON output to change ticket `CHG-4821`; that output records the pre-cutover snapshot ID. Promotion is ready only when database replica lag is at most 2 seconds and the dual-write mismatch rate is below 0.1% throughout the same uninterrupted 15-minute window. In other words, both metrics must remain within those limits together for one full 15-minute window; one healthy metric is not enough.

If the preflight fails, replica lag rises above 2 seconds, or the dual-write mismatch rate reaches 0.1% or higher before promotion, the release engineer stops and posts `BLOCKED` with a link to `CHG-4821` in `#schema-cutover`, tagging the database incident commander.

### Promotion

After the readiness window passes, the release engineer posts the `CHG-4821` link in `#schema-cutover` and waits for the database incident commander to reply `GO`. Only after that reply does the release engineer run `./bin/schema-cutover promote --plan orders-v3`. The promotion command must not run before the commander replies `GO`.

Do not add `--force` to the promotion command. `--force` skips the readiness and `GO` checks and can expose partially backfilled rows.

### Recovery boundary

The promotion can be rolled back in place only until the application accepts its first write containing a field that exists only in `orders-v3`; that write is the irreversible in-place rollback boundary. After it, do not run `./bin/schema-cutover rollback --plan orders-v3`, because the old schema cannot represent that write. Only the database incident commander—not the release engineer—decides whether to continue forward or restore the pre-cutover snapshot recorded in `CHG-4821`.
