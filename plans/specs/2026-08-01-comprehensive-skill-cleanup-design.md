# Comprehensive skill cleanup — design

## Status

Design decisions approved; execution controls amended after final review on 2026-08-01.

## Objective

Review all nine skills from top to bottom and make them compact, coherent, and easy for a human to read without weakening their established agent behavior.
Audit and normalize the validation framework before changing skill prose so the current suite becomes a trustworthy regression baseline.

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
`disciplined-development` is the orchestrator and intentionally depends on all eight companions.
The other three integrated-development skills are its tightly coupled children; the five portable skills also participate as routed companions.

## Preservation rule

The cleanup is behavior-preserving refactoring.
Readability, organization, consistency, and concision may change; established doctrine may not change accidentally.

Pin the current skill tree at commit `4296647` as the regression control for original behavior.
Do not edit a skill until its current promises, coverage, and observed variance are understood.
Compare cleaned drafts against the applicable immediate readability control with identical prompts and rubrics while continuing to protect original behavior against `4296647`.

Handle desired behavioral improvements as separate RED/GREEN slices, never inside a behavior-preserving readability commit.
Complete prerequisite improvements such as portability before readability cleanup and defer unrelated improvements until afterward.

Portable extraction is an approved target, not assumed control behavior.
If a portable skill fails extraction, record the watched RED, make the minimal portability change in a separate behavioral slice, establish its 5/5 GREEN, and only then perform readability cleanup.
The portability slice must preserve the skill's software-development behavior.
After a portability slice reaches GREEN, that committed version becomes the immediate control for the skill's readability cleanup; `4296647` remains the regression control for original behavior.
For skills that need no portability slice, `4296647` is also the immediate readability control.

## Validation environment

The primary authoring and validation configuration is `gpt-5.6-sol` at high reasoning effort.
All active scenarios must reach 5/5 on that configuration.
One repetition standard is easier to audit than a complexity-dependent rule, and five fresh contexts expose variance that three can miss.

The orchestrator owns every validation-bearing task, evaluator dispatch, result inspection, human approval gate, and commit.
It may dispatch read-only evaluator or reviewer subagents directly, but it must not delegate a validation-bearing task to a development subagent that would need to dispatch its own evaluators.
Each evaluator starts without inherited conversation history and receives an explicit model, reasoning effort, skill bundle, and task context.

After the complete Sol-high baseline results are recorded, run every frozen preservation and target scenario against the control tree on `gpt-5.6-sol` at low reasoning effort and record comparative scores.
Low-effort results characterize robustness; they do not replace or dilute the high-effort 5/5 gate.
Run the complete suite on Sol low again after cleanup to compare the control and cleaned skill trees.
A lower cleaned score pauses sign-off for inspection and user review but is not an automatic failure of the Sol-high preservation gate.

Record for every run:

- skill-tree commit or content hash;
- exact prompt and fixture;
- model and reasoning effort;
- Superpowers version;
- sibling skills made available;
- run date;
- scoring rubric withheld from evaluator prompts and contexts;
- manually scored outcome.

Later Claude model and effort testing is outside this cleanup's completion gate.

## Control materialization

Materialize each regression or immediate readability control as an immutable scratch bundle outside the repository before comparing it with a draft.
Identify the bundle by commit plus content hash, include every sibling or declared dependency the scenario supplies, and never read control material from the mutable working tree.
Verify before Task 1's baseline runs that the nine live skill files still match `4296647`.

The scenario prompt, fixture, rubric, supplied context, model, and reasoning effort must be identical between comparison arms except for the skill bundle intentionally under test.
For subjective comparisons, anonymize immutable control and draft outputs before scoring.

## Validation protocol

Create one compact shared protocol for universal rules.
Keep each skill's current scenario catalog near the top of its existing `skill-validation/<skill>.md` record and retain historical evidence below it.
Do not rewrite genuine history or commit raw subagent transcripts.

Every scenario uses:

- five independent fresh contexts;
- read-only, bounded evaluators with no nested dispatch;
- an exact evaluator prompt with no answer key or scoring criteria;
- only the skill material and task context named by the scenario;
- manual inspection of every response;
- an evaluator-withheld rubric with observable pass criteria;
- five passes, with no averaging or discarded runs.

If wording changes after a failed run, restart the affected scenario at zero.
Record the missed criterion and relevant rationalization for failures.
A completed response that misses the rubric is a failure and cannot be discarded.
An infrastructure error that produces no evaluable response is recorded separately and retried; it is not counted as a behavioral pass or failure.
After three consecutive infrastructure errors for one scenario and configuration, pause the run and surface the blocker rather than retrying indefinitely.

Use atomic scenarios for individual skill promises.
Use composite prompts only when composition is the behavior under test; never combine unrelated tasks to reduce dispatch count.
This avoids artificial conflicts between unrelated output contracts.

A skill's **complete active suite** contains its owned scenarios plus every shared discovery, direct-invocation, portability, and composition scenario mapped to one of its promises.
Every shared or supporting scenario record has one owner and lists every affected skill.

Blind the arm labels when scoring subjective prose quality.
Score behavioral preservation before comparing readability.
Because raw baseline transcripts are not committed, rerun fresh immediate-readability-control and draft arms for each subjective comparison, anonymize their labels, and keep the temporary outputs outside the repository until their scored summary is recorded.

## Minimum coverage

Every skill needs:

- a simple discovery test using all nine descriptions rather than skill bodies;
- a simple application test;
- a non-trivial application test with competing constraints, pressure, or edge conditions;
- a safe direct-invocation test;
- every still-relevant focused regression already protecting a specific rule.

A scenario may satisfy multiple related coverage categories when its rubric names each promise explicitly.
Do not create near-duplicate prompts merely to give every category a separate row.

The portable five also need extraction tests with only the skill and its declared external dependencies available, including at least one non-software application.
The integrated development group needs cross-skill ownership and composition tests.
`disciplined-development` needs full-suite orchestration tests.

Existing behavior is covered by **preservation scenarios**, which require a 5/5 control baseline.
Newly approved behavior such as a missing portability contract is covered by a **target scenario**, which requires a watched control RED and a 5/5 GREEN before joining the active regression suite.
If an approved portability scenario is already 5/5 against `4296647`, classify it as preservation coverage rather than a target.

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
Audit the project-level evaluator-isolation scenario with the framework and either repair it to the common protocol or retire it from the active suite explicitly.

After the Sol-low control freeze, any change to a scenario's prompt, fixture, rubric, supplied context, or protected promise invalidates its comparative baseline.
Before using the changed scenario, rerun its Sol-high and Sol-low control arms and update every owning and shared record.
New target scenarios additionally require their watched control RED before the GREEN arm.

## Baseline failure handling

A current scenario that does not reach 5/5 is not silently accepted and is not automatically a skill defect.
Classify the result before cleanup:

1. The scenario or rubric is flawed: repair it and restart the control baseline.
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
- Preserve every established control behavior at 5/5.

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

1. Audit the validation framework and add the shared protocol plus active scenario catalogs.
2. Establish complete Sol-high baseline results for all nine skills: 5/5 for preservation scenarios and watched REDs for approved target scenarios.
3. Run every frozen preservation and target scenario against the control tree on Sol low and record comparative scores.
4. Process one portable skill at a time: close any approved portability RED in its own behavioral slice, then perform readability cleanup against the expanded active suite.
5. Clean `adversarial-review`, `adversarial-review-loop`, and `dispatching-development-subagents` one at a time, rerunning affected composition scenarios and preserving safe direct invocation.
6. Clean `disciplined-development` last against the settled child contracts.
7. Run final Sol-high direct invocation of all nine skills with the complete bundle, portable extraction of the five, and whole-suite composition scenarios.
8. Run the complete cleaned suite on Sol low and compare it with the control scores.
9. Run the repository's automated hook, installer, and research suites.

The parent comes last because its routing can only be reconciled cleanly after every child contract is settled.

For each skill cleanup:

1. Show the draft to the user and wait for approval before applying it.
2. Run the skill's complete active suite at 5/5 on Sol high.
3. Run a cold editorial and skill-writing review.
4. Show the edited skill in place and wait for final user approval.
5. Run the repository's automated hook, installer, and research suites.
6. Commit only after behavioral preservation, repository verification, and user approval.

Any skill edit after final approval returns to the draft, validation, in-place review, and approval sequence before commit.

Whole-skill cleanup reruns the skill's complete active suite.
Narrow later edits may use the scenario-to-promise map to select impacted tests.
Shared ownership changes rerun both sides plus their composition scenarios.
Parent orchestration changes rerun the parent suite and affected child-composition scenarios.

## Success criteria

- Every scenario has an exact prompt, evaluator-withheld rubric, and environment record.
- Every preservation scenario has a 5/5 Sol-high control baseline.
- Every approved target scenario has a watched control RED and a 5/5 Sol-high GREEN before joining the active regression suite.
- The control and cleaned skill trees have comparative Sol-low scores.
- The portable five pass extraction tests without project siblings.
- Any portability gap observed in the control is closed through a separate watched RED/GREEN slice before readability cleanup.
- All nine skills are safe to invoke directly with the complete bundle installed.
- Cleaned skills preserve their control behavior at 5/5 on Sol high.
- Human and cold editorial review find each skill coherent, compact, and easy to read.
- `disciplined-development` consistently routes the settled child contracts without duplicating them.
- Validation records are replayable without becoming narrative or transcript archives.
- Repository automated tests remain green.
- Every PR boundary passes the orchestrator-owned Gate 5 review and smoke pass.
- The completed plan and design are archived under `plans/completed/` and `plans/completed/specs/`.
