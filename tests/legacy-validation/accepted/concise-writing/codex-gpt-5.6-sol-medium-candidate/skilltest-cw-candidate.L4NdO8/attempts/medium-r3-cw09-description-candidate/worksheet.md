# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-09/description |
| Scenario ID | cw-09-description-candidate-medium |
| Scenario purpose | Description-only authoring selection diagnostic, not native discovery or body application. |
| Run ID | 20260909T014926611Z-cw-09-description-candidate-medium-4a3a4cb2-fddc-4ca3-a386-56583efe821f-mhy4hidh |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-09T01:49:26.611Z |
| Finished | 2026-09-09T01:49:42.880Z |
| Duration seconds | 16.269 |

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
| Rendered prompt | prompt.txt | a199c4aa4a8f9abce13ff73f73effc02964b060d38e6c0b01df60ca3cd300900 |
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
| Description selection | Select CW and writing-skills, no unrelated loop | PASS | [final][final] | Exactly concise-writing and superpowers:writing-skills. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated consumer | N/A | Frozen rubric | Ordinary prose/JSON presentation is not a deterministic protocol. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Supplied descriptions and faithful answer | PASS | [trace][trace] | All three exact descriptions returned; candidate CW includes authoring prose, not the baseline exclusion. |
| Output and boundaries | PASS | [trace][trace] | Compact alphabetical JSON array only; no skill-body reads, mutation, outside access, network or dispatch. |

## Readability

| Observation | Evidence |
|---|---|
| PASS — exact, compact selection. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | Expected selection is faithful to the candidate description and authoring-owner trigger. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Complete visible trace cannot establish absence of hidden provider inputs. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command/provider exit 0; exact argv, frozen inputs, artifact/prelaunch hashes, protected fixtures and owned cleanup verified. Complete visible trace, empty provider/command stderr; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260909T014926611Z-cw-09-description-candidate-medium-4a3a4cb2-fddc-4ca3-a386-56583efe821f-mhy4hidh/final.txt
[trace]: ../../runs/skilltest-runs/20260909T014926611Z-cw-09-description-candidate-medium-4a3a4cb2-fddc-4ca3-a386-56583efe821f-mhy4hidh/stdout.txt
