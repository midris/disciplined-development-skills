# CW catalog mapping

**Status:** The complete baseline is owner-accepted; candidate collection is complete and awaits owner review under the [current testing plan](../../plans/2026-09-09-dd-skill-testing.md#remaining-work).
The [accepted evidence index](../accepted/concise-writing/codex-gpt-5.6-sol-medium/README.md) retains results and recoverable provenance.
Both command batches are exhausted; this mapping preserves their declared inputs and does not authorize further provider calls.
The [archived spec](../../plans/completed/specs/2026-09-07-cw-validation-design.md) preserves the completed comparison contract; the [runbook](cw-runbook.md) owns execution.
All rows use Codex / gpt-5.6-sol / medium, three observations per condition.
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

## Routine suite proposal awaiting owner review

The 2026-09-09 provider-free audit mapped all 22 variants above to the shared categories, charter obligations and distinct risks.
The owner's subsequent framing is a routine suite of distinct, clearly runnable and scoreable questions, with no requirement to retain every historical scenario or match counts across skills.
The following is the latest proposal, not approval to change inputs, retire evidence or run models.
It supersedes the audit's more conservative recommendation to keep most diagnostics in the routine suite.

| Existing coverage | Proposed routine disposition and reason |
|---|---|
| CW-01–06, CW-08 and CW-19 loaded prose | Keep their distinct conservation/removal cases: local states/outcomes; rationale/navigation; global definitions; structural padding; unsupported advice; emphasis/universal force; non-software policy; complex operational boundaries. Passing no-DD controls remain useful regressions, not evidence that the skill is unnecessary elsewhere. |
| CW-01/13/14/17/18 native discovery | Keep five separate contexts: explicit tightening, discipline authoring, reference authoring, detailed-response non-trigger and durable-file creation. Preserve per-target loading evidence and the response/file polarity. |
| CW-09/11 description and CW-17/18 scope quizzes | Move out of the routine suite into optional diagnostics; they may explain selection failures but do not demonstrate actual application. |
| CW-10/12 ownership extraction | Drop from routine model testing; extracting the same ownership clause adds little beyond composition behavior. Preserve original records. |
| CW-07 direct-load transport | Retain with invocation/qualification checks, outside routine skill-effectiveness claims. |
| CW-13/14 loaded lifecycle decisions | Replace or strengthen the multiple-choice tasks with actual warning/reference revision material and observable composition criteria. Preserve distinct discipline-pressure and reference-validation contexts; a safe answer is not executed validation. |

Proposed missing coverage: restraint on already-effective prose; a longer artifact mixing wasteful duplication with useful recap/warning/navigation; and actual loaded response-only versus durable-file output cases.
These are coverage hypotheses, not frozen scenarios or an approved count.
A future CW case composed with plan completeness, rationale ownership or referenced-anchor reconciliation remains deferred behind those choices; no other catalog is activated.
Keep removal and conservation outcomes separately visible within a revision test; split scenarios only when the questions need different setup, evidence or independent diagnosis.
CW-19 remains an integrated case with criterion-level failures; a threshold-only microcase is optional diagnostic work, not automatically another permanent test.

Before keeping a proposed case, identify its distinct question, observable result, scoring boundary and the coverage lost if it is removed.
Approve one concrete membership/input proposal before implementation; use this mapping and the existing runbook rather than creating another registry or tooling layer.
The 99 accepted baseline and 66 scratch candidate observations keep their original inputs and judgments regardless of prospective suite membership.
