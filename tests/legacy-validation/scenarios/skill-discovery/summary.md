# Skill Discovery Scenario Audit

## Status

The scenario-by-scenario audit and first current-main observations were completed
on 2026-09-05. All 12 scenarios remain in the catalog, and no prompt, rubric,
configuration, or fixture contract required repair during the audit. The
provider-free catalog test now recognizes the accepted evidence triplet in every
scenario. All 12 accepted high-effort runs are judgeable `PASS` results. These
single observations develop the scoring method and test process; they do not
measure routing effectiveness.

This catalog does not exercise a repository `skill-discovery` skill file. Its
subject is the canonical set of nine local skill descriptions embedded in each
prompt at source commit
`13599fb7d3127334b0d07bfe468767e586ec5f9c`. Each fresh evaluator must choose
the descriptions that directly apply to the nested request without reading
skill bodies. All accepted runs used Codex `gpt-5.6-sol` at high effort and have
retained `COMPLETED` bundles. This is a human-authored audit record, not a
generated manifest.

## Scenario decisions

| Scenario | Decision | Coverage and rationale | Evidence disposition |
|---|---|---|---|
| [DISC-01](disc-01/README.md) | Keep | Distinguishes internal logical review of supplied API text from unrelated development companions. | The [accepted observation](disc-01/accepted/worksheet.md) is a `PASS`: it selects adversarial review, parent development, and research, with no prohibited route. |
| [DISC-02](disc-02/README.md) | Keep | Distinguishes remediation of already-reported external findings from starting a new review. | The [accepted observation](disc-02/accepted/worksheet.md) is a `PASS`: it selects the review loop, parent development, and research while correctly omitting adversarial review. |
| [DISC-03](disc-03/README.md) | Keep | Isolates purely stylistic shortening of reader-facing README prose. | The [accepted observation](disc-03/accepted/worksheet.md) is a `PASS`: it selects concise writing, parent development, and research exactly. |
| [DISC-04](disc-04/README.md) | Keep | Separates executing an active plan from authoring or revising one. | The [accepted observation](disc-04/accepted/worksheet.md) is a `PASS`: it selects parent development and research plus optional concise writing, but not lean plan writing. |
| [DISC-05](disc-05/README.md) | Keep | Tests routing of a repository fact lookup without allowing the evaluator to perform the lookup. | The [accepted observation](disc-05/accepted/worksheet.md) is a `PASS`: it selects parent development and research plus optional concise writing and remains routing-only. |
| [DISC-06](disc-06/README.md) | Keep | Exercises the required parent-and-research composition for a development-subagent dispatch. | The [accepted observation](disc-06/accepted/worksheet.md) is a `PASS`: it selects all three required routes and does not actually dispatch an agent. |
| [DISC-07](disc-07/README.md) | Keep | Isolates plan creation and the lean-plan companion. | The [accepted observation](disc-07/accepted/worksheet.md) is a `PASS`: it selects parent development, research, lean plan writing, and optional concise writing. |
| [DISC-08](disc-08/README.md) | Keep | Tests a load-bearing exact identifier rename across code and documentation under a no-prose-revision constraint. | The [accepted observation](disc-08/accepted/worksheet.md) is a `PASS`: it selects stale-reference sweeping with parent development and research, plus rubric-permitted concise writing. |
| [DISC-09](disc-09/README.md) | Keep | Isolates durable rationale for a deliberate temporary shortcut beside code. | The [accepted observation](disc-09/accepted/worksheet.md) is a `PASS`: it selects explicit rationale with parent development and research, plus optional concise writing. |
| [DISC-10](disc-10/README.md) | Keep | Tests plan editing combined with migration of supplied deferral rationale out of a PR description. | The [accepted observation](disc-10/accepted/worksheet.md) is a `PASS`: it selects all four required routes plus both permitted optionals, concise writing and stale-reference sweeping. |
| [DISC-11](disc-11/README.md) | Keep | Tests whether a private, uncommitted, unpublished destination incorrectly suppresses research for a factual software claim. | The [accepted observation](disc-11/accepted/worksheet.md) is a `PASS`: it preserves parent-development and research routing with no prohibited skill. |
| [DISC-12](disc-12/README.md) | Keep | Provides a non-development control for a casual response that repeats and relies on a user-supplied factual claim. | The [accepted observation](disc-12/accepted/worksheet.md) is a `PASS`: it requires research, permits concise writing, and correctly excludes disciplined development. |

## Catalog assessment

The catalog covers the intended routing boundaries in compact, independently
judgeable groups:

- DISC-01 and DISC-02 distinguish new review from remediation of findings that
  have already been reported.
- DISC-03 through DISC-05 distinguish prose revision, active-plan execution,
  and repository fact lookup while preserving the parent-and-research routes.
- DISC-06 through DISC-09 isolate dispatch, plan creation, stale-reference
  sweeping, and durable-rationale companions.
- DISC-10 exercises composition of multiple required and optional companions in
  one plan amendment.
- DISC-11 and DISC-12 test research's destination-independent trigger, including
  private scratch and non-development conversational contexts.

All required routes were selected in all 12 observations, and no prohibited
route was selected. The paired boundary cases were particularly clean:
DISC-01/DISC-02 separated review from review-loop remediation; DISC-04 did not
mistake plan execution for plan writing; DISC-11 retained development for a
software note while DISC-12 excluded it from a personal conversation.

No authenticated deterministic consumer applies to these scenarios. JSON
syntax, alphabetical order, and absence of prose are therefore task-fidelity
constraints rather than deterministic protocol. Every accepted response passed
those constraints.

## Scenario-contract observations

One non-blocking rubric ambiguity should survive into later cleanup. DISC-08
expressly forbids rewriting or tightening surrounding prose, but its canonical
rubric permits `concise-writing` as optional. The accepted response selected
that optional skill and therefore passes the frozen rubric. When the catalog is
later revised, decide whether a mechanical documentation-token replacement
should prohibit concise writing instead.

DISC-12 retains a historical `smoke-result.json` in its scenario package. The
provider-free test and accepted run confirm that the file is metadata only: it
was not copied into the prepared workspace or transmitted as provider input.
Neither observation required changing the accepted scenario contracts during
baseline capture.

## Execution-process observation

All 12 accepted runs were fully fixture-only. The providers issued no commands
or tool calls, read no installed skill or repository file, made no edits, and
left empty evidence directories. This catalog therefore avoids the ambient
skill-read limitation seen in most task-execution catalogs and provides clean
causal observations of the nine inline descriptions.

DISC-11's first shell escalation was rejected before provider invocation
because the nested request described a private, unpublished note. The owner then
explicitly approved transmission of that and comparable remaining catalog
prompts. The retained run is the first provider invocation, so the authorization
event is not an `INFRA_RETRY` and is not counted as a sampled infrastructure
failure.

Fixture-only execution does not make this an installed-skill effectiveness
test. The inline descriptions, enclosing routing instructions, and constrained
JSON response are the tested contract. Future claims about ambient discovery or
automatic skill loading require a separately isolated design.

## Later effectiveness campaign

Once scenario coverage and scoring methodology are stable, effectiveness
testing should use multiple independent runs for each selected model-and-effort
configuration. The intended first matrix is `gpt-5.6-sol` at high, medium, and
low effort. A later `gpt-5.6-terra` high-effort arm may help determine whether a
different model is a useful baseline subject. Repetition counts, acceptance
thresholds, aggregation, and comparison rules remain deliberately undecided;
these 12 single runs do not answer those questions.

## Next actions

1. Continue with the concise-writing catalog using the same scenario-by-scenario
   current-main audit and single-run process-development exercise.
2. Before controlled comparisons, execute the deferred provider-input-isolation
   plan and decide how undeclared runtime reads will be prevented or classified.
3. Do not begin rewrite comparison, model-matrix execution, or rewrite work until
   the current scenario portfolio and scoring process are sufficiently
   established.
