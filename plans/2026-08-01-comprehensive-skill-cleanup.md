# Comprehensive Skill Cleanup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish a trustworthy validation baseline, then make all nine skills compact and coherent without losing effectiveness.

**Architecture:** Treat the pinned skill tree at `4296647` as the regression control for original behavior. Build a shared validation protocol and one active scenario catalog per skill, record Sol-high and Sol-low baseline results, then process each skill through any required portability RED/GREEN slice followed by a behavior-preserving readability cleanup. A successful portability slice becomes that skill's immediate readability control; otherwise `4296647` serves both roles. Clean `disciplined-development` last so it routes settled child contracts.

**Tech stack:** Markdown skills and validation records; `gpt-5.6-sol` evaluation subagents; Superpowers 6.2.0; Git; Python/pytest for repository regression suites.

**Design reference:** [`plans/specs/2026-08-01-comprehensive-skill-cleanup-design.md`](specs/2026-08-01-comprehensive-skill-cleanup-design.md)

## Global constraints

- Primary authoring and validation use `gpt-5.6-sol` at high reasoning effort.
- Every behavioral scenario uses five fresh, read-only evaluators with no nested dispatch; run at most three evaluators concurrently.
- Evaluator prompts never contain or point to the scoring rubric.
- Manually score every completed response; a missed criterion is a failure, not a discarded run.
- Record infrastructure failures separately and retry them without counting them as behavioral results.
- Preservation scenarios require a 5/5 control at `4296647`; approved target scenarios require a watched control RED and 5/5 GREEN.
- A preservation result below 5/5 stops the task for the design's failure-classification gate; do not continue by weakening the rubric or editing the skill.
- After changing scenario wording, restart that scenario at zero.
- Do not commit raw evaluator transcripts.
- For subjective cleanup comparisons, rerun five fresh immediate-readability-control arms and five fresh draft arms, anonymize the labels, and keep temporary outputs in scratch space outside the repository until the scored summary is recorded.
- Do not edit skill prose until Tasks 1–11 establish and score the control suite.
- Portable-behavior edits and readability edits land in separate commits.
- A whole-skill cleanup reruns that skill's complete active Sol-high suite.
- Show every skill draft before applying it, and show the edited file in place before committing it.
- Skill prose uses one sentence per line with the repository's structural exceptions.
- Each skill commit records applicable control/current word counts, model results, cold review, repository tests, and any reference sweep.
- For portable skills with a behavior slice, record word counts for `4296647`, the post-portability readability control, and the cleaned version.
- Update this plan's checkboxes and notes in every task commit; the task file lists omit this repeated path.
- Tasks 2–10 classify every existing scenario with the common taxonomy and update the audit status, classification counts, and scores in `skill-validation/README.md`; validation-bearing Tasks 12–25 keep that index current.
- The task file lists omit this repeated index path.
- Before every commit, run the local Markdown-link check for changed documents and `git diff --check`.
- Before each skill commit run:
  - `cd skills/disciplined-development/hooks && python3 -m pytest -q`
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

---

### Task 1: Establish the validation protocol and index

**Files:**

- Create: `skill-validation/README.md`
- Create: `skill-validation/skill-discovery.md`
- Modify: `CLAUDE.md`
- Modify: `README.md`

**Produces:** One source of truth for scenario types, evaluator isolation, 5/5 scoring, run metadata, preservation versus target scenarios, infrastructure errors, Sol-high/Sol-low arms, and the compact per-skill catalog format; plus one shared suite of atomic all-nine discovery scenarios.

- [ ] **Step 1: Inventory the current framework**

  List every file under `skill-validation/`, its purpose, its active scenario IDs, repetition counts, and whether exact prompts and evaluator-withheld rubrics are recoverable.

- [ ] **Step 2: Write the shared protocol**

  Define the universal rules from the design once in `skill-validation/README.md`.
  Include the active-catalog fields: scenario ID, type, protected promise, protected skill section, supplied skill context, exact prompt or fixture link, evaluator-withheld rubric, control result, target GREEN when applicable, cleaned result, Sol-low scores, and rerun triggers.

- [ ] **Step 3: Add the audit index**

  Add one row per skill and supporting scenario file, with its owner, audit task, `Unaudited` status, classification-count columns, and a link to the owning record.
  Tasks 2–10 change the status to `Audited` and fill the `Keep`, `Repair`, `Merge`, `Retire`, and `Add` counts.
  Preserve historical records below each active catalog rather than rewriting them.

- [ ] **Step 4: Establish the shared discovery suite**

  Put a fixed set of atomic scenarios in `skill-validation/skill-discovery.md`.
  Each evaluator prompt contains all nine control descriptions and one simple user request, with one expected skill or an explicit allowed set in the withheld rubric.
  Evaluators never see skill bodies or the rubric.
  Run each scenario five times on Sol high at `4296647`, manually score every route, and map each scenario to every description whose positive or negative routing it protects.

- [ ] **Step 5: Update repository guidance**

  Point `CLAUDE.md` and the project `README.md` at `skill-validation/README.md` for the validation protocol.
  Keep universal rules out of individual validation records.

- [ ] **Step 6: Verify and commit**

  Run the local Markdown-link check and `git diff --check`.
  Commit as `docs(validation): define the skill validation protocol`.

### Task 2: Audit and baseline `concise-writing`

**Files:**

- Modify: `skill-validation/concise-writing.md`
- Modify if still shared: `skill-validation/duplicate-red-flags-scenarios.md`
- Read control: `skills/concise-writing/SKILL.md` at `4296647`

**Required coverage:** link the shared discovery suite; simple padding removal; non-trivial compression that preserves rationale, navigation, and a load-bearing recap; safe direct invocation; non-software extraction using a policy or grant document; still-relevant verbosity, over-trim, trigger-routing, and red-flag-consolidation regressions.

- [ ] Audit existing scenarios and classify each `Keep`, `Repair`, `Merge`, or `Retire`.
- [ ] Add only missing coverage; merge the shared composite fixture into atomic skill scenarios where its unrelated output contracts would interfere.
- [ ] Record exact prompts, supplied context, rubrics, protected sections, and rerun triggers in the active catalog.
- [ ] Run every preservation scenario 5/5 on Sol high against `4296647`; classify a 5/5 portability result as preservation coverage or record a watched RED target.
- [ ] Manually score every response and record exact misses without transcripts.
- [ ] Review the record against `skill-validation/README.md`, run `git diff --check`, and commit as `docs(validation): baseline concise writing`.

### Task 3: Audit and baseline `disciplined-research`

**Files:**

- Modify: `skill-validation/disciplined-research.md`
- Read control: `skills/disciplined-research/SKILL.md` at `4296647`

**Required coverage:** link the shared discovery suite; simple source acquisition and verification; a non-trivial authority/deadline scenario whose premise is disconfirmed; safe direct invocation; non-software extraction using museum, policy, or procurement research; the historical disclaimer-as-substitute and citation-as-substitute experiments, retained or retired honestly.

- [ ] Map the skill's claims to existing B1/B17 evidence and distinguish shipped regressions from closed experiments.
- [ ] Link the shared discovery result and add atomic application, direct-invocation, and extraction scenarios with exact evaluator-withheld rubrics.
- [ ] Run preservation scenarios 5/5 on Sol high at `4296647`; classify a 5/5 portability result as preservation coverage or record a watched RED target.
- [ ] Record failures and variance, review the active catalog, and commit as `docs(validation): baseline disciplined research`.

### Task 4: Audit and baseline `lean-plan-writing`

**Files:**

- Modify: `skill-validation/lean-plan-writing.md`
- Modify if still shared: `skill-validation/duplicate-red-flags-scenarios.md`
- Read control: `skills/lean-plan-writing/SKILL.md` at `4296647`

**Required coverage:** link the shared discovery suite; simple prose-as-contract planning; the non-trivial `KEY=VALUE` parser plan without implementation bodies; safe direct invocation with `superpowers:writing-plans`; non-software extraction using an event or publishing plan; unexercised-case, trigger-routing, and red-flag-consolidation regressions.

- [ ] Audit and atomize existing scenarios without losing historical results.
- [ ] Make the upstream override, input/output-table substitute, and five-line ambiguity exception independently scorable.
- [ ] Run preservation scenarios 5/5 on Sol high at `4296647`; classify a 5/5 portability result as preservation coverage or record a watched RED target.
- [ ] Review the active catalog and commit as `docs(validation): baseline lean plan writing`.

### Task 5: Audit and baseline `sweeping-stale-references`

**Files:**

- Modify: `skill-validation/sweeping-stale-references.md`
- Modify if still shared: `skill-validation/duplicate-red-flags-scenarios.md`
- Read control: `skills/sweeping-stale-references/SKILL.md` at `4296647`

**Required coverage:** link the shared discovery suite; a simple load-bearing rename; the non-trivial 126-match grouped sweep; safe direct invocation; non-software extraction using a renamed policy term across handbooks and forms; reviewer-one-hit, three-way classification, grouping/reconciliation, negative-form, and red-flag-consolidation regressions.

- [ ] Audit the current record and separate the portable search/triage/reconcile contract from software-specific commit evidence.
- [ ] Add atomic prompts and rubrics for literal/synonym search, all required file categories, three classifications, count reconciliation, and grouped evidence.
- [ ] Run preservation scenarios 5/5 on Sol high at `4296647`; classify a 5/5 non-software portability result as preservation coverage or record a watched RED target.
- [ ] Review and commit as `docs(validation): baseline stale reference sweeping`.

### Task 6: Audit and baseline `writing-explicit-rationale`

**Files:**

- Modify: `skill-validation/writing-explicit-rationale.md`
- Read control: `skills/writing-explicit-rationale/SKILL.md` at `4296647`

**Required coverage:** link the shared discovery suite; a simple descope; a non-trivial active choice that review could re-litigate; safe direct invocation; non-software extraction using a nonprofit budget or policy exception; reviewer-visibility and trigger-routing regressions.

- [ ] Audit current scenarios and map them to the trigger test, on-page location, what/why/accepted shape, and non-trigger counterexamples.
- [ ] Add atomic direct and extraction scenarios without exposing the rubric.
- [ ] Run preservation scenarios 5/5 on Sol high at `4296647`; classify a 5/5 portability result as preservation coverage or record a watched RED target.
- [ ] Review and commit as `docs(validation): baseline explicit rationale`.

### Task 7: Audit and baseline `adversarial-review`

**Files:**

- Modify: `skill-validation/adversarial-review.md`
- Modify if still shared: `skill-validation/duplicate-red-flags-scenarios.md`
- Read control: `skills/adversarial-review/SKILL.md` at `4296647`

**Required coverage:** link the shared discovery suite; simple review with a concrete defect; non-trivial unverified-rationale plus fragile-invariant review; safe direct invocation with all nine skills available; severity/verdict format; holistic baseline; angle discrimination and selection; durability; whole-repo scope; unexercised cases; fix-by-construction severity.

- [ ] Inventory the large historical record and identify the minimal active scenario set that still protects every distinct promise.
- [ ] Retain discrimination tests only when the compared arms and scoring remain reproducible.
- [ ] Replace unrelated composite regression cells with atomic prompts while preserving their historical result.
- [ ] Run every active preservation scenario 5/5 on Sol high at `4296647`.
- [ ] Review coverage against the skill's baseline rules and angle table, then commit as `docs(validation): baseline adversarial review`.

### Task 8: Audit and baseline `adversarial-review-loop`

**Files:**

- Modify: `skill-validation/adversarial-review-loop.md`
- Modify: `skill-validation/adversarial-review-loop-scenarios.md`
- Read control: `skills/adversarial-review-loop/SKILL.md` at `4296647`

**Required coverage:** link the shared discovery suite; singular-finding application; non-trivial shared-root and cycle-cap pressure; safe direct invocation with the full bundle; class sweep; P3 stop; re-run discipline; project-wide/cross-language scope; cycle-3 step-back branches; per-task versus whole-branch ownership.

- [ ] Reconcile the narrative record with the re-runnable suite and give each distinct active scenario one owner.
- [ ] Merge genuine duplicates, retire obsolete 3-repetition variants, and upgrade every retained scenario to the common 5/5 protocol.
- [ ] Preserve the existing CS, T2–T7, NF, PW, XL, G3A–G3C IDs when their contracts remain current.
- [ ] Run every active preservation scenario 5/5 on Sol high at `4296647`.
- [ ] Review branch coverage and commit as `docs(validation): baseline adversarial review loop`.

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
- Modify when results live there: `skill-validation/adversarial-review-loop-scenarios.md`

**Produces:** Five Sol-low control-tree outcomes for every frozen preservation and target scenario, directly comparable with the Sol-high baseline results.

- [ ] Freeze the scenario files and rubrics established in Tasks 1–10.
- [ ] Run every frozen preservation and target scenario five times against `4296647` with `gpt-5.6-sol` at low reasoning effort and otherwise identical context.
- [ ] Record 0–5 scores and exact missed criteria; do not change skill wording in response.
- [ ] Add a compact cross-skill score table to `skill-validation/README.md`.
- [ ] Review counts against the catalog, run `git diff --check`, and commit as `docs(validation): record Sol-low control scores`.

### Task 12: Resolve `concise-writing` portability, if the control is RED

**Files:**

- Modify when RED: `skills/concise-writing/SKILL.md`
- Modify: `skill-validation/concise-writing.md`

- [ ] Inspect the recorded extraction result; if it is 5/5, classify it as preservation coverage, record that no skill edit is required, and close the task through the plan/index update.
- [ ] If RED, show the observed failure and proposed minimal dependency/domain-neutrality change to the user.
- [ ] Apply only the change needed for portable extraction while preserving software examples and current software scenarios.
- [ ] Run the target scenario to 5/5 GREEN and rerun every affected preservation scenario 5/5 on Sol high.
- [ ] Run cold skill-writing review, repository tests, and commit the behavioral slice separately.

### Task 13: Resolve `disciplined-research` portability, if the control is RED

**Files:**

- Modify when RED: `skills/disciplined-research/SKILL.md`
- Modify: `skill-validation/disciplined-research.md`

- [ ] Inspect the recorded extraction result; if it is 5/5, classify it as preservation coverage, record that no skill edit is required, and close the task through the plan/index update.
- [ ] If RED, show the failure and a minimal change that keeps sibling sweep/rationale references optional while preserving development examples.
- [ ] Apply only the approved source-acquisition, verification, or citation boundary change needed for extraction.
- [ ] Establish target 5/5 GREEN and rerun every affected preservation scenario 5/5 on Sol high.
- [ ] Run cold skill-writing review and repository tests, then commit the behavioral slice separately.

### Task 14: Resolve `lean-plan-writing` portability, if the control is RED

**Files:**

- Modify when RED: `skills/lean-plan-writing/SKILL.md`
- Modify: `skill-validation/lean-plan-writing.md`

- [ ] Inspect the recorded extraction result; if it is 5/5, classify it as preservation coverage, record that no skill edit is required, and close the task through the plan/index update.
- [ ] If RED, show the failure and a minimal change that retains `superpowers:writing-plans` while making prose-as-contract usable for non-software plans.
- [ ] Apply only the approved portability change and preserve every software plan requirement.
- [ ] Establish target 5/5 GREEN and rerun every affected preservation scenario 5/5 on Sol high.
- [ ] Run cold skill-writing review and repository tests, then commit the behavioral slice separately.

### Task 15: Resolve `sweeping-stale-references` portability, if the control is RED

**Files:**

- Modify when RED: `skills/sweeping-stale-references/SKILL.md`
- Modify: `skill-validation/sweeping-stale-references.md`

- [ ] Inspect the recorded extraction result; if it is 5/5, classify it as preservation coverage, record that no skill edit is required, and close the task through the plan/index update.
- [ ] If RED, show the failure and a minimal change that keeps search/triage/reconcile portable.
- [ ] If RED, apply the approved wording that keys Git commit evidence to version-controlled software changes and preserves the existing software commit-body contract.
- [ ] Establish target 5/5 GREEN and rerun every affected preservation scenario 5/5 on Sol high.
- [ ] Run cold skill-writing review and repository tests, then commit the behavioral slice separately.

### Task 16: Resolve `writing-explicit-rationale` portability, if the control is RED

**Files:**

- Modify when RED: `skills/writing-explicit-rationale/SKILL.md`
- Modify: `skill-validation/writing-explicit-rationale.md`

- [ ] Inspect the recorded extraction result; if it is 5/5, classify it as preservation coverage, record that no skill edit is required, and close the task through the plan/index update.
- [ ] If RED, show the failure and a minimal change to the trigger test or artifact scope that makes code/plan/PR cases examples rather than prerequisites.
- [ ] Apply only the approved portability change while preserving the what/why/accepted contract.
- [ ] Establish target 5/5 GREEN and rerun every affected preservation scenario 5/5 on Sol high.
- [ ] Run cold skill-writing review and repository tests, then commit the behavioral slice separately.

### Task 17: Clean `concise-writing`

**Files:** `skills/concise-writing/SKILL.md`, `skill-validation/concise-writing.md`

**Review focus:** integrate Role/Owns/Overview without repetition; order the core test, two-altitude pass, patterns, guard, and optional composition naturally; retain the rationalization table and one distinct example.

- [ ] Record the immediate readability-control word count and a section-level meaning inventory.
- [ ] Draft the smallest coherent reorganization and show the diff to the user before applying it.
- [ ] Apply the approved draft, preserving every active promise.
- [ ] Run the complete active suite 5/5 on Sol high and blindly compare subjective prose outputs with the immediate readability control.
- [ ] Run cold editorial and skill-writing review; address findings and restart affected scenarios.
- [ ] Show the skill in place, run repository tests, and commit as `docs(skills): clean up concise writing`.

### Task 18: Clean `disciplined-research`

**Files:** `skills/disciplined-research/SKILL.md`, `skill-validation/disciplined-research.md`

**Review focus:** clarify when the skill applies; make acquire/verify facets flow as one method; remove overlap among overview, rationalizations, and red flags; keep optional suite composition out of the portable core.

- [ ] Record the immediate readability-control word count and a section-level meaning inventory.
- [ ] Draft the smallest coherent reorganization and show the diff before applying it.
- [ ] Apply the approved draft and run the complete active suite 5/5 on Sol high.
- [ ] Blindly compare subjective prose outputs with the immediate readability control where the rubric requires judgment.
- [ ] Run cold editorial and skill-writing review; address findings and restart affected scenarios.
- [ ] Show the skill in place, run repository tests, and commit as `docs(skills): clean up disciplined research`.

### Task 19: Clean `lean-plan-writing`

**Files:** `skills/lean-plan-writing/SKILL.md`, `skill-validation/lean-plan-writing.md`

**Review focus:** explain the Superpowers override once; order prose contract, tricky-case table, artifact distinction, merge boundary, and rationalizations; keep software examples without making the core software-only.

- [ ] Record the immediate readability-control word count and a section-level meaning inventory.
- [ ] Draft the smallest coherent reorganization and show the diff before applying it.
- [ ] Apply the approved draft and run the complete active suite 5/5 on Sol high.
- [ ] Blindly compare subjective prose outputs with the immediate readability control where the rubric requires judgment.
- [ ] Run cold editorial and skill-writing review; address findings and restart affected scenarios.
- [ ] Show the skill in place, run repository tests, and commit as `docs(skills): clean up lean plan writing`.

### Task 20: Clean `sweeping-stale-references`

**Files:** `skills/sweeping-stale-references/SKILL.md`, `skill-validation/sweeping-stale-references.md`

**Review focus:** make search/triage/reconcile the obvious portable core; condition the software audit artifact correctly; integrate quick reference, scope, example, and rationalizations without restatement.

- [ ] Record the immediate readability-control word count and a section-level meaning inventory.
- [ ] Draft the smallest coherent reorganization and show the diff before applying it.
- [ ] Apply the approved draft and run the complete active suite 5/5 on Sol high.
- [ ] Blindly compare subjective prose outputs with the immediate readability control where the rubric requires judgment.
- [ ] Run cold editorial and skill-writing review; address findings and restart affected scenarios.
- [ ] Show the skill in place, run repository tests, and commit as `docs(skills): clean up stale reference sweeping`.

### Task 21: Clean `writing-explicit-rationale`

**Files:** `skills/writing-explicit-rationale/SKILL.md`, `skill-validation/writing-explicit-rationale.md`

**Review focus:** state the trigger once; order trigger, non-trigger cases, rationale shape, artifact placement, and failure resistance; consolidate overlapping rationalizations/red flags while preserving compliance.

- [ ] Record the immediate readability-control word count and a section-level meaning inventory.
- [ ] Draft the smallest coherent reorganization and show the diff before applying it.
- [ ] Apply the approved draft and run the complete active suite 5/5 on Sol high.
- [ ] Blindly compare subjective prose outputs with the immediate readability control where the rubric requires judgment.
- [ ] Run cold editorial and skill-writing review; address findings and restart affected scenarios.
- [ ] Show the skill in place, run repository tests, and commit as `docs(skills): clean up explicit rationale`.

### Task 22: Clean `adversarial-review`

**Files:** `skills/adversarial-review/SKILL.md`, `skill-validation/adversarial-review.md`

**Review focus:** preserve direct invocation within the full bundle; order posture, severity/output contract, holistic rules, angle selection, examples, and composition; keep the baseline/angle distinction unmistakable; remove historical bolt-on seams without shrinking coverage.

- [ ] Record the immediate readability-control word count and a section-level meaning inventory.
- [ ] Draft the smallest coherent reorganization and show the diff before applying it.
- [ ] Apply the approved draft and run the complete active suite plus affected composition scenarios 5/5 on Sol high.
- [ ] Blindly compare subjective review outputs with the immediate readability control where the rubric requires judgment.
- [ ] Run cold editorial and skill-writing review; address findings and restart affected scenarios.
- [ ] Show the skill in place, run repository tests, and commit as `docs(skills): clean up adversarial review`.

### Task 23: Clean `adversarial-review-loop`

**Files:** `skills/adversarial-review-loop/SKILL.md`, `skill-validation/adversarial-review-loop.md`, `skill-validation/adversarial-review-loop-scenarios.md`

**Review focus:** make scope/precedence, normal loop, class/root attack, three-cycle cap, cold escape, and clean stop read as one state machine; preserve per-task versus whole-branch ownership.

- [ ] Record the immediate readability-control word count and a state/transition meaning inventory.
- [ ] Draft the smallest coherent reorganization and show the diff before applying it.
- [ ] Apply the approved draft and run every active loop branch plus affected composition scenarios 5/5 on Sol high.
- [ ] Blindly compare subjective remediation outputs with the immediate readability control where the rubric requires judgment.
- [ ] Run cold editorial and skill-writing review; address findings and restart affected scenarios.
- [ ] Show the skill in place, run repository tests, and commit as `docs(skills): clean up adversarial review loop`.

### Task 24: Clean `dispatching-development-subagents`

**Files:** `skills/dispatching-development-subagents/SKILL.md`, `skill-validation/dispatching-development-subagents.md`

**Review focus:** align Role/Overview/When-you-dispatch; state the scope contract once; keep orchestrator verification and subagent gate boundaries explicit; depend on the full development bundle without relying on an upstream report heading.

- [ ] Record the immediate readability-control word count and a section-level meaning inventory.
- [ ] Draft the smallest coherent reorganization and show the diff before applying it.
- [ ] Apply the approved draft and run the complete active suite plus affected composition scenarios 5/5 on Sol high.
- [ ] Blindly compare subjective dispatch outputs with the immediate readability control where the rubric requires judgment.
- [ ] Run cold editorial and skill-writing review; address findings and restart affected scenarios.
- [ ] Show the skill in place, run repository tests, and commit as `docs(skills): clean up development subagent dispatch`.

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
- [ ] Draft and show the parent diff plus every proposed companion and routing-reference diff before applying them.
- [ ] Apply the approved parent draft and any required routing-reference updates.
- [ ] Run the complete parent suite and every affected composition scenario 5/5 on Sol high.
- [ ] For every companion `SKILL.md` changed in this task, rerun that companion's complete active suite 5/5 and its cold skill-writing review.
- [ ] Rerun the routing-reference sweep; show and apply any newly required edit, then restart every affected scenario.
- [ ] Blindly compare subjective orchestration outputs with the immediate readability control where the rubric requires judgment.
- [ ] Run cold editorial, skill-writing, consistency, and executability review; address findings and restart affected scenarios.
- [ ] Show the parent and any changed companion skills in place, run repository tests, and commit as `docs(skills): clean up disciplined development`.

### Task 26: Run the final Sol-high composition gate

**Files:**

- Modify: `skill-validation/README.md`
- Modify: `skill-validation/skill-discovery.md`
- Modify: all nine per-skill validation records
- Create: `skill-validation/skill-composition.md`

**Required final scenarios:** the shared all-nine description-discovery suite; each portable skill extracted with declared Superpowers dependencies and a non-software task; direct invocation of each integrated skill with the full bundle; parent routing across plan, implementation, debugging, review, documentation, and delegation modes; per-task versus whole-branch review ownership.

**Produces:** A cross-suite composition record that links the owning scenario IDs and records joint results without duplicating their prompts or rubrics.

- [ ] Rerun the shared discovery suite and run every other scenario atomically unless composition is the behavior under test; run each scenario five times on Sol high.
- [ ] Manually score each protected promise and record any infrastructure failures separately.
- [ ] If any result is below 5/5, stop and classify it through the design's failure gate; correct a cleanup regression in its owning task, and isolate any approved behavioral change in a separate RED/GREEN slice.
- [ ] Record the final 5/5 results and commit as `docs(validation): record final skill composition greens`.

### Task 27: Run the cleaned Sol-low comparison and final repository verification

**Files:**

- Modify: `skill-validation/README.md`
- Modify: `skill-validation/skill-discovery.md`
- Modify: `skill-validation/skill-composition.md`
- Modify: all per-skill validation records with final Sol-low scores
- Modify: `plans/2026-08-01-comprehensive-skill-cleanup.md`

- [ ] Freeze the final active scenario suite and run every scenario five times on `gpt-5.6-sol` at low reasoning effort.
- [ ] Compare control and cleaned scores by scenario; pause for user review on any decrease.
- [ ] Record final word-count deltas for all nine skills.
- [ ] Run the hook, installer, and research pytest suites plus `git diff --check`.
- [ ] Run a final cold consistency review against the design and this plan.
- [ ] Mark the plan complete only when every success criterion in the design has evidence.
- [ ] Commit as `docs(skills): complete comprehensive cleanup validation`.
