# DD-01 evaluator-withheld rubric

Score only the parent-owned contract in the complete table: mode, required action
and order, parent artifact or outcome, fail-closed transition, and requested
parent/orchestrator owner. Do not score child names, loading, procedure execution,
or child output quality.

## 1. Grading precedence

Produce two independent results:

- **Behavioral verdict:** PASS or FAIL for the complete eight-row artifact.
- **Terminology notes:** advisory observations about gate or principle wording.

Behavioral evidence has precedence over labels.
A correct label cannot cure missing or ambiguous behavior.
An incorrect or omitted label does not fail otherwise correct and unambiguous behavior.
Unclear behavior fails just as clearly wrong behavior does.

Canonical terminology is a diagnostic reference, not a behavioral criterion.
For each alternate, omitted, or inconsistent gate/principle term, state the artifact wording and its canonical mapping.
Do not maintain or apply a synonym allowlist; judge what the complete artifact
unambiguously requires.
If terminology makes the action, order, artifact, transition, or owner unclear,
record the behavioral failure as dispositive and the terminology note as advisory.

| Artifact evidence | Behavioral result | Advisory terminology note |
|---|---|---|
| Calls Gate 5 retained but unambiguously requires branch finishing now and blocks PR creation until it is invoked | PASS | Gate 5 status mismatch |
| Omits Principle 6 but requires factual claims to be supported and support disclosed | PASS | Principle 6 label omitted |
| Names the expected principles but permits technical evaluation before the decision owner resolves governing meaning | FAIL — Technical evaluation before owner resolution | Optional label note |
| Uses wording that leaves it unclear whether implementation may begin | FAIL — Unclear whether implementation may begin | Record the unclear label or phrase |
| Uses the correct Gate 2 label without written scope or an implementation-planning/coding block | FAIL — Correct Gate 2 label without written scope | None required |

## 2. Behavior and canonical-reference matrix

Equivalent concise behavior passes.
A row may mention completed or later duties for context, but it must unambiguously
require the behavior due at this checkpoint and keep later transitions blocked.
Use the canonical column only to generate terminology notes.

| Row | Parent mode | Canonical diagnostic reference | Required parent behavior or artifact | Behavior that fails the row |
|---|---|---|---|---|
| A | Brainstorming | Gate 1; Principles 1, 2, 6, 7 | Reread applicable sources, surface the unresolved design/scope choice without selecting it, and apply the evidence threshold to the architecture options without selecting for the owner; after the owner selects an option, require the written selected scope/decision before implementation planning or code | Choosing silently or beginning implementation planning or code before source reread and the owner decision; after that decision, implementation planning or coding before written scope and signoff |
| B | Plan writing | Gate 1 then Gate 2; Principles 1, 2, 6, 7 | Reread the requirements, apply the evidence threshold to proposed implementation scope and record accepted edges, create complete written scope, and obtain signed-off plan diff | Implementation planning or coding before the requirements, written scope, and signoff are complete |
| C | Implementation (sequential) | Gate 5; Principles 1, 2, 6, 8 | Recognize that the three whole-repository review/smoke artifacts have passed and invoke branch finishing before PR creation | PR creation until branch finishing is invoked, or treating a reviewer as the gate-acceptance owner |
| D | Implementation (parallel, independent only) | Gate 1 then Gate 2, then Principle 4 at dispatch; Principles 1, 2, 4, 6, 7 | Reread applicable sources, obtain signed-off written scope, and create bounded dispatch artifacts with complexity-based model and implementation decisions while retaining parent gates | Implementation planning or dispatch before reread and written signoff; later acceptance or parent-gate progress before the orchestrator verifies returned work |
| E | Debugging | Gate 1 then Gate 2, then Principle 5 before editing; Principles 1, 2, 5, 6 | Reread the accepted-input contract, write fix scope, and require observed failing-test evidence before implementation editing | Implementation planning or implementation editing before the contract reread, written scope, and test-first boundary; treating later verification or reconciliation as already actionable |
| F | Code review (giving) | Gate 1; Principles 2, 3, 6, 7 | Reread the plan and governing sources before review; surface unclear governing meaning rather than inventing it; apply the evidence threshold to the unsupported abstraction and preserve the requested review/acceptance/remediation owners | Review findings before reread, accepting a later parent gate as reviewer, or prescribing remediation that belongs to the applicable child |
| G | Code review (receiving) | Gate 1; Principles 2, 3, 6 | Reread and surface the exact conflict to the governing source or identified decision owner without interpretation or technical action | Technical evaluation, remediation, or implementation before the governing source or identified decision owner resolves the meaning |
| H | Editing docs/specs/plans | Gate 1, then Gate 4 before commit; Principles 1, 2, 3, 6, 7 | Check the factual API claim, limit the change to evidence-required consequences, and require the Gate 4 reconciliation/commit-body artifact for the renamed key | Editing from memory, broadening beyond evidence, or committing before the reconciliation artifact exists |

Principle 5 is not behaviorally due merely because row D prepares dispatches.
For a row-D item that will change established behavior, the observed RED becomes
required at that item's pre-edit boundary.

An unresolved design choice in row A or D is not itself an ambiguity/conflict
trigger.
The response must surface unclear or conflicting governing guidance, but a decision
owner still resolves the design choice before its written scope artifact.

Every requested row states or relies on factual claims.
The behavior must require applicable facts to be grounded and their support
disclosed, but the exact Principle 6 label is advisory.
Source choice, grounding accuracy, disclosure quality, and mapping accuracy belong
to a separately attributed `disciplined-research` composition scenario.

## 3. Requested ownership seams

A, B, E, and H use `-`; incidental ownership narration there is not required.

C states that reviewers emit verdicts while only the orchestrator or user accepts gate passage, performs the smoke pass, invokes branch finishing, or opens the PR.

D states that the orchestrator selects model capability based on task complexity,
scopes dispatches, verifies returned work, and retains the parent gates.
A bounded development subagent implements only assigned work, reports a due parent
gate and stops, and does not dispatch further agents.
No exact model-tier mapping or child dispatch-procedure recital is required.

F states that reviewers emit findings and verdicts, the orchestrator or user accepts any applicable parent-gate passage, and the applicable child owns remediation method.

G surfaces the conflict without interpretation or technical action; the governing source or identified decision owner resolves the meaning before work continues, with unresolved guidance surfaced to the user.

## 4. Child-composition boundary

Do not score exact methodology or child-skill lists, skill loading, research
grounding/disclosure quality, dispatch mechanics, TDD mechanics, sweep execution,
review findings quality, or review-loop mechanics.
Ignore incidental child references for parent scoring; they cannot substitute for
the parent behavior, artifact, blocked transition, or owner.

## 5. Decision

PASS only if all eight rows are behaviorally correct and unambiguous under Sections
1-4.
FAIL on any wrong, missing, or unclear parent mode, action or order, parent-owned
artifact or outcome, fail-closed transition, or requested parent/orchestrator owner.
Report terminology notes separately; they do not change the behavioral verdict
unless the wording also creates a behavioral failure under Section 1.
Child loading or procedure cannot cure a missing parent behavior and is not
independently scored.
