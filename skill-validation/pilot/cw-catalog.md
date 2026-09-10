# CW catalog mapping

**Status:** Baseline and candidate evidence validity are owner-accepted. The owner approved preparation under the [routine coverage](#routine-suite-coverage); its six changed/new input packages await exact-input review under the [current testing plan](../../plans/2026-09-09-dd-skill-testing.md#remaining-work).
The [accepted evidence index](../accepted/concise-writing/codex-gpt-5.6-sol-medium/README.md) retains results and recoverable provenance.
Both command batches are exhausted; this mapping preserves their declared inputs and does not authorize further provider calls.
The [archived spec](../../plans/completed/specs/2026-09-07-cw-validation-design.md) preserves the completed comparison contract; the [runbook](cw-runbook.md) owns execution.
The completed-comparison rows use Codex / gpt-5.6-sol / medium, three observations per condition; no new collection schedule is selected here.
A linked config is an input declaration, not permission to invoke it.

## Source-to-variant map

All 17 existing sources are represented; CW-15/16 do not exist.
The 22 variants below preserve original task material and split mixed purposes without rewriting a skill.
Worksheet scenario is the directory containing the linked prompt and rubric, not the medium config directory.
Read each complete linked rubric, including historical sources, before scoring.

| Order | Source / purpose | Conditions: exact prompt, rubric and config | Fixture group | Change from existing test |
|---|---|---|---|---|
| 1 | CW-01: Loaded prose | [no-dd](cw-01/no-dd/prompt.md) · [rubric](cw-01/no-dd/rubric.md) · [config](efforts/medium/cw01-no-dd.json)<br>[current-dd](cw-01/current-dd/prompt.md) · [rubric](cw-01/current-dd/rubric.md) · [config](efforts/medium/cw01-current-dd.json) | ordinary | Existing behavior prompts/rubrics; add medium configs. Export states and distinct outcomes. |
| 2 | CW-01: Native discovery | [discovery](cw-01/discovery/prompt.md) · [rubric](cw-01/discovery/rubric.md) · [config](efforts/medium/cw01-discovery.json) | ordinary | Existing positive discovery variant, unchanged; separate from CW-01 behavior. |
| 3 | CW-02: Loaded prose | [no-dd](cw-02/no-dd/prompt.md) · [rubric](cw-02/no-dd/rubric.md) · [config](efforts/medium/cw02-no-dd.json)<br>[current-dd](cw-02/current-dd/prompt.md) · [rubric](cw-02/current-dd/rubric.md) · [config](efforts/medium/cw02-current-dd.json) | ordinary | Keep retry task; native load prefix and common read-only boundary. Preserve rationale/navigation. |
| 4 | CW-03: Loaded prose | [no-dd](cw-03/no-dd/prompt.md) · [rubric](cw-03/no-dd/rubric.md) · [config](efforts/medium/cw03-no-dd.json)<br>[current-dd](cw-03/current-dd/prompt.md) · [rubric](cw-03/current-dd/rubric.md) · [config](efforts/medium/cw03-current-dd.json) | ordinary | Keep complete access-link guide; one definition, recipient and administrator rules. |
| 5 | CW-04: Loaded prose | [no-dd](cw-04/no-dd/prompt.md) · [rubric](cw-04/no-dd/rubric.md) · [config](efforts/medium/cw04-no-dd.json)<br>[current-dd](cw-04/current-dd/prompt.md) · [rubric](cw-04/current-dd/rubric.md) · [config](efforts/medium/cw04-current-dd.json) | ordinary | Keep session guide; collapse unnecessary subheadings without losing timings, input types or recovery. |
| 6 | CW-05: Loaded prose | [no-dd](cw-05/no-dd/prompt.md) · [rubric](cw-05/no-dd/rubric.md) · [config](efforts/medium/cw05-no-dd.json)<br>[current-dd](cw-05/current-dd/prompt.md) · [rubric](cw-05/current-dd/rubric.md) · [config](efforts/medium/cw05-current-dd.json) | ordinary | Keep authoritative notes and archive prose; remove unsupported advice. |
| 7 | CW-06: Loaded prose | [no-dd](cw-06/no-dd/prompt.md) · [rubric](cw-06/no-dd/rubric.md) · [config](efforts/medium/cw06-no-dd.json)<br>[current-dd](cw-06/current-dd/prompt.md) · [rubric](cw-06/current-dd/rubric.md) · [config](efforts/medium/cw06-current-dd.json) | ordinary | Keep API-key prose; score redundant wording and emphasis once under CW-I2, with source forms as examples rather than a separate lexical prohibition. |
| 8 | CW-07: Direct-load transport | [no-dd](cw-07/no-dd/prompt.md) · [rubric](cw-07/no-dd/rubric.md) · [config](efforts/medium/cw07-no-dd.json)<br>[current-dd](cw-07/current-dd/prompt.md) · [rubric](cw-07/current-dd/rubric.md) · [config](efforts/medium/cw07-current-dd.json) | ordinary | Keep release notice and BLOCKED fallback; add a matching no-DD task control. Loading itself is N/A in no-DD. |
| 9 | CW-08: Loaded prose | [no-dd](cw-08/no-dd/prompt.md) · [rubric](cw-08/no-dd/rubric.md) · [config](efforts/medium/cw08-no-dd.json)<br>[current-dd](cw-08/current-dd/prompt.md) · [rubric](cw-08/current-dd/rubric.md) · [config](efforts/medium/cw08-current-dd.json) | ordinary | Reuse prepared policy pair unchanged, subject to evidence checks. |
| 10 | CW-09: Description classification | [description](cw-09/description/prompt.md) · [rubric](cw-09/description/rubric.md) · [config](efforts/medium/cw09-description.json) | description | Retain closed-list quiz and description inputs; label target mismatch separately from source-faithful extraction. |
| 11 | CW-10: Ownership contract | [contract](cw-10/contract/prompt.md) · [rubric](cw-10/contract/rubric.md) · [config](efforts/medium/cw10-contract.json) | ordinary | Retain ownership extraction; native CW path. Accept an actual explicit equivalent ownership sentence, not one prescribed sentence. |
| 12 | CW-11: Description classification | [description](cw-11/description/prompt.md) · [rubric](cw-11/description/rubric.md) · [config](efforts/medium/cw11-description.json) | description | Retain reference-authoring description quiz; not native discovery or an executed reference edit. |
| 13 | CW-12: Ownership contract | [contract](cw-12/contract/prompt.md) · [rubric](cw-12/contract/rubric.md) · [config](efforts/medium/cw12-contract.json) | ordinary | Same ownership/extraction separation as CW-10 for supporting references. |
| 14 | CW-13: Loaded composition decision | [no-dd](cw-13/no-dd/prompt.md) · [rubric](cw-13/no-dd/rubric.md) · [config](efforts/medium/cw13-no-dd.json)<br>[current-dd](cw-13/current-dd/prompt.md) · [rubric](cw-13/current-dd/rubric.md) · [config](efforts/medium/cw13-current-dd.json) | authoring | Explicitly load judged skills; retain pressure and A/B/C options. Remove applicable_skills; retain owner and action. |
| 15 | CW-13: Native discovery | [discovery](cw-13/discovery/prompt.md) · [rubric](cw-13/discovery/rubric.md) · [config](efforts/medium/cw13-discovery.json) | authoring | Retain deadline/reviewer pressure; remove read-all, named choices and routing JSON. Ask for the next decision, not an edit. |
| 16 | CW-14: Loaded composition decision | [no-dd](cw-14/no-dd/prompt.md) · [rubric](cw-14/no-dd/rubric.md) · [config](efforts/medium/cw14-no-dd.json)<br>[current-dd](cw-14/current-dd/prompt.md) · [rubric](cw-14/current-dd/rubric.md) · [config](efforts/medium/cw14-current-dd.json) | authoring | Explicitly load judged skills; retain reference pressure/options. Remove applicable_skills; retain owner and action. |
| 17 | CW-14: Native discovery | [discovery](cw-14/discovery/prompt.md) · [rubric](cw-14/discovery/rubric.md) · [config](efforts/medium/cw14-discovery.json) | authoring | Retain reference/deadline pressure; ask for a next decision without skill hints, answer options or actual authoring. |
| 18 | CW-17: Loaded scope contract | [contract](cw-17/contract/prompt.md) · [rubric](cw-17/contract/rubric.md) · [config](efforts/medium/cw17-contract.json) | ordinary | Read CW explicitly, retain the embedded request and boolean only. No selected_skills; do not carry out the embedded request. |
| 19 | CW-17: Native non-trigger | [discovery](cw-17/discovery/prompt.md) · [rubric](cw-17/discovery/rubric.md) · [config](efforts/medium/cw17-discovery.json) | ordinary | Reuse the existing detailed response-only discovery variant unchanged. |
| 20 | CW-18: Loaded scope contract | [contract](cw-18/contract/prompt.md) · [rubric](cw-18/contract/rubric.md) · [config](efforts/medium/cw18-contract.json) | ordinary | Read CW explicitly; retain the file/brief-response contrast and boolean only. No actual file creation in this diagnostic. |
| 21 | CW-18: Native discovery | [discovery](cw-18/discovery/prompt.md) · [rubric](cw-18/discovery/rubric.md) · [config](efforts/medium/cw18-discovery.json) | ordinary | Execute the existing embedded request: write clothing-swap-guide.md and give a brief notice. Only that file may be created. |
| 22 | CW-19: Loaded prose | [no-dd](cw-19/no-dd/prompt.md) · [rubric](cw-19/no-dd/rubric.md) · [config](efforts/medium/cw19-no-dd.json)<br>[current-dd](cw-19/current-dd/prompt.md) · [rubric](cw-19/current-dd/rubric.md) · [config](efforts/medium/cw19-current-dd.json) | ordinary | Reuse prepared cutover pair unchanged, including all eight semantic criteria. |

## Fixture groups and evidence boundaries

- **Ordinary:** the existing four Superpowers files; current-DD adds all nine frozen DD bodies, no-DD removes those nine only.
- **Authoring:** ordinary plus the three checked-in CW-13 fixtures: writing-skills body, its testing reference and TDD body.
  These are reused source files, not newly authored skills; both conditions retain the same added substrate.
  Audit their content/references and freeze their bytes without claiming a package version from a later installation.
  Read-only checkpoint tasks require these bodies, not an executable authoring project, provider dispatch or deployment toolchain.
  Guidance for actual authoring, unrelated platform setup and optional examples is outside these tasks; a needed missing dependency stops qualification.
- **Description:** the four common Superpowers files plus the source scenario's three description files, with no DD bodies.
  Here current-DD means the frozen DD descriptions being examined, not the ordinary nine-body composition.
  Audit those descriptions against the frozen DD metadata; do not silently use stale description text in a future candidate arm.

Ordinary and authoring skill files use native `.agents/skills/` targets.
Descriptions remain explicit task data under `descriptions/`, deliberately not native discovery.
Evaluator rubrics, accepted answers and runbooks are never subject fixtures.
Only CW-18 discovery permits a write: the newly created `fixture/clothing-swap-guide.md`.
Every declared input remains protected, including all skills; retain and inspect the new file as task-fidelity evidence.
No-DD controls exist for the nine prose/transport tasks and two loaded lifecycle decisions.
No-DD is N/A for unavailable-target discovery, ownership/scope extraction and description diagnostics: removing the inspected object would test missing input, not DD's behavioral contribution.

CW-13/14 native discovery independently scores complete CW and writing-skills body loading before the decision, including disclosed composition-mediated routes.
Their loaded counterparts score lifecycle ownership, safe action and subordinate companion use; they do not also claim discovery.
CW-17/18 contract variants score the declared application decision only; native selection belongs to the separate discovery variants.
Neither contract answers nor writing style prove that a model internally applied or withheld a method.
The full catalog still does not establish executed skill authoring or every charter behavior; new coverage ideas wait until after the baseline.

## Reviewed rubric changes

Keep every historical semantic target, including targets absent from current main.
Do not erase an accepted failure by changing its old rubric or rescoring its evidence.

- CW-01–08/19 preserve task facts and padding/conservation requirements; explicitly assign loading, output-only narration and ordinary presentation to fidelity.
  CW-06's redundant wording and emphasis belong only to CW-I2 because removing them is the behavior being tested; source forms illustrate padding, not a separate fidelity blacklist.
  CW-07's standalone completion remains a transport check, not a new CW-owned invariant.
- CW-09/11 preserve the target selection of CW plus writing-skills and exclusion of review-loop.
  The frozen CW description excludes authoring; report source faithfulness separately from the target-composition FAIL.
- CW-10/12 require explicit writing-skills ownership but allow equivalent complete ownership wording.
  Exact copying of an actual source sentence and JSON shape are extraction fidelity.
  An absent clause may yield truthful nulls and a contract FAIL simultaneously.
  This removes a literal-wording lock without relaxing ownership; changed rubrics require fresh observations.
- CW-13/14 move applicable-skill selection to native discovery and keep owner/action under loaded composition.
  A safe multiple-choice answer is decision evidence, not proof of performed validation.
- CW-17/18 remove selected_skills from the loaded contract diagnostic.
  Preserve the charter's false/true response-versus-file polarity, even when the supplied skill lacks the response exception.
  Discovery uses natural tasks and full observable traces rather than the old closed-list JSON selection.

These are the owner-approved contracts frozen for this baseline; historical source prompts, rubrics and accepted results remain untouched.
No exact-format criterion has an authenticated consumer, so deterministic protocol is N/A throughout this set.

## Counts, order and reuse

| Purpose | Current-DD conditions | No-DD conditions | Observations at three each |
|---|---:|---:|---:|
| Prose revision | 8 | 8 | 48 |
| Direct-load transport with prose checks | 1 | 1 | 6 |
| Loaded authoring-lifecycle decisions | 2 | 2 | 12 |
| Description/ownership/scope diagnostics | 6 | 0 | 18 |
| Native discovery | 5 | 0 | 15 |
| Total | 22 | 11 | 99 |

There are 66 current-DD observations and 33 no-DD observations, not 51 current-DD observations.
The increase is four mixed sources split into two purposes, plus the already existing CW-01 positive discovery variant.
Per repetition, traverse the map in order and each row's conditions left-to-right (no-DD then current-DD for pairs).
Run serially with fresh runtimes, without adaptive repeats or verdict-dependent stopping.
This is a simple auditable order, not randomized or fully counterbalanced; disclose order and collection-time effects.

The [qualification and reuse audit](/private/tmp/skilltest-cw-catalog-qualification.YiAoRu/summary.md) supports reuse of CW-08 no-DD/current-DD, CW-19 no-DD/current-DD, CW-01 discovery and CW-17 discovery: 18 observations.
The audit checks each original bundle, frozen revision, prompt/rubric/linked guidance, source/target bytes, actual CLI version/digest, invocation, controls and trace against this declaration.
Reuse does not change owner-acceptance status.
The [earlier summary](/private/tmp/skilltest-cw-baseline.ksDeiD/summary.md) owns those records.
Keep their original timestamps and outcome, referencing rather than copying or relabeling them.
The 81-call fresh batch is complete; the linked complete-set summary reconciles it with these 18 reused observations.
If inputs or controls drift before launch, re-evaluate affected reuse; replace complete three-observation sets and disclose any changed count before approval.
Never substitute the completed discovery variants for historical routing/contract quizzes, or low/high pilot observations for medium repetitions.

## Before command approval

1. Complete the provider-free preparation audit for every selected config: declared paths/bytes, pair equality, body-load directives, hint-free discovery, withheld guidance and permitted-write target.
2. Reconcile ordinary-group controls against retained qualification; unchanged prose tasks alone need no new paid setup probe.
3. Reconcile the added authoring catalog/dependencies and description-only setup.
   Establish the CW-18 create-file/retained-artifact path; the old read-only discovery observation does not prove it.
   Missing trace, permission, dependency or control evidence stops the affected launch; any required live qualification gets separate exact-command approval.
4. Resolve reuse, review and freeze exact prompts/rubrics with the owner, then freeze a recoverable clean revision and allocate scratch.
5. Show the complete finite command list, cwd, final count/order and provider/model/effort for explicit approval.
   A preparation or baseline approval does not itself authorize candidate provider calls or new skill edits.

## CW rewrite candidate configs

The [candidate snapshot](inputs/candidates/cw-rewrite/README.md) pins the unchanged source body and its exact description.
Each candidate config below reuses its baseline config's prompt and evaluator-only rubric, fixture targets, other supplied bytes and execution settings.
Only CW body/description bytes and recording IDs/source paths differ; no extra candidate hint is added to subject prompts.
The worksheet scenario remains the original prompt/rubric directory, even when its name contains `current-dd`; the candidate scenario ID and recorded fixture hash identify the treatment.
The two description diagnostics replace only `descriptions/concise-writing.txt`, not their other description inputs.
Rubric remarks that the frozen CW excludes authoring (CW-09/11) or lacks the response exception (CW-17) describe the baseline arm, not candidate facts.
Keep the same required outcomes and source-faithfulness judgments, checking the actual supplied candidate bytes; do not copy a baseline mismatch into a candidate score.

| Baseline config / shared test contract | Candidate config |
|---|---|
| [cw01-current-dd.json](efforts/medium/cw01-current-dd.json) | [candidate](efforts/medium/cw-rewrite/cw01-current-dd.json) |
| [cw01-discovery.json](efforts/medium/cw01-discovery.json) | [candidate](efforts/medium/cw-rewrite/cw01-discovery.json) |
| [cw02-current-dd.json](efforts/medium/cw02-current-dd.json) | [candidate](efforts/medium/cw-rewrite/cw02-current-dd.json) |
| [cw03-current-dd.json](efforts/medium/cw03-current-dd.json) | [candidate](efforts/medium/cw-rewrite/cw03-current-dd.json) |
| [cw04-current-dd.json](efforts/medium/cw04-current-dd.json) | [candidate](efforts/medium/cw-rewrite/cw04-current-dd.json) |
| [cw05-current-dd.json](efforts/medium/cw05-current-dd.json) | [candidate](efforts/medium/cw-rewrite/cw05-current-dd.json) |
| [cw06-current-dd.json](efforts/medium/cw06-current-dd.json) | [candidate](efforts/medium/cw-rewrite/cw06-current-dd.json) |
| [cw07-current-dd.json](efforts/medium/cw07-current-dd.json) | [candidate](efforts/medium/cw-rewrite/cw07-current-dd.json) |
| [cw08-current-dd.json](efforts/medium/cw08-current-dd.json) | [candidate](efforts/medium/cw-rewrite/cw08-current-dd.json) |
| [cw09-description.json](efforts/medium/cw09-description.json) | [candidate](efforts/medium/cw-rewrite/cw09-description.json) |
| [cw10-contract.json](efforts/medium/cw10-contract.json) | [candidate](efforts/medium/cw-rewrite/cw10-contract.json) |
| [cw11-description.json](efforts/medium/cw11-description.json) | [candidate](efforts/medium/cw-rewrite/cw11-description.json) |
| [cw12-contract.json](efforts/medium/cw12-contract.json) | [candidate](efforts/medium/cw-rewrite/cw12-contract.json) |
| [cw13-current-dd.json](efforts/medium/cw13-current-dd.json) | [candidate](efforts/medium/cw-rewrite/cw13-current-dd.json) |
| [cw13-discovery.json](efforts/medium/cw13-discovery.json) | [candidate](efforts/medium/cw-rewrite/cw13-discovery.json) |
| [cw14-current-dd.json](efforts/medium/cw14-current-dd.json) | [candidate](efforts/medium/cw-rewrite/cw14-current-dd.json) |
| [cw14-discovery.json](efforts/medium/cw14-discovery.json) | [candidate](efforts/medium/cw-rewrite/cw14-discovery.json) |
| [cw17-contract.json](efforts/medium/cw17-contract.json) | [candidate](efforts/medium/cw-rewrite/cw17-contract.json) |
| [cw17-discovery.json](efforts/medium/cw17-discovery.json) | [candidate](efforts/medium/cw-rewrite/cw17-discovery.json) |
| [cw18-contract.json](efforts/medium/cw18-contract.json) | [candidate](efforts/medium/cw-rewrite/cw18-contract.json) |
| [cw18-discovery.json](efforts/medium/cw18-discovery.json) | [candidate](efforts/medium/cw-rewrite/cw18-discovery.json) |
| [cw19-current-dd.json](efforts/medium/cw19-current-dd.json) | [candidate](efforts/medium/cw-rewrite/cw19-current-dd.json) |

Completed candidate collection: three repetitions, traversing the source-to-variant map in order and selecting its candidate config once per row, for 66 observations.
The handoff links collection and audit evidence, including qualified reuse of all 99 accepted current-DD/no-DD observations; these configs do not authorize replaying the batch.
The [provider-free preparation audit](/private/tmp/skilltest-cw-candidate.pITN2u/input-audit.json) checks all 22 configs and prepared fixtures, including exact source bytes, unchanged tasks/rubrics, and one changed CW target each.
The [separate provider-free qualification](/private/tmp/skilltest-cw-candidate.pITN2u/qualification/summary.md) now checks the actual candidate catalogs/dependencies and supports reuse of all 99 accepted observations.
The file-copy audit alone does not establish those controls; clean freeze and complete command approval remain launch gates.

## Routine suite coverage

This provider-free audit refines the preserved coverage discussion against the 22 existing purpose-separated prompts and rubrics above.
The owner approved these membership and coverage boundaries for input preparation on 2026-09-10.
The [routine input map](#routine-input-map) links prospective task/rubric drafts; completed-comparison inputs and judgments remain unchanged, and no provider calls are authorized.
The current criteria remain usable for their existing examples.
The question is which distinct risks deserve routine tests, not how to produce more failures or minimize a word count.

CW-I1 preserves consequential meaning, rationale and useful framing; CW-I2 removes lossless local/global padding; CW-I3 governs domain and the detailed-response boundary.
Authoring ownership and validation remain with `superpowers:writing-skills`; CW’s composition responsibility is subordinate, lossless prose revision.
Discovery scores observable selection/body access; loaded effectiveness scores the artifact; composition attributes each responsibility to its owner.
Supporting diagnostics and transport qualification do not become extra effectiveness results.

### Every existing purpose-separated variant

The row order matches the source-to-variant map; treatment arms and repetitions are not additional scenarios.
“Drop” means no routine model test, never deletion or rescoring of historical evidence.

| Existing variant | Common category or support role | Obligation / distinct failure mode or context | Recommendation and observable boundary |
|---|---|---|---|
| CW-01 loaded prose | Effectiveness | CW-I1/I2: ordinary local restatements around four states and distinct outcomes. | **Keep.** Remove the opener and two restatements; retain every state and correct link/error relationship, with no added meaning. Removing it loses the small ordinary revision regression. |
| CW-01 native discovery | Discoverability | CW-I3: explicit tightening request without a skill-loading hint. | **Keep.** Require complete model-initiated CW body access before the revision; good prose alone cannot pass discovery. This separates selection failure from loaded behavior on the same task. |
| CW-02 loaded prose | Effectiveness | CW-I1/I2: short mixed passage where rationale, navigation and an exact failure boundary must survive trimming. | **Keep.** Preserve per-delivery scope, synchronous-order rationale, navigation and third-unsuccessful-attempt boundary while removing actual duplication. CW-01 does not protect those framing functions. |
| CW-03 loaded prose | Effectiveness | CW-I1/I2: whole-document duplication across sections, rather than adjacent repetition. | **Strengthen and consolidate** the proposed longer-document gap here. Retain the access-link use/recovery facts, but distinguish redundant definitions from a useful recap or repeated warning in a longer complete artifact. Score waste removed and useful framing preserved separately; do not add a second routine global-duplication case. |
| CW-04 loaded prose | Effectiveness | CW-I1/I2: structural padding from four one-sentence subheadings. | **Keep.** Collapse the structure while retaining timeout, warning timing, reset inputs and recovery. Sentence-level duplicate removal does not exercise this decision. |
| CW-05 loaded prose | Effectiveness | CW-I1/I2: unsupported advice already present in a draft, contrasted with supplied authoritative notes. | **Keep.** Remove both unsupported recommendations and preserve the three source facts without inventing replacements. Other cases mostly prohibit additions; this requires removing an existing unsupported elaboration. |
| CW-06 loaded prose | Effectiveness | CW-I1/I2: inflated emphasis versus necessary universal scope and obligation. | **Keep.** Remove redundant emphasis/repetition while preserving every-request key/header requirements and rejection. Do not turn illustrative words into a blacklist or weaken universal force. |
| CW-07 direct-load transport | Harness qualification | Standalone invocation must not acquire an unnecessary project/workflow prerequisite; prose checks overlap CW-01. | **Remove from routine effectiveness; retain for affected invocation/qualification checks.** Requalify when invocation mechanics or skill/composition wording changes project-state requirements, companion dependencies or mandatory procedures, even with an unchanged runner. Require standalone completion and actual supplied-body access. Unrelated prose edits do not alone require this check; any provider call still needs batch approval. |
| CW-08 loaded prose | Effectiveness | CW-I1/I2/I3: non-software policy with eligibility exception, contact route, deadlines and appeal navigation. | **Keep.** Preserve all policy conditions and means of acting on them, remove duplicate deadline/meta prose, add no software assumptions. This is meaningful domain coverage even if a Codex control passes. |
| CW-09 description classification | Supporting diagnostic | Authoring composition applicability in frontmatter, inferred from three supplied descriptions. | **Optional diagnostic only.** Use to investigate a description-related discovery failure; distinguish source-faithful classification from the intended CW/writing-skills pairing. A closed list does not demonstrate native selection. |
| CW-10 ownership extraction | Supporting diagnostic | Explicit writing-skills ownership in CW’s body, not exercised lifecycle behavior. | **Drop from routine model testing altogether.** Inspect the contract during skill review if needed; native composition/actual behavior carry the useful test burden. Preserve the historical absent-clause results. |
| CW-11 description classification | Supporting diagnostic | Reference-file authoring applicability in the same closed description list. | **Optional diagnostic only.** Keep the reference context available for diagnosis, not as a second routine selection mechanism. Its distinct boundary belongs in CW-14 discovery/composition. |
| CW-12 ownership extraction | Supporting diagnostic | Supporting-reference wording asks for the same explicit ownership clause as CW-10. | **Drop from routine model testing altogether.** It repeats extraction rather than testing reference behavior; preserve the actual reference-specific validation boundary in CW-14. |
| CW-13 loaded lifecycle decision | Composition | CW-I1/I2 plus writing-skills authority: deadline/seniority pressure to halve a warning whose protective purpose is evidenced. | **Replace the multiple-choice task with an authorized draft revision and a separate deployment decision.** Supply warning text with losslessly removable padding and a protected pressure guard; require the draft to remove the padding while preserving the guard, without enforcing the requested halving. Deployment remains blocked pending required validation of that draft. Refusal alone cannot demonstrate CW's contribution; apply the draft/authority scoring rules below. |
| CW-13 native discovery | Discoverability | CW-I3 and authoring-owner selection under discipline/release pressure. | **Keep.** Require separate full CW and writing-skills loads before the decision; disclose composition-mediated routes. Do not score the lifecycle decision a second time as effectiveness. |
| CW-14 loaded lifecycle decision | Composition | CW-I1/I2 plus writing-skills authority: a supporting reference changes even though SKILL.md does not. | **Replace the multiple-choice task with an authorized draft reference revision and a separate deployment decision.** Supply losslessly removable padding; require its removal while preserving parameter relationships and findable use. Unchanged SKILL.md cannot waive required retrieval/application/gap validation of the draft. Refusal alone cannot pass the whole case; apply the draft/authority scoring rules below. This remains a distinct scope/validation bypass from CW-13. |
| CW-14 native discovery | Discoverability | CW-I3 and authoring-owner selection for a shipped reference, without main-body edits. | **Keep.** Require separate complete CW/writing-skills loads before the decision. This catches the supporting-file scope boundary that the discipline-warning context does not. |
| CW-17 loaded scope quiz | Supporting diagnostic | CW-I3: the explicit detailed, response-only exception, expressed as a boolean. | **Remove the quiz from routine testing; replace its coverage with a loaded explanation-generation case.** Keep the quiz optional for contract diagnosis. Require explicitly requested explanations and examples from supplied facts; a factually correct outline that omits that depth fails. This tests over-summarizing a new explanation, not destructive editing of the already-effective source in the restraint case. No output proves a hidden decision to withhold the method. |
| CW-17 native non-trigger | Discoverability | CW-I3: inappropriate selection for explicitly detailed response-only prose. | **Keep.** Require no observed CW selection/body access on a completed task with qualified availability and complete trace. Shortness or quality of the answer is not evidence of non-selection. |
| CW-18 loaded scope quiz | Supporting diagnostic | CW-I3: a detailed file remains in scope despite a brief completion response. | **Remove the quiz from routine testing; replace its coverage with an actual loaded file deliverable.** Keep the quiz optional for contract diagnosis. Inspect the file’s preservation/padding outcome and the brief notice separately. |
| CW-18 native discovery | Discoverability | CW-I3: durable-file generation with a brief response, contrasting CW-17’s sole response deliverable. | **Keep.** Require full CW loading before file prose and independently verify the file. This proves selection and task execution, not lossless application; keep that distinction from the proposed loaded case. |
| CW-19 loaded prose | Effectiveness | CW-I1/I2: integrated operational requirements, exact threshold conjunctions, order, authority and irreversible recovery boundary. | **Keep as one integrated test.** Retain criterion-level failures for all eight source criteria and unsupported meaning. Splitting every threshold into a separate routine case loses the whole-artifact interaction and needlessly repeats setup. |

### Gaps and how to cover them

| Gap | Proposed coverage | Scoring boundary to settle before input implementation |
|---|---|---|
| Restraint when the source is already effective | **One new loaded-effectiveness case.** Ask for tightening of an existing complete passage whose detail and framing are useful, with no planted redundant passage. | Score resistance to destructive edits under a shortening request: no consequential fact, relationship, rationale or necessary framing lost; no unsupported additions or less readable compression. An unchanged answer or harmless equivalent wording may pass. Do not require edits or an exact-copy answer. |
| A longer artifact containing both wasteful repetition and useful repetition | **Strengthen CW-03**, rather than add another routine case. | A source map distinguishes each unnecessary duplicate from a recap/warning/navigation element with a reader-use purpose. Require lossless removal and preservation of those purposes across the whole artifact; no maximum word count or “every fact once” rule for intentional reinforcement. |
| Loaded response-only versus loaded durable-file behavior | **Two replacement cases** derived from CW-17/18's scope quizzes. | Use a common factual basis but distinct task contracts. CW-17 generates an explicitly requested detailed explanation from facts, with specified explanatory relationships and examples; merely listing the facts fails the depth requirement. CW-18 revises a supplied padded draft into a detailed file: remove lossless padding, preserve required detail, and assess the brief notice separately. Neither output nor self-report proves an unobserved internal method was applied or withheld. |
| CW's actual contribution inside authoring composition | **Replace CW-13/14's decision-only inputs** as described above. | Supply source prose, evidence satisfying prerequisites for drafting, an explicit draft-only edit boundary, and a requirement to return the draft without deploying it. Required validation of the proposed wording remains outstanding. Score the actual revision under CW and the deployment decision under writing-skills separately; neither a safe refusal alone nor a good draft with premature deployment approval passes the whole case. |

Retain the response-generation and restraint cases for their different failure triggers: suppressing explicitly requested depth versus damaging already-effective prose when asked to shorten it.
The file case instead requires lossless removal inside the durable deliverable despite a brief completion response; changing the output destination alone would not justify an additional effectiveness case.
At exact-input review, check these distinct failure examples against the proposed criteria; if the response and restraint cases reduce to the same preservation check, consolidate them and revise the provisional count before collection.
Keep removal and conservation criteria together for each revision.

For both authoring composition replacements, draft authorization permits only the bounded candidate revision, not deployment or a waiver of the authoring owner's prerequisites.
Provide enough existing evidence to make drafting permissible under the supplied composition, so refusal is not the only compliant action.
A missing draft is a deliverable-fidelity failure and leaves CW behavior unassessed, not passed; an unchanged supplied draft with the identified lossless padding fails CW-I2.
A correct blocked-deployment decision may pass its writing-skills criterion independently, but cannot substitute for a judgeable revision satisfying CW's criteria.
These cases demonstrate draft revision and an authority decision, not an executed validation lifecycle.

CW-20 is the new restraint case; the other changed inputs strengthen or replace existing purposes.
No new routine threshold microcase, standalone generic prose-format test, or separate CW-10/12 ownership model call is recommended.
Plan-completeness, rationale-owner and anchor-reconciliation composition extensions remain deferred; this audit activates no other skill catalog.

### Routine input map

Rows identify purposes, not provider calls, treatment arms or repetitions.
The 18 purposes comprise 11 effectiveness, five discoverability and two composition cases.
Existing pairs retain their two linked prompt/rubric directories; new `routine/` prompts are common tasks assembled with the [declared loading prefixes](cw-runbook.md#routine-suite-preparation) before a batch freeze.
No existing config automatically points at a new routine task.

| Purpose | Category | Prompt and rubric material |
|---|---|---|
| CW-01 local padding | Effectiveness | Unchanged [no-DD prompt](cw-01/no-dd/prompt.md) / [rubric](cw-01/no-dd/rubric.md); [current-DD prompt](cw-01/current-dd/prompt.md) / [rubric](cw-01/current-dd/rubric.md). |
| CW-02 mixed preservation | Effectiveness | Unchanged [no-DD prompt](cw-02/no-dd/prompt.md) / [rubric](cw-02/no-dd/rubric.md); [current-DD prompt](cw-02/current-dd/prompt.md) / [rubric](cw-02/current-dd/rubric.md). |
| CW-03 long guide | Effectiveness | Strengthened [common prompt](cw-03/routine/prompt.md) / [rubric](cw-03/routine/rubric.md). |
| CW-04 structural padding | Effectiveness | Unchanged [no-DD prompt](cw-04/no-dd/prompt.md) / [rubric](cw-04/no-dd/rubric.md); [current-DD prompt](cw-04/current-dd/prompt.md) / [rubric](cw-04/current-dd/rubric.md). |
| CW-05 unsupported elaboration | Effectiveness | Unchanged [no-DD prompt](cw-05/no-dd/prompt.md) / [rubric](cw-05/no-dd/rubric.md); [current-DD prompt](cw-05/current-dd/prompt.md) / [rubric](cw-05/current-dd/rubric.md). |
| CW-06 inflated emphasis | Effectiveness | Unchanged [no-DD prompt](cw-06/no-dd/prompt.md) / [rubric](cw-06/no-dd/rubric.md); [current-DD prompt](cw-06/current-dd/prompt.md) / [rubric](cw-06/current-dd/rubric.md). |
| CW-08 non-software policy | Effectiveness | Unchanged [no-DD prompt](cw-08/no-dd/prompt.md) / [rubric](cw-08/no-dd/rubric.md); [current-DD prompt](cw-08/current-dd/prompt.md) / [rubric](cw-08/current-dd/rubric.md). |
| CW-17 requested response depth | Effectiveness | Replacement [common prompt](cw-17/routine/prompt.md) / [rubric](cw-17/routine/rubric.md). |
| CW-18 detailed file revision | Effectiveness | Replacement [common prompt](cw-18/routine/prompt.md) / [rubric](cw-18/routine/rubric.md). |
| CW-19 operational conservation | Effectiveness | Unchanged [no-DD prompt](cw-19/no-dd/prompt.md) / [rubric](cw-19/no-dd/rubric.md); [current-DD prompt](cw-19/current-dd/prompt.md) / [rubric](cw-19/current-dd/rubric.md). |
| CW-20 restraint | Effectiveness | New [common prompt](cw-20/routine/prompt.md) / [rubric](cw-20/routine/rubric.md). |
| CW-01 explicit tightening trigger | Discoverability | Unchanged [prompt](cw-01/discovery/prompt.md) / [rubric](cw-01/discovery/rubric.md). |
| CW-13 warning-authoring trigger | Discoverability | Unchanged [prompt](cw-13/discovery/prompt.md) / [rubric](cw-13/discovery/rubric.md). |
| CW-14 reference-authoring trigger | Discoverability | Unchanged [prompt](cw-14/discovery/prompt.md) / [rubric](cw-14/discovery/rubric.md). |
| CW-17 detailed-response non-trigger | Discoverability | Unchanged [prompt](cw-17/discovery/prompt.md) / [rubric](cw-17/discovery/rubric.md). |
| CW-18 file-generation trigger | Discoverability | Unchanged [prompt](cw-18/discovery/prompt.md) / [rubric](cw-18/discovery/rubric.md). |
| CW-13 warning draft and deployment decision | Composition | Replacement [common prompt](cw-13/routine/prompt.md) / [rubric](cw-13/routine/rubric.md). |
| CW-14 reference draft and deployment decision | Composition | Replacement [common prompt](cw-14/routine/prompt.md) / [rubric](cw-14/routine/rubric.md). |

This replaces the previous open-ended gap list with a concrete review proposal: seven current variants leave routine testing, three output-producing cases enter, and three retained purposes gain stronger material.
Of those seven removals, four quizzes remain optional diagnostics (CW-09/11/17/18), two ownership extractors leave routine model testing entirely (CW-10/12), and one transport case belongs to qualification (CW-07).
The 18-case total is the consequence of these distinct questions, not a target count or a rule for other skills.
Keep meaningful no-DD controls and ordinary cases; a pass without DD on Sol medium does not establish lack of value on every model or task.

Input preparation is approved; owner review of these exact tasks/rubrics precedes freezing a provider-specific batch under the existing runbook.
The response task requires generating causal explanations and worked examples from notes; the restraint task supplies complete prose whose useful explanations must survive a tightening request.
Those concrete failure boundaries remain distinct, so provider-free review retains both purposes for owner review rather than consolidating them.
No model schedule, provider run, skill edit or adoption is approved by this mapping.
The 99 accepted baseline and 66 accepted candidate observations retain their original inputs and judgments, including any mismatch between the supplied skill and the historical target contract.
