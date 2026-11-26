# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-11/description |
| Scenario ID | cw-11-description-candidate-medium |
| Scenario purpose | Description-only selection for supporting-reference authoring; not native discovery. |
| Run ID | 20260909T015031562Z-cw-11-description-candidate-medium-eb69a3b9-9ec5-4f52-810d-5fe8a6184aeb-wacba2md |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-09T01:50:31.562Z |
| Finished | 2026-09-09T01:50:49.992Z |
| Duration seconds | 18.43 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | eec356adb82bc1c28044cca69bc09ad802cd456e2aadf36f9f4e37f968c9d357 |
| Prompt template | prompt-template.txt | 441dae342fb53387b0effde82a183ec4a26018437f1fb1e3e906efceba956e95 |
| Rendered prompt | prompt.txt | e2e8f538f65129cac3dfc745f480477323da7e43d42d289e26c8422df96f9c33 |
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
| Rubric | skill-validation/pilot/cw-11/description/rubric.md | 784c4784829fda7647384974f508973e84ede733517dd36536d9a76ec9ffba34 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| Description selection | Select CW and writing-skills, no unrelated loop | PASS | [final][final] | Exactly concise-writing and superpowers:writing-skills. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated consumer | N/A | Frozen rubric | Ordinary prose/JSON presentation is not a deterministic protocol. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Description read and source faithfulness | PASS | [trace][trace] | All three complete supplied descriptions returned; expected pair matches actual triggers. |
| JSON array only | FAIL | [trace][trace], item_0 | Extra I’ll read only the three supplied descriptions and match them to the request announcement. |
| Boundaries | PASS | [trace][trace] | No body reads, mutation, outside access, network or dispatch. |

## Readability

| Observation | Evidence |
|---|---|
| PASS — exact, compact selection. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | Selection diagnostic passes; extra announcement fails separate JSON-only task fidelity. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Complete visible trace cannot establish absence of hidden provider inputs. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command/provider exit 0; exact argv, frozen inputs, artifact/prelaunch hashes, protected fixtures and owned cleanup verified. Complete visible trace, empty provider/command stderr; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260909T015031562Z-cw-11-description-candidate-medium-eb69a3b9-9ec5-4f52-810d-5fe8a6184aeb-wacba2md/final.txt
[trace]: ../../runs/skilltest-runs/20260909T015031562Z-cw-11-description-candidate-medium-eb69a3b9-9ec5-4f52-810d-5fe8a6184aeb-wacba2md/stdout.txt
