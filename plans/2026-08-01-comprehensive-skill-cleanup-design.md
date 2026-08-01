# Comprehensive skill cleanup — design

## Status

Design decisions approved on 2026-08-01; awaiting written-spec review before implementation planning.

## Objective

Review all nine skills from top to bottom and make them compact, coherent, and easy for a human to read without weakening their established agent behavior.
Audit and normalize the validation framework before changing skill prose so the current suite becomes a trustworthy behavioral control.

## Non-goals

- Do not redesign effective doctrine during the readability cleanup.
- Do not treat fewer words as success when tested behavior regresses.
- Do not force every skill into an identical heading template.
- Do not require the integrated development skills to work when extracted individually.
- Do not run the full suite across Claude models during this project; that cross-provider calibration is a later user-led pass.

## Skill categories

All nine skills travel together in this repository and must be safe to invoke directly when the complete bundle is installed.

Five skills are also **portable**: they must retain their core value when extracted without the rest of this repository and used outside a software-development project.
Software examples may remain because development is their primary current use, but the core contract must not depend on a development environment.

- `concise-writing`
- `disciplined-research`
- `lean-plan-writing`
- `sweeping-stale-references`
- `writing-explicit-rationale`

Four skills form the **integrated development group**:

- `disciplined-development`
- `adversarial-review`
- `adversarial-review-loop`
- `dispatching-development-subagents`

The group coordinates tightly but is not a separately installable mini-bundle.
Direct-invocation tests for these skills run with all nine project skills available.
`disciplined-development` is the orchestrator and intentionally depends on its children.

## Preservation rule

The cleanup is behavior-preserving refactoring.
Readability, organization, consistency, and concision may change; established doctrine may not change accidentally.

Pin the current skill tree at commit `4296647` as the behavioral control.
Do not edit a skill until its current promises, coverage, and observed variance are understood.
Compare cleaned drafts against the pinned control with identical prompts and rubrics.

Handle desired behavioral improvements as separate RED/GREEN changes after the preservation cleanup unless a baseline failure makes safe cleanup impossible.

## Validation environment

The primary authoring and validation configuration is `gpt-5.6-sol` at high reasoning effort.
All primary scenarios must reach 5/5 on that configuration.
One repetition standard is easier to audit than a complexity-dependent rule, and five fresh contexts expose variance that three can miss.

After the complete Sol-high baseline is established, run the same suite on `gpt-5.6-sol` at low reasoning effort and record comparative scores.
Low-effort results characterize robustness; they do not replace or dilute the high-effort 5/5 gate.

Record for every run:

- skill-tree commit or content hash;
- exact prompt and fixture;
- model and reasoning effort;
- Superpowers version;
- sibling skills made available;
- run date;
- private scoring rubric;
- manually scored outcome.

Later Claude model and effort testing is outside this cleanup's completion gate.

## Validation protocol

Create one compact shared protocol for universal rules.
Keep each skill's current scenario catalog near the top of its existing `skill-validation/<skill>.md` record and retain historical evidence below it.
Do not rewrite genuine history or commit raw subagent transcripts.

Every scenario uses:

- five independent fresh contexts;
- an exact evaluator prompt with no answer key or scoring criteria;
- manual inspection of every response;
- a private rubric with observable pass criteria;
- five passes, with no averaging or discarded runs.

If wording changes after a failed run, restart the affected scenario at zero.
Record the missed criterion and relevant rationalization for failures.

Use atomic scenarios for individual skill promises.
Use composite prompts only when composition is the behavior under test; never combine unrelated tasks to reduce dispatch count.
This avoids artificial conflicts between unrelated output contracts.

Blind the arm labels when scoring subjective prose quality.
Score behavioral preservation before comparing readability.

## Minimum coverage

Every skill needs:

- a simple discovery test using descriptions rather than skill bodies;
- a simple application test;
- a non-trivial application test with competing constraints, pressure, or edge conditions;
- a safe direct-invocation test;
- every still-relevant focused regression already protecting a specific rule.

The portable five also need extraction tests with only the skill and its declared external dependencies available.
The integrated development group needs cross-skill ownership and composition tests.
`disciplined-development` needs full-suite orchestration tests.

Add scenarios for each meaningful branch, boundary, output contract, and demonstrated failure mode.
Complex skills may therefore have substantially larger suites than narrow skills.

## Framework audit

Map every existing scenario to the promise it protects and classify it:

- **Keep:** strong, current, and replayable.
- **Repair:** useful but contaminated, ambiguous, incompletely recorded, or below the 5/5 repetition standard.
- **Merge:** duplicates another scenario's protected behavior.
- **Retire:** obsolete or tests wording rather than behavior.
- **Add:** a current promise has no adequate scenario.

Preserve retired or superseded evidence as history while removing it from the active suite.
Each active scenario must identify the promises and skill sections it protects so later edits can select reruns by impact.

## Baseline failure handling

A current scenario that does not reach 5/5 is not silently accepted and is not automatically a skill defect.
Classify the result before cleanup:

1. The scenario or rubric is flawed: repair it and restart the baseline.
2. The skill is genuinely inconsistent: pause and obtain user approval for a separate behavioral RED/GREEN change.
3. The behavior is inherently variable: make the variance and acceptable contract explicit, then redesign the scenario around observable requirements.

Do not hide a 4/5 result, average it into a pass, or preserve a current failure as desired behavior by default.

## Skill review rubric

### Readability

- State the purpose immediately and progress in a natural order from trigger to rule, procedure, output, and mistakes.
- Keep related guidance together and use stable terminology.
- Integrate, relocate, or remove bolt-on sections.
- Use one sentence per line with the repository's structural exceptions.
- Retain tables when they improve scanning or resist agent rationalization.
- Use examples only when they demonstrate distinct behavior.

### Effectiveness

- Make every imperative observable and actionable.
- Key conditional behavior to explicit predicates.
- Give required outputs a clear shape.
- Cover important boundaries and failure modes.
- Do not rely on implication, accidental section order, or examples alone.
- Preserve the complete 5/5 baseline.

### Prose economy

- Use the fewest words that preserve information, necessary framing, and tested behavior.
- Prefer one strong statement over a rule followed by a paraphrase.
- Keep explanations that prevent demonstrated misunderstanding.
- Prefer tables for repeated mappings and short procedures for sequential work.
- Remove throat-clearing, meta-commentary, accidental repetition, and obvious transitions.
- Cross-reference the owning skill instead of duplicating its procedure.
- Treat word count as a diagnostic, not a target.

### Direct invocation and portability

- Route correctly from the description.
- State ownership and dependencies explicitly.
- Remain safe to invoke directly with the complete bundle installed.
- For the portable five, keep the core workflow free of repository, hook, sibling-skill, and software-development requirements.
- Present suite integration as optional composition in portable skills.

### Suite integration

- Keep ownership boundaries explicit and non-overlapping.
- Make cross-references agree in both directions.
- Keep review cadence, remediation, dispatch, and orchestration responsibilities consistent.
- Let `disciplined-development` route to children without duplicating their detailed procedures.
- Give children enough contract for reliable orchestration.

## Cleanup workflow

1. Audit the validation framework and publish the shared protocol plus active scenario catalogs.
2. Establish the complete Sol-high control baseline for all nine skills.
3. Run the same baseline suite on Sol low and record comparative scores.
4. Clean one portable skill at a time, rerunning its complete active suite against the draft.
5. Clean `adversarial-review`, `adversarial-review-loop`, and `dispatching-development-subagents`, preserving their coordinated contracts and safe direct invocation.
6. Clean `disciplined-development` last against the settled child contracts.
7. Run final direct-invocation, portable-extraction, and whole-suite composition matrices.
8. Run the repository's automated hook, installer, and research suites.

The parent comes last because its routing can only be reconciled cleanly after every child contract is settled.

For each skill cleanup:

1. Show the draft to the user.
2. Run the complete impacted 5/5 regression set.
3. Run a cold editorial and skill-writing review.
4. Show the edited skill in place for human readability review.
5. Commit only after behavioral preservation and user approval.

Whole-skill cleanup reruns the skill's complete active suite.
Narrow later edits may use the scenario-to-promise map to select impacted tests.
Shared ownership changes rerun both sides plus their composition scenarios.
Parent orchestration changes rerun the parent suite and affected child-composition scenarios.

## Success criteria

- Every active scenario has an exact prompt, private rubric, environment record, and 5/5 Sol-high baseline.
- The complete baseline has comparative Sol-low scores.
- The portable five pass extraction tests without project siblings.
- All nine skills are safe to invoke directly with the complete bundle installed.
- Cleaned skills preserve their control behavior at 5/5.
- Human and cold editorial review find each skill coherent, compact, and easy to read.
- `disciplined-development` consistently routes the settled child contracts without duplicating them.
- Validation records are replayable without becoming narrative or transcript archives.
- Repository automated tests remain green.
