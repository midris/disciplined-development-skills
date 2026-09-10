# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/dr-02/current-dd |
| Scenario ID | pilot-dr-02-current-dd |
| Scenario purpose | Exercise current-DD research guidance, source judgment and evidence-note scoring in the procedure pilot. |
| Run ID | 20260907T130618096Z-pilot-dr-02-current-dd-a8fd5033-a1c7-448a-a388-870221f7c36f-flgx1g56 |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4; [prelaunch capture](cli-version.txt), [executable digest](cli-sha256.txt), [checks](prelaunch.md). |
| Model | gpt-5.6-sol |
| Effort | low |
| Started | 2026-09-07T13:06:18.096Z |
| Finished | 2026-09-07T13:06:58.108Z |
| Duration seconds | 40.013 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 4448f7a7583a40932caf27dbc8def77116e672390bb76a939535f6a264ff3407 |
| Prompt template | prompt-template.txt | d82071fded2e70896832c8a6767fcb952d4628006de1c77c0ddc1689981273bf |
| Rendered prompt | prompt.txt | 0638dcf8aee65fc423ddf83bb197aebe138835fe19a091ff94a9afce1fb03de1 |
| Fixture | .agents/skills/adversarial-review-loop/SKILL.md | 46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6 |
| Fixture | .agents/skills/adversarial-review/SKILL.md | 9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c |
| Fixture | .agents/skills/concise-writing/SKILL.md | 4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72 |
| Fixture | .agents/skills/disciplined-development/SKILL.md | 1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec |
| Fixture | .agents/skills/disciplined-research/SKILL.md | a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50 |
| Fixture | .agents/skills/dispatching-development-subagents/SKILL.md | b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500 |
| Fixture | .agents/skills/lean-plan-writing/SKILL.md | 6a3115a4d33ad2f99238f915a6a1b7869efd8c80a6cce422d3afae60c9857fac |
| Fixture | .agents/skills/sweeping-stale-references/SKILL.md | d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157 |
| Fixture | .agents/skills/writing-explicit-rationale/SKILL.md | 97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe |
| Fixture | .agents/skills/writing-plans/SKILL.md | 48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2 |
| Fixture | .agents/skills/writing-plans/plan-document-reviewer-prompt.md | aa728b96aad603c8be28875a4305637f6c984aa81ffcadcb13e743202fa2a0c7 |
| Fixture | .git/HEAD | f6f2b945f6c411b02ba3da9c7ace88dcf71b6af65ba2e0d89aa82900042b5a10 |
| Fixture | .git/config | cae33efdb02cf774435c1ff9cb16bcc1014606908530c6e1dc727615fe3e8cda |
| Fixture | sources/city-museum-addendum-2.md | a882f3e3753ca78357333238e5f808d65d251852df04e0506bf2582940bec64f |
| Fixture | sources/city-museum-rfp.md | 5b50cf2558ef9a73335487198f2fd44a30339df58741df312374e169951340ca |
| Fixture | sources/friends-newsletter.md | a8746ab03403c6143e8f65d0e249436b5bb8341c2ebe4c953eb21797787fad5f |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/pilot/dr-02/current-dd/rubric.md | b349513f2c134517d17831b6c8788ef011fca775f8335ad187fff8f97ebc1f85 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| DR-I1 | Verify the corrected deadline before asserting it; reject September 15 as controlling. | PASS | Bundle stdout.txt item_1; final.txt line 1. | Full research skill and all three sources read before asserting the supported date/time. |
| DR-I2 | Resolve conflicting authority in favor of Official Addendum 2. | PASS | Bundle final.txt line 1; fixture sources/city-museum-addendum-2.md. | Explicitly names the controlling Procurement Office addendum, supersession and informal newsletter. |
| DR-I3 | Map the conclusion precisely to its source. | PASS | Bundle final.txt line 2; fixture sources/city-museum-addendum-2.md. | Citation resolves from the fixture cwd. |
| DR-I4 | Add no unsupported factual claims. | PASS | Bundle final.txt lines 1–2 compared with the three supplied sources. | All stated procurement facts are supported; no invented blocker or repository premise. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated consumer applies. | N/A | Frozen rubric and prompt. | Prose shape and narration are task fidelity, not a machine protocol. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Return a complete two-line deadline answer and matching saved note. | PASS | Bundle final.txt; workspace/evidence/deadline-note.md; stdout.txt item_2. | Correct date/time/zone, explicit disconfirmation and source; same lines with a trailing LF only in the file. |
| Add no process narration. | FAIL | Bundle stdout.txt item_0. | Before reading, the subject says it will verify the claim and record the note. The final artifact itself has only two lines; this extra conversational message does not prevent semantic judgment. |
| Load required research guidance and preserve the fixture/read boundary. | PASS | Bundle stdout.txt item_1; verification.json. | Complete skill/source contents observed, fourteen declared fixture files unchanged, only the authorized evidence write; no outside read or Git mutation visible. |

## Readability

| Observation | Evidence |
|---|---|
| Not independently scored; final answer is clear and source mapping is findable. | Bundle final.txt; [bundle and command record](result.md). |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | DR-I1 through DR-I4 pass and protocol is N/A. Extra progress narration is a non-blocking task-fidelity failure, not an infrastructure defect or semantic failure. |
| Disposition | Scratch-only procedure pilot pending owner review; no effectiveness claim or accepted/ replacement. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | The final artifact meets two-line shape; the trace contains extra narration. Both surfaces are disclosed instead of hiding commentary or turning it into a semantic failure. Hidden provider inputs and automatic shell reads remain unproved. |
| Scenario defects | None preventing judgment. |
| Proposed methodology changes | Keep final-artifact shape separate from conversational narration when recording task fidelity; no rubric or runner change needed for this pilot. |
