# DD skill testing: current state and next step

**Status:** Installation and baseline tooling are settled for the current Codex and Claude local workflows.
The accepted CW evidence and completed-plan cleanup are consolidated on `main`; ongoing testing work uses this primary checkout.
Next: agree the concrete CW test coverage before editing prompts, skills or collecting more observations.
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
| Coverage discussion | The existing [catalog proposal](../skill-validation/pilot/cw-catalog.md#routine-suite-proposal-awaiting-owner-review) distinguishes routine coverage from diagnostics and qualification. Membership/input changes still need owner agreement. |

## Retained and deferred work

Keep `docs/comprehensive-skill-cleanup` and its worktree active at `13599fb7d3127334b0d07bfe468767e586ec5f9c` as a source of candidates after methodology settles.
Only its unchanged CW snapshot has undergone the completed comparison; no other rewritten skill is evaluated or adopted here.
The CW collection history and accepted evidence are integrated on `main`; retire its branch/worktree after verifying the pushed merge.
Its complete `.claude` DD log/state history is copied and hash-verified under `/private/tmp/dd-cw-retirement-5qvesacx/`; retain that package alongside the original validation scratch.

- Strict universal input isolation was replaced by scoped controls and disclosed common-input/hidden-provider limits; do not restart that project.
- [Campaign/baseline organization](deferred/2026-09-03-skill-validation-baseline-design.md), [all-skill catalog repairs](deferred/2026-09-07-skilltest-discovery-behavior-catalog-separation.md), larger model/effort matrices and [older hook/skill proposals](deferred/2026-07-17-dd-skills-backlog.md) remain deferred.
- The parked hook-fix history remains at remote tag `archive/2026-09-09-pre-pr-review-false-positives`, with a recovery bundle under `/private/tmp/dd-testing-cleanup.b9v_1z7g/`. Archiving did not resolve its unmerged review findings.
- Original CW, candidate, pilot and Claude qualification scratch packages remain retained for review. Evidence validity acceptance does not authorize adoption, rescoring, deletion or new provider calls.

## Remaining work

- [x] Consolidate completed plans and preserve the accepted evidence packages without changing judgments.
- [x] Implement the copy installer and update Steno’s `.claude` and `.agents` installations.
- [x] Complete and qualify Claude support through the existing runner and worksheets.
- [ ] Agree one concrete routine CW suite in the [existing catalog mapping](../skill-validation/pilot/cw-catalog.md), identifying every retained, retired, replaced and new case and its observable scoring boundary.
- [ ] Evaluate what the accepted CW comparison supports and what remains uncertain before any skill-change or adoption decision.
- [ ] After suite agreement, prepare only approved prompt/rubric and runbook changes; review exact inputs before proposing a finite provider batch.

The current rubrics remain usable for their existing examples.
The next decision concerns distinct coverage and unnecessary overlap, not redesigning scoring or manufacturing failures.
Retain ordinary cases even when a particular no-DD model passes them; the owner’s experience of model verbosity is context, not a measured cross-provider result.
Once an agreed CW suite works end to end, use that method for the next owner-selected skill; a complete nine-skill campaign is not a prerequisite to finishing CW.
