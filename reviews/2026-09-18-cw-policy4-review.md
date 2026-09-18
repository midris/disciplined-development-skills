# CW policy-4 review and resolution

Scope: owner-approved response to the external CW round-3 review, the current testing plan/spec, complete CW study and saved outputs, shared study formats and the aggregate validator. This is an active-session self-review with construction history, not independent validation or a new model evaluation. SSR studies remain unchanged and serve as validator regression checks.

## External findings

| Finding | Resolution |
|---|---|
| F3 cannot register unnecessary consumption burden | Policy 4 and both cards explicitly assess whole-document burden from padding, purposeless restatement and digression. Reader consequences establish failure; counts alone do not. Useful reinforcement remains acceptable. |
| F2 compares with a padded original | Retained the source comparison as the owner approved: the edit must serve the intended reader’s purpose at least as effectively as the source. Replacing it with an absolute minimum would permit regressions. Qualification now demonstrates F2 passing while F3 fails. |
| No current failure boundary | Re-judged all six existing constructed edits and both source controls. Local-only cleanup fails F3 despite improvement and shorter length; both over-trimmed edits fail F1/F2. Examples remain outside execution counts. |
| Stale qualification status | Rewrote qualification around current policy, completed collection and its actual exposure/coverage limits. |
| Validator requires historical P1 | Aggregation now resolves criteria through result-pinned assessment manifests while independently checking unchanged supplied-input identities. Standalone report and protocol readiness pass. |
| Pinning churn | Retained the existing evidence layers: collection manifests identify what subjects received; reassessment manifests identify changed rules; results and the index identify judgments and actual attempts. Removing a layer would conflate these responsibilities under the accepted format. Reduced avoidable churn by reviewing rules once before freezing and updating downstream identities once in dependency order. No corrective re-pinning was needed in this change. |

## Self-review

Reviewed the two sources, all eight delivered outputs, all six constructed edits, both case definitions, policy/body equality, eight result records, both reassessment manifests, index, aggregate and current authority/handoff links. Checked that pass counts are not presented as equal quality, length cannot compensate for harm, and prior sentence-omission failures remain withdrawn for whole-document reasons.

Reviewed validator paths for ordinary collection rules, changed assessment rules, unchanged subject identities, invalid identities, old aggregate rows, wrong counts, missing criteria, mixed criterion coverage and unattempted groups. The existing schemas/reference checks still reject malformed records; the aggregate fix does not substitute working files for missing pinned evidence. No new provider calls, skill edits, raw-evidence changes or schema layer were introduced.

One additional defect was confirmed during self-review: missing or incompatible per-result criteria raised StopIteration inside a generator, which escaped as RuntimeError instead of a diagnostic. Failing regression tests reproduced both a missing criterion and mixed rule sets. Aggregation now reports the missing criterion explicitly, and the tests pass. A further regression check confirms that entirely unattempted groups still require protocol-defined criterion rows.

The six initial offline-suite failures were nested macOS sandbox startup failures under the outer execution sandbox. The same dummy-provider suite passes with host permission, as specified by the runner guide; no real models or owner authentication are used by these tests.

Final verification includes the full offline runner suite, hook and format suites, live CW report/readiness checks, both SSR core/comparison readiness checks, all 16 CW aggregate rows, committed identity/evidence hashes and affected local links. Detailed counts are recorded in the completion commit. Existing examples do not exercise a longer-output flag; qualification states that limit explicitly rather than claiming coverage.

No unresolved P0/P1/P2 findings remain after the fixes and re-review. The pin-layer removal suggestion is intentionally not adopted for the responsibility-separation reason above; future comparison scope remains separately authorized.

No findings.

DD-VERDICT: PASS
