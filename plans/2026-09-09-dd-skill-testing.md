# DD skill testing: current state and next step

**Status:** Installation and baseline tooling are settled for the current Codex and Claude local workflows.
The accepted CW evidence and completed-plan cleanup are consolidated on `main`; ongoing testing work uses this primary checkout.
Current work: the next five CW observations are prepared and reviewed; committing/pushing the status notes and executing the batch await owner approval.
This is the single active testing plan; the [validation guide](../skill-validation/README.md) indexes the durable contracts and execution instructions.

**Goal:** A repeatable set of tests for each DD skill’s discoverability, effectiveness and composition, with distinct questions and observable scoring criteria.
Use as many cases as the obligations require; neither a minimum count nor retaining every historical test is a goal.
The [charter](../skill-validation/charter/core-contracts.md) supplies core intent, the existing skill supplies detailed promises, and the accepted [coverage policy](completed/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-methodology-decision-shared-test-categories-and-coverage) supplies the common categories.
The [intended-use and authoring guidance](../skill-validation/README.md#intended-use-and-dependencies) records the owner's development-first context, broader uses, varied composition requirements and Superpowers writing-skills workflow.
All nine baseline DD bodies were read for the [composition map](../ARCHITECTURE.md#composition-boundaries); this did not evaluate their other catalogs or rewritten versions.
CW remains the recommended first pilot because ordinary source-to-prose tasks exercise its own complete procedure without the DD parent, with existing specification and evidence available.
Focus first on its leaf discovery/effectiveness coverage, then its bounded composition cases; conditional pairings remain part of the specification, and full validation of their owning skills is not a prerequisite to CW's leaf tests.

## Baseline specification before testing

The owner clarified that the current skill is the source of its detailed behavioral specification, not merely an implementation judged against a short charter or a desired future rewrite.
Follow the [baseline-specification-first method](../skill-validation/README.md#baseline-specification-first).
The [reviewed CW specification](specs/2026-09-10-cw-baseline-specification.md) records the exact baseline source and extracts its scope, rules, exceptions, method and companion boundaries; the owner authorized proceeding to catalog evaluation.
The [completed catalog audit](../skill-validation/pilot/cw-catalog.md#routine-suite-coverage) recommends a disposition for all 22 historical purpose variants and six subsequent packages, and maps every specification obligation to proposed coverage or an explicit evidence limit.
Its proposal retains ordinary cases, replaces mismatched discovery expectations, retires authoring/extraction tasks from routine CW coverage and adds uncertain-framing plus two named-companion composition cases.
The owner authorized preparing the 18-purpose proposal: 12 effectiveness, four discoverability and two composition cases.
Following input review and remediation, the owner authorized committing and pushing the prepared tasks.
Input and scoring review are complete, and the approved ten-call scoring pilot below is collected and assessed.
Its exact-command approval is exhausted; additional collection requires a new evidence decision and approval.
Earlier observations remain evidence under their recorded contracts; neither their collection nor the retrospective corrections establish a completed baseline against this new specification.

### Resuming this work

The specification-first decision above is settled methodology for every DD skill, not an open CW-only proposal.
The question is how effectively the existing skill fulfills its actual promises; the charter supplies core intent, and the complete skill supplies specifics and exceptions.
An extraction error calls for correcting the specification or test; a demonstrated failure to fulfill an actual promise is evidence about the skill.
Desired new behavior requires an explicit specification change before evaluation.
Continue from the reviewed CW specification, catalog and scoring rather than reopening those stages without a concrete mismatch or new evidence.
Use the next small batch to test remaining distinct boundaries; tooling is settled unless an observed mechanical gap requires a change.

On the same machine, resume in this primary checkout on `main`, read `AGENTS.md` → `CLAUDE.md`, then this plan and the linked next-batch summary; verify actual Git state before acting.
The latest completion/preparation and handoff notes are local uncommitted documentation changes pending commit/push approval.
Recent raw observations and preparation packages under `/private/tmp` are retained local evidence, not a durable Git backup or cross-device handoff; do not delete them or assume their links alone preserve their contents.
The repository contains the methodology and current decisions; continuity must not depend on conversation memory being available in another app.
No new test calls, historical rescoring, evidence promotion or candidate adoption follow from moving interfaces.

## Owner clarification: CW effectiveness and readability

The owner authorized rescoring the latest 18 routine observations on 2026-09-10.
The [charter](../skill-validation/charter/core-contracts.md#concise-writing) now owns the whole-document effectiveness/readability promise; the [runbook](../skill-validation/pilot/cw-runbook.md#routine-suite-assessment) owns comparative assessment and the [six routine rubrics](../skill-validation/pilot/cw-catalog.md#routine-input-map) express reader outcomes.
That retrospective reassessment changed no categories or suite membership; the later catalog audit proposes coverage changes separately.

All 18 observations have separate rescored worksheets linked from `/private/tmp/skilltest-cw-routine.c81p4an9/summary.md`, with the revised evaluation inputs frozen in that package.
The original inputs, rubrics, worksheets, schedule, collection audit and summary remain preserved; the accepted 99/66-run comparison and historical records are unchanged.
This reassessment follows inspection of the outcomes, so it is retrospective interpretation rather than fresh validation under a predeclared contract.

All three CW-03 guides and CW-18/current-DD and candidate now pass CW semantics under whole-document assessment.
The owner's repetition correction prompted a check of the exact supplied baseline CW body: emphasis and retention do not require new information, and uncertain framing must not be treated as a demonstrated failure.
The latest CW-18 worksheets remove repetition-only failure grounds in both candidate and no-DD; no-DD still fails for content-free introductory narration.
CW-20/current-DD already passed semantics; its overall verdict is corrected because narration is fidelity, not a blocking CW failure.
Remaining CW failures concern lost warning rationale, an unsupported reservation policy, residual padding and an added handoff deadline; the worksheets distinguish these from readability gains and correct operational content.
Owner review of those judgments remains open; there is no automatic evidence promotion, new collection, skill edit or adoption.

## Completed work

| Work | Result and durable home |
|---|---|
| Copy installer | Copies whole shipped skill folders into `.claude/skills` or `.agents/skills`, replacing same-name skills and preserving unrelated consumer files/history. Implemented on main and applied to both Steno installations. [Completed spec](completed/specs/2026-09-09-copy-based-installer-design.md). |
| Runner and worksheets | The same configuration, run bundles and model-scored worksheets support Codex and Claude. No campaign manager or automatic semantic scorer. [Runner](../skill-validation/runner/README.md), [methodology](completed/specs/2026-09-02-skill-testing-methodology-design.md). |
| Controlled-input qualification | Codex controls and the procedure pilot are complete. Claude’s native catalogs/loading, companion access, seven local tools, file/Git work and capture/cleanup passed scoped qualification. [Qualification reference](../skill-validation/pilot/qualification/README.md), [completed Claude spec](completed/specs/2026-09-09-claude-skill-testing-design.md). |
| Historical records and procedure pilot | All 105 historical records and 14 procedure observations are preserved. These are not matching-input controls for the later CW comparison. [Historical catalog](../skill-validation/scenarios/README.md), [accepted pilot package](../skill-validation/accepted/procedure-pilot/codex-gpt-5.6-sol-low/README.md). |
| CW baseline | Owner-accepted: 99 observations covering 22 purpose-separated variants, current-DD and meaningful no-DD conditions, Sol medium. [Accepted baseline](../skill-validation/accepted/concise-writing/codex-gpt-5.6-sol-medium/README.md). |
| Existing CW candidate comparison | All 66 observations are collected, scored and audited under unchanged criteria; their validity is owner-accepted. Further interpretation remains open and the candidate is not adopted. [Accepted candidate package](../skill-validation/accepted/concise-writing/codex-gpt-5.6-sol-medium-candidate/README.md), [comparison contract](completed/specs/2026-09-07-cw-validation-design.md). |
| Previous coverage and initial pass | The earlier approved 18-purpose proposal had 11 effectiveness, five discoverability and two composition cases; six changed/new packages produced the retained initial observations. The specification-based [coverage proposal](../skill-validation/pilot/cw-catalog.md#proposed-routine-portfolio) now supersedes that proposal for review, without changing historical evidence. |

## Retained and deferred work

Keep `docs/comprehensive-skill-cleanup` and its worktree active at `13599fb7d3127334b0d07bfe468767e586ec5f9c` as a source of candidates after methodology settles.
Only its unchanged CW snapshot has undergone the completed comparison; no other rewritten skill is evaluated or adopted here.
The CW collection history and accepted evidence are integrated on pushed `main`; its local/remote branch and worktree are retired.
Its complete `.claude` DD log/state history is copied and hash-verified under `/private/tmp/dd-cw-retirement-5qvesacx/`; retain that package alongside the original validation scratch.

- Strict universal input isolation was replaced by scoped controls and disclosed common-input/hidden-provider limits; do not restart that project.
- [Campaign/baseline organization](deferred/2026-09-03-skill-validation-baseline-design.md), [all-skill catalog repairs](deferred/2026-09-07-skilltest-discovery-behavior-catalog-separation.md), larger model/effort matrices and [older hook/skill proposals](deferred/2026-07-17-dd-skills-backlog.md) remain deferred.
- The parked hook-fix history remains at remote tag `archive/2026-09-09-pre-pr-review-false-positives`, with a recovery bundle under `/private/tmp/dd-testing-cleanup.b9v_1z7g/`. Archiving did not resolve its unmerged review findings.
- Original CW, candidate, pilot and Claude qualification scratch packages remain retained for review. Evidence validity acceptance does not authorize adoption, rescoring, deletion or new provider calls.

## Remaining work

- [x] Draft the CW baseline specification from the exact existing skill and charter, and identify mismatches in the existing catalog without implementing new scenarios.
- [x] Review the CW specification against the complete baseline skill and obtain owner authorization to proceed to catalog evaluation.
- [x] Reevaluate the full CW catalog against that specification, covering retained, replaced and diagnostic purposes; propose gap remedies and consolidations in the existing mapping.
- [x] Obtain owner authorization to prepare the coverage proposal.
- [x] Prepare and internally review the agreed task inputs, including representative standalone CW conditions and DD-guided development composition with required Superpowers available.
- [x] Complete input review and remediation and obtain owner authorization to commit/push the prepared tasks; this does not establish measured coverage or skill effectiveness.
- [x] Define and reconcile scoring from the reviewed specification and catalog; complete the initial scoring-usability pilot.
- [x] Review the pilot judgments and select the next distinct coverage gaps.
- [ ] Complete the additional evidence needed to establish baseline effectiveness; a small coverage batch does not establish reliability or the complete portfolio.
- [x] Consolidate completed plans and preserve the accepted evidence packages without changing judgments.
- [x] Implement the copy installer and update Steno’s `.claude` and `.agents` installations.
- [x] Complete and qualify Claude support through the existing runner and worksheets.
- [x] Add a blank `Test category / supporting purpose` worksheet field and document the five labels for the evaluator; retain existing configuration and accepted evidence unchanged.
- [x] Agree the earlier routine CW suite, identifying every retained, retired, replaced and new case and its observable scoring boundary. Its separately reviewed specification-based successor is recorded above.
- [ ] Evaluate what the accepted CW comparison supports and what remains uncertain before any skill-change or adoption decision.
- [x] Document the clarified CW contract in its durable homes, reconcile the six affected routine rubrics and rescore all 18 latest observations separately from their original judgments.
- [ ] Revisit earlier scored outcomes after specification, catalog coverage and scoring are settled; preserve all prior judgments meanwhile.
- [x] Prepare and review CW-03/13/14/17/18 replacements and CW-20 restraint inputs, update the existing catalog/runbook, and check the distinct response-generation and restraint criteria. All completed-comparison inputs are preserved; no runner code or skill edits.
- [x] Obtain owner review of the six exact input packages; approval was given after commit `6867030`.
- [x] Approve and execute a separately frozen initial evidence pass. The completed Codex / Sol medium batch covered only CW-03/13/14/17/18/20: no-DD, current-DD and unchanged candidate, one observation each (18 calls). This reduces the first commitment while exposing real scoring/task issues; it does not establish consistency. Further repetitions require a decision-specific sampling choice and separate approval, retaining these initial observations. The other 12 routine cases remain historical context rather than fresh observations.

### Current input preparation

Use new `specification/` packages beneath the existing CW scenario directories, with their task inputs linked from the catalog.
This keeps the earlier prompts/rubrics recoverable without introducing another tracking system.

- [x] Prepare CW-02/04/08 context/structure repairs, CW-13/14 authoring-scope discovery inputs and CW-21 uncertain framing.
- [x] Prepare CW-22 plan/rationale and CW-23 linked-document fixtures with explicit work boundaries and actual required guidance available.
- [x] Map all 18 purposes to exact task inputs and declare representative standalone conditions without duplicating the suite.
- [x] Review source fidelity, scope observability, companion dependencies and input consistency; run provider-free verification and present the inputs for owner review.
- [x] Address the follow-up review: provide CW-22's unchanged comparison copy, align its design's input-stability assumption, and make CW-23's comparison/commit setup compatible with the existing adapters' empty Git boundary.

No scoring changes, runner changes, skill edits, evidence changes or provider calls belong to this preparation step.
Execution configurations and a frozen collection package follow agreement on task inputs and scoring.
The [prospective input map](../skill-validation/pilot/cw-catalog.md#prospective-input-map) links the reviewable tasks and fixture conditions.
Provider-free previews, frozen source copies, checks and review notes are retained in [/private/tmp/dd-cw-specification-inputs-n_sfodg5/summary.md](/private/tmp/dd-cw-specification-inputs-n_sfodg5/summary.md).
The [corrected composition previews and probes](/private/tmp/dd-cw-specification-inputs-n_sfodg5/review-1/summary.md) supersede the earlier CW-22/23 previews; the other task previews are unchanged.
The checks exercise both native path layouts, matching control inputs, file comparison and a disposable Git index/commit sequence; they are not model observations or a provider schedule.

### Current scoring preparation

The owner approved simplifying the draft and improving evaluation before further collection.
Use evaluator-only rubrics under each case's `specification/` directory, with CW-01/18 discovery in its `discovery/` subdirectory; the [input map](../skill-validation/pilot/cw-catalog.md#prospective-input-map) links all 18.
The [shared rules](../skill-validation/pilot/cw-runbook.md#prospective-scoring) define grouped results, source checklists and readability evidence using the unchanged worksheet generator.
Record shared provenance once per collection summary, inspect prose before condition labels where practical, then verify the trace and compare matching control outcomes.

- [x] Draft and internally review all 18 source-grounded rubrics and verify compatibility with the existing worksheet generator.
- [x] Simplify scoring and repeated boilerplate while preserving concrete source checks and separate companion ownership.
- [x] Propose the [six-purpose first collection](../skill-validation/pilot/cw-catalog.md#initial-pilot-selection) and a repeat assessment of two future observations; retain all other purposes without requiring every case in every batch.
- [x] Mark CW-21's uncertainty coverage provisional, with repair/replacement considered if that behavior is not observed.
- [x] Review all edited documents, address findings and reverify preservation, links and worksheet compatibility.
- [x] Complete owner review of the revised scoring and obtain authorization to commit/push.
- [x] Prepare the initial 10-call proposal: Codex / gpt-5.6-sol / medium, one observation per condition across the six selected purposes.
- [x] Obtain approval for the ten exact commands and committing/pushing the preparation note.
- [x] Execute and assess the approved batch after the clean-checkout and frozen-input checks; retain both selected repeat assessments.
- [x] Obtain owner review of the new evidence and scoring judgments before expanding collection.

This smaller first collection checks whether scoring is usable before investing in wider coverage; it does not establish baseline reliability or approve candidate comparison.
The [completed scratch package](/private/tmp/skilltest-cw-pilot-1eqpbvg1/summary.md) links all ten observations, frozen inputs, full traces, worksheets and the final audit.
All calls completed without infrastructure retries; the exact-command approval is exhausted.
Eight semantic results pass; the no-DD CW-20 notice adds a confirmation deadline, and the no-DD CW-22 plan loses rationale/context and weakens a required test.
CW-03/current-DD passes semantics with a separate delivery-preface failure.
CW-13's final proposal correctly excludes CW after correcting its initial selection; preserve that distinction for owner review.
The two retained repeat assessments agree on semantic results, fidelity and readability; this same-evaluator check does not establish independent agreement or skill reliability.
Sol medium keeps the provider/model/effort consistent with the prior CW comparison while testing the new scoring and supplied context; it does not reuse those observations.
The earlier [draft review](/private/tmp/dd-cw-scoring-review-kowdw1x0/summary.md) remains retained; [simplification review](/private/tmp/dd-cw-scoring-streamline-w12bzsmf/summary.md) records the current verification.
Approved prompts, fixture declarations, skill bodies and retained evidence remain unchanged.
The repeat assessments use only CW-03/current-DD and CW-22/current-DD from this new batch and preserve both judgments; historical evidence remains unchanged.
The owner agreed the scoring is usable and authorized moving to the next coverage preparation; a passing control is valid evidence and no control failure is required.
Evidence remains scratch-only, with no automatic promotion, further calls or candidate adoption.

### Next coverage preparation

Prepare five calls from existing tasks/rubrics, one observation per condition, Codex / gpt-5.6-sol / medium:

- CW-18 discoverability: current-DD only; implicit prose creation without a tightening request.
- CW-21 effectiveness: no-DD and current-DD; uncertain framing. If uncertainty is not expressed, record keep-and-flag as unobserved rather than claiming coverage or manufacturing a failure.
- CW-23 composition: no-DD and current-DD; preserve the restart guide and reconcile linked documents in one local fixture commit.

These exercise distinct remaining boundaries before broader sampling; no candidate, repetitions or additional scoring self-check is scheduled.
The [preparation package](/private/tmp/skilltest-cw-next-_24fuk1d/summary.md) links rendered inputs, exact proposed commands and qualification evidence.
Codex changed from 0.153.4 to 0.154.0, including built-in OpenAI documentation guidance; keep this provenance separate from the earlier pilot.
The DD and Superpowers snapshots and runner are unchanged. Fresh provider-free catalog, surrogate-profile/ancestor and local file/Git checks cover the affected controls.
The first approved CW-18 call also checks the new CLI's actual execution, capture and cleanup; inspect that evidence before proceeding to the remaining calls. A missing control stops the batch without authorizing extra calls.

- [x] Finish provider-free preparation and review of all five exact commands; local input/control checks and 263 hook tests passed (three skipped).
- [ ] Obtain approval to commit/push the reviewed preparation notes and execute the new five-call batch.
- [ ] Collect and assess each approved observation, checking complete traces and actual file/commit state; retain valid control passes and failures alike.

No provider calls are authorized by preparation. The previous ten-call approval remains exhausted.

### Retained earlier routine evidence

The [routine input map](../skill-validation/pilot/cw-catalog.md#routine-input-map) links the six packages used in the initial pass; the proposed portfolio and full audit are above it in the same catalog.
Provider-free preparation evidence remains in `/private/tmp/dd-cw-routine-inputs-6gx080gt/summary.md`; it exercises no-DD/current-DD/candidate assembly, not a new provider schedule or skill-effectiveness claim.
All 18 observations are collected, scored and mechanically audited with no infrastructure retries. Their evidence remains scratch-only pending owner review. The exhausted command batch, worksheets, full traces, frozen inputs and qualification reconciliation are retained under `/private/tmp/skilltest-cw-routine.c81p4an9/summary.md`; the superseded 54-call proposal is preserved under `prior-54-proposal/` in that package and authorizes no calls.
The initial-pass preparation verified Codex's executable against the completed comparison and checked the selected catalogs/common inputs.
That preparation recorded Claude `2.1.267`, newer than its qualification at `2.1.266`; any future collection requires checking the then-selected executable and reconciling affected controls.

Original rubrics still define their frozen records; the separate retrospective worksheets apply the clarified contract without replacing those records.
The exact 18-call approval is exhausted; further interpretation of these older observations remains a separate decision now that specification, coverage and scoring review are complete. No automatic repetitions, promotion or candidate adoption follow. The scratch summary reports the original and revised judgments with separate CW prose, authoring authority, task fidelity and comparative readability evidence.
Retain ordinary cases even when a particular no-DD model passes them; the owner’s experience of model verbosity is context, not a measured cross-provider result.
Once an agreed CW suite works end to end, follow the [per-skill starting workflow](../skill-validation/README.md#starting-the-next-skill) for the next owner-selected skill; a complete nine-skill campaign is not a prerequisite to finishing CW.
