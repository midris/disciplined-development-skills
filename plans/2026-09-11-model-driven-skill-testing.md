# Model-driven skill testing: first complete study

> **For agentic workers:** Use `superpowers:executing-plans` for authorized work. This document alone owns the execution checklist.

**Goal:** Reach an evidence-backed decision about improving one DD skill, then use the experience to refine the general testing approach.
**Architecture:** Models interpret skills and assess outcomes; the existing runner and deterministic checks execute tasks and preserve independently inspectable evidence.
**Tech stack:** Checked-in Markdown skills, the Python `skilltest` runner, files and Git.
**Spec:** [General testing responsibilities](specs/2026-09-11-model-driven-skill-testing-framework.md).

**Authority and state:** This is the current plan for preparing the study; it replaces the previous nine-task plan and its separate six-stage proposal.
Preparation and documentation work are authorized. Candidate selection, provider spending, a rewrite objective and adoption require the owner decisions identified below; no experiment or rewrite has begun.
The spec governs how the study is designed. Neither document grants provider-run authorization.
External reviews and responses are recorded in the [review record](../reviews/2026-09-11-model-driven-testing-plan-review.md); the latest supplied protocol review reported BLOCK, with no subsequent external PASS on these edits.
On 2026-09-12 the owner accepted the next steps and selected `sweeping-stale-references`. Stage 1 preparation is active; limits remain provisional until the contract/allocation walkthrough, before test design.

## Starting or resuming without conversation history

Read [CLAUDE.md](../CLAUDE.md), this plan and the spec; inspect the working tree and existing worktrees before editing.
Preserve unrelated changes and identify original skill bytes by revision and hash.
Use the [runner guide](../skill-validation/runner/README.md) for mechanics; its fixed worksheet and historical methodology links do not govern this study.
Read installed workflow skills from the available catalog rather than relying on a previous installation path.
Read the [purpose and relationship map](../ARCHITECTURE.md#composition-boundaries) for orientation; distinguish independent use, explicit pairings and DD orchestration before deciding subject context.

The study workspace is `skill-studies/sweeping-stale-references/`.
Its only new narrative document is [protocol.md](../skill-studies/sweeping-stale-references/protocol.md): it holds concrete decisions, versions, commands, artifact links, run accounting and the final conclusion, without another task checklist.
Fixtures, checkers, raw bundles and assessments are supporting artifacts linked from that record.
This plan owns progress; the spec owns general rules; the protocol owns study-specific facts and decisions.
On resumption, use recorded decisions and evidence to select the next incomplete action; do not repeat settled approvals or infer authorization from a checked box.

Historical material stays in place with its abandonment notices.
The [preservation record](../skill-validation/archive/local-cw-scoring-rebuild-2026-09-11/README.md) indexes a verified local snapshot of `/private/tmp/cw-scoring-rebuild-gep1e4ek/` and the eight archived CW-17/CW-18 inputs; the scratch payload stays outside Git, while the inputs and manifest are versioned.
A broader archival reorganization is outside this study.

## Proposed limits and information boundaries

**Proposed outer limits: 40 subject, 12 evaluator, 4 authoring and 4 retry invocations (60 total), plus 20 hours of active study work.**
Use these provisional ceilings to prepare Stage 1's allocation; the owner confirms or revises them at the contract/allocation walkthrough before Stage 2. No provider calls are authorized now.
Track active sessions from Stage 1, including preparation, review and model-run waits; exclude recorded periods awaiting owner input.
Keep model latency inside the ceiling to bound actual study time and expose tooling costs. Budget for sequential execution initially, then replace estimates with pilot timings; do not assume all available calls must be used.
Stage 1's allocation table must fit pilot, baseline, comparison, calibration and development within these separate pools before Stage 2 chooses cases and repetitions.
Protect the comparison allocation: evaluation repairs cannot consume subject/authoring capacity, and every retry uses the retry pool. No automatic transfers or extensions are allowed.
At either limit, stop collection and close with the supported decision or uncertainty. Inspect which framework steps consumed effort and remove or combine steps that did not support the decision before proposing further work; do not silently extend the limit or weaken correctness criteria.

Keep reserved cases, reference answers and revealing results in `../skill-study-private/sweeping-stale-references/`, with verified copies in `../skill-study-backups/sweeping-stale-references/`, outside this repository and its Git history.
Stage 1 records both absolute paths resolved from the canonical project checkout, not a worktree's working directory. These local copies protect against loss of a working copy, not loss of the host.
Record their identities and storage references in an evaluator-only index; give the author only the development protocol and permitted evidence.
A fresh author must use an isolated input workspace with filesystem/tool permissions that prevent reading either private copy or the evaluator's checkout; verify those restrictions before claiming unexposed transfer evidence.
A different directory or branch alone is insufficient. If isolation cannot be established within the budget, classify affected cases as development evidence and disclose the limit.

## Stage 1: agree on the skill and its contract

- [x] Recommend `sweeping-stale-references` as the first candidate: fixtures can expose required changes, intentional historical references and unrelated matches with checkable expected outcomes.
- [x] Record the owner-selected candidate, study start and active-time accounting, and open its protocol. Keep limits provisional until the allocation is reviewed.
- [x] Read the complete skill, relevant dependencies and installed `writing-skills` testing guidance; record versions and missing capabilities before dependent work.
- [ ] Derive intended behavior, exclusions, ownership and observable evidence from those sources. Review the contract and unresolved interpretations with the owner.
  All nine skills have been read and their purpose/relationships recorded in the architecture map. The owner agreed with the broad purpose, clarified path-move reconciliation and code-to-documentation drift, and directed independent evaluation. The protocol now specifies skill-only versus no skill guidance; detailed procedural interpretations and execution qualification remain open.
- [x] Write the phase-by-role allocation table, with feasible case/repetition assumptions, evaluator batch composition, estimated preparation/run/review time, protected comparison capacity and repair reserves. Declare whether the affordable repetitions support a variability estimate or only descriptive observations; otherwise report variability as not estimable.
- [x] Inspect the runner paths needed for this candidate. Distinguish code/document inspection from live qualification.
- [ ] Identify a feasible model-evaluator mechanism satisfying the no-write-tool rule before Stage 2 selects model-assessed criteria. Inspect existing options first; record a concrete alternative or narrower scope for owner decision if none fits. Stage 3 verifies actual permissions and evidence integrity before evaluator dispatch.
- [ ] Walk through the proposed contract, control context and feasible allocation with the owner; confirm the limits before designing tests.

**Complete when:** the protocol identifies the exact original, agreed contract, feasible allocation, absolute storage paths and capabilities requiring pilot verification.
The candidate and independent-use direction are settled; do not reopen them as prerequisites for the remaining walkthrough.
Batch evaluator inputs across distinct cases, never across conditions of the same case in one evaluator context, and use fresh contexts for later batches. Conceal condition labels and identifying metadata in evaluator copies while preserving raw evidence separately; content may still reveal the condition, so record that residual limit and its effect on claims before collection.
The evaluator pool need not cover every subject run with a separate call: allocate model judgments only where used or measured, and independently validate deterministic checks for the other properties.

## Stage 2: define representative tests and assessment

- [ ] Prepare cases covering reconciliation, preservation and accounting within Stage 1's allocation; one case may exercise multiple properties. Map each assessed property to the contract and evidence.
  Initial contribution cases present the trigger without directing the sweep or enumerating consumers; an explicit sweep request tests a separately identified execution question. Preserve clear task scope and permission to fix related files.
- [ ] Define source-supported expected outcomes, valid alternatives and failure/insufficient-evidence boundaries. Counting replacements alone does not establish correct triage or preservation.
- [ ] Designate development and reserved cases before calibration or pilot exposure. Keep reference answers out of subject inputs and model-evaluator inputs when testing evaluator accuracy.
- [ ] Select deterministic checks for properties they fully establish, and model judgments for the remaining questions. Have the model assess known outcomes and compare its reasoning and verdicts with independently checked references.

**Complete when:** every selected criterion has an observable basis, the checks preserve valid alternatives, and coverage gaps and information boundaries are explicit.
Follow the spec's proportional evaluation rule; do not add model calibration for a judgment the study never uses.

## Stage 3: qualify and freeze execution

- [ ] Write exact configurations, input identities, provider/model/effort, commands, working directories, permissions, evidence checks and call allocation in the protocol before proposing dispatch.
- [ ] Record authorization for the concrete pilot and evaluation calls; use existing authorization when it already covers them.
- [ ] Verify deterministic checkers on known correct and incorrect artifacts. For model judgments actually used, declare reference distinctions, repeats and allowed disagreement before calibration; repair unresolved decision-changing errors or reduce the evaluated scope explicitly.
- [ ] Pilot task feasibility, context isolation, skill availability, evidence capture and preservation. Keep infrastructure failures distinct from behavioral failures, and account for every attempt.
- [ ] Inspect and measure the first complete pilot bundle before committing raw evidence; record the retention decision under the evidence rules below. Use measured latency to update the allocation within the existing ceiling. Consider bounded concurrent dispatch only if timing demonstrates a need and isolation, run ordering and preservation barriers can be maintained; record the mechanism before use.
- [ ] Use pilot findings to freeze tasks, criteria, model/evaluator settings, repetitions, run order, retry/stopping rules and acceptance boundaries. Confirm that recorded authorization covers the baseline and later comparison allocation.

**Complete when:** mechanical paths and the evaluation procedure pass their declared checks and the measured collection has concrete authorization within the whole-study ceiling.
For every conditional safeguard, record its implementation or its evidence limitation and effect on the claim before collection.

## Stage 4: establish the baseline

- [ ] Run the original-skill and no-target-skill conditions under the frozen protocol, recording which companions and surrounding instructions remain in the control.
- [ ] Assess raw evidence with the declared checks and fresh model contexts. Conceal condition labels using the mechanism established in Stage 3, or apply its recorded limitation.
- [ ] Report per-case outcomes, evaluator accuracy, costs and observed variation; apply Stage 1's declared limit on variability estimation. Inspect evidence supporting passes as well as failures.
- [ ] Resolve defective tests or criteria through a versioned amendment applied consistently across affected conditions; preserve prior records and recollect only where necessary and authorized.
- [ ] Present supported rewrite opportunities and agree on an objective, or proceed to closure retaining the original.

**Complete when:** conclusions trace to retained evidence and distinguish observed success, attributed skill contribution, evaluator error and uncertainty.
A successful no-skill control is useful evidence, not a reason to invent a failure.

## Stage 5: rewrite and compare

- [ ] Re-read `writing-skills` and reconcile its evidence requirements with the agreed edit before authoring. Resolve a passing-control/RED conflict explicitly; preserve the intended behavioral contract.
- [ ] Give a fresh author only permitted development inputs. Use bounded development checks and preserve each candidate version and the original.
- [ ] Fix the selected candidate before exposing reserved results to its author. Compare it with contemporaneous original-skill runs; include a current no-target control when claiming benefit over unguided behavior.
- [ ] Investigate material model/runtime drift before attributing improvement. If reserved results guide an edit, reclassify them as development evidence; renewed transfer claims require new reserved cases on both versions within remaining authorization.

**Complete when:** the comparison answers the declared acceptance question or identifies exactly why it cannot. Report regressions and limitations alongside gains; do not hide them in aggregate scores.

## Stage 6: decide and close

- [ ] Recommend adoption, retention or an inconclusive result, citing the comparison and actual effort. Obtain the owner's adoption decision before rollout.
- [ ] Record which framework steps helped the decision and which should be removed, combined or changed. Close the study explicitly, including any unperformed rewrite or exhausted limit.
- [ ] Propose a contrasting second skill only after closure, using what the first study demonstrated. General templates and new tools require evidence of recurring need.

**Complete when:** the decision, supporting evidence, limits and next recommendation are recorded. An inconclusive result does not automatically authorize another cycle.

## Evidence and version control

After every invocation stops writing, copy the entire bundle to durable study storage, verify file identities and index its original/preserved locations before the next dispatch.
Keep reserved bundles in the private store; verify each backup against the primary's file/hash inventory before the next dispatch. Record successful verification and both absolute locations in the private index.
Preserve raw contents and historical absolute paths; the index resolves their new locations.
Stop dispatch if preservation fails. Retain unsuccessful attempts; a runner completion status is not a behavioral pass.
The run index accounts for case, condition, repetition, attempts, configuration identity, authorization and remaining call budget, so a later agent can resume without duplication.
Preserve complete bundles, including inputs, workspace state, stdout/stderr, final output, logs and result metadata; use file inventories as the completeness check.
Commit the reset and reviewed protocol before measured collection. Preserve the first pilot bundle outside Git, inspect its contents and byte size, and estimate whole-study storage before deciding what belongs in repository history; raw provider streams can be large and cannot be removed from history by an ordinary deletion.
Record the retention decision before the first evidence commit and measured collection, following CLAUDE.md's never-commit rules for transcripts and scratch notes. At stage boundaries, commit reviewed development artifacts and a manifest of the complete retained evidence. Any raw evidence kept outside Git requires recorded absolute primary/backup paths and verified file/hash copies before the next dispatch; do not describe a manifest-only checkout as containing the raw evidence.
Reserved bundles and revealing assessments stay entirely in the verified private stores, never in public Git history. Do not add a tool unless a demonstrated mechanical need justifies its interface and focused tests.

## Current next action

Walk through the remaining procedural interpretations and provisional limits in the study protocol with the owner before designing cases. Source inventory, allocation arithmetic and runner inspection are prepared; detailed contract/limit acceptance remains open.
Resolve evaluator feasibility during this preparation; a separate workspace is not evidence that the current write-capable adapters meet the no-write-tool rule.
The first study evaluates sweeping-stale-references alone against the same task without skill guidance; the earlier DD-present control is superseded. Exact input isolation remains a pilot requirement.
The owner selected Sol low for initial process checks (Terra medium is an alternative); the protocol keeps the five-repetition wording campaign conditional on reaching authoring, outside the initial pilot.
The reset documents and abandonment notices are prepared; experimental stages remain incomplete.
