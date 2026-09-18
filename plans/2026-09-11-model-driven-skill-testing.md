# Model-driven skill testing: first complete study

> **For agentic workers:** Use `superpowers:executing-plans` for authorized work. This document alone owns the execution checklist.

**Goal:** Reach an evidence-backed decision about improving one DD skill, then use the experience to refine the general testing approach.
**Architecture:** The active Codex/Claude session runs fixed scenarios, waits for the existing harness to capture evidence, applies versioned rules, records detailed execution results and assesses the aggregate batch. A human can use the same rules. Separate evaluator calls and calibration are not required.
**Tech stack:** Checked-in Markdown skills, the Python `skilltest` runner, files and Git.
**Spec:** [General testing responsibilities](specs/2026-09-11-model-driven-skill-testing-framework.md).

**Authority and state:** This is the current plan for executing the study; it replaces the previous nine-task plan and its separate six-stage proposal.
Preparation and documentation work are authorized. Candidate selection, provider spending, a rewrite objective and adoption require the owner decisions identified below. Pre-baseline development is closed after two completed pairs. The owner authorized baseline design and then the collection scopes recorded below; no new skill authoring was needed: the owner-selected existing rewrite has now been compared under fixed rules.
The spec governs how the study is designed. Neither document grants provider-run authorization.
External reviews and responses are recorded in the [review record](../reviews/2026-09-11-model-driven-testing-plan-review.md). Claude passed the committed preparation at `314b72e`; public-source attribution limits and the development exit were then documented. Pre-baseline development is closed; current authority and progress are recorded below.
On 2026-09-12 the owner selected `sweeping-stale-references`, settled the contract and accepted the outer ceilings while directing minimal initial real-model runs to establish the process. Stage 1 and conceptual coverage review are complete. The first SSR study is closed with both historical pilot pairs, the semantic-delivery pair, the core baseline and the comprehensive comparison assessed. The owner deferred adoption until later experiments; the owner selected concise-writing as the contrasting second skill. Its [draft protocol](../skill-studies/concise-writing/protocol.md) owns the accepted intent, assessment-policy direction and developing case definitions.

## Starting or resuming without conversation history

Use the [fresh-session handoff](../skill-studies/sweeping-stale-references/HANDOFF.md) for the current reading route and evidence map; this plan remains the checklist authority.

Read [CLAUDE.md](../CLAUDE.md), this plan and the spec; inspect the working tree and existing worktrees before editing.
Preserve unrelated changes and identify original skill bytes by revision and hash.
Use the [runner guide](../skill-validation/runner/README.md) for mechanics; its fixed worksheet and historical methodology links do not govern this study.
Read installed workflow skills from the available catalog rather than relying on a previous installation path.
Read the [purpose and relationship map](../ARCHITECTURE.md#composition-boundaries) for orientation; distinguish independent use, explicit pairings and DD orchestration before deciding subject context.

The study workspace is `skill-studies/sweeping-stale-references/`.
Its primary skill-specific narrative document is [protocol.md](../skill-studies/sweeping-stale-references/protocol.md): it holds concrete decisions, versions, commands, artifact links, run accounting and the final conclusion, without another task checklist.
Fixtures, checkers, raw bundles and assessments are supporting artifacts linked from that record.
This plan owns progress; the spec owns general rules; the protocol owns study-specific facts and decisions.
On resumption, use recorded decisions and evidence to select the next incomplete action; do not repeat settled approvals or infer authorization from a checked box.

Historical material stays in place with its abandonment notices.
The [preservation record](../skill-validation/archive/local-cw-scoring-rebuild-2026-09-11/README.md) indexes a verified local snapshot of `/private/tmp/cw-scoring-rebuild-gep1e4ek/` and the eight archived CW-17/CW-18 inputs; the scratch payload stays outside Git, while the inputs and manifest are versioned.
A broader archival reorganization is outside this study.

## Limits and information boundaries

**Accepted outer limits: 40 subject, 12 evaluator, 4 authoring and 4 retry invocations (60 total), plus 20 hours of active study work.**
These are ceilings, not a dispatch commitment. The owner requested minimal real-model runs to establish the process before broader testing; the initial Sol-low pair and its two-call extension are complete. Pre-baseline development is now closed at four subject calls; its remaining additional-development slot stays unused. A new facet alone cannot reopen that phase. A diagnostic exception requires a named readiness defect and separate owner approval; no automatic full campaign follows.
Track active sessions from Stage 1, including preparation, review and model-run waits; exclude recorded periods awaiting owner input.
Keep model latency inside the ceiling to bound actual study time and expose tooling costs. Budget for sequential execution initially, then replace estimates with pilot timings; do not assume all available calls must be used.
The old phase table is superseded as an execution plan. Select only the calls needed for the next session test/comparison; active-session assessment consumes session effort, not a separately dispatched evaluator invocation. Unused evaluator/authoring pools are not automatically transferred.
Protect the comparison allocation: evaluation repairs cannot consume subject/authoring capacity, and every retry uses the retry pool. No automatic transfers or extensions are allowed.
At either limit, stop collection and close with the supported decision or uncertainty. Inspect which framework steps consumed effort and remove or combine steps that did not support the decision before proposing further work; do not silently extend the limit or weaken correctness criteria.

Only for an explicitly selected held-out transfer claim, keep reserved cases, reference answers and revealing results in `../skill-study-private/sweeping-stale-references/`, outside this repository and its Git history.
Record the absolute storage path resolved from the canonical project checkout and any ordinary backup arrangement; a second study-managed copy is not required.
Record private storage identities for that optional claim; ordinary in-session assessment uses the retained evidence and known rules directly.
For that held-out claim, an unexposed author must use an isolated input workspace with filesystem/tool permissions that prevent reading private evidence, any accessible backups or the evaluator's checkout; verify those restrictions before claiming unexposed transfer evidence.
A different directory or branch alone is insufficient. If isolation cannot be established within the budget, classify affected cases as development evidence and disclose the limit.

## Stage 1: agree on the skill and its contract

- [x] Recommend `sweeping-stale-references` as the first candidate: fixtures can expose required changes, intentional historical references and unrelated matches with checkable expected outcomes.
- [x] Record the owner-selected candidate, study start and active-time accounting, and open its protocol. Keep limits provisional until the allocation is reviewed.
- [x] Read the complete skill, relevant dependencies and installed `writing-skills` testing guidance; record versions and missing capabilities before dependent work.
- [x] Derive intended behavior, exclusions, ownership and observable evidence from those sources. Review the contract and unresolved interpretations with the owner.
  Record the spec's required consumer check in the protocol: known output consumers, their dependencies and the consequences of inconsistent output; carry these into assessment severity.
  All nine skills have been read and their purpose/relationships recorded in the architecture map. The owner agreed with the broad purpose, clarified path-move reconciliation and code-to-documentation drift, directed independent evaluation, and accepted that single-file/no-sweep requires checking scope. Functional outcomes and procedural/mechanical effectiveness are scored separately; outcome failures are hard failures. Within the owner's discretion for this skill, the protocol treats purely procedural failures as visible, non-blocking defects. Limits are accepted as outer ceilings; execution qualification follows in Stage 3.
- [x] Agree the outer call/time ceilings and scope limits. Select and estimate each batch within those limits; declare whether its repetitions support a variability estimate or only descriptive observations.
- [x] Inspect the runner paths needed for this candidate. Distinguish code/document inspection from live qualification.
- [x] Implement and probe read-only execution as an optional runner capability. This completed work does not require separate evaluators or calibration in the session workflow.
- [x] Walk through the proposed contract, control context and feasible allocation with the owner; confirm the limits before designing tests.

**Complete when:** the protocol identifies the exact original, agreed contract, feasible allocation, absolute storage paths and capabilities requiring pilot verification.
The candidate and independent-use direction are settled; do not reopen them as prerequisites for the remaining walkthrough.
The active agent scores under the fixed rules by default. The earlier fresh-evaluator/batching requirement is superseded by the owner's reaffirmed session workflow; the general spec owns that rule.

## Stage 2: define representative tests and assessment

- [x] Review the protocol's proposed facets and observation methods with the owner before choosing scenarios.
- [x] After conceptual coverage is agreed, inspect prior scenarios for fit. Reuse/adapt a suitable scenario under the current contract; create a new one where no good fit exists. Do not inherit old scores or methodology.
  Inspected the six existing SSR prompts and their fixture shapes. Adapt ssr-02's reviewer-triggered config rename into an executable repository for the process pilot; the old supplied inventory, rubric and accepted results are not subject inputs or scoring authority.
- [x] Prepare cases covering reconciliation, preservation and accounting for the selected run scope within the outer limits; one case may exercise multiple properties. Map each assessed property to the contract and evidence.
  Pilot 01 is complete. Pilot 02 has completed the new moved-guide pair: original repaired and committed all four consumers; control only README. Both preserved protected material. See its [report](../skill-studies/sweeping-stale-references/pilot-02-results.md). Core committed reconciliation takes priority; semantic drift is required in baseline design, while justified-local-change coverage is deferred. Discovery comparisons are diagnostic, not a requirement to outperform the control.
  The vendor-heavy synthetic `cases/pilot-03/` draft is preserved and undispatched. Its mechanical checks did not establish discovery adequacy.
  The approved replacement [Shiv case](../skill-studies/sweeping-stale-references/cases/discovery-shiv/assessment.md) is locally prepared: 50 project files excluding the runtime, four executable stale consumers, standalone original/control inputs, fixed outcome/accounting criteria, four CLI tests and fourteen controller tests. Real loader/copy and isolated-runtime checks require no providers. Source adaptations, qualification and file identities are retained in the case package. Its primary value is checking complete reconciliation across real consumers; discovery difficulty is unmeasured and does not gate collection. Case preparation itself grants no provider authorization; the protocol records the completed core-baseline collection.
  The [semantic delivery case](../skill-studies/sweeping-stale-references/cases/semantic-delivery/assessment.md) is now locally prepared: nine project files, three stale current statements, historical/independent preservation, seven behavior tests, twelve controller tests and nine reconstructed reference variants. Both runner configurations copy correctly; the active agent assesses documentation meaning using the fixed rules and evidence.
  Initial contribution cases present the trigger without directing the sweep or enumerating consumers; an explicit sweep request tests a separately identified execution question. Preserve clear task scope and permission to fix related files.
  Include at least one case with a plausible functional miss beyond the triggering reference, including latent consumers in config, CI or fixtures. This supplies an opportunity to observe scope expansion, not a requirement that the control fail.
- [x] Define source-supported expected outcomes, valid alternatives and failure/insufficient-evidence boundaries. Counting replacements alone does not establish correct triage or preservation.
  Subsequent SSR cases must map criteria to the [current assessment policy](../skill-studies/sweeping-stale-references/protocol.md#current-ssr-assessment-policy): committed functional completeness leads; detailed accounting remains secondary and non-blocking.
  Pilot-specific setup, functional and procedural criteria are recorded in its assessment artifact. The [execution-result schema and batch-assessment template](../skill-studies/formats/README.md) express the agreed outcome and aggregate responsibilities; the retained historical example illustrates evidence-backed reasoning. The owner accepted the reconciled layouts; current formats are version 1.
  Map criteria to functional outcomes or procedure/mechanics, recording any overlap and the agreed failure consequence. Expose both dimensions in assessments; do not let format success offset an outcome failure or hide non-blocking procedural defects.
- [x] Select active suite membership and keep scoring rules/reference examples out of subject inputs. Designate reserved cases only for an explicitly chosen held-out claim.
- [x] Map mechanical facts to deterministic checks and semantic questions to written rules applied by the active agent or human. Use worked examples only where needed to clarify those rules; no separate calibration campaign.
- [x] At the end of baseline design, agree with the owner on a versioned protocol template before freezing collection. Fix section names/order, required fields, optional sections with applicability rules, artifact links, and how decisions or amendments are recorded. Apply version 1 to SSR and use it for subsequent skills; later changes require an explicit template version rather than ad hoc structural drift.
- [x] At that checkpoint, agree on the companion case/criteria, run-index, manifest, execution-result/batch-assessment and layout/lifecycle contracts described in the spec. Check the runner's configuration/result interfaces and version any required changes; keep skill-specific expectations and semantic judgments outside structural conformance rules.
- [x] Reconcile actual time and the total remaining forecast, including tooling, against remaining authorized time before freezing collection. Apply the spec’s effort policy and present any forecast extension need at the owner walkthrough.

Selected scope is complete for semantic-delivery, moved-guide and discovery-shiv. Justified-local-change coverage remains explicitly deferred; no held-out claim was selected. The fixed definitions/manifests and completed batch assessment provide the criterion-to-evidence mapping.

**Complete when:** every selected criterion has an observable basis, the checks preserve valid alternatives, and coverage gaps and information boundaries are explicit.
Follow the spec’s session workflow; separate evaluator qualification is not a stage gate.
Separate process qualification from suite construction: prepare one non-reserved pilot case and its required checks first, then exercise Stage 3 on that subset before expanding the suite. Keep unbuilt coverage and unchecked assessment work visible; a successful process pilot does not complete Stage 2 or establish a baseline.

## Stage 3: qualify and freeze execution

Qualification and freeze are complete for the selected three-case baseline. The [batch assessment](../skill-studies/sweeping-stale-references/core-baseline-01-assessment.md) traces fixed inputs, permissions, capture/runtime amendments, all attempts and the two setup exclusions. Historical pilot qualification remains in its linked reports; it is not authorization for another pilot. Evidence establishes observed guidance boundaries and complete skill reads where included, not exhaustive host-wide isolation or held-out validation.

- [x] Write exact configurations, input identities, provider/model/effort, commands, working directories, permissions, evidence checks and call allocation in the protocol before proposing dispatch.
- [x] Record authorization for the concrete subject calls and any separately selected evaluation calls; use existing authorization when it already covers them.
- [x] Verify deterministic checkers on known correct and incorrect artifacts. Confirm that the active agent can locate each required fact, apply the rules and write an execution result and reconcile it into the declared batch assessment; use existing retained evidence for this format check rather than inventing another model-run gate.
  Include the current policy and case criteria in assessment inputs and record exact identities. They are not subject inputs. Resolve genuine criterion ambiguity with the owner; do not repeatedly seek approval for settled scoring rules.
- [x] Pilot task feasibility, context isolation, skill availability, evidence capture and preservation. Keep infrastructure failures distinct from behavioral failures, and account for every attempt.
- [x] Inspect and measure the first complete pilot bundle before committing raw evidence; record the retention decision under the evidence rules below. Use measured latency to update the allocation within the existing ceiling. Consider bounded concurrent dispatch only if timing demonstrates a need and isolation, run ordering and preservation barriers can be maintained; record the mechanism before use.
- [x] Use pilot findings to freeze tasks, criteria, subject settings, score format, repetitions, run order, retry/stopping rules and acceptance boundaries. Confirm that recorded authorization covers the actual batch being dispatched; forecast and protect later comparison capacity without requiring approval of an unselected future campaign.

**Complete when:** mechanical paths and the evaluation procedure pass their declared checks and the measured collection has concrete authorization within the whole-study ceiling.
For every conditional safeguard, record its implementation or its evidence limitation and effect on the claim before collection.

## Stage 4: establish the baseline

- [x] Run the original-skill and no-target-skill conditions under the frozen protocol, recording which companions and surrounding instructions remain in the control.
- [x] In the active session, inspect raw evidence and check results, apply the fixed rules, and write/index one canonical execution result per assessed execution. Record assessor context and inspect passes as well as failures; no fresh scoring context is required.
- [x] Complete one batch assessment with per-case/condition/criterion aggregates, evidence limitations, failure patterns and observed variation. Reconcile planned repetitions and all attempts, apply the declared inclusion/retry/acceptance rules, and cite accounting where relevant. Inspect evidence supporting passes as well as failures; apply the declared limit on reliability claims.
- [x] Resolve defective tests or criteria through a versioned amendment applied consistently across affected conditions; preserve prior records and recollect only where necessary and authorized.
  Capture-2 and runtime-1 address observed infrastructure faults prospectively; both affected attempts remain charged and excluded, with no replacements. Criteria and subject inputs did not change.
- [x] Present supported rewrite opportunities and agree on an objective: owner approved the existing comprehensive candidate for complete-repair preservation and reporting accuracy on 2026-09-17.
  The batch assessment's interpretation correction distinguishes clear counting errors from the unresolved Shiv negative-assertion category boundary. Resolve that skill/criterion attribution before treating it as a rewrite target; the recorded fixed-rule judgments remain unchanged.

**Complete when:** conclusions trace to retained evidence and distinguish observed success, attributed skill contribution, evaluator error and uncertainty.
A successful no-skill control is useful evidence, not a reason to invent a failure. The selected SSR original/control baseline is collected; routine later edit checks need only the conditions relevant to their question.

## Document tooling: after baseline collection

This work follows format agreement and baseline assessment; it is not a Stage 2/3 completion or collection-freeze requirement. The reusable document commands now cover SSR’s mechanical checks; semantic review remains with the active session. This avoids delaying first measurement for general conformance automation while preserving the owner's requested tool deliverable. Its scope and CLI must be agreed before implementation, with an explicit effort estimate and attention to the overall authorization ceiling.
The [concrete tooling proposal](specs/2026-09-16-study-document-tooling.md) records the owner-accepted simplifications: protocol-only whole-study entry, ordinary shared definitions and parsing limited to agreed structures. The owner approved implementation and its provisional allowance on 2026-09-16; the implemented commands have been exercised on actual SSR structures and disposable invalid variants.
It also records the document-module boundary, full-revision runner identity and future execution checks; historical batch identity claims remain unchanged.

- [x] After baseline collection and assessment, agree an effort estimate and implementation scope, then design and implement the owner-requested document generator/validator against shared versioned definitions. Generate drafts without overwriting files; validate existing documents read-only with actionable diagnostics and distinct structural/readiness results. Verify cross-document identities and valid/invalid examples, then apply the tool to current study documents without rewriting frozen evidence. Agree on the CLI and implementation scope before coding.
  Treat the inspected `skilltest worksheet` and its tests as evidence of the recurring pattern, not a required basis. Choose reuse, adaptation, replacement or retirement against the agreed deterministic-tool requirements. Update scoring/assessment tooling and formats as needed without inheriting the abandoned methodology or silently rewriting historical evidence.

### Approved implementation steps

Continue in the existing study checkout and branch named in the handoff; preserve the pending documentation changes. Execute sequentially with test-first changes, using `superpowers:executing-plans` and `test-driven-development`. This plan owns progress; the tooling spec owns requirements. Review the completed tool as one bounded change on this branch.

Files: add `skill-validation/runner/src/skilltest/documents/` for shared formats, document validation, reference resolution and batch reconciliation; extend `cli.py`, `pyproject.toml` and its lock for the CLI/runtime dependency and packaged format resources. Keep the canonical templates/schema in `skill-studies/formats/`, package those bytes without independent copies, and add `skill-validation/runner/tests/test_documents.py`. Update runner/formats guides and study status at completion.

- [x] **Drafts and structural checks.** Inspect actual SSR headings, cards, scope and aggregate tables; use their accepted representations. Write failing CLI tests for six draft kinds, no overwrite, required fields/sections, enum/type/duplicate-ID errors, unknown versions, JSON diagnostics and exit status. Implement shared template/schema definitions and read-only checks; generated drafts pass structure but expose incomplete values. Verify the installed command can find its packaged definitions outside this checkout.
- [x] **Identities and execution records.** Test real temporary Git repositories and retained evidence references: changed working files with valid historical pins, wrong/missing hashes/revisions, exact configured sources, controller overlap, applicable criterion coverage, evidence IDs, setup separation, inventories and result/index identity. Reuse the config loader against disposable materialized pinned inputs. All Git reads are bounded and argument-based; missing/malformed identities fail clearly without executing document commands or repairing evidence.
- [x] **Batch checks and qualification.** Test protocol-only readiness, ambiguous batch selection, declared order/repetitions, missing/unusable/retried attempts, charges, coverage, outcome aggregates and runtime strata. Reconcile existing explicit scope tables and supported aggregate layouts; unsupported scope/inclusion/strata representations return an explicit incomplete-check diagnostic, never success. Apply the real CLI to SSR and invalid disposable variants, verify no source writes/provider calls, run runner/formats/hooks suites, review against the spec and update guides/status/accounting. Check the existing worksheet callers/docs before proposing any separate retirement.

Qualification: the offline runner suite passes (367 tests, including 56 document tests), format tests pass (9), and hooks pass (263, with 3 environment skips). A wheel installed outside the checkout generates all six drafts, refuses overwrites and checks both SSR batch assessments, current manifests/index and protocol readiness. Invalid fixtures cover identities, evidence, coverage, aggregates, accounting and malformed inputs, including corrupt result, inventory and authorization references in the current index while the assessment’s frozen index remains valid. Historical inputs/results remain unchanged; the active-session review does not claim independent validation.

Absent or unreadable files, invalid UTF-8/JSON, unsupported versions/layouts and unresolved placeholders must yield located diagnostics and the declared failure status. Arrays and input graphs are traversed without assuming one case, one condition or one attempt; duplicate and cyclic identities cannot silently pass or recurse indefinitely. No semantic interpretation, automatic history migration or extra metadata record is introduced.

## Stage 5: rewrite and compare

- [x] Resolve the authoring step: reuse the owner-selected existing candidate exactly; no new authoring, wording loop or manufactured RED test is required. Any later edit must re-read `writing-skills` and reconcile its evidence requirements.
- [x] Preserve the selected candidate and original separately. The approved candidate is the exact committed comprehensive rewrite; no held-out or unexposed-author claim is selected.
  Original conditions use `skill-studies/sweeping-stale-references/cases/skill-original/SKILL.md`, including later contemporaneous runs. Never point them at the mutable live skill; keep candidate sources distinct.
- [x] Run the relevant fixed scenarios after the edit and record execution results and compare aggregate assessments. Use contemporaneous original runs for a version-comparison claim and a current no-target control for a contribution claim. Apply reserved-result restrictions only when that claim was selected.
- [x] Investigate material model/runtime drift before attributing improvement. If reserved results guide an edit, reclassify them as development evidence; renewed transfer claims require new reserved cases on both versions within remaining authorization.

The [comparison assessment](../skill-studies/sweeping-stale-references/comprehensive-comparison-01-assessment.md) records all twelve valid executions under one frozen runner/runtime: functional preservation in both repetitions per case/version and mixed reporting differences. No material runtime change was observed; original functional outcomes remain consistent with baseline, while reporting varies. The whole-version comparison does not demonstrate an overall reporting improvement, and the known accounting interpretation limits remain explicit.

**Complete when:** the comparison answers the declared acceptance question or identifies exactly why it cannot. Report regressions and limitations alongside gains; do not hide them in aggregate scores.

## Stage 6: decide and close

- [x] Record the evidence-backed recommendation and owner disposition. The owner deferred adoption while further studies proceed; no rollout follows.
- [x] Record process lessons and limits in the protocol’s Results and decision section. Close SSR with adoption deferred, all selected collection complete, and unused capacity unspent.
- [x] Propose a contrasting second skill after closure: the owner selected concise-writing. Reuse the existing formats and tools; its accepted intent and next preparation steps are linked under Current next action.

**Complete when:** the findings, owner disposition (including deferred adoption), limits and next recommendation are recorded. Closure or unused capacity does not automatically authorize another cycle.

## Evidence and version control

After every invocation stops writing, retain one complete bundle in durable study storage, verify it against one inventory and record its location before the next dispatch.
Use ordinary backup arrangements for recovery; a second study-managed copy and per-run backup verification are not required. Record the actual backup arrangement or its unverified status; existing historical copies stay in place.
Preserve raw contents and historical absolute paths; the index resolves their new locations.
Stop dispatch if preservation fails. Retain unsuccessful attempts; a runner completion status is not a behavioral pass.
Keep the run index to attempt/case/condition identity, input-manifest and authorization references, call charge, bundle location/verification and the canonical execution-result link. Read execution settings, status and timing from the runner artifacts; derive remaining capacity from distinct attempts and protocol ceilings.
Preserve complete bundles, including inputs, workspace state, stdout/stderr, final output, logs and result metadata; use file inventories as the completeness check.
Commit the reset and reviewed protocol before measured collection. Preserve the first pilot bundle outside Git, inspect its contents and byte size, and estimate whole-study storage before deciding what belongs in repository history; raw provider streams can be large and cannot be removed from history by an ordinary deletion.
Record the retention decision before the first evidence commit and measured collection, following CLAUDE.md's never-commit rules for transcripts and scratch notes. At stage boundaries, commit reviewed development artifacts and the evidence inventory/reference. Raw evidence outside Git requires a recorded absolute durable location and verified inventory before the next dispatch; do not describe a manifest-only checkout as containing the raw evidence.
Reserved bundles and revealing assessments stay entirely in the verified private stores, never in public Git history. Do not add a tool unless a demonstrated mechanical need justifies its interface and focused tests.

## Current next action

- [x] Reconcile document responsibilities to the agreed spec and review whole-set conformance.
- [x] Record owner acceptance of the formats and publish version 1.
- [x] Apply the accepted case/manifest layouts to both unrun cases, preserving subject inputs, policy and historical evidence.
- [x] Verify criterion coverage, source membership, Git retrieval and schema behavior; prepare exact commands and a remaining-work forecast.
- [x] Obtain approval for the protocol's `semantic-delivery-01` scope/commands: original then control, Sol-low, one execution each, no retries.
- [x] Freeze accepted collection identities, collect only those two authorized attempts, preserve evidence and write execution results plus the [batch assessment](../skill-studies/sweeping-stale-references/semantic-delivery-01-assessment.md).
- [x] Review the first measured batch and select the next scope: owner approved three cases × original/control × two executions each (12 additional subject calls).
- [x] Prepare/freeze `core-baseline-01` inputs without changing historical inputs or settled criteria.
- [x] Collect and assess the twelve approved executions. The [batch assessment](../skill-studies/sweeping-stale-references/core-baseline-01-assessment.md) records ten valid observations and two setup exclusions, all retained without retries or replacements, with separate runtime strata.
- [x] Agree the reviewed generator/validator scope, CLI and provisional 120-minute implementation / 60-minute verification allowance. Owner approved proceeding on 2026-09-16.
- [x] Complete and qualify the document-tooling implementation steps above, without new model executions or skill edits.
- [x] Inspect and preserve the owner-suggested existing SSR rewrite, prepare matching candidate configurations and present the protocol’s twelve-execution comparison proposal. Preparation includes offline input-parity checks; no subject calls.
- [x] Owner approved `comprehensive-comparison-01` and its condition-applicability extension on 2026-09-17.
- [x] Freeze version-2 controller applicability and comparison manifests; collection readiness passed. The invocation-authority commit is also the full runner revision for this batch; record its hash in each actual attempt.
- [x] Collect and assess the twelve approved attempts in order, retaining each before the next dispatch, then write the aggregate comparison. No retry, replacement or skill edit occurred.
- [x] Present the completed comparison and recommendation; record the owner’s decision to defer adoption and close the first study.
- [x] Select concise-writing with the owner and preserve the current original.
- [x] Review the [CW intended outcomes and process-only policy](../skill-studies/concise-writing/protocol.md) with the owner: improve ease of consumption, preserve meaning and useful emphasis, allow restructuring, and judge document quality separately from procedural compliance. Consistency is assessed across repetitions; no numerical threshold is implied.
- [x] Prepare the proposed two CW cases: fictional source documents, tasks, contextual criterion cards and [constructed boundary examples](../skill-studies/concise-writing/qualification.md). Whole-document quality remains the judgment unit, including unchanged and partially edited saved files; the examples distinguish these from absent output and incomplete capture. These are active-session worked examples, not model observations or independent validation.
- [ ] Review the concrete CW cases and eight-call capacity proposal with the owner, then prepare configurations, manifests, setup/evidence checks, storage/recovery decision and exact collection commands before freeze and dispatch approval. The [CW protocol](../skill-studies/concise-writing/protocol.md) owns remaining-work accounting. No provider call or skill edit is authorized yet.

The owner accepted the reconciled [format set](../skill-studies/formats/README.md), now version `1`. The protocol and the Shiv and semantic-delivery case definitions/manifests use the accepted layouts; historical observed-case inputs and the `1-draft` worked example remain unchanged under their recorded identities.
The [semantic-delivery batch](../skill-studies/sweeping-stale-references/protocol.md#first-collection-semantic-delivery-01) is complete; its results informed the approved core-baseline-01 scope. No further layout review, new scenario, evaluator layer or pre-baseline pilot is needed.
Preserve SSR's agreed policy: complete/correct/preserved/committed outcomes lead; purely procedural defects are visible and non-blocking; insufficient evidence is not failure. Batch counts describe repetitions without relabelling execution failures or inventing an acceptance threshold.
The owner-authorized first semantic-delivery original/control pair is collected and assessed under the prepared Sol-low settings; both calls are spent; core-baseline-01 is separately authorized, with all twelve calls spent and assessed; no remaining call is authorized by that batch. Any larger baseline batch, repetitions and acceptance rule must be declared before its collection.
The protocol's [core-baseline-01 scope](../skill-studies/sweeping-stale-references/protocol.md#core-baseline-core-baseline-01) is complete, with no retries or skill edits. The protocol owns selected work, ceilings and accounting; old full-campaign tables are in Git, not a current run plan. The document generator/validator is implemented and qualified; the approved comprehensive comparison is complete, and SSR is closed with adoption deferred. Next is CW case preparation and review; no further calls or skill edits are authorized.
The owner wants to complete the studies and experiments before finalizing adoption. A Claude subject pass and selected effort-level benchmarks are desired follow-ups, but their skill coverage, model/settings, repetition counts, budget and order remain to be proposed. This direction does not select an all-skills or all-models campaign, and the first study’s unused capacity does not transfer automatically.
