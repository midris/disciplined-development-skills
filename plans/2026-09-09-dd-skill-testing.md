# DD skill testing: current state and next step

**Status:** Baseline tooling is settled for the current Codex workflow.
Evidence validity is accepted and the complete packages are preserved in the working tree.
Next: implement copy-based installation directly on `main` in the primary checkout, as the owner requested on 2026-09-09, then Claude test support before returning to evidence interpretation and CW methodology.
The owner requested this consolidation on 2026-09-09 to close completed work, remove inactive branches from the working set and stop cycling through testing-system redesign.
This is the single active testing plan.
The [validation guide](../skill-validation/README.md) indexes the durable contracts and execution instructions.

**Goal:** A repeatable set of tests for each DD skill's discoverability, effectiveness and composition, with distinct questions and observable scoring criteria.
Use as many cases as the obligations require; neither a minimum count nor preserving every historical test is a goal.
The [charter](../skill-validation/charter/core-contracts.md) supplies intended behavior, and the accepted [coverage policy](completed/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-methodology-decision-shared-test-categories-and-coverage) supplies the common categories.

## What is complete

| Work | Result and durable home |
|---|---|
| Mechanical runner and worksheet | Implemented and on main: one configured provider invocation, retained evidence, blank worksheet generation and separate model-owned judgment. See the [runner](../skill-validation/runner/README.md) and [methodology](completed/specs/2026-09-02-skill-testing-methodology-design.md). |
| Historical scenario migration and observations | All 105 scenario records are preserved in the [catalog](../skill-validation/scenarios/README.md). These are historical evidence, not qualified controls for the later CW comparison. |
| Controlled-input feasibility | Codex and Claude reached owner-accepted scoped feasibility. The [Codex](completed/2026-09-05-skilltest-provider-input-isolation.md) and [Claude](completed/2026-09-06-skilltest-claude-controlled-inputs.md) records retain limits; only Codex proceeded to production integration and scenario qualification. |
| Codex runtime and procedure pilot | Private runtime, native fixtures, CLI provenance and bounded cleanup are implemented on main. Four initial, six extension and four CW procedure observations completed; the [pilot record](completed/2026-09-06-skilltest-sol-low-pilot.md) retains evidence and historical judgments. |
| CW baseline | Owner-accepted: 99 observations, 22 purpose-separated variants, current-DD and meaningful no-DD controls, Sol medium. The [accepted index](../skill-validation/accepted/concise-writing/codex-gpt-5.6-sol-medium/README.md) retains complete evidence. |
| Existing CW candidate comparison | All 66 candidate observations are collected, scored and mechanically audited under unchanged criteria. The [comparison record](completed/specs/2026-09-07-cw-validation-design.md#candidate-comparison-handoff) links scratch evidence; the owner accepted its validity on 2026-09-09. Further evaluation remains open; no candidate was adopted. |
| Provider-free coverage audit | All 22 variants were mapped in the owner discussion to purpose, obligation and distinct risk. The follow-up distinguished routine tests from optional diagnostics and qualification. The resulting suite changes are proposals, not approved inputs. |

The pilot tooling is no longer an open implementation project.
The [pilot design](completed/specs/2026-09-06-skilltest-controlled-inputs-design.md) retains accepted methodology decisions; its implementation steps and old model schedules are historical.

## Retired and deferred work

| Work | Disposition |
|---|---|
| Old comprehensive rewrite execution plans | The original execution path was superseded; main's replacement [cleanup plan](completed/2026-08-01-comprehensive-skill-cleanup.md) was retired without execution. The owner explicitly retains `docs/comprehensive-skill-cleanup` and its worktree as a source of candidates to test after methodology settles. Its work is not abandoned or adopted wholesale; only its unchanged CW snapshot has undergone the current comparison. |
| Strict universal input isolation | Replaced by qualified observable controls and disclosed common-input/hidden-provider limits. Do not restart an absolute-isolation project. |
| Baseline directory/campaign redesign | [Deferred](deferred/2026-09-03-skill-validation-baseline-design.md). Existing layouts, runbooks and whole-set evidence retention are sufficient for current work. |
| All-skill discovery/behavior repairs | [Deferred](deferred/2026-09-07-skilltest-discovery-behavior-catalog-separation.md). Its original CW preparation is complete; further CW suite design proceeds here before expanding to other skills. |
| Model/effort matrices and larger samples | Deferred. Claude test support is now requested below; the completed Sol-medium batches authorize no additional calls. |
| Hook redesign and older skill/backlog proposals | Separate, deferred work in the [backlog inventory](deferred/2026-07-17-dd-skills-backlog.md). The parked July hook-fix branch was unmerged with unresolved review findings; archiving it does not resolve those defects. |

## Where the work lives

The 2026-09-09 audit fetched origin and checked all remote branches and GitHub PRs; no open PR was present.
At that audit, main was `4c4ba1b2792b8fd5ed0a046f2a6ac6a2c5428165`, and the active CW branch was `595f8e2bce0a62c5d4143ffebcdcf30cf8422b0d`, five commits ahead.
Main contains the baseline tools, historical catalog and completed procedure pilot; the CW branch adds the full baseline and candidate comparison inputs.
The [accepted candidate package](../skill-validation/accepted/concise-writing/codex-gpt-5.6-sol-medium-candidate/README.md) and [accepted procedure-pilot package](../skill-validation/accepted/procedure-pilot/codex-gpt-5.6-sol-low/README.md) retain complete bundles and supporting provenance.
Their original scratch packages remain retained.
The seven documentation edits present before consolidation were preserved in the moved/reconciled documents; an exact pre-cleanup patch and copies also remain at `/private/tmp/dd-testing-cleanup.b9v_1z7g/`.

Keep `docs/comprehensive-skill-cleanup` active at `13599fb7d3127334b0d07bfe468767e586ec5f9c`, including its remote and clean worktree.
Only the parked July hook-fix branch is selected for archival; a tag preserves its complete committed history without keeping it as apparent ongoing work.
The hook-fix tip `3c60c1951d7fea32047e7ab91e8a0d15aed6f33f` is preserved at remote tag `archive/2026-09-09-pre-pr-review-false-positives`; its remote branch was deleted only after verifying that exact tag target.
A verified complete-history recovery bundle also remains at `/private/tmp/dd-testing-cleanup.b9v_1z7g/parked-hook-fix.bundle`.
No unmerged implementation is integrated by archiving it, and no retained validation scratch is disposable under this cleanup.

## Remaining work

- [x] Finish this documentation consolidation and verify local links, preserved evidence and the required hook suite.
- [x] Archive the parked hook-fix tip under a verified remote tag, then remove its inactive remote branch ref. Preserve both the CW and comprehensive-rewrite branches/worktrees.
- [x] Record owner acceptance of evidence validity and preserve the complete candidate and procedure-pilot packages, verifying restoration without changing judgments or deleting scratch. Further evaluation and skill decisions remain open.
- [ ] On `main` in the primary checkout, change installation from repository symlinks to copies of the necessary skill files and folders, preserving unrelated consumer files and folders. Cover initial installation, migration, updates and preservation with installer tests; reconcile installation guidance. Establish the installed copies before moving ongoing testing work into the primary repository checkout, so checkout changes do not silently change installed skills. Keep the comprehensive rewrite branch and worktree active.
- [ ] Complete the missing Claude test support using the existing runner and accepted feasibility findings. Bound the work to the equivalent controlled runtime, retained evidence and written run procedure needed to run and score Claude tests; avoid a harness redesign or model matrix. Review any necessary live qualification as a separate exact command batch.
- [ ] Evaluate what the accepted CW comparison supports and what remains uncertain before making skill-change or adoption decisions. Evidence validity acceptance does not close this work.
- [ ] Agree one concrete routine CW suite in the [existing catalog mapping](../skill-validation/pilot/cw-catalog.md), identifying every retained, retired, replaced and new case and its observable scoring boundary. Do not create another tracking framework.
- [ ] After suite agreement, prepare only the approved prompt/rubric changes and the existing runbook updates; review those exact inputs before proposing any provider batch.

Methodology resumes after evidence closure and the two requested workflow improvements.
The current rubrics remain usable for their existing examples.
The [coverage proposal](../skill-validation/pilot/cw-catalog.md#routine-suite-proposal-awaiting-owner-review) records the latest discussion so it need not be reconstructed again.
Once an agreed CW suite works end to end, use that method for the next owner-selected skill; a complete nine-skill campaign is not a prerequisite to finishing CW.

New runs require a finite approved command batch and frozen comparable inputs.
No new provider calls, skill edits, candidate adoption, hook implementation or merge follows from this cleanup or evidence acceptance.
Historical scenario inputs, accepted result/worksheet/trace bytes and frozen candidate skill inputs remain unchanged; navigation-only README links follow the archived document paths.

## Evidence validity accepted; evaluation remains open

On 2026-09-09 the owner accepted the candidate and procedure-pilot evidence as valid, explicitly retaining further evaluation and decision-making work.
This closes the pending validity decision for the 66 candidate observations and 14 procedure observations; it does not close interpretation, test-coverage selection or candidate adoption.
The 99-observation CW baseline and 105 historical records were already accepted and remain unchanged.
The accepted packages above preserve the original judgments, full bundles, approval and qualification evidence, with archive restoration and byte comparisons completed.
No provider calls or skill adoption follow from this acceptance.

## Cleanup verification

Moved eight completed or closed records to `plans/completed/`, and the deferred baseline-organization design and older backlog to `plans/deferred/`.
The June telemetry/fail-open proposals were already subsumed; the announcement proposal was already closed without implementation.
Unresolved older proposals remain deferred rather than being marked complete by assumption.
Provider-free verification checked protected files and link-only changes to the three navigation READMEs beside runner/candidate/accepted evidence; it introduced no new local-link failures.
The required hook suite passed 263 tests with three skips; authored-documentation diff checks passed.
Byte-identical evidence copies retain original trailing whitespace and blank lines; checksum verification governs those files rather than whitespace cleanup.
The owner authorized committing and pushing the completed documentation and accepted-evidence unit on 2026-09-09; the remote hook-branch archival is already complete.
The path-reference sweep spans the moved records and their navigation callers; the commit body lists each affected path so the archive moves remain reviewable together with their links.
Evidence preservation restored both archives, checked all 82 complete bundles and 2,822 source file hashes, verified 1,624 readable copies and 342 worksheet links, and left all previously protected files unchanged.
