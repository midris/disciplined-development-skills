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

## External review of c1ca959

Claude supplied **DD-VERDICT: PASS — no findings** for the simplified pilot 02 package. It independently verified the four required consumers, preservation cases, all manifest/policy identities and subject-input boundaries, and reproduced eight passing observer tests. Its probes confirmed that blanket basename replacement damages the vendor link and that a cwd-relative export repair fails from outside the project, both covered by the assessment.
The review confirms that accounting scope is explicit before collection and the proposed pair fits two additional-development slots. No case change or further document review is required. Exact provider dispatch remains pending owner authorization; model-call usage remains two subjects from pilot 01.

## Pilot 02 execution checkpoint, 2026-09-13

The owner approved the exact control/original Sol-low pair after the preparation PASS. Both calls completed; the [assessment](../skill-studies/sweeping-stale-references/pilot-02-results.md) records 4/4 committed repairs for original versus 1/4 for control, with preservation met in both. No independent post-run model review is claimed; owner review of the bundles is next.
Controller inspection verified identical initial trees, complete original-skill loading, ordered traces, committed diffs and replay from two working directories. Full source/primary/backup inventories and frozen input hashes were reverified after inspection. The six-versus-seven-path summary error is a minor procedural defect with no functional consequence. No scoring-policy amendment or extra run is warranted by it.
A controller-package omission was corrected by copying and verifying the checker's existing pristine-fixture dependency; frozen inputs and checks were unchanged. Active plan/protocol status and allocation now reflect four subject calls, no evaluator/authoring/retry calls and no unspent dispatch authorization. Local document links, JSON parsing and `git diff --check` pass; hook suite: 263 passed, 3 skipped.

Owner follow-up: accepted the explanation that seven real matches occupy six paths, with no invented reference or unwanted edit, and requested commit/push. This closes the requested walkthrough; it does not constitute an independent post-run review or authorize more model calls.

## External review of e5381e2

Claude supplied **DD-VERDICT: PASS**, independently reproducing bundle preservation, sizes, baseline equivalence, required committed changes, protected content, path resolution, export behavior and search-before-edit ordering. It confirmed the accounting issue is only a mistaken distinct-path total, not invented matches or incorrect grouping.
Accepted P3: both controls encountered the required current consumers before their narrow repair, so these cases primarily distinguish scope/reconciliation decisions. Broad-search procedure is observed; added discovery effectiveness under realistic repository complexity is not established. Rechecked pilot 01 control `stdout.txt:8` and pilot 02 control `stdout.txt:10` against retained traces. The protocol now separates discovery from action after discovery and records the gap; the plan recommends reviewing that concept before building another case. A successful control remains valid evidence, not a reason to manufacture a miss.
No scoring or frozen-input changes, new model calls, budget transfers or skill edits. Four subject calls remain spent, with one additional-development slot available but no further dispatch authorized. This is a coverage clarification for future case design, not a revision to either pilot assessment.

## Discovery-case local preparation checkpoint, 2026-09-13

Owner approved the concept; all six historical SSR prompts and fixture inventories were inspected for reuse, with no structurally suitable case found. Prepared pilot 03 as a new working packager, with complete locally vendored packaging 26.3 source and licenses. No prior result or rubric became authority. Four fixture-application tests and eleven controller tests pass; paired configs load/copy exactly with frozen original and no provider calls.
Self-inspection identifies an unresolved design limitation: 49 files / 505,460 bytes / 13,210 lines appear substantial, but first-party/independent-tool material totals only 23 files / 12,246 bytes. The fixture may still reproduce easy discovery after ignoring vendor source. This is explicitly not a discovery-adequacy PASS or dispatch recommendation. Review the scale limitation before spending; use a more substantial first-party project if this candidate does not support the intended question. Local construction does not make this case mandatory catalog content.
The controller checks deliberately remain facts-only: unsupported Markdown/workflow forms require inspection, preservation byte differences need semantic judgment, and nonzero retired-option exit alone cannot establish correct rejection without a working canonical CLI. Complete/incomplete/damaging/no-op/rollback variants are covered before any model observation. Model-call budget remains 4 subject / 0 evaluator / 0 authoring / 0 retry; no transfer or extra dispatch authorized.

Preparation verification: source/controller/dependency hashes, input parity and local links pass. Hook suite passes from its documented working directory (263 passed, 3 skipped); an initial root-directory invocation produced four import-path failures, corrected by using the documented command location without code changes. Self-inspection recommendation is to withhold dispatch of this draft and find a more substantial first-party project; added vendor volume does not convincingly address the discovery gap.

## Discovery replacement-base selection, 2026-09-13

Following the owner's continuation request, inspected available local projects and the existing runner, then selected pinned public Shiv source as a closer fit to the approved offline packaging-CLI concept. Its source/tests/docs/CI provide 84,665 bytes / 2,514 lines of actual first-party material, compared with the synthetic draft's small first-party core. Source provenance and reproducible scratch-probe scripts/results are retained in discovery-project-selection.json.
Offline probes build and execute an archive without pip installation; the study-only long-option rename also works while preserving the short alias. These establish feasibility, not a qualified case or discovery advantage. A final isolated runtime and case consumers/checks are still required. The discarded draft and previous assessed inputs remain unchanged; no model calls or budget transfers occurred. No independent review PASS is claimed for the replacement.

## Shiv discovery-case preparation and self-review

Owner approved proceeding and clarified that packaging is merely the scenario domain. First-party tools remain eligible; the protocol now states Shiv's selection without implying an eligibility restriction.
The distinct `cases/discovery-shiv/` package is locally prepared. All 40 pinned upstream files are present, with exactly four recorded modifications and ten added project files. Project scale is 50 files / 106,979 bytes, separately from the 19-file / 424,152-byte runtime. The source is real; the settled rename, consumers and preservation examples are explicitly study-authored. The rejected synthetic pilot-03 draft and all assessed evidence remain unchanged.
Self-review enumerated all nine old-option occurrences across eight paths, verified source adaptations and policy provenance, and checked input parity: 70 common fixture entries, plus only the frozen skill and its read instruction in original. The real loader/preparer reproduced all source bytes and modes; each subject baseline includes exactly 50 project files. The isolated runtime probe verifies local module origins and an offline build with pip installation forbidden at its call site.
Qualification: four public CLI tests and eleven controller tests pass; the pristine fixture has zero working consumers out of four and the constructed complete repair succeeds 4/4, preserving the supported alias, independent tool and unrelated bytes. Tests also cover README-only/hidden-CI omissions, blanket replacement damage, no-op artifacts, rollback, unsupported document form, changed payload and outside-directory execution. Hook suite: 263 passed, 3 skipped. All new case files and the active diff pass whitespace checks.
The case criteria lead with functional completeness, preservation and committed edits; discovery/exposure, explicit triage and detailed accounting are separate. No exact-byte or parser limitation is promoted into an automatic semantic failure. Runtime source files need explicit Git inclusion despite the subject-facing ignore rule; the assessment and manifest record that retention requirement. Existing reviewed results and frozen criteria are intentionally unchanged.
No remaining blocking finding in this preparation self-review. This is not an independent review or model-evaluator qualification. Discovery difficulty remains unproven, full upstream/hosted-CI tests are outside local qualification, and actual subject setup/traces still need observing. No model call, retry, budget transfer or skill rewrite occurred. One development slot remains; a pair requires an owner-approved allocation revision before dispatch.

## Pilot-wide review before committing the Shiv case

Scope: current framework/plan/protocol, both assessed pilot pairs and retained evidence, the undispatched synthetic draft, and the Shiv replacement's source, input boundaries, checker and qualification. Preserve prior assessed criteria and results; fix the new case before any dispatch. This is controller self-review, with no provider invocation.

- [P2] `cases/discovery-shiv/check_consumers.py`: preservation observations derive their coverage from whichever pristine files happen to be present. A missing directory or omitted historical file can produce an incomplete comparison rather than a setup failure. Reproduced with missing-directory and missing/changed-file tests. Pin the complete pristine inventory in controller expectations and verify it before any replay command or output deletion.
- [P2] `cases/discovery-shiv/check_consumers.py`: a retired-option timeout produces `retired_option_nonzero: false`, collapsing unobserved behavior into a negative observation. Reproduced with a timeout at that process boundary. Preserve unknown as null and retain the underlying infrastructure error.
- [P3] `discovery-project-selection.json`: the selection-time decision still says assembly and qualification are required, although the current case is prepared. Mark that as selection-time context and link the current preparation state.

These are distinct reference-integrity, uncertainty-representation and status-routing issues. Fix the full classes in the new, undispatched checker; do not rewrite frozen historical instruments or retrospectively alter prior judgments.

Resolution and re-review: both P2s and the status-routing P3 are closed. The checker verifies every declared pristine SHA-256 before any command or output deletion, and its preservation loop uses that fixed inventory. Missing directory, missing/changed historical reference and timed-out retired-option probes were observed failing before the fixes; the final 14-test checker suite passes. The inventory matches all 69 supplied fixture files; subject inputs and the original/control difference are unchanged. Selection-time language is distinguished from current qualified state in both routing documents.
The new [pilot-wide verification record](../skill-studies/sweeping-stale-references/pilot-review-2026-09-13.json) retains fresh checks of all four primary/backup bundle inventories, matching baseline trees, complete retained Git histories and disposable runtime replays. Both prior original runs still contain all required committed edits; both controls contain only README. Assessment and policy identities verify. No prior outcome, accounting ambiguity or severity rule changed.
Final local checks: four CLI tests, fourteen checker tests, 285 runner unit tests, twelve dummy-provider process smokes, and 263 hook tests with three existing skips. The initial combined runner invocation had six Claude process failures because the outer sandbox denied nested sandbox-exec; a minimal invocation reproduced that restriction. All process smokes passed with host execution, with no model calls. No runner code change or new sandbox qualification claim follows.
All remaining limits are explicit: actual Shiv subject behavior and discovery difficulty are unobserved; the full upstream/hosted-CI suite, reserved-case isolation and model-evaluator reliability remain unqualified. Prior assessed artifacts and rejected pilot-03 content remain intentionally unchanged. No remaining blocking finding in this controller re-review; this is not an independent evaluator review. The owner authorized committing and pushing the reviewed preparation, not further subject dispatch.

DD-VERDICT: PASS

Staged-checkout verification: all manifest-referenced files match their staged Git blobs, including the 19 runtime files ignored only for subject baselines. A clean checkout of the index loads and copies both runner configurations and passes all four public CLI tests without the preparation scratch environment. The staged diff passes whitespace checks and changes no prior assessed fixture, report or raw bundle.

## External review of 314b72e

Claude reports PASS on committed preparation, independently reproducing the project/runtime sizes, nine-match inventory, paired input boundaries, frozen skill identity, 14 checker tests, four CLI tests and hook suite. It raises two P2 decision issues before further allocation and one advisory coverage limitation.

- Development termination: confirmed that the current per-call process-purpose gate has no phase exit. Recommend closing pre-baseline development now at four subject calls and selecting Shiv for baseline design instead of buying another pilot pair. The protocol records the proposed stopping rule and the existing eight-call/two-case baseline arithmetic; the plan routes the owner to that decision. This remains pending owner approval, with no capacity transfer, new call or retroactive baseline classification. Precision correction: two pairs have run, not four; the rejected synthetic draft and Shiv preparation have not run.
- Public-source exposure: confirmed as an unrecorded attribution limit, not demonstrated knowledge of any particular model. General spec, study attribution guidance and Shiv Setup now distinguish possible prior familiarity from in-session leakage. Trace inspection records upstream-API claims without inferring non-exposure from silence. An upstream-restoring edit receives task/evidence and attribution review; verified violation of the explicitly settled rename remains a hard F2 failure under the owner's policy. We do not adopt an exemption from functional scoring or assume a failure was caused by memory. The suggested invented option is already present as --destination; a study rename necessarily differs from this pinned upstream interface.
- Lexical diversity: accepted as a limitation and deferred as additional fixture work. All four current consumers contain the retired literal; the case adds meaningful location diversity but does not require variant search. Pilot 02 exercised relative-path variants in a small fixture; pilot 01 does not establish difficult lexical discovery because its control exposed every current consumer. Record the gap without adding a consumer or another pair solely to force difficulty.

Only controller guidance, phase recommendations and their identities changed. Skill bytes, task/prompts, fixture/configuration bytes, deterministic checks, prior results and SSR-assessment-2 remain unchanged. Preparation remains mechanically qualified; the phase-exit decision is explicitly pending. No new model call, evaluator dispatch, budget transfer, commit or push is implied by this review response.
Verification: all current manifest hashes and active document file links resolve; both complete subject input sets are byte-identical to 314b72e, and the SSR-assessment-2 policy copy remains verbatim and unchanged. `git diff --check` passes; hook suite: 263 passed, 3 skipped. No code or fixture changed, so the prior CLI/checker qualification remains applicable. The proposed phase exit is the only owner decision requested by this response; it has not been marked accepted.


## Owner decision: baseline design

Owner approved ending pre-baseline development at the four completed calls and moving to baseline design. The remaining additional-development slot stays unused. The plan, protocol and unrun Shiv case metadata now route to baseline selection and freeze rather than another pilot allocation request. This closes the pending phase-exit decision from the review of 314b72e; the eight-call baseline remains a design envelope, not dispatch authorization. Earlier proposal/approval statements above remain historical records.


## Owner decisions: artifact formats and deterministic tooling

At the end of baseline design, agree on version 1 of the protocol and companion case/criteria, run-index, manifest, assessment/comparison and layout/lifecycle contracts. The plan owns the checkpoint; the framework spec owns the proposed boundaries and generator/validator requirements. These are recorded design decisions, not completed schemas or implemented tools.

Inspected the existing worksheet command, implementation and focused tests. It generates blank assessments with mechanical run identity; it does not validate completed assessments or general study documents. The owner explicitly rejected making it a required foundation: choose reuse, adaptation, replacement or retirement from the agreed deterministic requirements, and update scoring tooling as needed while preserving settled assessment policy and historical evidence.

Consistency review reconciled remaining current-state pilot instructions with the accepted baseline transition. Historical review proposals above remain intentionally preserved and are superseded by the owner decision. No subject inputs, skill bytes, executable checks or prior judgments changed. Focused worksheet tests: 15 passed; hook suite: 263 passed, 3 skipped. Manifest hashes, unchanged subject inputs and policy copy, active file links and diff whitespace are checked before commit. No provider call was made.


## External review of 7f8d38b

Claude reports PASS, confirms the prior P2 closures, and corrects its earlier pair count. Three new observations were checked against the current plan and protocol:

- Time tracking: accepted. The original 240/180-minute preparation/qualification targets had no actual-versus-forecast reconciliation. The protocol now exposes the mixed historical booking without inventing a split, forecasts remaining work, shows the preparation/qualification shortfall, and requires reconciliation at subsequent checkpoints. Tool implementation has a separate zero-funded row and a proposed 120-minute ceiling; neither a transfer nor additional capacity is approved. The baseline-design walkthrough must settle the shortfall; this finding is not declared budget-resolved merely because tracking exists.
- Tool sequencing: accepted as a planning correction. Format agreements remain before collection freeze. Tool design/build/qualification move after baseline collection and assessment, with scope and funding agreed first. The owner requested formats before tooling, not tooling before measurement. Manual structural/identity checks remain required, and the requested tool remains an outstanding deliverable.
- Rename collision: corrected our reading. Claude meant the retired upstream name, not the new name. The framework now requires considering both-name invention and documenting the choice; it is an optional mitigation, not a universal requirement or proof of no prior exposure. The qualified Shiv fixture stays unchanged: the task explicitly settles its rename, and a verified rollback remains an F2 failure.

No provider dispatch, fixture change, new tool implementation or budget increase follows from these edits. The proposed tool cap and any time reallocation remain owner decisions.


## Owner clarification: estimates are not failure criteria

The owner confirmed that effort estimates are useful and that variance can prompt checking test scope, but missing a time budget is not a failure in itself. This supersedes the phase-cap, mandatory reallocation and tooling stop-limit language in the preceding review response. The spec owns the general distinction; the plan and protocol now treat phase amounts and the preliminary tooling estimate as planning aids. The separately agreed overall autonomous-work ceiling remains an authorization boundary, not a scoring threshold. Necessary work is not weakened to meet an estimate, and incomplete evidence is reported as a limitation rather than a failed skill outcome. No fixture, frozen scoring-policy bytes or prior result changed.


## External review of 718f06d

Claude reports PASS and verifies prior arithmetic. Accepted the missing aggregate: carrying forward the later phase estimates yields 990–1,080 remaining minutes without tooling, or 1,110–1,200 with its preliminary estimate. The protocol now compares both with remaining authorized time, reports projected whole-study totals and extension needs, and labels the unchanged later-phase estimates as planning assumptions rather than fresh forecasts. The need is presented for the owner walkthrough; no extension or provider dispatch is inferred.

Trimmed repeated timing-policy statements within the spec, plan and protocol. The spec owns the general rule; the protocol links to it and states SSR's ceiling and next decision; the plan owns the reconciliation checkpoint. Historical review responses remain intact. Checks cover aggregate arithmetic, current accounting, active links, unchanged frozen policy and diff whitespace.


## Owner priority: core outcomes before expanded coverage

The owner asked to focus on real value and establish the core before edges. The protocol now leads with complete, correct, preserved and committed reconciliation. Broad search remains an explicit procedural obligation; a discovery advantage over the control is diagnostic, not a separate success criterion or collection prerequisite. The plan uses the prepared Shiv/moved-guide pair as its working proposal and routes next to evaluation preparation rather than another scenario-choice loop. Semantic drift remains intended behavior with deferred coverage, not an excluded requirement. Case freeze and provider authorization remain outstanding; current policy bytes and prior judgments are unchanged.


## Owner decision: three core baseline situations

The owner accepted interface rename, moved file and semantic documentation drift as necessary core coverage for this design stage. This supersedes the immediately preceding two-case proposal and semantic deferral. The protocol now distinguishes prepared Shiv/moved-guide foundations from the undesigned semantic case; the plan routes next to its conceptual review before reuse or construction. The prior call table is explicitly pending revision for both baseline and later comparison. Core-first prioritization does not exclude an intended core outcome merely because it needs a new case. No run or budget extension is approved by the coverage decision.


## Semantic-delivery case: local preparation review

The owner accepted the retry-policy concept and authorized construction. Inspected all six historical SSR prompts after concept acceptance; none supplies the semantic-drift mechanism. The new nine-file fixture leaves code correct and three differently worded current claims stale, with historical/independent preservation targets. Subject conditions differ only by the frozen skill and read instruction.

Local review checked the task against the core contract, the five reference blocks against actual files, the attempts/retries arithmetic, valid consolidation links, unchanged early-success behavior, and all nine constructed document/Git variants. The runtime probe reports facts independently of subject tests and distinguishes missing/failed probe evidence from observed behavior. All documentation variants pass runtime checks despite different semantic reference judgments; the records do not claim independent model-evaluator qualification. Kept incomplete-repair/perfect-account calibration as an explicit remaining evaluator requirement rather than implying the sparse-account variants qualify it. Overlapping F1/F3 consequences are identified as a shared cause, not independent failures.

Verification: seven subject behavior tests and eight controller tests passed after recorded failing stubs; all nine variants reconstructed with inspected Git changes; real runner loading/copy yielded 10/11 inputs and identical nine-file baseline trees. Hook suite: 263 passed, 3 skipped. No provider calls, old-result edits, scoring-policy changes or tool-framework implementation occurred. Verified 34 manifest records, 22 qualification-source hashes, original-skill/policy identities, active and fixture links, and Git inclusion of every case input.

No unresolved findings in local case preparation. Baseline freeze, model-evaluator calibration, information-boundary qualification and revised allocation remain outstanding study work.

DD-VERDICT: PASS

## Semantic-delivery preparation: requested review and remediation

Reviewed the complete case, constructed evidence and current plan/protocol/spec against the owner’s core-coverage and scoring decisions. Re-read all nine reconstructed current-document sets, checked the five reference meanings, runtime schedules and committed/uncommitted distinctions, and exercised failure paths in the controller. The case remains a semantic reconciliation test; search advantage and exact prose/accounting format are not functional gates.

Findings verified and resolved:

- [P2] `cases/semantic-delivery/probe_behavior.py`: successful subprocess exit plus parseable JSON was accepted without a complete observation record. A module printing null, a list or an incomplete object and exiting reproduced missing/false evidence; undecodable output also escaped as an exception. The observer now requires all seven schedule records and consistent observed types/status, and reports malformed/incomplete output as needing inspection. This is evidence-shape checking, not semantic scoring or a security boundary.
- [P2] `cases/semantic-delivery/qualify_case.py`: optimized Python silently removed the assertions that establish qualification. An actual `python -O` invocation returned success before the fix; qualification now rejects optimization before creating scratch output.
- [P2] `cases/semantic-delivery/qualify_case.py`: inherited Git directory/worktree/index overrides could redirect scratch operations. A test using only disposable paths reproduced the redirection. The child environment now clears inherited `GIT_*` overrides before applying its explicit configuration. The sweep found no other current case qualification CLI; embedded historical reconstruction text remains evidence of its original execution, not a replacement command to dispatch.
- [P2] `protocol.md`, whole-study allocation: stale initial-pilot wording invited another process run, and the original two-case table lacked a local supersession notice. The section now records both completed pairs, links the closure rule, and marks the old allocation pending revision for the three accepted core situations. Resumption status and the plan now route to formats, evaluator preparation and allocation.

Verification after fixes: seven subject tests and twelve controller tests pass; all nine variants reconstruct with expected runtime/Git facts, and real runner preparation retains identical nine-file baseline trees with 10/11 declared inputs. Hook suite: 263 passed, 3 skipped. All 35 manifest records plus the frozen skill record and all 23 qualification-source hashes verify; the policy slice is unchanged. Regression tests failed before remediation. Subject fixture/configuration/prompt bytes and authored semantic judgments remain unchanged; the unrun construction record was regenerated to identify the repaired controller.

Follow-up consistency review found no unresolved local preparation finding. Model-evaluator calibration, information boundaries, versioned baseline artifacts and revised allocation remain explicit stage work; no model was dispatched. This is a local self-review, not an independent assessment.

DD-VERDICT: PASS

## Response to external review of b22cf5d

Verified both pending-design findings against the allocation and evaluation rules. The expanded subject scenario is 12 baseline + 15 conditional diagnostic + 16 comparison = 43 remaining, against 40 − 4 = 36 outer capacity: 47 projected total, seven over the ceiling. It is eight above the previously scheduled 35 remaining calls; the closed development slot remains unused without an approved transfer. The protocol now presents this aggregate beside its phase assumptions and routes call/time revision to the same walkthrough. No allocation increase is approved by the arithmetic.

The semantic case has a planned assessment path, but no qualified model evaluator yet. Applied the existing readiness rule at the decision site: unresolved calibration pauses full baseline freeze and subject collection; bounded repair needs an explicit allocation/approval. Controller inspection stays development evidence, and the required case is not silently omitted. If qualification remains unresolved within authorized work, the intended full baseline is inconclusive; a different evaluation method or reduced claim requires an owner decision before collection. The plan links resumption to this branch.

The reviewer’s search observation is best read as a triage distinction: no single literal substitution supplies the repair, while search can still locate the references. Semantic interpretation is the core outcome tested; a discovery advantage remains diagnostic. No fixture, criterion, qualification evidence or scoring-policy bytes changed.

Both findings are addressed as planning instructions, not claims that allocation or evaluator qualification is complete. The initial hook invocation from the repository root produced four module-import errors; verification was rerun from the hook directory required by CLAUDE.md. Local arithmetic, links, frozen identities and whitespace checks passed; hook suite: 263 passed, 3 skipped. No model dispatch or budget extension occurred.

DD-VERDICT: PASS

## Evaluator-calibration proposal and local package review

Prepared the [proposal](../plans/specs/2026-09-14-ssr-evaluator-calibration.md) and eleven neutral constructed document/Git records for owner review. Two fresh Sol-low read-only calls are proposed, repeating the examples in different orders without feedback; no call is authorized or performed. The second call is conditional on a valid first assessment without a material error. The draft requires correct criterion judgments with defensible evidence on both calls, not merely matching labels.

The reference key distinguishes sparse/full accounting, a truthful account of incomplete work, preservation damage, attempts/retries confusion, always-four wording, removed versus consolidated guidance, uncommitted work, two-commit completeness and missing Git evidence. The truthful-incomplete-account and grouping/completeness readings are explicit proposed interpretations for owner review, not silent changes to frozen criteria or old scores. All P1 references remain insufficient evidence because action streams are absent; positive/negative action-order qualification is still open.

Local checks re-derived all eleven final snapshots and committed/working patches against actual disposable Git repositories, verified unchanged runtime code against the qualified case, checked both complete batch permutations and source hashes, and verified reader-facing links. The allowlist covers 19 distinct evaluator files across both batches (18 per call); the answer key, construction identities and proposal remain controller-only. Neutral input omission is not host read isolation: read-boundary qualification or an explicitly accepted limitation remains required before dispatch. Criteria and policy retain their source identities; copied archival citations are provenance rather than requests for external retrieval.

Self-review checked the evidence/instruction boundary, functional/procedural distinctions, unsupported calibration claims and resumption path. No unresolved defect in the draft preparation; exact configs, information boundary, retention/authorization, shared format agreement and whole-study allocation remain next-stage work. The package is neither dispatch-ready nor an independent evaluator qualification. Hook suite: 263 passed, 3 skipped; whitespace and identity checks passed.

DD-VERDICT: PASS

## Correction: restore the already-intended active-session workflow

The owner reaffirmed, rather than introduced, the intended workflow: the active Codex/Claude session runs fixed scenarios, waits for the deterministic harness to capture evidence, applies fixed interpretation rules and writes a fixed-format score record. A human can use the same rules. The existing spec already assigned interpretation/evaluation to the model and described layers as responsibilities, not separate agents.

The implementation plan nevertheless required fresh evaluation contexts, prohibited direct-session baseline scoring as an unrecorded substitute, and blocked semantic collection on separate evaluator calibration. At `32eaa61`, the protocol said “routine orchestration is not a source of unrecorded substitute scores”; the plan required “fresh model contexts.” These operative instructions contradicted the stated workflow. That inconsistency was introduced by the agent, not caused by a missing owner decision. A responsibility had been turned into a mandatory extra process, and later checks reinforced that mistaken assumption.

Corrected the spec’s default session loop and fixed rule/score-record requirements; swept the plan, protocol and project entry points to remove mandatory evaluator/calibration gates. Optional independent review and held-out evaluation remain available only when chosen for those claims. The old whole-campaign allocation and forecast are marked superseded; actual ceilings and spent calls remain unchanged, with no automatic transfers. The next action is the reusable rule/score formats and a concrete small run set, not a separate evaluator.

SSR-assessment-3 records this workflow correction while preserving the owner’s functional/procedural priorities and criterion-level judgments from policy 2. Prior assessments and frozen case inputs retain their exact policy-2 identities. The separate-evaluator proposal/package is visibly superseded; packet payloads, reference key and evaluator input bytes remain unchanged, with previous controller-document identities retained in its manifest. Its proposed scoring interpretations are not promoted to owner decisions. No subject observation is relabelled or scored anew.

Verification: current rule/score responsibilities, stage exits and resumption links were checked for consistency; historical evaluator requirements remain only under explicit supersession or optional-dispatch scope. Frozen case/example hashes and current controller-document identities verify. Local links/anchors and whitespace checks pass; hook suite: 263 passed, 3 skipped. No runner code, core skill, provider call or spending authorization changed.

DD-VERDICT: PASS

## Follow-up: current case inputs and writable score artifacts

Claude's review of `952f83e` returned PASS on the corrected direction, with two P2 cleanup findings and one P3 missing deliverable. Both P2s were valid: the prior sweep wrongly treated current unrun controller inputs as frozen observation history. That left the separate-evaluator gate at the point where the next assessor would read it, despite the corrected spec.

- Updated both unrun packages, discovery-shiv and semantic-delivery: policy-3 copies, assessment instructions, expected-policy identity, preparation provenance and manifests. Subject fixtures, prompts, configurations, checkers and the original-skill snapshot are unchanged. Semantic reconstruction was rerun against the revised controller inputs; its prior qualification is identified at `952f83e`. Shiv's existing qualification remains historical evidence for unchanged mechanics, explicitly scoped in the current manifest.
- Added a verbatim copyable `assessment-policies/SSR-assessment-3.txt`, derived from the protocol's policy section. Observed pilot-01/02 inputs and assessments, the superseded evaluator proposal and its historical packets remain unchanged. Preparation records retain prior policy provenance rather than silently relabelling it.
- Addressed the P3 with a draft completed-score schema, blank template, format instructions and a separately indexed policy-3 example from the retained pilot-02 original bundle. This is a new format example, not a new subject run or replacement historical score. All three functional criteria remain met; registered audit usefulness remains met with the same explicit minor non-blocking path-total defect. No new scoring interpretation or evaluator prerequisite was introduced.

Verification: 191 current case-manifest hashes and 23 fresh semantic-qualification input hashes match; all four unrun configs load and exclude controller scoring inputs. Original configuration manifests and frozen skill records match the prior revision. The original pilot-02 primary and backup each match all 55 retained file hashes. Disposable replay confirms every link, preservation fact, all four committed repairs, a clean tree and correct export from both working directories. Score provenance, criterion coverage and evidence-ID references were checked directly.

Format checks were written before the schema/example and first failed for the missing artifact; all 8 now pass, covering required provenance/evidence, invalid values, functional failure/uncertainty precedence, separate procedure and rejection of an incomplete template. Semantic controller tests: 12 passed; Shiv controller tests: 14 passed; hook suite: 263 passed, 3 skipped. Self-review checked the changed current-input class, preservation boundaries, three-state scoring and resumption links; no unresolved findings. The format remains `1-draft` for owner review, and broader rule/layout agreement and the later generator/validator remain open. No provider calls, skill edits, invocation allocation changes or authorization extensions.

DD-VERDICT: PASS

## Fresh-session handoff verification

Added `skill-studies/sweeping-stale-references/HANDOFF.md` and routed to it from the active plan. It identifies authoritative documents, current artifacts, preserved observations, runner interfaces, settled decisions, superseded work and the exact next format task. The proposed first baseline batch is the semantic original/no-target pair; it remains unapproved for dispatch. The protocol explains carrying cumulative effort into a new session without requiring the old conversation log.

Fresh verification: 8 score-format checks pass; 191 manifest and 23 current qualification hashes match; both unrun case pairs load with unchanged subject configuration identities. The original pilot-02 primary and backup match all 55 retained files each; disposable replay again confirms links, preservation, the complete committed repair and both export working directories. All 101 local Markdown link targets in the checked changed documents/handoff resolve. Hook suite passes (263 passed, 3 skipped). No paid model calls, old assessment mutations or core skill changes. The next session needs no scratch helper script; operational commands and identities are in the versioned format/case documents and manifests.

DD-VERDICT: PASS

## Bounded format pass for owner review

The `1-draft` companion proposal now supplies protocol/case templates, a filled semantic-delivery F1 card, manifest/index JSON templates and a comparison template alongside the retained score format.
Reviewed against the active plan, general spec, SSR policy and existing runner interfaces for consistency, executability, provenance durability and necessity.
The review checked every artifact role, criterion field, condition applicability, setup/score separation, unknown evidence, partial attempts, retry accounting, frozen-source preservation and reassessment relationships.
Clarified immutable protocol snapshots and acyclic hashes, precise score/index relationships, and the distinction between runner test IDs and study case/condition IDs.
No runner/schema implementation or proposed baseline dispatch is part of this format pass; owner format agreement and explicit migration remain open.

Removed the remaining calibration-pending limit from unrun semantic-delivery `expected.json` and refreshed its manifest identity.
The manifest records the prior qualification's scope explicitly: fixed facts, semantic criteria, policy, subject bytes and retained observations are unchanged.
Historical pilot records, score/example bytes and superseded workflows remain intact.

Verification: 8 score contract checks, 12 semantic controller tests and 263 hook tests pass (3 hook skips).
All 191 current case-manifest identities and 9 score source/evidence hashes match; evidence IDs resolve, all four prepared configs load and exclude controller scoring material, and policy copies match.
The unchanged score schema accepts an in-memory functional-only control structure; this is a structural probe, not a newly saved control assessment.
The final check resolves 116 local Markdown links/anchors in the changed/new documents; JSON parses and whitespace checks pass.
Self-review only, with no additional model calls or independent-review claim.

No findings.

DD-VERDICT: PASS

## Claude format review: pinned index preservation

The owner supplied Claude's independent review: PASS, with one P3 concerning a pinned hash of the live pilot-02 run index.
The owner subsequently directed one canonical accepted run record with Git providing history.
The example index now identifies the pinned run index by full Git commit, repository path and SHA-256; the score and live pilot indexes remain unchanged.
An earlier uncommitted duplicate snapshot was removed in favor of Git history.
The format contract, instructions, spec and active plan now state that accepted records are committed before correction; separate historical files and extensive amendment ledgers are unnecessary.
Git-backed preservation applies to committed repository artifacts; full raw bundles retain their existing external storage policy.

Verification: the pinned bytes resolve through Git and match the recorded size/hash, including under a simulated future live-index amendment; the existing score bytes/hash remain unchanged.
All 8 score-format checks pass; this documentation change introduces no runner code or model calls.
Remaining format decisions and version-1 migration stay open.

DD-VERDICT: PASS

## Accepted retention simplification

Applied the owner's accepted scope: one durable bundle and completeness inventory per actual run, a small index referencing runner metadata and one canonical score, and ordinary backups instead of mandatory duplicate local copies.
Reconciled the active plan/spec, companion contract, index/protocol templates, SSR storage policy and handoff; historical pilot records and copies remain unchanged.
Self-review checked failed attempts, unknown call charges, preservation failure, Git-backed citations and the distinction between durable storage and verified backup coverage.
The current ordinary backup arrangement is explicitly unverified; no backup system was configured or evidence deleted.
Verification: 8 format checks and 263 hook tests pass (3 skips); 118 local links/anchors resolve, the reduced index shape matches its contract, historical pilot indexes/score are unchanged and whitespace checks pass.
This is a format/documentation change, with no new runtime tooling or model calls.

DD-VERDICT: PASS

## Backup-state follow-up

The owner supplied Claude's follow-up confirming the Git-backed citation and smaller index, with a P2 that ordinary backup coverage is not operating for the evidence location.
Independently reproduced `tmutil destinationinfo` reporting no destinations and `tmutil isexcluded` reporting Included; Claude's broader agent/iCloud checks remain attributed to that review.
Corrected the protocol and generic wording to distinguish verified local preservation from host-loss recovery.
The owner then accepted single-host retention after the explicit host-loss explanation; the protocol records that decision without implying off-host recovery.
No system configuration or evidence was changed. Whitespace verification passes; the backup-state finding is closed by the accepted scope.

DD-VERDICT: PASS

## Live-protocol accounting cleanup

Addressed the owner-supplied Claude P3: replaced the booking chronology with one current entry, removed obsolete time-forecast tables and moved accepted format decisions beside their subjects.
The template now requires updating current accounting in place; Git retains prior checkpoints. Full seven-section migration remains pending.
The live protocol shrank from 435 to 377 lines; scoring-policy bytes, pilot indexes and the worked score are unchanged.
Verification: 14 incoming protocol links/anchors and outgoing targets resolve; accounting checks and 8 format tests pass; hook suite 263 passed, 3 skipped; whitespace clean.
No model calls or new authorization. Self-review found no remaining issue in this bounded cleanup.

DD-VERDICT: PASS
