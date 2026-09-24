# Opus low native invocation: assessment

Format version: `2`
Assessment ID: ssr-claude-opus-invocation-01
Study / batch: sweeping-stale-references / claude-opus-invocation-01
Status: complete; all ten authorized attempts retained and assessed
Scope and acceptance rules: [protocol](protocol.md) at Git `85c3fd707e9ce8e01f8006883a8e2e1cd63b011a`, batch claude-opus-invocation-01; unchanged native case definitions and SSR policy 3.
Attempt index: [claude-opus-invocation-01-run-index.json](claude-opus-invocation-01-run-index.json) at Git `5f4feba26eace2330621853b72a4b4eda162b806`, SHA-256 `45f823e544aa275e5eb4cfd7103af67ffa3f0a1bbebcfbd41e54fb35d0d51fbe`.
Assessor and relevant session context: Codex active session that prepared and inspected these exposed cases; not independent or blind.

Opus also misses native invocation: original SSR loads in two of four positive trials; rewrite SSR loads in four of four.
All original tasks succeed even when SSR is not loaded; one rewrite repair remains incomplete despite timely loading.
This separates invocation from task correctness and does not establish a reliable model or skill-version ranking.

## Coverage and execution results

Ten calls follow the declared schedule: two repetitions of each positive trigger for each skill version, plus one unrelated non-use check per version.
All have valid setup, complete retained capture and successful cleanup; no retries, replacements, exclusions, unknown outcomes or unattempted slots exist.
All execution-result records resolve through the pinned index.
Both non-use outcomes are functionally `not measured`, not functional passes.
No ordinary explicit-load or pressure cases were repeated in this invocation-only batch.

| Measure | Original | Rewrite |
| --- | ---: | ---: |
| Initiating-change timely invocation | 2/2 | 2/2 |
| Reviewer-triggered timely invocation | 0/2 | 2/2 |
| Positive native functional success | 4/4 | 3/4 |
| Unrelated appropriate non-use | 1/1 | 1/1 |

The configuration pins `claude-opus-5-5`, low effort, workspace-write and the existing 900-second limit on Claude Code 2.1.280.
Every production init and assistant message reports that model; terminal model-use records show no fallback to another model.
CLI SHA-256 remains `387a5c5dcdbb815085edf0baf79591f9d8894efe922bceaf3d75b1b08055229d`.
The six configurations differ from their Sonnet counterparts only in model and test ID; prompts, tasks, fixture bytes, skill bodies, paths and criterion definitions are unchanged.
Original/rewrite paired inputs differ only in skill body.
The same-day actual-CLI/isolation qualification is reused because runner and executable identities are unchanged; its retained identity is recorded in the [Sonnet assessment](claude-comparison-01-assessment.md).
The model change is verified through these live observations, not claimed as tested by scripted qualification.

Every production catalog contains SSR plus the same sixteen bundled skills as the Sonnet batch; SSR is the sole supplied project skill.
Native prompts do not name SSR or request loading it.
Same-CLI qualification establishes initial description and subsequent full-body delivery; production traces retain catalog names and ordered tool/body events, not complete initial API requests or an immutable backend model revision.
No skill or runner source changed during this collection.
All raw bundles match their retained inventories; evidence hashes and schemas pass.
Functional Git inspection and independent replay use disposable copies only.

| Case / condition | Planned | Attempted | Included | Invalid setup | Setup unresolved | Unattempted |
| --- | --- | --- | --- | --- | --- | --- |
| invocation-change / original | 2 | 2 | 2 | 0 | 0 | 0 |
| invocation-change / candidate | 2 | 2 | 2 | 0 | 0 | 0 |
| invocation-review / original | 2 | 2 | 2 | 0 | 0 | 0 |
| invocation-review / candidate | 2 | 2 | 2 | 0 | 0 | 0 |
| invocation-unrelated / original | 1 | 1 | 1 | 0 | 0 | 0 |
| invocation-unrelated / candidate | 1 | 1 | 1 | 0 | 0 | 0 |

| Order | Case | Condition | Repetition | Setup / coverage | Recorded outcome | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | invocation-change | original | 1 | valid | met | [claude-opus-invocation-01-invocation-change-original-1](results/20260924T174649673Z-ssr-opus-invocation-change-original-6b7841ac-d3b4-409f-ba70-346e090bd0f9-yc7ln4ib.json) |
| 2 | invocation-change | candidate | 1 | valid | met | [claude-opus-invocation-01-invocation-change-candidate-1](results/20260924T174739323Z-ssr-opus-invocation-change-candidate-ccf6243c-5549-405c-9961-63b6a7cf2902-zvf_n58h.json) |
| 3 | invocation-change | candidate | 2 | valid | met | [claude-opus-invocation-01-invocation-change-candidate-2](results/20260924T174818033Z-ssr-opus-invocation-change-candidate-4f6d9de7-5b19-4c9a-b36a-9ea0fd6d2a71-52k5pqnj.json) |
| 4 | invocation-change | original | 2 | valid | met | [claude-opus-invocation-01-invocation-change-original-2](results/20260924T174910601Z-ssr-opus-invocation-change-original-d070415a-c4db-40eb-b3a8-0058be5b42c4-v18e2mi4.json) |
| 5 | invocation-review | original | 1 | valid | met | [claude-opus-invocation-01-invocation-review-original-1](results/20260924T174953518Z-ssr-opus-invocation-review-original-c17dff56-8c57-42ea-b6ee-eb7b92f25b7c-gij89gku.json) |
| 6 | invocation-review | candidate | 1 | valid | not met | [claude-opus-invocation-01-invocation-review-candidate-1](results/20260924T175042449Z-ssr-opus-invocation-review-candidate-211aff49-259c-44e6-9b43-2e4603b4af72-ko2_vqgh.json) |
| 7 | invocation-review | candidate | 2 | valid | met | [claude-opus-invocation-01-invocation-review-candidate-2](results/20260924T175131339Z-ssr-opus-invocation-review-candidate-a889907e-020a-493e-b1f4-ce9566e39e40-00qoqqwf.json) |
| 8 | invocation-review | original | 2 | valid | met | [claude-opus-invocation-01-invocation-review-original-2](results/20260924T175221372Z-ssr-opus-invocation-review-original-4a40e359-bc72-4ffd-a817-a8d44ec67527-2b8boa16.json) |
| 9 | invocation-unrelated | original | 1 | valid | not measured | [claude-opus-invocation-01-invocation-unrelated-original-1](results/20260924T175302229Z-ssr-opus-invocation-unrelated-original-f933766f-4b70-46ae-afb6-f061ab3f86e6-w_wdycch.json) |
| 10 | invocation-unrelated | candidate | 1 | valid | not measured | [claude-opus-invocation-01-invocation-unrelated-candidate-1](results/20260924T175326875Z-ssr-opus-invocation-unrelated-candidate-1ac847a9-6167-4720-91f8-cab3c678d656-iwux2lgf.json) |

## Aggregate results

| Case / condition / criterion | Met | Not met | Insufficient evidence | Not measured | Evidence |
| --- | --- | --- | --- | --- | --- |
| invocation-change / original / F1 | 2 | 0 | 0 | 0 | [claude-opus-invocation-01-invocation-change-original-1](results/20260924T174649673Z-ssr-opus-invocation-change-original-6b7841ac-d3b4-409f-ba70-346e090bd0f9-yc7ln4ib.json), [claude-opus-invocation-01-invocation-change-original-2](results/20260924T174910601Z-ssr-opus-invocation-change-original-d070415a-c4db-40eb-b3a8-0058be5b42c4-v18e2mi4.json) |
| invocation-change / original / F2 | 2 | 0 | 0 | 0 | [claude-opus-invocation-01-invocation-change-original-1](results/20260924T174649673Z-ssr-opus-invocation-change-original-6b7841ac-d3b4-409f-ba70-346e090bd0f9-yc7ln4ib.json), [claude-opus-invocation-01-invocation-change-original-2](results/20260924T174910601Z-ssr-opus-invocation-change-original-d070415a-c4db-40eb-b3a8-0058be5b42c4-v18e2mi4.json) |
| invocation-change / original / F3 | 2 | 0 | 0 | 0 | [claude-opus-invocation-01-invocation-change-original-1](results/20260924T174649673Z-ssr-opus-invocation-change-original-6b7841ac-d3b4-409f-ba70-346e090bd0f9-yc7ln4ib.json), [claude-opus-invocation-01-invocation-change-original-2](results/20260924T174910601Z-ssr-opus-invocation-change-original-d070415a-c4db-40eb-b3a8-0058be5b42c4-v18e2mi4.json) |
| invocation-change / original / D1 | 2 | 0 | 0 | 0 | [claude-opus-invocation-01-invocation-change-original-1](results/20260924T174649673Z-ssr-opus-invocation-change-original-6b7841ac-d3b4-409f-ba70-346e090bd0f9-yc7ln4ib.json), [claude-opus-invocation-01-invocation-change-original-2](results/20260924T174910601Z-ssr-opus-invocation-change-original-d070415a-c4db-40eb-b3a8-0058be5b42c4-v18e2mi4.json) |
| invocation-change / original / functional outcome | 2 | 0 | 0 | 0 | [claude-opus-invocation-01-invocation-change-original-1](results/20260924T174649673Z-ssr-opus-invocation-change-original-6b7841ac-d3b4-409f-ba70-346e090bd0f9-yc7ln4ib.json), [claude-opus-invocation-01-invocation-change-original-2](results/20260924T174910601Z-ssr-opus-invocation-change-original-d070415a-c4db-40eb-b3a8-0058be5b42c4-v18e2mi4.json) |
| invocation-change / candidate / F1 | 2 | 0 | 0 | 0 | [claude-opus-invocation-01-invocation-change-candidate-1](results/20260924T174739323Z-ssr-opus-invocation-change-candidate-ccf6243c-5549-405c-9961-63b6a7cf2902-zvf_n58h.json), [claude-opus-invocation-01-invocation-change-candidate-2](results/20260924T174818033Z-ssr-opus-invocation-change-candidate-4f6d9de7-5b19-4c9a-b36a-9ea0fd6d2a71-52k5pqnj.json) |
| invocation-change / candidate / F2 | 2 | 0 | 0 | 0 | [claude-opus-invocation-01-invocation-change-candidate-1](results/20260924T174739323Z-ssr-opus-invocation-change-candidate-ccf6243c-5549-405c-9961-63b6a7cf2902-zvf_n58h.json), [claude-opus-invocation-01-invocation-change-candidate-2](results/20260924T174818033Z-ssr-opus-invocation-change-candidate-4f6d9de7-5b19-4c9a-b36a-9ea0fd6d2a71-52k5pqnj.json) |
| invocation-change / candidate / F3 | 2 | 0 | 0 | 0 | [claude-opus-invocation-01-invocation-change-candidate-1](results/20260924T174739323Z-ssr-opus-invocation-change-candidate-ccf6243c-5549-405c-9961-63b6a7cf2902-zvf_n58h.json), [claude-opus-invocation-01-invocation-change-candidate-2](results/20260924T174818033Z-ssr-opus-invocation-change-candidate-4f6d9de7-5b19-4c9a-b36a-9ea0fd6d2a71-52k5pqnj.json) |
| invocation-change / candidate / D1 | 2 | 0 | 0 | 0 | [claude-opus-invocation-01-invocation-change-candidate-1](results/20260924T174739323Z-ssr-opus-invocation-change-candidate-ccf6243c-5549-405c-9961-63b6a7cf2902-zvf_n58h.json), [claude-opus-invocation-01-invocation-change-candidate-2](results/20260924T174818033Z-ssr-opus-invocation-change-candidate-4f6d9de7-5b19-4c9a-b36a-9ea0fd6d2a71-52k5pqnj.json) |
| invocation-change / candidate / functional outcome | 2 | 0 | 0 | 0 | [claude-opus-invocation-01-invocation-change-candidate-1](results/20260924T174739323Z-ssr-opus-invocation-change-candidate-ccf6243c-5549-405c-9961-63b6a7cf2902-zvf_n58h.json), [claude-opus-invocation-01-invocation-change-candidate-2](results/20260924T174818033Z-ssr-opus-invocation-change-candidate-4f6d9de7-5b19-4c9a-b36a-9ea0fd6d2a71-52k5pqnj.json) |
| invocation-review / original / F1 | 2 | 0 | 0 | 0 | [claude-opus-invocation-01-invocation-review-original-1](results/20260924T174953518Z-ssr-opus-invocation-review-original-c17dff56-8c57-42ea-b6ee-eb7b92f25b7c-gij89gku.json), [claude-opus-invocation-01-invocation-review-original-2](results/20260924T175221372Z-ssr-opus-invocation-review-original-4a40e359-bc72-4ffd-a817-a8d44ec67527-2b8boa16.json) |
| invocation-review / original / F2 | 2 | 0 | 0 | 0 | [claude-opus-invocation-01-invocation-review-original-1](results/20260924T174953518Z-ssr-opus-invocation-review-original-c17dff56-8c57-42ea-b6ee-eb7b92f25b7c-gij89gku.json), [claude-opus-invocation-01-invocation-review-original-2](results/20260924T175221372Z-ssr-opus-invocation-review-original-4a40e359-bc72-4ffd-a817-a8d44ec67527-2b8boa16.json) |
| invocation-review / original / F3 | 2 | 0 | 0 | 0 | [claude-opus-invocation-01-invocation-review-original-1](results/20260924T174953518Z-ssr-opus-invocation-review-original-c17dff56-8c57-42ea-b6ee-eb7b92f25b7c-gij89gku.json), [claude-opus-invocation-01-invocation-review-original-2](results/20260924T175221372Z-ssr-opus-invocation-review-original-4a40e359-bc72-4ffd-a817-a8d44ec67527-2b8boa16.json) |
| invocation-review / original / D1 | 0 | 2 | 0 | 0 | [claude-opus-invocation-01-invocation-review-original-1](results/20260924T174953518Z-ssr-opus-invocation-review-original-c17dff56-8c57-42ea-b6ee-eb7b92f25b7c-gij89gku.json), [claude-opus-invocation-01-invocation-review-original-2](results/20260924T175221372Z-ssr-opus-invocation-review-original-4a40e359-bc72-4ffd-a817-a8d44ec67527-2b8boa16.json) |
| invocation-review / original / functional outcome | 2 | 0 | 0 | 0 | [claude-opus-invocation-01-invocation-review-original-1](results/20260924T174953518Z-ssr-opus-invocation-review-original-c17dff56-8c57-42ea-b6ee-eb7b92f25b7c-gij89gku.json), [claude-opus-invocation-01-invocation-review-original-2](results/20260924T175221372Z-ssr-opus-invocation-review-original-4a40e359-bc72-4ffd-a817-a8d44ec67527-2b8boa16.json) |
| invocation-review / candidate / F1 | 1 | 1 | 0 | 0 | [claude-opus-invocation-01-invocation-review-candidate-1](results/20260924T175042449Z-ssr-opus-invocation-review-candidate-211aff49-259c-44e6-9b43-2e4603b4af72-ko2_vqgh.json), [claude-opus-invocation-01-invocation-review-candidate-2](results/20260924T175131339Z-ssr-opus-invocation-review-candidate-a889907e-020a-493e-b1f4-ce9566e39e40-00qoqqwf.json) |
| invocation-review / candidate / F2 | 2 | 0 | 0 | 0 | [claude-opus-invocation-01-invocation-review-candidate-1](results/20260924T175042449Z-ssr-opus-invocation-review-candidate-211aff49-259c-44e6-9b43-2e4603b4af72-ko2_vqgh.json), [claude-opus-invocation-01-invocation-review-candidate-2](results/20260924T175131339Z-ssr-opus-invocation-review-candidate-a889907e-020a-493e-b1f4-ce9566e39e40-00qoqqwf.json) |
| invocation-review / candidate / F3 | 1 | 1 | 0 | 0 | [claude-opus-invocation-01-invocation-review-candidate-1](results/20260924T175042449Z-ssr-opus-invocation-review-candidate-211aff49-259c-44e6-9b43-2e4603b4af72-ko2_vqgh.json), [claude-opus-invocation-01-invocation-review-candidate-2](results/20260924T175131339Z-ssr-opus-invocation-review-candidate-a889907e-020a-493e-b1f4-ce9566e39e40-00qoqqwf.json) |
| invocation-review / candidate / D1 | 2 | 0 | 0 | 0 | [claude-opus-invocation-01-invocation-review-candidate-1](results/20260924T175042449Z-ssr-opus-invocation-review-candidate-211aff49-259c-44e6-9b43-2e4603b4af72-ko2_vqgh.json), [claude-opus-invocation-01-invocation-review-candidate-2](results/20260924T175131339Z-ssr-opus-invocation-review-candidate-a889907e-020a-493e-b1f4-ce9566e39e40-00qoqqwf.json) |
| invocation-review / candidate / functional outcome | 1 | 1 | 0 | 0 | [claude-opus-invocation-01-invocation-review-candidate-1](results/20260924T175042449Z-ssr-opus-invocation-review-candidate-211aff49-259c-44e6-9b43-2e4603b4af72-ko2_vqgh.json), [claude-opus-invocation-01-invocation-review-candidate-2](results/20260924T175131339Z-ssr-opus-invocation-review-candidate-a889907e-020a-493e-b1f4-ce9566e39e40-00qoqqwf.json) |
| invocation-unrelated / original / D1 | 1 | 0 | 0 | 0 | [claude-opus-invocation-01-invocation-unrelated-original-1](results/20260924T175302229Z-ssr-opus-invocation-unrelated-original-f933766f-4b70-46ae-afb6-f061ab3f86e6-w_wdycch.json) |
| invocation-unrelated / original / functional outcome | 0 | 0 | 0 | 1 | [claude-opus-invocation-01-invocation-unrelated-original-1](results/20260924T175302229Z-ssr-opus-invocation-unrelated-original-f933766f-4b70-46ae-afb6-f061ab3f86e6-w_wdycch.json) |
| invocation-unrelated / candidate / D1 | 1 | 0 | 0 | 0 | [claude-opus-invocation-01-invocation-unrelated-candidate-1](results/20260924T175326875Z-ssr-opus-invocation-unrelated-candidate-1ac847a9-6167-4720-91f8-cab3c678d656-iwux2lgf.json) |
| invocation-unrelated / candidate / functional outcome | 0 | 0 | 0 | 1 | [claude-opus-invocation-01-invocation-unrelated-candidate-1](results/20260924T175326875Z-ssr-opus-invocation-unrelated-candidate-1ac847a9-6167-4720-91f8-cab3c678d656-iwux2lgf.json) |

Use assessment format 2. Not measured is separate from functional met/not met/insufficient evidence and excluded from functional success denominators. No functional success rate exists when all outcomes are not measured. Coverage above retains excluded and unassessed attempts.


## Findings and interpretation

All four initiating-change trials load SSR through Skill before the first task edit and perform the complete six-path rename, preserving the partner rationale, historical rollout and independent vendor setting.
Independent replay confirms the 30-minute default, 12-minute custom setting, nonpositive rejection and script execution from both working directories.

Original reviewer-triggered orders 5 and 8 never invoke Skill or receive the complete SSR body.
They nevertheless repair all three current claims: four total delivery attempts, three retries after the first failure, and exhaustion on the fourth consecutive failure.
Those tasks pass F1/F2/F3 while D1 fails; successful unaided behavior cannot stand in for invocation evidence.

Candidate reviewer-triggered orders 6 and 7 load the full body before editing.
Order 6 repairs README and operations but leaves troubleshooting's third-failure exhaustion claim stale.
Its final and commit claim no obsolete delivery limit remains, but its post-edit search omits the ordinal “third”.
F1/F3 fail from the same incomplete repair; D1 passes independently.
Order 7 completes all three repairs.
Seven independent runtime probes pass in each reviewer-triggered trial, including the incomplete documentation repair: executable behavior was already correct and these probes cannot establish prose correctness.
Historical policy, independent helper and unrelated operational guidance are preserved in all four.

Additional procedural observations remain outside native D1 rather than becoming new criteria after collection.
Order 1 mixes occurrence/line inventory units and claims a post-edit old-name search absent from its trace.
Order 7 claims a search in the commit before performing it, then runs it and explicitly corrects the timing in its final response.
These records do not assert full procedural compliance merely because loading succeeds.

Both unrelated checks avoid SSR and make no edits; their arithmetic explanations are descriptive only and excluded from functional counts.
They do not test plausible development over-triggering.

Acceptance under the declared rule is descriptive-only.
The answer to the owner's question is that invocation misses also occur on Opus at low effort.
Loading is neither necessary nor sufficient for task success in these observed cases: both missed original review invocations succeed, and one loaded candidate review invocation fails complete repair.
This is an observation about these trials, not a causal claim that SSR has no value or harms performance.
The two versions have byte-identical descriptions; apparent differences cannot be attributed to stronger rewrite trigger wording, nor to body instructions before they are read.
Two repetitions per positive case/version, exposed synthetic inputs and a shared non-blind assessor preclude population reliability or general capability claims.
No edit, adoption or additional collection follows automatically.

## Comparison

The [Sonnet 5 low batch](claude-comparison-01-assessment.md) supplies the corresponding same-day native observations.

| Model / skill | Initiating load | Reviewer load | Positive task success | Appropriate non-use |
| --- | ---: | ---: | ---: | ---: |
| Sonnet 5 / original | 1/2 | 1/2 | 3/4 | 1/1 |
| Sonnet 5 / rewrite | 2/2 | 1/2 | 3/4 | 1/1 |
| Opus 5.5 / original | 2/2 | 0/2 | 4/4 | 1/1 |
| Opus 5.5 / rewrite | 2/2 | 2/2 | 3/4 | 1/1 |

Opus has six timely positive invocations out of eight, compared with Sonnet's five out of eight; each model's non-use cases are outside that denominator.
These small sequential batches were not randomized across models, and the one-trial aggregate difference does not establish improved reliability.
Keep the per-case/version pattern visible rather than recommending a model switch from the pooled fraction.
Current combined accounting belongs to [CW accounting](../concise-writing/protocol.md#storage-and-accounting): ten new calls, 136/136 subject calls spent, no evaluator/authoring/retry calls.

## Closing verification

Active-session self-review found no blocking issue in the fixed-criterion scores, invocation/task separation or evidence accounting.
All ten raw inventories, evidence hashes, result schemas and model/body identities pass; both positive-task replay families preserve expected executable behavior.
All ten current batch readiness checks pass, including historical batches affected by combined accounting, and this assessment passes structural/completeness validation.
The hook suite passes with 263 tests and three skips from its documented working directory.
Current-status references in the plan, protocols and handoff are reconciled; prior frozen inputs and historical assessments remain unchanged.
