# Fresh testing framework: plan and specification review

Status: historical internal reviews and responses to four owner-supplied external reviews.
Claude's latest reported verdict is BLOCK (round 4: one P2); the response below addresses its findings in the [current plan](../plans/2026-09-11-model-driven-skill-testing.md), without claiming external approval of these edits.
Earlier task numbers and layout descriptions below refer to the revisions reviewed at the time, not the current six-stage checklist.

Reviewed the [plan](../plans/2026-09-11-model-driven-skill-testing.md) and [specification](../plans/specs/2026-09-11-model-driven-skill-testing-framework.md) for consistency, executability, evidence quality and unnecessary prerequisites.
This was an in-session self-review, followed by a review of the corrections; it was not an independent evaluation or an empirical validation of the framework.
The scope included current tooling capabilities and skill instructions relevant to the proposed workflow.
Historical scenarios, rubrics and grades were not used as design authority.

## Initial review findings and resolutions

| Finding | Consequence | Resolution in both documents |
|---|---|---|
| P1: Reserved tests lacked a complete exposure rule. | Calibration, baseline reporting or the author's existing context could reveal tests later described as independent transfer evidence. | Reserve cases before calibration/pilot; use a fresh author context with declared inputs; exclude revealing results from the author's report; reclassify exposed cases as development evidence. Fix the candidate before revealing reserved results to its author. |
| P2: Calibration lacked a concrete readiness decision. | Repeated evaluator agreement could be mistaken for correct interpretation. | Establish source-supported reference judgments and a declared readiness rule before calibration. Unresolved consequential errors require repair and recalibration or an owner-agreed scope reduction. |
| P2: Rewrite comparisons did not explicitly control for model/runtime drift. | A difference between an old baseline and a later rewrite could be attributed to the skill without support. | Capture available versions, compare the original and candidate contemporaneously, and investigate material drift. Include a contemporary no-target control for claims of current benefit over unguided behavior. |
| P2: Task ordering could make full archival a prerequisite for fresh design. | Historical migration complexity could stall the first skill's contract and tests. | Establish the minimum workspace/archive boundary early and continue preservation alongside design; block only dependent actions or removal of unverified originals. |

The follow-up review checked that these rules agree across the specification and execution tasks, including the order of starting the fresh author context before authoring.
No unresolved actionable findings remained in this document review.

## Verification and limits

- Hook suite: `python3 -m pytest -q` in `skills/disciplined-development/hooks` — 263 passed, 3 skipped.
- Checked local document links and whitespace in the reviewed files.
- Checked that this work changed no skill bodies or runner files.

These checks support the document changes and repository integrity; they do not establish evaluator reliability or skill effectiveness.
Candidate choice, collection budget, repetition policy, calibration thresholds and rewrite acceptance boundaries remain explicitly assigned to the candidate study.
No provider experiment, archive migration or skill rewrite was performed by this review.

## Additional executability and consistency review

The owner requested another review focused on an implementer without conversation history.
This was an in-session walkthrough of the written handoffs, not a separately launched fresh-context agent or an implementation trial.

| Finding | Correction |
|---|---|
| P1: Active entry points still routed to the old charter, plan and record-update workflow. | Reconciled `CLAUDE.md`, `README.md` and `ARCHITECTURE.md`; added an explicit historical boundary to `skill-validation/README.md`. The plan distinguishes the runner's mechanics from its optional legacy worksheet conventions. |
| P2: Resumption depended on conversation knowledge of artifacts, decisions and temporary material. | Added starting/resuming instructions, decision and authorization provenance, links to evidence and the next authorized action, and the known scratch location for preservation. Kept author handoffs separate from reserved-case content. |
| P2: The pilot-to-baseline handoff did not explicitly require a runnable record. | Required exact inputs, commands, setup, evidence checks and case/condition/repetition-to-attempt mapping before dispatch. Reuse that record for baseline and comparison; prepare the concrete proposal before obtaining any additional authorization. |
| P2: `writing-skills` evidence requirements were first read at the authoring task. | Read them in Task 1 so they inform suite design; re-read and reconcile changes before rewriting. |

Walked the full dependency chain after the corrections:

| Handoff | Written path and completion boundary |
|---|---|
| Start → foundation | Current entry points lead to this plan/spec; Task 1 can begin with read-only inspection and ends with an owner-selected skill and identified sources. |
| Foundation → contract | Tasks 1 and 3 cover behavioral-contract layer 1; Task 2's archive migration proceeds alongside fresh design. |
| Contract → tests and evaluation | Task 4 covers layers 2 and 3 with two-way coverage, evidence requirements and early reserved-case separation. |
| Proposed tests → runnable study | Tasks 5 and 6 cover layer 4 with calibration readiness, qualified mechanics, concrete run records and bounded authorization. |
| Study → baseline | Tasks 6 and 7 cover layers 5 and 6 with retained attempts, frozen criteria, supported judgments and a permitted author report. |
| Baseline → rewrite and decision | Tasks 8 and 9 cover layer 7 with an agreed objective, appropriate author context, fixed candidate, contemporary controls and owner adoption decision. |
| First skill → reusable framework | Task 9 requires a contrasting second application before standardizing conventions or adding recurring mechanical tools. |

The consistency pass checked scope, terminology, task order, completion status, approval persistence, source identity, information boundaries and spec-to-plan coverage.
Candidate-dependent choices remain assigned to named tasks with prerequisites; they do not prevent starting the foundation inventory.
The corrected walkthrough left no unresolved actionable findings.
Fresh verification: hook suite — 263 passed, 3 skipped; current document links and whitespace checked; skill bodies and runner files unchanged.

## Abandoned testing-process reference cleanup

The owner clarified that prior testing frameworks and pending workflows are abandoned, with existing runner documentation and core skill documentation retained.
The reference sweep therefore covered project navigation, framework plans/specs, CW process reviews, validation-directory entry points and known continuation handoffs.

- Added explicit abandonment notices and current spec/plan links to 49 historical project documents: 39 plans/specs, three CW reviews, six validation entry documents and `scratch.md`.
- Marked both known temporary continuation handoffs so their former approvals cannot be mistaken for instructions to resume.
- Made the abandonment explicit in current project entry points and the fresh spec/plan; added a historical-results notice at `skill-validation/accepted/README.md`.
- Preserved historical bodies, status labels and references beneath the notices rather than rewriting the evidence of what happened.
- Left runner documentation, core skills, their implementation histories and raw test evidence unchanged; matches in those excluded documents do not activate an abandoned framework.

Verification checked all 49 original project-document bodies and both handoff bodies byte-for-byte after removing only the inserted notices, and confirmed the new notice links resolve.
The final consistency pass checked the current routes and the historical/current boundary; no unresolved actionable findings remained in this cleanup scope.
The hook suite passed with 263 passed and 3 skipped, and `git diff --check` passed.
Physical archive migration remains separate work; this change makes the retained locations unambiguous now.

## Response to Claude's second external review

The repeated failure was adding another execution structure while retaining the first.
The plan has been rewritten from 3,987 to 1,636 words with one six-stage checklist, one workspace and one next action; the nine tasks and overlaid proposal were removed.
`protocol.md` now holds study-specific facts, decisions and evidence links, without a second checklist.

The spec's calibration rule now distinguishes checked properties from model judgments actually used, and its status explicitly governs preparation while reserving execution authority to recorded owner decisions.
The plan proposes a 60-call, five-calendar-day outer limit, pending owner confirmation, and requires removing or combining unhelpful framework work when that limit is reached.
Reserved material belongs outside the main repository and its history, with access restrictions verified before transfer claims; a separate branch alone does not qualify.

The runner worksheet link remains unchanged under the owner's explicit instruction to leave runner documentation intact; the plan and abandoned target document state its historical status.
This is an accepted scope limit on the P3 finding, not a claim that the link was removed.
The documentation reset is being preserved separately from the old untracked test inputs; Git history is the evidence of its commit state.
The source-preservation and link checks passed, and the hook suite passed with 263 passed and 3 skipped.
External reviewer acceptance and owner confirmation of the candidate/limits remain open; the earlier internal PASS below is not their substitute.

## Response to Claude's third external review

The external review closes the structural objections. Its new resource and preservation concerns are addressed within the existing six stages.
Across the three rounds, no single correction would close all findings: the first identified missing safeguards, the second conflicting execution structures, and the third allocation timing and incomplete storage specifications. This pass fixes the resource/storage class without introducing another workflow.

The budget concern is accepted as a feasibility risk, not a demonstrated impossibility: three properties do not require three separate cases, the comparison's third condition is conditional, and observed differences can be reported without claiming a stable variability estimate.
Stage 1 now requires the allocation table before case selection. Proposed pools remain 60 total (40 subject, 12 evaluator, 4 authoring, 4 retry), with protected comparison capacity and no automatic transfers.
The proposed time limit is 20 active hours, excluding documented owner-response waits; candidate and budget approval remain pending.

Private primary and backup locations must be canonical absolute paths, and every backup must pass file/hash verification before dispatch continues. Both copies are excluded from author access.
Project navigation now names the planned study directory and private stores. The spec no longer duplicates candidate progress, and the plan explicitly preserves entire development bundles, including raw streams, while keeping reserved bundles out of repository history.
The temporary packet has a verified local snapshot with a versioned manifest; its scratch payload is excluded from Git. The eight abandoned v2 inputs are archived byte-for-byte for removal from the active paths after their archive commit is verified.
These are the implementation responses; external acceptance is still pending.

Historical internal verdict, preceding the fourth external review: **PASS**.

## Response to Claude's fourth external review — 2026-09-12

The owner supplied Claude's report that round 3 findings were closed and its independent verification matched all 54 preserved scratch files and eight archived inputs; this response does not claim to have repeated that verification.
Claude reported **DD-VERDICT: BLOCK** for one P2, with two P3 advisories, and recommended beginning Stage 1 rather than another general document review.

Across the four rounds, the findings concern missing safeguards, duplicate execution structures, resource/storage feasibility, and concrete batch/retention/latency choices. There is no single invariant whose correction closes all four sets; severity has declined as the execution structure was consolidated.
Claude describes round 4 as its cold read, although fresh-context isolation is not independently established here. Accept its recommendation to stop general document iteration and carry the remaining implementation checks into the existing stages; do not relabel its BLOCK as PASS or launch another review cycle.

| Finding | Disposition |
|---|---|
| P2: Evaluator batching can expose comparison conditions. | Stage 1 must specify batch composition: distinct cases, no different conditions of one case in a shared evaluator context, and fresh contexts between batches. Conceal labels/identifying metadata in evaluator copies; preserve originals separately and disclose content-based inference limits before collection. Twelve evaluator calls do not alone force batching because validated deterministic checks may establish some properties without model assessment. |
| P3: Complete bundles commit raw provider streams permanently. | Preserve the first pilot bundle outside Git, inspect its contents and size, and estimate total storage before any raw evidence commit. Stage 3 records the retention decision, respecting CLAUDE.md's never-commit rules. Stage boundaries commit reviewed development artifacts plus complete evidence manifests; external raw evidence requires verified primary/backup copies and absolute locations. Completeness of preservation is required regardless of Git placement. |
| P3: Model latency consumes the 20-hour ceiling. | Retain waits in the ceiling to bound study time and make tooling costs visible. Stage 1 budgets sequential latency; Stage 3 substitutes pilot timings. Consider bounded concurrency only after demonstrated need and verification of isolation, ordering and preservation. The suggested 15–25% latency share is an estimate, not a measured result of this study. |

The reference sweep updated current plan/review claims; prior review sections remain historical, and abandoned plans, runner history and unrelated fixture matches retain their existing scope. The general spec already assigns safeguard limitations, proportional evaluation and bounded dispatch to the study, so it requires no amendment.
The owner's latest instruction limits this work to the plan and review record followed by proposed next steps. Candidate and limits remain pending confirmation; no protocol, fixtures, provider calls or skill edits are authorized by this update.
Verification: hook suite (`python3 -m pytest -q` in `skills/disciplined-development/hooks`) — 263 passed, 3 skipped; document links resolve, six stages remain, and `git diff --check` passes. These are repository/document checks, not another external review or evidence of study effectiveness.

## Stage 1 transition — 2026-09-12

The owner subsequently accepted preparation for `sweeping-stale-references`, with limits provisional until the allocation walkthrough, and requested Sol low or Terra medium for initial process checks.
The [study protocol](../skill-studies/sweeping-stale-references/protocol.md) records the selected Sol-low pilot setting, source identities, proposed contract/control and allocation, installed writing-skills requirements and runner inspection.
The file-by-file fixture constraint is confirmed in the loader and workspace implementation; no new preparation tool is justified yet.
The protocol surfaces the parent's missing-companion conflict and unqualified filesystem isolation before test design, rather than treating them as collection bookkeeping.
This is implementation of Stage 1 preparation, not another external review. Contract and limit acceptance, test design and provider dispatch remain pending.

## Protocol review and skill-relationship correction — 2026-09-12

The owner supplied Claude's protocol review (BLOCK), then clarified that DD orchestrates sibling skills rather than making them dependent on DD, and requested a complete skill read and durable account of their purposes.
All nine checked-in skill bodies have now been read; the [architecture map](../ARCHITECTURE.md#composition-boundaries) records their purposes and directional relationships, with all nine identities in the study source inventory.
The previous map already allowed standalone sweeping-stale-references; the study author failed to apply it and inferred a dependency from DD's Gate 4 invocation.
The spec and resumption guidance now require distinguishing independent use, explicit pairings and orchestration before selecting subject context.
This is a correction to the study design, not a change to the skill bodies or a new testing framework.

| Review issue | Current disposition |
|---|---|
| Path/document drift presented as an explicit existing promise. | The protocol distinguishes the skill's explicit documented-behavior/synonym scope, the interpretation that this covers moved paths, and the owner's intended outcomes. Missing literal wording does not prove exclusion; neither does owner clarification retroactively make relative-path handling an explicit instruction. Outcome assessment remains separate from procedural compliance. |
| DD/target overlap and the coherence of the missing-companion control. | Superseded by owner-directed standalone evaluation: original target alone versus no skill guidance, with identical task and neutral setup. No Gate 4 bootstrap or missing-companion exception remains in the operative design. Input isolation and successful target loading still require pilot evidence. |
| Wording campaign spends original/candidate capacity before checking the control. | Run the five no-target diagnostics first, conditional on reaching this later campaign. Stop if they supply no failure supporting the rewrite; do not automatically hunt for another failing probe. The initial pilot remains two proposed Sol-low calls. |
| Commit accounting omits grouping/length permission. | The contract now preserves grouping before exceeding normal commit-body preferences and permits necessary audit detail after grouping. No hard word/line cap is invented. |
| Evaluator dispatch lacks a qualified read-only mechanism. | Still unresolved before dispatch. Both collaboration's missing no-write-tool type and the runner's write-capable execution are stated; prompting alone does not satisfy repository policy. |

The study remains at Stage 1, with detailed contract interpretations and limits awaiting walkthrough, and no provider calls or skill rewrites.
These dispositions are an implementation response, not external acceptance or a new PASS verdict.
Verification: all 21 recorded source identities match; local document link targets resolve; `git diff --check` passes; hook suite **263 passed, 3 skipped**.
The protocol also marks the nine-minute time entry as an initial checkpoint, with subsequent unclocked preparation still to reconcile before confirming remaining capacity.

## Response to external review of 86f2286

Claude reports the previous scope, parent-attribution, control-coherence, grouping and diagnostic-sequencing findings closed, and independently reports 21 matching source hashes.
Its new verdict is BLOCK for two P2 findings, with two P3 clarifications; this response is not external acceptance.

| Finding | Response |
|---|---|
| P2: Outcome instructions can supply the sweep being measured. | Initial contribution cases now present a realistic trigger without directing the sweep or enumerating consumers, while preserving clear task scope and permission to reconcile related files. An explicit sweep request can still test execution quality; it does not null all possible comparisons, but cannot establish that the skill prompted scope expansion. No guaranteed control failure is assumed. |
| P2: Evaluator feasibility is an unscheduled gap. | The plan now assigns mechanism selection to the study orchestrator in Stage 1, before selecting model-assessed criteria, with live qualification in Stage 3. The proposed argument alone does not close the gap: `providers.py` grants writes to fixture/evidence, and Claude exposes Write/Edit/Bash. Codex uses a workspace permission profile; Claude's runtime denies HOME writes, but these controls are not a no-write-tool evaluator type and copied evidence remains mutable. Inspect existing compliant options first; any alternative requiring a policy change must be explicit. |
| P3: The first contract row blends instruction and clarified intent. | The row now labels the explicit procedure and owner-clarified outcome inline, and states that a path-handling miss alone does not prove violation of an explicit instruction. |
| P3: Format differences could dominate the contribution claim. | The protocol now bars format presence/spelling alone from supporting effectiveness, and prioritizes search breadth, triage, complete reconciliation and useful audit evidence. The control could independently emit the format; its absence is not guaranteed by construction. |

No provider calls, skill edits or new tooling were performed. Evaluator feasibility remains open and explicitly scheduled; the contract and limits retain their recorded owner-review status.

## Implemented evaluator permission modes

After inspecting the current runner and historical launch records, the owner approved read-only permissions for both Codex and Claude instead of disabling all tools.
The runner accepts optional `execution.permissions`, preserving the existing writable default, and CLAUDE.md explicitly accepts verified read-only enforcement as an alternative to a no-write-tool type.
The evaluator mechanism is now feasible; the earlier no-tools proposal and unimplemented-mode statements above are historical.
Read isolation, exact evaluator configuration and an authorized model/tool round trip remain separate qualification requirements.

Validation: new configuration/propagation/capture tests failed before implementation, then passed; runner unit suite **273 passed**, local dummy-provider process suite **12 passed**, hook suite **263 passed, 3 skipped**.
Installed local probes passed for both read-only policies and the existing Codex writable Git policy, including actual mutation denials and Claude scratch symlink escape denial.
No authentication or model calls occurred; initial nested-sandbox failures were preserved before host-permitted probes succeeded.
The [qualification index](../skill-studies/sweeping-stale-references/permissions-qualification.json) records source/CLI identities and verified same-host primary/backup evidence copies.
This is implementation verification, not a new external PASS or study-effectiveness result.

## Response to external review of dd5880c

Claude reports the prior design findings closed and independently reproduced 273 runner unit passes and 263 hook passes with 3 skips; it did not repeat process smokes or installed sandbox checks.
The new external verdict is BLOCK for two P2s, with one P3 advisory.

| Finding | Disposition |
|---|---|
| P2: Claude read-only advertises Write/Edit. | Removed both dedicated mutation tools from read-only `--tools` and `--allowedTools`; writable mode is unchanged. Bash remains useful for reading and is still constrained by the process sandbox. `--add-dir` retains evidence read access, not a sandbox write exception. The change removes avoidable write-tool affordances; it does not guarantee that no model will attempt a denied shell write. |
| P2: Canonical result lacks permission mode. | Every new result records resolved `execution.permissions`, including pre-launch failures. Output schema is now 0.3 with a required enum; input schema stays 0.2 with the optional, defaulted extension. Existing input configurations retain behavior. Historical result files are not rewritten; consumers must distinguish versions rather than assume a missing permission mode. The protocol checks mode/configuration identity against the intended condition before scoring. |
| P3: Runtime/HOME exclusion is only documented. | Not reproduced: `ClaudeRuntime.prepare()` already rejects a runtime root or fixture beneath resolved HOME before authentication, Git setup and child-policy use. Added both containment regression cases; both passed against the existing guard without changing production behavior. |

The tool-list and result-record tests failed before implementation and now pass.
The previously qualified filesystem policies are unchanged; retained sandbox evidence remains applicable to those boundaries, while the updated tool list and result contract receive focused and process regression coverage.
Validation: runner unit suite **285 passed**, dummy-provider process suite **12 passed**, hook suite **263 passed, 3 skipped**. All five original qualification source hashes match `dd5880c`; all four follow-up source hashes match the current files. No authentication or model calls occurred.
This response is not an external PASS or authorization for model collection.

## External review of 463e0e2 and cc978be

The owner supplied Claude's review with **DD-VERDICT: PASS**, closing the prior runner findings and accepting the contract decisions.
Claude reports independently reproducing 285 runner unit passes and checking schema versioning and output consumers; it did not repeat process smokes or installed sandbox probes.
One historical attribution correction: the HOME containment guard was already present in `dd5880c`; `463e0e2` added regression coverage, not that production guard. Verified against the committed source.

| Walkthrough item | Disposition |
|---|---|
| P3: Cases need a functional opportunity beyond accounting differences. | Stage 2 explicitly requires a case with latent config, CI or fixture consumers beyond the trigger. Successful controls remain valid evidence. The protocol also makes a functional tie plus procedural advantage visible, instead of collapsing it to “no difference.” |
| P3: Reconcile preparation time before confirming the ceiling. | Reconstructed closed active-turn intervals from the local task log, replacing the incomplete checkpoints with a cumulative booking and labeled allowance/rounding. The protocol owns the current total and remaining time. |

The observation about document growth is retained for Stage 6's existing review of which framework steps to remove or combine; it does not introduce another review round.
The PASS applies to the reviewed commits, not these follow-up edits or unqualified model execution. The subsequent owner walkthrough accepted the outer ceilings and directed conceptual coverage review before scenario selection, with minimal initial real-model runs to establish the process. No model calls or skill changes occurred.

## External review of 9058f4a

The owner supplied Claude's **DD-VERDICT: PASS** and accepted the seven conceptual facets.
Claude verified the storage-anchor sweep and time reconstruction; its observation that the allowed four-minute turn ran longer is handled by cumulative recomputation, not another additive allowance.
The P3 about repeated Stage 3 checkboxes is addressed by a pilot-only status table: pilot configuration, authorization, check validation, execution qualification and retention are scoped to the two calls; whole-collection boxes remain open, and the measured-collection freeze cannot be closed by the pilot.
The next external review should inspect the two actual bundles, including traces, Git history and functional/procedural evidence; no additional document review is scheduled.

## External review of 4037fa3

Claude independently verified the fixture inventory, condition manifests and reachable runtime failures, and reported **DD-VERDICT: BLOCK** for a future original-source attribution risk; the prior pilot-checkbox P3 is closed.
P2 addressed now: `original.json` sources a byte-identical snapshot at `cases/skill-original/SKILL.md` instead of the live skill path. A scratch-checkout check with a different live candidate confirmed the original config still loads the pinned original; the live repository skill was not modified.
P3 addressed as an observation: record control attempts to inspect `.agents/`, whether guidance was loaded, and whether absence stopped the task. A harmless missing-directory probe alone is not a new task failure or evidence of contamination.
Config loading, shared-input/settings parity, prompt parity and original-byte identity pass; manifests and the study's future original-condition routing are updated. No model calls occurred, and this response does not claim an external PASS on the edits.

## External review of 2ca4701

Claude supplied **DD-VERDICT: PASS — no findings**, closing the original-source and control-probe items. It independently verified the snapshot/manifest hashes and loaded both configurations with the real loader without provider invocation.
The owner continuation requests dispatch of the reviewed pair. Execution evidence, not another document review, is the next qualification step; the protocol and pilot run index record the bounded authorization and attempts.

## Pilot execution checkpoint, 2026-09-12

Both authorized Sol-low subject calls completed; [the pilot report](../skill-studies/sweeping-stale-references/pilot-results.md) links retained evidence and separate functional/procedural observations.
The original repaired all seven current consumers; the control found the siblings but repaired only the README.
The original's nine-entry account omitted six broader-search matches, a non-blocking procedural defect under the pre-run criteria.
Both complete raw bundles have verified primary and backup copies outside Git. No additional model call, skill edit or measured-baseline claim follows from this checkpoint.
This is orchestrator inspection, not a new independent review verdict. The next review target is the two bundles and their interpretation.

## External review of the pilot through 5615f58

Claude reported **DD-VERDICT: BLOCK** with one P2 concerning the accounting disposition and one P3 concerning the presentation of preservation. Its independent checks confirmed the functional results, retained commits, bundle sizes and two-call limit.
P2 response: withdraw the confirmed P2/P4 procedural-defect disposition in a versioned assessment correction and retain the accounting-scope ambiguity; it is not evidence supporting a rewrite objective. The review's assertion that the registered scope says the opposite is not established: both the frozen assessment and `expected.json` expressly discuss additional query results, including the new name. Accordingly, neither an unequivocal full-compliance verdict nor a definite skill-defect verdict follows from the disputed scope.
P3 response: retain equal F2 outcomes and distinguish inspection/triage behavior. The review's claim that the control never looked at the historical plan is contradicted by control trace line 10, which reads it explicitly; no vendor-content read is observed. The original's explicit historical/vendor accounting remains a procedural advantage.
The prior pilot assessment at `5615f58` and all frozen inputs/raw evidence remain unchanged in history. The current report and run index identify the correction and applied policy/criteria. No subject/evaluator call, skill rewrite or new independent PASS is claimed.

## External review of f36ffa0

Claude supplied **DD-VERDICT: PASS**, verifying the prior/current assessment identities, applied policy and frozen case criteria. It accepted the unresolved accounting scope, corrected its earlier claim about control inspection of the historical plan, and confirmed the functional findings and two-call limit.
Its precision note is verified: the preservation statement comes from the control's mid-run agent message at `stdout.txt:13`, not `final.txt`. The report now points there; assessment judgments are unchanged and the index retains the reviewed report identity alongside the editorial update.
Pilot review is closed. Next is the moved-file facet, with owner-clarified outcomes distinguished from explicit instructions before fixture construction. No new run or skill rewrite is authorized by this review.
