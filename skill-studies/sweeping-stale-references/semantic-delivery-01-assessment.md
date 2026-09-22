# Semantic delivery: first collection assessment

Format version: `1`
Assessment ID: `semantic-delivery-01`
Study / batch: `sweeping-stale-references` / `semantic-delivery-01`
Status: assessed; descriptive-only, ready for owner review.
Scope and acceptance rules: [protocol](protocol.md#first-collection-semantic-delivery-01) at Git `784d5d52672a5554a5b5152bbaa190f08462abe3`, the authorized original-then-control pair with one execution per condition and no retries.
Attempt index: [semantic-delivery-01-run-index.json](semantic-delivery-01-run-index.json) at Git `43bca3968cdcdc2e239fc02ebb630b09d4f38178`, SHA-256 `a7d64c2246aa8f95741af9534480c9e235713729b47b735d2ab4b4acaf50e8a5`.
Assessor: Codex active session, with case construction, owner decisions, prior pilots and both current outputs available; not independent or blind validation.

## Coverage and execution results

The declared `semantic-delivery` original/control executions both completed under the frozen Sol-low/workspace-write configurations. Both setups are valid for this bounded comparison; their initial project trees are identical and input hashes match the frozen manifest.
Both complete raw bundles are retained and inventory-verified at the index's absolute paths. Their controller checks were performed on disposable copies.
Uncompleted repetitions, unusable attempts and unresolved evidence: none.
Included attempts: `semantic-delivery-01-original-1-1` and `semantic-delivery-01-control-1-1`. No retries, replacement observations or exclusions.
Setup/input differences: only the declared original skill and its loading instruction; no observed controller guidance or external skill loading in either trace. Trace review is not exhaustive host-wide read exclusion.
All execution results resolve through the accepted index revision above and their own Git pins. Historical pilot results and worked examples do not enter these counts.

## Aggregate results

Case: `semantic-delivery`. Each criterion is counted separately; the functional-outcome rows count executions, not failed criteria.

| Condition / criterion | Met | Not met | Insufficient evidence | Evidence |
|---|---:|---:|---:|---|
| original / F1 | 1 | 0 | 0 | [semantic-delivery-01-original](results/20260916T065509138Z-ssr-semantic-delivery-original-d9863671-a7b7-4567-883a-423f2afa8d1d-b_hgjgpz.json) |
| original / F2 | 1 | 0 | 0 | [semantic-delivery-01-original](results/20260916T065509138Z-ssr-semantic-delivery-original-d9863671-a7b7-4567-883a-423f2afa8d1d-b_hgjgpz.json) |
| original / F3 | 1 | 0 | 0 | [semantic-delivery-01-original](results/20260916T065509138Z-ssr-semantic-delivery-original-d9863671-a7b7-4567-883a-423f2afa8d1d-b_hgjgpz.json) |
| original / P1 | 1 | 0 | 0 | [semantic-delivery-01-original](results/20260916T065509138Z-ssr-semantic-delivery-original-d9863671-a7b7-4567-883a-423f2afa8d1d-b_hgjgpz.json) |
| original / P2 | 1 | 0 | 0 | [semantic-delivery-01-original](results/20260916T065509138Z-ssr-semantic-delivery-original-d9863671-a7b7-4567-883a-423f2afa8d1d-b_hgjgpz.json) |
| original / P3 | 0 | 1 | 0 | [semantic-delivery-01-original](results/20260916T065509138Z-ssr-semantic-delivery-original-d9863671-a7b7-4567-883a-423f2afa8d1d-b_hgjgpz.json) |
| original / functional outcome | 1 | 0 | 0 | [semantic-delivery-01-original](results/20260916T065509138Z-ssr-semantic-delivery-original-d9863671-a7b7-4567-883a-423f2afa8d1d-b_hgjgpz.json) |
| control / F1 | 0 | 1 | 0 | [semantic-delivery-01-control](results/20260916T065737416Z-ssr-semantic-delivery-control-e26f87b4-4156-494c-8574-26b8da287849-9adtabwo.json) |
| control / F2 | 1 | 0 | 0 | [semantic-delivery-01-control](results/20260916T065737416Z-ssr-semantic-delivery-control-e26f87b4-4156-494c-8574-26b8da287849-9adtabwo.json) |
| control / F3 | 0 | 1 | 0 | [semantic-delivery-01-control](results/20260916T065737416Z-ssr-semantic-delivery-control-e26f87b4-4156-494c-8574-26b8da287849-9adtabwo.json) |
| control / functional outcome | 0 | 1 | 0 | [semantic-delivery-01-control](results/20260916T065737416Z-ssr-semantic-delivery-control-e26f87b4-4156-494c-8574-26b8da287849-9adtabwo.json) |

Original's observed functional success fraction is 1/1; control's is 0/1. Both have zero unknowns and full planned coverage. P1–P3 do not apply to control; its process is described in its result without an undisclosed compliance penalty.

Failure pattern: the one failed control execution repairs README while leaving the operations “two additional tries” and troubleshooting “third consecutive failed send” claims stale. Its search returns related paths/context but omits the complete stale clauses; it then diagnoses the contradiction as README-only. The evidence supports a search/inspection gap, not a claim that it read and knowingly ignored both full statements.
The missing repairs cause both F1 and F3 to fail; they contribute one failed functional execution. Both conditions preserve the fixed runtime behavior and protected meaning, with all seven controller runtime observations matching expectations.
Original repairs all three current documents in one commit. Its P3 defect is separate: the reference account uses search-match counts including excluded hits, splits the historical block into two matches, and mixes update/false-positive outcomes within the README entry. Required meanings are accounted for, but units/grouping depart from the fixed case rules; this is non-blocking and does not change functional success.

Acceptance: descriptive-only under the predeclared rule; no pass threshold or reliability claim was selected.
Limits: one execution per condition, one small known case, fixed non-counterbalanced order, shared assessor context and no immutable underlying model revision. No within-condition consistency or recurring frequency can be estimated from this pair.
Supported conclusion: original achieves complete committed semantic reconciliation in this observation; control does not. This is an observed condition difference, not proof of reliable skill benefit or a sufficient basis by itself for a broad rewrite.

## Comparison, when applicable

The observed difference is repair completeness after a realistic single-reference trigger. Preservation ties; original's accounting defect remains visible separately.
Recommendation: retain the current skill while reviewing this first observation and selecting any further baseline scope. Do not rewrite solely for P3 or rerun to obtain a cleaner account. Further collection or a rewrite requires its own declared scope and authorization in the protocol.

Historical isolation check: the [round-9 trace audit](../../reviews/2026-09-21-round9-review.md#historical-trace-audit) found no targeted exposure markers in the 46 earlier attempts. It records seven stdout-only capture limits and does not establish exhaustive isolation; existing setup judgments and scores are unchanged.
