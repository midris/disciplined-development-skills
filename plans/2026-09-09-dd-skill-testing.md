# DD skill testing: current state and next step

**Status:** Installation and baseline tooling are settled for the current Codex and Claude local workflows.
The accepted CW evidence and completed-plan cleanup are consolidated on `main`; ongoing testing work uses this primary checkout.
Next: execute and score the owner-approved 18-call initial evidence pass for the six reviewed CW input packages.
This is the single active testing plan; the [validation guide](../skill-validation/README.md) indexes the durable contracts and execution instructions.

**Goal:** A repeatable set of tests for each DD skill’s discoverability, effectiveness and composition, with distinct questions and observable scoring criteria.
Use as many cases as the obligations require; neither a minimum count nor retaining every historical test is a goal.
The [charter](../skill-validation/charter/core-contracts.md) supplies intended behavior, and the accepted [coverage policy](completed/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-methodology-decision-shared-test-categories-and-coverage) supplies the common categories.

## Completed work

| Work | Result and durable home |
|---|---|
| Copy installer | Copies whole shipped skill folders into `.claude/skills` or `.agents/skills`, replacing same-name skills and preserving unrelated consumer files/history. Implemented on main and applied to both Steno installations. [Completed spec](completed/specs/2026-09-09-copy-based-installer-design.md). |
| Runner and worksheets | The same configuration, run bundles and model-scored worksheets support Codex and Claude. No campaign manager or automatic semantic scorer. [Runner](../skill-validation/runner/README.md), [methodology](completed/specs/2026-09-02-skill-testing-methodology-design.md). |
| Controlled-input qualification | Codex controls and the procedure pilot are complete. Claude’s native catalogs/loading, companion access, seven local tools, file/Git work and capture/cleanup passed scoped qualification. [Qualification reference](../skill-validation/pilot/qualification/README.md), [completed Claude spec](completed/specs/2026-09-09-claude-skill-testing-design.md). |
| Historical records and procedure pilot | All 105 historical records and 14 procedure observations are preserved. These are not matching-input controls for the later CW comparison. [Historical catalog](../skill-validation/scenarios/README.md), [accepted pilot package](../skill-validation/accepted/procedure-pilot/codex-gpt-5.6-sol-low/README.md). |
| CW baseline | Owner-accepted: 99 observations covering 22 purpose-separated variants, current-DD and meaningful no-DD conditions, Sol medium. [Accepted baseline](../skill-validation/accepted/concise-writing/codex-gpt-5.6-sol-medium/README.md). |
| Existing CW candidate comparison | All 66 observations are collected, scored and audited under unchanged criteria; their validity is owner-accepted. Further interpretation remains open and the candidate is not adopted. [Accepted candidate package](../skill-validation/accepted/concise-writing/codex-gpt-5.6-sol-medium-candidate/README.md), [comparison contract](completed/specs/2026-09-07-cw-validation-design.md). |
| Coverage audit | The owner approved preparation under the revised [18-case coverage](../skill-validation/pilot/cw-catalog.md#routine-suite-coverage): 11 effectiveness, five discoverability and two composition. Exact-input review must confirm distinct coverage or consolidate overlapping cases; approval of the coverage does not authorize collection. |

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

- [x] Consolidate completed plans and preserve the accepted evidence packages without changing judgments.
- [x] Implement the copy installer and update Steno’s `.claude` and `.agents` installations.
- [x] Complete and qualify Claude support through the existing runner and worksheets.
- [x] Add a blank `Test category / supporting purpose` worksheet field and document the five labels for the evaluator; retain existing configuration and accepted evidence unchanged.
- [x] Agree one concrete routine CW suite in the [existing catalog mapping](../skill-validation/pilot/cw-catalog.md), identifying every retained, retired, replaced and new case and its observable scoring boundary.
- [ ] Evaluate what the accepted CW comparison supports and what remains uncertain before any skill-change or adoption decision.
- [x] Prepare and review CW-03/13/14/17/18 replacements and CW-20 restraint inputs, update the existing catalog/runbook, and check the distinct response-generation and restraint criteria. All completed-comparison inputs are preserved; no runner code or skill edits.
- [x] Obtain owner review of the six exact input packages; approval was given after commit `6867030`.
- [ ] Approve and execute a separately frozen initial evidence pass. The owner-approved Codex / Sol medium batch covers only CW-03/13/14/17/18/20: no-DD, current-DD and unchanged candidate, one observation each (18 calls). This reduces the first commitment while exposing real scoring/task issues; it does not establish consistency. Further repetitions require a decision-specific sampling choice and separate approval, retaining these initial observations. The other 12 routine cases remain historical context rather than fresh observations.

The [routine input map](../skill-validation/pilot/cw-catalog.md#routine-input-map) links all 18 purposes and the six changed/new packages.
Provider-free preparation evidence remains in `/private/tmp/dd-cw-routine-inputs-6gx080gt/summary.md`; it exercises no-DD/current-DD/candidate assembly, not a new provider schedule or skill-effectiveness claim.
The approved batch, exact commands, frozen inputs and qualification reconciliation are retained under `/private/tmp/skilltest-cw-routine.c81p4an9/summary.md`; the superseded 54-call proposal is preserved under `prior-54-proposal/` in that package and authorizes no calls.
Codex's executable matches the completed comparison; fresh provider-free catalogs/common-input checks cover the current runner and fixture groups.
Claude is now `2.1.267`, newer than the qualified `2.1.266`; choosing Claude requires affected-control reconciliation before collection.

The current rubrics remain usable for their existing examples.
The owner approved the exact 18-call batch and requested commit/push followed by execution; the 18-case coverage and six exact input packages are also approved.
Retain ordinary cases even when a particular no-DD model passes them; the owner’s experience of model verbosity is context, not a measured cross-provider result.
Once an agreed CW suite works end to end, use that method for the next owner-selected skill; a complete nine-skill campaign is not a prerequisite to finishing CW.
