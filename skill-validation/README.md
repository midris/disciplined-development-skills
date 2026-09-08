# Skill Validation

This directory contains the repository's validation contracts, packaged scenarios,
mechanical runner, and legacy records. This page summarizes the testing approach
and links its governing contracts; it creates no new scoring rules or execution authority.

Before authoring, editing or evaluating a skill, read the [charter](charter/core-contracts.md).
It already defines each skill's intended behavior through named invariants; test that contract rather than reconstructing it from the current skill's wording.
The [overall rewrite goal](../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#overall-goal) and [RED/GREEN authoring requirement](../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#redgreen-authoring-requirement) explain what this testing infrastructure supports.

## Model-led testing

Testing is model-led, built around the existing simple, reusable, deterministic tools: dumb tools for smart agents.
The orchestrating model selects or prepares tests from the charter, audits inputs, invokes the tools, inspects raw evidence and applies the scenario rubrics.
The tools scaffold execution and record results; they do not decide what good skill behavior means.

- [`skilltest run CONFIG`](runner/README.md#run) prepares one declared run, invokes the configured provider and retains mechanical evidence.
- [`skilltest worksheet SCENARIO RUN_BUNDLE --output PATH`](runner/README.md#worksheet) renders run metadata and a blank assessment worksheet for the model to complete.

Reuse these tools for the testing workflow; extend them only when an observed mechanical gap justifies it, rather than building a separate autonomous testing framework.
The intended workflow is agent-followed written runbooks for baseline collection and skill edits, not more shell or Python programs.
Those runbooks specify fixture setup, exact commands, models/effort, actual CLI-version capture, repetitions, validation and evidence review before collection; routine test changes belong in those documents and test inputs, not runner code.
The [pilot-first scope](../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-immediate-scope-one-usable-pilot) starts with one provisional runbook and a few Codex / gpt-5.6-sol / low scenarios in the existing layout, with medium available for justified workflow diagnostics; Claude integration, the broader campaign and reorganization wait for practical feedback.
Use the [routine runbook](pilot/README.md) for input/version checks, execution, evidence inspection, worksheet scoring and summary updates; consult the separate [qualification reference](pilot/qualification/README.md) when relevant controls change.
Use its [bounded-batch approval and verification cadence](pilot/README.md#bounded-batches-and-approval); retain per-run controls without repeated unchanged test suites or per-observation status commits.
The [pilot plan](../plans/2026-09-06-skilltest-sol-low-pilot.md) retains completed procedure/qualification checkpoints; the [CW design](../plans/specs/2026-09-07-cw-validation-design.md) owns full-CW catalog preparation, collection and owner review before rewrite evaluation.
Use the [CW baseline/edit runbook](pilot/cw-runbook.md) and [source-to-variant mapping](pilot/cw-catalog.md), not historical pilot command paths.
This README is navigation, not another progress record.
For new controlled testing, keep current accepted evidence in the working tree and recover superseded accepted results from Git history, rather than maintaining dated result archives; commit accepted evidence before replacing it.
Active experiments remain scratch-only pending review; historical baseline judgments and evidence remain protected, with only the [metadata-only CLI-version worksheet backfill](../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-baseline-decision-current-dd-and-no-dd-with-cli-provenance) authorized.
The orchestrator owns evidence-backed judgments, the owner retains acceptance authority, and provider calls remain subject to approval.
Keep [setup qualification, discovery and behavior tests separate](../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-separation-setup-discovery-and-behavior): behavior prompts explicitly load the relevant skills; only dedicated discovery scenarios omit loading hints.
Every DD skill needs both discoverability and loaded-behavior coverage; the [catalog audit and repair proposal](../plans/deferred/2026-09-07-skilltest-discovery-behavior-catalog-separation.md) track gaps and link the currently authorized CW increment without activating the broader repairs.
The [live design](../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-methodology-decision-model-led-testing-with-simple-tools) records the accepted model/tool boundary, workflow decisions and separately labeled proposals.

## Coverage by test purpose

This is a design map of reusable scenario material, not an effectiveness score or a claim that every charter invariant has executed-work coverage.
The catalog summaries retain detailed scenario assessments; representative IDs below link directly to the relevant task or rubric.
None of the 105 historical configs declares native skill targets; DISC-01–12 paste descriptions and prohibit body reads.
Those historical packages do not test native discoverability; the explicitly loaded pilot and setup qualification do not fill that gap.
The separate [CW procedure batch](../plans/2026-09-06-skilltest-sol-low-pilot.md#task-9-qualify-and-exercise-the-cw-purposes) adds one positive and one non-trigger native-discovery observation, pending owner acceptance; native discovery remains unexercised for the other eight skills.
The discovery seeds below need fresh natural-task prompts and frozen native fixtures before use, not replay of the routing quizzes.

| Skill / charter | Explicitly loaded behavior material | Diagnostics, composition and discovery seeds |
|---|---|---|
| [concise-writing](charter/core-contracts.md#concise-writing) | [CW-01](scenarios/concise-writing/cw-01/rubric.md)–06/08: lossless compression (CW-I1/I2); [CW-19](scenarios/concise-writing/cw-19/rubric.md): complex conservation. | [Catalog](scenarios/concise-writing/summary.md): CW-07 transport, CW-09/11 description classification, CW-10/12 literal contract extraction. CW-13/14 and CW-17/18 mix selection with contract decisions. [DISC-03](scenarios/skill-discovery/disc-03/prompt.md) seeds positive discovery; CW-I3's response/file boundary needs separate tests. |
| [writing-explicit-rationale](charter/core-contracts.md#writing-explicit-rationale) | [WER-01](scenarios/writing-explicit-rationale/wer-01/rubric.md)/06/08: useful rationale and placement (WER-I1/I2); [WER-05](scenarios/writing-explicit-rationale/wer-05/rubric.md): one home (WER-I2/I3); WER-02: repeated-challenge audit (WER-I4). | [Catalog](scenarios/writing-explicit-rationale/summary.md): WER-07 keeps target and composition-owner judgments separate. [DISC-09](scenarios/skill-discovery/disc-09/prompt.md)/10 seed discovery. |
| [sweeping-stale-references](charter/core-contracts.md#sweeping-stale-references) | [SSR-01](scenarios/sweeping-stale-references/ssr-01/rubric.md)/02: observed reads/searches and proposed reconciliation (SSR-I1–I4); SSR-03/05/06: inventory/count boundaries; SSR-07: rationale preservation. | [Catalog](scenarios/sweeping-stale-references/summary.md): no actual edit/commit claim from read-only answers. [DISC-08](scenarios/skill-discovery/disc-08/prompt.md) seeds discovery; its optional CW route needs a future-contract decision. |
| [lean-plan-writing](charter/core-contracts.md#lean-plan-writing) | [LP-02](scenarios/lean-plan-writing/lp-02/rubric.md)/03: prose versus necessary illustration (LP-I1/I3); [LP-05](scenarios/lean-plan-writing/lp-05/rubric.md)/06: executable contract and edges (LP-I2); LP-07/08: split/atomic polarity (LP-I4). | [Catalog](scenarios/lean-plan-writing/summary.md): retain writing-plans composition, with LP-01's upstream scaffold separate. [DISC-07](scenarios/skill-discovery/disc-07/prompt.md)/10 versus plan execution in DISC-04 seed discovery boundaries. |
| [disciplined-research](charter/core-contracts.md#disciplined-research) | [DR-02](scenarios/disciplined-research/dr-02/rubric.md): authority/conflict/support (DR-I1–I3); [DR-05](scenarios/disciplined-research/dr-05/rubric.md)/06: missing facts and unsupported leads (DR-I4); DR-07: conversational grounding. | [Catalog](scenarios/disciplined-research/summary.md): actual source reads plus truthful answer support, not source-name recall. [DISC-05](scenarios/skill-discovery/disc-05/prompt.md)/11/12 seed discovery across destinations. |
| [disciplined-development](charter/core-contracts.md#disciplined-development) | [DD-05](scenarios/disciplined-development/dd-05/rubric.md)/02: gate/block/restart decisions (DD-I1); DD-07: parent authority (DD-I2); DD-08: evidence/commit decisions (DD-I3); DD-03: bounded implementation (DD-I4). | [Catalog](scenarios/disciplined-development/summary.md): DD-01 mode routing is loaded behavior; DD-04 separates research ownership. [DISC-04](scenarios/skill-discovery/disc-04/prompt.md)/05 versus non-development DISC-12 seed native selection. Repository-defect discovery in DD-02/09 is not skill discovery. |
| [adversarial-review](charter/core-contracts.md#adversarial-review) | [AR-03](scenarios/adversarial-review/ar-03/rubric.md): evidenced blocker, caller accounting and rationale (AR-I1–I3); AR-06: generated cases; AR-10/12: necessity; AR-13/15: false-pattern/clean-work restraint (AR-I1/I4). | [Catalog](scenarios/adversarial-review/summary.md): AR-04 lens routing and AR-02 output-contract checks are not native discovery. [DISC-01](scenarios/skill-discovery/disc-01/prompt.md) versus remediation DISC-02 seeds selection. |
| [adversarial-review-loop](charter/core-contracts.md#adversarial-review-loop) | [CS](scenarios/adversarial-review-loop/cs/rubric.md)/T2: class completeness (ARL-I1); NF/PW and G3A/B: shared-root/scattered decisions (ARL-I2); T3/CE: cap escape (ARL-I3); OWN/G3C/T5: ownership and disposition (ARL-I4). | [Catalog](scenarios/adversarial-review-loop/summary.md): next-action responses do not prove executed remediation or fresh-reviewer identity. [DISC-02](scenarios/skill-discovery/disc-02/prompt.md) versus new review DISC-01 seeds discovery. |
| [dispatching-development-subagents](charter/core-contracts.md#dispatching-development-subagents) | [DSD-01](scenarios/dispatching-development-subagents/dsd-01/rubric.md)/04/07: scope (DSD-I1); DSD-02/09/10: child authority (DSD-I2); [DSD-03](scenarios/dispatching-development-subagents/dsd-03/prompt.md)/08: inspection and disclosure decisions (DSD-I3/I4). | [Catalog](scenarios/dispatching-development-subagents/summary.md): DSD-09 omits an upstream read directive; DSD-11 supplies no research body. Method selection does not prove companion execution. [DISC-06](scenarios/skill-discovery/disc-06/prompt.md) seeds discovery. |

Composition results belong to their owning skills, not a pooled verdict; supplied availability, observed loading and applied behavior remain different facts.
The [criterion map and first-repair proposal](../plans/deferred/2026-09-07-skilltest-discovery-behavior-catalog-separation.md#task-1-map-purposes-without-moving-the-catalog) identify the next design checkpoint without activating the charter's broader rebuilt suite.

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
- [Controlled-input design amendment](../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md)
  records accepted feasibility constraints and the current step-by-step design discussion.
  Its status identifies approved implementation units separately from deferred work and provider-call approvals.

The broader baseline organization design is deferred. This index does not designate
accepted baselines, create manifests or campaign state, or declare any scenario
audited.
