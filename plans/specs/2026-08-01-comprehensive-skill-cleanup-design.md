# Comprehensive skill cleanup — design

## Status

Design decisions approved; execution controls amended through follow-up review on 2026-08-04.

## Objective

Review all nine skills from top to bottom and make them compact, coherent, and easy for a human to read without weakening their established agent behavior.
Audit and normalize the validation framework before readability edits so the current
suite becomes a trustworthy regression baseline. If that audit exposes a genuine
skill inconsistency, an isolated user-approved pre-freeze RED/GREEN slice may proceed
after enforceable evaluator isolation exists; its repaired scenarios restart at zero,
and the slice remains separate from later readability work.

## Non-goals

- Do not redesign effective doctrine during the readability cleanup.
- Do not treat fewer words as success when tested behavior regresses.
- Do not force every skill into an identical heading template.
- Do not require development skills to work outside their authored domain or without declared dependencies.
- Do not add a second behavioral provider gate; Gate 5 remains the separate external-review boundary.

## Skill categories

All nine skills travel together in this repository and must be safe to invoke
directly when the complete bundle is installed.

Portability means that a skill authored and previously exercised with Claude reads and
behaves correctly to a cold non-Claude model within its intended task domain and with
its declared dependencies available.
All nine skills use five fresh `gpt-5.6-sol` high-effort contexts and the existing
failure-classification gate for that evidence.
Sol-low measures effort robustness, not an additional portability domain or model
family.
Domain breadth and standalone/extraction packaging are separate coverage dimensions;
neither defines cross-model portability.

Three **broad-domain companions** have contracts that genuinely include non-software
work and therefore retain isolated broad-domain application coverage:

- `concise-writing`
- `disciplined-research`
- `writing-explicit-rationale`

Two **development companions** retain their authored software-development domain and
declared dependencies:

- `lean-plan-writing`
- `sweeping-stale-references`

Four skills form the **integrated development group**:

- `disciplined-development`
- `adversarial-review`
- `adversarial-review-loop`
- `dispatching-development-subagents`

The group coordinates tightly but is not a separately installable mini-bundle.
Direct-invocation tests for these skills run with all nine project skills available.
`disciplined-development` is the orchestrator and intentionally depends on all eight companions.
The other three integrated-development skills are its tightly coupled children; the
five companions also participate at their routed boundaries.

## Preservation rule

The cleanup is behavior-preserving refactoring.
Readability, organization, consistency, and concision may change; established doctrine may not change accidentally.

Pin the current skill tree at commit `4296647` as the regression control for original behavior.
Do not edit a skill until its current promises, coverage, and observed variance are understood.
Compare cleaned drafts against the applicable immediate readability control with identical prompts and rubrics while continuing to protect original behavior against `4296647`.

Handle desired behavioral improvements as separate RED/GREEN slices, never inside a behavior-preserving readability commit.
Complete prerequisite behavior repairs before readability cleanup and defer unrelated improvements until afterward.
During Task 1, discovery audit exposed inconsistent parent co-selection. The user
approved the minimal frontmatter-only parent-routing target as the pre-freeze exception
above; it requires a watched control RED, 5/5 Sol-high target, cold review, final
in-place approval, repository tests, and its own behavioral commit after the Task 1
protocol commit.

During Task 2, the authoring-boundary audit exposed inconsistent exclusion of
`concise-writing` during skill and reference authoring. On 2026-08-02 the user
approved a separate pre-freeze RED/GREEN slice: remove the frontmatter exclusion and
state in the body that `superpowers:writing-skills` owns authoring decisions and
validation. After its watched controls, 5/5 GREEN, cold review, final in-place
approval, repository tests, and separate behavioral commit, that committed GREEN
becomes `concise-writing`'s immediate readability control.

During Task 7, the audit exposed that internal enumeration was not observable in
review output and the owner approved shared-pattern synthesis as an adjacent output
feature. On 2026-08-04 the user approved a separate pre-freeze RED/GREEN slice for
member-by-member named accounting, one evidence-backed `DD-PATTERN` line, and its
`NONE` branch. The owner also approved folding effectiveness into the existing
necessity section and resolving the base-review response-template precedence as
clarifications with preserved 5/5 behavior. These changes require watched controls,
5/5 GREEN, cold review, final in-place approval, repository tests, and a behavioral
commit separate from Task 22's readability cleanup.

During Task 18, review of `disciplined-research` exposed that its load-bearing and
destination tests left factual claims outside the grounding contract. On 2026-08-09
the owner approved a separate RED/GREEN behavior slice with the exact discovery
description `Use before stating any factual claim.` The body must apply one rule to
every factual claim, including claims in casual answers and private notes: acquire
the fact from the best available source, verify it before stating it, and disclose
the source. It must not retain a load-bearing threshold, a destination test, a
scratch-work exemption, or another exclusion. Project, external, and cross-domain
distinctions remain useful only for choosing and ranking sources; they do not bound
when the skill applies. A single source may support multiple claims when the mapping
is unambiguous. If no acceptable source supports a claim, do not state the claim as
fact or attach a source that lacks the claimed datum. Absent, unreadable, malformed,
datum-missing, conflicting, and large source sets do not create an exception: apply
the same source-ranking, verification, and disclosure rule to every emitted factual
claim, without sampling.

This behavior slice adds three watched target scenarios. `DISC-11` requires
`disciplined-research` selection before an agent records a factual claim in a private
software-development scratch note. `DR-04` requires the private note to acquire,
verify, and disclose support for every factual claim. `DR-05` exercises a casual
answer when an available source lacks the requested datum: the answer must not
assert the unsupported claim or falsely cite the incomplete source. Existing
`DR-01`–`DR-03` retain source ranking, conflicting-authority, multi-source mapping,
and unsupported-claim guards. Before drafting, reclassify every `DISC-01`–`DISC-10`
allowed set against the exact new description; do not presume the old routing
contracts remain valid. Freeze and backfill any repaired discovery contract plus the
three new targets before skill edits.

The live README, architecture summary, parent Principle 6, and
`sweeping-stale-references` ownership boundary must stop presenting research as
load-bearing-only. Any dependent skill-prose change follows the same
complete-draft and final in-place approval gates and reruns the parent's complete
active suite. The sweeping repair therefore adds its complete active suite:
`DISC-08`, `SSR-01`–`SSR-03`, and `SSR-05`. Before drafting that change,
reclassify `DD-01`, `DD-02`, `DD-03`,
`DSD-01`, `DSD-02`, `OWN`, and `WER-07` against universal grounding, repair and
backfill each changed contract at Sol high and low, and classify new positive
routing as target behavior. Require the combined candidate to reach 5/5 on the complete affected
discovery, disciplined-research, disciplined-development, and sweeping-stale-references suites. Show complete proposed versions of all three changed skills and obtain approval before applying them; after review, show all three complete final skills in place and obtain final approval. After watched
REDs, candidate GREEN, cold review, staged adversarial review, final in-place
approval, and repository verification, commit the behavior slice separately. That
commit becomes Task 18's immediate readability control, and the active closure
becomes 85 scenarios or 425 five-repetition slots only after all Task 18A routing
and application targets are GREEN. The pre-draft discovery reclassification determines the final
preservation/target split; a new positive-routing promise is target behavior, not a
preservation requirement retroactively imposed on the old description.

The 2026-08-09 pre-draft sweep classified research as required for every
`DISC-01`–`DISC-11` request and for `DD-01`–`DD-03`, `DSD-01`, `DSD-02`, `OWN`,
and `WER-07`. Each complete output states factual claims, including preserved claims
in stylistic transformations, plan premises and decisions, review/routing findings,
dispatch scope, workflow ownership, and private scratch notes. Classification does
not depend on destination or on whether the user first supplied the claim.
The sweep also found the live `sweeping-stale-references` ownership boundary's
“load-bearing fact” narrowing. Its tracked bytes remain unchanged during this
freeze, and its complete active suite plus proposed/final approval gates are now in
scope. Owning validation records freeze exact repaired
contracts and base-control hashes; fresh high/low controls and prose work remain
pending.

Broad-domain isolation is coverage only for the three companions whose contracts
include that work; it does not expand the two development companions beyond their
authored domain or remove any dependency.
`CW-08`, `DR-02`, and `WER-03` supply that isolated-application evidence.
`LP-04` and `SSR-04` remain preserved as historical exploratory cross-domain evidence,
but they are retired from active coverage and cannot drive a skill change.
The current `writing-explicit-rationale` policy scope is approved current behavior.
`4296647` remains the original-behavior control unless an independently approved
behavior slice establishes a later immediate readability control.

## Validation environment

The primary authoring and validation configuration is `gpt-5.6-sol` at high reasoning effort.
All active scenarios must reach 5/5 on that configuration.
One repetition standard is easier to audit than a complexity-dependent rule, and five fresh contexts expose variance that three can miss.

The orchestrator owns every validation-bearing task, evaluator dispatch, scoring workflow, result inspection, human approval gate, and commit.
It may dispatch read-only evaluator or reviewer subagents directly, but it must not delegate a validation-bearing task to a development subagent that would need to dispatch its own evaluators.
Each evaluator starts without inherited conversation history and receives an explicit model, reasoning effort, skill bundle, and task context.
Task 1 must select and probe an enforceable no-write evaluator transport; an instruction to remain read-only is insufficient, and unavailable enforcement blocks validation.

Response generation and scoring use separate fresh contexts for subjective comparisons.
The read-only scorer receives the evaluator-withheld rubric and outputs under opaque arm IDs but never receives the control/draft mapping.
Freeze the scoring record before mapping those IDs back to control and draft for result recording.

After the complete Sol-high baseline results are recorded, run every frozen preservation and target scenario against the control tree on `gpt-5.6-sol` at low reasoning effort and record comparative scores.
Low-effort results characterize robustness; they do not replace or dilute the high-effort 5/5 gate.
Run the complete suite on Sol low again after cleanup to compare the control and cleaned skill trees.
A lower cleaned score pauses sign-off for inspection and user review but is not an automatic failure of the Sol-high preservation gate.
Record one of two dispositions for every decrease: user-approved acceptance with an on-page what/why/accepted rationale, or remediation followed by the affected Sol-high and Sol-low reruns.
Task 11's frozen 81-scenario/405-slot aggregate remains historical fact.
After retiring `LP-04` and `SSR-04`, that closure contained 79 scenarios; Task 17
added three active scenarios for a current total of 82. The approved Task 18
behavior slice will add three more after they are GREEN, producing the 85-scenario
closure used by Tasks 26–27. Do not recompute the frozen aggregate.

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

Gate 5 external reviews use the shared protocol's different-provider and
different-model-family rule.
When Claude orchestrates, a scratch `DD_CONFIG` project override pins
`gpt-5.6-sol` at high effort; when Codex orchestrates, a fresh Claude reviewer uses
the plan-recorded model and effort.
This keeps experiment-specific settings out of the public default while requiring
recorded provider, model, effort, and verdict metadata at every cleanup boundary.

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

A skill's **complete active suite** contains its owned scenarios plus every shared
discovery, direct-invocation, domain-appropriate application, dependency, and
composition scenario mapped to one of its promises.
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

The three broad-domain companions also need isolated non-software application tests
with their declared dependencies available.
The two development companions need in-domain application tests with their declared
dependencies available.
The integrated development group needs cross-skill ownership and composition tests.
`disciplined-development` needs full-suite orchestration tests.

Existing behavior is covered by **preservation scenarios**, which require a 5/5 control baseline.
Newly approved behavior is covered by a **target scenario**, which requires a watched
control RED and a 5/5 GREEN before joining the active regression suite.

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
- Preserve each skill's intended domain and declared dependencies.
- Keep the broad-domain companions usable in their genuine non-software domains.
- Keep development companions and the integrated group grounded in software work.

### Suite integration

- Keep ownership boundaries explicit and non-overlapping.
- Make cross-references agree in both directions.
- Keep review cadence, remediation, dispatch, and orchestration responsibilities consistent.
- Let `disciplined-development` route to children without duplicating their detailed procedures.
- Give children enough contract for reliable orchestration.

## Cleanup workflow

1. Audit the validation framework and add the shared protocol plus active scenario catalogs; resolve only genuine inconsistencies through the isolated, user-approved pre-freeze RED/GREEN exceptions above.
2. Establish complete Sol-high baseline results for all nine skills: 5/5 for preservation scenarios and watched REDs for approved target scenarios.
3. Run every frozen preservation and target scenario against the control tree on Sol low and record comparative scores.
4. Clean the three broad-domain companions and two development companions one at a time against their domain-appropriate active suites.
5. Clean `adversarial-review`, `adversarial-review-loop`, and `dispatching-development-subagents` one at a time, rerunning affected composition scenarios and preserving safe direct invocation.
6. Clean `disciplined-development` last against the settled child contracts.
7. Run final cold Sol-high direct invocation of all nine skills in their intended domains with declared dependencies, plus whole-suite composition scenarios.
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
- Every evaluator uses a probed no-write transport, and every subjective score is frozen before its opaque arm mapping is revealed.
- Every preservation scenario has a 5/5 Sol-high control baseline.
- Every approved target scenario has a watched control RED and a 5/5 Sol-high GREEN before joining the active regression suite.
- The control and cleaned skill trees have comparative Sol-low scores.
- Every skill passes cold Sol-high coverage in its intended domain with declared dependencies.
- The three broad-domain companions retain isolated non-software application coverage.
- `LP-04` and `SSR-04` remain preserved historical evidence outside the active suite.
- All nine skills are safe to invoke directly with the complete bundle installed.
- Cleaned skills preserve their control behavior at 5/5 on Sol high.
- Human and cold editorial review find each skill coherent, compact, and easy to read.
- `disciplined-development` consistently routes the settled child contracts without duplicating them.
- Validation records are replayable without becoming narrative or transcript archives.
- Repository automated tests remain green.
- Every PR boundary passes the orchestrator-owned Gate 5 review and smoke pass, with its different-provider/model-family metadata and verdict logged under the shared protocol.
- Every lower cleaned Sol-low score has a recorded user-approved disposition and any required reruns.
- The completed plan and design are archived under `plans/completed/` and `plans/completed/specs/`.
