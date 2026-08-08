# Comprehensive Skill Cleanup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` with the orchestrator executing validation-bearing tasks inline. Do not delegate a whole validation-bearing task through `superpowers:subagent-driven-development`; its implementer would be prohibited from dispatching the required evaluator subagents. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish a trustworthy validation baseline, then make all nine skills compact and coherent without losing effectiveness.

**Architecture:** Treat the pinned skill tree at `4296647` as the regression control for original behavior. Build a shared validation protocol and one active scenario catalog per skill, record Sol-high and Sol-low baseline results, then process each skill through any required portability RED/GREEN slice followed by a behavior-preserving readability cleanup. A successful portability slice becomes that skill's immediate readability control; otherwise `4296647` serves both roles. Clean `disciplined-development` last so it routes settled child contracts.

**Tech stack:** Markdown skills and validation records; `gpt-5.6-sol` evaluation subagents; Superpowers 6.2.0; Git; Python/pytest for repository regression suites.

**Design reference:** [`plans/specs/2026-08-01-comprehensive-skill-cleanup-design.md`](specs/2026-08-01-comprehensive-skill-cleanup-design.md)

## Global constraints

- All skill authoring, validation design, scoring, and cold reviews use `gpt-5.6-sol` at high reasoning effort.
- Sol low is used only for the comparative score arms in Tasks 11 and 27 and any control backfill required by the post-freeze rule.
- The orchestrator owns validation-bearing tasks, evaluator, scorer, and reviewer dispatch, the scoring workflow, user approval gates, and commits; evaluators, scorers, and reviewers remain read-only and never dispatch nested agents.
- Every behavioral scenario uses five fresh, read-only evaluators with no nested dispatch; run at most three evaluators concurrently.
- Start each evaluator without inherited conversation history and specify its model, effort, immutable skill bundle, and task context explicitly.
- Use only a probed transport that enforces no-write evaluator access; instruction-only isolation is invalid, and unavailable enforcement blocks validation.
- Evaluator prompts never contain or point to the scoring rubric.
- For subjective comparisons, a separate fresh scorer manually applies the evaluator-withheld rubric to outputs under opaque arm IDs but never receives the control/draft mapping.
- Freeze each subjective scoring record before mapping those IDs back to control and draft.
- Manually score every other completed response; in every scoring context, a missed criterion is a failure, not a discarded run.
- Record infrastructure failures separately and retry them without counting them as behavioral results.
- After three consecutive infrastructure errors for one scenario and configuration, pause and surface the blocker.
- Preservation scenarios require a 5/5 control at `4296647`; approved target scenarios require a watched control RED and 5/5 GREEN.
- A preservation result below 5/5 stops the task for the design's failure-classification gate; do not continue by weakening the rubric or editing the skill.
- After changing scenario wording, restart that scenario at zero.
- Do not commit raw evaluator transcripts.
- Materialize every regression and immediate-readability control as an immutable scratch bundle outside the repository, identified by commit and content hash; never use the mutable working tree as a control arm.
- For subjective cleanup comparisons, rerun five fresh immediate-readability-control arms and five fresh draft arms, anonymize the labels, and keep temporary outputs in scratch space outside the repository until the scored summary is recorded.
- Do not edit skill prose until Tasks 1–11 establish and score the control suite, except a user-approved RED/GREEN slice required to resolve a genuine baseline inconsistency.
- Task 7 has an owner-approved pre-freeze exception for visible member enumeration, `DD-PATTERN` synthesis, the `NONE` branch, response-template precedence, and folding effectiveness into the necessity section; keep this behavior slice separate from the later readability cleanup and commit it as its own behavioral boundary after final approval. The precedence and effectiveness wording are approved clarifications with preserved 5/5 controls, not claimed behavioral lifts.
- Portable-behavior edits and readability edits land in separate commits.
- A skill's complete active suite includes its owned scenarios and every shared discovery, direct-invocation, portability, and composition scenario mapped to its promises.
- Every shared or supporting scenario record has one owner and lists every affected skill.
- A whole-skill cleanup reruns that skill's complete active Sol-high suite.
- After Task 11, any change to a scenario prompt, fixture, rubric, supplied context, or protected promise requires fresh Sol-high and Sol-low control results before the scenario is used again.
- Show every skill draft and wait for user approval before applying it; show the final edited file in place and wait for user approval before committing it.
- Any skill edit after final approval returns to the draft/test/in-place approval sequence before commit.
- Skill prose uses one sentence per line with the repository's structural exceptions.
- Each skill commit records applicable control/current word counts, model results, cold review, repository tests, and any reference sweep.
- For portable skills with a behavior slice, record word counts for `4296647`, the post-portability readability control, and the cleaned version.
- Update this plan's checkboxes and notes in every task commit; the task file lists omit this repeated path.
- Task 1 classifies the project-level and supporting scenario records it owns; Tasks 2–10 classify every skill-owned record, including its supporting records, with the common taxonomy and update the audit status, classification counts, and scores in `skill-validation/README.md`; validation-bearing Tasks 12–25 keep that index current.
- The task file lists omit this repeated index path.
- Before Task 1's commit, resolve every changed local Markdown link relative to its source file and verify each target with `test -e`.
- Task 1 records one exact reusable local Markdown-link command in `skill-validation/README.md`; after Task 1, run it for every changed document before each commit.
- Before every commit run `git diff --check`.
- Before each skill commit run:
  - `(cd skills/disciplined-development/hooks && python3 -m pytest -q)`
  - `python3 -m pytest tests/ -q`
  - `python3 -m pytest research/ -q`
  - `git diff --check`

## Merge boundaries

- Task 1 is the validation-protocol boundary.
- Tasks 2–6 form the portable-skill control-baseline boundary.
- Tasks 7–10 form the integrated-development control-baseline boundary.
- Task 11 is the Sol-low control-score boundary.
- Each Task 12–16 portability edit is its own boundary; a 5/5 control requires no skill-change boundary.
- Each Task 17–25 skill cleanup is its own boundary.
- Tasks 26–27 form the final validation boundary.

Use one branch/PR per boundary when executing through PRs.
Within a boundary, retain the per-task commits named below so validation history remains reviewable.
Before opening a PR at any boundary, the orchestrator runs the complete Gate 5 whole-branch review and smoke pass.
Gate 5's external reviewer must use a different provider and model family from the orchestrator.
For a Claude orchestrator, use the Task 1 scratch `DD_CONFIG` override that pins `gpt-5.6-sol` at high effort and verify its logged model metadata before the boundary passes.
For this Codex-orchestrated Task 10 session, use a fresh Claude Opus 4.8 review at high effort and record its invocation and verdict in the Gate 2 artifact.
Keep that cleanup-specific override outside the repository rather than changing the shipped reviewer defaults.
When work proceeds without PRs, the same orchestrator-owned review runs at the repository's Principle 8 cadence.

---

### Task 1: Establish the validation protocol and index

**Files:**

- Create: `skill-validation/README.md`
- Create: `skill-validation/skill-discovery.md`
- Modify or retire from the active suite: `skill-validation/evaluation-subagents-read-only.md`
- Modify for the user-approved pre-freeze behavior slice: `skills/disciplined-development/SKILL.md`
- Modify for that slice's evidence: `skill-validation/disciplined-development.md`
- Modify for the approved exception: `plans/specs/2026-08-01-comprehensive-skill-cleanup-design.md`
- Modify: `CLAUDE.md`
- Modify: `README.md`

**Produces:** One source of truth for scenario types, immutable control bundles, enforced evaluator isolation, blinded subjective scoring, 5/5 scoring, run metadata, preservation versus target scenarios, infrastructure errors, suite ownership, post-freeze baseline changes, Sol-high/Sol-low arms, the cleanup-scoped Gate 5 override, the exact local-link command, and the compact per-skill catalog format; plus one shared suite of atomic all-nine discovery scenarios.

- [x] **Step 1: Inventory the current framework**

  List every file under `skill-validation/`, its purpose, owner, affected skills, active scenario IDs, repetition counts, and whether exact prompts and evaluator-withheld rubrics are recoverable.
  Inspect the available evaluator transport and record that `research/replay_codex.py` reviews historical diffs rather than executing skill scenarios; do not treat it as the skill-validation runner.
  Select a fresh-context transport that enforces no-write access, record its exact invocation, and run a disposable denial probe that confirms a write attempt leaves the repository unchanged; stop if enforcement is unavailable.

- [x] **Step 2: Write the shared protocol**

  Define the universal rules from the design once in `skill-validation/README.md`.
  Include immutable bundle materialization, fresh-context dispatch, explicit model/effort selection, three-error infrastructure escalation, complete-active-suite closure, post-freeze baseline invalidation, and one exact read-only command for checking local Markdown links.
  Define a blind-scoring handoff in which a separate fresh scorer receives the rubric and opaque output IDs, fixes the scoring record, and returns it before the control/draft mapping is revealed.
  Define a scratch Gate 5 `DD_CONFIG` project override that pins a Codex external review to `gpt-5.6-sol` at high effort, the exact invocation that consumes it, and the logged-metadata check that fails the boundary on mismatch.
  Require the external reviewer to use a different provider and model family from the orchestrator; when Codex orchestrates, use a fresh Claude review and record its model, effort, invocation, and verdict in the Gate 2 artifact.
  Keep the override outside the repository because it is specific to this cleanup rather than a new shipped reviewer default.
  Include the active-catalog fields: scenario ID, owner, affected skills, type, protected promise, protected skill section, supplied skill context, exact prompt or fixture link, evaluator-withheld rubric, control bundle commit and hash, control result, target GREEN when applicable, cleaned result, Sol-low scores, and rerun triggers.

- [x] **Step 3: Add the audit index**

  Add one row per skill and supporting scenario file, with its owner, audit task, `Unaudited` status, classification-count columns, and a link to the owning record.
  Task 1 marks the project-level and supporting rows it owns as `Audited` and fills their classification counts.
  Tasks 2–10 change the status to `Audited` and fill the `Keep`, `Repair`, `Merge`, `Retire`, and `Add` counts.
  Preserve historical records below each active catalog rather than rewriting them.

- [x] **Step 4: Materialize and verify the regression control**

  Create an immutable scratch bundle outside the repository containing all nine skill files and scenario-declared dependencies from `4296647`.
  Record its commit and content hashes, verify the nine live skill files still match it before baseline testing, and define the same procedure for post-portability readability controls.

- [x] **Step 5: Audit evaluator isolation**

  Classify `skill-validation/evaluation-subagents-read-only.md` under the common taxonomy.
  Repair it to the exact prompt, evaluator-withheld rubric, environment metadata, and 5/5 protocol if retained; otherwise retire it explicitly as historical project-rule evidence.
  Record the successful no-write denial probe and the blinded-scoring isolation check in the shared protocol without committing raw outputs.

- [x] **Step 6: Establish the shared discovery suite**

  Put a fixed set of atomic scenarios in `skill-validation/skill-discovery.md`.
  Each evaluator prompt contains all nine control descriptions and one simple user request, with one expected skill or an explicit allowed set in the withheld rubric.
  Evaluators never see skill bodies or the rubric.
  Run each scenario five times on Sol high at `4296647`, manually score every route, and map each scenario to every description whose positive or negative routing it protects.

- [x] **Step 7: Update repository guidance**

  Point `CLAUDE.md` and the project `README.md` at `skill-validation/README.md` for the validation protocol.
  Keep universal rules out of individual validation records.

- [x] **Step 8: Verify and commit**

  First verify each new local link target directly, stage only the protocol, index,
  guidance, design, and plan files, run the exact local-link command against that
  staged snapshot, and run both diff checks. Commit those files as
  `docs(validation): define the skill validation protocol`; explicitly exclude
  `skills/disciplined-development/SKILL.md` and
  `skill-validation/disciplined-development.md` from this commit.
  For the user-approved parent-co-selection behavior slice, record control/current
  word counts, complete Sol-high results, cold review, reference sweep, final
  in-place user approval, and all three repository test suites. Then stage the skill,
  its now-self-contained validation record whose linked protocol files are already in
  HEAD, and this plan's completed checkbox/evidence note; rerun the exact link and
  diff checks and commit as `docs(skills): require parent companion co-selection`.

**Task 1 execution note (2026-08-01):** The immutable control archive is pinned to `4296647f0dff48a9e77b979ef07e813bf1f66db2` with SHA-256 `8f21c8267d005c349702ec94d6aff26c13a09bfbe29f2b43efcfbb37304f16e3`.
Codex CLI 0.146.0 required `agents.enabled=false` in addition to read-only sandboxing to remove nested-agent tools; one provider 503 was recorded and the identical retry passed.
The instruction-only evaluator record and unrelated composite red-flags fixture were retired from the active suite, while their history was preserved.
After a cadence review exposed genuine parent-routing inconsistency, the user approved a minimal pre-freeze RED/GREEN exception: four watched control REDs now reach 5/5 on the immutable parent-co-selection target, and all five preservation cells remain 5/5.
Two ambiguous discovery requests were narrowed to atomic supplied-text and purely stylistic cases; every affected scenario restarted at zero after prompt or rubric repair.
The parent skill's control/current word counts are 1,981/1,985; only its frontmatter
description changed. A cadence review later required the alphabetical output contract
to become an explicit scoring criterion, invalidating and restarting both complete
discovery arms at zero.
After user-approved compression, one broad research noun phrase caused a 44/45 target
regression; an action-specific repair and complete target restart passed 45/45.
The final 338-character description received explicit in-place user approval after a
cold `writing-skills` and concision review returned no findings. The stale-reference
sweep found no obsolete live wording or hashes; two broad-research matches remain as
intentional failed-experiment history. Final repository verification passed: hook
suite 263 passed/3 skipped, installer suite 11 passed, and research suite 4 passed.
The protocol landed first as `ee776f9`, leaving the behavior record self-contained.

### Task 2: Audit and baseline `concise-writing`

**Files:**

- Modify: `skill-validation/concise-writing.md`
- Modify if still shared: `skill-validation/duplicate-red-flags-scenarios.md`
- Read control: `skills/concise-writing/SKILL.md` at `4296647`

**Required coverage:** link the shared discovery suite; simple padding removal; non-trivial compression that preserves rationale, navigation, and a load-bearing recap; safe direct invocation; non-software extraction using a policy or grant document; still-relevant verbosity, over-trim, trigger-routing, and red-flag-consolidation regressions.

- [x] Audit existing scenarios and classify each `Keep`, `Repair`, `Merge`, or `Retire`.
- [x] Add only missing coverage; merge the shared composite fixture into atomic skill scenarios where its unrelated output contracts would interfere.
- [x] Record exact prompts, supplied context, rubrics, protected sections, and rerun triggers in the active catalog.
- [x] Run every preservation scenario 5/5 on Sol high against `4296647`; classify a 5/5 portability result as preservation coverage or record a watched RED target.
- [x] Manually score every response and record exact misses without transcripts.
- [x] Review the record against `skill-validation/README.md`, run `git diff --check`, and commit as `docs(validation): baseline concise writing`.

**Task 2 execution note (2026-08-02):** The audit classified prior scenarios as
Keep 0, Repair 2, Merge 4, and Retire 2, then added six missing atomic scenarios.
`CW-01`–`CW-08` passed 5/5 on Sol high with zero infrastructure errors, classifying
`CW-08` portability as preservation. The approved Task 2A targets `CW-09`–`CW-12`
each produced a clean 0/5 watched RED: routing omitted `concise-writing`, while the
ownership probes returned null owners and evidence. Three cold record reviews found
and resolved premature and ambiguous live/history labeling; the final review returned
no findings. The skill remains byte-identical to control SHA-256 `4d12a2eb…`.

### Task 2A: Clarify `concise-writing` ownership during skill authoring

**User-approved behavior slice (2026-08-02):** allow `concise-writing` and
`superpowers:writing-skills` to be co-selected during skill or reference authoring,
while making `superpowers:writing-skills` the explicit owner of authoring decisions
and validation. This is a separate RED/GREEN change, not readability cleanup.

**Files:**

- Modify: `skills/concise-writing/SKILL.md`
- Modify: `skill-validation/concise-writing.md`
- Modify: `skill-validation/skill-discovery.md` if its results are rerun
- Modify: `README.md` if the stale-reference sweep finds old routing guidance
- Modify: this plan

- [x] Freeze `CW-09`–`CW-14`, run each five times on Sol high against immutable controls, and record watched RED without weakening their rubrics.
- [x] Remove the frontmatter exclusion and add only: “During skill or reference authoring, `superpowers:writing-skills` owns authoring decisions and validation.”
- [x] Materialize the target bundles, verify their hashes, and run the complete affected Sol-high suite at 5/5: `CW-01`–`CW-14`, shared discovery, and `CW-08` only if Task 2 classified it as preservation; otherwise retain its watched RED for Task 12.
- [x] Run cold editorial and skill-writing review, show the edited skill in place, and wait for final user approval.
- [x] After approval, run repository tests, stale-reference and link sweeps, and both diff checks; commit as `docs(skills): clarify concise writing authoring ownership`.

**Task 2A execution note (2026-08-02):** The final skill changes only the approved
frontmatter exclusion removal and ownership sentence; control/current word counts are
860/866 and current SHA-256 is `6c3a8382…`. `CW-01`–`CW-14` passed 70/70 on the
immutable target bundles with zero infrastructure errors. The two behavioral
composition controls each produced 0/5 watched RED by omitting `concise-writing`;
their targets co-selected both skills and left authoring and validation ownership
with `superpowers:writing-skills` in all ten runs. A cold design review froze those
forced-choice scenarios after rejecting two leading drafts; an earlier batch using
incomplete evaluator isolation was superseded before inclusion and both final arms
restarted at zero. Shared discovery passed
45/45 after a fresh validation-design review classified its original mechanical
rename request as ambiguous; repaired `DISC-08` restarted and passed 5/5 in all three
invalidated arms. The staged adversarial review then found that the Task 2A extractor
had dropped the apostrophe from an unrelated dispatch description; all 45 Task 2A
discovery results were superseded, and the byte-identical full arm restarted and
passed 45/45. A blinded scorer confirmed the sole borderline preservation output
under its frozen rubric. The second cold review using both `concise-writing` and
`superpowers:writing-skills` returned no findings, and the user approved the in-place
skill. Repository verification passed: hook suite 263 passed/3 skipped, installer
suite 11 passed, and research suite 4 passed. The stale-reference sweep found old
authoring exclusions only in immutable controls or explicitly labeled history. The
exact local-link check passed with 6 working links across 6 staged documents, and
both `git diff --check` and `git diff --cached --check` passed.

### Task 3: Audit and baseline `disciplined-research`

**Files:**

- Modify: `skill-validation/disciplined-research.md`
- Read control: `skills/disciplined-research/SKILL.md` at `4296647`

**Required coverage:** link the shared discovery suite; simple source acquisition and verification; a non-trivial authority/deadline scenario whose premise is disconfirmed; safe direct invocation; non-software extraction using museum, policy, or procurement research; the historical disclaimer-as-substitute and citation-as-substitute experiments, retained or retired honestly.

- [x] Map the skill's claims to existing B1/B17 evidence and distinguish shipped regressions from closed experiments.
- [x] Link the shared discovery result and add atomic application, direct-invocation, and extraction scenarios with exact evaluator-withheld rubrics.
- [x] Run preservation scenarios 5/5 on Sol high at `4296647`; classify a 5/5 portability result as preservation coverage or record a watched RED target.
- [x] Record failures and variance, review the active catalog, and commit as `docs(validation): baseline disciplined research`.

**Task 3 execution note (2026-08-02):** The audit classified B1 as Repair via
the replayable `DR-02` successor and B17 as Retire from the active suite, for totals
Keep 0, Repair 1, Merge 0, Retire 1, and Add 2.
Git history corrected B17's broad “not shipped” label: the behavior-neutral
`verify the citation yourself` nudge landed in `2be8db4` after scoring 0/6, while
the broader behavior change remained unshipped and the limitation remained in the
control.
A fresh Sol-high design review required executable and date-anchored fixtures,
fixed output shapes, candidate labels until results existed, and explicit discovery
mapping before the catalog froze.
`DR-01`–`DR-03` then passed 15/15 on immutable `4296647` bundles with zero
infrastructure errors; `DR-02` portability is therefore preservation coverage.

### Task 4: Audit and baseline `lean-plan-writing`

**Files:**

- Modify: `skill-validation/lean-plan-writing.md`
- Modify if still shared: `skill-validation/duplicate-red-flags-scenarios.md`
- Read control: `skills/lean-plan-writing/SKILL.md` at `4296647`

**Required coverage:** link the shared discovery suite; simple prose-as-contract planning; the non-trivial `KEY=VALUE` parser plan without implementation bodies; safe direct invocation with `superpowers:writing-plans`; non-software extraction using an event or publishing plan; unexercised-case, trigger-routing, and red-flag-consolidation regressions.

- [x] Audit and atomize existing scenarios without losing historical results.
- [x] Make the upstream override, input/output-table substitute, and five-line ambiguity exception independently scorable.
- [x] Run preservation scenarios 5/5 on Sol high at `4296647`; classify a 5/5 portability result as preservation coverage or record a watched RED target.
- [x] Review the active catalog and commit as `docs(validation): baseline lean plan writing`.

Execution note (2026-08-02, in progress): audited the historical families into
`LP-01`–`LP-08`, retained their sourced limitations, and ran five fresh Sol-high
processes per original-control arm. `LP-01` and `LP-05`–`LP-08` preserved their
promises at 5/5; `LP-04` remains a 4/5 watched portability RED for Task 14.
`LP-02` and `LP-03` exposed pre-freeze prose-contract gaps; after user-approved
skill wording and independently approved test repairs, the final intent-focused
candidate passed both targets 5/5. The final-change triggers also reran `LP-01`,
`LP-05`, and `LP-06` at 5/5. Cold review then exposed an underdetermined scale
fixture and duplicated upstream-TDD criterion in `LP-05`; the independently
approved test-only repair restarted and passed 5/5. A fresh final cold review
approved the skill, scenarios, hashes, and record. No hook changed. Final user
approval followed. Repository verification passed: hook suite 263 passed/3
skipped, installer suite 11 passed, and research suite 4 passed. The stale-reference
sweep found no obsolete live wording. The exact local-link check passed across four
working and four staged Markdown documents, and both diff checks passed.

### Task 5: Audit and baseline `sweeping-stale-references`

**Files:**

- Modify: `skill-validation/sweeping-stale-references.md`
- Modify if still shared: `skill-validation/duplicate-red-flags-scenarios.md`
- Read control: `skills/sweeping-stale-references/SKILL.md` at `4296647`

**Required coverage:** link the shared discovery suite; a simple load-bearing rename; the non-trivial 126-match grouped sweep; safe direct invocation; non-software extraction using a renamed policy term across handbooks and forms; reviewer-one-hit, three-way classification, grouping/reconciliation, negative-form, and red-flag-consolidation regressions.

- [x] Audit the current record and separate the portable search/triage/reconcile contract from software-specific commit evidence.
- [x] Add atomic prompts and rubrics for literal/synonym search, all required file categories, three classifications, count reconciliation, and grouped evidence.
- [x] Run preservation scenarios 5/5 on Sol high at `4296647`; classify a 5/5 non-software portability result as preservation coverage or record a watched RED target.
- [x] Review and commit as `docs(validation): baseline stale reference sweeping`.

**Task 5 execution note (2026-08-02):** Audited the historical families as
Keep 0, Repair 2, Merge 0, Retire 0, and Add 3, producing the smallest coherent
five-scenario suite after a section-by-section and whole-skill simplification review.
`SSR-01`–`SSR-05` passed 25/25 on Sol high against immutable `4296647` controls;
`SSR-04` classified non-software portability as preservation coverage. Pre-approved
fixture, rubric, and prompt repairs restarted their affected scenarios at zero and
left the skill and hooks unchanged. The final independent cold review found no
issues. Repository verification passed: hook suite 263 passed/3 skipped, installer
suite 11 passed, research suite 4 passed, the exact local Markdown-link command
passed, and `git diff --check` passed.

### Task 6: Audit and baseline `writing-explicit-rationale`

**Files:**

- Modify: `skill-validation/writing-explicit-rationale.md`
- Modify: `skill-validation/skill-discovery.md`
- Read control: `skills/writing-explicit-rationale/SKILL.md` at `4296647`

**Required coverage:** link the shared discovery suite; a simple descope; a non-trivial active choice that review could re-litigate; safe direct invocation; non-software extraction using a nonprofit budget or policy exception; reviewer-visibility and trigger-routing regressions.

- [x] Audit current scenarios and map them to the trigger test, on-page location, rationale-content necessity, authoritative reuse, and non-trigger counterexamples.
- [x] Add atomic direct and extraction scenarios without exposing the rubric.
- [x] Run preservation scenarios 5/5 on Sol high at `4296647`; classify a 5/5 portability result as preservation coverage or record a watched RED target.
- [x] Review and commit as `docs(validation): baseline explicit rationale`.

### Task 7: Audit and baseline `adversarial-review`

**Files:**

- Modify: `skills/adversarial-review/SKILL.md`
- Modify: `skill-validation/adversarial-review.md`
- Modify: `skill-validation/README.md`
- Modify if still shared: `skill-validation/duplicate-red-flags-scenarios.md`
- Add: `skill-validation/fixtures/adversarial-review/**`
- Modify: `plans/specs/2026-08-01-comprehensive-skill-cleanup-design.md`
- Read control: `skills/adversarial-review/SKILL.md` at `4296647`

**Required coverage:** link the shared discovery suite; simple review with a concrete defect; non-trivial unverified-rationale plus fragile-invariant review; safe direct invocation with all nine skills available; severity/verdict format; holistic baseline; angle discrimination and selection; durability; whole-repo scope; unexercised cases; fix-by-construction severity.

- [x] Inventory the large historical record and identify the minimal active scenario set that still protects every distinct promise.
- [x] Retain discrimination tests only when the compared arms and scoring remain reproducible.
- [x] Replace unrelated composite regression cells with atomic prompts while preserving their historical result.
- [x] Run every active preservation scenario 5/5 on Sol high at `4296647`.
- [x] Review coverage against the skill's baseline rules and angle table, then commit as `docs(validation): baseline adversarial review`.

Because Task 7 now contains an owner-approved skill behavior slice, its final commit
is the explicit behavioral boundary `docs(skills): strengthen adversarial review output`;
it carries the audit and RED/GREEN evidence with the skill and supersedes the generic
validation-only commit name above. Task 22's readability cleanup remains a separate commit.

**Task 7 execution note (2026-08-04, pre-commit):** The historical families classify
as Keep 0, Repair 7, Merge 2, Retire 1, and Add 7, producing thirteen atomic active
scenarios. Nine preservation scenarios passed 45/45 on both the immutable
`4296647` control and the current draft. `AR-03` reproduced incomplete visible
caller enumeration at 2/5; owner-approved member-by-member accounting brought it
to 5/5. Owner-approved `DD-PATTERN` synthesis and `NONE` branches reproduced at
0/5 and reached 5/5, including a two-unrelated-findings `NONE` branch. Necessity and effectiveness application checks are
preservation coverage at 5/5 each; an `End of posture` probe was retired as
non-discriminating after its full-section ablation also passed 5/5. A replayable
skill-authoring discrimination passes 5/5 on the complete original and current
skills while its holistic-only ablation, with the same authoring dependencies
available, misses both specialized traps at 0/5.
The active current suite is 65/65 with one recovered infrastructure error. Exact prompts, withheld
rubrics, synthetic fixtures, and source manifests are committed replay artifacts.
The approved behavior slice changes the skill from 1,554 to 1,646 words and will
land separately from Task 22's later readability cleanup. Historical source
slices resolve through the former meeting-pipeline checkout and renamed Steno
repository. No hook changed. Cold review and its scoped repair review are clean.
Repository verification and final in-place owner approval are complete; this task's
commit records the approved behavioral boundary and its validation evidence.

### Task 8: Audit and baseline `adversarial-review-loop`

**Files:**

- Modify: `skill-validation/adversarial-review-loop.md`
- Modify: `skill-validation/adversarial-review-loop-scenarios.md`
- Read control: `skills/adversarial-review-loop/SKILL.md` at `4296647`

**Required coverage:** link the shared discovery suite; singular-finding application; non-trivial shared-root and cycle-cap pressure; safe direct invocation with the full bundle; class sweep; P3 stop; re-run discipline; project-wide/cross-language scope; cycle-3 step-back branches; per-task versus whole-branch ownership.

- [x] Reconcile the narrative record with the re-runnable suite and give each distinct active scenario one owner.
- [x] Merge genuine duplicates, retire obsolete 3-repetition variants, and upgrade every retained scenario to the common 5/5 protocol.
- [x] Preserve the existing CS, T2–T7, NF, PW, XL, G3A–G3C IDs when their contracts remain current.
- [x] Run every active preservation scenario 5/5 on Sol high at `4296647`.
- [x] Review branch coverage and commit as `docs(validation): baseline adversarial review loop`.

**Task 8 execution note (2026-08-04, pre-commit):** The active catalog preserves
all thirteen current IDs, canonicalizes the existing ownership transition as
`OWN`, and adds `CE` for the previously untested cold-read result matrix. `T2`
also owns safe direct invocation with the complete nine-skill bundle. Shared
`DISC-01`–`DISC-10` retain Task 1 ownership, while `CW-09` and `CW-11` retain
`concise-writing` ownership. Exact prompt isolation repairs answer leakage,
recurrence coverage, and cycle-state ambiguity without changing the control skill.
All fifteen owned scenarios passed 75/75 on fresh Sol-high control evaluators;
with the 50/50 shared discovery suite and the two 5/5 authoring-boundary targets,
the complete active closure is 135/135. Two fresh Sol-high cold reviews returned
SPEC PASS and QUALITY PASS after the record repairs. No skill or hook changed.

### Task 9: Audit and baseline `dispatching-development-subagents`

**Files:**

- Modify: `skill-validation/dispatching-development-subagents.md`
- Read control: `skills/dispatching-development-subagents/SKILL.md` at `4296647`

**Required coverage:** link the shared discovery suite; simple implementation dispatch; non-trivial nudge/identity/audience pressure; safe direct invocation with the full bundle; scope contract; governing-file reload; no nested dispatch or orchestrator gates; verify-every-commit behavior; upstream report-shape independence.

- [x] Reconcile the three existing tests with the current ownership boundary.
- [x] Link the shared discovery result and add missing direct-invocation and returned-commit verification coverage.
- [x] Run every active preservation scenario 5/5 on Sol high at `4296647`.
- [x] Review and commit as `docs(validation): baseline development subagent dispatch`.

**Task 9 execution note (2026-08-04, pre-commit):** The active catalog repairs
historical Tests 2 and 3 as `DSD-01` and `DSD-02`, merges Test 1 into the current
nudge composition, and adds `DSD-03` and `DSD-04` for returned-commit verification
and finding partition. Four owned Sol-high controls passed 20/20; with the current
shared discovery suite, complete active closure is 70/70. Fixture ambiguities were
repaired and restarted at zero. On 2026-08-04, the owner prospectively approved
prompt, fixture, rubric, and validation-record repairs; only skill or hook changes
require a future approval stop.
Final fresh Sol-high cold review returned SPEC PASS and QUALITY PASS.
No skill or hook changed.

### Task 10: Audit and baseline `disciplined-development`

**Files:**

- Modify: `ARCHITECTURE.md`
- Modify: `CLAUDE.md`
- Modify: `MIGRATIONS.md`
- Modify: `README.md`
- Modify: `.claude/commands/dd-log.md`
- Modify: `commands/dd-log.md`
- Modify: `examples/CLAUDE.md-snippet.md`
- Modify: `examples/starter.CLAUDE.md`
- Modify: `skills/disciplined-development/SKILL.md`
- Modify: `skills/dispatching-development-subagents/SKILL.md`
- Modify: `skills/writing-explicit-rationale/SKILL.md`
- Modify: `skills/disciplined-development/hooks/README.md`
- Modify: `skills/disciplined-development/hooks/dd-config.md`
- Modify: `skills/disciplined-development/hooks/hook-recipes-claude-code.md`
- Modify behavior test-first:
  `skills/disciplined-development/hooks/lib/command_match.py`,
  `skills/disciplined-development/hooks/lib/config.py`,
  `skills/disciplined-development/hooks/lib/plan.py`,
  `skills/disciplined-development/hooks/lib/review_record.py`,
  `skills/disciplined-development/hooks/lib/severity.py`,
  `skills/disciplined-development/hooks/lib/state.py`,
  `skills/disciplined-development/hooks/commit_block.py`,
  `skills/disciplined-development/hooks/external_review.py`,
  `skills/disciplined-development/hooks/log_review.py`,
  `skills/disciplined-development/hooks/pre_pr_review.py`, and
  `skills/disciplined-development/hooks/review_nudge.py`
- Modify shared-mechanics call sites without changing cadence policy:
  `skills/disciplined-development/hooks/lib/cleanup.py`,
  `skills/disciplined-development/hooks/discipline_nudge.py`,
  `skills/disciplined-development/hooks/edit_block.py`, and
  `skills/disciplined-development/hooks/edit_counter.py`
- Delete: `skills/disciplined-development/hooks/lib/reviewer_runner.py`
- Modify: `skills/disciplined-development/hooks/lib/dd-defaults.json`
- Modify: `examples/dd-config.full.json`
- Modify tests: `skills/disciplined-development/hooks/tests/test_cleanup.py`,
  `test_command_match.py`, `test_commit_block.py`, `test_config.py`,
  `test_discipline_nudge.py`, `test_edit_block.py`, `test_edit_counter.py`,
  `test_external_review.py`,
  `test_log_review.py`, `test_plan.py`, `test_pre_pr_review.py`,
  `test_review_nudge.py`, `test_review_record.py`, `test_scaffold_smoke.py`,
  `test_severity.py`, and `test_state.py` in the same tests directory
- Modify comments/docstrings only in any other touched hook Python file
- Modify: `skill-validation/adversarial-review-loop.md`
- Modify: `skill-validation/README.md`
- Modify: `skill-validation/disciplined-development.md`
- Modify: `skill-validation/dispatching-development-subagents.md`
- Modify: `skill-validation/fixtures/dispatching-development-subagents/README.md`
- Modify: `skill-validation/fixtures/dispatching-development-subagents/prompts/dsd-02.md`
- Modify: `skill-validation/writing-explicit-rationale.md`
- Add: `skill-validation/fixtures/disciplined-development/`
- Read control: `skills/disciplined-development/SKILL.md` at `4296647`

**Required coverage:** link the shared discovery suite; simple mode-to-child routing; a non-trivial development sequence crossing Gates 1–5; safe direct invocation with all companions; full-suite orchestration; per-task versus whole-branch review ownership; Principle 7 analysis/implementation threshold; description routing.

- [x] Map all five gates, eight principles, and every mode-table row to active scenarios without restating each child procedure.
- [x] Add explicit scenarios for child availability, required versus optional routing, and direct invocation.
- [x] Run every active preservation scenario 5/5 on Sol high at `4296647`.
- [x] Review orchestration coverage and commit the behavior-bearing baseline as `docs(skills): clarify orchestration and rationale`.

**Task 10 behavior boundary:** While the baseline was under review, the owner
approved holistic repairs to Gate 5 and the rationale threshold through
both skill-writing approval gates. The original Task 16 behavior slice already
landed separately in `1678f49`. During Task 10 review, `WER-07` exposed a later
rationale-threshold ambiguity, and the owner approved its repair. That follow-on
repair lands with Task 10 because the final current bundles and cold review cover
the integrated staged candidate, not an intermediate commit. This explicit
behavior-bearing boundary replaces only Task 10's earlier validation-only commit
name; it does not complete the later readability work in Tasks 21 or 25. Parent word
count is 1,998 pre-boundary HEAD / 2,076 current; explicit-rationale is 378 / 372.
Evaluated skill hashes are
`dff55e1348ebde0ec45c8b1861e48c000a5befdbd2f23deb4e857fa1945c93a6`
and `ce0ba16731a31b5e7a08dbd7c12256d6c50b094808f3eb3c349ba4f78acdc482`.
Cycle 3 required only a source-line split in the rationale paragraph; its final hash
is `568b2a61bef3f7694014fb89228f933261837acd4f2b5978b2b8ef55aa108c9f`.
No `DD` behavioral rerun trigger was met. The stricter post-approval rule restarted
the six rationale scenarios, which passed 30/30 with one excluded pre-start
approval-service timeout. The owner later approved one narrow hook-safety repair:
malformed user configuration now falls back to defaults instead of escaping the
hard gates as a non-blocking exit 1.

**Task 10 validation note (2026-08-06):** `DD-01` maps all eight modes,
active companion loading, explicit negatives, and ownership seams; `DD-02` crosses
Gates 1–5; `DD-03` protects Principle 7. The target controls reproduced their
watched failures, and the then-current suite closed at 85/85. The final rationale suite
also passed 30/30 after its approved wording and layout repairs.

Whole-repository review cycles 1–3 found replayability, infrastructure-record,
model-tier, governing-plan, architecture, and layout defects. The required cold-read
escape then exposed incomplete owner records and Task 16 history; successor reviews
found the same manifest/ownership pattern plus rubric, inventory, and architecture
drift. The owner rejected restarting self-review after external remediation because
each external rerun already reviews the whole current repository while the PR stays
blocked. A later successor caught the pre-PR hook's advisory-path behavior missing
from its documentation, and the owner approved a holistic documentation and diagram
repair. The next review found five more documentation classes; after their repair,
a successor found six remaining accuracy and stale-coordinate classes. The owner
approved the one skill-prose repair, and its affected `DSD-02`, `DD-01`, and
`DD-02` scenarios passed fresh 5/5 reruns. Later successors found and prompted
repairs to the review-log producer inventory, two opaque hook-test coordinates,
the review-loop diagram's cap/logging transitions, the commit matcher's existing
direct-command boundary, hook-extension guidance, and Task 10's file inventory.
All seven diagrams render. An intermediate docstring-stripped AST comparison
against the Task 10 base covered all 30 changed Python files: 27 were identical;
`log_review.py` differs only in two user-facing strings that now describe an
attempted write accurately, `lib/config.py` contains the approved malformed-config
containment, and `tests/test_config.py` contains its regression. No other hook
control flow or state behavior changed. The
latest successor found that the curated-log
docs still guaranteed a row for every attempt and that this history retained
superseded pending-review statements. The log contract is now explicitly
best-effort with its pre-log omissions enumerated. Its successor found remaining
producer-facing guarantees of trace persistence. All cited producers and diagrams
now say that recording is attempted and that PASS-driven cadence reset is
independent of a successful trace write. Its successor found five remaining
summary and record classes: state-reset terminology, best-effort producer
summaries, consumer onboarding, Task 10 inventory, and a historical bundle
label. Its successor found `DD_CODEX_BIN` missing from both hook configuration
summaries. The next successor found two residual PASS/trace statements, now
repaired, and a malformed-config path that could make all three hard gates exit 1.
The owner approved a test-first repair to the shared loader's existing
discard-on-failure contract. Its focused regression passed, the focused config and
hard-gate set passed 22/22, malformed-config process probes now exit 0, 0, and 2
rather than 1, and the complete hook suite passed 264 with 3 skipped. Its
successor found two documentation
misses: the bundle-local `/dd-log` variant still guaranteed trace persistence,
and a test header mislabeled the shared row builder as the sole producer. Both
secondary surfaces now use the current contract. Its successor found two more
stale-model classes: hook onboarding
still grouped the independent pre-PR backstop into edit/commit cadence, and two
emitted messages plus their references counted from the "last deep review"
rather than the review checkpoint or fork-base fallback. The owner approved the
hook-prose repair. Four focused assertions failed on the old wording and passed
after the repair, and the complete hook suite again passed 264 with 3 skipped.
The then-current AST boundary was 27 unchanged files plus the approved user-facing
prose in `commit_block.py`, `review_nudge.py`, and `log_review.py`; the approved
loader containment in `lib/config.py`; and their regressions in
`tests/test_commit_block.py`, `tests/test_review_nudge.py`, and
`tests/test_config.py`. No gate condition, threshold, state mutation, or exit
behavior beyond the recorded malformed-config repair changed. The next
successor found the stale DSD-02 hook quotation and hashes, an overstated
wrapper-output guarantee, an incomplete state inventory and commit-state edge,
P3-dropping `/dd-log` instructions, and the overbroad exit-behavior claim above.
The fixture, records, hook documentation and comments, slash-command variants,
architecture summary, and commit-state diagram now match the executable
behavior. DSD-02 restarted at zero against the refreshed read-only bundle and
passed 5/5 fresh Sol-high repetitions with no infrastructure errors. Its
successor found three high-level documentation classes: reviewer verdict and
effective-decision conflation, incomplete advisory-pass output descriptions,
and obsolete review-diff and plan/spec-path data flow. The hook summaries,
configuration table, plan-resolver docstring, and repository guidance now use
the branch-specific executable contracts. Its successor found stale predecessor
and cutover history in five live hook docstrings and comments, including a claim
that wrapper recursion mattered only to a retired gate. Those surfaces now state
the current direct-command, active-plan, wiring, and wrapper invariants while
the negative regression assertions remain intact. Its successor found two final
bookkeeping omissions: the Task 10 inventory now names the staged validation
index, and the then-current 32-file AST boundary was recorded as 25 unchanged
plus seven approved differences. Its successor found eight residual
migration-relative test comments. The complete live class now states current
invariants; related headings, the unsupported plan-key comment, and stray-event
guidance were repaired in the same sweep while necessary negative assertions
and technical Git rationale remain. The resulting 34-file AST boundary was 27
unchanged plus the same seven approved differences. Its successor found that an
advisory-normalized PASS message overclaimed every finding matched an advisory
path even though unrelated P3 findings do not participate in that decision. The
owner approved a test-first hook-prose repair. A mixed P2/P3 regression failed
on the old message and passed after it was narrowed to all P0-P2 findings. The
same consistency pass made onboarding and recipe guidance explicit that
`dd-log` records every round and resets cadence only on a derived PASS. The
final 34-file AST boundary is 25 unchanged plus nine approved differences,
adding only `external_review.py` and its regression to the prior seven. The next
successor found two residual transition-era statements. The matcher now names
the current commit ceiling and post-commit nudge directly, and the loop owner
record states that parent linkage is complete rather than future Task 10 work.
Its successor found the remaining producer-facing recovery messages still
implied that logging one review resets cadence, two completed audit-index rows
still said their mapping was pending, and a config-test comment named a removed
consumer. The index and comment now state current ownership. The owner approved
a test-first holistic hook-prose repair: six focused assertions failed on the
old recovery text and passed after all four hook messages adopted “log every
round” and “Only a PASS resets.” The final 37-file AST boundary is 24 unchanged
plus 13 approved differences. The next successor found that `DSD-02`'s quoted
T2 message and evaluated hashes predated that recovery-text repair. The active
prompt and four-file manifest now match the staged bytes, the prior 5/5 remains
historical evidence, and `DSD-02` restarted at zero. The orchestrator then
manually scored five fresh external repetitions P / P / P / P / P with zero
infrastructure errors. The current arm is 5/5, restoring dispatch closure to
70/70 and parent closure to 85/85.
The next external review found two residual best-effort persistence overclaims; a documentation/comment-only repair now describes downgraded findings as included in the attempted trace write and states that PASS resets the edit counter independently of logging success.

**Approved dumb-hooks simplification (2026-08-07).** The next Gate 5 review
proved that target-changing Git and GitHub commands can make the hooks inspect a
different repository from the command. The owner approved a broader repair under
the repository's “dumb hooks, smart models” posture:

- For matching commit/PR actions, accept only the payload cwd as repository.
  Repository selectors—including `gh --repo` / `-R`, `GH_REPO`, `git -C`,
  `GIT_DIR`, `--git-dir`, and `--work-tree`—are unresolved.
  `pre_pr_review.py` and `commit_block.py` block unresolved matching commands
  with a rewrite/bypass instruction. A post-commit `review_nudge.py` emits only
  its Gate 3 verification reminder when the target is unresolved; it never reads
  cadence state from the caller's repository. Inline or inherited `GH_REPO`
  makes a PR target unresolved. Inline or inherited `GIT_DIR`, `GIT_WORK_TREE`,
  or `GIT_COMMON_DIR` makes a commit target unresolved. Remove all four from
  hook-owned Git probes and the external-review subprocess so
  `git -C <resolved-repo>` / `codex exec --cd <resolved-repo>` governs the
  operation. A matching command with absent or non-string payload `cwd` is
  unresolved; never substitute the process cwd.
- Keep command detection narrow. A supported commit or PR create is one
  standalone direct Bash command in the payload cwd. A top-level `&&` command
  containing a recognizable direct `git commit` or `gh pr create` is an
  unresolved match, whether the action has a prefix, a suffix, or follows
  `cd <path>`. The commit and pre-PR gates block it without reading or
  delegating against repository state and instruct the model to run the action
  as a standalone Bash call from the target repository, with other commands in
  separate calls. Unrelated `&&` commands remain outside both gates. Keep `;`,
  `||`, and `|` around either action unresolved, and keep shell-wrapped commits
  outside the direct-commit boundary without adding a loose commit substring
  detector. The existing loose PR-shaped net continues to block unresolved
  wrapped PR commands. Determine whether a recognizable direct commit landed
  from a zero tool-response exit code while excluding `--dry-run`; an
  unsupported zero-exit compound commit may therefore receive Gate 3
  verification only, without cadence lookup. Do not infer success from Git
  stdout or model arbitrary shell behavior.
- Trust explicit review verdicts. `external_review.py` maps reviewer `PASS` to
  allow and reviewer `BLOCK` to block. Remove `pr_review.advisory_paths` and the
  hook-side finding downgrade; accepted exceptions belong in reviewer guidance
  or the human bypass, not a parser that reverses the reviewer.
- Require every `dd-log` input to end with an explicit `DD-VERDICT: PASS|BLOCK`.
  Missing or malformed verdicts are usage errors and never reset cadence.
  Structured finding parsing may remain for telemetry, but it cannot derive or
  override the decision.
- Resolve the active plan only from `DD_ACTIVE_PLAN` or
  `.claude/active-plan`. Remove newest-mtime fallback and
  the entire `plans` config block (`active_plan_pointer` and `fallback_glob`);
  the pointer location is fixed. The discipline nudge reports an unpinned plan;
  external review fails closed before launch when no plan is pinned. Anchor a
  relative pin to the resolved repository root. An explicit missing or
  unreadable plan remains the selected pin so the nudge can name it, but the
  external gate rejects it before launching the reviewer. For an absent,
  missing, or unreadable plan pin, do not launch the reviewer or reset state;
  return 1 and attempt an ERROR telemetry row with reason `plan_unavailable`.
- Replace the bespoke reviewer runner with a standard timeout-bounded subprocess
  call. Preserve missing-binary, timeout, abnormal-exit, empty-output, final
  verdict, temporary-output cleanup, and fail-closed behavior.
- Centralize the repeated mechanical repository/branch and
  checkpoint-or-fork-base calculations in `lib/state.py`; every consumer uses
  the same result.

The external-review machinery remains independently configurable and
orchestrator-owned: preserve target-repository config resolution,
`review.reviewer`, `review.model`, `review.effort`, `DD_CODEX_BIN`, the
whole-repository plan-anchored prompt, `codex exec --cd`, read-only sandboxing,
the cleanup-only no-agent wrapper, timeout, last-message capture, best-effort
telemetry, and fail-closed PR translation. Preserve all cadence thresholds,
three hard gates, repeated edit nudging, both Gate 5 external-review moments,
and the smoke result in this Gate 2 artifact. This slice does not authorize a
telemetry-schema reduction or cadence-policy change.

The external command contract remains
`<DD_CODEX_BIN> exec --cd <repo> [-m <review.model>] [-c
model_reasoning_effort=<review.effort>] -s read-only -o <last-message-file>
<prompt>`. `review.model` selects a model independently of the orchestrator;
`review.effort` selects its reasoning effort; `review.reviewer` labels the
telemetry row and does not select the binary. `DD_CODEX_BIN` selects the
executable or enforcement wrapper. Launch the reviewer with the inherited
environment minus `GH_REPO`, `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_COMMON_DIR`
so those selectors cannot redirect its repository.

Implement test-first. Matcher and hard-consumer tests cover the standalone
payload-cwd form; `prefix && action`, `action && suffix`, and
`cd <path> && action` as unresolved matches; and unrelated `&&` commands as
outside both gates. Preserve selector coverage. Consumer regressions prove that
the pre-PR and commit gates never inspect caller state for another target and
that the post-commit hook emits verification-only on unresolved targets.
External-review tests pin configured model/effort argv, target-repository config,
read-only execution, timeout, every fail-closed branch, direct verdict mapping,
and no-plan failure. `dd-log` tests pin explicit PASS/BLOCK and missing-verdict
no-reset behavior. Shared-state tests pin current/detached branch resolution,
checkpoint preference, stale-checkpoint fork-base fallback, and unresolved Git.
Update all hook docs, examples, migration guidance, architecture diagrams, and
validation instructions to the executable contract; remove obsolete runner,
advisory-path, and fallback-plan references.

**Implementation interfaces and inventory:**

This approved slice supersedes Task 10's earlier Python-change restrictions,
AST boundary, and regression-file list; those earlier statements remain only as
chronology for the candidate that preceded this approval.

- `lib/command_match.py` exposes
  `find_git_commit(command, base_cwd, env=None) -> str | None` and
  `find_gh_pr_create(command, base_cwd, env=None) -> str | None`; `env=None`
  reads `os.environ`. `is_git_commit` remains the direct-command discriminator
  that lets callers distinguish no match from an unresolved match.
  `looks_like_gh_pr_create` remains only the pre-PR fail-closed net.
  `commit_landed` uses a recognizable direct commit plus tool exit status so an
  unsupported compound can still trigger verification-only. Both matchers
  return the absolute payload cwd only for a standalone supported action; they
  return `None` for a matching compound. Consumers resolve a returned cwd
  through `state.repo_root`; failure to obtain a Git top-level follows the
  unresolved matching-command behavior.
- `lib/state.py` exposes `current_branch(repo) -> str` (`"detached"` on
  detached HEAD or failure) and
  `review_distance(repo, branch, trunks) -> tuple[int | None, str | None]`,
  where the basis is `"checkpoint"`, `"fork_base"`, or `None`. Preserve the
  ancestor check before checkpoint counting. Migrate all production copies to
  these helpers; do not build a general hook framework.
- `lib/review_record.py` requires callers to pass `decision` explicitly as
  `PASS`, `BLOCK`, or `ERROR`; it may parse findings only for telemetry counts.
  `lib/severity.py` keeps `parse_verdict` and telemetry-only `parse_findings`
  but deletes advisory-path rewriting. `log_review.py` parses the final verdict
  before building a row and returns exit 2 without logging or resetting when it
  is absent or malformed.
- Modify behavior in `pre_pr_review.py`, `commit_block.py`, `review_nudge.py`,
  `external_review.py`, `log_review.py`, `lib/command_match.py`, `lib/plan.py`,
  `lib/review_record.py`, `lib/severity.py`, and `lib/state.py`. Migrate exact
  repository/branch or distance copies in `edit_counter.py`, `edit_block.py`,
  `cleanup.py`, and `log_review.py` without changing their user-visible
  cadence. Modify `discipline_nudge.py` only to use the shared context helper
  and replace fallback plan discovery with the explicit unpinned-plan message.
  Delete `lib/reviewer_runner.py`.
- Update `lib/dd-defaults.json`, `examples/dd-config.full.json`, both `dd-log`
  command variants, the three hook docs, `README.md`, `ARCHITECTURE.md`,
  `MIGRATIONS.md`, relevant examples, and Gate 5 validation instructions.
  Apply the standalone-call recovery above to agent-facing hook output, docs,
  and examples. Remove the obsolete reviewer-runner import smoke assertion.
- Test in `test_command_match.py`, `test_pre_pr_review.py`,
  `test_commit_block.py`, `test_review_nudge.py`, `test_external_review.py`,
  `test_log_review.py`, `test_review_record.py`, `test_plan.py`,
  `test_state.py`, `test_config.py`, `test_cleanup.py`,
  `test_discipline_nudge.py`, `test_severity.py`, `test_edit_counter.py`,
  `test_edit_block.py`, and `test_scaffold_smoke.py`. Remove advisory-rewrite
  expectations while preserving verdict and finding parsing; prove that the
  shared-helper migrations leave edit cadence unchanged. Add a consumer-level
  regression before each corresponding production change and record the
  expected RED cause. Run the focused files after each GREEN, then the complete
  hook suite with
  `cd skills/disciplined-development/hooks && python3 -m pytest -q`.

**Task 10 Gate 5 cycle-1 validation note (2026-08-07):** The current
`DSD-02` bundle at content-manifest SHA-256
`487178d1656de7513a8139b09ef6b69f42d717eaf2d72c011e1a70d5c74c10f5`
passed five fresh Sol-high, high-effort, read-only/no-agents repetitions after
orchestrator manual scoring. Runs 1–5 were P / P / P / P / P across all four
rubric criteria, with zero infrastructure errors. The prior 5/5 arm remains
historical; current dispatch closure is 70/70 and parent closure is 85/85.

**Task 10 Gate 5 completion (2026-08-07).** The orchestrator's final
whole-repository self-review passed after correcting three non-behavioral
comment/documentation inaccuracies; no P0–P2 findings remained. Because Codex
orchestrated this session, the owner authorized the relevant repository,
worktree, diff, plan, and derived validation artifacts for read-only review by
Anthropic through the local Claude CLI. The final independent review ran after
self-review with this command:

```bash
claude -p --model claude-opus-4-8 --effort high --safe-mode \
  --no-session-persistence --permission-mode plan \
  --tools Read,Glob,Grep,Bash \
  --disallowedTools Edit,Write,NotebookEdit,WebFetch,WebSearch,Task \
  --output-format text < /private/tmp/task10-claude-external-review-prompt.md
```

That fresh Opus 4.8 high-effort review recomputed the load-bearing hashes and
word counts, traced the matcher, gate, plan, state, verdict, logging, and
consumer paths, checked the skill/documentation/validation contracts, found no
issues, and ended `DD-VERDICT: PASS`. No secrets, credentials, unrelated files,
write tools, web tools, or nested agents were supplied.

After the external PASS, the orchestrator ran:

```bash
python3 /private/tmp/task10-gate5-smoke.py \
  /Users/simon/work/personal/disciplined-development-skills/.worktrees/comprehensive-skill-cleanup
```

The hermetic real-entry-point smoke exited 0. It proved: standalone commit
allow, commit-compound block, unrelated-compound allow; unresolved landed
compound verification-only; standalone PR delegation to the canonical payload
repository, PR-compound block before delegation; no-plan external-review
fail-closed before launch; and explicit-PASS logging with edit reset and HEAD
checkpoint stamp. The final regression results were hook suite 373 passed / 3
skipped, installer suite 11 passed, and research suite 4 passed.

### Task 11: Record the Sol-low control scores

**Files:**

- Modify: `skill-validation/README.md`
- Modify: `skill-validation/skill-discovery.md`
- Modify: all nine `skill-validation/<skill>.md` records
- Modify: every active shared or supporting scenario record established in Tasks 1–10, including `skill-validation/adversarial-review-loop-scenarios.md`

**Produces:** Five Sol-low control-tree outcomes for every frozen preservation and target scenario, directly comparable with the Sol-high baseline results.

- [x] Freeze the scenario files and rubrics established in Tasks 1–10.
- [x] Run every frozen preservation and target scenario five times against `4296647` with `gpt-5.6-sol` at low reasoning effort and otherwise identical context.
- [x] Record 0–5 scores and exact missed criteria; do not change skill wording in response.
- [x] Add a compact cross-skill score table to `skill-validation/README.md`.
- [x] Record the freeze commit and hashes; any later scenario-contract change follows the global control-backfill rule before execution continues.
- [x] Review counts against the catalog, run `git diff --check`, and commit as `docs(validation): record Sol-low control scores`.

**Task 11 execution note (2026-08-07):** The orchestrator froze the 81-scenario catalog at `db985d203fdbe812dc5161f63565e6e2021f0872` (tracked validation archive `7e626ccc1dd2c596e54688dfaa32a6c090e4f4c50c1ea293352669051f0b4f8b`; canonical 125-file manifest `bbb4fdaa873aa009715bf815d18ab148eac831c92aa00fa647dfa2ca5390751d`) and ran 405 fresh `gpt-5.6-sol` low-effort, read-only/no-agents responses with maximum concurrency three, zero infrastructure errors, and zero retries. The original-control archive/content-manifest pair was `8f21c8267d005c349702ec94d6aff26c13a09bfbe29f2b43efcfbb37304f16e3` / `e2249c4b24132523f1374d506957197a303314e2bfbc6e32c9c1b233909cbbff`; `WER-07` used its catalog-declared frozen mixed-control exception rather than pure `4296647` bytes. Codex CLI 0.147.0 passed the enforced transport probe. A separate high-effort scorer completed 81 isolated packets/405 slots with zero infrastructure errors, after which the orchestrator manually adjudicated every output against its withheld rubric. Preservation scored 237/300, targets 15/105, and the full suite 252/405. These REDs remain recorded control behavior, not fixes.

**Task 11 Gate 5 completion (2026-08-07).** The orchestrator's
whole-repository self-review found no P0–P2 issues after the task-level review
removed ambiguous historical metadata, duplicate detailed outcomes, and the
current loop results' accidental placement inside a historical collapsed block.
Because Codex orchestrated this session, the owner authorized the relevant
repository, worktree, diff, plan, and derived Task 11 validation artifacts for
read-only review by Anthropic through the local Claude CLI. The independent
review used a fresh Opus 4.8 high-effort context with this command:

```bash
claude -p --model claude-opus-4-8 --effort high --safe-mode \
  --no-session-persistence --permission-mode plan \
  --add-dir /private/tmp/dd-task11.LoaSbS \
  --tools Read,Glob,Grep,Bash \
  --disallowedTools Edit,Write,NotebookEdit,WebFetch,WebSearch,Task \
  --output-format text < /private/tmp/dd-task11.LoaSbS/gate5-claude-review-prompt.md
```

That review independently recomputed the four freeze/control hashes, counted
the 405 low-effort runs and 81 scorer packets, reconciled every family score and
row owner, found no P0–P2 issues, and ended `DD-VERDICT: PASS`. Its sole P3
observed that the commit checkbox necessarily becomes historically true only
when this task commit lands. No secrets, credentials, unrelated files, write
tools, web tools, or nested agents were supplied.

After the external PASS, the orchestrator ran the Task 11 runner and scorer
dry-runs (81 scenarios, 405 commands/slots, maximum concurrency three, zero
source/hash errors), reconciled all 81 canonical rows/405 verdict slots against
the manual ledger, recomputed the 60/21 scenario split and 252/405 aggregate,
reverified the four recorded hashes and 125-file manifest, and passed the exact
local Markdown-link command plus `git diff --check`. The final regression
results were hook suite 373 passed / 3 skipped, installer suite 11 passed, and
research suite 4 passed.

### Task 12: Resolve `concise-writing` portability, if the control is RED

**Files:**

- Modify when RED: `skills/concise-writing/SKILL.md`
- Modify: `skill-validation/concise-writing.md`

- [ ] Inspect the recorded extraction result; if it is 5/5, classify it as preservation coverage, update the plan/index, run the local Markdown-link command and `git diff --check`, and commit as `docs(validation): confirm concise writing portability` without a separate skill-change PR boundary.
- [ ] If RED, show the observed failure and proposed minimal dependency/domain-neutrality change, then wait for user approval.
- [ ] If RED, apply only the approved change needed for portable extraction while preserving software examples and current software scenarios.
- [ ] If RED, run the target scenario to 5/5 GREEN and rerun the complete affected active suite 5/5 on Sol high.
- [ ] If RED, run cold skill-writing review; show proposed fixes, wait for user approval, apply them, and restart affected scenarios.
- [ ] If RED, show the edited skill in place and wait for final user approval.
- [ ] If RED, after final approval, run repository tests and commit the behavioral slice separately.

### Task 13: Resolve `disciplined-research` portability, if the control is RED

**Files:**

- Modify when RED: `skills/disciplined-research/SKILL.md`
- Modify: `skill-validation/disciplined-research.md`

- [ ] Inspect the recorded extraction result; if it is 5/5, classify it as preservation coverage, update the plan/index, run the local Markdown-link command and `git diff --check`, and commit as `docs(validation): confirm disciplined research portability` without a separate skill-change PR boundary.
- [ ] If RED, show the failure and a minimal change that keeps sibling sweep/rationale references optional while preserving development examples, then wait for user approval.
- [ ] If RED, apply only the approved source-acquisition, verification, or citation boundary change needed for extraction.
- [ ] If RED, establish target 5/5 GREEN and rerun the complete affected active suite 5/5 on Sol high.
- [ ] If RED, run cold skill-writing review; show proposed fixes, wait for user approval, apply them, and restart affected scenarios.
- [ ] If RED, show the edited skill in place and wait for final user approval.
- [ ] If RED, after final approval, run repository tests and commit the behavioral slice separately.

### Task 14: Resolve `lean-plan-writing` portability, if the control is RED

**Files:**

- Modify when RED: `skills/lean-plan-writing/SKILL.md`
- Modify: `skill-validation/lean-plan-writing.md`

- [ ] Inspect the recorded extraction result; if it is 5/5, classify it as preservation coverage, update the plan/index, run the local Markdown-link command and `git diff --check`, and commit as `docs(validation): confirm lean plan writing portability` without a separate skill-change PR boundary.
- [ ] If RED, show the failure and a minimal change that retains `superpowers:writing-plans` while making prose-as-contract usable for non-software plans, then wait for user approval.
- [ ] If RED, apply only the approved portability change and preserve every software plan requirement.
- [ ] If RED, establish target 5/5 GREEN and rerun the complete affected active suite 5/5 on Sol high.
- [ ] If RED, run cold skill-writing review; show proposed fixes, wait for user approval, apply them, and restart affected scenarios.
- [ ] If RED, show the edited skill in place and wait for final user approval.
- [ ] If RED, after final approval, run repository tests and commit the behavioral slice separately.

### Task 15: Resolve `sweeping-stale-references` portability, if the control is RED

**Files:**

- Modify when RED: `skills/sweeping-stale-references/SKILL.md`
- Modify: `skill-validation/sweeping-stale-references.md`

- [ ] Inspect the recorded extraction result; if it is 5/5, classify it as preservation coverage, update the plan/index, run the local Markdown-link command and `git diff --check`, and commit as `docs(validation): confirm stale reference sweeping portability` without a separate skill-change PR boundary.
- [ ] If RED, show the failure and a minimal change that keeps search/triage/reconcile portable, then wait for user approval.
- [ ] If RED, apply the approved wording that keys Git commit evidence to version-controlled software changes and preserves the existing software commit-body contract.
- [ ] If RED, establish target 5/5 GREEN and rerun the complete affected active suite 5/5 on Sol high.
- [ ] If RED, run cold skill-writing review; show proposed fixes, wait for user approval, apply them, and restart affected scenarios.
- [ ] If RED, show the edited skill in place and wait for final user approval.
- [ ] If RED, after final approval, run repository tests and commit the behavioral slice separately.

### Task 16: Implement the approved `writing-explicit-rationale` behavior slice

**Files:**

- Modify: `CLAUDE.md`
- Modify: `README.md`
- Modify: `skills/disciplined-development/SKILL.md`
- Modify: `skills/lean-plan-writing/SKILL.md`
- Modify: `skills/writing-explicit-rationale/SKILL.md`
- Modify: `skill-validation/README.md`
- Modify: `skill-validation/disciplined-development.md`
- Modify: `skill-validation/lean-plan-writing.md`
- Modify: `skill-validation/skill-discovery.md`
- Modify: `skill-validation/sweeping-stale-references.md`
- Modify: `skill-validation/writing-explicit-rationale.md`

- [x] Run the approved necessity, authoritative-home, and reference-not-repeat targets against the immutable control; classify each 5/5 result as preservation and each observed failure as a watched RED. Classify `WER-03` portability independently by the same rule.
- [x] Apply only the approved behavior slice: necessary rationale lives in one durable code or project-document home; existing rationale is referenced rather than repeated; why and history are included only when they affect correctness or future decisions.
- [x] For each section and the whole skill, remove any structure that does not preserve a distinct necessary behavior.
- [x] Establish target 5/5 GREEN and rerun the complete affected active suite on Sol high. The rationale suite is 5/5; the pairing-only LP-01 preservation rerun was 4/5 because one evaluator used an unrelated upstream test-only commit. The owner explicitly accepted that recorded variance on 2026-08-03 because WER-07 directly covers the changed companion behavior at 5/5 and no rationale or lean-body change caused the miss.
- [x] Run cold skill-writing review; stop for user approval before applying any additional skill-prose finding, and restart affected scenarios after an approved repair.
- [x] Show the complete edited skill in place and wait for final user review before committing.
- [x] After final approval, run repository tests and commit the behavioral slice
  separately as `1678f49` (`docs(skills): make rationale durable and
  nonduplicative`). The later rationale-threshold repair approved during Task 10
  review is tracked in Task 10's explicit behavior boundary.

### Task 17: Clean `concise-writing`

**Files:** `skills/concise-writing/SKILL.md`, `skill-validation/concise-writing.md`

**Review focus:** integrate Role/Owns/Overview without repetition; order the core test, two-altitude pass, patterns, guard, and optional composition naturally; retain the rationalization table and one distinct example.

- [ ] Record the immediate readability-control word count and a section-level meaning inventory.
- [ ] Draft the smallest coherent reorganization, show the diff, and wait for user approval.
- [ ] Apply the approved draft, preserving every active promise.
- [ ] Run the complete active suite 5/5 on Sol high and blindly compare subjective prose outputs with the immediate readability control.
- [ ] Run cold editorial and skill-writing review; show proposed fixes, wait for user approval, apply them, and restart affected scenarios.
- [ ] Show the final skill in place and wait for user approval.
- [ ] After approval, run repository tests and commit as `docs(skills): clean up concise writing`.

### Task 18: Clean `disciplined-research`

**Files:** `skills/disciplined-research/SKILL.md`, `skill-validation/disciplined-research.md`

**Review focus:** clarify when the skill applies; make acquire/verify facets flow as one method; remove overlap among overview, rationalizations, and red flags; keep optional suite composition out of the portable core.

- [ ] Record the immediate readability-control word count and a section-level meaning inventory.
- [ ] Draft the smallest coherent reorganization, show the diff, and wait for user approval.
- [ ] Apply the approved draft and run the complete active suite 5/5 on Sol high.
- [ ] Blindly compare subjective prose outputs with the immediate readability control where the rubric requires judgment.
- [ ] Run cold editorial and skill-writing review; show proposed fixes, wait for user approval, apply them, and restart affected scenarios.
- [ ] Show the final skill in place and wait for user approval.
- [ ] After approval, run repository tests and commit as `docs(skills): clean up disciplined research`.

### Task 19: Clean `lean-plan-writing`

**Files:** `skills/lean-plan-writing/SKILL.md`, `skill-validation/lean-plan-writing.md`

**Review focus:** explain the Superpowers override once; order prose contract, tricky-case table, artifact distinction, merge boundary, and rationalizations; keep software examples without making the core software-only.

- [ ] Record the immediate readability-control word count and a section-level meaning inventory.
- [ ] Draft the smallest coherent reorganization, show the diff, and wait for user approval.
- [ ] Apply the approved draft and run the complete active suite 5/5 on Sol high.
- [ ] Blindly compare subjective prose outputs with the immediate readability control where the rubric requires judgment.
- [ ] Run cold editorial and skill-writing review; show proposed fixes, wait for user approval, apply them, and restart affected scenarios.
- [ ] Show the final skill in place and wait for user approval.
- [ ] After approval, run repository tests and commit as `docs(skills): clean up lean plan writing`.

### Task 20: Clean `sweeping-stale-references`

**Files:** `skills/sweeping-stale-references/SKILL.md`, `skill-validation/sweeping-stale-references.md`

**Review focus:** make search/triage/reconcile the obvious portable core; condition the software audit artifact correctly; integrate quick reference, scope, example, and rationalizations without restatement.

- [ ] Record the immediate readability-control word count and a section-level meaning inventory.
- [ ] Draft the smallest coherent reorganization, show the diff, and wait for user approval.
- [ ] Apply the approved draft and run the complete active suite 5/5 on Sol high.
- [ ] Blindly compare subjective prose outputs with the immediate readability control where the rubric requires judgment.
- [ ] Run cold editorial and skill-writing review; show proposed fixes, wait for user approval, apply them, and restart affected scenarios.
- [ ] Show the final skill in place and wait for user approval.
- [ ] After approval, run repository tests and commit as `docs(skills): clean up stale reference sweeping`.

### Task 21: Clean `writing-explicit-rationale`

**Files:** `skills/writing-explicit-rationale/SKILL.md`, `skill-validation/writing-explicit-rationale.md`

**Review focus:** state the trigger once; order trigger, non-trigger cases, rationale shape, artifact placement, and failure resistance; consolidate overlapping rationalizations/red flags while preserving compliance.

- [ ] Record the immediate readability-control word count and a section-level meaning inventory.
- [ ] Draft the smallest coherent reorganization, show the diff, and wait for user approval.
- [ ] Apply the approved draft and run the complete active suite 5/5 on Sol high.
- [ ] Blindly compare subjective prose outputs with the immediate readability control where the rubric requires judgment.
- [ ] Run cold editorial and skill-writing review; show proposed fixes, wait for user approval, apply them, and restart affected scenarios.
- [ ] Show the final skill in place and wait for user approval.
- [ ] After approval, run repository tests and commit as `docs(skills): clean up explicit rationale`.

### Task 22: Clean `adversarial-review`

**Files:** `skills/adversarial-review/SKILL.md`, `skill-validation/adversarial-review.md`

**Review focus:** preserve direct invocation within the full bundle; order posture, severity/output contract, holistic rules, angle selection, examples, and composition; keep the baseline/angle distinction unmistakable; remove historical bolt-on seams without shrinking coverage.

- [ ] Record the immediate readability-control word count and a section-level meaning inventory.
- [ ] Draft the smallest coherent reorganization, show the diff, and wait for user approval.
- [ ] Apply the approved draft and run the complete active suite plus affected composition scenarios 5/5 on Sol high.
- [ ] Blindly compare subjective review outputs with the immediate readability control where the rubric requires judgment.
- [ ] Run cold editorial and skill-writing review; show proposed fixes, wait for user approval, apply them, and restart affected scenarios.
- [ ] Show the final skill in place and wait for user approval.
- [ ] After approval, run repository tests and commit as `docs(skills): clean up adversarial review`.

### Task 23: Clean `adversarial-review-loop`

**Files:** `skills/adversarial-review-loop/SKILL.md`, `skill-validation/adversarial-review-loop.md`, `skill-validation/adversarial-review-loop-scenarios.md`

**Review focus:** make scope/precedence, normal loop, class/root attack, three-cycle cap, cold escape, and clean stop read as one state machine; preserve per-task versus whole-branch ownership.

- [ ] Record the immediate readability-control word count and a state/transition meaning inventory.
- [ ] Draft the smallest coherent reorganization, show the diff, and wait for user approval.
- [ ] Apply the approved draft and run every active loop branch plus affected composition scenarios 5/5 on Sol high.
- [ ] Blindly compare subjective remediation outputs with the immediate readability control where the rubric requires judgment.
- [ ] Run cold editorial and skill-writing review; show proposed fixes, wait for user approval, apply them, and restart affected scenarios.
- [ ] Show the final skill in place and wait for user approval.
- [ ] After approval, run repository tests and commit as `docs(skills): clean up adversarial review loop`.

### Task 24: Clean `dispatching-development-subagents`

**Files:** `skills/dispatching-development-subagents/SKILL.md`, `skill-validation/dispatching-development-subagents.md`

**Review focus:** align Role/Overview/When-you-dispatch; state the scope contract once; keep orchestrator verification and subagent gate boundaries explicit; depend on the full development bundle without relying on an upstream report heading.

- [ ] Record the immediate readability-control word count and a section-level meaning inventory.
- [ ] Draft the smallest coherent reorganization, show the diff, and wait for user approval.
- [ ] Apply the approved draft and run the complete active suite plus affected composition scenarios 5/5 on Sol high.
- [ ] Blindly compare subjective dispatch outputs with the immediate readability control where the rubric requires judgment.
- [ ] Run cold editorial and skill-writing review; show proposed fixes, wait for user approval, apply them, and restart affected scenarios.
- [ ] Show the final skill in place and wait for user approval.
- [ ] After approval, run repository tests and commit as `docs(skills): clean up development subagent dispatch`.

### Task 25: Clean `disciplined-development`

**Files:**

- Modify: `skills/disciplined-development/SKILL.md`
- Modify: `skill-validation/disciplined-development.md`
- Modify if routing summaries drift: `ARCHITECTURE.md`, `README.md`
- Modify if cross-references drift: `skills/adversarial-review/SKILL.md`, `skills/adversarial-review-loop/SKILL.md`, `skills/concise-writing/SKILL.md`, `skills/disciplined-research/SKILL.md`, `skills/dispatching-development-subagents/SKILL.md`, `skills/lean-plan-writing/SKILL.md`, `skills/sweeping-stale-references/SKILL.md`, `skills/writing-explicit-rationale/SKILL.md`
- Modify if routing examples drift: `examples/CLAUDE.md-snippet.md`, `examples/starter.CLAUDE.md`

**Review focus:** make the Iron Law, five gates, eight principles, and mode table consistent; route every settled companion at the correct boundary; remove duplicated child procedures; preserve exact review-loop and subagent ownership.

- [ ] Re-read all eight cleaned companion skills and build a parent-to-child ownership matrix.
- [ ] Record the parent's immediate readability-control word count and a gate/principle/mode meaning inventory.
- [ ] Sweep `README.md`, `ARCHITECTURE.md`, examples, and companion cross-references to identify every routing-reference update the parent cleanup requires.
- [ ] Draft and show the parent diff plus every proposed companion and routing-reference diff, then wait for user approval.
- [ ] Apply the approved parent draft and any required routing-reference updates.
- [ ] Run the complete parent suite and every affected composition scenario 5/5 on Sol high.
- [ ] For every companion `SKILL.md` changed in this task, rerun that companion's complete active suite 5/5 and its cold skill-writing review.
- [ ] Rerun the routing-reference sweep; show any newly required edit, wait for approval, apply it, and restart every affected scenario.
- [ ] Blindly compare subjective orchestration outputs with the immediate readability control where the rubric requires judgment.
- [ ] Run cold editorial, skill-writing, consistency, and executability review; show proposed fixes, wait for approval, apply them, and restart affected scenarios.
- [ ] Show the final parent and any changed companion skills in place and wait for user approval.
- [ ] After approval, run repository tests and commit as `docs(skills): clean up disciplined development`.

### Task 26: Run the final Sol-high suite gate

**Files:**

- Modify: `skill-validation/README.md`
- Modify: `skill-validation/skill-discovery.md`
- Modify: all nine per-skill validation records
- Modify: every active shared or supporting scenario record
- Create: `skill-validation/skill-composition.md`

**Required final scenarios:** the shared all-nine description-discovery suite; direct invocation of each of the nine skills with the complete bundle; each portable skill extracted with declared Superpowers dependencies and a non-software task; parent routing across plan, implementation, debugging, review, documentation, and delegation modes; per-task versus whole-branch review ownership.

**Produces:** A cross-suite composition record that links the owning scenario IDs and records joint results without duplicating their prompts or rubrics.

- [ ] Rerun the shared discovery suite, all-nine direct-invocation set, portable-extraction set, and composition set; keep scenarios atomic unless composition is the behavior under test, and run each scenario five times on Sol high.
- [ ] Manually score each protected promise and record any infrastructure failures separately.
- [ ] If any result is below 5/5, stop and classify it through the design's failure gate; correct a cleanup regression in its owning task, and isolate any approved behavioral change in a separate RED/GREEN slice.
- [ ] Record the final 5/5 results and commit as `docs(validation): record final skill composition greens`.

### Task 27: Run the cleaned Sol-low comparison and final repository verification

**Files:**

- Modify: `skill-validation/README.md`
- Modify: `skill-validation/skill-discovery.md`
- Modify: `skill-validation/skill-composition.md`
- Modify: all per-skill validation records with final Sol-low scores
- Modify: every active shared or supporting scenario record with final Sol-low scores
- Move after completion: `plans/2026-08-01-comprehensive-skill-cleanup.md` to `plans/completed/2026-08-01-comprehensive-skill-cleanup.md`
- Move after completion: `plans/specs/2026-08-01-comprehensive-skill-cleanup-design.md` to `plans/completed/specs/2026-08-01-comprehensive-skill-cleanup-design.md`

- [ ] Freeze the final active scenario suite and run every scenario five times on `gpt-5.6-sol` at low reasoning effort.
- [ ] Compare control and cleaned scores by scenario and pause for user review on any decrease.
- [ ] For every decrease, record the user-approved disposition in `skill-validation/README.md` and each affected record.
- [ ] If accepted, record the what/why/accepted rationale; if remediation changes a skill or scenario contract, reopen its owning task, complete the required Sol-high backfill or regression suite, rerun the affected Sol-low arm, and return to this comparison.
- [ ] Record final word-count deltas for all nine skills.
- [ ] Run the hook, installer, and research pytest suites plus `git diff --check`.
- [ ] Run a final cold consistency review against the design and this plan.
- [ ] Mark the plan complete only when every success criterion in the design has evidence.
- [ ] Move the completed plan and design to their completed directories, update the plan's design-reference label and target plus every live repository reference, and run the exact local-link command plus `git diff --check`.
- [ ] Commit as `docs(skills): complete comprehensive cleanup validation`.
