# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/writing-explicit-rationale/wer-08 |
| Scenario ID | wer-08 |
| Scenario purpose | Test whether the rationale policy applies outside software by moving a repeatedly requested cause into the durable nonprofit policy. |
| Run ID | 20260904T115537576Z-wer-08-f31577c7-0920-4b7e-8ccc-d73960a81ddc-xck24ppa |
| Provider | codex |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-04T11:55:37.576Z |
| Finished | 2026-09-04T11:55:55.867Z |
| Duration seconds | 18.291 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 801ebf78c50d9c34ba193a90b719d2e556eeb73fdfcf50781da8289340febb16 |
| Prompt template | prompt-template.txt | 0b5c3b220cd085cc01e1c06cab3156e838b8683a33c30034e9a96ed644189260 |
| Rendered prompt | prompt.txt | a66f2a60153fe1ef13316b0585933a1f63a97b0d064c80e71880d90971bcfa1f |
| Fixture | skills/writing-explicit-rationale/SKILL.md | 97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/writing-explicit-rationale/wer-08/rubric.md | 98781f268c1b7f4d6052c896ca6bbc257377d2daff8a493ec9d9325121ef73ec |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| WER-I1 | Add the supplied winter-shelter-demand cause for the temporary $5,000 cap without changing or competing with the existing policy decision. | PASS | final.txt:3; prompt.txt:9-20 | The proposed sentence states that winter-shelter demand has outgrown the ordinary per-grant limit and ties it directly to the temporary increase. Its added acceptance framing restates existing controls but does not alter the owned cause or decision. |
| WER-I2 | Place the missing rationale in the `Emergency grants` policy section adjacent to the temporary cap. | PASS | final.txt:1-3; prompt.txt:9-17 | The response directs insertion immediately after the section's first sentence, which is the temporary-cap sentence. |
| WER-I3 | Keep the policy as the single authoritative rationale home rather than using chat, minutes, or a newsletter. | PASS | final.txt:1-3; prompt.txt:16-22 | The response supplies a policy insertion and creates no competing rationale home. It need not explicitly reject the alternatives. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer applies. | N/A | prompt.txt; rubric.md | The location and policy prose are interpreted by a maintainer, and the rubric expressly permits equivalent wording and formatting. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Return only the durable policy change and insertion location without rewriting the existing policy or narrating the process. | PASS | final.txt:1-3 | The response contains only an insertion location and proposed inserted text. It does not rewrite the quoted policy or add process narration. The new sentence unnecessarily repeats the existing aggregate limit, monthly review, and sunset controls and adds acceptance framing; the rubric classifies such non-material surplus as a task-fidelity note. |

## Readability

| Observation | Evidence |
|---|---|
| The insertion location and causal sentence are clear, though the sentence is longer than necessary because it restates controls already present immediately below it. | final.txt:1-3 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | The run is mechanically complete and judgeable. WER-I1 through WER-I3 pass: the response puts the correct winter-shelter cause beside the temporary cap in the durable policy and creates no competing rationale home. WER-I4 is not independently exercised. The extra acceptance framing and repeated controls do not change the owned rationale and remain task-fidelity observations under the rubric. No deterministic protocol applies. |
| Disposition | Accepted by the owner on 2026-09-04 as the latest judgeable `PASS` baseline with a non-blocking task-fidelity observation. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None affecting judgment. WER-I4 is not independently pressured because the scenario supplies no related decision sites for a batched audit. |
| Scenario defects | None observed. The prompt supplies the durable artifact, missing cause, repeated-review pressure, and rejected non-authoritative homes; the rubric clearly separates semantic failure from non-material task-fidelity surplus. |
| Proposed methodology changes | Preserve the distinction between the owning semantic verdict and task-fidelity observations: unnecessary surplus does not flip the owner verdict when the scenario rubric expressly makes it non-material. No runner or worksheet change is needed. |
