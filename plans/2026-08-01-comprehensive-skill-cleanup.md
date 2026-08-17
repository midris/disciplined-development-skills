# Comprehensive Skill Cleanup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` with the orchestrator executing validation-bearing tasks inline. Do not delegate a whole validation-bearing task through `superpowers:subagent-driven-development`; its implementer would be prohibited from dispatching the required evaluator subagents. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish a trustworthy validation baseline, then make all nine skills compact and coherent without losing effectiveness.

**Architecture:** Treat the pinned skill tree at `4296647` as the regression control for original behavior. Build a shared validation protocol and one active scenario catalog per skill, record Sol-high and Sol-low baseline results, then perform behavior-preserving readability cleanup in each skill's intended domain with its declared dependencies. Cold Sol-high supplies the non-Claude portability gate; Sol-low characterizes effort robustness. Clean `disciplined-development` last so it routes settled child contracts.

**Tech stack:** Markdown skills and validation records; `gpt-5.6-sol` evaluation subagents; Superpowers 6.2.0; Git; Python/pytest for repository regression suites.

**Design reference:** [`plans/specs/2026-08-01-comprehensive-skill-cleanup-design.md`](specs/2026-08-01-comprehensive-skill-cleanup-design.md)

## Global constraints

- All skill authoring, validation design, scoring, and cold reviews use `gpt-5.6-sol` at high reasoning effort.
- Portability means that a skill authored and previously exercised with Claude reads and behaves correctly to that cold non-Claude model within its intended domain and with declared dependencies available.
- Domain breadth and standalone/extraction packaging are separate coverage dimensions; neither broadens a skill's authored contract.
- Broad-domain companions are `concise-writing`, `disciplined-research`, and `writing-explicit-rationale`; development companions are `lean-plan-writing` and `sweeping-stale-references`; the integrated development group is `disciplined-development`, `adversarial-review`, `adversarial-review-loop`, and `dispatching-development-subagents`.
- Sol low is used only for the comparative score arms in Tasks 11 and 27 and any control backfill required by the post-freeze rule.
- The orchestrator owns validation-bearing tasks, evaluator, scorer, and reviewer dispatch, the scoring workflow, user approval gates, and commits; evaluators, scorers, and reviewers remain read-only and never dispatch nested agents.
- Every behavioral scenario uses five fresh, read-only evaluators with no nested dispatch; run at most three evaluators concurrently.
- Start each evaluator without inherited conversation history and specify its model, effort, immutable skill bundle, and task context explicitly.
- Use only a probed transport that enforces no-write evaluator access; instruction-only isolation is invalid, and unavailable enforcement blocks validation.
- Evaluator prompts never contain or point to the scoring rubric.
- For subjective comparisons, a separate fresh scorer manually applies the evaluator-withheld rubric to outputs under opaque arm IDs but never receives the control/draft mapping.
- Freeze each subjective scoring record before mapping those IDs back to control and draft.
- Manually score every other completed response; scorer labels are advisory, and the orchestrator counts only misses that change observable action, outcome, ordering, ownership, blocked transition, or truthful bookkeeping.
- Do not fail correct behavior for omitted optional rationale, failure to repeat a supplied fact, or different wording, placement, formatting, or rendering; exact wording can fail only when literal output is itself a necessary owned behavior, and the validity of that promise must still be challenged.
- In every scoring context, a genuine behavioral miss is a failure, not a discarded run.
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
- Behavioral edits and readability edits land in separate commits except the owner-approved Task 17 whole-skill rewrite, which combines its response-routing boundary and readability cleanup in one preservation-first commit.
- A skill's complete active suite includes its owned scenarios and every shared discovery, direct-invocation, domain-appropriate application, dependency, and composition scenario mapped to its promises.
- Every shared or supporting scenario record has one owner and lists every affected skill.
- A whole-skill cleanup reruns that skill's complete active Sol-high suite.
- After Task 11, any change to a scenario prompt, fixture, rubric, supplied context, or protected promise requires fresh Sol-high and Sol-low control results before the scenario is used again.
- Show every skill draft and wait for user approval before applying it; show the final edited file in place and wait for user approval before committing it.
- Any skill edit after final approval returns to the draft/test/in-place approval sequence before commit.
- Skill prose uses one sentence per line with the repository's structural exceptions.
- Each skill commit records applicable control/current word counts, model results, cold review, repository tests, and any reference sweep.
- For skills with a behavior slice, record word counts for `4296647`, the post-slice readability control, and the cleaned version.
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
- Tasks 2–6 form the companion-skill control-baseline boundary.
- Tasks 7–10 form the integrated-development control-baseline boundary.
- Task 11 is the Sol-low control-score boundary.
- Tasks 12–15 are scope and catalog dispositions; Task 16's approved behavior slice retains its own boundary.
- Task 17 combines the approved routing change and whole-skill readability rewrite in one preservation-first boundary.
- Each Task 17–25 skill cleanup is its own boundary.
- Tasks 26–27 form the final validation boundary.

Use one branch/PR per boundary when executing through PRs.
Within a boundary, retain the per-task commits named below so validation history remains reviewable.
Before opening a PR at any boundary, the orchestrator runs the complete Gate 5 whole-branch review and smoke pass.
Gate 5's external reviewer must use a different provider and model family from the orchestrator.
That external review is a separate repository gate, not a second behavioral portability provider requirement.
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
  Record its commit and content hashes, verify the nine live skill files still match it before baseline testing, and define the same procedure for post-behavior-slice readability controls.

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

**Required coverage:** link the shared discovery suite; simple padding removal; non-trivial compression that preserves rationale, navigation, and a load-bearing recap; safe direct invocation; isolated broad-domain application using a policy or grant document; still-relevant verbosity, over-trim, trigger-routing, and red-flag-consolidation regressions.

- [x] Audit existing scenarios and classify each `Keep`, `Repair`, `Merge`, or `Retire`.
- [x] Add only missing coverage; merge the shared composite fixture into atomic skill scenarios where its unrelated output contracts would interfere.
- [x] Record exact prompts, supplied context, rubrics, protected sections, and rerun triggers in the active catalog.
- [x] Run every preservation scenario 5/5 on cold Sol high against `4296647`; classify broad-domain coverage separately from cross-model portability.
- [x] Manually score every response and record exact misses without transcripts.
- [x] Review the record against `skill-validation/README.md`, run `git diff --check`, and commit as `docs(validation): baseline concise writing`.

**Task 2 execution note (2026-08-02):** The audit classified prior scenarios as
Keep 0, Repair 2, Merge 4, and Retire 2, then added six missing atomic scenarios.
`CW-01`–`CW-08` passed 5/5 on Sol high with zero infrastructure errors; `CW-08`
is isolated broad-domain application coverage. The approved Task 2A targets `CW-09`–`CW-12`
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

**Required coverage:** link the shared discovery suite; simple source acquisition and verification; a non-trivial authority/deadline scenario whose premise is disconfirmed; safe direct invocation; isolated broad-domain application using museum, policy, or procurement research; the historical disclaimer-as-substitute and citation-as-substitute experiments, retained or retired honestly.

- [x] Map the skill's claims to existing B1/B17 evidence and distinguish shipped regressions from closed experiments.
- [x] Link the shared discovery result and add atomic application, direct-invocation, and broad-domain scenarios with exact evaluator-withheld rubrics.
- [x] Run preservation scenarios 5/5 on cold Sol high at `4296647`; classify broad-domain coverage separately from cross-model portability.
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
infrastructure errors; `DR-02` is therefore isolated broad-domain preservation coverage.

### Task 4: Audit and baseline `lean-plan-writing`

**Files:**

- Modify: `skill-validation/lean-plan-writing.md`
- Modify if still shared: `skill-validation/duplicate-red-flags-scenarios.md`
- Read control: `skills/lean-plan-writing/SKILL.md` at `4296647`

**Required coverage:** link the shared discovery suite; simple prose-as-contract planning; the non-trivial `KEY=VALUE` parser plan without implementation bodies; safe direct invocation with declared `superpowers:writing-plans`; in-domain software planning; unexercised-case, trigger-routing, and red-flag-consolidation regressions. Preserve the non-software publishing probe only as exploratory cross-domain history.

- [x] Audit and atomize existing scenarios without losing historical results.
- [x] Make the upstream override, input/output-table substitute, and five-line ambiguity exception independently scorable.
- [x] Run preservation scenarios 5/5 on cold Sol high at `4296647`; classify failures through the standard gate.
- [x] Review the active catalog and commit as `docs(validation): baseline lean plan writing`.

Execution note (2026-08-02, in progress): audited the historical families into
`LP-01`–`LP-08`, retained their sourced limitations, and ran five fresh Sol-high
processes per original-control arm. `LP-01` and `LP-05`–`LP-08` preserved their
promises at 5/5. `LP-04` recorded a 4/5 exploratory cross-domain result that is
retired from active coverage by Task 14 and cannot drive a skill change.
The repaired audit counts are Keep 0, Repair 4, Merge 1, Retire 1, and Add 3,
with seven active owned scenarios.
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

**Required coverage:** link the shared discovery suite; a simple load-bearing software rename; the non-trivial 126-match grouped sweep; safe direct invocation in the development domain; reviewer-one-hit, three-way classification, grouping/reconciliation, negative-form, and red-flag-consolidation regressions. Preserve the non-software policy probe only as exploratory cross-domain history.

- [x] Audit the current record and separate the reusable search/triage/reconcile method from its software-specific commit evidence.
- [x] Add atomic prompts and rubrics for literal/synonym search, all required file categories, three classifications, count reconciliation, and grouped evidence.
- [x] Run preservation scenarios 5/5 on cold Sol high at `4296647`; classify failures through the standard gate.
- [x] Review and commit as `docs(validation): baseline stale reference sweeping`.

**Task 5 execution note (2026-08-02):** Audited the historical families as
Keep 0, Repair 2, Merge 0, Retire 1, and Add 2, producing the smallest coherent
four-scenario active suite after a section-by-section and whole-skill simplification review.
The original five scenarios passed 25/25 on Sol high against immutable `4296647`
controls; Task 15 retires `SSR-04` as exploratory cross-domain evidence. Pre-approved
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

**Required coverage:** link the shared discovery suite; a simple descope; a non-trivial active choice that review could re-litigate; safe direct invocation; isolated broad-domain application using a nonprofit budget or policy exception; reviewer-visibility and trigger-routing regressions.

- [x] Audit current scenarios and map them to the trigger test, on-page location, rationale-content necessity, authoritative reuse, and non-trigger counterexamples.
- [x] Add atomic direct and broad-domain scenarios without exposing the rubric.
- [x] Run preservation scenarios 5/5 on cold Sol high at `4296647`; classify broad-domain coverage separately from cross-model portability.
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
The frozen 81-row/405-slot result remains historical fact and is not recomputed.
The then-forecast future active closure contained 82 scenarios: 60 preservation
and 22 target rows, or 410 five-repetition slots. Task 14 retires `LP-04` and Task 15 retires `SSR-04`
without altering their frozen outcomes; Task 17 adds `CW-17`–`CW-19`.
Task 18A has frozen pre-draft targets `DISC-11` and `DR-04`, preservation
scenario `DR-05`, and post-draft unverified-lead target `DR-06`.
Its accepted pre-draft reclassification remains the 17-target,
three-preservation split; `DR-06` is the additional watched target.
At that point, the forecast was 86 scenarios / 430 slots after Task 18A GREEN.
The 2026-08-13 atomic/composite redesign in Task 18A supersedes that forecast;
Tasks 26–27 must recompute final closure without changing this historical Task 11
result.

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

### Task 12: Confirm `concise-writing` broad-domain evidence and portability

**Files:**

- Modify: `skill-validation/concise-writing.md`

- [x] Relabel `CW-08` as isolated broad-domain application coverage without changing its prompt, fixture, rubric, hashes, or scores.
- [x] Confirm cross-model portability from the complete cold Sol-high in-domain suite, retaining declared dependencies and the authored contract.
- [x] Update the plan/index and run the local Markdown-link command plus `git diff --check`; no skill edit or behavioral rerun is required.

**Task 12 historical implementation note (2026-08-07):** The then-canonical
`CW-08` arm was accepted as isolated broad-domain evidence. Cross-model confidence
came from the complete cold Sol-high in-domain suite, and the orchestrator's exact
local-link and diff checks passed before the task commit.

**Task 17 supersession (2026-08-08):** The owner later classified that arm's
`contact the program` source as incomplete and approved the exact-email fixture
repair recorded under Task 17. The old arm is now historical only; the repaired
active arm later passed fresh Sol-high and Sol-low controls 5/5 and the Task 17
candidate arm 5/5.

### Task 13: Confirm `disciplined-research` broad-domain evidence and portability

**Files:**

- Modify: `skill-validation/disciplined-research.md`

- [x] Relabel `DR-02` as isolated broad-domain application coverage without changing its prompt, fixture, rubric, hashes, or scores.
- [x] Confirm cross-model portability from the complete cold Sol-high in-domain suite, retaining the skill's authored contract.
- [x] Update the plan/index and run the local Markdown-link command plus `git diff --check`; no skill edit or behavioral rerun is required.

**Task 13 implementation note (2026-08-07):** The canonical
[`DR-02` result](../skill-validation/disciplined-research.md#control-results) remains
valid isolated broad-domain evidence. Cross-model confidence comes from the complete
cold Sol-high in-domain suite, so no skill edit or evaluation rerun is needed. The
orchestrator's exact local-link and diff checks passed before the task commit.

### Task 14: Repair `lean-plan-writing` validation scope

**Files:**

- Do not modify: `skills/lean-plan-writing/SKILL.md`
- Modify: `skill-validation/lean-plan-writing.md`

- [x] Retire `LP-04` from active coverage as exploratory cross-domain evidence; preserve its exact prompt, fixture, rubric, manifests, hashes, and raw outcomes.
- [x] Record that `lean-plan-writing` remains a development companion with declared `superpowers:writing-plans` composition and seven active owned scenarios.
- [x] Apply the section-level and whole-record necessity/simplification test, update the index and future closure count, and run the local Markdown-link command plus `git diff --check`.

`LP-04` cannot drive a skill change or rerun. No lean skill edit, behavioral
evaluation, Gate 5 run, or portability target follows from its historical 4/5 result.

### Task 15: Repair `sweeping-stale-references` validation scope

**Files:**

- Do not modify: `skills/sweeping-stale-references/SKILL.md`
- Modify: `skill-validation/sweeping-stale-references.md`

- [x] Retire `SSR-04` from active coverage as exploratory cross-domain evidence; preserve its exact prompt, fixture, rubric, manifests, hashes, and raw outcomes.
- [x] Record that `sweeping-stale-references` remains a development companion with four active owned scenarios.
- [x] Apply the section-level and whole-record necessity/simplification test, update the index and future closure count, and run the local Markdown-link command plus `git diff --check`.

`SSR-04` cannot drive a skill change or rerun. No stale-reference skill edit,
behavioral evaluation, Gate 5 run, or portability target follows from its historical
5/5 result.

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

- [x] Run the approved necessity, authoritative-home, and reference-not-repeat targets against the immutable control; classify each 5/5 result as preservation and each observed failure as a watched RED. Treat `WER-03` as isolated broad-domain application coverage.
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

**Approved whole-skill rewrite (2026-08-08):** combine the former Task 17A routing change with the readability cleanup as one preservation-first boundary.
Apply `concise-writing` to prose in project files and durable project records and to response-only prose by default.
When the user explicitly requests a detailed explanation intended only as the agent response, do not select or apply `concise-writing` to that explanation.
Detailed prose written to a project file or durable project record remains in scope even when the accompanying agent response is brief.
Code, structured data, and required syntax remain outside the prose method unless prose itself is the deliverable.
Any loss of readability, meaning, impact, effectiveness, completeness, or correctness is a hard failure.

**CW-08 fixture repair (2026-08-08):** replace the ambiguous accommodation source
with an exact email instruction while preserving every other fact and criterion.
The active prompt/rubric hashes are recorded in the owning validation record; the
old prompt, rubric, and results remain a separate superseded arm. Counts do not
change. Fresh Sol-high and Sol-low active controls passed 5/5, and the final
Sol-high arm also passed 5/5.

**CW-19 fixture repair (2026-08-08):** replace the generic pre-promotion failure
trigger with the readiness thresholds' exact complements: replica lag above 2
seconds and mismatch rate at 0.1% or higher. Preserve the actor-repaired 5/5 as a
separate superseded threshold-ambiguous arm and keep the earlier actor-repetition
rubric-defect arm separate. The first threshold-exact rubric produced historical
sentence-local adjudications of 2/5 on Sol high and 1/5 on Sol low. The owner then
repaired the rubric to evaluate the complete artifact: readiness below 0.1% makes
`reaches 0.1%` an unambiguous at-or-above failure boundary, while generic wording
still fails when it leaves the required `BLOCKED` action at equality ambiguous.
Total scenario and slot counts do not change; classification remains 60
preservation / 22 target.

**Files:** `skills/concise-writing/SKILL.md`, `skill-validation/concise-writing.md`, `skill-validation/README.md`, `skill-validation/skill-discovery.md`, `skill-validation/disciplined-development.md`, `skill-validation/fixtures/disciplined-development/prompts/dd-01.md`, `skill-validation/fixtures/disciplined-development/rubrics/dd-01.md`, `skill-validation/fixtures/disciplined-development/rubrics/dd-02.md`

**Review focus:** make the response-only detailed-explanation exemption and the project-file/record preservation guard explicit; order the complete meaning inventory, draft, local/global compression, equivalence gate, patterns, examples, rationalizations, and composition naturally; retain every active promise without weakening readability, impact, or effectiveness.

**Validation scope:** broad-domain companion with a mandatory full affected rerun on fresh Sol-high contexts.
The 29-scenario affected set is `CW-01`–`CW-14`, `CW-17`–`CW-19`,
`DISC-01`–`DISC-10`, `DD-01`, and `DD-02`, with only scenario-declared dependencies.

- [x] Freeze repaired `CW-08` and `CW-17`–`CW-19` prompts, rubrics, protected promises, complete scenario-specific bundle bytes, per-file and aggregate hashes, `gpt-5.6-sol` high/low effort, Codex CLI version, and enforced read-only/no-agents transport before dispatch; preserve all active and superseded arms separately.
- [x] Run five fresh Sol-high and five fresh Sol-low current controls for each new or repaired scenario, including every later prompt/rubric repair before closure, at most three concurrent, retaining every completed response and recording infrastructure errors separately; Sol low remains effort evidence rather than another portability gate.
- [x] Record repaired `CW-08` at high/low 5/5, `CW-18` at high/low 5/5, `CW-17` at high/low 0/5 watched RED, the threshold-exact `CW-19` high 2/5 and low 1/5 sentence-local adjudications as superseded history, and the active whole-artifact `CW-19` controls at high 4/5 and low 2/5; keep all fixture and rubric arms isolated.
- [x] Record the immediate readability-control word count and a section-level inventory protecting meaning, readability, purpose, impact, effectiveness, completeness, correctness, and every existing contract boundary.
- [x] Apply only the approved whole-skill rewrite after the current-control prerequisites pass.
- [x] Run fresh Sol-high candidate arms for `CW-17`, `CW-18`, and `CW-19` at 5/5 and rerun the complete affected set above at 5/5; after the rubric-only `CW-19` repair, restart only `CW-19` because every other scenario contract and candidate byte remained unchanged.
- [x] Blindly compare subjective prose outputs with the immediate readability control and treat any completeness, readability, impact, or effectiveness loss as a hard failure.
- [x] Run fresh Sol-high editorial and skill-writing review; show proposed fixes, wait for approval, apply only approved fixes, and restart at zero every scenario whose prompt, rubric, supplied context, protected promise, or affected skill contract changes.
- [x] Show the complete final skill in place and wait for final owner approval.
- [x] After approval, run repository verification and commit as `docs(skills): clean up concise writing`.
- [x] Do not open a PR.

**Task 17 execution completion note (2026-08-08):** The immutable immediate readability
control is 866 words at skill SHA-256 `6c3a8382…`; the pre-rewrite routing control
is 849 words at `d3a1b7ba…`; and the current evaluated candidate is 665 words at
`f763b43e…`. All current and candidate arms used fresh `gpt-5.6-sol`, maximum
concurrency three, enforced read-only/no-agents transport, first attempts, and zero
infrastructure errors. The 29-scenario candidate arm is 145/145 GREEN: owned
`CW-01`–`CW-14` and `CW-17`–`CW-19` 85/85, shared `DISC-01`–`DISC-10` 50/50,
and `DD-01`/`DD-02` 10/10. The first integrated `DISC-01` arm scored 4/5 under a
stale rubric; the prompt stayed fixed, the pre-approved repaired rubric made
supplied-source `disciplined-research` optional, and the fresh arm passed 5/5.
The `CW-19` design ladder's sentence-local scores remain historical. The owner
repaired the rubric at `8c7ae23f…` to evaluate the complete artifact, then restarted
only `CW-19` at `/private/tmp/dd-task17-cw19-whole-artifact-current`; five fresh
Sol-high outputs and five fresh rubric scorers passed on attempt 1 with zero
infrastructure errors. Cold semantic classification makes the `f763b43e…`
truth-ablation arm 5/5, the rationalizations-deletion arm 4/5 because R5 leaves
`BLOCKED` at mismatch equality ambiguous, and the qualifier-rule arm 5/5 but
behaviorally ineffective. Their former 2/5, 1/5, and 0/5 adjudications remain
superseded history. The rationalizations section remains restored, the unnecessary
qualifier rule remains reverted, and the tracked skill remains the exact 665-word
`f763b43e…` candidate. Full hashes,
bundles, roots, per-repetition outcomes, section necessity, and superseded-arm
isolation are recorded in the owning validation record and index. The blinded
subjective comparison, editorial and skill-writing review, and final owner approval
are complete. Final repository verification passed: hook tests 373 passed/3 skipped,
installer tests 11 passed, research tests 4 passed, and the required link and diff
checks passed. This commit closes Task 17; no PR was opened.

**Task 17 repaired-definition control closure (2026-08-08):** The active
whole-artifact `CW-19` rubric now has five fresh controls per effort against
control skill `21e558b3…`: Sol high scored 4/5 and Sol low 2/5 at
`/private/tmp/dd-task17-cw19-whole-artifact-control-high` and
`/private/tmp/dd-task17-cw19-whole-artifact-control-low`. The shared root
`/private/tmp/dd-task17-repaired-definition-controls` supplied the remaining
fresh high/low controls against original definitions and bundle bytes:
`DISC-01` scored 0/5 at both efforts because every output omitted required
`disciplined-development`; `DD-01` and `DD-02` each scored 0/5 at both efforts
under independent repetition-level scoring. All runs used five fresh
`gpt-5.6-sol` processes per effort, read-only/no-agents transport, maximum
concurrency three, attempt 1, and zero infrastructure errors. This closes the
prior protocol gap: every changed Task 17 prompt or rubric has five current high
and five current low controls. Historical pre-repair scores remain isolated.
The candidate arms remain `CW-19` 5/5, `DISC-01` 5/5, and `DD-01`/`DD-02`
10/10, so the candidate-only arithmetic remains 85 + 50 + 10 = **145/145 GREEN**.

**Task 17 post-GREEN exploration note (2026-08-08):** The active baseline remains
the exact 665-word `f763b43e…` skill at 145/145 GREEN. A fresh repaired-rubric
no-rationalizations arm at
`/private/tmp/dd-task17-cw19-no-rationalizations-whole-artifact` scored 4/5;
R1's generic `either metric breaches its limit` left the required `BLOCKED`
action at mismatch equality ambiguous, so the section remains restored. An
approved one-line Method tightening at 664-word skill SHA `d7c4e549…` passed
`CW-02`, `CW-05`, and `CW-08` 5/5 but scored 1/5 on `CW-19` through criterion 4
escalation losses and criterion 7 first-accepted-write and rationale losses; it
was reverted before a full affected-suite rerun. A 637-word self-rewrite draft at
`/private/tmp/dd-task17-self-rewrite/candidate.md`, SHA `5377515e…`, never entered
the working tree. Its focused guards passed `CW-02`, `CW-05`, `CW-08`, `CW-17`,
and `CW-18` 5/5 but `CW-19` scored 4/5 because R5 used the same ambiguous generic
breach wording. The draft was rejected. These arms do not reopen the completed
145/145 candidate gate. Editorial and skill-writing review and final owner approval
are complete. Final repository verification and no-PR completion are recorded above.

**Task 17 blind-comparison completion (2026-08-08):** Nine fresh Sol-high judges
at `/private/tmp/dd-task17-blind-readability-whole-artifact` evaluated five
randomized, blinded candidate/control pairs for each of `CW-01`–`CW-08` and
`CW-19` under read-only/no-agents transport with maximum concurrency three. The
current `f763b43e…` candidate had zero material losses across all 45 pairs.
Thirty-seven pairs were equivalent; the immediate readability control had the
only eight losses: one in `CW-05`, three in `CW-08`, and four in `CW-19`.
`CW-01`, `CW-02`, `CW-03`, `CW-04`, `CW-06`, and `CW-07` were equivalent in all
five pairs. The candidate was never worse, so the blinded comparison gate is
complete. Editorial and skill-writing review and final owner approval are also
complete. Final repository verification and no-PR completion are recorded above.

### Task 18A: Ground every factual claim

**Files:**

- Modify: `skills/disciplined-research/SKILL.md`
- Modify: `skills/disciplined-development/SKILL.md`
- Modify: `skills/dispatching-development-subagents/SKILL.md`
- Modify: `skills/sweeping-stale-references/SKILL.md`
- Modify: `skills/adversarial-review-loop/SKILL.md`
- Modify: `README.md`
- Modify: `ARCHITECTURE.md`
- Modify: `skill-validation/disciplined-research.md`
- Modify: `skill-validation/disciplined-development.md`
- Modify: `skill-validation/sweeping-stale-references.md`
- Modify: `skill-validation/skill-discovery.md`
- Modify: `skill-validation/README.md`
- Modify: `skill-validation/fixtures/disciplined-research/README.md`
- Create: `skill-validation/fixtures/disciplined-research/prompts/dr-06.md`
- Create: `skill-validation/fixtures/disciplined-research/rubrics/dr-06.md`
- Create: `skill-validation/fixtures/disciplined-research/project/upload-403/evidence-index.md`
- Create: `skill-validation/fixtures/disciplined-research/project/upload-403/runtime-config.json`
- Create: `skill-validation/fixtures/disciplined-research/project/upload-403/worker.log`
- Modify: `plans/specs/2026-08-01-comprehensive-skill-cleanup-design.md`
- Modify: `plans/2026-08-01-comprehensive-skill-cleanup.md`
- Modify if reclassified: `skill-validation/dispatching-development-subagents.md`
- Modify if reclassified: `skill-validation/adversarial-review-loop.md`
- Modify if reclassified: `skill-validation/adversarial-review-loop-scenarios.md`
- Modify if reclassified: `skill-validation/writing-explicit-rationale.md`
- Modify if reclassified: `skill-validation/fixtures/disciplined-development/README.md`
- Modify if reclassified: `skill-validation/fixtures/disciplined-development/prompts/dd-01.md`
- Modify if reclassified: `skill-validation/fixtures/disciplined-development/prompts/dd-02.md`
- Modify if reclassified: `skill-validation/fixtures/disciplined-development/prompts/dd-03.md`
- Modify if reclassified: `skill-validation/fixtures/disciplined-development/rubrics/dd-01.md`
- Modify if reclassified: `skill-validation/fixtures/disciplined-development/rubrics/dd-02.md`
- Modify if reclassified: `skill-validation/fixtures/disciplined-development/rubrics/dd-03.md`
- Modify if reclassified: `skill-validation/fixtures/dispatching-development-subagents/README.md`
- Modify if reclassified: `skill-validation/fixtures/dispatching-development-subagents/prompts/dsd-01.md`
- Modify if reclassified: `skill-validation/fixtures/dispatching-development-subagents/prompts/dsd-02.md`
- Modify if reclassified: `skill-validation/fixtures/dispatching-development-subagents/rubrics/dsd-01.md`
- Modify if reclassified: `skill-validation/fixtures/dispatching-development-subagents/rubrics/dsd-02.md`
- Modify if reclassified: `skill-validation/fixtures/adversarial-review-loop/README.md`
- Modify if reclassified: `skill-validation/fixtures/adversarial-review-loop/prompts/own.md`
- Modify if reclassified: `skill-validation/fixtures/adversarial-review-loop/rubrics/own.md`

The implemented validation redesign also creates focused `DD-04`–`DD-09`,
`DSD-05`–`DSD-11`, `DISC-12`, `DR-07`, and `SSR-06`–`SSR-07` prompt/rubric
fixtures plus their required project fixtures and manifests. These additions split
single behavioral seams from retained composite scenarios; they are not new
rendering contracts.

**Approved behavior:** use the current discovery description `Use before every response, interaction, action, or task that will state, repeat, transform, or rely on a factual claim or premise—including internal logical review of supplied text, claims and premises supplied by the user or embedded in requested work, plus mechanical edits, searches, and verification.`
The explicit internal-logical-review trigger is the evidence-driven repair for the
observed `DISC-01` omission; it clarifies the universal rule rather than adding an
applicability exception.
Every factual claim, including one in a casual answer or private note, must be acquired from the best available source, verified before it is stated, and accompanied by an unambiguous source disclosure.
Do not preserve or introduce a load-bearing threshold, destination test, scratch-work exemption, project/external applicability bound, scale threshold, or other exclusion.
Project, external, and cross-domain categories may guide source selection only.
One source may support multiple claims when the mapping is unambiguous.
If no acceptable source supports a claim, do not state it as fact or attach a source that lacks the claimed datum.
When useful, an unsupported technical possibility may be shared only as an explicitly unverified investigation lead, with an explicit disclosure that no source supports or establishes it; do not attach an incomplete or unrelated source as support.
Absent, unreadable, malformed, datum-missing, conflicting, and large source sets follow the same invariant: every emitted factual claim has source support acquired and verified before output, and its disclosure identifies that support without ambiguity.

**Validation scope:** add watched targets `DISC-11`, `DR-04`, and `DR-06`.
Add `DR-05` as preservation, reclassify the ten existing discovery contracts before
implementation, and preserve the established `DR-01`–`DR-03` source-ranking and
verification behavior.
`DISC-11` covers private-note routing, `DR-04` covers private-note application, `DR-05` covers a casual answer under incomplete-source pressure, and `DR-06` covers an incident handoff that must retain an unsupported technical possibility only as an explicitly unverified lead without false evidence mapping.
`DR-01`–`DR-03` retain project-source precedence, conflicting-authority handling, multiple claims and sources, and unsupported-claim rejection.
Absent, unreadable, malformed, and datum-missing sources share the same no-support branch, so `DR-05` exercises the demonstrated datum-missing failure rather than duplicating near-identical fixtures.
Large claim sets receive no sampling exemption, and the one-source/many-claims rule changes disclosure grouping rather than verification coverage.
The frozen tasks remain in their declared domains; portability means reliable execution across agent and model families on those same tasks, not behavior on unrelated tasks.

**Pre-draft contract-freeze record (2026-08-09):** the live sweep found five later
prose repairs: `skills/disciplined-research/SKILL.md`, parent Principle 6 in
`skills/disciplined-development/SKILL.md`, the ownership boundary in
`skills/sweeping-stale-references/SKILL.md`, `README.md`, and
`ARCHITECTURE.md`. The sweeping skill's boundary assigns initial grounding only
for a “load-bearing fact,” which narrows the research companion even though the
sweeping trigger itself remains development-specific.
`dispatching-development-subagents` delegates claim verification without narrowing
it. `CLAUDE.md`, consumer snippets, hook docs/code, config, and archived plans contain
names, independent rules, or historical evidence rather than another live bound.

All `DISC-01`–`DISC-11` rows and `DD-01`–`DD-03`, `DSD-01`, `DSD-02`, `OWN`,
and `WER-07` are classified research **required** because every complete requested
output states factual claims. User-supplied origin, mechanical transformation, and
private/scratch destination do not change that classification. Exact repaired
prompts, rubrics, contexts, and base-control hashes are frozen in owning records.
The final split is 17 targets and three preservation cells. Targets are
`DISC-01`, `DISC-02`, `DISC-03`, `DISC-04`, `DISC-06`, `DISC-07`, `DISC-08`,
`DISC-09`, `DISC-11`, `DR-04`, `DD-01`, `DD-02`, `DD-03`, `DSD-01`, `DSD-02`,
`OWN`, and `WER-07`. Preservation is `DISC-05`, `DISC-10`, and `DR-05`.
Research is required in all 20. Post-freeze controls are complete: `DISC-02`
scored 0/5 high and low; `DISC-04` scored 4/5 high and 3/5 low and is a target RED
because research changed from optional to required; `DISC-05` scored 5/5 at both
efforts and is preservation. `DISC-10` and `DR-05` retain exact 5/5 high
preservation evidence. Sol-low is recorded robustness only.

The accepted affected control root is
`/private/tmp/dd-task18a-control-postfreeze-f59608a`, with freeze SHA-256
`0119bdb403fdb89978ed6c2f34bae8de5db13c392071b97b06687d81f9be0210`
and 80-slot plan SHA-256
`4de14a3e7531c8cf0e6258f82c9c8050b849ca9d0f0f8c1c633248dafcd81b4b`.
The other 12 unchanged/no-rerun scenarios retain accepted evidence from the prior
full-matrix root `/private/tmp/dd-task18a-control-backfill-bd60966-escalated`,
whose surviving freeze SHA-256 is
`4671cfef15368088eaa554fdb67e5bea115d7a4a9a9610f7e07d16b160539b2d`
and accepted plan SHA-256 is
`60b753fe17539876893f367763d59bbd53b7f584a9001217ffe07bbd607c2ce3`.
Contextful application scoring is final at
`/private/tmp/dd-task18a-control-scoring-contextful-f59608a`: freeze
`a72902e254706d2a13c9ff573bcffff6469271fdaf914f1b9e55db6a36fa0675`,
plan `cfb8e3f7949afc2b35407abd203fdd02767fdc1f698081f2fa952156f2f801bb`,
aggregate `c801090c6252298da41954663dd3f671164cd77fceaa77abf71583fa43fa2f60`.
All controls and scorers selected a1 with zero retries/errors under Codex CLI
0.147.0, read-only/no-agents transport. The context-stripped `289ef0fd…`
aggregate is transport-defective historical evidence only. Skill drafting is now
unblocked by control evidence but remains pending the explicit draft/approval gate.

- [x] Run a pre-draft routing/reference sweep across live skill, architecture, README, plan, and validation surfaces.
  Record every affected file before proposing prose.
  Treat `README.md`, `ARCHITECTURE.md`, and parent Principle 6 as required repairs; if the sweep finds another skill-prose dependency, add its complete active suite and both approval gates before proceeding.
- [x] Reclassify `DISC-01` through `DISC-10` individually against the exact new description with a fresh Sol-high validation-design reviewer.
  Record for every ID whether `disciplined-research` is required, optional, or prohibited.
  Apply pre-approved prompt, fixture, or rubric repairs before skill prose changes, freeze each changed contract, and run its five Sol-high plus five Sol-low control backfills under the global post-freeze rule.
  Treat a changed positive-routing promise as approved target behavior with a watched Sol-high control RED and later 5/5 candidate GREEN, not as preservation imposed retroactively on the old description.
- [x] Reclassify the remaining parent-suite members `DD-01`, `DD-02`, `DD-03`, `DSD-01`, `DSD-02`, `OWN`, and `WER-07` individually before drafting the parent change.
  Check every prompt, fixture, rubric, affected-skill mapping, and supplied bundle for a load-bearing-only research assumption, including `DD-01` vignette A's explicit research exclusion.
  Apply and freeze pre-approved contract repairs, update every owning/shared record, and run five Sol-high plus five Sol-low control backfills for each changed contract.
  Treat every new positive-routing promise as watched target behavior with later 5/5 candidate GREEN.
- [x] Freeze exact prompts, fixtures, rubrics, supplied contexts, control bundles, and high/low metadata for `DISC-11`, `DR-04`, and `DR-05`.
  Run five Sol-high and five Sol-low control repetitions for each new scenario under fresh read-only/no-agents transport with maximum concurrency three.
  Require watched Sol-high REDs for `DISC-11` and `DR-04`, require 5/5
  Sol-high preservation for `DR-05`, and record Sol-low as robustness only.
  Frozen accepted results are `DISC-11` 3/5 high and 4/5 low target RED,
  `DR-04` 0/5 high and 1/5 low target RED, and `DR-05` 5/5 high and low
  preservation; low is robustness-only.
- [x] Freeze the exact `DR-06` prompt, producer-shaped upload-403 fixture, eight-criterion withheld rubric, current control, and ignored candidate bytes before any run.
- [x] Preserve repaired-rubric RED acceptance and the scorer-correct failed `a0497ff` candidate at high 3/5 and low 1/5; run and accept the separate-root GREEN candidate SHA-256 `381a10aaa01b17e02d863287718c2e6cfde5c5ac587f42921146726a49725fc5` / bundle `cd87d897d6c3cf976f004c28b874dfec2c9f1064a9754a567160b64518a59477` at high 5/5 and low 1/5 with zero retries.
  The fixture contains a malformed runtime export and a deterministic 230,400-byte worker log with exactly three dispersed HTTP 403 upload-attempt records and a final collector-truncation record, without a credential-expiry datum.
  Freeze two opaque arms × two efforts × five repetitions as 20 evaluator slots, followed by four contextful high-effort scorer processes; withhold the rubric from evaluators, require the candidate SHA-256 as a frozen parameter, and launch no process during contract preparation.
  The repaired-rubric control is 0/5 high and low. Accepted terminal evidence is combined evaluator SHA-256 `c8d995ee00d4448259c5baf38afde721720b378a7d0f6fc6e35fd0cec0aba37c`, GREEN evaluator phase SHA-256 `4ecb85f53ebfcc63affd77e5d0d46d76dd2eca0ae15294b5a70fa8e2666d99d0`, combined score SHA-256 `8f86bd56c93736198120e9250c5412bc4d9d956944461acfdf4dddb0bdd4a51d`, and GREEN scorer phase SHA-256 `b2ce209a994c9bf2fea7caebaf17804d85923450588218fcbc277904b20648ae`.

**Focused parent-candidate checkpoint (2026-08-09):** The approved ignored parent
candidate SHA-256 `3e80cd1add0abd5022cb3d2df5e209f03f9a107f4f0d0c2ef1c7d28cf9b172da`
was tested with approved research candidate `381a10aaa01b17e02d863287718c2e6cfde5c5ac587f42921146726a49725fc5`
and the unchanged tracked sweeping skill. The accepted v5 evaluator root is
`/private/tmp/dd-task18a-parent-green-3e80cd1-v5`: freeze `03387d5ca3e30179aa32df42bd72779458d308de590a32e564c40f3cd1dbd7b0`,
plan `c7ab398ab4f99fdb2b16fa226686683b828d11b71eb35177dcf329f6d33bc36f`,
and verification `059dd5d6c4e8f90f624841917601ee6b6d6a8e9906fa1706602137fa3dedbf0d`.
All 35 evaluators completed at `a1` with zero accepted retries. The v5 scorer root
is `/private/tmp/dd-task18a-parent-green-scoring-3e80cd1-v5`: score freeze
`75c1bcd1e6cead0ba09589551a9d0dc9de1f707f1d8dbd91bccf85e3923b0961`,
plan `83232d6d7f0559a94524b76cc7fa085d2ebe3b972d57408784562f5fe1fa35ab`,
and aggregate `a39194d7a496246081e3b97aed70761468c749a57d8aadb67c0ebbcc370d94e8`.
All seven scorers completed at `a1` with zero accepted retries.

The orchestrator classified `DD-01` 0/5, `DD-02` 0/5, `DD-03` 3/5,
`DSD-01` 0/5, `DSD-02` 1/5, `OWN` 5/5, and `WER-07` 5/5: 14 PASS and
21 FAIL. This focused slice is **not GREEN**. Seventeen failures are genuine
source-disclosure/application misses; the other four are genuine `DD-02`
schema/orchestration misses. No prompt, fixture, or rubric repair is indicated.
The earlier v4 launch remains excluded infrastructure history: the first three
scenario configurations each recorded three non-evaluable attempts after the
outer sandbox denied the in-process app-server client, then the run stopped with
zero completion markers. The accepted v5 run is a full fresh restart, not a retry
continuation from v4.

This checkpoint does not satisfy the candidate-application or 28-scenario union
steps below. No parent candidate is applied. The complete sweeping proposal still
requires approval, and after approval the integrated 140-response union must be
refrozen and restarted with all three exact approved candidate skills.

**Approved focused GREEN restart result (2026-08-09):** The revised ignored
parent candidate SHA-256
`a6aa8b6bf572b859b489eba260ca4592c368ad8ea0d8d536fa0610f2d164a1bb`
was tested with the approved research candidate
`381a10aaa01b17e02d863287718c2e6cfde5c5ac587f42921146726a49725fc5`
and unchanged tracked sweeping skill
`d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157`.
The evaluator root `/private/tmp/dd-task18a-parent-green-a6aa8b6-v1` has freeze
SHA-256
`6311597844bfaae83c60ba2840e944bf81264693a692447d9718db30a29fb38e`
and plan / verification SHA-256 values
`4dad925d034b63fdf42421dc32c16a4c32019f24c9b80bf381c037a39c08003a` /
`ece73478efe26387da62c62dd340b108ec4a95b189281b61f8c5df20fcd4dbe4`.
All 35 evaluators selected `a1` with zero retries. The scorer root
`/private/tmp/dd-task18a-parent-green-scoring-a6aa8b6-v1` has score-freeze /
plan / aggregate SHA-256 values
`136e5db31a960d574b96513824ccc1a274422751a761c0720b222dc0220cd447` /
`e6b40b3c700a2af1a991b96b0609efcdf09953c0dc0698ba2965ac5d2936434f` /
`377598853c63c15970639f5c2cdf4c17529fcb5103ce82e9283ce000895541f1`.
All seven scorers selected `a1` with zero retries. The descriptive scorer emitted
15 PASS / 20 FAIL. Whole-artifact adjudication corrected its five phrase-local
`DD-03` false failures because every complete table generated all three required
cases and applied distinct implementation thresholds. Final results are `DD-01`
0/5, `DD-02` 2/5, `DD-03` 5/5, `DSD-01` 2/5, `DSD-02` 3/5, `OWN` 5/5,
and `WER-07` 3/5: 20 PASS / 15 FAIL, so the candidate is **not GREEN**.
All remaining misses are genuine and no contract repair is indicated. The failed
`3e80cd1…` v5 result above remains immutable history. Candidate application,
complete sweeping approval, and the freshly refrozen 28-scenario union remain
open gates.

**Next approved focused GREEN restart result (2026-08-10):** Parent candidate
SHA-256
`320cdba2b30779e7066be203a0add40defd1dc94f8068b227e861991e684b2f2`
was tested with the same approved research candidate and unchanged tracked
sweeping skill. The evaluator root is
`/private/tmp/dd-task18a-parent-green-320cdba-v1`; freeze and execution-plan
SHA-256 values are
`dc0c390bf87c52dd88c4a725d3ac595f399a83e034492e60e3c57059432c5568` /
`f59cf66995610d2fd4f38f068cfe5c05c9b4c9bfdda029e717e2db422e7c7da5`;
evaluator verification is
`2f13b6eadf1ec0842c78b2d3ae85e251e416e6e1fb37507163275b05cae87838`.
All 35 evaluators selected `a1` with zero retries/errors. Scorer root
`/private/tmp/dd-task18a-parent-green-scoring-320cdba-v1` has score-freeze /
plan / aggregate SHA-256 values
`115328d4bbb0f8fcc1c42be7f9784f6dfc7972d6380543d8b92062561dd0e0a3` /
`c40cab48d5dba11b05295c6bcc50cf7095f712020800d7e3fd21e206b2d2191f` /
`1e24058a3ff5d9de5e3d934d6b5649deb8d64a7ad0f2cb92e536fbd15853acaa`.
All seven scorers selected `a1` with zero retries/errors. Descriptive scoring and
orchestrator whole-artifact adjudication agree exactly: `DD-01` 0/5, `DD-02`
0/5, `DD-03` 4/5, `DSD-01` 0/5, `DSD-02` 3/5, `OWN` 3/5, and `WER-07`
5/5, totaling 15 PASS / 20 FAIL. The candidate is **not GREEN**; all misses are
genuine and no contract repair is indicated. The completed `a6aa8b6…` result and
all earlier evidence above remain immutable history; application and full-union
gates remain open.

**Approved parent contract architecture applied (2026-08-10):** the pre-comparison
tracked parent was SHA-256
`366b3dad7e49d48d2744e63f10286f05385ded1120e164bb2dd1e8dcf925b9a7`.
After the original/current comparison and owner approval, its reviewed successor was
applied byte-for-byte at tracked SHA-256
`34e105ccfd08f4b08e4879e6280ee9c2c9092d7f714d8fd7d47048f4059b1723`.
The owner approved the complete in-place skill. A fresh candidate arm observed
`DD-01` 0/5, `DD-02` 0/5, and `DD-03` 5/5, so it is not GREEN and is not
approved for staging or commit. Because the repaired `DD-01`/`DD-02` rubrics
required a five-high/five-low control backfill before candidate work, this candidate
arm remains failure evidence rather than an accepted validation arm: the controls are
now accepted, but they occurred later, so the arm cannot be reused.
The reviewed v3 `DD-01`/`DD-02`/`DD-03` prompt hashes are `b41c2835…`,
`95deb138…`, and `e3295864…`; active withheld rubric hashes are `3599c856…`,
`e644990b…`, and `8daf6068…`. The prior DD-01 rubric `e2076d7c…` and the
pre-behavior-first-repair DD-02 rubric `69f985c4…` remain exact
historical provenance for every frozen evaluation through fail-fast cycle 6.
These three scenarios are the complete parent
acceptance denominator: 15 Sol-high slots. `DSD-01`, `DSD-02`, `OWN`, and
`WER-07` remain 20 separately attributed child-composition slots and are never
pooled with the parent score. `DISC-01`–`DISC-11` own discovery.

The completed original-versus-current comparison below used the pre-repair
`DD-01` and `DD-02` rubrics at `40b28364…` and `576015f8…`. Those hashes and
results remain historical provenance and do not validate the repaired active
rubric bytes.

Parent scoring covers mode, gate/principle timing and order, parent-owned
artifacts/outcomes/destinations, fail-closed transitions, and parent/orchestrator
owners. Child invocation, loading, procedure execution, output quality, and research
correctness/disclosure are not parent PASS/FAIL criteria. Active evaluator bundles
are parent-only for `DD-01`, parent plus seven named project sources for `DD-02`, and
parent plus two named project sources for `DD-03`; `operator-note.md` is excluded.
All prior seven-scenario/35-slot arms remain immutable history under their former
contracts. None was inferred from or carried forward from that history.

**Original-versus-current parent comparison (2026-08-10):** the pinned
`4296647f…` original parent (`1151a757…`) and then-tracked comparison parent (`366b3dad…`)
each completed 15 fresh Sol-high slots, all on `a1` with zero retries/errors. The
evaluator verification is `08696989…`; the contextful descriptive-score aggregate
is `2e278de0…`. Descriptive and whole-artifact results are original `DD-01` 0/5,
`DD-02` 0/5, `DD-03` 5/5, and current `DD-01` 0/5, `DD-02` 0/5, `DD-03` 5/5.
`DD-03` is a genuine original-contract preservation success. Original-arm
`DD-01`/`DD-02` misses mix genuine original-contract effectiveness failures with
broadened post-original observables; they cannot all be assigned to either class.
Current-arm misses are genuine against the explicit current request and cluster
around Principle 2/Principle 6 salience, but the equal arm scores and original-arm
omissions do not demonstrate that original wording performed better. Two
non-dispositive active-rubric defects
were identified for repair: Gate 2 is not due at `DD-01` row A's pre-choice exact
checkpoint, and declining a review-severity `[P3]` finding does not automatically
require parent-owned rationale. The ignored post-v8 proposal remains unapplied and
is superseded for owner review by the complete ignored post-comparison proposal
`.superpowers/sdd/2026-08-01-comprehensive-skill-cleanup/task-18A-parent-post-comparison-proposed-SKILL.md`,
SHA-256 `34e105ccfd08f4b08e4879e6280ee9c2c9092d7f714d8fd7d47048f4059b1723`.
It retains the Gate 5 and signed-scope repairs, replaces the passive mode preamble
with a positive exact-checkpoint selection recipe, and passed final cold
contract/skill-writing review with P0/P1/P2/P3 = 0/0/0/0. The owner approved the
complete proposal, and it matched the then-tracked skill byte-for-byte at `34e105cc…`.
Complete in-place owner approval was recorded. The fresh active-rubric candidate arm completed
all 15 evaluators and three contextful scorers at `a1` with zero retries/errors.
Evaluator freeze / plan / verification are `31160131…` / `37e91598…` /
`6942dc09…`; score freeze / plan / aggregate are `c7891da4…` / `aa1f7a16…` /
`3028303a…`. Whole-artifact adjudication agrees with the descriptive totals:
`DD-01` 0/5, `DD-02` 0/5, and `DD-03` 5/5, or 5/15. `DD-01` repeatedly omits
explicitly requested due Principles 1/2/6; `DD-02` repeatedly loses parent gate,
order, or review-pass-boundary observables; `DD-03` genuinely preserves Principle 7.
The scorer omits wrong-timing Principle 8 defects in `DD-01/r1` and `DD-01/r2`;
one `DD-02/r5` rationale incorrectly disputes Principle 8 at a defensible
returned-work chunk boundary. None changes a verdict because those artifacts have
independent genuine failures. No prompt, fixture, or active-rubric repair is indicated.
The repaired-rubric five-high/five-low control backfill is complete and accepted;
no candidate result from the prematurely ordered arm carries forward. The tracked
skill remains not GREEN, unstaged, and unapproved for commit; any prose repair
returns to complete proposal and owner-approval gates.
The accepted control is original commit `4296647f…` / parent `1151a757…`:
`DD-01` original-parent only at manifest `4ad78825…`, and `DD-02` original parent
plus seven active project sources at manifest `922ebd5e…`. It completed two scenarios
× high/low × five repetitions = 20 evaluators, followed by four contextful Sol-high
scorers / 20 verdicts. All 20 evaluators and four scorers selected `a1` with zero
retries/errors. Evaluator freeze / plan / verification are `4e8be5b3…` /
`625ff413…` / `79c266ed…`; score freeze / plan / aggregate are `b8e7c0d3…` /
`0d25e502…` / `83a34d7a…`. Whole-artifact adjudication confirms `DD-01` and
`DD-02` at 0/5 high and 0/5 low. Both required high cells are accepted watched
REDs; low remains robustness only. `DD-03` keeps its unchanged original 5/5
preservation control.
A repeated post-scoring verification exposed a wrapper-only static-inventory defect.
The test-first repair admits and authenticates the immutable aggregate only during
result verification; the repaired real-root verifier passed twice, 14/14 repaired
harness tests and 12/12 inherited active tests pass, and the evaluator verification
and aggregate hashes above did not change. Launch-time scorer wrapper `5e90a2fb…`
is preserved as provenance; repaired verifier `aafb6220…` and tests `57507b4b…`
own final lifecycle verification.
The owner-approved focused ledger-versus-ASCII-flow experiment is also complete.
It compared two complete ignored proposals on `DD-01` and `DD-02` only, five fresh
Sol-high repetitions per opaque arm and scenario. All 20 evaluators and four
contextful scorers selected `a1` with zero retries/errors. Evaluator freeze / plan /
verification are `159943f3…` / `d13c8bb3…` / `a3c004c1…`; score freeze / plan /
aggregate are `96a3e20a…` / `5e2fd020…` / `8a4e0922…`. After aggregate
authentication and manual adjudication of every complete artifact, sealed arm A
revealed as the ASCII flow proposal `eb4b13ba…` and arm B as the lean ledger
proposal `5bec5d07…`. Both scored `DD-01` 0/5 and `DD-02` 0/5. The diagram added no
measured benefit and is abandoned; neither proposal is approved for application.
The lean proposal remains the smaller basis for a narrow revision that must separate
due-now, future/conditional, satisfied/retained, and reopened-conflict obligations
while preserving global Gate 1 / Principles 1, 2, and 6 salience. No prompt repair
is indicated; some non-dispositive rubric/scorer observations about additive
conflict-triggered selections are recorded. The tracked skill remains unchanged by
this experiment, not GREEN, unstaged, and unapproved for commit.
The pre-repair comparison did **not establish GREEN**. The comparison adjudication is recorded
in `.superpowers/sdd/2026-08-01-comprehensive-skill-cleanup/task-18A-parent-original-comparison-adjudication.md`.
The active-run adjudication is recorded in
`.superpowers/sdd/2026-08-01-comprehensive-skill-cleanup/task-18A-parent-active-adjudication.md`.
The repaired-rubric control adjudication is recorded in
`.superpowers/sdd/2026-08-01-comprehensive-skill-cleanup/task-18A-parent-repaired-control-adjudication.md`.
The focused proposal comparison adjudication is recorded in
`.superpowers/sdd/2026-08-01-comprehensive-skill-cleanup/task-18A-parent-ledger-flow-comparison-adjudication.md`.
The owner-approved lean-v2 focused candidate is also complete. Proposal
`06280f03…` ran ten fresh Sol-high evaluator slots and two contextful scorers, all
at `a1` with zero retries/errors. Evaluator freeze / plan / verification are
`2ebbbf37…` / `5311b471…` / `4bac0f73…`; score freeze / plan / aggregate are
`98b7ddff…` / `f91632a9…` / `267131a0…`. Descriptive scoring and orchestrator
whole-artifact adjudication agree on `DD-01` F/F/F/F/F = 0/5 and `DD-02`
F/P/F/F/F = 1/5. The proposal is rejected, unapplied, and not GREEN; `DD-03` was
not run because the focused pair did not reach 10/10. `DD-01` still loses global
Principles 1/2/6 and the unresolved-owner boundary. In `DD-02`, the new rule that
an active ordered item remains selected caused early Gate 2 selection in four runs;
remove that regression in the next complete proposal. No prompt/rubric repair is
indicated. Before launch, repeat-verification and frozen-byte authentication harness
defects were repaired test-first; final wrapper/tests `93811137…` / `b15d9040…`
passed 46/46 no-model checks and independent tamper review without changing frozen
inputs. Full classification is in
`.superpowers/sdd/2026-08-01-comprehensive-skill-cleanup/task-18A-parent-lean-v2-focused-adjudication.md`.

The owner then authorized an initial three-cycle fail-fast effectiveness experiment. Each
complete ignored proposal ran `DD-01` first with five fresh Sol-high evaluators and
no scorer; a result below exact 5/5 stopped before `DD-02`. Cycle 1 `f26251a9…`
scored 0/5, cycle 2 `a03075fe…` scored 1/5, and cycle 3 `75e764bf…` scored 3/5.
The final proposal preserves Gate 5 P1/P2/P6, per-item Gate 2, unresolved-owner
blocking, A/H P1, artifacts, transitions, and owners in all five runs. R1 and R4
still omit P6 in brainstorming row A despite making factual claims, so the proposal
is rejected, unapplied, and not GREEN. `DD-02` and `DD-03` were not run; the
initial three-cycle tranche was exhausted. The fail-fast order reduced each failed semantic cycle
to five evaluator calls. A cycle-1 shared-directory race was repaired test-first and
resumed without duplicating its two completed evaluator calls. Full provenance and
classification are in
`.superpowers/sdd/2026-08-01-comprehensive-skill-cleanup/task-18A-parent-effectiveness-three-cycle-adjudication.md`.

The owner subsequently authorized three final fail-fast cycles. Cycle 4 proposal
`bcab889d…` passed `DD-01` 5/5, then failed `DD-02` 0/5; `DD-03` stayed locked.
Cycle 5 `081e1b3a…` failed `DD-01` 3/5. Final cycle 6 `0d710564…` failed
`DD-01` F/F/F/P/F = 1/5 with verifier `814a95a1…`; `DD-02` and `DD-03` stayed
locked. Its two targeted repairs nevertheless worked 5/5: row-F P1 was not due
for the pure standalone review and row-C Gate-5 P6 remained selected despite
retained support. The remaining misses were premature conditional P5 in row D,
premature P3 for unresolved design choices in A/D, and row-H P7 marked not due.
The final proposal in this six-cycle tranche is rejected, unapplied, and not
GREEN. Its frozen results remain bound to the historical rubric.

Post-adjudication inspection found a genuine active DD-01 rubric omission: row H
did not require the parent P7 cue stated by the proposal routing/mode rules. Under
the standing repair authorization, only the active rubric was repaired test-first
to SHA-256 `3599c856d7e0cf12006b1f548a854f9038badf71c56986046e9eda1baf62e21d`;
the prompt remains `b41c2835…`. The repair also makes row-D P7, conditional P5
pre-edit timing, and unresolved-design-versus-P3 conflict timing explicit. It does
not retroactively reclassify any frozen artifact. Final classification remains
orchestrator-owned; the proposal remains not GREEN and unapplied. Full cycle-6
classification is in
`.superpowers/sdd/2026-08-01-comprehensive-skill-cleanup/task-18A-parent-effectiveness-cycle-6-dd01-adjudication.md`.

After that repair, the owner authorized a final three-cycle matched-control
experiment under the active prompt/rubric. Cycle 7 proposal `3ed5c984…` scored
`DD-01` 0/5 with verifier `c1c2081b…`; cycle 8 `d305c73d…` scored 1/5 with
verifier `f7fc1424…`; and cycle 9 `fec4668f…` scored P/F/F/F/F = 1/5 with
verifier `ad5a7fad…`, a repaired-rubric progression of 0/5 → 1/5 → 1/5. Cycle 9
fixed its target: H P7 was present 5/5, while P3
remained stable and P6 was correct 5/5. Two genuine P1 classes remain: Gate 5 and
its active P1/P2/P6/P8 are sometimes downgraded to satisfied/retained, and P5 is
sometimes selected too late for the pre-edit established-behavior check. They are
not caused by the cycle-9 P7 delta; no prompt/rubric defect was found.

No repaired-rubric candidate reached 5/5, so `DD-02`, `DD-03`, and scorers
remained locked. Cycle 9 is the strongest proposal, but it
is rejected, unapplied, and not GREEN; classification remains orchestrator-owned.
The final cap is exhausted, no cycle 10 is authorized, and no further model run or
proposal edit is permitted. Full cycle-9 adjudication is in
`.superpowers/sdd/2026-08-01-comprehensive-skill-cleanup/task-18A-parent-effectiveness-cycle-9-dd01-adjudication.md`.

The owner subsequently authorized a separate DD-01 rubric repair and matched
comparison, not a cycle 10 prose edit. The new rubric grades correct, unambiguous
parent behavior and records terminology mismatches separately as advisory evidence;
unclear behavior fails. Keep the prompt, tracked parent, and cycle-7 proposal exact.
Run five Sol-high plus five Sol-low tracked-parent controls before five fresh
Sol-high cycle-7 artifacts, manually adjudicate all 15, and preserve historical
strict-rubric classifications unchanged. DD-02, DD-03, skill application, staging,
commit, and PR creation remain outside this authorization. The approved design and
execution plan are
`.superpowers/sdd/2026-08-01-comprehensive-skill-cleanup/task-18A-dd01-behavior-first-rubric-design.md`
and
`.superpowers/sdd/2026-08-01-comprehensive-skill-cleanup/task-18A-dd01-behavior-first-rubric-plan.md`.
The behavior-first DD-01 rubric is frozen at SHA-256
`bb994c3b2e4adfc4feead9220ab9df89d53f5a74d1efa0e6bffbf733c7c0c9bb`; its independent
contract review passed P0/P1/P2/P3 = 0/0/0/0. The tracked-parent baseline v2 root
is `/private/tmp/task-18A-dd01-behavior-first-baseline-v2`, with freeze / plan
SHA-256 values `a888fad7ec1117e8d01128d7731edc1a85806febcfddbb39299cf7889000f340`
/ `89672ca6036dd0737e7e165cff0373e58398bc62452e49dcecac0ec3a09829dd`.
Its cold launch review passed
P0/P1/P2/P3 = 0/0/0/0 after test-first repairs froze the exact wrapper and
hardened engine and separated pre-launch live checks from durable result
authentication. Cycle-7 preparation remained blocked until the baseline verifier
and manual adjudication were immutable.
The ten-slot baseline then completed at `a1` with zero retries/errors and verifier
SHA-256 `def4fb3731139df4a02fcc0ebb4c286ef59ca3c664fc1450074c1f1c2c77a9a5`.
Orchestrator behavior-first adjudication is Sol-high 0/5 and
Sol-low 0/5; terminology differences were recorded separately and did not cause
failure. Every run has an independent A/B behavioral miss, chiefly an unresolved
architecture-selection owner, missing evidence-threshold application, or an
implementation-planning transition left open before written scope/signoff. The
immutable adjudication SHA-256 is
`fd67624ad3575e391f248393997295307cc9042f5adadf3f0f65513d118058d0`;
exact cycle-7 preparation is now
complete under the same prompt and rubric at root
`/private/tmp/task-18A-dd01-behavior-first-cycle-7-v1`, with freeze / plan
SHA-256 values `d10e460f35fccd032fd44b14ea1b65cf5749004d23b5bfa2a7c6203aee2ee6fc`
/ `8e7c12bda7667ca3ee758ce59b5d2e152682938b0b5cd51db7bce831ed310f64`.
Its exact proposal SHA-256 is
`3ed5c984c583aa0498366c091c42f57af0dda3722cc87a02c6c34d831d87c296`.
All five cycle-7 Sol-high slots completed at `a1` with zero retries/errors, and
repeated durable authentication passed with verifier SHA-256
`7403b8eb16c84852b18b5ee3ed85c75523e6694c612ae75948658542d882e26d`.
Orchestrator behavior-first adjudication is F/F/P/F/F = 1/5. Repetitions 1, 2,
4, and 5 fail because section E does not clearly block implementation planning
through contract reread and written scope; repetition 3 passes despite terminology
differences. The immutable cycle-7 adjudication SHA-256 is
`fa62a9d119ea5d502fdfa3bfeea42a584b90320a26fe5b99ec0a88dc1fb3f044`.
This comparison covers DD-01 only. It does not validate DD-02, DD-03, or the
complete skill suite and does not establish skill GREEN. The exact cycle-7
proposal is rejected and unapplied; the tracked parent remains unchanged. No
skill application, staging, commit, or PR is authorized. Historical
strict-terminology classifications remain unchanged and separately preserved.

The owner then authorized a new behavior-first effectiveness loop of at most three
cycles, starting from exact cycle 7 and stopping early at 5/5. This authorization
does not reopen the exhausted historical strict-rubric loop or create a historical
cycle 10. Each new cycle changes one genuine behavioral failure class, uses five
fresh Sol-high DD-01 contexts under unchanged prompt `b41c2835…` and rubric
`bb994c3b…`, and leaves terminology-only differences for later owner review. The
design and execution plan are
`.superpowers/sdd/2026-08-01-comprehensive-skill-cleanup/task-18A-dd01-behavior-first-effectiveness-cycles-1-3-design.md`
and
`.superpowers/sdd/2026-08-01-comprehensive-skill-cleanup/task-18A-dd01-behavior-first-effectiveness-cycles-1-3-plan.md`.
Tracked skill prose, DD-02, DD-03, application, staging, commit, and PR remain
outside this loop.

The three-cycle behavior-first effectiveness loop is complete. Starting from the
cycle-7 1/5 RED, cycle 1 repaired the debugging planning/editing boundary and
scored P/P/P/P/F = 4/5; cycle 2 required evidence-grounded architecture options
and scored P/P/F/P/P = 4/5; cycle 3 required the decision owner to select before
Gate 2 scope and scored P/P/P/P/P = 5/5. Cycle-3 proposal SHA-256 is
`652abda14206472f28e5e0a8bb7c8cc2b197df32bad2d5ebaba9d00e014e608b`;
verifier / adjudication are
`64f9acdd44f06f48b597ce6f10a52750eab5c1557fbb1d44c79603ef9cc3bed2`
/ `11bcd0cfbbf63eda227ec098268b999dc33fcb5bc6e77170e7e5c3d649cd98ce`.
Terminology remained advisory. The loop stopped at the authorized cap with its
focused DD-01 target satisfied. The owner approved the complete cycle-3 proposal,
and it is now applied byte-for-byte as the tracked parent at SHA-256
`652abda14206472f28e5e0a8bb7c8cc2b197df32bad2d5ebaba9d00e014e608b`.
Its authenticated DD-01 5/5 evidence carries forward because the applied bytes are
identical. Checkpoint commit
`c9f0eba148ff73477c41e4403ea5dcd8baf4f7db` records this approved applied-parent
baseline without establishing parent GREEN or authorizing a PR.

Formal behavior-only DD-02 rubric epoch `288dd142…` grades actions, timing, ownership,
blocked transitions, and truthful bookkeeping rather than rendering. The minimal
Gate 4 candidate `987bdf42…` scored 5/5 and is owner-approved and applied
byte-for-byte, so the focused Task 18A parent-behavior goal is satisfied. DD-03,
child composition, and union validation had not yet rerun at that checkpoint; the
parent was not GREEN, and the broader five-skill Task 18A gates remained open. The
[owning validation record](../skill-validation/disciplined-development.md#formal-dd-02-behavioral-rubric--minimal-gate-4-proposal-55)
contains the full results and provenance.

- [x] With `superpowers:writing-skills`, draft complete proposed versions of `disciplined-research`, `disciplined-development`, `dispatching-development-subagents`, `adversarial-review-loop`, and `sweeping-stale-references` plus the complete documentation-only repairs.
  For every section and each whole skill, record whether it is necessary and whether a simpler formulation preserves intent and effectiveness.
  Show every complete proposed skill, including the complete sweeping skill, and wait for approval before applying any skill prose.
- [x] Apply only the approved complete drafts.
  The complete applied candidate, including the owner-authorized unattended
  behavior-cycle repairs, is frozen at SHA-256
  `f4001332065b9829b0e9893e7289842c17e1c6cde6f627aa6bba211ca873f8c9`
  for `disciplined-research`,
  `872529574af4f4fabcd58ff3721ce6c241af99936c19403b40abca7e9c252e8b`
  for `disciplined-development`,
  `bf616daa594a90282ccfa22af210214b30393158838b5feb9220859268f9fe54`
  for `dispatching-development-subagents`,
  `d92afd5dc74681d3037b1d5ab2543276698d9cd7b7c0fafc858cfe6b709b5609`
  for `sweeping-stale-references`, and
  `56e08642a8005ac526898ed7b9cd178bcfd08a655464f2249b9ccae22aeb5387`
  for `adversarial-review-loop`. Their current word counts are respectively
  1,459, 3,308, 1,551, 1,527, and 1,477. Checkpoint commit `c9f0eba…` remains the
  historical applied-parent baseline; later Gate 4, Gate 5, dispatch, research,
  and sweeping repairs are validated at their exact final hashes by the expanded
  scenario design below rather than carried forward from that checkpoint.
  In `disciplined-research`, retain acquire/verify, source ranking, recency/applicability, conflict handling, and pressure resistance where they serve the universal rule; remove the load-bearing, destination, and scratch exceptions rather than renaming them.
  In `disciplined-development`, align Principle 6 and its routing language without copying the child procedure.
  In `sweeping-stale-references`, remove the load-bearing narrowing from the research ownership boundary without changing the sweeping trigger or procedure.
  Make `README.md` and `ARCHITECTURE.md` describe the executable behavior accurately.
- [x] Run the expanded changed-skill union five times on cold Sol high: `DISC-01`–`DISC-12`, `DR-01`–`DR-07`, `DD-01`–`DD-09`, `DSD-01`, `DSD-02`, `DSD-05`–`DSD-11`, `OWN`, `WER-07`, `SSR-01`–`SSR-03`, and `SSR-05`–`SSR-07`.
  This is 225 responses across 45 unique scenarios. The 13 new focused seam tests
  are `DD-05`–`DD-09`, `DSD-06`–`DSD-11`, and `SSR-06`–`SSR-07`; retained
  composites still exercise the whole parent, dispatch, and sweeping flows.
  Combined execution does not combine acceptance: every scenario retains its own
  five-slot denominator and owner, including parent versus child composition.
  Score complete artifacts in supplied context; any scenario below 5/5 pauses the slice for failure classification.
  Earlier full-union epochs are superseded after evidence-driven repairs. Union v62
  exposed genuine direct-running-system/failed-verification bookkeeping and intended
  new-prose-search misses. Focused repair roots v63/v64 passed `SSR-01` 5/5 and
  final `DSD-02` 5/5. Completed union v65 exposed genuine parent first-read,
  evidence-limit, and plan-reread salience misses; focused v66/v67 repairs reached
  5/5 on each affected behavior. A final cold review then exposed that “governing
  and task sources” excluded a separately categorized supplied external source.
  The exact parent was repaired to require every supplied applicable source globally
  and at Gate 5; focused v69 passed `DD-01` and `DD-09` 10/10 behaviorally, and
  exact-hash cold review v70 returned `VERDICT: PASS`. Zeroed union v71 then
  exposed one genuine `DD-01` response that released implementation planning after
  rereading instead of after complete signed scope. The narrow parent clarification
  passed focused `DD-01` v72 5/5 and exact-hash cold review v72 at SHA-256
  `872529574af4f4fabcd58ff3721ce6c241af99936c19403b40abca7e9c252e8b`.
  Zeroed union v73 then completed 225/225 evaluator responses and all 33 scenario
  scorers on attempt 1 with zero retries or infrastructure errors. Descriptive
  scoring passed 218/225; complete-artifact adjudication passed 225/225 after seven
  false negatives demanded redundant pressure/breaker/count wording or literal
  same-reviewer/PR-action phrasing despite the required behavior being explicit.
  The durable provenance manifest records every accepted hash and adjudication.
- [x] Run cold editorial and skill-writing review of all five changed skills.
  Show any proposed prose fix and wait for approval; after an approved fix, restart every affected scenario and both in-place approval gates.
  The final exact hashes received fresh read-only Sol-high reviews with no P0–P3
  findings and `VERDICT: PASS`, including the final DD-02 ordering repair review at
  `/private/tmp/task18a-dd02-v61-cold-review.md` and the final dispatch/sweeping
  review at `/private/tmp/task18a-v64-two-skill-cold-review.md`. The final parent
  review at `/private/tmp/task18a-v72-parent-cold-review.md` also returned
  `VERDICT: PASS` at exact SHA-256 `87252957…`; the earlier v70 review passed the
  supplied-source repair before union v71 exposed the final planning-block seam.
- [x] Stage only the approved behavior slice, then run a deep staged `adversarial-review` against the complete plan and governing documents.
  Any finding-driven skill edit returns to proposed-draft approval, affected validation, cold review, and final in-place approval before restaging.
  The first staged review found only two P2 bookkeeping defects: stale current-state
  language and superseded scenario denominators. After those documentation-only
  repairs, a fresh authorized OpenAI read-only review of the exact 91-file stage
  returned `VERDICT: PASS` with no P0–P3 findings at
  `/private/tmp/task18a-final-staged-review-openai-v2.md`, SHA-256 `9ef9e238…`.
- [x] Show all five reviewed final skills in place, including the complete sweeping skill, and wait for approval.
  The owner's carried-forward unattended authorization approves the evidence-driven
  in-scope repair sequence and removes an extra pause after exact-hash review.
- [x] Run the hook, installer, and research pytest suites; rerun the routing/reference sweep and exact local-link command; and run `git diff --check` plus `git diff --cached --check`.
  After approval, commit the behavior slice separately as `docs(skills): ground every factual claim`.
  Do not open a PR.
  Final verification passed: hook tests 373 passed / 3 skipped, installer tests 11
  passed, research tests 4 passed, all five skill-package validators passed, local
  Markdown links passed for 88 working and 88 staged documents, the provenance
  manifest reproduced byte-for-byte at SHA-256 `77104644…`, and the routing,
  current-denominator, JSON-integrity, skill-hash, and diff checks passed.
- [x] Materialize the behavior commit as Task 18's immutable immediate readability control.
  Record all five changed skills' current word counts and hashes, then resume the behavior-preserving cleanup below from new research- and sweeping-skill section inventories and complete drafts.

**Task 18 immediate readability control (2026-08-14):** Commit
`a69e253221dd8bb054f68941ea0f7466d08448eb` is the immutable Task 18 control.
Its nine-skill archive SHA-256 is `b00a2e669b04d564102ae911044698fc4ed5573a56af49597d25cf89fc1e1961`,
and its canonical content-manifest SHA-256 is
`d51553182a68339e90d17cb07d6526542ff2f4aa52d293f82312e6f23573633c`.
The five changed skill word-count / SHA-256 pairs are `disciplined-research`
1,459 / `f4001332065b9829b0e9893e7289842c17e1c6cde6f627aa6bba211ca873f8c9`,
`disciplined-development` 3,308 / `872529574af4f4fabcd58ff3721ce6c241af99936c19403b40abca7e9c252e8b`,
`dispatching-development-subagents` 1,551 /
`bf616daa594a90282ccfa22af210214b30393158838b5feb9220859268f9fe54`,
`sweeping-stale-references` 1,527 /
`d92afd5dc74681d3037b1d5ab2543276698d9cd7b7c0fafc858cfe6b709b5609`,
and `adversarial-review-loop` 1,477 /
`56e08642a8005ac526898ed7b9cd178bcfd08a655464f2249b9ccae22aeb5387`.

### Task 18: Clean `disciplined-research`

**Files:** `skills/disciplined-research/SKILL.md`, `skill-validation/disciplined-research.md`, `skill-validation/skill-discovery.md`, `skill-validation/README.md`

**Review focus:** keep universal factual-claim applicability explicit; make acquire/verify facets flow as one method; remove overlap among overview, rationalizations, and red flags; keep optional suite composition out of the broad-domain core.

**Validation scope:** broad-domain companion; use its complete cold Sol-high suite,
including isolated non-software research, with only scenario-declared dependencies.

- [x] Record the post-Task 18A immediate readability-control word count and hashes, then rebuild the section-level and whole-skill necessity/simplification inventory from those exact bytes.
- [x] Draft the smallest coherent reorganization, show the diff, and wait for user approval.
- [x] Apply the approved draft and run `DISC-01`–`DISC-12` plus `DR-01`–`DR-07` five times each on Sol high: 95 responses across 19 scenarios.
- [x] Blindly compare subjective prose outputs with the immediate readability control where the rubric requires judgment.
- [x] Run cold editorial and skill-writing review plus deep staged `adversarial-review`; show proposed fixes, wait for user approval, apply them, and restart affected scenarios.
- [x] Show the final skill in place and wait for user approval.
- [x] After approval, run repository tests, the exact local-link command, `git diff --check`, and `git diff --cached --check`; commit as `docs(skills): clean up disciplined research`.

**Task 18 execution note (2026-08-08, in progress):** Preflight confirmed clean
HEAD `ecfd2ef4d88694ee36ffe30ebe852173c5629d50` and passed the hook suite
(373 passed / 3 skipped), installer suite (11 passed), and research suite
(4 passed). The immutable immediate readability control is the byte-identical
1,388-word skill at SHA-256 `a5c4079e…`; its nine-skill archive is `8bf4540d…`
and canonical manifest is `af36615b…`. The owning validation record contains
the section-level and whole-skill necessity/simplification inventory. The tracked
skill remained unchanged through the complete-draft review gate.
The reviewed scratch proposal is 1,016 words at SHA-256 `38cbe2ae…`.
One pre-approval fix round restored generic file-path reporting, removed added
non-version authority doctrine, and clarified the frontmatter category; its scoped
SPEC/QUALITY re-review passed with no open finding.
On 2026-08-09 the owner instead approved Task 18A's universal factual-claim behavior
slice. That approval supersedes the pending scratch draft before any tracked skill
prose was applied. After Task 18A is committed, its skill becomes the new immediate
readability control and Task 18 restarts its word count, necessity inventory, and
draft against that behavior. The completed pre-slice inventory is historical and
does not satisfy the reset checkbox above.

**Task 18 restarted audit (2026-08-14):** The fresh post-Task-18A inventory is
recorded in `skill-validation/disciplined-research.md` against exact control
`a69e253` / `f4001332…`.
It finds a meaningful behavior-preserving cleanup: consolidate repeated universal
contract wording and four fragmented source-selection/applicability sections while
retaining the exact discovery description, ownership boundary, four-step method,
all difficult-source branches, literal unverified-lead stamp, and all nine pressure
defenses.
The initial scratch proposal was 1,197 words at SHA-256 `54a95c62…`, down
262 words (18.0%) from the 1,459-word control. At that checkpoint it awaited owner
approval and no tracked skill edit or model evaluation had occurred; later evidence
and approved preservation repairs supersede it as the current candidate.

**Task 18 candidate closure (2026-08-14):** The final owner-approved skill is
1,210 words at SHA-256 `6fa7d81c67c3075429c1fd9f54d37d494d0e24f877de976a6c0da71da8a61984`,
249 words (17.1%) below the immutable control. The approved initial arm completed
all 95 affected responses on attempt 1: discovery 60/60 and research application
35/35. Reviews found three unexercised baseline-preservation drifts; owner-approved
repairs restored the official-repository implementation tier, mandatory current-
first-party precedence for current public state, and the source-authority versus
fact-control distinction. Narrow final-hash reruns passed `DR-02` and `DR-03`
10/10 on attempt 1. Under the scenario-to-promise rule, the unchanged discovery
and unaffected research cells remain active, so the final affected gate is 95/95.
The active blinded comparison has zero candidate material losses across 35 pairs:
31 are equivalent and the control has the only four losses. Final exact-hash skill-
writing review passed SPEC/QUALITY, staged adversarial review returned
`DD-VERDICT: PASS`, and the owner approved the complete in-place skill. Durable
hashes and superseded-arm labels are in `skill-validation/disciplined-research.md`.
Fresh repository verification passed: hook tests 373 passed / 3 skipped, installer
tests 11 passed, research tests 4 passed, the skill-package validator passed, local
Markdown links passed for four working and four staged documents, and routing/
reference, non-fixture JSON, exact hash/word/frontmatter, 103-scenario denominator,
and working/staged diff checks passed.

### Task 19: Clean `lean-plan-writing`

**Files:** `skills/lean-plan-writing/SKILL.md`, `skill-validation/lean-plan-writing.md`

**Review focus:** explain the Superpowers override once; order prose contract, tricky-case table, artifact distinction, merge boundary, and rationalizations; keep the contract grounded in software-development planning.

**Validation scope:** development companion; use the seven active owned scenarios in
its intended domain with declared `superpowers:writing-plans`. `LP-04` is historical
and does not rerun or drive a skill change.

- [x] Record the immediate readability-control word count and a section-level meaning inventory.
- [x] Draft the smallest coherent reorganization, show the diff, and wait for user approval.
- [x] Apply the approved draft and run the complete active suite 5/5 on Sol high.
- [x] Blindly compare subjective prose outputs with the immediate readability control where the rubric requires judgment.
- [x] Run cold editorial and skill-writing review; show proposed fixes, wait for user approval, apply them, and restart affected scenarios.
- [x] Show the final skill in place and wait for user approval.
- [x] After approval, run repository tests and commit as `docs(skills): clean up lean plan writing`.

**Task 19 execution note (2026-08-14):** Preflight confirmed the
clean linked worktree on `docs/comprehensive-skill-cleanup`, with local HEAD,
tracking ref, and remote branch all at immutable control
`4cfdee2e7ade66f2937b88031130bd062ec9954e`. The immediate skill control is 813
words / `76351124307a05429d4d594394bca215df92ff7d33679f6367811beb0d8488eb`.
The fresh section and whole-skill audit found a behavior-preserving reorganization
warranted. The owner approved the complete 689-word proposal, and the exact
approved bytes were applied at
`9011ec53995759ff9b99ac2ae880c9e6fea350b1f764c5a138c70fb191e2d835`.
Historical `LP-04` remained excluded from evaluation and change decisions.

The first frozen run completed 70/70 control/candidate generation slots on attempt
1 in its authorized transport. A scorer initially labeled candidate `LP-08` 0/5
only because its five otherwise-correct boundaries did not repeat the supplied
small-change fact. That classification is superseded: all five selected one atomic
branch/PR, kept the three coupled files together, rejected red or inconsistent
splits, and added no compatibility or rollout work. The first scorer ledger therefore
provisionally read 35/35 under the owner-confirmed behavior standard.

Before correction, the scorer result prompted an owner-approved 698-word clarity
variant at `c5ea438f…` and a 10/10 focused rerun. Its nominal `LP-08` 4/5 was the
same processing error: one correct boundary omitted optional reviewability
narration. The behavior is 10/10, and the proposed follow-on bullet rewrite is
withdrawn. The owner selected the smaller, already-evaluated 689-word candidate;
the exact in-place skill is restored at
`9011ec53995759ff9b99ac2ae880c9e6fea350b1f764c5a138c70fb191e2d835`
with then-provisional evidence 35/35 before blind inspection.

The subsequent sealed 35-pair blind comparison reported five raw candidate losses.
Behavior-first inspection overruled the `LP-01` exact-assertion preference but
confirmed four action-level misses: executable syntax in `LP-02` R1, invented input
behavior in `LP-03` R1/R5, and missing RED-before-implementation ordering in
`LP-06` R4. The exact-hash active result is therefore 31/35, not 35/35; the earlier
aggregate above is superseded, and Task 19 is paused before a repair loop.

Fresh cold skill-writing and staged adversarial reviews both block this evidence
state. They reject redundant edits for isolated `LP-02`/`LP-06` noncompliance. The
adversarial review alone proposes conditioning the edge inventory on a task actually
consuming inputs, which directly addresses both `LP-03` misses without changing the
intended contract. That exact fix and its `LP-03`/`LP-05`/`LP-06` restart map await
owner approval; no further skill change has been applied.

The owner approved the exact input-conditional clarification. It is applied at 693
words / `db1ade9e0ba7395bf662d041c866ce80965f729725d3829983adcdfd21946129`.
Fresh final-hash `LP-03`, `LP-05`, and `LP-06` generations completed 15/15 on
attempt 1. Two raw `LP-06` scorer misses and the affected blind comparison's sole
raw candidate loss demand an unrequired “previous completed day”; behavior-first
inspection confirms account-local-day identity and boundaries are correct, so the
affected blind comparison has zero authoritative candidate losses across 15 pairs.
A fresh exact-final-hash `LP-02` arm passed 5/5 on attempt 1 and its focused blind
comparison found zero candidate losses across five pairs. Unchanged `LP-01`,
`LP-07`, and `LP-08` retain their mapped 5/5 evidence, producing an authoritative
active union of 35/35; `LP-04` remains historical and excluded.

Final exact-hash skill-writing review passed SPEC/QUALITY and proposed no change.
The first final adversarial process timed out before a verdict and is
infrastructure-only; its fresh bounded replacement returned no findings and
`DD-VERDICT: PASS`. The owner approved the complete 693-word in-place skill, a
120-word (14.8%) reduction from the immediate readability control.
Durable freeze, score, seal, output, superseded-arm, and transport dispositions are
recorded in `skill-validation/lean-plan-writing.md`.
Fresh repository verification passed: hook tests 373 passed / 3 skipped, installer
tests 11 passed, research tests 4 passed, the skill-package validator passed, and
the exact local-link command passed for five working and five staged Markdown
documents. Routing/reference, exact skill hash/word/frontmatter, frozen-output,
blind-seal, non-fixture JSON, documented malformed-fixture hash, and working/staged
diff checks passed.

### Task 20: Clean `sweeping-stale-references`

**Files:** `skills/sweeping-stale-references/SKILL.md`, `skill-validation/sweeping-stale-references.md`

**Review focus:** make search/triage/reconcile obvious within the authored development domain; keep the software audit artifact explicit; integrate quick reference, scope, example, and rationalizations without restatement.

**Validation scope:** development companion; use the six active owned scenarios in
its intended domain. `SSR-04` is historical and does not rerun or drive a skill
change.

- [x] Record the immediate readability-control word count and a section-level meaning inventory.
- [x] Draft the smallest coherent reorganization, show the diff, and wait for user approval.
- [x] Apply the approved draft and run the complete active suite 5/5 on Sol high.
- [x] Blindly compare subjective prose outputs with the immediate readability control where the rubric requires judgment.
- [x] Run cold editorial and skill-writing review; show proposed fixes, wait for user approval, apply them, and restart affected scenarios.
- [x] Show the final skill in place and wait for user approval.
- [x] After approval, run repository tests and commit as `docs(skills): clean up stale reference sweeping`.

**Task 20 pre-approval evidence (2026-08-14):** The immutable immediate control is
1,527 words at SHA-256 `d92afd5d…`. The current 923-word candidate is
`15992341…`, a 604-word (39.6%) reduction. The initial approved candidate passed
the six-scenario active suite 30/30. Two owner-approved cold-review clarifications
restarted five affected scenarios at 25/25 while unaffected `SSR-07` retained 5/5.
The owner then requested a direct test of the initial cleaned negative-form sentence;
it produced a genuine 0/5 artifact/accounting RED when sibling classified matches
existed. The approved repair passed a two-sided 10/10 focused GREEN covering both
sibling classified matches and multiple matches confined to the changed file, then
restarted active `SSR-05` at 5/5. Across the
30-pair initial comparison, 25-pair affected comparison, and five-pair final
`SSR-05` comparison, manual behavior-first adjudication found zero candidate
material losses. The final exact-hash cold skill-writing/editorial review returned
both verdicts PASS with no findings. The fresh exact-stage adversarial review returned
no findings and `DD-VERDICT: PASS`; the owner approved the complete 923-word
in-place skill. Fresh repository verification passed: hook tests 373 passed / 3
skipped, installer tests 11 passed, research tests 4 passed, the skill-package
validator passed, and local-link, routing/reference, exact hash/word/frontmatter,
frozen-output, blind-seal, JSON-integrity, changed-scope, and both diff checks passed.

### Task 21: Clean `writing-explicit-rationale`

**Files:** `skills/writing-explicit-rationale/SKILL.md`;
`skill-validation/writing-explicit-rationale.md`;
`plans/specs/2026-08-01-comprehensive-skill-cleanup-design.md`;
`skill-validation/fixtures/writing-explicit-rationale/prompts/wer-08.md`;
`skill-validation/fixtures/writing-explicit-rationale/prompts/wer-dev.md`;
`skill-validation/fixtures/writing-explicit-rationale/rubrics/wer-03.md`;
`skill-validation/fixtures/writing-explicit-rationale/rubrics/wer-07.md`;
`skill-validation/fixtures/writing-explicit-rationale/rubrics/wer-08.md`;
`skill-validation/fixtures/writing-explicit-rationale/rubrics/wer-dev.md`.

**Review focus:** state the trigger once; order trigger, non-trigger cases, rationale shape, artifact placement, and failure resistance; consolidate overlapping rationalizations/red flags while preserving compliance.

**Validation scope:** broad-domain companion; the current policy scope is approved
behavior. Use its complete cold Sol-high suite, including isolated non-software
application, and do not introduce a policy-scope edit.

- [x] Record the immediate readability-control word count and a section-level meaning inventory.
- [x] Draft the smallest coherent reorganization, show the diff, and wait for user approval.
- [x] Evaluate the approved draft against the complete active Sol-high suite; reject it after its 29/30 result and restore the exact immediate control, whose corrected result is also 29/30.
- [x] Blindly compare subjective prose outputs with the immediate readability control where the rubric requires judgment.
- [x] Run cold editorial and skill-writing review; repair review-found validation bookkeeping without changing the skill, and obtain a clean final exact-stage review.
- [x] Record the owner-approved no-change disposition: reject the cleanup attempt, retain the exact control, preserve the `WER-07` misses as model-execution evidence, and do not treat them as either a pass or grounds for another wording trial.
- [x] Show the final skill in place and wait for user approval.
- [x] After approval, run repository tests and commit as `docs(validation): repair explicit rationale tests`.

**Task 21 repair evidence and closure (2026-08-15):** The immutable immediate
control is 372 words at SHA-256 `568b2a61…`. The initially approved 357-word
candidate is `1bc78cb7…`. Its first run completed without infrastructure errors,
but the later exact-stage adversarial review correctly invalidated the reported
30/30 result: `WER-03` was 2/5 because three outputs shifted monthly-review scope,
invented review ownership, or narrowed the contingency boundary. The owner approved
a separate behavioral RED/GREEN slice, but both approved wording trials failed.
A fresh committed-control/restored-candidate comparison then showed the analogous
software probe failing primarily on generic amendment-rewriting fidelity in both
arms. The owner approved a validation-only behavior-first contract repair: retire
`WER-03` and `WER-DEV` to historical diagnostics, replace active broad-domain
coverage with isolated `WER-08`, and score each active test by observable owned
behavior rather than exact wording or generic rendering. The revised contracts
passed fresh Sol-high design review with no findings. Fresh execution completed all
60 high control/candidate and 30 low-control slots on attempt 1 with zero
infrastructure errors. Initial manual behavior-first adjudication scored high
control 30/30, restored candidate 29/30, and low control 29/30; new `WER-08` passed
15/15 across those arms. Candidate `WER-02` r4 genuinely replaces the supplied
third-interactive-caller revisit boundary with a different future guard-placement
action, so the active gate remains blocked. The low `WER-07` miss invents an
unsupported quota alternative and is recorded as robustness evidence. No third
skill wording edit is authorized. At that point, a disposition, any owner-approved
next slice, cold skill review, final owner approval, repository verification,
closure bookkeeping, commit, and push remained pending.

The owner then approved an attribution-only WER-02 expansion with exact unchanged
prompt, rubric, control, and candidate bytes. All 20 new Sol-high slots completed on
attempt 1 with zero infrastructure errors. The sealed ten-pair result is control
10/10 and candidate 9/10; combined with the prior frozen cells, WER-02 is control
15/15 and candidate 13/15. Both candidate failures change or omit the supplied
third-interactive-caller extraction boundary, while no control output does. This
supports candidate-linked unreliability on an owned behavior but does not identify
causal wording or authorize another skill trial. The original 29/30 candidate gate
remains authoritative and blocked.

The owner accepted the recommendation to reject that candidate and restore the
exact 372-word immediate control. The tracked skill now has SHA-256 `568b2a61…`
and zero diff from its `c54c4016…` control object. Because those are the exact bytes
used by the fresh behavior-first control arm, its frozen results apply directly; a
duplicate generative arm would not establish a different contract. Final
restoration review then corrected one earlier manual override: high-control
`WER-07` r2 omits the supplied no-downstream-consequence fact, so high control is
29/30, not 30/30. The correction is `8f4f48c0…`, and the blocking review is
`ca99e251…`. The cleanup candidate and both repair trials remain rejected historical
evidence, while combined WER-02 remains control 15/15 versus candidate 13/15.
The restored current skill therefore also misses the active gate; no further skill
wording change is authorized. A user-approved disposition or separate repair slice
must precede final in-place approval, repository verification, closure bookkeeping,
commit, or push.

The concurrent cold skill-writing/editorial review passed `SPEC` and `QUALITY` with
no finding at `01c8d43e…`. Exact-stage review `ca99e251…` found the high-control
adjudication error, stale restored-heading references, and an incomplete Task 21
file inventory; all are now corrected in the records. Follow-up review `b2ae1066…`
verified those repairs but found archival prose inside three supposedly exact
historical evaluator fixtures. Those fixtures now match their evaluated bytes at
WER-03 rubric `c2c586c8…`, WER-DEV prompt `93f5fb44…`, and WER-DEV rubric
`5dc06e1a…`; their historical disposition remains outside evaluator inputs.
The final exact-stage follow-up returned no findings and `DD-VERDICT: PASS` at
`585149ab…`. Review is clean, but the corrected 29/30 current behavioral gate still
blocks final in-place approval and closure.

The owner then approved a no-edit WER-07 causal diagnostic. Ten fresh exact-current
Sol-high repetitions completed on attempt 1 with zero infrastructure errors at
freeze `456736a6…` and verification file `33ec55f7…`. The WER ledger is 8/10:
r5 omits the approved-only `persist()` boundary and r9 attaches the no-consequence
fact only to Library B; the composition ledger is 10/10. Five independent causal
meta-reviewers unanimously returned `CLEAR_RULE_TASK_FIDELITY` with no skill gap or
composition failure; meta verification is `4374f7c5…`. The current skill already
states the necessary consequences/limits/lack-of-either rule, so this evidence does
not justify a third wording trial. It raises a validation-architecture disposition:
whether strict 5/5 blocks an unchanged skill even when failure causality is generic
semantic transformation under an already-clear rule. No protocol change is yet
authorized, so Task 21 remains blocked before final approval or closure.

The owner approved the no-change disposition. Task 21's readability attempt is
rejected rather than accepted at 29/30: the exact 372-word control remains in place,
and no third skill wording trial is authorized. The `WER-07` misses remain genuine
owned model-execution evidence, are not relabeled as passes, and do not justify an
edit to an already-clear rule. This disposition permits Task 21 to proceed to the
separate final in-place approval gate because it ships no cleanup candidate; it does
not waive the active scenario's strict 5/5 requirement or remove `WER-07` from the
final repository-wide suite. Final owner approval, repository verification, closure
bookkeeping, commit, and push remain pending.

The owner then approved the complete in-place 372-word skill at exact SHA-256
`568b2a61…`. This final approval accepts the restored skill, not the rejected
readability candidate and not a relabeling of the retained WER-07 failures.
Fresh repository verification passed on the final tree: hook tests 373 passed / 3
skipped, installer tests 11 passed, research tests 4 passed, and the exact local-link
command passed for 10 working and 10 staged Markdown documents. Exact skill/control
identity, historical fixture hashes, causal and correction JSON consistency, the
routing/reference sweep, and both working and staged diff checks passed. Task 21
closes as a rejected no-change readability attempt in
`docs(validation): repair explicit rationale tests`; the final repository-wide suite
retains strict WER-07 coverage. No PR is opened.

### Task 22: Clean `adversarial-review`

**Approved validation-design ruling (2026-08-15; activated 2026-08-16):** Task 22’s semantic/protocol split, execution status, activation conditions, and pre-redesign evidence boundary are owned by [the adversarial-review validation record](../skill-validation/adversarial-review.md#approved-task-22-validation-method-2026-08-15-activated-2026-08-16). The plan records status only; the exact current skill at `309bd02c…` passed semantic 75/75, same-byte protocol and actual-renderer gates 70/70, affected composition 5/5, a balanced/net-positive blinded comparison with no causal regression, final cold review, final owner approval, and repository verification. The first staged review's two documentation findings are corrected and the scoped staged re-review returned no findings; commit and push remain pending.

**Files:**

- Modify: `plans/specs/2026-08-01-comprehensive-skill-cleanup-design.md`, `skill-validation/README.md`, `skill-validation/adversarial-review.md`, and `skill-validation/fixtures/adversarial-review/README.md`
- Modify: `plans/2026-08-01-comprehensive-skill-cleanup.md` (this Task 22 inventory and ruling)
- Modify: `skill-validation/fixtures/adversarial-review/prompts/ar-04.md`, `skill-validation/fixtures/adversarial-review/rubrics/ar-04.md`, `skill-validation/fixtures/adversarial-review/rubrics/ar-05.md`, `skill-validation/fixtures/adversarial-review/rubrics/ar-08.md`, `skill-validation/fixtures/adversarial-review/rubrics/ar-13.md`, and `skill-validation/fixtures/adversarial-review/rubrics/ar-14.md`
- Modify: `skills/adversarial-review/SKILL.md`
- Modify: `skills/disciplined-development/hooks/lib/severity.py`, `skills/disciplined-development/hooks/tests/test_severity.py`
- Modify: `ARCHITECTURE.md`, `CLAUDE.md`, and `README.md` for the bundled renderer surface
- Create: `skill-validation/validate_adversarial_review_output.py`, `skill-validation/tests/test_validate_adversarial_review_output.py`, and `skill-validation/tests/test_render_adversarial_review_output.py`
- Create: `skills/adversarial-review/scripts/render_review.py`
- Create: `skill-validation/fixtures/adversarial-review/prompts/ar-15.md`, `skill-validation/fixtures/adversarial-review/rubrics/ar-15.md`, `skill-validation/fixtures/adversarial-review/ar-15/project/approval-evidence.md`, `skill-validation/fixtures/adversarial-review/ar-15/project/change-request.md`, `skill-validation/fixtures/adversarial-review/ar-15/project/decision-record.md`, `skill-validation/fixtures/adversarial-review/ar-15/project/interface-contract.md`, `skill-validation/fixtures/adversarial-review/ar-15/project/proposal.md`, and `skill-validation/fixtures/adversarial-review/ar-15/project/support-evidence.md`
- Create: `skill-validation/fixtures/adversarial-review/prompts/ar-16.md`, `skill-validation/fixtures/adversarial-review/rubrics/ar-16.md`, `skill-validation/fixtures/adversarial-review/ar-16/project/contract.md`, and `skill-validation/fixtures/adversarial-review/ar-16/project/EventLog.swift`
- Create: `skill-validation/fixtures/adversarial-review/prompts/ar-17.md`, `skill-validation/fixtures/adversarial-review/rubrics/ar-17.md`, `skill-validation/fixtures/adversarial-review/ar-17/project/contract.md`, and `skill-validation/fixtures/adversarial-review/ar-17/project/EventLog.swift`

**Review focus:** preserve direct invocation within the full bundle; order posture, severity/output contract, holistic rules, angle selection, examples, and composition; keep the baseline/angle distinction unmistakable; remove historical bolt-on seams without shrinking coverage.

**Validation scope:** integrated development group; use the complete bundle and cold
Sol-high model gate in the authored software-review domain.

- [x] Record the immediate readability-control word count and a section-level meaning inventory.
- [x] Draft the smallest coherent reorganization, show the diff, and wait for user approval.
- [x] Apply the approved draft and run the complete active suite plus affected composition scenarios 5/5 on Sol high.
- [x] Blindly compare subjective review outputs with the immediate readability control where the rubric requires judgment.
- [x] Run cold editorial and skill-writing review; show proposed fixes, wait for user approval, apply them, and restart affected scenarios.
- [x] Show the final skill in place and wait for user approval.
- [x] After approval, run repository tests and `git diff --check` plus `git diff --cached --check`; commit as `docs(skills): clean up adversarial review`, push the branch, do not open a PR, and do not remove this worktree.

### Task 23: Clean `adversarial-review-loop`

**Files:** `skills/adversarial-review-loop/SKILL.md`, `skill-validation/adversarial-review-loop.md`, `skill-validation/adversarial-review-loop-scenarios.md`

**Review focus:** make scope/precedence, normal loop, class/root attack, three-cycle cap, cold escape, and clean stop read as one state machine; preserve per-task versus whole-branch ownership.

**Validation scope:** integrated development group; use the complete bundle and cold
Sol-high model gate in the authored software-review domain.

**Current Task 23 result (2026-08-16):** the exact approved 1,486-word candidate
`0113503c…` passed its 75/75 owned/composition slice. The all-scenario blinded
comparison was materially net-positive at 13 candidate preferences, 8 control
preferences, and 54 equivalent pairs; causal reconciliation found no missing or
weakened candidate rule, and no zero-loss blind gate is specified here. A fresh Sol-high reviewer
applying `superpowers:writing-skills` returned PASS with no proposed skill change
or restart map. The owner's subsequent in-place approval covered exact SHA
`0113503c…`, but the first staged review correctly found that the complete active
suite also requires fresh `DISC-01`–`DISC-12`, `CW-09`, and `CW-11` evidence.
Those 70 shared slots now pass 70/70 at attempt 1 with zero transport errors or
retries, making the complete active gate 145/145 against the unchanged candidate.
The catalog omission found by that review is also corrected. The earlier approval
remains non-final because it preceded this evidence. Fresh staged Gate 5 then
returned PASS with no P1/P2 findings and `DD-PATTERN: NONE`; final verification
then passed, and the owner renewed final approval for exact SHA `0113503c…`.
Closure commit and push are authorized.

- [x] Record the immediate readability-control word count and a state/transition meaning inventory.
- [x] Draft the smallest coherent reorganization, show the diff, and wait for user approval.
- [x] Apply the approved draft and run every active loop branch plus affected composition scenarios 5/5 on Sol high.
- [x] Run the complete shared discovery and authoring-boundary slice so the full
  current candidate gate reaches 145/145.
- [x] Blindly compare subjective remediation outputs with the immediate readability control where the rubric requires judgment.
- [x] Run cold editorial and skill-writing review; show proposed fixes, wait for user approval, apply them, and restart affected scenarios.
- [x] Pass fresh staged Gate 5 against the complete 145/145 evidence and corrected
  affected-skill catalog.
- [x] After the complete 145-slot active gate and staged review pass, show the
  unchanged final skill in place and wait for renewed user approval.
- [x] After approval, run repository tests, the exact local-link command, and
  `git diff --check` plus `git diff --cached --check`; commit as
  `docs(skills): clean up adversarial review loop`, push the current branch, do
  not open a PR, and do not remove this worktree.

### Task 24: Clean `dispatching-development-subagents`

**Files:** `skills/dispatching-development-subagents/SKILL.md`, `skill-validation/dispatching-development-subagents.md`

**Review focus:** align Role/Overview/When-you-dispatch; state the scope contract once; keep orchestrator verification and subagent gate boundaries explicit; depend on the full development bundle without relying on an upstream report heading.

**Validation scope:** integrated development group; use the complete bundle and cold
Sol-high model gate with all declared orchestration dependencies.

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

**Validation scope:** integrated development group; use the complete bundle and cold
Sol-high model gate across the authored development modes.

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

**Required final scenarios:** the shared all-nine description-discovery suite; direct invocation of each of the nine skills in its intended domain with declared dependencies; isolated non-software application of the three broad-domain companions; in-domain validation of the two development companions; complete-bundle composition for the integrated development group; parent routing across plan, implementation, debugging, review, documentation, and delegation modes; per-task versus whole-branch review ownership.

**Produces:** A cross-suite composition record that links the owning scenario IDs and records joint results without duplicating their prompts or rubrics.

- [ ] Freeze the 105-scenario active closure, excluding historical `LP-04` and `SSR-04`.
- [ ] Rerun every scenario in the frozen 105-scenario closure five times on cold Sol high, including all focused regressions as well as the shared discovery, domain-appropriate direct-invocation, broad-domain isolated-application, development-companion dependency, and integrated composition sets; keep scenarios atomic unless composition is the behavior under test.
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

**Validation scope:** reuse the same 105 domain-appropriate scenarios and declared
dependencies from the cold Sol-high gate. Sol-low measures effort robustness and does
not create another portability domain or provider gate.

- [ ] Freeze the 105-scenario final active suite, which excludes historical `LP-04` and `SSR-04`, and run every scenario five times on `gpt-5.6-sol` at low reasoning effort.
- [ ] Compare control and cleaned scores by scenario and pause for user review on any decrease.
- [ ] For every decrease, record the user-approved disposition in `skill-validation/README.md` and each affected record.
- [ ] If accepted, record the what/why/accepted rationale; if remediation changes a skill or scenario contract, reopen its owning task, complete the required Sol-high backfill or regression suite, rerun the affected Sol-low arm, and return to this comparison.
- [ ] Record final word-count deltas for all nine skills.
- [ ] Run the hook, installer, and research pytest suites plus `git diff --check`.
- [ ] Run a final cold consistency review against the design and this plan.
- [ ] Mark the plan complete only when every success criterion in the design has evidence.
- [ ] Move the completed plan and design to their completed directories, update the plan's design-reference label and target plus every live repository reference, and run the exact local-link command plus `git diff --check`.
- [ ] Commit as `docs(skills): complete comprehensive cleanup validation`.
