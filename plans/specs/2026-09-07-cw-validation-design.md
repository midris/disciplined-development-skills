# Minimal CW baseline and edit testing

**Status:** The owner approved the presented portfolio/inputs and an 18-run baseline schedule: Codex / gpt-5.6-sol / medium only, three repetitions per condition, fully scored.
Preparation and freezing may proceed; provider invocation still requires explicit approval of the exact command list.
No skill edit, additional model/catalog campaign or promotion of pilot evidence is authorized.
**Workspace:** `.worktrees/cw-validation-design`, branch `feature/cw-validation-design`.
**Contract:** [CW charter](../../skill-validation/charter/core-contracts.md#concise-writing), [controlled-input decisions](2026-09-06-skilltest-controlled-inputs-design.md), and the [CW runbook](../../skill-validation/pilot/cw-runbook.md).

## Selected portfolio

| Source | Primary purpose | Conditions |
|---|---|---|
| CW-08 | Loaded behavior: remove policy padding without losing eligibility, dates, exceptions or navigation; CW-I1/I2 and the non-software domain of CW-I3. | No-DD and current-DD; candidate-DD after separately authorized authoring. |
| CW-19 | Loaded behavior: conserve exact thresholds, actors, order, authorization, rationale and recovery boundaries under compression; CW-I1/I2. | No-DD and current-DD; candidate-DD after separately authorized authoring. |
| Prepared CW-01 discovery variant | Native positive discovery for a prose-shortening task; CW-I3. | Current-DD; candidate-DD when comparing edits. |
| Prepared CW-17 discovery variant | Native non-trigger for an explicitly detailed response-only request; CW-I3. | Current-DD; candidate-DD when comparing edits. |

CW-08 overlaps the pilot's ordinary CW-01 behavior case while adding a non-software boundary, so the routine set does not repeat CW-01 behavior.
Keep that completed evidence and its inputs unchanged; it remains available for a targeted regression if a later edit warrants it.
CW-19 protects a distinct, previously observed conservation failure; the historical result does not predict a new no-DD result or establish controlled RED.

This is useful focused coverage, not the whole charter or a replacement for all historical scenarios.
Explicitly loaded detailed-response handling, CW-18's durable-file contrast, the remaining padding patterns and skill-authoring composition remain outside this increment.
They need separate observable contracts rather than being inferred from discovery, response length or a good rewrite.
The [broader catalog repairs](../deferred/2026-09-07-skilltest-discovery-behavior-catalog-separation.md) remain deferred.

## Inputs and attribution

Add CW-08/CW-19 pairs alongside existing pilot packages; preserve historical scenarios and completed pilot inputs.
Reuse the already frozen nine DD bodies and four Superpowers files; current-DD is this recorded pre-rewrite composition, not a moving alias for installed skills.
No-DD removes all DD files and loading directives, retaining the same Superpowers files and ordinary task tools.
Both behavior tasks explicitly load only CW in current-DD, then revise supplied prose; they do not execute the operational commands quoted in the prose.
Other observed skill reads are disclosed composition evidence, not independently attributed CW effectiveness.
Discovery reuses its existing hint-free prompts, native paths and separate selection rubrics without modification.
No DD hooks, new subject tools, runner changes, schema changes or directory migration are needed.

Use identical task text, rubric and restrictions within each behavior pair; the CW loading prefix and DD availability are the intended treatment differences.
CW-19's existing eight semantic criteria and actor/context rules remain normative; the new rubric explicitly separates output-only/read-only fidelity from semantics.
Freeze linked evaluator guidance as well as each local rubric; worksheet hashing of the local rubric alone does not freeze its links.
Keep all evaluator guidance outside subject inputs.

## Collection and edit boundary

The approved schedule is six conditions × three repetitions at Sol medium = 18 fresh observations: 12 behavior and six discovery.
Sol medium matches the owner's ordinary workload; retain repetitions to observe some run-to-run variation while deferring cross-effort/model comparisons.
Low, high, Astra, Terra, Claude and the remaining CW scenarios are excluded; these results do not establish effectiveness in those settings.
The former 54-command proposal is superseded and must not be executed.
The [runbook](../../skill-validation/pilot/cw-runbook.md#test-set) fixes order, config/rubric mapping and reporting before execution.
Three repetitions give an initial view of variation, not a precise reliability estimate, universal effectiveness claim or automatic skill-GREEN decision.
Report each scenario/condition/effort separately with all criterion judgments; do not pool discovery with behavior or increase counts in response to split verdicts.
Later authoring acceptance/repetition rules still require agreement; this schedule does not activate the charter's conditional historical suite or waive applicable writing-skills requirements.

Before authoring, identify a judgeable no-DD failure against a frozen behavior criterion.
If no-DD passes, retain it as a passing control; do not label the absence of DD as RED or raise effort/repeat until failure.
Current-DD versus candidate-DD tests improvements/regressions in the declared composition; no-DD remains the authoring control.
Discovery failures are separate from behavioral RED, and an unavailable target is not a discovery failure.
The runbook specifies candidate preparation and evidence reuse checks without authorizing candidate files or assuming a fixed number of edit iterations.

## Review checkpoint

- [x] Record the owner-approved portfolio and bounded omissions.
- [x] Prepare and provider-free audit the four new input packages; preserve all previous inputs/evidence.
- [x] Draft and review one baseline/edit runbook with existing commands and linked recovery/scoring procedures.
- [x] Owner reviews the presented inputs and approves the medium-only 18-run baseline schedule; candidate authoring remains separately gated.
- [x] Prepare and audit the six selected medium configs; review the schedule amendment.
- [x] Reconcile qualification against retained evidence; no new paid setup probe is required for unchanged controls.
- [ ] Freeze the reviewed revision and present a fully expanded finite command batch for approval.

Stop at exact-command approval; no provider command is approved by completing the preceding checks.
The selected six medium configs are unchanged members of the provider-free audited matrix: shared prompt/fixture identity, paired rubric/loading differences, withheld inputs and argv controls were verified.
Unused low/high configs remain outside the authorized schedule; no input or runner change is required to narrow collection.
Protected skills, runner code, historical scenarios and previous pilot inputs are unchanged; the frozen-input verification passed 231 runner tests and 263 hook tests with three skips.
Review was inline because the session has no no-write-tool reviewer type; no provider or authentication call was used.
