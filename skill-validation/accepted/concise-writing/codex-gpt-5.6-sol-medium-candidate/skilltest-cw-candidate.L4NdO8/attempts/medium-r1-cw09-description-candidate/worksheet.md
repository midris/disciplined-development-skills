# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-09/description |
| Scenario ID | cw-09-description-candidate-medium |
| Scenario purpose | CW-09 description classification diagnostic with candidate CW description; not native discovery. |
| Run ID | 20260909T005217442Z-cw-09-description-candidate-medium-5696868c-3869-4e32-a51f-a1d9e53be1f9-rsfjdqox |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-09T00:52:17.442Z |
| Finished | 2026-09-09T00:52:31.403Z |
| Duration seconds | 13.961 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | e95f3d64d281c689cc942e5e43c4148ac2cce9c90f26b5d07dd34249bd8b4164 |
| Prompt template | prompt-template.txt | a61fffa973d1e4cc884d868632e23b22f3dd4e336e71bce1dd594d139cfa172b |
| Rendered prompt | prompt.txt | 5396ef63d2d59a5c479d20b73f52a209e3cc971f56030b1ea11d6fabb50b854c |
| Fixture | .agents/skills/requesting-code-review/SKILL.md | d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8 |
| Fixture | .agents/skills/requesting-code-review/code-reviewer.md | 5eca5fcfd48a50e0a526ce5ffd64bf625d6b81bb46d11795274dae451fe6ffd4 |
| Fixture | .agents/skills/writing-plans/SKILL.md | 48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2 |
| Fixture | .agents/skills/writing-plans/plan-document-reviewer-prompt.md | aa728b96aad603c8be28875a4305637f6c984aa81ffcadcb13e743202fa2a0c7 |
| Fixture | .git/HEAD | f6f2b945f6c411b02ba3da9c7ace88dcf71b6af65ba2e0d89aa82900042b5a10 |
| Fixture | .git/config | cae33efdb02cf774435c1ff9cb16bcc1014606908530c6e1dc727615fe3e8cda |
| Fixture | descriptions/adversarial-review-loop.txt | 38843f7718501f52116bfd4f95a6640cb16b560851767df540c808a1ed18cefa |
| Fixture | descriptions/concise-writing.txt | 642b8ec050a0cc782e391fcf88ca7414186e28fa7ba8a145f313097f9c75f0cd |
| Fixture | descriptions/superpowers-writing-skills.txt | 5504b0825ec458aa8c20e9a55c6a932b36849e261a97aaf98af366e19a937154 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/pilot/cw-09/description/rubric.md | 0dcbc616c8f208af3cd015fc1fa607c96b140d34f6a69414012471201a80da19 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| Authoring composition | Required selections | PASS | [final][final] | Selects concise-writing and superpowers:writing-skills. |
| Authoring composition | Exclude unrelated selections | PASS | [final][final] | No adversarial-review-loop or other selection. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated consumer | N/A | Frozen rubric | Ordinary prose/JSON presentation is not a deterministic protocol. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Requested description loading | PASS | [trace][trace] | All three full descriptions read; no skill bodies accessed. |
| Deliverable and boundaries | PASS | [trace][trace] | Compact alphabetical JSON array only; read-only fixture task. Selection is faithful to the actual candidate description, which has no authoring exclusion. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: compact array is unambiguous. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | Both intended composition criteria pass; faithful to candidate inputs. Description diagnostic, not native discovery or authoring execution. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Complete visible trace cannot establish absence of hidden provider inputs. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command/provider exit 0; exact argv, frozen inputs, artifact/prelaunch hashes, protected fixtures and owned cleanup verified. Complete visible trace, empty provider/command stderr; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260909T005217442Z-cw-09-description-candidate-medium-5696868c-3869-4e32-a51f-a1d9e53be1f9-rsfjdqox/final.txt
[trace]: ../../runs/skilltest-runs/20260909T005217442Z-cw-09-description-candidate-medium-5696868c-3869-4e32-a51f-a1d9e53be1f9-rsfjdqox/stdout.txt
