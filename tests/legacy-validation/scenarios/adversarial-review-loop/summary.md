# Adversarial Review Loop Scenario Audit

## Status

The scenario-by-scenario audit and first current-main observations were completed
on 2026-09-05. All 15 scenarios remain in the catalog. No prompt, rubric,
configuration, or fixture contract required repair; the T2 README was clarified
to enumerate its nine supplied skills. The accepted set contains one judgeable
high-effort run per scenario: 13 `PASS` results and two `FAIL` results. These
observations develop the scoring method and test process; they do not measure
skill effectiveness.

The audited subject was `main` at
`ac45ab2f3d467f5df0a49c543d8b3242423789b1`. The supplied
`skills/adversarial-review-loop/SKILL.md` had SHA-256
`46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6`.
All accepted runs used Codex `gpt-5.6-sol` at high effort and have retained
`COMPLETED` bundles. This is a human-authored audit record, not a generated
manifest.

## Scenario decisions

| Scenario | Decision | Coverage and rationale | Evidence disposition |
|---|---|---|---|
| [CS](cs/README.md) | Keep | Tests whether recurrence after a one-line fix is recognized as an incomplete class sweep. | The [accepted observation](cs/accepted/worksheet.md) is a qualified judgeable `PASS`. It names the unscoped-directory-change class, sweeps all setup and runbook documents, and reruns the same reviewer. |
| [T2](t2/README.md) | Keep | Tests restraint when a complete search proves a one-member class while preserving the safe reviewer rerun. | The [accepted observation](t2/accepted/worksheet.md) is a qualified judgeable `PASS`. It accepts the bounded class, reruns the same reviewer, and does not substitute another workflow. |
| [T3](t3/README.md) | Keep | Tests the mandatory memory-free escape after the third completed blocking cycle. | The [accepted observation](t3/accepted/worksheet.md) is a qualified judgeable `PASS`. It treats the third rerun as the cap, forbids cycle four, and records the cold-read result. |
| [T4](t4/README.md) | Keep | Provides a below-cap negative control for unrelated findings that must remain scattered. | The [accepted observation](t4/accepted/worksheet.md) is a qualified judgeable `PASS`. It keeps SQL injection and N+1 behavior separate, sweeps the current N+1 class, and reruns without escaping early. |
| [T5](t5/README.md) | Keep | Tests whether a P3-only result ends the blocking loop while every advisory item receives a disposition. | The [accepted observation](t5/accepted/worksheet.md) is a qualified judgeable `PASS`. It declares the run clean, records individual dismissal rationales, and avoids an unnecessary rerun. |
| [T6](t6/README.md) | Keep | Tests that a complete self-sweep cannot certify its own result. | The [accepted observation](t6/accepted/worksheet.md) is a qualified judgeable `PASS`. It requires the same reviewer to rerun against the new HEAD before declaring clean. |
| [T7](t7/README.md) | Keep | Tests remediation of a new blocking class despite pressure to defer it as different work. | The [accepted observation](t7/accepted/worksheet.md) is a qualified judgeable `PASS`. It sweeps every unqualified-threshold claim and reruns only after the class is fixed. |
| [NF](nf/README.md) | Keep | Tests an early shared-root attack when the error-contract axis is already visible below the cap. | The [accepted observation](nf/accepted/worksheet.md) is a qualified judgeable `PASS`. It audits every EventLog path, fixes the typed-error invariant project-wide, and reruns the same reviewer. |
| [PW](pw/README.md) | Keep | Tests whether a shared-axis audit reaches uncited persistence components and failure paths. | The [accepted observation](pw/accepted/worksheet.md) is a qualified judgeable `PASS`. It expands beyond EventLog, enumerates other persistence sites, and fixes the whole axis before rerun. |
| [XL](xl/README.md) | Keep | Tests project-wide translation of one source-of-truth invariant across Swift, Python, and Go. | The [accepted observation](xl/accepted/worksheet.md) is a qualified judgeable `PASS`. It identifies plausible language-specific hazards, repairs all sites in one pass, and reruns the same reviewer. |
| [G3A](g3a/README.md) | Keep | Tests whether cycle-three analysis can locate a shared root in governing text rather than only implementation. | The [accepted observation](g3a/accepted/worksheet.md) is a qualified judgeable `FAIL`. It records a shared-root verdict before fixing, but says the governing rule forbids the behavior and never commits to changing that rule. |
| [G3B](g3b/README.md) | Keep | Provides the cycle-three no-shared-pattern polarity case. | The [accepted observation](g3b/accepted/worksheet.md) is a judgeable `PASS`. It distinguishes dead-code hygiene, documentation consistency, and test hermeticity, then sweeps only the network-test class. |
| [G3C](g3c/README.md) | Keep | Tests reviewer-side re-litigation, durable ruling, non-appeasement, and explicit P3 disposition. | The [accepted observation](g3c/accepted/worksheet.md) is a qualified judgeable `PASS`. It preserves the disputed rationale placement, closes the P2 re-raise with a ruling, and fixes the separate P3. |
| [OWN](own/README.md) | Keep | Tests ownership, precedence, counters, breakers, and factual grounding across the SDD and ARL composition. | The [accepted observation](own/accepted/worksheet.md) is a judgeable `FAIL`. Every ownership and counter criterion passes, but the provider never reads or applies the supplied disciplined-research companion before stating workflow facts. |
| [CE](ce/README.md) | Keep | Tests all three cold-read outcomes and their distinct redo, stop, or bounded-reset routes. | The [accepted observation](ce/accepted/worksheet.md) is a qualified judgeable `PASS`. It routes confirmed blockers to redo, trusts material divergence, and bounds productive fix-forward to another three-cycle window and escape. |

## Catalog assessment

The catalog covers all four adversarial-review-loop charter invariants:

- ARL-I1 is exercised through complete class remediation, reviewer continuity,
  and P3 disposition in CS, T2, T5 through T7, and the class-sweep portions of
  T4, NF, PW, XL, and G3B.
- ARL-I2 is exercised through scattered-versus-shared-root polarity, early root
  attack, and project-wide axis translation in T4, NF, PW, XL, G3A, and G3B.
- ARL-I3 is exercised through the cycle-three written-verdict gate, cap escape,
  reviewer-side drift, and all escape outcomes in T3, G3A through G3C, and CE.
- ARL-I4 is exercised through task-versus-whole-branch ownership in OWN and the
  reviewer-ruling and advisory boundaries in G3C and T5.

The positive results show strong handling of class breadth, same-reviewer
continuity, below-cap root attacks, scattered-finding restraint, and cap escape.
The polarity cases are useful: NF, PW, and XL require a real shared invariant;
T4 and G3B reject false umbrella causes; G3C locates the repeated problem in
reviewer behavior.

The two failures expose different composition seams. G3A recognizes the
fail-open pattern but does not locate or repair it in the governing sentence that
causes implementations to normalize anomalies. OWN gets every review owner,
round, counter, and next action right but omits the supplied research companion
whose process governs those factual claims. Both failures are precise enough to
retain as current-main baselines.

No authenticated deterministic consumer applies to these scenarios. Exact prose
shape remains task fidelity rather than protocol. Read-only behavior passed in
all accepted runs.

## Execution-process observation

Thirteen of 15 runs read an installed `using-superpowers` skill outside the
declared fixture inventory. G3B and OWN remained fixture-only. The outside read
is recorded as a task-fidelity failure that limits causal attribution but does
not change any semantic verdict in this catalog.

OWN illustrates a separate composition failure: staying fixture-only does not
prove that every applicable supplied input was used. It reads only declared
fixtures but omits disciplined research. Runtime isolation and complete
composition loading therefore need separate observations.

The deferred input-isolation plan records the post-baseline investigation. Until
that work is complete, comparisons must disclose undeclared reads rather than
claiming that fixture packaging alone isolates provider inputs.

## Later effectiveness campaign

Once scenario coverage and scoring methodology are stable, effectiveness testing
should use multiple independent runs for each selected model-and-effort
configuration. The intended first matrix is `gpt-5.6-sol` at high, medium, and
low effort. A later `gpt-5.6-terra` high-effort arm may help determine whether a
different model is a useful baseline subject. Repetition counts, acceptance
thresholds, aggregation, and comparison rules remain deliberately undecided;
these 15 single runs do not answer those questions.

## Next actions

1. Continue with the next untested skill catalog using the same
   scenario-by-scenario current-main audit and single-run process-development
   exercise.
2. Before controlled comparisons, execute the deferred provider-input-isolation
   plan and decide how undeclared runtime reads will be prevented or classified.
3. Do not begin rewrite comparison, model-matrix execution, or rewrite work until
   the current scenario portfolio and scoring process are sufficiently
   established.
