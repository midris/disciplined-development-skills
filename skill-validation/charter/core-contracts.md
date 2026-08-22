# Charter-first core validation contracts

## Status

The owner approved this validation architecture on 2026-08-21.
This record maps the existing scenario catalog into the proposed core suite.
It does not activate repaired prompts or rubrics, retire the prior hard gates, or
authorize a skill wording change.
The existing suite remains binding until the rebuilt suite has independent control
evidence, review, and owner approval.

## Acceptance model

Every scored criterion belongs to exactly one ledger:

| Ledger | What it measures | Blocks skill acceptance |
|---|---|---|
| Core behavior | Observable action, outcome, order, owner, blocked transition, or truthful evidence mapped to a charter invariant | Yes |
| Deterministic protocol | Bytes consumed or produced by an authenticated renderer, validator, or production consumer | Yes, when applicable |
| Task or fixture fidelity | Requested shape or datum that does not change the skill-owned behavior | No; if it prevents judgment, repair and invalidate the scenario |
| Readability | Findability, processing effort, and material clarity | Separate quality gate |
| Infrastructure | Transport or harness failure with no evaluable response | No; exclude from the behavioral denominator and retry under the recorded policy |

Scorers are advisory.
The orchestrator reads the raw artifact or independently inspected state and owns the
final ledger assignment and verdict.
A read-only response proves action selection, not that a search, edit, verification,
commit, or review loop was executed.

## Skill contracts and proposed core portfolios

### `disciplined-development`

**Charter:** Prevent progress across development boundaries until the required
evidence exists, while retaining parent gate and acceptance authority.

| Invariant | Observable promise |
|---|---|
| `DD-I1` | A gate fails closed until its applicable source, scope, or completion artifact exists; before any factual claim or relied-on premise, the parent selects grounding and blocks every dependent transition until research supplies a support-mapped outcome; invalidated evidence restarts the earliest affected gate. |
| `DD-I2` | The parent selects and accepts gates, bounds delegation, and never transfers parent review, smoke, finishing, or PR authority to a child. |
| `DD-I3` | Behavior work has directly observed RED, running-system evidence, reconciled references, coherent commit state, and truthful review/smoke evidence at their boundaries. |
| `DD-I4` | Analysis generates absent, malformed, and scale cases, while implementation remains limited to contract, reachability, observation, or robust-invariant needs. |

Proposed core sources: `DD-05` positive Gate 1, `DD-07` pressure at test/delegation,
`DD-08` unauthorized-work and Gate 4 boundary, `DD-03` proportionality boundary,
and `DD-02` integrated invalidation/restart lifecycle.
Absorb `DD-06` and `DD-09` into the focused/integrated cases.
Keep `DD-04` as an atomic attributed parent-core and research-composition case: the
parent owns universal selection and the dependent block, while research owns source
selection, acquisition, verification, and support disclosure.
Reclassify `DD-01` as broad routing diagnostic/shared coverage rather than a single
dense core verdict.

### `disciplined-research`

**Charter:** Prevent unsupported factual claims or premises from entering reasoning
or work.

| Invariant | Observable promise |
|---|---|
| `DR-I1` | Every factual claim or relied-on premise is verified before use. |
| `DR-I2` | The selected source is authoritative, applicable, and current enough for the claim; conflicts are resolved rather than averaged or hidden. |
| `DR-I3` | Each emitted fact has a precise, truthful support mapping. |
| `DR-I4` | Unsupported facts are omitted; a useful investigation lead remains explicitly unverified without false support. |

Proposed core sources: `DR-02` authority/conflict positive, `DR-06` unsupported-lead
pressure with semantic rather than literal-stamp scoring, `DR-05` missing-datum
boundary, and `DR-07` ordinary non-development conversation.
Absorb the distinct local-implementation, cross-source, and private-note pressures
from `DR-01`, `DR-03`, and `DR-04` without retaining their line-count or source-order
requirements.

### `writing-explicit-rationale`

**Charter:** Preserve decision-useful rationale in one durable, discoverable home
without duplicating irrelevant history.

| Invariant | Observable promise |
|---|---|
| `WER-I1` | The decision and material operational consequences remain; causal history is retained only when it helps future correctness or decisions. |
| `WER-I2` | Necessary rationale lives beside the decision in the nearest durable authoritative project artifact. |
| `WER-I3` | Other sites reference the authoritative rationale rather than creating competing explanations. |
| `WER-I4` | Repeated challenge triggers an audit of related decision sites and a batched repair. |

Proposed core sources: `WER-01` positive, `WER-02` re-litigation pressure, `WER-05`
authoritative-home boundary, and `WER-08` broad-domain boundary.
Absorb `WER-06`'s relevant-history distinction and the WER-owned portion of
`WER-07`; keep research mapping in separately attributed composition coverage.
Keep `WER-03` and `WER-DEV` historical.

### `concise-writing`

**Charter:** Remove prose that adds no value without changing how a careful reader
understands or uses the artifact.

| Invariant | Observable promise |
|---|---|
| `CW-I1` | Every consequential fact, relationship, boundary, rationale, and findable use remains; the revision adds no unsupported meaning. |
| `CW-I2` | Local and whole-artifact padding, duplication, and unsupported elaboration are removed when lossless. |
| `CW-I3` | The method applies to its reader-facing and durable-prose domain while respecting the explicit detailed-response exception. |

Proposed core sources: a merged ordinary positive corpus based on `CW-01`–`CW-06`,
`CW-19` as the complex conservation pressure case, and `CW-08` as the isolated
broad-domain boundary.
Keep `CW-17`/`CW-18` as shared routing polarity if still necessary.
Move `CW-09`–`CW-14` to authoring/discovery composition and treat their JSON order,
keys, whitespace, and verbatim quotation as fixture fidelity.
`CW-07` remains direct-invocation transport evidence, not owned core behavior.

### `lean-plan-writing`

**Charter:** Produce an executable behavioral contract without writing the
implementation in the plan.

| Invariant | Observable promise |
|---|---|
| `LP-I1` | Plans specify behavior in prose rather than implementation/test bodies or copyable templates. |
| `LP-I2` | Concrete changes, behavioral tests, edges, dependencies, and silent-invariant dispositions make implementation possible. |
| `LP-I3` | Test contracts express tricky logic; one illustration of at most five lines appears only for an irreducibly ambiguous exact artifact. |
| `LP-I4` | Independently green, reviewable units split; tightly coupled work that cannot remain green stays atomic. |

Proposed core sources: `LP-05` with `LP-06` edge cases as the positive case,
`LP-02` as implementation-template pressure, `LP-03` as the precision-exception
boundary, and the `LP-07`/`LP-08` split-versus-atomic polarity family.
Retain `LP-01` only as shared `writing-plans` composition coverage.
Keep `LP-04` historical.

### `sweeping-stale-references`

**Charter:** Find, disposition, and reconcile every mutable encoding of a changed
fact before the change is accepted.

| Invariant | Observable promise |
|---|---|
| `SSR-I1` | Searches cover every applicable old/new encoding, synonym, and mutable repository surface before and after editing. |
| `SSR-I2` | Every mutable match receives one truthful disposition while immutable history remains outside the rewrite inventory. |
| `SSR-I3` | All updates land together and preserve the changed fact's distinct causal constraint and accepted cost. |
| `SSR-I4` | Durable sweep evidence reconciles to independently observed paths, outcomes, locations, and counts, including the no-sibling branch. |

Proposed core sources: rebuild `SSR-01` as the executable positive while absorbing
`SSR-06` and `SSR-07`; rebuild `SSR-02` as executable reviewer/IDE pressure while
absorbing `SSR-03`'s useful scale and grouping semantics; retain `SSR-05` as the
executable no-sibling branch.
Keep `SSR-04` historical.
Commit-body placement or a `Verification:` heading is not a core failure unless a
deterministic consumer is added; truthful durable reconciliation remains core.

### `dispatching-development-subagents`

**Charter:** Make delegated development changes safely integrable through bounded
scope, retained parent authority, and returned-diff verification.

| Invariant | Observable promise |
|---|---|
| `DSD-I1` | Each dispatch has one source-faithful bounded scope and preserves the applicable out-of-scope gradient. |
| `DSD-I2` | The recipient remains a subagent: it dispatches no children, takes no parent gate, reports the due gate to the orchestrator, and stops. |
| `DSD-I3` | The orchestrator independently inspects every returned commit's stat and complete diff and verifies direct evidence before integration. |
| `DSD-I4` | The handoff truthfully discloses beyond-scope work and unsupported rationale is not landed as fact. |

Proposed core sources: one new executable positive path rebuilt from `DSD-01`,
`DSD-03`, and `DSD-06` that proceeds from source-faithful bounded scope through
dispatch, returned commits and handoff, independent diff/direct-evidence inspection,
and an integration decision; `DSD-04` partitioning pressure; and `DSD-02` integrated
identity/nudge pressure.
Absorb `DSD-07`–`DSD-10` into those cases.
Move `DSD-05` and `DSD-11` factual-support criteria to separately attributed
research composition coverage.

### `adversarial-review`

**Charter:** Find evidenced material defects that ordinary review misses without
inventing requirements or false shared causes.

| Invariant | Observable promise |
|---|---|
| `AR-I1` | Findings are real, evidenced, appropriately severe, and produce the correct blocking disposition; clean work is not blocked. |
| `AR-I2` | The holistic baseline enumerates referenced classes and generates absent, malformed, out-of-scale, and fragile-invariant cases. |
| `AR-I3` | Rationale is verified and every artifact part is challenged for necessity and effectiveness rather than activity or proxy value. |
| `AR-I4` | Specialized lenses add relevant scrutiny and pattern synthesis names only evidence-backed shared causes. |

Proposed semantic core sources: `AR-03` positive, a merged `AR-05`/`AR-06`
durability and generated-case pressure, and a polarity boundary combining `AR-15`
clean-work restraint with `AR-13` no-false-pattern behavior.
Absorb useful seams from `AR-07`, `AR-08`, `AR-10`, `AR-12`, `AR-14`, `AR-16`, and
`AR-17` only when the rebuilt fixtures remain diagnostic.
Fold `AR-01`'s ordinary finding/disposition behavior into `AR-03`, keep `AR-04` as
angle-routing/shared diagnostic, and keep `AR-09` historical.

The deterministic protocol ledger remains separate: use `AR-02`, the bundled
renderer/checker, and the final bytes of retained semantic responses to verify finding
grammar, quoted-marker isolation, one adjacent pattern line, terminal verdict, and
severity/verdict consistency.
The checker never decides whether a shared pattern is semantically true.

### `adversarial-review-loop`

**Charter:** Remediate findings by complete class or shared root, preserve counter
ownership, and escape reactive churn at the cap.

| Invariant | Observable promise |
|---|---|
| `ARL-I1` | Every blocking class is enumerated and remediated completely before the same reviewer reruns. |
| `ARL-I2` | Accumulated findings are classified as scattered or as one evidenced invariant; a real root is audited project-wide. |
| `ARL-I3` | Cycle-3 entry records the all-round verdict first, and a blocking third completed rerun takes the cold-read escape rather than a fourth ordinary cycle. |
| `ARL-I4` | Task and whole-branch workflows, counters, reviewers, rulings, and records retain their correct owners. |

Proposed core sources: one class-sweep positive/recurrence-pressure case from
`T2`/`CS`/`T6`/`T7`; one shared-root versus no-pattern polarity case from
`G3A`/`G3B`/`NF`/`PW`/`XL`/`T4`; `CE` with `T3` for the cap and all escape outcomes;
and `OWN` with `G3C`/`T5` for workflow, counter, reviewer-ruling, and P3 boundaries.
Research mapping remains separately attributed composition coverage.

## Executed-work requirements

The rebuilt suite must independently inspect state for these claims:

| Scenario family | Independent evidence |
|---|---|
| `SSR-01` / `SSR-02` / `SSR-05` | Seeded old/new encodings and false-positive/history cases; post-edit searches; final file state; one actual commit; durable sweep evidence reconciled to observed paths, outcomes, and counts. |
| `DD-08` | Unauthorized change is dispositioned before positive-path work; actual CLI result; reference reconciliation; actual green commit containing the intended test, implementation, and references. |
| `DD-02` / Gate 5 restart | Seeded outside-diff discrepancy; scope decision before remediation; invalidated evidence replaced; independent review and smoke outcomes; finishing invocation before PR eligibility. |
| `DSD-03` | Real returned commits; independent stat and full diff per commit; beyond-scope change surfaced; integration decision supported by direct evidence rather than the handoff text. |
| `ARL` class/root cases | Seeded complete classes and uncited cross-surface members; an independently inspected ordered event log and artifact snapshots proving the all-round verdict precedes cycle-3 remediation, every unacted P3 has an on-page disposition, the same reviewer reruns, task/whole-branch counters stay separate, the third blocking rerun persists the escape verdict, the cold reviewer has a fresh context identity, and no fourth ordinary cycle occurs first. |

An executable fixture may prove multiple composed invariants, but its result remains
attributed to each owning skill rather than pooled into an undifferentiated score.

## Frozen comparison arms

Original skills come from local branch `main` at
`5219997ff580f7cfac4115e4c38d396d3dd9101e`.
Current skills are the exact worktree bytes recorded below on 2026-08-21.

| Skill | Original SHA-256 | Current SHA-256 |
|---|---|---|
| `adversarial-review-loop` | `46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6` | `0113503cfe69fbd88b6ce9125ec3db18b46e2f370d046e19d8419b93b8a17716` |
| `adversarial-review` | `9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c` | `309bd02c8bc6c06bb09d166c29a06152183bb4d4197755a35653e01131c703c6` |
| `concise-writing` | `4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72` | `f763b43e88c56d6fdc2a96457bc2415cba60b75a1e7cb59cd1b0ebaa3fb199ba` |
| `disciplined-development` | `1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec` | `4e5b52205c560448579eaafacc4ad55c81ae4156bb3bf6b1997b68669cadae42` |
| `disciplined-research` | `a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50` | `6fa7d81c67c3075429c1fd9f54d37d494d0e24f877de976a6c0da71da8a61984` |
| `dispatching-development-subagents` | `b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500` | `bf616daa594a90282ccfa22af210214b30393158838b5feb9220859268f9fe54` |
| `lean-plan-writing` | `6a3115a4d33ad2f99238f915a6a1b7869efd8c80a6cce422d3afae60c9857fac` | `db1ade9e0ba7395bf662d041c866ce80965f729725d3829983adcdfd21946129` |
| `sweeping-stale-references` | `d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157` | `15992341f7ab2fb1e4d8a775092199d7d4e6a9de1167895dbe5a805aeafbd38c` |
| `writing-explicit-rationale` | `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe` | `568b2a61bef3f7694014fb89228f933261837acd4f2b5978b2b8ef55aa108c9f` |

The current arm must be re-frozen if any supplied skill byte changes.
Prompt, rubric, fixture, dependency, or result-contract changes invalidate both arms
for every affected scenario.

## Execution schedule

During rebuild, run each behavioral scenario three times at Sol low against both
arms.
Expand that round to five only when the first three split, expose rubric ambiguity,
or show unstable task fidelity.
After prompts, rubrics, fixtures, result processing, and ledger attribution are
stable, freeze both arms and run three fresh Sol-high repetitions per core scenario.
The current arm must pass every core behavior and applicable deterministic protocol
scenario 3/3.
This owner-approved schedule supersedes the transitional protocol's prior five-run
Sol-high rule only when the rebuilt suite is activated; the existing suite retains
its current hard gates during the transition.
