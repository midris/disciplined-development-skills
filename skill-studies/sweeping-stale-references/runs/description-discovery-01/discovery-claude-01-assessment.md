# SSR description discovery: claude assessment

Format version: `2`
Assessment ID: ssr-discovery-claude-01
Study / batch: sweeping-stale-references / discovery-claude-01
Status: early stopped; unattempted scope preserved
Scope and acceptance rules: [protocol](../../protocol.md) at Git `52b8920c838987bcc22f550a50ac8c6c97f1d161`.
Attempt index: [discovery-claude-01-run-index.json](discovery-claude-01-run-index.json), Git `42230d24febc5a38b15bc69fb778cb8ffe49acd4`, SHA-256 `844272c7d89760fc268f37d3823aee3f75d2886bb3a5c05cafe3e62455fdca17`.
Assessor: active Codex preparer/assessor with prior/version awareness; not blind or independent.

## Coverage and execution results

6 of 40 planned subjects completed with valid setup, without retries or substitutions.
The combined screen stopped at slot 13 after an incomplete Codex candidate repair; the remaining 34 provider slots are unattempted.
The [combined assessment](description-discovery-01-assessment.md) records selection, repair results, the failure mechanism and attribution limits.
No independent output review was dispatched and no adoption recommendation follows from this incomplete comparison.

## Aggregate results

Generated tables only; judgments and conclusions remain with the assessor.

| Case / condition | Planned | Attempted | Included | Invalid setup | Setup unresolved | Unattempted |
| --- | --- | --- | --- | --- | --- | --- |
| invocation-review / current | 5 | 1 | 1 | 0 | 0 | 4 |
| invocation-review / candidate | 5 | 1 | 1 | 0 | 0 | 4 |
| invocation-change / current | 5 | 1 | 1 | 0 | 0 | 4 |
| invocation-change / candidate | 5 | 1 | 1 | 0 | 0 | 4 |
| invocation-verification / current | 5 | 1 | 1 | 0 | 0 | 4 |
| invocation-verification / candidate | 5 | 1 | 1 | 0 | 0 | 4 |
| invocation-unrelated / current | 5 | 0 | 0 | 0 | 0 | 5 |
| invocation-unrelated / candidate | 5 | 0 | 0 | 0 | 0 | 5 |

| Order | Case | Condition | Repetition | Setup / coverage | Recorded outcome | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | invocation-review | current | 1 | valid | met | [discovery-claude-01-invocation-review-current-1](results/20261101T000125149Z-ssr-discovery-claude-invocation-review-current-e8278bc6-d716-410c-8bf1-650ce083b6cf-nzxvs45x.json) |
| 2 | invocation-review | candidate | 1 | valid | met | [discovery-claude-01-invocation-review-candidate-1](results/20261101T000219730Z-ssr-discovery-claude-invocation-review-candidate-3bc0adf1-c294-4083-979c-4165d1158246-q8bo7p9i.json) |
| 3 | invocation-change | current | 1 | valid | met | [discovery-claude-01-invocation-change-current-1](results/20261101T000446040Z-ssr-discovery-claude-invocation-change-current-c939a8ca-db3f-46fc-9133-9772a5b9f73d-khrcczjq.json) |
| 4 | invocation-change | candidate | 1 | valid | met | [discovery-claude-01-invocation-change-candidate-1](results/20261101T000527960Z-ssr-discovery-claude-invocation-change-candidate-31437719-3aa9-4fe9-b366-a20010a6fcdf-s45p82hg.json) |
| 5 | invocation-verification | current | 1 | valid | not measured | [discovery-claude-01-invocation-verification-current-1](results/20261101T000756280Z-ssr-discovery-claude-invocation-verification-current-6a507c90-71a8-4990-b635-d7572170656d-pqc3pee2.json) |
| 6 | invocation-verification | candidate | 1 | valid | not measured | [discovery-claude-01-invocation-verification-candidate-1](results/20261101T000820463Z-ssr-discovery-claude-invocation-verification-candidate-68baa39d-3f27-4502-b83c-7128bab973fb-9bifslg3.json) |
| 7 | invocation-review | candidate | 2 | unattempted | not assessed | none |
| 8 | invocation-review | current | 2 | unattempted | not assessed | none |
| 9 | invocation-change | candidate | 2 | unattempted | not assessed | none |
| 10 | invocation-change | current | 2 | unattempted | not assessed | none |
| 11 | invocation-verification | candidate | 2 | unattempted | not assessed | none |
| 12 | invocation-verification | current | 2 | unattempted | not assessed | none |
| 13 | invocation-review | current | 3 | unattempted | not assessed | none |
| 14 | invocation-review | candidate | 3 | unattempted | not assessed | none |
| 15 | invocation-change | current | 3 | unattempted | not assessed | none |
| 16 | invocation-change | candidate | 3 | unattempted | not assessed | none |
| 17 | invocation-verification | current | 3 | unattempted | not assessed | none |
| 18 | invocation-verification | candidate | 3 | unattempted | not assessed | none |
| 19 | invocation-review | candidate | 4 | unattempted | not assessed | none |
| 20 | invocation-review | current | 4 | unattempted | not assessed | none |
| 21 | invocation-change | candidate | 4 | unattempted | not assessed | none |
| 22 | invocation-change | current | 4 | unattempted | not assessed | none |
| 23 | invocation-verification | candidate | 4 | unattempted | not assessed | none |
| 24 | invocation-verification | current | 4 | unattempted | not assessed | none |
| 25 | invocation-review | current | 5 | unattempted | not assessed | none |
| 26 | invocation-review | candidate | 5 | unattempted | not assessed | none |
| 27 | invocation-change | current | 5 | unattempted | not assessed | none |
| 28 | invocation-change | candidate | 5 | unattempted | not assessed | none |
| 29 | invocation-verification | current | 5 | unattempted | not assessed | none |
| 30 | invocation-verification | candidate | 5 | unattempted | not assessed | none |
| 31 | invocation-unrelated | current | 1 | unattempted | not assessed | none |
| 32 | invocation-unrelated | candidate | 1 | unattempted | not assessed | none |
| 33 | invocation-unrelated | candidate | 2 | unattempted | not assessed | none |
| 34 | invocation-unrelated | current | 2 | unattempted | not assessed | none |
| 35 | invocation-unrelated | current | 3 | unattempted | not assessed | none |
| 36 | invocation-unrelated | candidate | 3 | unattempted | not assessed | none |
| 37 | invocation-unrelated | candidate | 4 | unattempted | not assessed | none |
| 38 | invocation-unrelated | current | 4 | unattempted | not assessed | none |
| 39 | invocation-unrelated | current | 5 | unattempted | not assessed | none |
| 40 | invocation-unrelated | candidate | 5 | unattempted | not assessed | none |

| Case / condition / criterion | Met | Not met | Insufficient evidence | Not measured | Evidence |
| --- | --- | --- | --- | --- | --- |
| invocation-review / current / F1 | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-review-current-1](results/20261101T000125149Z-ssr-discovery-claude-invocation-review-current-e8278bc6-d716-410c-8bf1-650ce083b6cf-nzxvs45x.json) |
| invocation-review / current / F2 | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-review-current-1](results/20261101T000125149Z-ssr-discovery-claude-invocation-review-current-e8278bc6-d716-410c-8bf1-650ce083b6cf-nzxvs45x.json) |
| invocation-review / current / F3 | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-review-current-1](results/20261101T000125149Z-ssr-discovery-claude-invocation-review-current-e8278bc6-d716-410c-8bf1-650ce083b6cf-nzxvs45x.json) |
| invocation-review / current / D1 | 0 | 1 | 0 | 0 | [discovery-claude-01-invocation-review-current-1](results/20261101T000125149Z-ssr-discovery-claude-invocation-review-current-e8278bc6-d716-410c-8bf1-650ce083b6cf-nzxvs45x.json) |
| invocation-review / current / functional outcome | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-review-current-1](results/20261101T000125149Z-ssr-discovery-claude-invocation-review-current-e8278bc6-d716-410c-8bf1-650ce083b6cf-nzxvs45x.json) |
| invocation-review / candidate / F1 | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-review-candidate-1](results/20261101T000219730Z-ssr-discovery-claude-invocation-review-candidate-3bc0adf1-c294-4083-979c-4165d1158246-q8bo7p9i.json) |
| invocation-review / candidate / F2 | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-review-candidate-1](results/20261101T000219730Z-ssr-discovery-claude-invocation-review-candidate-3bc0adf1-c294-4083-979c-4165d1158246-q8bo7p9i.json) |
| invocation-review / candidate / F3 | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-review-candidate-1](results/20261101T000219730Z-ssr-discovery-claude-invocation-review-candidate-3bc0adf1-c294-4083-979c-4165d1158246-q8bo7p9i.json) |
| invocation-review / candidate / D1 | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-review-candidate-1](results/20261101T000219730Z-ssr-discovery-claude-invocation-review-candidate-3bc0adf1-c294-4083-979c-4165d1158246-q8bo7p9i.json) |
| invocation-review / candidate / functional outcome | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-review-candidate-1](results/20261101T000219730Z-ssr-discovery-claude-invocation-review-candidate-3bc0adf1-c294-4083-979c-4165d1158246-q8bo7p9i.json) |
| invocation-change / current / F1 | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-change-current-1](results/20261101T000446040Z-ssr-discovery-claude-invocation-change-current-c939a8ca-db3f-46fc-9133-9772a5b9f73d-khrcczjq.json) |
| invocation-change / current / F2 | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-change-current-1](results/20261101T000446040Z-ssr-discovery-claude-invocation-change-current-c939a8ca-db3f-46fc-9133-9772a5b9f73d-khrcczjq.json) |
| invocation-change / current / F3 | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-change-current-1](results/20261101T000446040Z-ssr-discovery-claude-invocation-change-current-c939a8ca-db3f-46fc-9133-9772a5b9f73d-khrcczjq.json) |
| invocation-change / current / D1 | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-change-current-1](results/20261101T000446040Z-ssr-discovery-claude-invocation-change-current-c939a8ca-db3f-46fc-9133-9772a5b9f73d-khrcczjq.json) |
| invocation-change / current / functional outcome | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-change-current-1](results/20261101T000446040Z-ssr-discovery-claude-invocation-change-current-c939a8ca-db3f-46fc-9133-9772a5b9f73d-khrcczjq.json) |
| invocation-change / candidate / F1 | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-change-candidate-1](results/20261101T000527960Z-ssr-discovery-claude-invocation-change-candidate-31437719-3aa9-4fe9-b366-a20010a6fcdf-s45p82hg.json) |
| invocation-change / candidate / F2 | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-change-candidate-1](results/20261101T000527960Z-ssr-discovery-claude-invocation-change-candidate-31437719-3aa9-4fe9-b366-a20010a6fcdf-s45p82hg.json) |
| invocation-change / candidate / F3 | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-change-candidate-1](results/20261101T000527960Z-ssr-discovery-claude-invocation-change-candidate-31437719-3aa9-4fe9-b366-a20010a6fcdf-s45p82hg.json) |
| invocation-change / candidate / D1 | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-change-candidate-1](results/20261101T000527960Z-ssr-discovery-claude-invocation-change-candidate-31437719-3aa9-4fe9-b366-a20010a6fcdf-s45p82hg.json) |
| invocation-change / candidate / functional outcome | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-change-candidate-1](results/20261101T000527960Z-ssr-discovery-claude-invocation-change-candidate-31437719-3aa9-4fe9-b366-a20010a6fcdf-s45p82hg.json) |
| invocation-verification / current / D1 | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-verification-current-1](results/20261101T000756280Z-ssr-discovery-claude-invocation-verification-current-6a507c90-71a8-4990-b635-d7572170656d-pqc3pee2.json) |
| invocation-verification / current / functional outcome | 0 | 0 | 0 | 1 | [discovery-claude-01-invocation-verification-current-1](results/20261101T000756280Z-ssr-discovery-claude-invocation-verification-current-6a507c90-71a8-4990-b635-d7572170656d-pqc3pee2.json) |
| invocation-verification / candidate / D1 | 1 | 0 | 0 | 0 | [discovery-claude-01-invocation-verification-candidate-1](results/20261101T000820463Z-ssr-discovery-claude-invocation-verification-candidate-68baa39d-3f27-4502-b83c-7128bab973fb-9bifslg3.json) |
| invocation-verification / candidate / functional outcome | 0 | 0 | 0 | 1 | [discovery-claude-01-invocation-verification-candidate-1](results/20261101T000820463Z-ssr-discovery-claude-invocation-verification-candidate-68baa39d-3f27-4502-b83c-7128bab973fb-9bifslg3.json) |
| invocation-unrelated / current / D1 | 0 | 0 | 0 | 0 | none |
| invocation-unrelated / current / functional outcome | 0 | 0 | 0 | 0 | none |
| invocation-unrelated / candidate / D1 | 0 | 0 | 0 | 0 | none |
| invocation-unrelated / candidate / functional outcome | 0 | 0 | 0 | 0 | none |

Use assessment format 2. Not measured is separate from functional met/not met/insufficient evidence and excluded from functional success denominators. No functional success rate exists when all outcomes are not measured. Coverage above retains excluded and unassessed attempts.

