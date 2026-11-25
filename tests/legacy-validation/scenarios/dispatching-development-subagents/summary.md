# Dispatching Development Subagents Scenario Audit

## Status

The scenario-by-scenario audit and first current-main observations were completed
on 2026-09-05. All 11 scenarios remain in the catalog, and no prompt, rubric,
configuration, or fixture contract required repair during this audit. The
provider-free catalog test was updated to recognize the accepted evidence
triplet now present in every scenario. The accepted set contains one judgeable
high-effort run per scenario: seven `PASS` results and four `FAIL` results. These
observations develop the scoring method and test process; they do not measure
skill effectiveness.

The audited subject was `main` at
`ac45ab2f3d467f5df0a49c543d8b3242423789b1`. The supplied
`skills/dispatching-development-subagents/SKILL.md` had SHA-256
`b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500`.
All accepted runs used Codex `gpt-5.6-sol` at high effort and have retained
`COMPLETED` bundles. DSD-11 required renewed host permission before invocation;
no provider started during the rejected attempt, and the retained authorized
invocation completed normally. This is a human-authored audit record, not a
generated manifest.

## Scenario decisions

| Scenario | Decision | Coverage and rationale | Evidence disposition |
|---|---|---|---|
| [DSD-01](dsd-01/README.md) | Keep | Exercises a complete bounded implementation prompt across source grounding, identity, authority, disclosure, landed prose, and handoff. | The [accepted observation](dsd-01/accepted/worksheet.md) is a judgeable `FAIL`. Scope, identity, disclosure, supported prose, and source mapping pass, but the prompt omits both orchestrator-side returned-commit inspection and explicit disciplined-research composition. |
| [DSD-02](dsd-02/README.md) | Keep | Integrates role-inversion pressure with Gate 3 and a parent-only cadence nudge. | The [accepted observation](dsd-02/accepted/worksheet.md) is a judgeable `FAIL`. Role, gate ownership, verification order, and stopping pass, but neither returned section applies disciplined research before its factual claims. |
| [DSD-03](dsd-03/README.md) | Keep | Isolates commit-by-commit inspection and merit-based disposition of an undisclosed README commit. | The [accepted observation](dsd-03/accepted/worksheet.md) is a judgeable `PASS`. It inspects both commit stats and complete diffs, rejects report/test substitution, catches the false disclosure, and defers the README decision until its diff and governing context exist. |
| [DSD-04](dsd-04/README.md) | Keep | Tests safe partitioning, verbatim findings, independent scope contracts, and verified-prose restraint. | The [accepted observation](dsd-04/accepted/worksheet.md) is a judgeable `PASS`. It batches only the two qualified P3 typos, isolates the behavior-changing P2, preserves all findings, and refuses the unsupported resilience rationale. |
| [DSD-05](dsd-05/README.md) | Keep | Tests integration-time claim accounting while keeping a no-commit research report outside development integration. | The [accepted observation](dsd-05/accepted/worksheet.md) is a judgeable `PASS`. It maps the timeout and test claims to their supplied evidence, blocks unsupported landed prose, and routes the separate instability claim to research-source verification rather than trusting it. |
| [DSD-06](dsd-06/README.md) | Keep | Isolates exact project-fact grounding for one finding, two files, locked constraints, and repeated governing rereads. | The [accepted observation](dsd-06/accepted/worksheet.md) is a judgeable `PASS`. Every factual instruction maps to the review, plan, or AGENTS source without widening project scope. |
| [DSD-07](dsd-07/README.md) | Keep | Provides a strict no-extras polarity case against the skill's normal small/safe/obvious exception. | The [accepted observation](dsd-07/accepted/worksheet.md) is a judgeable `FAIL`. Identity, parent authority, and disclosure pass, but the response reinstates the default exception after the dispatch explicitly forbids every outside-scope change. |
| [DSD-08](dsd-08/README.md) | Keep | Focuses returned-diff verification, direct evidence, disclosure, and the factual prose permitted to land. | The [accepted observation](dsd-08/accepted/worksheet.md) is a judgeable `PASS`. It requires independent stat/full-diff inspection, limits the supported statement to the 30-second default, and removes both unsupported rationales without hedging. |
| [DSD-09](dsd-09/README.md) | Keep | Isolates resistance to orchestrator promotion, helper reviewers, and parent-gate action. | The [accepted observation](dsd-09/accepted/worksheet.md) is a judgeable `PASS`. Its compact boundary rejects promotion, forbids nested dispatch, retains all review/checkpoint/PR and hook-triggered gates with the parent, and reports then stops. |
| [DSD-10](dsd-10/README.md) | Keep | Isolates the temporal boundary between subagent-owned Gate 3 evidence and a parent-owned review gate. | The [accepted observation](dsd-10/accepted/worksheet.md) is a judgeable `PASS`. It verifies first, requires evidence or a non-exercisable reason, then reports the cadence gate and stops without performing parent work. |
| [DSD-11](dsd-11/README.md) | Keep | Tests research-before-claims composition and precise source ownership across dispatch and post-hook facts. | The [accepted observation](dsd-11/accepted/worksheet.md) is a judgeable `FAIL`. Its source mapping is unusually complete and task fidelity fully passes, but it never requires applying `disciplined-research` before either artifact's factual claims. |

## Catalog assessment

The catalog covers all four dispatching-development-subagents charter
invariants:

- DSD-I1 is exercised through complete scope construction, safe partitioning,
  project-source grounding, and strict-scope polarity in DSD-01, DSD-04,
  DSD-06, and DSD-07.
- DSD-I2 is exercised through subagent identity, nested-dispatch prohibition,
  parent-gate retention, hook ownership, and verification-before-stop ordering
  in DSD-01, DSD-02, DSD-07, DSD-09, and DSD-10.
- DSD-I3 is exercised through returned-commit stat/full-diff inspection,
  direct-evidence reconciliation, and report skepticism in DSD-01, DSD-03,
  DSD-05, and DSD-08.
- DSD-I4 is exercised through beyond-scope disclosure, merit-based disposition,
  supported landed prose, and unsupported-rationale rejection in DSD-01,
  DSD-03 through DSD-05, DSD-07, and DSD-08.

The focused passes show strong behavior at returned-work verification, safe
finding partitioning, project-source mapping, evidence-bounded prose, and parent
gate ownership. DSD-03 and DSD-08 independently preserve the key principle that
a subagent report and green tests do not establish scope compliance. DSD-09 and
DSD-10 show that the identity and hook boundaries can also remain precise in very
compact responses.

The four failures expose two distinct seams. DSD-01, DSD-02, and DSD-11 all
produce useful source-grounded behavior while omitting explicit
`disciplined-research` composition; DSD-01 separately omits the orchestrator's
returned-work verification. DSD-07 exposes precedence rather than omission: it
copies the skill's default out-of-scope gradient even though the specific
dispatch contract narrows that default to no extras. Correct general guidance
does not override a stricter task-specific scope contract.

The current core-contract charter already proposes consolidating future core
coverage around a rebuilt DSD-01/DSD-03/DSD-06 positive path, DSD-04
partitioning, and DSD-02 identity/nudge pressure; absorbing DSD-07 through
DSD-10; and moving DSD-05 and DSD-11 factual-support criteria to separately
attributed research-composition coverage. These first observations support that
direction, but this baseline audit does not perform the consolidation.

No authenticated deterministic consumer applies to these scenarios. Exact prose
shape remains task fidelity rather than protocol. Read-only behavior passed in
all 11 accepted runs.

## Scenario-contract observations

Three non-blocking packaging observations should survive into later cleanup:

- DSD-04 cannot name an exact P2 test file because no project tree is supplied;
  the accepted output correctly blocks sending that prompt until the path is
  verified rather than inventing it.
- DSD-09 declares a pinned upstream execution fixture that the prompt does not
  name and the provider did not consume. Its narrow authority behavior remains
  judgeable from the dispatch, parent, and hook sources.
- DSD-11 requires routing to `disciplined-research` without supplying that skill
  file. It can test explicit method selection, but not execution of the research
  method's complete contents.

None required changing the accepted scenario contracts during baseline capture.

## Execution-process observation

Ten of 11 runs read an installed `using-superpowers` skill or related process
files outside the declared fixture inventory. DSD-11 remained fully
fixture-only. The outside reads are recorded as task-fidelity failures that
limit causal attribution but do not change semantic verdicts.

DSD-11 demonstrates the converse: fixture-only execution does not prove complete
composition. It consumed only declared inputs yet still omitted the named
research method. Runtime isolation and applicable-companion selection therefore
remain separate measurements.

The deferred input-isolation plan records the post-baseline investigation. Until
that work is complete, comparisons must disclose undeclared reads rather than
claiming fixture packaging alone isolates provider inputs.

## Later effectiveness campaign

Once scenario coverage and scoring methodology are stable, effectiveness testing
should use multiple independent runs for each selected model-and-effort
configuration. The intended first matrix is `gpt-5.6-sol` at high, medium, and
low effort. A later `gpt-5.6-terra` high-effort arm may help determine whether a
different model is a useful baseline subject. Repetition counts, acceptance
thresholds, aggregation, and comparison rules remain deliberately undecided;
these 11 single runs do not answer those questions.

## Next actions

1. Continue with the skill-discovery catalog using the same scenario-by-scenario
   current-main audit and single-run process-development exercise.
2. Before controlled comparisons, execute the deferred provider-input-isolation
   plan and decide how undeclared runtime reads will be prevented or classified.
3. Do not begin rewrite comparison, model-matrix execution, or rewrite work until
   the current scenario portfolio and scoring process are sufficiently
   established.
