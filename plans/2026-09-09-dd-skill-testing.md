# DD skill testing: current state and next step

**Status:** Installation and baseline tooling are settled for the current Codex and Claude local workflows.
The accepted CW evidence and completed-plan cleanup are consolidated on `main`; ongoing testing work uses this primary checkout.
Current work: CW-01/18/19 collection and scoring are complete; all 18 purposes now have judgeable initial evidence.
The final batch has five passes and one CW-19/current-DD preservation failure; owner review identifies lost execution responsibility, change-ticket context and operational clarity in the revised runbook.
The four-case independent scoring check is complete; the fresh grader missed CW-19's preservation failure and CW-14's separate proposal-fidelity failure.
The owner authorized repeating the same four-case check with a stronger model; Opus 5 preparation is underway with unchanged prompts and medium effort.
Original and owner-revised judgments remain unchanged.
Both CW-05 conditions separately fail the output-only request by emitting progress messages.
CW-14 separately fails proposal fidelity for omitting the selected authoring method’s observed-failure gate.
The preceding approved-design CW-23 pair completed the edit and commit in both conditions; both results are judgeable.
After owner review, preservation and economy pass in both; reference reconciliation/accounting fails in no-DD but passes in current-DD.
In that CW-23 pair, current-DD is PASS overall; no-DD remains FAIL for missing substantive reference accounting.
The prospective run verdict is now `RUN_NOT_JUDGEABLE`; earlier records retain their original `SCENARIO_INVALID` labels.
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
Keep all skill bodies unchanged while establishing the tests and consistent scoring; skill wording changes remain deferred.
Capture the readability and useful-repetition allowance in the specification and shared rubric instructions, then apply it to scoring rather than treating an evaluator error as a reason to rewrite the skill.
Use the next small batch to test remaining distinct boundaries; tooling is settled unless an observed mechanical gap requires a change.

On the same machine, resume in this primary checkout on `main`, read `AGENTS.md` → `CLAUDE.md`, then this plan and the linked next-batch summary; verify actual Git state before acting.
The reviewed preparation notes were committed and pushed before the approved batch; its scratch package records the clean launch revision and session approval.
Continue from the [CW-01/18/19 final coverage batch](#cw-011819-final-coverage-batch), preserving every preceding package and its original and revised judgments.
Both two-call approvals are exhausted; do not resume/replay those observations or execute the original unrun fifth command.
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

The owner approved five calls from existing tasks/rubrics, one observation per condition, Codex / gpt-5.6-sol / medium:

- CW-18 discoverability: current-DD only; implicit prose creation without a tightening request.
- CW-21 effectiveness: no-DD and current-DD; uncertain framing. If uncertainty is not expressed, record keep-and-flag as unobserved rather than claiming coverage or manufacturing a failure.
- CW-23 composition: no-DD and current-DD; preserve the restart guide and reconcile linked documents in one local fixture commit.

These exercise distinct remaining boundaries before broader sampling; no candidate, repetitions or additional scoring self-check is scheduled.
The [collection package](/private/tmp/skilltest-cw-next-_24fuk1d/summary.md) links frozen inputs, exact commands, qualification, all four attempted observations and their worksheets.
Codex changed from 0.153.4 to 0.154.0, including built-in OpenAI documentation guidance; keep this provenance separate from the earlier pilot.
The DD and Superpowers snapshots and runner are unchanged.
The first CW-18 call passed the required live execution, capture, input-provenance and cleanup checkpoint; all four attempts matched the qualified 60-file built-in guidance map.

- [x] Finish provider-free preparation and review of all five exact commands; local input/control checks and 263 hook tests passed (three skipped).
- [x] Obtain approval to commit/push the reviewed preparation notes and execute the new five-call batch.
- [x] Collect and assess CW-18 discovery and the CW-21 pair; retain the fourth attempt as invalid and pause before call 5 on the failed Git control.
- [x] Obtain owner authorization to continue the bounded fixture Git-write repair.
- [x] Verify a workspace-based profile with a write grant for the exact disposable fixture `.git` path and explicit read-only rules for protected directories elsewhere.
- [x] Test-first update the Codex adapter and provider tests, add a provider-free installed-CLI acceptance check, and reconcile the runner README.
- [x] Qualify staging, original-source diff, linked-document reconciliation and one root commit through the emitted policy; verify protected-path write denials and network-bind denial in fresh surrogate fixtures.
- [x] Review the repair and freeze two replacement CW-23 commands with unchanged task/skill/scoring inputs.
- [x] Obtain approval for the two replacement calls and collect both after the first-call infrastructure checkpoint passed.
- [x] Assess both as `SCENARIO_INVALID`: design approval requested, with no revised artifact or local commit.
- [x] Obtain owner approval for an explicit approved-design premise in the common CW-23 prompt and the prospective `RUN_NOT_JUDGEABLE` label.
- [x] Prepare and review a fresh no-DD/current-DD pair with that premise under the owner’s retry request and approval.
- [x] Collect the two fresh calls serially after the first-call live-control checkpoint; assess and review their retained evidence.
- [x] Review the fresh pair with the owner before selecting further collection; the owner corrected its economy judgments and approved the next coverage batch. Evidence promotion remains unapproved.

CW-18 passed discovery with complete CW access before file creation; extra progress messages failed its brief-completion-only fidelity requirement.
Both CW-21 outputs preserve operating facts and remove clear padding, and both express unresolved uncertainty about the training cue.
The no-DD control removes the cue and fails keep-and-flag; current-DD retains and flags it, passing all applicable groups.
The conditional behavior was observed, so the provisional unobserved-uncertainty rule does not call for task repair on these results.
This is one observed difference under the supplied bundle, not isolated causation or established reliability.

CW-23/no-DD stopped before editing when `git add` could not create `.git/index.lock`.
The runner completed and captured the blocker, but unchanged documents, an empty index and no commit leave the intended composition interaction unjudgeable: `SCENARIO_INVALID`, not a CW failure or an unchanged-command infrastructure retry.
The [diagnosis](/private/tmp/skilltest-cw-next-_24fuk1d/git-control-failure.md) shows that the preparation probe ran Git directly on the host; it did not establish the subject sandbox's Git-write capability.
A provider-free probe through the current built-in workspace profile reproduced ordinary-file writes succeeding while Git staging was denied.
The evidence establishes a concrete qualification gap, not when the restriction changed or a need to reopen CW methodology.

Call 5 remains unrun; the original batch stopped without retries, extra model calls or execution-policy changes.
The owner authorized the narrow repair after reviewing the failure; its [repair and replacement package](/private/tmp/skilltest-cw-git-repair-c7bwwsv7/summary.md) retains scope, provider-free evidence and the two exact commands.
That repair changed the fixed Codex adapter policy while preserving scenario inputs, scoring and the runtime’s rejection of preexisting fixture `.git` entries.
Use an exact path grant to avoid granting Git writes in sibling evidence or other repositories; unsupported profile syntax must fail without a broader fallback.
Provider-free checks passed the complete Git/link path for both unchanged CW-23 fixtures, with all supplied skills and project guidance unchanged.
Native catalogs match the earlier conditions, paired common messages match after declared DD entries and allocated paths are normalized, and all 60 built-in guidance hashes are unchanged.
The current CLI’s custom-profile inheritance did not retain built-in protected-directory exclusions in a differential sandbox probe; explicit `.git`, `.codex` and `.agents` read-only rules preserve them, with only the exact fixture Git override writable.
The separate installed-CLI check exercises protected-path writes and network binding; these are bounded controls, not a claim of exhaustive filesystem isolation or model effectiveness.
The owner approved the frozen replacement pair; both calls completed with verified inputs, retained emitted streams and verified runtime cleanup, without retries or extra calls.
No-DD successfully staged originals, then requested design approval; current-DD loaded all required DD/CW/SSR bodies but requested design approval before staging.
Neither edited the guide, changed navigation or committed, so all three semantic groups are `NOT_JUDGEABLE` and both runs are unjudgeable; the task-completion failures remain visible separately.
The second trace’s compound-read event exposes only trailing Git output; complete required DD/CW/SSR body access is verified in its earlier event, but later body reads are not independently confirmed.
Both conditions stopped at a design gate, leaving no CW-23 semantic comparison; this does not establish a DD benefit or regression.
The owner subsequently approved the task clarification below; the reviewed CW specification and scoring criteria remain intact.
The pair’s two-call approval is exhausted; any task change or further collection needs a reviewed proposal and fresh approval.
All new evidence remains scratch-only pending owner review, with no historical rescoring, promotion or adoption.

### CW-23 approved-design preparation

The owner accepted `RUN_NOT_JUDGEABLE` as the prospective run verdict, with the same conditions and precedence as `SCENARIO_INVALID`; historical labels and frozen judgments remain unchanged.
The revised common task explicitly states the approved edit design and directs execution; both conditions receive that paragraph, with their existing loading prefixes unchanged.
This addressed the observed approval hold without changing the CW specification, rubric, skills or requested documentation outcome.
The [fresh pair](/private/tmp/skilltest-cw-approved-design-ikjawbad/summary.md) freezes two serial calls, no-DD then current-DD, on Codex CLI 0.154.0 / gpt-5.6-sol / medium under the repaired Git policy.
The owner’s retry request and approval cover this pair; its expanded commands and authorization are retained in the package.
Provider-free checks verified both rendered prompts, all fixture bytes, withheld evaluation inputs, 85 frozen inputs, 46 unchanged runner files, and the unchanged CLI version/digest.
Of 68 supplied files, 66 match the previous pair byte-for-byte; only the two condition prompts gain the approved common paragraph.
Prior fixture capability qualification remains applicable because the CLI, policy and all fixture/skill bytes are unchanged; the first-call live-control checkpoint still applies.
Both calls completed with exit 0 and no infrastructure error; 163 artifact files, both 60-file live bootstrap maps and private-runtime cleanup verified.
Both created one local commit containing only the three project documents, and all four links resolve in each committed tree.
Preservation and economy pass in both after the owner identified useful reader orientation in their introductory sentences.
The initial economy failures treated removability as proof of padding; the [owner-review correction](/private/tmp/skilltest-cw-approved-design-ikjawbad/owner-framing-review.md) applies the existing framing allowance, preserving original and revised worksheets separately.
The specification now explicitly distinguishes useful framing from indispensability; the shared [padding-failure check](../skill-validation/pilot/cw-runbook.md#padding-failure-check) requires a contextual reader-function justification before an economy failure, with this case as calibration.
CW-23's rubric links that check. These prospective evaluator clarifications preserve the skill and historical frozen inputs; improved scoring consistency has not yet been measured.
Current-DD passes SSR reconciliation/accounting with ten independently reconcilable occurrences across six source lines; no-DD fixes navigation but omits substantive commit sweep accounting and fails SSR-I4.
The revised overall verdicts are current-DD `PASS` and no-DD `FAIL` for SSR-I4; both remain judgeable.
Both conditions pass the CW prose criteria; no added CW prose benefit is established.
The supplied bundle is associated with better reference accounting in this pair; one pair does not establish isolated causation or reliability.
The approved task premise reached execution in both conditions; the earlier approval holds remain preserved under their original contracts.
The pair’s approval is exhausted. Retain all results and successive owner-reviewed judgments scratch-only; no replay, historical rescoring or promotion follows.

### CW-02/04/14 coverage batch

The owner approved five serial calls using the existing reviewed tasks and current shared scoring, Codex / gpt-5.6-sol / medium, one observation per condition:

- CW-02 effectiveness: no-DD then current-DD; retry scope, rationale and usable ordering navigation.
- CW-04 effectiveness: no-DD then current-DD; simpler structure with useful warning/recovery lookup.
- CW-14 discoverability: current-DD only; exclude CW from shipped reference authoring while selecting the applicable authoring method.

The [collection package](/private/tmp/skilltest-cw-structure-7fbp_ugd/summary.md) freezes all five commands, task/configuration bytes, selected rubrics and the clarified specification/shared padding check.
All 60 DD/Superpowers source files match the preceding qualified contexts; the 46 runner files, CLI 0.154.0 and executable digest remain unchanged.
The fixtures contain only supplied skills, so the prior plain-context native availability qualification applies; there are no project instructions or writable task outputs.
All five tasks require read-only work, including unchanged Git state; the existing fixture Git capability grants no task authorization to mutate it.
The first call passed its live-control checkpoint before call 2; all five observations verified actual policy, input/capture and 60-file built-in provenance, read-only state and private-runtime cleanup.
Keep every observation and original judgment; no candidate, skill edit, extra call, historical rescoring, evidence promotion or extra scoring self-check is included.
These cases extend distinct coverage; a single observation per condition does not establish reliability or isolated CW causation.

- [x] Freeze and review the approved five-call preparation using the existing runner and previously qualified contexts.
- [x] Obtain owner approval for this batch and session commit/push workflow.
- [x] Collect the first call and pass its live-control checkpoint before the remaining four.
- [x] Collect and assess all five observations; review results and reconcile coverage before selecting further collection.
- [x] Review these results with the owner before selecting the next bounded batch; the owner approved CW-05/06/08 after discussing the interpretation limits.

Both CW-02 conditions preserve retry limits, per-delivery scope/rationale, synchronous ordering and usable navigation while removing clear duplication.
Both CW-04 conditions preserve session timing and recovery, collapse unnecessary structure and retain the repeated warning input rule for useful point-of-use recall.
All four pass preservation/economy; the pairs show no material DD task-success advantage.
CW-14 reads CW and explicitly rejects it for reference authoring, passing the scope boundary.
Its proposed writing-skills workflow tests before drafting but omits the required observed baseline failure before editing, so proposal fidelity fails separately; no authoring lifecycle was executed.
All five runs remain judgeable overall PASS under the separate-ledger rules.
The [collection audit](/private/tmp/skilltest-cw-structure-7fbp_ugd/collection-audit.json) verifies five unique serial calls, no retries, five worksheets, 292 artifact-entry hashes, frozen inputs and cleanup.

After the CW-02/04/14 batch, judgeable evidence covered 12 of 18 purposes: effectiveness CW-02/03/04/17/20/21, discovery CW-01/13/14/18, and composition CW-22/23.
That inventory contains 20 judgeable observations plus three retained unjudgeable CW-23 attempts, without pooling their scores or claiming reliability.
After that batch, unobserved effectiveness purposes under the reviewed contract were CW-01/05/06/08/18/19; the next selection is below. Historical versions do not substitute for them.
This batch’s five-call approval is exhausted; preserve all results scratch-only and review them before selecting further collection.

### CW-05/06/08 coverage batch

The owner approved six serial observations using the existing reviewed tasks, rubrics and shared scoring, Codex / gpt-5.6-sol / medium, one per condition:

- CW-05 effectiveness: no-DD then current-DD; remove unsupported operational advice while preserving the authoritative archive facts.
- CW-06 effectiveness: no-DD then current-DD; trim inflated emphasis without weakening a universal requirement.
- CW-08 effectiveness: no-DD then current-DD; preserve eligibility exceptions, deadlines and usable sponsor/appeal routes in a fictional applicant handbook.

The [collection package](/private/tmp/skilltest-cw-policy-w_12rbzo/summary.md) contains the six exact commands, frozen task/configuration bytes and withheld evaluation sources.
All 60 supplied DD/Superpowers files, 46 runner files and CLI 0.154.0 executable bytes match the preceding qualified contexts.
Every task is read-only; no-DD supplies only the common Superpowers substrate, while current-DD adds the nine baseline DD bodies and explicitly loads CW.
The first call passed its live-control checkpoint before call 2; all six runs verified capture, actual policy, input and built-in provenance, read-only fixture/Git state and private-runtime cleanup.
Keep all results scratch-only, including judgeable failures, with no replay, extra observations, historical rescoring, evidence promotion, candidate adoption or skill edits.
Control passes are valid evidence; this single observation per condition extends coverage rather than establishing reliability or requiring a control failure.

- [x] Prepare and review six matching-input previews and frozen commands under the owner-approved session workflow.
- [x] Obtain owner approval for the six-call batch and preparation/results commit/push workflow.
- [x] Collect the first observation and pass its live-control checkpoint before continuing.
- [x] Collect and assess all six; review evidence and reconcile the remaining coverage.
- [x] Review these results with the owner; the owner authorized scoring clarifications before further collection.

Both CW-05 conditions remove the two unsupported recommendations and retain all archive facts; their extra progress messages fail the explicit output-only task boundary separately.
Both CW-06 conditions preserve universal key/header/rejection requirements while trimming inflated emphasis; they also obey the output-only instruction.
Both CW-08 conditions preserve eligibility exceptions, deadlines, sponsor duties and appeal routes, while retaining usable navigation.
No-DD repeats appeal timing/finality in the overview and detailed procedure, where it has useful orientation and point-of-action value; current-DD uses a pointer and keeps those details in Appeals.
All six are judgeable overall PASS; no material DD task-success advantage appears in these pairs.
Complete CW access is verified in each loaded condition, but the full available bundle and single observations do not establish isolated causation or reliability.
The [collection audit](/private/tmp/skilltest-cw-policy-w_12rbzo/collection-audit.json) verifies six serial calls, no retries, six worksheets, 345 artifact-entry hashes, 95 unchanged frozen inputs, six built-in maps and runtime cleanup.

After that batch, judgeable coverage included 15 of 18 purposes: effectiveness CW-02/03/04/05/06/08/17/20/21, discovery CW-01/13/14/18 and composition CW-22/23.
The inventory then contained 26 judgeable observations plus three retained unjudgeable CW-23 attempts; these are coverage counts, not a pooled score.
That left CW-01, CW-18 and CW-19 effectiveness unobserved; their subsequent approved collection is recorded below.
This batch's six-call approval is exhausted; every observation and judgment remains scratch-only.

### CW-01/18/19 final coverage batch

The owner approved six serial Codex / gpt-5.6-sol / medium observations, one per condition, after the scoring clarifications below:

- CW-01 effectiveness: no-DD, then standalone current-CW alongside Superpowers.
- CW-18 effectiveness: no-DD, then current-DD; create only the requested volunteer guide.
- CW-19 effectiveness: no-DD, then current-DD; revise the operational runbook read-only.

The [collection package](/private/tmp/skilltest-cw-final-p2sc4e3n/summary.md) retains the clarified common prompts, condition prefixes, matching source inputs, evaluator sources, exact commands and six completed worksheets.
The fresh provider-free native check verifies CW-01's standalone catalog and matching normalized context; unchanged full-bundle and sandbox controls reuse their recorded qualifications.
All 60 source files and 46 runner files match the qualified versions; 230 frozen files include the new qualification evidence.
The session authorization covers preparation/results review and commit/push, existing private-runtime authentication and necessary host/network execution permissions.
Before call 2, the first call passed checks of actual capture, inputs, runtime policy, built-in hashes, task mutation boundaries and cleanup.
Both actual CW-18 files were inspected directly; final-answer-only limits permit separate progress messages in all three tasks.
Compare successful pairs directly for reader value and no observed degradation without requiring CW to win; these single observations do not establish reliability.

- [x] Prepare six previews and qualify the standalone condition without provider calls.
- [x] Freeze and review the inputs, commands and bounded session authorization.
- [x] Commit/push preparation and record the clean launch revision before launch.
- [x] Collect and score six observations, retaining every result without replay.
- [x] Reconcile judgeable initial coverage across all 18 purposes.
- [x] Review results with the owner and obtain approval for the bounded independent scoring check below.

CW-01 and CW-18 pass preservation/economy in both conditions, with direct paired comparison supporting no observed degradation in task success and usability.
CW-18/current-DD condenses the one-token-at-closing example into the unused-token example and universal expiry/stop rules; the worksheet records why the practical lesson remains available from the complete guide.
CW-19/no-DD passes; current-DD fails preservation, while economy and fidelity pass.
The [owner-revised failure notes](/private/tmp/skilltest-cw-final-p2sc4e3n/worksheets/06-cw19-current-dd-owner-revised.md) record four shortcomings of the post-CW output: the release engineer is never named, the example identifier CHG-4821 is never introduced as a change ticket, the technically correct metric boundary statement becomes harder to read, and “Never add --force” loses its explicit reference to the promotion command.
The compressed stop condition makes readers reconstruct differently inclusive failure bounds; the warning's section placement supplies context but does not replace a clear command reference.
CHG-4821 is fictional test text; no real-ticket lookup is involved.
The numeric thresholds, shared readiness window, GO ordering and recovery conditions remain present, but that alone does not preserve operational readability.
The original assessment remains unchanged; the separate owner revision expands the failure rationale under the existing information/readability contract without changing scores, rubrics or skills.
These are judgeable output shortcomings with valid controls, not an infrastructure failure or permission to replay the run.

The [collection audit](/private/tmp/skilltest-cw-final-p2sc4e3n/collection-audit.json) verifies six serial calls without retries, 230 frozen inputs, 339 artifact-entry hashes, allowed output boundaries, all six built-in maps and runtime cleanup.
All six fidelity results pass under their clarified final-answer scope; original fidelity judgments remain unchanged.
The [coverage inventory](/private/tmp/skilltest-cw-final-p2sc4e3n/coverage-inventory.md) links 32 judgeable observations across 12 effectiveness, four discovery and two composition purposes, plus three retained unjudgeable CW-23 attempts.
Its counts describe initial purpose coverage, not a pooled score, repeated reliability or independent evaluator agreement.
The six-call subject authorization is exhausted; the separately approved independent scoring check below uses retained outputs with existing judgments withheld.

### Independent scoring check

The owner approved a fresh AI grader after reviewing the purpose and separation from this conversation.
The [completed package](/private/tmp/cw-independent-scoring-j4sxgwi0/summary.md) assessed four retained observations: CW-08/no-DD for useful repetition, CW-18/current-DD for condensed examples, CW-19/current-DD for preservation/readability, and CW-14/discovery for scope selection versus proposal fidelity.
Claude Opus 4.6 (`claude-opus-4-6`) at medium effort completed exactly two serial, no-tool evaluator calls.
The first received common source tasks, outputs and their original frozen scoring rules with neutral case labels; the second additionally received its own unchanged first assessment, full subject traces and factual mechanical evidence.
The discovery proposal reveals some condition information itself; stage 2 deliberately reveals loading and execution evidence.
Prior operator judgments and owner comments are withheld throughout, and each evaluator report is retained separately.
This targeted check tests agreement on meaningful cases; it does not establish statistical independence or population reliability.

The current Claude CLI is 2.1.268, with a frozen executable digest and fresh provider-free authentication, option-parsing, host-state protection and runtime-cleanup checks.
The scratch launcher reuses unchanged private-runtime code and disables tools, skills, MCP and customizations; it introduces no runner or skill change.
The first live report verified model identity, empty tool exposure, unchanged fixture and cleanup before the second stage; both stages passed these controls.
The package freezes 66 source/control files; stage 2's only dynamic grading input is the first report, hashed at its checkpoint.
No subject rerun, third evaluator call, automatic verdict replacement, evidence promotion or skill edit follows from this approval.

- [x] Select the four observations and different evaluator; prepare, qualify and review the withheld-input package.
- [x] Commit/push preparation and run the two stages with the first-stage checkpoint.
- [x] Compare independent judgments with retained original and owner-revised assessments; preserve disagreements for owner review.
- [ ] Review the disagreement analysis with the owner before changing the grading procedure or running more assessments.

The [independent final report](/private/tmp/cw-independent-scoring-j4sxgwi0/attempts/2/final.md) passes all four cases and their fidelity checks.
The [comparison](/private/tmp/cw-independent-scoring-j4sxgwi0/comparison.md) records agreement on CW-08 and CW-18 scores, but CW-19 preservation PASS conflicts with the retained FAIL and CW-14 fidelity PASS misses the retained proposal-method omission.
The grader claims CW-19's actor is preserved even though the output never names the release engineer; the rubric already explicitly requires that actor.
It also claims CW-18's trace contains the guide read-back text, although the command's recorded output contains only diagnostics and Git status; the separately retained actual guide remains sufficient evidence to judge its contents.
These are grader evidence-checking/completeness gaps, not grounds for automatically replacing the original judgments or redesigning CW methodology.
The owner-reviewed threshold/warning clarity shortcomings involve reader judgment; the grader's blanket readability PASS does not examine or resolve those tradeoffs.

The [audit](/private/tmp/cw-independent-scoring-j4sxgwi0/collection-audit.json) verifies two distinct fresh sessions, one model turn each, no retries or subject reruns, 66 frozen files, 40 retained source files and both runtime removals.
The second prompt was derived only from frozen evidence and its own unchanged first report; no feedback about disagreement was supplied.
The two-call approval is exhausted, and both grader reports remain separate scratch records.
Next, discuss requiring concrete output/trace support for each applicable rubric obligation and an omission check within the existing grouped scores; this improvement is proposed, not implemented or authorized for another call.

### Stronger-model scoring comparison

The owner requested Opus 4.8 or 5, or Sonnet 5 after the completed independent check.
The [new package](/private/tmp/cw-independent-opus5-0z_e8u7x/summary.md) selects `claude-opus-5`, retaining medium effort and the same four cases, original frozen rules, system prompt and two-stage procedure.
[Anthropic's current documentation](https://platform.claude.com/docs/en/models/opus-5/whats-new-opus-5) identifies that model; the first approved invocation must verify actual account availability and resolved model identity.
All copied grading inputs are byte-identical to the previous package; stage 2 receives this new grader's own unchanged first report, never the earlier grader's report or operator feedback.
This keeps model choice as the intended comparison variable; equivalent named effort does not guarantee identical internal computation across models.
The proposed evidence-grounding prompt improvement above remains deferred while this comparison runs.

The [authorization](/private/tmp/cw-independent-opus5-0z_e8u7x/authorization.md) covers exactly two serial no-tool evaluator calls, with the existing first-stage checkpoint and private-runtime controls.
Current CLI version/digest match the preceding check; a fresh provider-free authentication, option-parsing and host-protection check passed.
Retain every original report and subject artifact; no automatic verdict replacement, new subject collection, skill/rubric edit or evidence promotion.

- [ ] Review and commit/push the model-only preparation, then execute both stages with the checkpoint.
- [ ] Compare both graders with the retained judgments and report evidence-supported differences and limits.

### Scoring clarifications before final coverage

The owner clarified that CW need not outperform the control on every test: preserving successful behavior is a useful outcome.
Record no observed degradation when a direct paired comparison supports equivalent task success and readability; two PASS labels alone do not establish equivalence or universal reliability.
The [specification](specs/2026-09-10-cw-baseline-specification.md) and [comparison rules](../skill-validation/pilot/cw-runbook.md#comparing-conditions) own that interpretation.

The authorized documentation change makes CW-08 repetition assessment explicitly depend on reader function and uses its retained two outputs as calibration.
The [output-scope rules](../skill-validation/pilot/cw-runbook.md#output-scope) distinguish final-answer content from conversation-wide silence.
New prospective prompt copies for the unrun CW-01/18/19 effectiveness tasks clarify final-answer scope while preserving source prose, permissions and historical prompts; both arms must receive the same common task.
Future selected tasks with ambiguous output scope require the same explicit clarification before their next freeze, recorded as changed task input rather than silently applied to old observations.
All original runs, frozen evaluation inputs and successive judgments remain unchanged, including CW-05's recorded fidelity failures.
No skill edit, subject call or historical reassessment belongs to this documentation change.

- [x] Review and verify the specification, shared scoring, CW-08 rubric and three clarified prospective tasks; reconcile their catalog/rubric links.
- [x] After the remaining three coverage purposes, prepare a small independent scoring check using a different evaluator without access to current judgments; see the selected package above.

[Verification](/private/tmp/cw-scoring-clarifications-zw1r9j57/verification.json) and [review](/private/tmp/cw-scoring-clarifications-zw1r9j57/review.md) confirm only response-scope wording changed in the three copied prompts, all 646 retained files are unchanged, and Markdown destinations/anchors resolve.
The hook suite passed with 263 tests and three skips; no provider was called and no observation was rescored.

That later check should include useful repetition, meaning-preservation judgment and the CW-14 proposal omission, with source tasks, applicable frozen rules and complete evidence available.
Assess artifacts before revealing condition/trace information where practical, then verify the trace for loading and fidelity; record what could not be blinded.
Retain separate assessments and explain disagreements without overwriting originals; it measures scoring agreement and requires no subject rerun.
Select the exact observations and evaluator before execution; no evaluator provider call or reassessment is launched by this change.

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
