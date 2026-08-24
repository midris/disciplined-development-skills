# Comprehensive skill cleanup — design

> **Superseded for post-charter execution on 2026-08-22.** This document preserves
> the approved charter decision and earlier project history, but its Task 26–27
> implementation path must not be resumed. A replacement behavioral-validation
> design and plan require owner approval.

## Task 22 approved validation method (2026-08-15; activated 2026-08-16)

Task 22 separates semantic review attribution from deterministic enforcement of the authored output envelope over the same bytes.
The detailed method, source-set counts, execution status, invalidation conditions, and historical boundary live in [the owning adversarial-review record](../../skill-validation/adversarial-review.md#approved-task-22-validation-method-2026-08-15-activated-2026-08-16); no independent result is asserted here.

## Status

Design decisions approved; execution controls amended through follow-up review on 2026-08-04.

## Approved charter-first validation redesign (2026-08-21)

The owner approved replacing the final exhaustive-format validation design with a
charter-first behavioral design. Existing scenarios remain useful source material,
but their prompts, rubrics, and results are reclassified against the reason each
skill exists before they can enter the new acceptance denominator.

### Skill charters

| Skill | Core identity |
|---|---|
| `disciplined-development` | Prevent progress across development boundaries until the required evidence exists, while retaining parent gate authority. |
| `disciplined-research` | Prevent unsupported factual claims or premises from entering reasoning or work. |
| `writing-explicit-rationale` | Preserve decision-useful rationale in one durable, discoverable home without duplicating irrelevant history. |
| `concise-writing` | Remove prose that adds no value without changing how a careful reader understands or uses the artifact. |
| `lean-plan-writing` | Produce an executable behavioral contract without writing the implementation in the plan. |
| `sweeping-stale-references` | Find, disposition, and reconcile every mutable encoding of a changed fact before the change is accepted. |
| `dispatching-development-subagents` | Make delegated development changes safely integrable through bounded scope, retained parent authority, and returned-diff verification. |
| `adversarial-review` | Find evidenced material defects that ordinary review misses without inventing requirements or false shared causes. |
| `adversarial-review-loop` | Remediate findings by complete class or shared root, preserve counter ownership, and escape reactive churn at the cap. |

Each charter owns at most four indispensable observable invariants. A core scenario
must map every scored criterion to one of those invariants. A criterion that cannot
be mapped is task fidelity, readability, protocol, or historical diagnostic evidence;
it does not fail the skill's core behavior.

### Validation layers

1. **Core behavior — hard gate.** Use the smallest useful portfolio for each skill:
   a positive application, a realistic pressure or known-rationalization case, and
   an ownership or boundary case. `disciplined-development` may use focused gate
   cases plus one integrated invalidation/restart lifecycle because its charter is
   orchestration across distinct boundaries.
2. **Executed-work evidence — hard gate when action is claimed.** A read-only
   response proves action selection, not execution. When the protected promise is
   that the agent searched, edited, verified, committed, or otherwise changed real
   state, use a writable isolated micro-repository and independently inspect the
   resulting state. The agent's report is never the proof.
3. **Deterministic protocol — separate hard gate.** Exact rendering is a hard
   requirement only for a genuine authored or machine-consumed interface backed by
   a deterministic renderer, validator, or production consumer. Test semantic input
   separately from rendered bytes. User-supplied literals and external schemas remain
   exact data-integrity requirements, not skill-output formatting requirements.
4. **Readability and processing — separate quality gate.** A cold reader must be
   able to identify the skill's purpose, trigger, indispensable invariants, next
   action, and ownership boundary. Blind comparison may identify a material loss;
   word count, headings, placement, and preferred wording are otherwise diagnostic.

The existing `adversarial-review` renderer/checker and the production terminal
`DD-VERDICT` parser remain deterministic protocols. No other exact response shape is
presumed to be a core contract. If another exact output is required, add its
deterministic production or validation path before making exactness release-blocking.

### Controls and model schedule

Compare two independently frozen arms with identical rebuilt scenarios:

- original skill forms from local branch `main` at
  `5219997ff580f7cfac4115e4c38d396d3dd9101e`;
- current skill forms from this worktree, freezing every supplied byte before each
  campaign and recording the worktree skill hashes separately from tracked `HEAD`.

Use `gpt-5.6-sol` at high reasoning effort for validation architecture, rubric
judgment, evidence reconciliation, and final decisions. Lower-cost agents may perform
bounded mechanical fixture, harness, inventory, and audit work, but the orchestrator
retains integration and final scoring.

During rebuild, run each behavioral scenario three times at Sol low. If the three
responses split, expose rubric ambiguity, or show unstable task fidelity, expand that
round to five before changing a skill or accepting the scenario. Iterate on the test
contract quickly; do not treat low-effort variance as a portability failure.

After the core suite and its result processing are stable, run three fresh Sol-high
repetitions per core scenario for both frozen arms. This owner-approved three-run
stabilization gate supersedes Tasks 26–27's earlier five-repetition Sol-high closure
design. Every final core scenario must pass 3/3 for the current arm. Original-arm
results are a comparative baseline: an original pass/current failure is a regression;
an original failure/current pass is an improvement; shared failures require
classification as a skill gap or non-diagnostic test before any skill wording change.

### Result processing

Score the whole artifact against observable actions, outcomes, ordering, ownership,
blocked transitions, and truthful evidence. Record each miss in exactly one ledger:

- core behavior;
- deterministic protocol;
- task or fixture fidelity;
- readability;
- infrastructure.

Only core behavior and applicable deterministic protocol failures block skill
acceptance. A claimed action passes only when independent state establishes it.
Scorer verdicts remain advisory; the orchestrator reads the underlying artifacts and
owns final adjudication. No skill wording changes follow automatically from a failed
run: first prove the test is diagnostic, then present any proposed skill wording to
the owner for explicit approval.

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
description `Use before every response, interaction, action, or task that will state, repeat, transform, or rely on a factual claim or premise—including internal logical review of supplied text, claims and premises supplied by the user or embedded in requested work, plus mechanical edits, searches, and verification.` The body must apply one rule to
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
When useful, an unsupported technical possibility may be retained only as an explicitly unverified investigation lead, with an explicit disclosure that no source supports or establishes it.
An incomplete or unrelated artifact must not be attached as support for that lead.

This behavior slice adds two watched target scenarios. `DISC-11` requires
`disciplined-research` selection before an agent records a factual claim in a private
software-development scratch note. `DR-04` requires the private note to acquire,
verify, and disclose support for every factual claim. `DR-05` is preservation and exercises a casual
answer when an available source lacks the requested datum: the answer must not
assert the unsupported claim or falsely cite the incomplete source. Existing
`DR-01`–`DR-03` retain source ranking, conflicting-authority, multi-source mapping,
and unsupported-claim guards. Before drafting, reclassify every `DISC-01`–`DISC-10`
allowed set against the exact new description; do not presume the old routing
contracts remain valid. Freeze and backfill any repaired discovery contract plus the
two new targets plus the `DR-05` preservation cell before skill edits.
`DR-06` is the post-draft watched target for the unverified-lead branch: an incident handoff must report only the supported three HTTP 403 outcomes, name expired temporary credentials as the requested investigation lead, explicitly mark that lead unverified, disclose that no supplied source supports expiry, and avoid false source mapping.
After the candidate made `Unverified — no supporting source found:` literal, DR-06 criterion 4 and its footer were repaired to reject semantic equivalents for that stamp while preserving semantic-equivalent allowance elsewhere. Repaired-rubric control is accepted at high 0/5 and low 0/5. Candidate `a0497ff` failed at high 3/5 and low 1/5 with scorer-correct evidence; after the single approved pressure-row deletion, candidate `381a10aaa01b17e02d863287718c2e6cfde5c5ac587f42921146726a49725fc5` / bundle `cd87d897d6c3cf976f004c28b874dfec2c9f1064a9754a567160b64518a59477` is accepted at high 5/5 and low 1/5 with zero retries. Its accepted combined evaluator/scorer aggregate hashes are `c8d995ee00d4448259c5baf38afde721720b378a7d0f6fc6e35fd0cec0aba37c` / `8f86bd56c93736198120e9250c5412bc4d9d956944461acfdf4dddb0bdd4a51d`.
Freeze its exact prompt, producer-shaped fixture, rubric, current control bytes, and ignored candidate bytes before any run.
Its focused comparison uses two opaque arms at high and low effort with five repetitions per cell, followed by four contextful high-effort scorer processes; candidate bytes are hash-parameterized and fail closed on change.

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
discovery, disciplined-research, disciplined-development, dispatch, review-loop,
and sweeping-stale-references suites. Show complete proposed versions of all five
changed skills and obtain approval before applying them; after review, show all
five complete final skills in place and obtain final approval. After watched
REDs, candidate GREEN, cold review, staged adversarial review, final in-place
approval, and repository verification, commit the behavior slice separately. That
commit becomes Task 18's immediate readability control. The then-current closure
forecast was 86 scenarios / 430 slots; the 2026-08-13 atomic/composite redesign
below supersedes that forecast. The pre-draft discovery reclassification determines the final
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
scope. Owning validation records freeze exact repaired contracts and base-control
hashes; the required high/low controls and contextful scoring are complete, while
skill prose remains pending the explicit draft/approval gate.

The final role split is 17 target REDs (`DISC-01`, `DISC-02`, `DISC-03`,
`DISC-04`, `DISC-06`, `DISC-07`, `DISC-08`, `DISC-09`, `DISC-11`, `DR-04`,
`DD-01`, `DD-02`, `DD-03`, `DSD-01`, `DSD-02`, `OWN`, `WER-07`) and three
preservation cells (`DISC-05`, `DISC-10`, `DR-05`). Preservation requires 5/5
Sol-high; Sol-low is robustness evidence only. The eight semantically changed
contracts completed their post-freeze 80-slot rerun. `DISC-04` is target RED at
4/5 high and 3/5 low because its research route changed from optional to required;
`DISC-05` is preservation at 5/5 high and low. Contextful application scoring over
the five changed application contracts is complete at 10 processes/50 verdicts;
the other 12 accepted controls remain exact evidence.

On 2026-08-13 the owner approved expanding the test architecture before final
Task 18A closure. The changed-skill union is now 45 scenarios / 225 Sol-high slots:
12 discovery, seven research, nine parent, nine dispatch, one review-ownership, one
rationale-composition, and six stale-reference scenarios. Thirteen of those are new
single-seam tests (`DD-05`–`DD-09`, `DSD-06`–`DSD-11`, `SSR-06`–`SSR-07`);
the retained broad scenarios still exercise end-to-end composition. Acceptance is
per scenario and owner, never pooled. The earlier forecast of 86 repository-closure
scenarios is superseded and must be recomputed by Tasks 26–27 after this expanded
catalog lands.

Final-union scoring also enforces three fail-closed seams discovered in complete
artifacts: a dispatched subagent reports direct running-system verification as
passed, failed/blocking, or not exercisable before handing a parent gate back, and
a stale-reference search pairs every applicable old symbol/prose form with its
intended new symbol/prose form. The parent also makes every supplied applicable
source—including external sources—the first read at a session/phase/governing-
artifact boundary and at Gate 5 self-review. Focused fresh validation passed the
repaired paths before the final union restarted from zero. A later union exposed
one parent response that treated the requirements reread as sufficient to release
implementation planning. The final parent clarification keeps that transition
blocked until complete written scope and required sign-off; focused validation and
exact-hash cold review passed before the union restarted again from zero.

The accepted affected-rerun control root is
`/private/tmp/dd-task18a-control-postfreeze-f59608a`, with freeze SHA-256
`0119bdb403fdb89978ed6c2f34bae8de5db13c392071b97b06687d81f9be0210`
and plan SHA-256
`4de14a3e7531c8cf0e6258f82c9c8050b849ca9d0f0f8c1c633248dafcd81b4b`.
The other 12 unchanged/no-rerun scenarios retain accepted evidence from
`/private/tmp/dd-task18a-control-backfill-bd60966-escalated`, freeze SHA-256
`4671cfef15368088eaa554fdb67e5bea115d7a4a9a9610f7e07d16b160539b2d`,
plan SHA-256
`60b753fe17539876893f367763d59bbd53b7f584a9001217ffe07bbd607c2ce3`.
Final application adjudication is rooted at
`/private/tmp/dd-task18a-control-scoring-contextful-f59608a`, with freeze
`a72902e254706d2a13c9ff573bcffff6469271fdaf914f1b9e55db6a36fa0675`,
plan `cfb8e3f7949afc2b35407abd203fdd02767fdc1f698081f2fa952156f2f801bb`,
and aggregate `c801090c6252298da41954663dd3f671164cd77fceaa77abf71583fa43fa2f60`.
The five application scenarios scored 3/25 high and 5/25 low (8 PASS / 42 FAIL);
all selected attempts were a1 with zero retries/errors under Codex CLI 0.147.0,
read-only/no-agents transport. The earlier context-stripped aggregate
`289ef0fdae9f344a477994fce75c57aef361b745ee71e2acea4e9d2726d248db`
is transport-defective historical evidence only.

Broad-domain isolation is coverage only for the three companions whose contracts
include that work; it does not expand the two development companions beyond their
authored domain or remove any dependency.
`CW-08`, `DR-02`, and `WER-08` supply that isolated-application evidence.
Historical `WER-03` and `WER-DEV` remain generic artifact-rewriting diagnostics and
do not determine `writing-explicit-rationale` acceptance.
`LP-04` and `SSR-04` remain preserved as historical exploratory cross-domain evidence,
but they are retired from active coverage and cannot drive a skill change.
The current `writing-explicit-rationale` policy scope is approved current behavior.
`4296647` remains the original-behavior control unless an independently approved
behavior slice establishes a later immediate readability control.
For Task 21, the approved readability candidate and two later repair wordings were
rejected after behavior-first evaluation. The owner selected exact restoration of
the 372-word immediate control at `c54c4016`; exact-byte fresh control evidence is
the current comparison arm, while the failed candidate arms remain historical
evidence rather than grounds for a third wording experiment. Final restoration
review corrected that control arm from 30/30 to 29/30 because one `WER-07` response
omits the supplied no-downstream-consequence fact. The current active gate is
therefore blocked pending an approved disposition or separate repair slice.
A later no-edit WER-07 diagnostic scored 8/10 on the owned ledger and 10/10 on its
composition ledger. Five independent causal meta-reviews unanimously found the
necessary current skill rule clear and attributed the misses to semantic task
fidelity rather than a documentation or organization gap. This evidence does not
alter the strict 5/5 rule or authorize a third skill wording trial; any distinction
between run-level ownership and skill-document causality is a validation-protocol
decision requiring explicit owner disposition.
The owner approved a no-change disposition for Task 21: reject the readability
attempt, retain the exact control, keep the WER-07 misses as genuine model-execution
evidence, and do not treat them as passes or as grounds for another wording trial.
Because no skill change is accepted, Task 21 may proceed to final in-place approval;
the disposition does not waive strict 5/5 or remove WER-07 from the final
repository-wide suite.
The owner subsequently approved the complete exact in-place 372-word skill at
`568b2a61…`. That approval closes the Task 21 skill-review gate without accepting a
readability change or changing the retained WER-07 verdicts.

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
behavior slice will add four more after they are GREEN, producing the 86-scenario
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

Scorer labels are inputs to orchestration, not authoritative verdicts.
Before counting a miss, confirm that it changes an observable action, outcome,
ordering, ownership, blocked transition, or truthful bookkeeping.
Do not fail correct behavior for omitted optional rationale, failure to repeat a
supplied fact, or different wording, placement, formatting, or rendering.
Exact wording can fail only when literal output is itself the skill's necessary
owned behavior; first challenge whether that exactness is a valid promise and test.

If wording changes after a failed run, restart the affected scenario at zero.
Record the missed criterion and relevant rationalization for failures.
A completed response with a genuine behavioral miss is a failure and cannot be discarded.
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
