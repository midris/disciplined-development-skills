# Separate Skill Discoverability and Effectiveness Coverage

> **For agentic workers:** On owner activation, use `superpowers:executing-plans` task by task with review checkpoints.

**Status:** CW-only catalog preparation is ACTIVE under the [CW design](../specs/2026-09-07-cw-validation-design.md); other-skill repairs and further provider calls remain DEFERRED or separately gated.
The pilot plan's Tasks 8–9 retain the completed first CW procedure batch, not the current preparation scope.
**Goal:** Give every one of the nine DD skills separately identified discoverability tests and explicitly loaded behavioral-effectiveness tests.
**Approach:** Reuse existing scenario material, runner configs, worksheets and written runbooks; no new testing framework or schema.
**Authority:** [Test-purpose separation](../specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-separation-setup-discovery-and-behavior) and [charter](../../skill-validation/charter/core-contracts.md).
**Return to:** [CW design and review checkpoint](../specs/2026-09-07-cw-validation-design.md#review-checkpoint).
The owner approved porting all existing CW sources and separating mixed purposes before baseline collection and rewrite evaluation; this does not activate the other eight skills' repairs.

## Audit findings

Read-only catalog-purpose review on 2026-09-07 against branch HEAD `d6ba84546e4e5547b457a8ed6f1982af75944c73`.
Inventoried all 105 prompt/config packages across ten catalogs; inspected loading/selection instructions, catalog summaries and relevant routing/composition rubrics.
This is a coverage/design audit, not a fresh execution, verdict review or complete re-audit of every semantic criterion.
The tenth catalog, skill-discovery, tests the nine DD descriptions; it is not a tenth DD skill.

1. **Native discoverability is untested by these packages.** None of the 105 configs declares native `.agents/skills/` or `.claude/skills/` targets. The twelve [DISC scenarios](../../skill-validation/scenarios/skill-discovery/summary.md) have no fixtures, paste descriptions and prohibit body reads. Their selection results are useful description-classification observations, not evidence of native discovery/loading. Earlier pilot catalog qualification proves setup availability, not spontaneous selection.
2. **Selection and application are combined in concise-writing.** [CW-17](../../skill-validation/scenarios/concise-writing/cw-17/prompt.md) and CW-18 read both descriptions and the skill body before requesting selection plus an application decision. [CW-13](../../skill-validation/scenarios/concise-writing/cw-13/prompt.md) and CW-14 require all supplied bodies, then combine applicable-skill selection, lifecycle ownership and an action choice in one exact-answer rubric. Split the future test purposes; a read-all directive cannot demonstrate spontaneous discovery.
3. **Not every skill-catalog test measures task effectiveness.** CW-09/11 are description classifiers; CW-10/12 extract a literal ownership sentence. Keep useful contract checks clearly labeled and optional to the core portfolio; do not count them as successful prose application or native discovery. Preserve the historical contract mismatches already disclosed by the [CW summary](../../skill-validation/scenarios/concise-writing/summary.md), without changing criteria to erase accepted FAILs.
4. **Composition and execution claims need bounded ownership.** The [DSD summary](../../skill-validation/scenarios/dispatching-development-subagents/summary.md#scenario-contract-observations) notes that DSD-11 asks for research-method selection without supplying the research body, and DSD-09 does not explicitly read its upstream fixture. Naming a method can test a loaded parent's dispatch judgment, but cannot establish the companion's execution effectiveness. WER-07 already separates target and composition-owner judgments; preserve that useful distinction.
5. **Existing routing language is not automatically a discovery defect.** DD mode/gate selection, AR lens selection and review-loop next-action choices are behavior after target loading. Their read-only answers are decision/application evidence, not proof of executed edits, dispatch, remediation or commits. Preserve these focused tests and label their claims accurately rather than splitting every choice into another scenario.

Across the inventory, 14 prompts are description-only selection tests (DISC-01–12 and CW-09/11); the other 91 request skill-body reads, including the four combined CW cases above.
This partitions prompt design only, not run validity or effectiveness.

## Per-skill coverage and reusable discovery seeds

The [validation guide's purpose map](../../skill-validation/README.md#coverage-by-test-purpose) is the single coverage table, with charter ownership, representative scenario links and discovery seeds for all nine skills.
The seeds are source material, not ready native tests or execution approval.

## Deferred work

The [CW mapping](../../skill-validation/pilot/cw-catalog.md) records the activated CW portion of Task 2; other-skill repairs and Task 3 collection remain separately gated.
The [batch/fixture-design amendment](../specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-bounded-batch-operation) governs later preparation and collection, not permission to launch them.

### Task 1: Map purposes without moving the catalog

- [x] Add one nine-skill coverage table to the validation guide: loaded behavior material, missing native discovery and separate diagnostics, with linked scenario IDs and charter ownership.
- [x] Map representative rubric clauses to evidence boundaries below. Preserve composition attribution and distinguish proposed workflow actions from executed work; this is not a clause-by-clause audit of all 105 rubrics.
- [x] Apply the criterion/evidence distinction to the pilot's LP and AR gaps without rescoring completed observations.
- [x] Obtain owner approval to prepare the three CW purposes for exact prompt/rubric review; keep broader contract dispositions such as DISC-08 pending.

### Representative criterion boundaries

These are design mappings, not replacement rubrics or new judgments of accepted runs.
Use the complete frozen rubric when scoring; exact presentation is fidelity unless an authenticated consumer gives it protocol ownership.

| Existing criterion | Owner / ledger | Required evidence and boundary |
|---|---|---|
| [CW-01](../../skill-validation/scenarios/concise-writing/cw-01/rubric.md): retain four states and download/error distinctions; add nothing | CW-I1 / semantic | Compare returned prose to supplied input. Missing a state/distinction or adding unsupported meaning fails preservation. A claimed skill read is not this evidence. |
| CW-01: remove the opener and both restatements | CW-I2 / semantic | Inspect the actual revision; retaining targeted padding fails. Shortness alone does not pass preservation. |
| [DD-05](../../skill-validation/scenarios/disciplined-development/dd-05/rubric.md): owner resolution before planning/implementation | DD-I1 / semantic | The checkpoint response must require fresh sources, owner resolution and both blocks. It proves the decision, not executed planning or a real approval. |
| [SSR-01](../../skill-validation/scenarios/sweeping-stale-references/ssr-01/rubric.md): read-only sweep evidence | SSR-I1–I4 / semantic | Actual reads/searches can support a proposed inventory and preserved rationale, not a completed edit or commit. Do not demand fabricated post-edit verification. |
| [DSD-03](../../skill-validation/scenarios/dispatching-development-subagents/dsd-03/prompt.md): integration inspection/disclosure | DSD-I3/I4 / semantic | Absent diffs permit only an inspection sequence and conditional disposition. Require each commit's stat/full-diff inspection in the response and flag the undisclosed README change; do not claim actual integration. |
| [LP-05](../../skill-validation/pilot/lp-05/current-dd/rubric.md): concrete tests and runnable verification | LP-I2 / semantic | The plan names behavioral tests and a command with usable task context; “run tests” does not suffice. Future fixtures supply framework/command/cwd; this does not mean the subject must execute absent application tests. |
| [AR-03](../../skill-validation/pilot/ar-03/current-dd/rubric.md) clauses 1–2: account for all callers and sorting | AR-I2 / semantic | Model-authored review must account for each caller's precondition. Tool output containing all source files is loading/inspection evidence, not an explicit caller account. |
| AR-03 clauses 3–5: benchmark, material defect and conclusion | AR-I3 and AR-I1 / respective semantic criteria | Review corrects 18% to 1.8%, explains the asymmetric ordering defect and blocks. These do not substitute for caller coverage. |
| AR-03 extra claims / future precision criterion | AR-I1 / semantic when explicitly included in a new rubric | Existing clause 2 does not require a post-normalization output-order finding. Retain completed caveats; a future rubric can explicitly reject unsupported extra findings, but not retrofit that verdict rule onto this pair. |

### First CW repair — bounded purposes

Start with concise-writing because it has a small real prose task and the clearest documented selection/application conflation; no new task-tool capability is needed to draft these inputs.
These three purposes defined the first CW increment, retaining all existing packages; the [prepared inputs](../../skill-validation/pilot/README.md#cw-purpose-separated-inputs) contain those unchanged prompts and criterion tables:

| New variant purpose | Reuse | Contract to preserve or separate |
|---|---|---|
| Loaded behavior | CW-01's supplied job-state prose and preservation/removal rubric | Explicitly load CW in current-DD; no-DD omits all DD directives/files. Compare the same actual prose task under fixed common inputs. |
| Native discovery, positive | The same prose task, using DISC-03's shortening trigger | Remove skill names, paths, descriptions and loading hints from the task prompt; supply qualified native skills. Judge observable unprompted CW selection/body loading, not prose effectiveness under the same verdict. |
| Native discovery, non-trigger | CW-17's response-only detailed-explanation request | Apply the charter's CW-I3 detailed-response exception without asking a routing quiz or loading CW first. Missing/ambiguous trace evidence is inconclusive, not proof of non-use. A complete observable trace supports only the scoped no-selection claim. |

The non-trigger expectation follows the charter even though current CW lacks that exception; retain any resulting failure rather than weakening the test to match the implementation.
The [full-CW expansion](../../skill-validation/pilot/cw-catalog.md) now prepares CW-18 durable-file discovery, separate loaded scope decisions, the remaining prose tasks and authoring/contract diagnostics.
The earlier CW-08/19 behavior pairs and discovery pair remain unchanged and eligible for audited medium-result reuse; CW-01 behavior receives new medium configs.
CW-09–14 remain composition/contract coverage, not core compression; the current skill deliberately excludes authoring, and its historical target mismatches are preserved.
Scope-contract answers do not establish hidden method use or actual authoring; that limit remains after this expansion.
For a future DISC-08 derivative, propose no CW selection for the explicit mechanical-only rename: the task forbids prose revision. Preserve the accepted optional-CW verdict under its original rubric until the owner approves a new contract.
No-DD is a behavioral control, not a discovery failure for an unavailable skill. The native-discovery variants test current-DD with target availability qualified and other skill loads disclosed.
Approve the exact prompts, input/criterion freeze and sampling separately before collection; preparation supplies neither run counts nor provider-call permission.

### Task 2: Prepare separate variants

The CW-only preparation and its review/qualification checkpoints are tracked by the [CW design](../specs/2026-09-07-cw-validation-design.md#review-checkpoint).
Other-skill items below remain deferred; no prepared config grants launch permission.

- [x] Prepare CW-13/14 native selection versus loaded lifecycle decisions and CW-17/18 native selection versus loaded scope diagnostics; retain CW-09–12 as labeled diagnostics. Owner input review and affected qualification remain pending in the CW design.
- [ ] For every DD skill, prepare native-discovery tasks without explicit skill names, paths, pasted descriptions or loading hints in the task prompt. Use frozen skills in the provider's qualified native paths. Start with relevant positive and boundary/non-trigger cases; reuse task ideas and approve exact counts before collection rather than multiplying the whole catalog.
- [ ] Keep behavior tasks explicitly loaded, with target/composed skill reads verified. No-DD omits all DD files/directives and retains the same relevant Superpowers; preserve common task facts, tools and criteria. Pin any companion whose actual behavior is judged rather than relying on ambient discovery.
- [ ] Supply prerequisite task facts in new fixtures. For LP variants requiring runnable verification, give both arms the same framework, command and cwd while retaining the explicit absent-source boundary; do not edit or recollect the completed pilot pair.
- [ ] Freeze separate discovery expectations: catalog availability is setup, observed unprompted selection/body loading is the measured path, and correct task output alone is not discovery success. Define missing/ambiguous trace handling without treating absence of evidence as proof of hidden non-use.

### Task 3: Audit, exercise and accept under separate approval

- [ ] Use existing config/preparation checks to validate sources, native targets, composition, withheld rubrics, CLI provenance and changed qualification controls. Missing dependencies or unproved controls stop launch.
- [ ] Publish written runbook commands, provider/model/effort, counts/order and separate worksheets before collection; obtain explicit approval of the bounded exact-command batch. Effectiveness sampling and acceptance criteria must be agreed before making effectiveness claims; one procedure observation is insufficient.
- [ ] Retain ignored loading instructions, behavioral FAILs and discovery failures; label fidelity/observability limits rather than discarding inconvenient observations. Do not pool discovery, contract diagnostics and effectiveness into one success score.
- [ ] Preserve all 105 historical accepted records. Collect new variants with fresh provenance; replace retained current sets only under the existing owner-accepted whole-set/Git-history policy. No automatic archive growth, directory migration or scratch cleanup.

## Scope and verification

Expected work is documentation, prompts, fixtures/configs and evaluator rubrics; change runner code only for a demonstrated required mechanical gap under separately approved scope.
No skill rewriting, hook work, Claude integration, model-matrix execution or unrelated worktree inspection belongs to this plan.
Use the [batch verification cadence](../../skill-validation/pilot/README.md#bounded-batches-and-approval): verify harness changes before collection, keep per-run controls, then check links/configs/evidence preservation and run the required hook suite once at the batch/unit handoff, not per observation.
Completion requires separately identifiable discovery and loaded-behavior coverage for all nine skills, reviewed evidence and an honest statement of what remains unexercised—not all observed skill results being PASS.
