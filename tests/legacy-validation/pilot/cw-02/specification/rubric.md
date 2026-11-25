# CW-02: Retry scope, rationale and navigation — evaluator only

**Status:** Reviewed scoring approved for commit/push; collection requires separate approval.
Test category / supporting purpose: **Effectiveness**.
Task: [approved prompt](prompt.md).
Apply the [prospective scoring rules](../../cw-runbook.md#prospective-scoring).
Baseline anchors: Core test; anti-over-trimming of rationale, orientation and navigation.

## Preservation (CW-I1)

- Preserve at most three attempts per delivery, not per endpoint, and failure only after the third unsuccessful attempt. Three retries in addition to an initial attempt changes the limit and fails.
- Preserve why per-delivery counting matters: a failing delivery must not exhaust later deliveries' retry budgets. Preserve synchronous retries because downstream acknowledgements must maintain delivery order.
- Preserve queue order within an endpoint: wait for the current delivery to succeed or fail before attempting the next; different endpoints proceed independently. A faster later delivery cannot overtake an earlier retrying delivery for that endpoint.
- An engineer changing retries can find and apply the ordering constraint. The original pointer/headings may change if that navigation or an equally usable integrated explanation survives.

## Economy (CW-I2)

- Remove the content-free section announcement and demonstrated restatement of the attempt limit. A short ordering reminder can aid correct changes; do not require eliminating it merely because the ordering section exists.

## Reading and task notes

Readability focus: the engineer can distinguish the per-delivery budget from the per-endpoint ordering boundary without reconstructing missing relationships.
