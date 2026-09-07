# Separate Skill Discoverability and Effectiveness Coverage

> **For agentic workers:** On owner activation, use `superpowers:executing-plans` task by task with review checkpoints.

**Status:** DEFERRED. Catalog-purpose audit complete; no catalog repairs, new scenario configs or provider runs authorized by this plan.
**Goal:** Give every one of the nine DD skills separately identified discoverability tests and explicitly loaded behavioral-effectiveness tests.
**Approach:** Reuse existing scenario material, runner configs, worksheets and written runbooks; no new testing framework or schema.
**Authority:** [Test-purpose separation](../specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-separation-setup-discovery-and-behavior) and [charter](../../skill-validation/charter/core-contracts.md).
**Return to:** [Current behavior-only pilot](../2026-09-06-skilltest-sol-low-pilot.md#task-4-simplify-the-routine-and-propose-a-bounded-extension).

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

All rows need distinct native-discovery coverage; the DISC references are seed tasks to adapt, not ready native tests or approval to execute.
Each skill must also retain independently identified explicitly loaded behavior coverage; a shared composition scenario may reference multiple skills only with separate owner criteria/results.

| DD skill | Existing catalog and behavior material | Description-selection seeds / focused improvement |
|---|---|---|
| concise-writing | 17 scenarios; CW-01–08/19 exercise prose, CW-10/12 contract extraction | DISC-03; CW-09/11 and CW-17/18 supply boundary ideas. Separate the four combined cases and distinguish contract checks from prose application. |
| writing-explicit-rationale | 6; explicit target loads, WER-07 separates composition ownership | DISC-09/10. Retain target/companion scoring separation. |
| sweeping-stale-references | 6; explicit loads, read-only sweep/rename artifacts | DISC-08. Resolve its existing optional-concise-writing ambiguity for new inputs, not old judgments. |
| lean-plan-writing | 7; explicit target + writing-plans composition | DISC-07/10; contrast plan execution in DISC-04. Keep Superpowers fixed across behavior conditions. |
| disciplined-research | 7; explicit loads and source-grounded answers | DISC-05/11/12. Verify new trigger expectations against the frozen skill/charter, not copied historical description text alone. |
| disciplined-development | 9; explicit parent loads, gate/action decisions | DISC-04/05 versus non-development DISC-12. Do not mislabel repository-defect discovery in DD-02/09 as skill discovery. |
| adversarial-review | 15; explicitly loaded review and review-contract tasks | DISC-01 versus remediation DISC-02. Keep lens selection as loaded review behavior. |
| adversarial-review-loop | 15; explicit loads and next-action/ownership decisions | DISC-02 versus new review DISC-01. Read-only loop decisions do not prove actual repeated execution. |
| dispatching-development-subagents | 11; explicit loads, dispatch/handoff construction and decisions | DISC-06. Freeze required composition and distinguish selecting a companion from executing it. |

## Deferred work

Activate only after the current procedure pilot is owner-reviewed and the owner explicitly selects this work.
Do not make completing this catalog program a prerequisite for the current six proposed behavior observations.

### Task 1: Map purposes without moving the catalog

- [ ] Add a concise per-skill coverage table to the validation guide or existing catalog summaries: loaded behavior, native discoverability, and optional contract/description diagnostics. Link scenario IDs; do not create a parallel manifest.
- [ ] Map existing charter invariants and rubric clauses to their owning test purpose and observable evidence. Preserve useful composition tests without claiming they isolate each skill's independent contribution.
- [ ] Identify proposed replacements/new variants and get owner agreement before changing test contracts. Resolve the disclosed CW and DISC-08 ambiguities against charter intent, not desired outcomes.

### Task 2: Prepare separate variants

- [ ] Split CW-13/14 and CW-17/18's future selection and loaded-application purposes into separate prompts/rubrics; retain only useful diagnostics from CW-09–12.
- [ ] For every DD skill, prepare native-discovery tasks without explicit skill names, paths, pasted descriptions or loading hints in the task prompt. Use frozen skills in the provider's qualified native paths. Start with relevant positive and boundary/non-trigger cases; reuse task ideas and approve exact counts before collection rather than multiplying the whole catalog.
- [ ] Keep behavior tasks explicitly loaded, with target/composed skill reads verified. No-DD omits all DD files/directives and retains the same relevant Superpowers; preserve common task facts, tools and criteria. Pin any companion whose actual behavior is judged rather than relying on ambient discovery.
- [ ] Freeze separate discovery expectations: catalog availability is setup, observed unprompted selection/body loading is the measured path, and correct task output alone is not discovery success. Define missing/ambiguous trace handling without treating absence of evidence as proof of hidden non-use.

### Task 3: Audit, exercise and accept under separate approval

- [ ] Use existing config/preparation checks to validate sources, native targets, composition, withheld rubrics, CLI provenance and changed qualification controls. Missing dependencies or unproved controls stop launch.
- [ ] Publish written runbook commands, provider/model/effort, counts/order and separate worksheets before collection; obtain required exact-command approvals. Effectiveness sampling and acceptance criteria must be agreed before making effectiveness claims; one procedure observation is insufficient.
- [ ] Retain ignored loading instructions, behavioral FAILs and discovery failures; label fidelity/observability limits rather than discarding inconvenient observations. Do not pool discovery, contract diagnostics and effectiveness into one success score.
- [ ] Preserve all 105 historical accepted records. Collect new variants with fresh provenance; replace retained current sets only under the existing owner-accepted whole-set/Git-history policy. No automatic archive growth, directory migration or scratch cleanup.

## Scope and verification

Expected work is documentation, prompts, fixtures/configs and evaluator rubrics; change runner code only for a demonstrated required mechanical gap under separately approved scope.
No skill rewriting, hook work, Claude integration, model-matrix execution or unrelated worktree inspection belongs to this plan.
Before each activated unit's handoff, check changed links/anchors, config loading, frozen input comparability and protected-record preservation; run relevant offline tests and the repository-required hook suite.
Completion requires separately identifiable discovery and loaded-behavior coverage for all nine skills, reviewed evidence and an honest statement of what remains unexercised—not all observed skill results being PASS.
