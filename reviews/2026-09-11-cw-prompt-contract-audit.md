# CW prompt audit against the baseline skill

> **Abandoned testing process — historical reference only (2026-09-11).**
> Testing-framework instructions, approvals and pending work below are no longer current. Follow the [new framework spec](../plans/specs/2026-09-11-model-driven-skill-testing-framework.md) and [new testing plan](../plans/2026-09-11-model-driven-skill-testing.md).
> The original text is preserved as history; this notice does not retire existing runner tooling or core skills.


Status: source-only review and actionable prompt repairs completed on 2026-09-11; no provider execution or historical rescoring.
The owner requested checking all CW testing prompts for instructions that conflict with the skill/specification or introduce inappropriate scoring interpretations.
This extends prompt inspection beyond CW-02/CW-19; it does not authorize other-skill catalog work, provider calls, historical rescoring or rubric replacement.
The complete [baseline skill](../skills/concise-writing/SKILL.md) governs, with the [derived specification](../plans/specs/2026-09-10-cw-baseline-specification.md) and the owner's whole-document clarification.

## Scope and evidence boundary

Read all 67 original `prompt.md` paths under `skill-validation/pilot/cw-*/` and `skill-validation/scenarios/concise-writing/`: 66 distinct contents.
The inventory below records every path and its content hash group.
Also inspected the CW-22/CW-23 project guidance and source documents, twelve description fixtures used by CW-09/CW-11/CW-17/CW-18, two shared upstream reviewer templates, and the runner's prompt preparation/transport code.
Resolved prompt references in all 86 original checked-in CW configurations plus four opt-in repaired configurations; the [expanded config map](/private/tmp/cw-scoring-rebuild-gep1e4ek/cw-prompt-audit-config-map-v2.json) records 90 paths and hashes.
The configuration inventory includes `pilot/efforts/**/cw*.json`, `pilot/cw-*/**/test*.json` and `scenarios/concise-writing/*/test*.json`; the first audit missed the last group's 17 original files.
All configuration prompt paths resolve to the 67 audited originals or four neutral revisions.
The six added CW-17/CW-18 description fixtures match the already-reviewed CW-09 description bytes.
Several checked-in effort configurations still reference the older prompt families; their existence does not establish which inputs were used by the latest scratch batches.
Verify actual retained input hashes at the permitted assessment checkpoint before applying rebuilt criteria.

The initial source audit did not open old rubrics, catalog scoring descriptions, worksheets, prior judgments, subject outputs, candidate skill bodies or completed-result sections.
During the subsequent plan/audit review, an unbounded plan read exposed historical assessment summaries beyond the permitted handoff.
Old rubric files and retained subject outputs remain unopened; fresh derivation must continue in a clean session, as recorded in the active handoff.
The prompt repairs and source inventory do not rely on those historical judgments.
Historical run-bundle copies, temporary batch configurations, other skills' scenario catalogs and arbitrary model-side system instructions are outside this inventory.
This is an audit of the repository's CW task/contract/routing prompts and the inspected shared inputs, not a claim that all historical evaluator instructions or every assembled run have been reviewed.
The old-rubric and retained-output checkpoints still apply.

## Conclusion

The ordinary prose-editing prompts do not mandate sentence-preserving edits, ban useful repetition or impose a minimum compression ratio.
Their source text may contain padding candidates, but it does not decide which passages lack reader value in the complete result.
The reviewed CW-02 and CW-19 specification prompts permit complete-document rewriting without changing necessary meaning or operational requirements.
Their current prompt text needs no repair for the owner's whole-document finding.

There are three concrete prompt/design limitations in older families and two recurring attribution boundaries to retain in scoring.
These findings do not establish that any subject response or prior grade was wrong; this audit does not reassess observations.
All 67 original prompt files and all original configuration routes remain unchanged.
Four `prompt-v2.md` files and four opt-in configurations remove the answer cue without redefining retained inputs; their task requests, fixtures and model settings are unchanged.
These are prepared input repairs, not approval to collect observations or reuse old scoring for a new prompt version.

## Findings and dispositions

### 1. Boolean examples can cue an answer in detailed-explanation contract tests

[CW-17 contract](../skill-validation/pilot/cw-17/contract/prompt.md) and [CW-18 contract](../skill-validation/pilot/cw-18/contract/prompt.md) show `{"apply_to_detailed_explanation":false}` before saying to set the value to true or false.
The combined [CW-17](../skill-validation/scenarios/concise-writing/cw-17/prompt.md) and [CW-18](../skill-validation/scenarios/concise-writing/cw-18/prompt.md) scenario definitions use the same default.
This supplies a directional example in a task intended to elicit an interpretation of the skill.
It is a potential priming risk, not an instruction requiring false and not measured evidence of an effect.
The baseline does not exclude detailed responses; requested useful detail and examples are compatible with CW.
A false answer must not be assumed correct merely because the request asks for detail.

Completed: the separately versioned prompts describe the required boolean in prose without a populated answer; the combined variants also describe the selected-skills array without a sample result.
Their new configuration IDs and prompt paths select the revisions explicitly; no historical configuration was retargeted.
Use these neutral versions if those contract tests are later approved for reuse, and disclose the original cue when interpreting retained observations.
No new run is authorized.
The [routine CW-17](../skill-validation/pilot/cw-17/routine/prompt.md) and [specification CW-18](../skill-validation/pilot/cw-18/specification/prompt.md) tasks instead exercise useful detailed explanations and have no populated answer cue.

### 2. Authoring-method decisions cannot become CW-owned effectiveness requirements

The older CW-13/CW-14 current-DD/no-DD multiple-choice prompts ask which skill leads authoring/validation and whether to deploy or merge after particular checks.
Their routine variants also ask for a deployment decision and next validation after editing a skill warning or shipped reference.
Those choices belong to the supplied authoring guidance, while baseline CW explicitly excludes skill/reference authoring.
An explicit CW-load instruction creates a controlled loaded condition; it does not establish that CW should discover itself for the excluded task or own the other skill's validation decisions.
The half-length demand in the quoted senior-reviewer pressure is scenario context, not a general CW compression target.

The current [CW-13 specification](../skill-validation/pilot/cw-13/specification/prompt.md) and [CW-14 specification](../skill-validation/pilot/cw-14/specification/prompt.md) stop at guidance selection and distinguish inspection from selection.
They therefore permit assessing CW's exclusion without requiring the model to demonstrate another skill's complete authoring process.
No prompt change is needed for those selection tasks.
For older mixed tasks, keep any measured prose contribution, exclusion behavior and other-skill decision correctness distinct; do not use the validation answer as a CW failure criterion.
The audit does not judge the correctness of the upstream authoring lifecycle itself.

### 3. Older excerpts do not supply the complete context used by rebuilt scenarios

Older [CW-02 current-DD](../skill-validation/pilot/cw-02/current-dd/prompt.md), [no-DD](../skill-validation/pilot/cw-02/no-dd/prompt.md) and [scenario definition](../skill-validation/scenarios/concise-writing/cw-02/prompt.md) refer to “Delivery ordering” below but do not supply that section.
The [CW-02 specification prompt](../skill-validation/pilot/cw-02/specification/prompt.md) supplies both sections.
Likewise, the older CW-08 excerpt names Appendix A and Appeals without their content, while the [CW-08 specification prompt](../skill-validation/pilot/cw-08/specification/prompt.md) supplies all three sections.

The older tasks can test preservation of a reference in an excerpt; they cannot establish reader effectiveness for the unseen destination or preservation of facts not supplied to the subject.
Do not apply the expanded source inventory to an output generated from the older partial prompt.
Preserve the historical inputs and use the reviewed complete prompts for prospective full-document comparisons.
This is a source-boundary limitation, not evidence that the old subjects should have invented the missing sections.

### 4. Formatting and explicit authoring-owner extraction have narrower evidentiary scope

CW-09/CW-11 request alphabetical compact JSON with no whitespace; CW-10/CW-12 require key order and a verbatim ownership quotation or `null` when absent.
These response-shape requirements do not establish an authenticated byte-level consumer or a CW concision promise.
CW-10/CW-12 explicitly permit absent ownership; baseline CW's lack of an authoring-owner sentence is not itself a skill failure.
Description routing tests establish selection from supplied descriptions, not whether normal development work would spontaneously discover and load the skill.

Keep JSON shape, key order and exact quotation in task fidelity unless a real consumer requirement independently makes protocol scoring applicable.
Evaluate the permitted absent-owner answer against the complete skill rather than inventing a required delegation statement.
The current explicit instructions are not inherently contradictory; their scoring interpretation must stay within that scope.

### 5. Task-specific structure and process instructions constrain the task, not CW generally

CW-02 asks for both source sections; CW-08 asks for three sections; CW-17 asks for two worked examples.
Those are legitimate requested deliverables and detail levels, not evidence that CW always requires that layout or those examples.
Meaning may still be consolidated or relocated within the requested artifact.
“Return only” restricts the requested final deliverable; it does not prove hidden internal processes occurred or failed, and absence of an unsolicited commentary is not evidence of uncertainty mishandling.

[CW-22](../skill-validation/pilot/cw-22/specification/prompt.md) asks for an actual file diff and comparison with an approved design.
Its fixture distinguishes future implementation checks from checks performed by the prose editor.
This is a legitimate observable editing task; it does not mean every read-only CW task must emit a draft/diff or execute implementation tests.
[CW-23](../skill-validation/pilot/cw-23/specification/prompt.md) explicitly mandates merging two named subsections, maintaining navigation and committing in a disposable fixture.
That setup exercises CW in a composed workflow; success does not prove CW independently discovered over-sectioning, and Git/link-maintenance correctness must not be attributed wholesale to CW.
No contradictory compression requirement was found in the inspected CW-22/CW-23 project guidance.

## Repairs and review disposition

| Finding | Disposition |
|---|---|
| Populated boolean answer cue | Fixed in all four versioned prompt revisions below; four opt-in configurations select them. |
| Incomplete configuration inventory | Added the omitted 17 scenario configurations and verified their prompt references; 90 configurations now covered including the four revisions. |
| Authoring ownership, JSON shape and task-process attribution | Assessment boundaries retained explicitly above; current guidance-selection prompts need no edit. Old rubric reconciliation remains behind the original checkpoint. |
| Partial older source excerpts | Keep their original evidence scope; use the already-reviewed complete prompts when full-document context is required. The actual retained-input match must be checked at assessment time. |
| Scope/status drift in the plan and report | Updated repair status and separated completed source work from later evidence checks; current prompt labels are not treated as execution provenance. |

| Revised prompt | Opt-in configuration |
|---|---|
| [skill-validation/pilot/cw-17/contract/prompt-v2.md](../skill-validation/pilot/cw-17/contract/prompt-v2.md) | [skill-validation/pilot/efforts/medium/cw17-contract-v2.json](../skill-validation/pilot/efforts/medium/cw17-contract-v2.json) |
| [skill-validation/scenarios/concise-writing/cw-17/prompt-v2.md](../skill-validation/scenarios/concise-writing/cw-17/prompt-v2.md) | [skill-validation/scenarios/concise-writing/cw-17/test-v2.json](../skill-validation/scenarios/concise-writing/cw-17/test-v2.json) |
| [skill-validation/pilot/cw-18/contract/prompt-v2.md](../skill-validation/pilot/cw-18/contract/prompt-v2.md) | [skill-validation/pilot/efforts/medium/cw18-contract-v2.json](../skill-validation/pilot/efforts/medium/cw18-contract-v2.json) |
| [skill-validation/scenarios/concise-writing/cw-18/prompt-v2.md](../skill-validation/scenarios/concise-writing/cw-18/prompt-v2.md) | [skill-validation/scenarios/concise-writing/cw-18/test-v2.json](../skill-validation/scenarios/concise-writing/cw-18/test-v2.json) |

The four revised prompts passed a full source diff review: only response-shape wording changed, and the booleans remain determined by the supplied contract.
The runner's real `load_config` function accepted all four new configurations without allocating a run or invoking a provider.
The original prompt hashes still match the inventory below.

## Other families checked

| Family | Prompt interpretation supported by the baseline |
|---|---|
| CW-01 | Ordinary tightening; judge the complete export-status document, not a fixed list of sentences to delete. Explicit load is not discovery evidence. |
| CW-03 | Both the short and longer guides permit revision; repetition can serve issuing/troubleshooting/navigation functions. No rule requires deleting a repeated fact simply because it appears twice. |
| CW-04 | Short or heavily subdivided help-page inputs do not prescribe a maximum heading count. Findability and whole-page usefulness decide. |
| CW-05 | Authoritative notes distinguish policy from unsupported advice in the editable draft; this does not license losing source-grounded meaning. |
| CW-06 | Inflated emphasis and repeated API-key statements are candidates for reader-function assessment, not a prohibited-word list. |
| CW-07 | The conditional `BLOCKED` response applies if a required input truly is unavailable. The complete release-notice source is supplied; CW has no unconditional requirement to invent a missing plan or parent procedure. |
| CW-17/CW-18 routine and specification tasks | Detailed explanation, worked examples and requested files are within the declared prose scope. Preserve usefulness; do not impose a detailed-response exclusion. |
| CW-19 | Complete operational source, preservation request and no command execution; no instruction requires original sentence structure or a fixed compression rate. |
| CW-20 | “Where doing so improves it” explicitly permits already-effective wording to remain. No forced shortening. |
| CW-21 | Conflicting editorial notes create a context for judgment, not proof the subject is uncertain. The requested editorial note permits reporting a real unresolved issue; do not force a particular doubt or keep/cut answer solely from the setup. |

## Shared inputs and remaining exposure limits

The runner's [workspace preparation](../skill-validation/runner/src/skilltest/workspace.py) copies the declared prompt and substitutes workspace/fixture/evidence paths.
Its [input check](../skill-validation/runner/src/skilltest/runtime.py) compares those bytes, and [provider transport](../skill-validation/runner/src/skilltest/providers.py) passes the prompt bytes to the CLI.
No CW-specific scoring instructions are appended by those inspected paths.
This is a code inspection, not a provider qualification run or a claim about all hidden harness messages.

The checked-in `inputs/dd/concise-writing/SKILL.md` matches the baseline hash, and the CW description fixtures retain the authoring exclusion.
The shared plan-review and code-review templates concern their upstream workflows; they supply no additional CW grading contract merely because a fixture includes them.
Candidate body/description contents and historical assessment prompts were not inspected.
If those evaluator inputs contain scenario-specific old criteria, inspect them only after the fresh assessments have been recorded under the agreed checkpoint.

## Next actions

- [x] Audit repository CW prompts and inspected shared inputs against the complete skill and derived specification.
- [x] Record prompt identity, source-boundary limitations and prospective repairs without changing frozen inputs or reading old grades.
- [x] Create and review all four neutral-boolean prompt revisions and their opt-in configurations, preserving originals.
- [x] Complete the configuration inventory, including the 17 scenario definitions omitted from the first pass.
- [ ] At retained-evidence selection, verify the actual CW-02/CW-19 task bytes against the source version before applying the new rubric.
- [x] Continue CW-19 derivation in a clean session using the accumulated CW-02 feedback; the [v1 criteria/examples draft](/private/tmp/cw-scoring-rebuild-gep1e4ek/cw-19-criteria-v1-draft.md) is ready for owner review.
- [ ] Finish both criteria/example reviews before freezing or assessing retained outputs.
- [ ] At the later permitted checkpoint, compare evaluator prompts/old rubrics with these findings and the new assessments; do not import them into fresh derivation now.

## Prompt inventory

This frozen inventory records the 67 original prompt paths, not the four new revisions linked above.
Each row groups byte-identical files; every listed file was read through its group's complete content.
Hashes and configuration mappings are also retained in the [scratch inventory](/private/tmp/cw-scoring-rebuild-gep1e4ek/cw-prompt-audit-inventory.json).

| Group | SHA-256 | Prompt paths |
|---|---|---|
| 1 | `ee17c7de4730f7dd0190e75e4d76292bf914f202dfdb6bc7ee160b5a65877e3e` | [skill-validation/pilot/cw-01/current-dd/prompt.md](../skill-validation/pilot/cw-01/current-dd/prompt.md) |
| 2 | `56a9c1f62782b81ed01801acaeef034534abb21ec55963863e941f4d1c10de86` | [skill-validation/pilot/cw-01/discovery/prompt.md](../skill-validation/pilot/cw-01/discovery/prompt.md)<br>[skill-validation/pilot/cw-01/no-dd/prompt.md](../skill-validation/pilot/cw-01/no-dd/prompt.md) |
| 3 | `31f27f12fe7a086af0aa7495e328304b886551ca1a0e0880cfe103b288a0c380` | [skill-validation/pilot/cw-01/specification/prompt.md](../skill-validation/pilot/cw-01/specification/prompt.md) |
| 4 | `71adee8f59521ef31a1175c1125abe888d3cea4b5ffc549aca57fe448d3185df` | [skill-validation/pilot/cw-02/current-dd/prompt.md](../skill-validation/pilot/cw-02/current-dd/prompt.md) |
| 5 | `370abfa623d1122d1f811452953cec1d023c7c96cbaa67d0d2849b40b7715add` | [skill-validation/pilot/cw-02/no-dd/prompt.md](../skill-validation/pilot/cw-02/no-dd/prompt.md) |
| 6 | `7d05a7071a8b5633311c7c1c45b2186673575ac2bc3970542a1dc6fb3405cc3c` | [skill-validation/pilot/cw-02/specification/prompt.md](../skill-validation/pilot/cw-02/specification/prompt.md) |
| 7 | `8586e43b9ed114e27eabc3164cb1cc0aeb665ef1e61d64b798c831919484194b` | [skill-validation/pilot/cw-03/current-dd/prompt.md](../skill-validation/pilot/cw-03/current-dd/prompt.md) |
| 8 | `f11f66645ab5855acdc495a3361b03da1c532ff9e8471e8057c661544648823e` | [skill-validation/pilot/cw-03/no-dd/prompt.md](../skill-validation/pilot/cw-03/no-dd/prompt.md) |
| 9 | `f027c205c4e637896d4b3d207d0785904e3dd6b214460e241bc8f3815ff87eff` | [skill-validation/pilot/cw-03/routine/prompt.md](../skill-validation/pilot/cw-03/routine/prompt.md) |
| 10 | `cf59ee2e5d52d0a1230bd1449b414cd9b8a25ba8b5f075da23be1af6c5767320` | [skill-validation/pilot/cw-04/current-dd/prompt.md](../skill-validation/pilot/cw-04/current-dd/prompt.md) |
| 11 | `f9f9a0abaf05fee1d82a74ab8a3baf6a86b07875c61a242c402a42ee314b9c11` | [skill-validation/pilot/cw-04/no-dd/prompt.md](../skill-validation/pilot/cw-04/no-dd/prompt.md) |
| 12 | `dc4a67892150cf773985fe2a95a4247291ea15146b1be0f5b817c778901d6f3f` | [skill-validation/pilot/cw-04/specification/prompt.md](../skill-validation/pilot/cw-04/specification/prompt.md) |
| 13 | `a0a32985b30c2a03872868e366d59f45b6d29d791a7fd9322472c50a49c2fd04` | [skill-validation/pilot/cw-05/current-dd/prompt.md](../skill-validation/pilot/cw-05/current-dd/prompt.md) |
| 14 | `52d1e47b62b2a318a5dab98e7562ee31160c0ed2fd12ed088882bd89bccd8d86` | [skill-validation/pilot/cw-05/no-dd/prompt.md](../skill-validation/pilot/cw-05/no-dd/prompt.md) |
| 15 | `bb72c140218df2ca53f6b254f7a7c780418eb3a0b4a05e94f505f58d4913bcbd` | [skill-validation/pilot/cw-06/current-dd/prompt.md](../skill-validation/pilot/cw-06/current-dd/prompt.md) |
| 16 | `002b15f13c50c55362ee8d9624c8a8aee6981fd956f9b13892d5e1c62a7e8886` | [skill-validation/pilot/cw-06/no-dd/prompt.md](../skill-validation/pilot/cw-06/no-dd/prompt.md) |
| 17 | `f30fad68bd17bc9d96b1dce1f61ed65438ef7e471a850f9c91039439f59cf0ac` | [skill-validation/pilot/cw-07/current-dd/prompt.md](../skill-validation/pilot/cw-07/current-dd/prompt.md) |
| 18 | `dca99819cfbef27c81f3524284ed47e4a948f15b82f5b296d13c042f28860ed4` | [skill-validation/pilot/cw-07/no-dd/prompt.md](../skill-validation/pilot/cw-07/no-dd/prompt.md) |
| 19 | `00a6e1d588d80fe97a4e36af638c7a6193294ac9922e3c1c977adbb7425d8e95` | [skill-validation/pilot/cw-08/current-dd/prompt.md](../skill-validation/pilot/cw-08/current-dd/prompt.md) |
| 20 | `7b0828c0e2919ba57bb12e82ff30f1f457a6cf463eecd8f055c537f929892d4a` | [skill-validation/pilot/cw-08/no-dd/prompt.md](../skill-validation/pilot/cw-08/no-dd/prompt.md) |
| 21 | `7d08420b0f2bafe85dc1ed1f00081cfa84c9caef334286a0954d77dd02c13ab8` | [skill-validation/pilot/cw-08/specification/prompt.md](../skill-validation/pilot/cw-08/specification/prompt.md) |
| 22 | `a61fffa973d1e4cc884d868632e23b22f3dd4e336e71bce1dd594d139cfa172b` | [skill-validation/pilot/cw-09/description/prompt.md](../skill-validation/pilot/cw-09/description/prompt.md) |
| 23 | `4c3d20a32f6de1ff10d3ccfbc383730f5541d1e69fcbb942fc5d183b4a46543a` | [skill-validation/pilot/cw-10/contract/prompt.md](../skill-validation/pilot/cw-10/contract/prompt.md) |
| 24 | `441dae342fb53387b0effde82a183ec4a26018437f1fb1e3e906efceba956e95` | [skill-validation/pilot/cw-11/description/prompt.md](../skill-validation/pilot/cw-11/description/prompt.md) |
| 25 | `10fe1ea50b5bfba895b82515a88d4ed460395e0471cd7c68f443d3c7d3f6d648` | [skill-validation/pilot/cw-12/contract/prompt.md](../skill-validation/pilot/cw-12/contract/prompt.md) |
| 26 | `73b6c0e7880d7b2d35e76d5c18f193e86a51598a4dc4eaf0107a54ef8b9b63f5` | [skill-validation/pilot/cw-13/current-dd/prompt.md](../skill-validation/pilot/cw-13/current-dd/prompt.md) |
| 27 | `e12cbb9bd7c50233252fba98365ef5b996de8fb4e4f6c7ac5906137fef4ffbc8` | [skill-validation/pilot/cw-13/discovery/prompt.md](../skill-validation/pilot/cw-13/discovery/prompt.md) |
| 28 | `63e3e40f4246cefc2746cf2dbea78b5c72c5b9c9b87f56d9705b170a2fa78bae` | [skill-validation/pilot/cw-13/no-dd/prompt.md](../skill-validation/pilot/cw-13/no-dd/prompt.md) |
| 29 | `b7d0d264f627694eee67613e90238af4d94167f6627bc92a3dccda48f34a55ee` | [skill-validation/pilot/cw-13/routine/prompt.md](../skill-validation/pilot/cw-13/routine/prompt.md) |
| 30 | `506a2cba0dfa11ffcaf910b5e6c7b0fe8192c2f38b7da6edcdbe137da12d2e53` | [skill-validation/pilot/cw-13/specification/prompt.md](../skill-validation/pilot/cw-13/specification/prompt.md) |
| 31 | `5c4a41eb242ff77eba4ff71a6c4320fc5ee3d5d4b5a123c414ffe4cb63f2fec8` | [skill-validation/pilot/cw-14/current-dd/prompt.md](../skill-validation/pilot/cw-14/current-dd/prompt.md) |
| 32 | `2dca0926ef4a374eb73044a6bff94b1e508afc4934224900a153e990605230b7` | [skill-validation/pilot/cw-14/discovery/prompt.md](../skill-validation/pilot/cw-14/discovery/prompt.md) |
| 33 | `7cd4d8286cf8396a6a8b5ad44d8c424c2ddb8a55530537af1f6f939ed7c9a99b` | [skill-validation/pilot/cw-14/no-dd/prompt.md](../skill-validation/pilot/cw-14/no-dd/prompt.md) |
| 34 | `bd9081b51537a0a406d0e2822cf4cc24fffcd3827e25ac9f090c7fd28369e507` | [skill-validation/pilot/cw-14/routine/prompt.md](../skill-validation/pilot/cw-14/routine/prompt.md) |
| 35 | `5dc34035f0dde82bc8ee8f74c29f1f35ee4e38ab6bd9b85430a9451cfbb72704` | [skill-validation/pilot/cw-14/specification/prompt.md](../skill-validation/pilot/cw-14/specification/prompt.md) |
| 36 | `a2770d0bf427eb95c6e64de16caed56f1cb873527820aabc8a7d6624f7583384` | [skill-validation/pilot/cw-17/contract/prompt.md](../skill-validation/pilot/cw-17/contract/prompt.md) |
| 37 | `ce90fecc0cc9a2a764863b797d50ef232e5b013437cf320d8251009bc5c4cd1c` | [skill-validation/pilot/cw-17/discovery/prompt.md](../skill-validation/pilot/cw-17/discovery/prompt.md) |
| 38 | `0b1e5ffe566fdf4f4c897fde5d2cde5437630665864978aedd938151539eecf4` | [skill-validation/pilot/cw-17/routine/prompt.md](../skill-validation/pilot/cw-17/routine/prompt.md) |
| 39 | `c8fbe6b2932e5d54496274de0d0c96f7d897cdda3e97953455ecd3765dfc0811` | [skill-validation/pilot/cw-18/contract/prompt.md](../skill-validation/pilot/cw-18/contract/prompt.md) |
| 40 | `f65c78cdf2950877618f2fc14a10f3baa5c03a78f1aafef8c921fac477d0c52d` | [skill-validation/pilot/cw-18/discovery/prompt.md](../skill-validation/pilot/cw-18/discovery/prompt.md) |
| 41 | `90691f55577b59f38f1c309c04717fbca63b843f9fdbcce083dad19de8f2d026` | [skill-validation/pilot/cw-18/routine/prompt.md](../skill-validation/pilot/cw-18/routine/prompt.md) |
| 42 | `3de1e1beaf52395e08fea746e96ac1f73bd7e221eec20ff8587411de6c0e8d12` | [skill-validation/pilot/cw-18/specification/prompt.md](../skill-validation/pilot/cw-18/specification/prompt.md) |
| 43 | `4a80e4c7a19286397624bd2e00d398d1d3c2568fdad1c9032fe6e71f1c84bf80` | [skill-validation/pilot/cw-19/current-dd/prompt.md](../skill-validation/pilot/cw-19/current-dd/prompt.md) |
| 44 | `c9e33a040244fdb810fc6c268d7f52ba8c657d40ecb1df367fc1dec7aad98fd4` | [skill-validation/pilot/cw-19/no-dd/prompt.md](../skill-validation/pilot/cw-19/no-dd/prompt.md) |
| 45 | `f6acf72cf901651cb95614e38a99464848608f02b143513ae5a617c396251b2f` | [skill-validation/pilot/cw-19/specification/prompt.md](../skill-validation/pilot/cw-19/specification/prompt.md) |
| 46 | `2bf6bf2dbee2f757feaf44c6f729990f075e9ef74ab64d99198e07cb9679dd27` | [skill-validation/pilot/cw-20/routine/prompt.md](../skill-validation/pilot/cw-20/routine/prompt.md) |
| 47 | `f3cd20733759fd809cbb44ddf54d28e3df54b7a855c72fb13d1f50895def7592` | [skill-validation/pilot/cw-21/specification/prompt.md](../skill-validation/pilot/cw-21/specification/prompt.md) |
| 48 | `069ee14840cf777843e9617dfe5462f04dbcc57a082f8ae96b732624d6e6493d` | [skill-validation/pilot/cw-22/specification/prompt.md](../skill-validation/pilot/cw-22/specification/prompt.md) |
| 49 | `380890599afb211486b17084b8b4d1199ee6e8dc22198070873f6f4ce858d7c0` | [skill-validation/pilot/cw-23/specification/prompt.md](../skill-validation/pilot/cw-23/specification/prompt.md) |
| 50 | `cf7b9fdcd21a35856f1c7a038a6fbd21a85af76258fd476910c2b512fed47c46` | [skill-validation/scenarios/concise-writing/cw-01/prompt.md](../skill-validation/scenarios/concise-writing/cw-01/prompt.md) |
| 51 | `6c6580ec1557f10443d33ed09a7497cebce72195ee74bb303901d98ef48db58b` | [skill-validation/scenarios/concise-writing/cw-02/prompt.md](../skill-validation/scenarios/concise-writing/cw-02/prompt.md) |
| 52 | `55bc07ef88d4c5e0a1e1fd23f12958ad5982d4424caaaf5c8d68bc17528e1067` | [skill-validation/scenarios/concise-writing/cw-03/prompt.md](../skill-validation/scenarios/concise-writing/cw-03/prompt.md) |
| 53 | `eb27f4a55d0ad55776f9394a606f5b08eb9be13b97df6ec1070d26faea28f288` | [skill-validation/scenarios/concise-writing/cw-04/prompt.md](../skill-validation/scenarios/concise-writing/cw-04/prompt.md) |
| 54 | `05393026ca0f4f79d7b96b57bb657fd6d16d947f3a98f612c0f329d93b80fe2e` | [skill-validation/scenarios/concise-writing/cw-05/prompt.md](../skill-validation/scenarios/concise-writing/cw-05/prompt.md) |
| 55 | `ec25b3eeb1e4f165f86cb43c558096ec7291f584d11b771442bf93f9a48edd85` | [skill-validation/scenarios/concise-writing/cw-06/prompt.md](../skill-validation/scenarios/concise-writing/cw-06/prompt.md) |
| 56 | `82cd1c8bcce6b726ab9e6d180d94879527c8b80fa304ff66547fa7fc1184faa5` | [skill-validation/scenarios/concise-writing/cw-07/prompt.md](../skill-validation/scenarios/concise-writing/cw-07/prompt.md) |
| 57 | `91db2173ab9bb9a8251c3571fdf26bf485e4d527ce92987d89e2c369a5b3b29b` | [skill-validation/scenarios/concise-writing/cw-08/prompt.md](../skill-validation/scenarios/concise-writing/cw-08/prompt.md) |
| 58 | `169a425529c0cfb5f0c77bcc99ef63e41244b94b46b068c83d48e491d9c17f16` | [skill-validation/scenarios/concise-writing/cw-09/prompt.md](../skill-validation/scenarios/concise-writing/cw-09/prompt.md) |
| 59 | `d89691bec1d5ee09531e65c1e2a5785e409196c118ce9ae76b708627e4852b35` | [skill-validation/scenarios/concise-writing/cw-10/prompt.md](../skill-validation/scenarios/concise-writing/cw-10/prompt.md) |
| 60 | `e902d1c5395512c068a77f5fcbb405a23a0cfdcb55ef63887e8c0741acd9312f` | [skill-validation/scenarios/concise-writing/cw-11/prompt.md](../skill-validation/scenarios/concise-writing/cw-11/prompt.md) |
| 61 | `f492f92ceb4a00753557f9d7365715694bd56deea9a45d320f48fdf1844cf7b6` | [skill-validation/scenarios/concise-writing/cw-12/prompt.md](../skill-validation/scenarios/concise-writing/cw-12/prompt.md) |
| 62 | `192c46c6f4650f42458aa93782f5aebbec422d9aa520e78d8f66adb2050983f7` | [skill-validation/scenarios/concise-writing/cw-13/prompt.md](../skill-validation/scenarios/concise-writing/cw-13/prompt.md) |
| 63 | `8ccb4f0d0aa82c2c06d3c861c153e93161e32f4580dd41706273010acd9339d9` | [skill-validation/scenarios/concise-writing/cw-14/prompt.md](../skill-validation/scenarios/concise-writing/cw-14/prompt.md) |
| 64 | `041117e026c2b823db8c21beb482f91da91822c4552e03c084be54e912ca180c` | [skill-validation/scenarios/concise-writing/cw-17/prompt.md](../skill-validation/scenarios/concise-writing/cw-17/prompt.md) |
| 65 | `b7fb1df8a6a8343004b0f5ccf5460a2abe94a26e058be5fb3ab3c6344a597376` | [skill-validation/scenarios/concise-writing/cw-18/prompt.md](../skill-validation/scenarios/concise-writing/cw-18/prompt.md) |
| 66 | `df33a3add2dc4ad6445076a381e35be307c35fdfbc50426fd0db4072a10b26b3` | [skill-validation/scenarios/concise-writing/cw-19/prompt.md](../skill-validation/scenarios/concise-writing/cw-19/prompt.md) |
