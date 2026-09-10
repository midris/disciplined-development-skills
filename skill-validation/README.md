# Skill Validation

This directory contains the repository's validation contracts, packaged scenarios,
mechanical runner, and legacy records. This page summarizes the testing approach
and links its governing contracts; it creates no new scoring rules or execution authority.

Before authoring, editing or evaluating a skill, read the [charter](charter/core-contracts.md) and the complete existing skill body.
The charter gives core intent; the skill defines the specifics that its tests must measure, including scope, exceptions and companion responsibilities.
The [overall rewrite goal](../plans/completed/specs/2026-09-06-skilltest-controlled-inputs-design.md#overall-goal) and [RED/GREEN authoring requirement](../plans/completed/specs/2026-09-06-skilltest-controlled-inputs-design.md#redgreen-authoring-requirement) explain what this testing infrastructure supports.

For current state and the next decision, read the [single active testing plan](../plans/2026-09-09-dd-skill-testing.md).
Completed implementation and collection plans are archived; their accepted methodology contracts remain applicable.

## Model-led testing

Testing is model-led, built around the existing simple, reusable, deterministic tools: dumb tools for smart agents.
The orchestrating model derives tests from the reviewed baseline specification, audits inputs, invokes the tools, inspects raw evidence and applies the scenario rubrics.
The tools scaffold execution and record results; they do not decide what good skill behavior means.

- [`skilltest run CONFIG`](runner/README.md#run) prepares one declared run, invokes the configured provider and retains mechanical evidence.
- [`skilltest worksheet SCENARIO RUN_BUNDLE --output PATH`](runner/README.md#worksheet) renders run metadata and a blank assessment worksheet for the model to complete.

Reuse these tools for the testing workflow; extend them only when an observed mechanical gap justifies it, rather than building a separate autonomous testing framework.
The intended workflow is agent-followed written runbooks for baseline collection and skill edits, not more shell or Python programs.
Those runbooks specify fixture setup, exact commands, models/effort, actual CLI-version capture, repetitions, validation and evidence review before collection; routine test changes belong in those documents and test inputs, not runner code.
The [completed pilot](../plans/completed/2026-09-06-skilltest-sol-low-pilot.md) exercised this procedure; baseline tooling is settled for the current Codex and Claude local workflows.
Claude support passed its [local qualification](pilot/qualification/README.md#claude-qualification-checkpoint); broader campaign and reorganization decisions remain separately scoped.
Use the [routine runbook](pilot/README.md) for input/version checks, execution, evidence inspection, worksheet scoring and summary updates; consult the separate [qualification reference](pilot/qualification/README.md) when relevant controls change.
Use its [bounded-batch approval and verification cadence](pilot/README.md#bounded-batches-and-approval); retain per-run controls without repeated unchanged test suites or per-observation status commits.
The [archived CW design](../plans/completed/specs/2026-09-07-cw-validation-design.md) retains the completed baseline/candidate comparison contract and its evidence handoff.
Use the [CW baseline/edit runbook](pilot/cw-runbook.md) and [source-to-variant mapping](pilot/cw-catalog.md), not historical pilot command paths.
This README is navigation, not another progress record.
For new controlled testing, keep current accepted evidence in the working tree and recover superseded accepted results from Git history, rather than maintaining dated result archives; commit accepted evidence before replacing it.
Active experiments remain scratch-only pending review; historical baseline judgments and evidence remain protected, including the completed [metadata-only CLI-version worksheet backfill](../plans/completed/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-baseline-decision-current-dd-and-no-dd-with-cli-provenance).
The orchestrator owns evidence-backed judgments, the owner retains acceptance authority, and provider calls remain subject to approval.
On 2026-09-09 the owner accepted the validity of the [66-observation CW candidate comparison](accepted/concise-writing/codex-gpt-5.6-sol-medium-candidate/README.md) and [14 procedure-pilot observations](accepted/procedure-pilot/codex-gpt-5.6-sol-low/README.md).
Their complete packages are preserved separately from the baseline; further evaluation and skill decisions remain open.
Keep [setup qualification, discovery and behavior tests separate](../plans/completed/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-separation-setup-discovery-and-behavior): behavior prompts explicitly load the relevant skills; only dedicated discovery scenarios omit loading hints.
Every DD skill needs both discoverability and loaded-behavior coverage; the [catalog audit and repair proposal](../plans/deferred/2026-09-07-skilltest-discovery-behavior-catalog-separation.md) track gaps and link the currently authorized CW increment without activating the broader repairs.
The [accepted design decisions](../plans/completed/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-methodology-decision-model-led-testing-with-simple-tools) record the accepted model/tool boundary, workflow decisions and separately labeled proposals.

## Baseline specification first

The owner established this approach on 2026-09-10.
Read the charter and the exact baseline skill body, then write a behavioral specification grounded in both: purpose, applicability, promised behavior, exceptions, method and composition boundaries.
Record the source revision/hash so a later rewrite cannot silently change the specification.
Where the charter, historical targets or existing rubrics differ from the baseline's actual promises, document the difference; do not score a desired future rule as an existing-skill failure.

Review that specification, then derive or reconcile scenarios and rubrics against its concrete obligations and reader outcomes.
Use existing catalog/rubric mappings and worksheet ledgers; do not add a tracking framework.
Establish how effectively the baseline fulfills those promises using actual evidence and meaningful controls, then compare rewrites against the agreed specification and conditions.
A baseline specification describes intended behavior; it does not assume the baseline passes its tests.
Preserve prior evidence and frozen judgments when correcting a specification or evaluator assumption.

The [reviewed CW baseline specification](../plans/specs/2026-09-10-cw-baseline-specification.md) is the first pilot under this approach; its [catalog audit](pilot/cw-catalog.md#routine-suite-coverage) led to [reviewed task inputs](pilot/cw-catalog.md#prospective-input-map), and [reviewed scoring](pilot/cw-runbook.md#prospective-scoring) approved for commit/push; the initial collection schedule is next.
This changes the source of test requirements, not the settled tools, common categories or evidence ledgers.
CW now uses grouped outcomes with source checklists and a [small initial selection](pilot/cw-catalog.md#initial-pilot-selection) to check scoring usability before broader collection.

### Starting the next skill

Apply this workflow to each owner-selected skill; CW is the pilot, not the only recipient of these requirements.
Use the [baseline composition map](../ARCHITECTURE.md#composition-boundaries) to identify leaf tasks and required upstream workflows, then verify those relationships against the selected skill bodies.
In that skill's baseline specification, record its primary development use, applicable broader uses, standalone limits, required Superpowers guidance and DD companion responsibilities using [intended use and dependencies](#intended-use-and-dependencies).
Read `superpowers:writing-skills` and the testing guidance relevant to that skill's behavior before auditing its catalog, using [Superpowers authoring guidance](#superpowers-authoring-guidance) to identify appropriate application, pressure, boundary and edit-regression coverage.
Review the specification against the actual skill, audit its full catalog and resolve coverage gaps, then settle scoring before collecting evidence or judging edits.
Keep the decisions in the skill's specification and existing catalog, with progress in the active plan; do not create a separate checklist system or activate other catalogs automatically.

## Coverage by test purpose

### Intended use and dependencies

Development projects are the primary use case: the DD bundle should work together through realistic project tasks.
Some skills also serve non-development projects; preserve representative cases where their baseline scope supports that use.
The owner specifically wants this broader usefulness from concise-writing and disciplined-development; record any mismatch with a skill's existing scope before proposing an extension.
For each specification, identify whether the skill orchestrates other skills, refines a named upstream skill, or can perform its task independently of other DD skills.
Standalone use still assumes Superpowers is installed and available, together with any dependencies required by the task.
DD hooks are not a prerequisite for skill effectiveness.

Cover the relevant standalone behavior and actual composition responsibilities, without requiring every skill pair or a full development lifecycle in every test.
Use the existing fixture declarations and worksheets to distinguish supplied skills, observed loading and behavior.
A successful run with the full DD bundle available does not by itself establish standalone effectiveness or isolate one skill's contribution.

### Superpowers authoring guidance

Use `superpowers:writing-skills` and its applicable testing reference when preparing skill edits; record the exact supplied version/bytes with the evaluation inputs.
Its RED-GREEN-REFACTOR and wording-test requirements are retained in the [authoring contract](../plans/completed/specs/2026-09-06-skilltest-controlled-inputs-design.md#redgreen-authoring-requirement).
Match test design to the behavior: discipline rules need realistic pressure and bypass opportunities; techniques need application, variation and missing-context cases; patterns need recognition and counterexamples; references need retrieval and use.
These approaches fit beneath the common categories below; they do not create additional categories or a fixed case count.

When reviewing an edit, inspect discoverable descriptions, usable instructions/examples/references, preserved scope and exceptions, and compatibility with required companions.
Record structural authoring checks as supporting review evidence; behavioral claims still require observable task evidence under the skill's specification.
Classify an observed failure before choosing a remedy: bypassed discipline, ineffective output, an omitted element or a mishandled condition need different guidance.
Use the existing cases for regressions and variations where they exercise that distinction; add a test only for a missing behavior or boundary.
An ordinary control pass remains useful baseline evidence even when it supplies no RED for new guidance.
Applying writing-skills to the authoring workflow does not make it a required companion of every skill being tested or impose its word-count targets on CW task outputs.

### Shared categories

Use the shared categories **discoverability, effectiveness and composition**, with cases derived from each skill's baseline specification beneath them.
The [coverage policy](../plans/completed/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-methodology-decision-shared-test-categories-and-coverage) defines evidence boundaries, supporting diagnostics, overlap/gap review and model-dependent interpretation.
Keep multiple tests when they cover distinct failures, boundaries or meaningful contexts; neither matching test counts across skills nor superficial variations establish adequate coverage.

This is a design map of reusable scenario material, not an effectiveness score or a claim that every charter invariant has executed-work coverage.
The catalog summaries retain detailed scenario assessments; representative IDs below link directly to the relevant task or rubric.
None of the 105 historical configs declares native skill targets; DISC-01–12 paste descriptions and prohibit body reads.
Those historical packages do not test native discoverability; the explicitly loaded pilot and setup qualification do not fill that gap.
The [CW mapping](pilot/cw-catalog.md) separates loaded behavior, contract diagnostics and native discovery in the controlled portfolio; the [active testing plan](../plans/2026-09-09-dd-skill-testing.md) owns remaining evidence decisions and prospective suite work.
Dedicated native-discovery validation for the other eight DD targets remains deferred; incidental companion loading in CW tests does not replace it.
The discovery seeds below need fresh natural-task prompts and frozen native fixtures before use, not replay of the routing quizzes.

| Skill / charter | Explicitly loaded behavior material | Diagnostics, composition and discovery seeds |
|---|---|---|
| [concise-writing](charter/core-contracts.md#concise-writing) | [CW-01](scenarios/concise-writing/cw-01/rubric.md)–06/08: lossless compression (CW-I1/I2); [CW-19](scenarios/concise-writing/cw-19/rubric.md): complex conservation. | [Historical catalog](scenarios/concise-writing/summary.md): transport, classification, extraction and mixed selection/contract tasks. The [current CW audit](pilot/cw-catalog.md#routine-suite-coverage) replaces the old response/file polarity and authoring targets with proposed baseline-aligned coverage; those historical expectations remain evidence context only. |
| [writing-explicit-rationale](charter/core-contracts.md#writing-explicit-rationale) | [WER-01](scenarios/writing-explicit-rationale/wer-01/rubric.md)/06/08: useful rationale and placement (WER-I1/I2); [WER-05](scenarios/writing-explicit-rationale/wer-05/rubric.md): one home (WER-I2/I3); WER-02: repeated-challenge audit (WER-I4). | [Catalog](scenarios/writing-explicit-rationale/summary.md): WER-07 keeps target and composition-owner judgments separate. [DISC-09](scenarios/skill-discovery/disc-09/prompt.md)/10 seed discovery. |
| [sweeping-stale-references](charter/core-contracts.md#sweeping-stale-references) | [SSR-01](scenarios/sweeping-stale-references/ssr-01/rubric.md)/02: observed reads/searches and proposed reconciliation (SSR-I1–I4); SSR-03/05/06: inventory/count boundaries; SSR-07: rationale preservation. | [Catalog](scenarios/sweeping-stale-references/summary.md): no actual edit/commit claim from read-only answers. [DISC-08](scenarios/skill-discovery/disc-08/prompt.md) seeds discovery; its optional CW route needs a future-contract decision. |
| [lean-plan-writing](charter/core-contracts.md#lean-plan-writing) | [LP-02](scenarios/lean-plan-writing/lp-02/rubric.md)/03: prose versus necessary illustration (LP-I1/I3); [LP-05](scenarios/lean-plan-writing/lp-05/rubric.md)/06: executable contract and edges (LP-I2); LP-07/08: split/atomic polarity (LP-I4). | [Catalog](scenarios/lean-plan-writing/summary.md): retain writing-plans composition, with LP-01's upstream scaffold separate. [DISC-07](scenarios/skill-discovery/disc-07/prompt.md)/10 versus plan execution in DISC-04 seed discovery boundaries. |
| [disciplined-research](charter/core-contracts.md#disciplined-research) | [DR-02](scenarios/disciplined-research/dr-02/rubric.md): authority/conflict/support (DR-I1–I3); [DR-05](scenarios/disciplined-research/dr-05/rubric.md)/06: missing facts and unsupported leads (DR-I4); DR-07: conversational grounding. | [Catalog](scenarios/disciplined-research/summary.md): actual source reads plus truthful answer support, not source-name recall. [DISC-05](scenarios/skill-discovery/disc-05/prompt.md)/11/12 seed discovery across destinations. |
| [disciplined-development](charter/core-contracts.md#disciplined-development) | [DD-05](scenarios/disciplined-development/dd-05/rubric.md)/02: gate/block/restart decisions (DD-I1); DD-07: parent authority (DD-I2); DD-08: evidence/commit decisions (DD-I3); DD-03: bounded implementation (DD-I4). | [Catalog](scenarios/disciplined-development/summary.md): DD-01 mode routing is loaded behavior; DD-04 separates research ownership. [DISC-04](scenarios/skill-discovery/disc-04/prompt.md)/05 versus non-development DISC-12 seed native selection. Repository-defect discovery in DD-02/09 is not skill discovery. |
| [adversarial-review](charter/core-contracts.md#adversarial-review) | [AR-03](scenarios/adversarial-review/ar-03/rubric.md): evidenced blocker, caller accounting and rationale (AR-I1–I3); AR-06: generated cases; AR-10/12: necessity; AR-13/15: false-pattern/clean-work restraint (AR-I1/I4). | [Catalog](scenarios/adversarial-review/summary.md): AR-04 lens routing and AR-02 output-contract checks are not native discovery. [DISC-01](scenarios/skill-discovery/disc-01/prompt.md) versus remediation DISC-02 seeds selection. |
| [adversarial-review-loop](charter/core-contracts.md#adversarial-review-loop) | [CS](scenarios/adversarial-review-loop/cs/rubric.md)/T2: class completeness (ARL-I1); NF/PW and G3A/B: shared-root/scattered decisions (ARL-I2); T3/CE: cap escape (ARL-I3); OWN/G3C/T5: ownership and disposition (ARL-I4). | [Catalog](scenarios/adversarial-review-loop/summary.md): next-action responses do not prove executed remediation or fresh-reviewer identity. [DISC-02](scenarios/skill-discovery/disc-02/prompt.md) versus new review DISC-01 seeds discovery. |
| [dispatching-development-subagents](charter/core-contracts.md#dispatching-development-subagents) | [DSD-01](scenarios/dispatching-development-subagents/dsd-01/rubric.md)/04/07: scope (DSD-I1); DSD-02/09/10: child authority (DSD-I2); [DSD-03](scenarios/dispatching-development-subagents/dsd-03/prompt.md)/08: inspection and disclosure decisions (DSD-I3/I4). | [Catalog](scenarios/dispatching-development-subagents/summary.md): DSD-09 omits an upstream read directive; DSD-11 supplies no research body. Method selection does not prove companion execution. [DISC-06](scenarios/skill-discovery/disc-06/prompt.md) seeds discovery. |

Composition results belong to their owning skills, not a pooled verdict; supplied availability, observed loading and applied behavior remain different facts.
The [criterion map and first-repair proposal](../plans/deferred/2026-09-07-skilltest-discovery-behavior-catalog-separation.md#task-1-map-purposes-without-moving-the-catalog) retain the earlier audit without activating the charter's broader rebuilt suite.

## Authority map

- [Core contracts](charter/core-contracts.md) records the owner-approved validation
  architecture and proposed core portfolios. Its own status governs what is active.
- [Scenario index](scenarios/README.md) inventories the packaged schema `"0.2"`
  scenarios and identifies their source and packaging authority.
- [Methodology](../plans/completed/specs/2026-09-02-skill-testing-methodology-design.md)
  defines the evaluation ledgers, evidence review and scenario verdicts.
- [Runner](runner/README.md) defines the mechanical `skilltest` interface. It does
  not score evidence or assign behavioral verdicts, and provider invocation still
  requires explicit owner approval.
- [Legacy archive](archive/README.md) holds the pre-baseline validation records.
  Until an approved catalog replaces one, its archived per-skill record remains the
  update target required by `CLAUDE.md`.
- [Controlled-input design amendment](../plans/completed/specs/2026-09-06-skilltest-controlled-inputs-design.md)
  preserves accepted feasibility/methodology constraints and the completed pilot design.
  Its status identifies approved implementation units separately from deferred work and provider-call approvals.

The broader baseline organization design is deferred. This index does not designate
accepted baselines, create manifests or campaign state, or declare any scenario
audited.
