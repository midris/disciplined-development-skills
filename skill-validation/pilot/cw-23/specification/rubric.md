# CW-23: prose edit with reference reconciliation — evaluator only

**Status:** Reviewed scoring approved for commit/push; collection requires separate approval.
Test category / supporting purpose: **Composition**.
Task: [approved prompt](prompt.md), [restart guide](fixture/docs/restarting.md), [README](fixture/README.md), [incident guide](fixture/docs/incidents.md).
Apply the [prospective scoring rules](../../cw-runbook.md#prospective-scoring).
Baseline anchors: CW core test, compression pass, navigation guard and Pairing; [SSR](../../../../skills/sweeping-stale-references/SKILL.md)'s Search / Triage / Reconcile and durable accounting, from the declared baseline source.

## Preservation (CW-I1)

- Preserve both pre-restart conditions: no new jobs accepted AND zero active jobs, with the reason an empty queue alone is insufficient. Restart only the worker assigned to the incident.
- Preserve recording worker ID and incident ID before restart and the reason connecting that action to the investigation.
- Preserve checking health before resuming intake, leaving intake paused and paging the service owner when unhealthy, and the prohibition on compensating with a second worker because it may have active jobs. Add no unsupported policy.

## Economy (CW-I2)

- Remove content-free guide/section announcements and demonstrated restatement while retaining useful safety emphasis and explanations. The requested section merge does not itself prove successful concision.

## Reference reconciliation (SSR-I1–I4)

- (SSR-I1) The full trace demonstrates a search before changing the referenced headings, covering their old names/fragments and relevant sibling references across the fixture. Finding only the edited heading without inspecting its consumers is insufficient. Inspect the resulting state to establish reconciliation; a claimed search alone fails with a complete trace showing none.
- (SSR-I2) Disposition the changed declarations and real consumers, plus any returned false-positive or intentionally preserved matches. The supplied inbound consumers are README's before-restarting link and both before-restarting/final-check links in docs/incidents.md. No extra negative-case quota applies.
- (SSR-I3) Project links still reach the intended instructions after the section merge. Reconcile all affected project documents in one actual local root commit; prose promising a later sweep/commit does not pass. Inspect the committed tree independently.
- (SSR-I4) The commit carries truthful, reconcilable sweep accounting: affected paths, outcomes, precise locations and counts matching the observed search/inventory, with preserved matches explained where present. Verify its claims against the trace and file states; a commit ID or generic “references checked” alone is insufficient.

## Reading and task notes

Readability focus: the on-call developer can follow checks, logging, restart and recovery in order and reach the guide from either entry point.
Record broken navigation as the SSR outcome above and cross-reference its CW reader consequence; do not count it as a second independent defect.
Equivalent working navigation, including valid preserved anchors, is acceptable if the requested section merge and reader function remain; do not demand one rewriting tactic.

The runtime starts with an empty Git repository. Inspect staged originals/pre-restaging diff and frozen input files for comparison; HEAD^ does not exist after the single root commit.
The final commit must contain the three project documents, with installed skills and project guidance preserved and excluded. A narration-only result cannot establish executed composition.
Fidelity: merge the two sections under the requested heading, stage originals before edits, inspect the requested diff, use the command-local test identity, respect allowed paths, and stop before PR/publication/service operations or external-review claims.
Equivalent heading wording with correct navigation is a fidelity difference, not an SSR semantic failure. If no section/anchor change occurs, record that the intended reference-change interaction was not exercised; that condition is not judgeable as successful composition.
SSR's References swept heading, label spelling, grouping presentation and placement before Verification are fidelity to its output convention; absent or false substantive accounting fails SSR-I4. No authenticated parser makes the heading a deterministic-protocol gate.
