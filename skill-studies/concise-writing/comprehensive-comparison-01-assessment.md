# CW comprehensive rewrite: batch assessment

Format version: `1`
Assessment ID: `comprehensive-comparison-01`
Study / batch: `concise-writing` / `comprehensive-comparison-01`
Status: complete; eight valid executions assessed under prospectively frozen policy 4.
Scope and acceptance rules: [protocol](protocol.md#comparison-comprehensive-comparison-01) at Git `d5da87c016bcf5aa2cf21bcd3e92df80b45eeb94`.
Attempt index: [comprehensive-comparison-01-run-index.json](comprehensive-comparison-01-run-index.json) at Git `ff59f5df1255981ad592086aba559e1049c0259f`, SHA-256 `d1461815838c5c472b6e17487d369c32836a6e17c25b3f2b3a553ec05743ed0c`.
Assessor: Codex active session with the source cases, qualification examples, prior baseline and candidate available; neither blind nor independent validation.

The existing comprehensive candidate preserves the tested outcomes: both versions pass 2/2 on each case. This does not establish an overall effectiveness or readability improvement. All eight outputs are shorter than their source; the original produces shorter outputs than the candidate in all four matched pairs. The candidate skill itself is 665 words versus 860, but neither instruction size nor output size determines a quality pass.

## Coverage and execution results

Exactly eight attempts ran in the approved order. All have valid setup; no retries, replacements, exclusions, unknown factors or unattempted slots.
Both existing cases, source/task/prompt bytes, qualification examples and policy 4 were held fixed. Definition 5 adds candidate applicability and current status metadata only; F1–F3 rule text did not change. No candidate-derived coverage or scoring was introduced.
The [recommendation](cases/agent-recommendation/comparison-manifest.json) and [briefing](cases/effective-briefing/comparison-manifest.json) manifests preserve the original and exact candidate independently. Fresh original runs provide the contemporaneous comparator; the earlier original/control baseline remains separate and unchanged.
All executions requested gpt-5.6-sol, low effort, workspace-write. Codex CLI 0.154.0, its executable hash, runner execution code and provider base instructions match baseline and each other. An immutable model revision is unavailable.
Pre-launch source/configuration hashes, baseline Git source/TASK bytes, unchanged task and skill files, stdout/session thread identity and cwd, and complete skill tool-response exposure before editing were verified for every attempt. Observed catalogs contain native system skills and the intended CW version; no DD, controller criteria or worked examples were observed. These checks do not prove exhaustive host-read isolation.
Every stopped bundle was retained and inventory-verified before the next dispatch. Eight bundles contain 224 files totaling 1,585,847 bytes. Runner duration totals 508.067 seconds; storage risk and total study accounting belong to the [protocol](protocol.md#storage-and-accounting).

Each pass requires F1 correctness, F2 effectiveness at least equal to the complete source, and F3 whole-document readability including consumption burden. Length is separate; shorter preferred, unchanged acceptable, longer flagged. Process is unscored. Counts use wc -w on complete Markdown.

| Order | Case / condition / repetition | Setup | Functional outcome | Source words | Output words | Change | Longer flag |
|---:|---|---|---|---:|---:|---:|---|
| [1](results/20260918T201942773Z-cw-agent-recommendation-original-824b61cf-ede6-4a1d-a43c-bbd0aa2b79cb-plql5fqx.json) | agent-recommendation / original / 1 | valid | met | 625 | 223 | -402 | no |
| [2](results/20260918T202103899Z-cw-agent-recommendation-candidate-comprehensive-74e7978d-77b1-40b4-bb5a-e360ed9f2ec4-g8uwiexe.json) | agent-recommendation / candidate-comprehensive / 1 | valid | met | 625 | 254 | -371 | no |
| [3](results/20260918T202248957Z-cw-effective-briefing-candidate-comprehensive-b770db17-bd79-4729-9d4b-7a2f857039b2-ch2zfzfr.json) | effective-briefing / candidate-comprehensive / 1 | valid | met | 279 | 255 | -24 | no |
| [4](results/20260918T202458250Z-cw-effective-briefing-original-d8465f78-0ff5-4aab-a491-bd82ce4f613b-hn26b08a.json) | effective-briefing / original / 1 | valid | met | 279 | 235 | -44 | no |
| [5](results/20260918T202610818Z-cw-agent-recommendation-candidate-comprehensive-7b3a0c9d-75eb-43ec-a3fb-77a6abdf5b53-ffaixt32.json) | agent-recommendation / candidate-comprehensive / 2 | valid | met | 625 | 258 | -367 | no |
| [6](results/20260918T202739534Z-cw-agent-recommendation-original-b4b02b7f-0a5d-48ba-a611-b8f27723336b-x8_nkog_.json) | agent-recommendation / original / 2 | valid | met | 625 | 213 | -412 | no |
| [7](results/20260918T202913040Z-cw-effective-briefing-original-50436db3-93e7-4766-95d3-89f095d5ad18-2xxg96ji.json) | effective-briefing / original / 2 | valid | met | 279 | 212 | -67 | no |
| [8](results/20260918T203053069Z-cw-effective-briefing-candidate-comprehensive-c1b45a8b-8a74-41c5-b8d9-ff5a5e5781f5-atwhx6qr.json) | effective-briefing / candidate-comprehensive / 2 | valid | met | 279 | 259 | -20 | no |

| Case / condition | Planned | Attempted | Included | Invalid setup | Setup unresolved | Unattempted |
|---|---:|---:|---:|---:|---:|---:|
| agent-recommendation / original | 2 | 2 | 2 | 0 | 0 | 0 |
| agent-recommendation / candidate-comprehensive | 2 | 2 | 2 | 0 | 0 | 0 |
| effective-briefing / original | 2 | 2 | 2 | 0 | 0 | 0 |
| effective-briefing / candidate-comprehensive | 2 | 2 | 2 | 0 | 0 | 0 |

## Aggregate results

Counts are met / not met / insufficient evidence among valid setups. There is no weighted score or compensation between criteria.

| Case / condition / criterion | Met | Not met | Insufficient evidence | Evidence |
|---|---:|---:|---:|---|
| agent-recommendation / original / F1 | 2 | 0 | 0 | [1](results/20260918T201942773Z-cw-agent-recommendation-original-824b61cf-ede6-4a1d-a43c-bbd0aa2b79cb-plql5fqx.json), [6](results/20260918T202739534Z-cw-agent-recommendation-original-b4b02b7f-0a5d-48ba-a611-b8f27723336b-x8_nkog_.json) |
| agent-recommendation / original / F2 | 2 | 0 | 0 | [1](results/20260918T201942773Z-cw-agent-recommendation-original-824b61cf-ede6-4a1d-a43c-bbd0aa2b79cb-plql5fqx.json), [6](results/20260918T202739534Z-cw-agent-recommendation-original-b4b02b7f-0a5d-48ba-a611-b8f27723336b-x8_nkog_.json) |
| agent-recommendation / original / F3 | 2 | 0 | 0 | [1](results/20260918T201942773Z-cw-agent-recommendation-original-824b61cf-ede6-4a1d-a43c-bbd0aa2b79cb-plql5fqx.json), [6](results/20260918T202739534Z-cw-agent-recommendation-original-b4b02b7f-0a5d-48ba-a611-b8f27723336b-x8_nkog_.json) |
| agent-recommendation / original / functional outcome | 2 | 0 | 0 | [1](results/20260918T201942773Z-cw-agent-recommendation-original-824b61cf-ede6-4a1d-a43c-bbd0aa2b79cb-plql5fqx.json), [6](results/20260918T202739534Z-cw-agent-recommendation-original-b4b02b7f-0a5d-48ba-a611-b8f27723336b-x8_nkog_.json) |
| agent-recommendation / candidate-comprehensive / F1 | 2 | 0 | 0 | [2](results/20260918T202103899Z-cw-agent-recommendation-candidate-comprehensive-74e7978d-77b1-40b4-bb5a-e360ed9f2ec4-g8uwiexe.json), [5](results/20260918T202610818Z-cw-agent-recommendation-candidate-comprehensive-7b3a0c9d-75eb-43ec-a3fb-77a6abdf5b53-ffaixt32.json) |
| agent-recommendation / candidate-comprehensive / F2 | 2 | 0 | 0 | [2](results/20260918T202103899Z-cw-agent-recommendation-candidate-comprehensive-74e7978d-77b1-40b4-bb5a-e360ed9f2ec4-g8uwiexe.json), [5](results/20260918T202610818Z-cw-agent-recommendation-candidate-comprehensive-7b3a0c9d-75eb-43ec-a3fb-77a6abdf5b53-ffaixt32.json) |
| agent-recommendation / candidate-comprehensive / F3 | 2 | 0 | 0 | [2](results/20260918T202103899Z-cw-agent-recommendation-candidate-comprehensive-74e7978d-77b1-40b4-bb5a-e360ed9f2ec4-g8uwiexe.json), [5](results/20260918T202610818Z-cw-agent-recommendation-candidate-comprehensive-7b3a0c9d-75eb-43ec-a3fb-77a6abdf5b53-ffaixt32.json) |
| agent-recommendation / candidate-comprehensive / functional outcome | 2 | 0 | 0 | [2](results/20260918T202103899Z-cw-agent-recommendation-candidate-comprehensive-74e7978d-77b1-40b4-bb5a-e360ed9f2ec4-g8uwiexe.json), [5](results/20260918T202610818Z-cw-agent-recommendation-candidate-comprehensive-7b3a0c9d-75eb-43ec-a3fb-77a6abdf5b53-ffaixt32.json) |
| effective-briefing / original / F1 | 2 | 0 | 0 | [4](results/20260918T202458250Z-cw-effective-briefing-original-d8465f78-0ff5-4aab-a491-bd82ce4f613b-hn26b08a.json), [7](results/20260918T202913040Z-cw-effective-briefing-original-50436db3-93e7-4766-95d3-89f095d5ad18-2xxg96ji.json) |
| effective-briefing / original / F2 | 2 | 0 | 0 | [4](results/20260918T202458250Z-cw-effective-briefing-original-d8465f78-0ff5-4aab-a491-bd82ce4f613b-hn26b08a.json), [7](results/20260918T202913040Z-cw-effective-briefing-original-50436db3-93e7-4766-95d3-89f095d5ad18-2xxg96ji.json) |
| effective-briefing / original / F3 | 2 | 0 | 0 | [4](results/20260918T202458250Z-cw-effective-briefing-original-d8465f78-0ff5-4aab-a491-bd82ce4f613b-hn26b08a.json), [7](results/20260918T202913040Z-cw-effective-briefing-original-50436db3-93e7-4766-95d3-89f095d5ad18-2xxg96ji.json) |
| effective-briefing / original / functional outcome | 2 | 0 | 0 | [4](results/20260918T202458250Z-cw-effective-briefing-original-d8465f78-0ff5-4aab-a491-bd82ce4f613b-hn26b08a.json), [7](results/20260918T202913040Z-cw-effective-briefing-original-50436db3-93e7-4766-95d3-89f095d5ad18-2xxg96ji.json) |
| effective-briefing / candidate-comprehensive / F1 | 2 | 0 | 0 | [3](results/20260918T202248957Z-cw-effective-briefing-candidate-comprehensive-b770db17-bd79-4729-9d4b-7a2f857039b2-ch2zfzfr.json), [8](results/20260918T203053069Z-cw-effective-briefing-candidate-comprehensive-c1b45a8b-8a74-41c5-b8d9-ff5a5e5781f5-atwhx6qr.json) |
| effective-briefing / candidate-comprehensive / F2 | 2 | 0 | 0 | [3](results/20260918T202248957Z-cw-effective-briefing-candidate-comprehensive-b770db17-bd79-4729-9d4b-7a2f857039b2-ch2zfzfr.json), [8](results/20260918T203053069Z-cw-effective-briefing-candidate-comprehensive-c1b45a8b-8a74-41c5-b8d9-ff5a5e5781f5-atwhx6qr.json) |
| effective-briefing / candidate-comprehensive / F3 | 2 | 0 | 0 | [3](results/20260918T202248957Z-cw-effective-briefing-candidate-comprehensive-b770db17-bd79-4729-9d4b-7a2f857039b2-ch2zfzfr.json), [8](results/20260918T203053069Z-cw-effective-briefing-candidate-comprehensive-c1b45a8b-8a74-41c5-b8d9-ff5a5e5781f5-atwhx6qr.json) |
| effective-briefing / candidate-comprehensive / functional outcome | 2 | 0 | 0 | [3](results/20260918T202248957Z-cw-effective-briefing-candidate-comprehensive-b770db17-bd79-4729-9d4b-7a2f857039b2-ch2zfzfr.json), [8](results/20260918T203053069Z-cw-effective-briefing-candidate-comprehensive-c1b45a8b-8a74-41c5-b8d9-ff5a5e5781f5-atwhx6qr.json) |

Recommendation: all four edits preserve the bounded ten-account pilot, staging evidence, mechanism, production limitations, staffing and timing, mismatch evidence, and separate release decision. Their decision-first organization removes the source’s scattered instructions and communication digression.
Briefing: all four edits preserve the Thursday invitation decision, continuing preview, evidence and limitations, named readiness checks, approval, opt-in choice and later expansion/default decisions. The conditional recommendation is read with the checks and approval gate; it is not an unconditional rollout instruction.
All eight outputs are readable and easier to consume than the padded Recommendation or at least as usable as the already effective Briefing. No output exceeds its source length, so there are zero longer-output flags.

## Comparison and interpretation

Equal pass counts establish equal threshold outcomes on these executions, not identical quality. The following are qualitative reading judgments, not measured reader timings or a hidden numeric scale.

| Pair | Evidence-backed effectiveness and reading differences |
|---|---|
| Recommendation, repetition 1: original 1 / candidate 2 | Original gives a continuous request → evidence/risk → safeguards sequence. Candidate separates evidence bullets, mechanism and outcome bullets, aiding targeted lookup while requiring more section transitions. Candidate repeats limits beside the request and evidence to connect rationale; neither document loses the pilot boundaries. No clear overall quality advantage. |
| Recommendation, repetition 2: original 6 / candidate 5 | Candidate puts both outcome branches together immediately after the request, making operating consequences available in one place. Original puts the success branch up front and gives the mismatch procedure its own heading. Candidate explicitly connects untested risks to pilot rationale, but its evidence paragraph repeats cross-region limitations; original conveys that rationale through the adjacent limits with less restatement. This is a tradeoff in explicit explanation and reading effort, not an established pass/fail difference. |
| Briefing, repetition 1: original 4 / candidate 3 | Original opens with a conditional recommendation and presents evidence in connected paragraphs; candidate opens with a decision request and uses evidence bullets. Both retain current-team continuity, checks and follow-up. Candidate explicitly explains permission to try beside opt-in choice; original states that an invitation does not enable it. Neither creates a materially better decision basis. |
| Briefing, repetition 2: original 7 / candidate 8 | Candidate places named checks and approval directly below the opening decision, favoring immediate action lookup. Original presents evidence before its compact check list, favoring reading the argument first. Candidate’s permission/default explanation is more explicit and repetitive; original conveys the same boundary in a shorter connected sequence. Both remain usable; no overall quality winner established. |

The original outputs contain 223/213 words on Recommendation and 235/212 on Briefing; candidate outputs contain 254/258 and 255/259. Every candidate output is longer than its matched original output, although still shorter than the source. These are comparative length observations, not policy “longer than source” flags or automatic failures.
The candidate instruction is 195 words smaller (22.7%), while its outputs here are less compressed. The results support preservation of the tested quality outcomes, not a claim that the candidate produces more concise or more effective documents.
Contemporaneous original outcomes agree with the earlier baseline’s policy-4 passes. No material observed runtime drift required separate strata. The earlier controls also passed; this comparison does not establish new causal contribution by CW.

## Decision and limits

Recommendation: treat the candidate as viable on the tested ordinary-prose scope, with no demonstrated quality advantage. Retain the live original while the owner’s deferred adoption decision remains in force. A smaller instruction and passing cases alone do not justify claiming universal equivalence or automatically adopting the wider candidate.
This completes the selected CW comparison step. The framework has now carried fixed prose cases and a settled whole-document rule through a real version comparison, preserved complete evidence and reported quality tradeoffs alongside threshold outcomes. No scoring revision or new scenario was needed after seeing the rewrite.
Limits remain the same two short constructed software updates, two repetitions per version and one model/effort setting. The same informed session scored all outputs. No population reliability, held-out transfer, discovery/composition or broad adoption claim follows. Candidate applicability changes outside these tasks are untested and did not alter the baseline.
Reusing the existing candidate deliberately leaves fresh evidence-led skill authoring untested. All eight authorized calls are spent; no additional scenario, retry, provider pass or live skill edit follows automatically.

Verification: all eight execution-result records and the complete attempt index pass document checks. Source/configuration identities, inventories, policy-copy equality, all 16 aggregate rows and word counts are checked directly; final assessment readiness and self-review are recorded in the protocol.
