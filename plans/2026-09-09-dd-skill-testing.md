# DD skill testing: current state and next step

**Status:** Installation and baseline tooling are settled for the current Codex and Claude local workflows.
The accepted CW evidence and completed-plan cleanup are consolidated on `main`; ongoing testing work uses this primary checkout.
Next: review the completed CW catalog audit and its coverage proposal, prepare the agreed repairs/additions, then settle scoring.
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
The proposed 18 purposes comprise 12 effectiveness, four discoverability and two composition cases; approval and implementation of gap remedies remain open.
CW remains the pilot: review specification fidelity first, then evaluate the complete catalog and address gaps or unnecessary overlap, then define scoring from the settled specification and scenarios.
Do not continue adjusting scores while those earlier steps remain open.
Earlier observations remain evidence under their recorded contracts; neither their collection nor the retrospective corrections establish a completed baseline against this new specification.

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
- [ ] Review the coverage proposal, then prepare and review the agreed repairs/additions, including representative standalone CW conditions and DD-guided development composition with required Superpowers available; the identified gaps are not closed by documenting them.
- [ ] Once the catalog and gaps are settled, define/reconcile scoring, then determine what evidence is needed to establish baseline effectiveness.
- [x] Consolidate completed plans and preserve the accepted evidence packages without changing judgments.
- [x] Implement the copy installer and update Steno’s `.claude` and `.agents` installations.
- [x] Complete and qualify Claude support through the existing runner and worksheets.
- [x] Add a blank `Test category / supporting purpose` worksheet field and document the five labels for the evaluator; retain existing configuration and accepted evidence unchanged.
- [x] Agree the earlier routine CW suite, identifying every retained, retired, replaced and new case and its observable scoring boundary. The new specification-based proposal above requires its own review.
- [ ] Evaluate what the accepted CW comparison supports and what remains uncertain before any skill-change or adoption decision.
- [x] Document the clarified CW contract in its durable homes, reconcile the six affected routine rubrics and rescore all 18 latest observations separately from their original judgments.
- [ ] Revisit earlier scored outcomes after specification, catalog coverage and scoring are settled; preserve all prior judgments meanwhile.
- [x] Prepare and review CW-03/13/14/17/18 replacements and CW-20 restraint inputs, update the existing catalog/runbook, and check the distinct response-generation and restraint criteria. All completed-comparison inputs are preserved; no runner code or skill edits.
- [x] Obtain owner review of the six exact input packages; approval was given after commit `6867030`.
- [x] Approve and execute a separately frozen initial evidence pass. The completed Codex / Sol medium batch covered only CW-03/13/14/17/18/20: no-DD, current-DD and unchanged candidate, one observation each (18 calls). This reduces the first commitment while exposing real scoring/task issues; it does not establish consistency. Further repetitions require a decision-specific sampling choice and separate approval, retaining these initial observations. The other 12 routine cases remain historical context rather than fresh observations.

The [routine input map](../skill-validation/pilot/cw-catalog.md#routine-input-map) links the six packages used in the initial pass; the proposed portfolio and full audit are above it in the same catalog.
Provider-free preparation evidence remains in `/private/tmp/dd-cw-routine-inputs-6gx080gt/summary.md`; it exercises no-DD/current-DD/candidate assembly, not a new provider schedule or skill-effectiveness claim.
All 18 observations are collected, scored and mechanically audited with no infrastructure retries. Their evidence remains scratch-only pending owner review. The exhausted command batch, worksheets, full traces, frozen inputs and qualification reconciliation are retained under `/private/tmp/skilltest-cw-routine.c81p4an9/summary.md`; the superseded 54-call proposal is preserved under `prior-54-proposal/` in that package and authorizes no calls.
The initial-pass preparation verified Codex's executable against the completed comparison and checked the selected catalogs/common inputs.
That preparation recorded Claude `2.1.267`, newer than its qualification at `2.1.266`; any future collection requires checking the then-selected executable and reconciling affected controls.

Original rubrics still define their frozen records; the separate retrospective worksheets apply the clarified contract without replacing those records.
The exact 18-call approval is exhausted; further evidence interpretation waits for the specification, coverage and scoring work above. No automatic repetitions, promotion or candidate adoption follow. The scratch summary reports the original and revised judgments with separate CW prose, authoring authority, task fidelity and comparative readability evidence.
Retain ordinary cases even when a particular no-DD model passes them; the owner’s experience of model verbosity is context, not a measured cross-provider result.
Once an agreed CW suite works end to end, follow the [per-skill starting workflow](../skill-validation/README.md#starting-the-next-skill) for the next owner-selected skill; a complete nine-skill campaign is not a prerequisite to finishing CW.
