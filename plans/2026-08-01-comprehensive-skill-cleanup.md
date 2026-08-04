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
Invoke Gate 5's external review with the Task 1 scratch `DD_CONFIG` override that pins `gpt-5.6-sol` at high effort, and verify its logged model metadata before the boundary passes.
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
  Define a scratch Gate 5 `DD_CONFIG` project override that pins external review to `gpt-5.6-sol` at high effort, the exact invocation that consumes it, and the logged-metadata check that fails the boundary on mismatch.
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

- [ ] Reconcile the three existing tests with the current ownership boundary.
- [ ] Link the shared discovery result and add missing direct-invocation and returned-commit verification coverage.
- [ ] Run every active preservation scenario 5/5 on Sol high at `4296647`.
- [ ] Review and commit as `docs(validation): baseline development subagent dispatch`.

### Task 10: Audit and baseline `disciplined-development`

**Files:**

- Modify: `skill-validation/disciplined-development.md`
- Read control: `skills/disciplined-development/SKILL.md` at `4296647`

**Required coverage:** link the shared discovery suite; simple mode-to-child routing; a non-trivial development sequence crossing Gates 1–5; safe direct invocation with all companions; full-suite orchestration; per-task versus whole-branch review ownership; Principle 7 analysis/implementation threshold; description routing.

- [ ] Map all five gates, eight principles, and every mode-table row to active scenarios without restating each child procedure.
- [ ] Add explicit scenarios for child availability, required versus optional routing, and direct invocation.
- [ ] Run every active preservation scenario 5/5 on Sol high at `4296647`.
- [ ] Review orchestration coverage and commit as `docs(validation): baseline disciplined development`.

### Task 11: Record the Sol-low control scores

**Files:**

- Modify: `skill-validation/README.md`
- Modify: `skill-validation/skill-discovery.md`
- Modify: all nine `skill-validation/<skill>.md` records
- Modify: every active shared or supporting scenario record established in Tasks 1–10, including `skill-validation/adversarial-review-loop-scenarios.md`

**Produces:** Five Sol-low control-tree outcomes for every frozen preservation and target scenario, directly comparable with the Sol-high baseline results.

- [ ] Freeze the scenario files and rubrics established in Tasks 1–10.
- [ ] Run every frozen preservation and target scenario five times against `4296647` with `gpt-5.6-sol` at low reasoning effort and otherwise identical context.
- [ ] Record 0–5 scores and exact missed criteria; do not change skill wording in response.
- [ ] Add a compact cross-skill score table to `skill-validation/README.md`.
- [ ] Record the freeze commit and hashes; any later scenario-contract change follows the global control-backfill rule before execution continues.
- [ ] Review counts against the catalog, run `git diff --check`, and commit as `docs(validation): record Sol-low control scores`.

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
- [x] After final approval, run repository tests and commit the behavioral slice separately.

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
