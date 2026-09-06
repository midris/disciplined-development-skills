# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/dispatching-development-subagents/dsd-11 |
| Scenario ID | dsd-11 |
| Scenario purpose | Require research and precise source mapping for dispatch and post-hook factual claims. |
| Run ID | 20260906T013821976Z-dsd-11-8ec7acac-d17e-4de3-b87d-737e2772c849-4rpjp5u8 |
| Provider | codex |
| Provider CLI version | Unknown — no contemporaneous CLI-version evidence found in the accepted record or matching retained scratch logs. |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-06T01:38:21.976Z |
| Finished | 2026-09-06T01:39:35.868Z |
| Duration seconds | 73.893 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 88c6dcf0c834bf93f3c82e5dacba41b2a158fc75c579209e3ada639ecb8c68fc |
| Prompt template | prompt-template.txt | 2d1ad2701ed71a224e10a4ebdb9aba4ef1c65e8e999212290f06558c055a34a1 |
| Rendered prompt | prompt.txt | 43642f9915cd857986614a9321793b50d3860bb94d81877498d99d31b473f969 |
| Fixture | skills/disciplined-development/SKILL.md | 1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec |
| Fixture | skills/disciplined-development/hooks/review_nudge.py | 4c7fc6940939c0e7a148b339ac7862a0ad0980a8f8f153d0ab640dc8271363b0 |
| Fixture | skills/dispatching-development-subagents/SKILL.md | b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500 |
| Fixture | skills/superpowers/subagent-driven-development/SKILL.md | 8dd1b8e698edec3700c6d89517dbe96febd3bacd3f6ea21c1a3569c62ea104b5 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/dispatching-development-subagents/dsd-11/rubric.md | eaa14d182248e0267bef934c3307a782a14836848b453a7690df1b4a11e615df |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| DR-I1 — Shared research-before-claims rule | Explicitly require applying `disciplined-research` before factual claims in both the dispatch boundary and expected post-hook response. | FAIL | final.txt:1-17; stdout.txt | The response never names or requires `disciplined-research`. It proceeds directly to claim requirements and source citations, so neither a duplicated rule nor a shared rule establishes the required research composition. |
| DR-I3 — Dispatch-boundary mapping | Map identity, hook, gate, counter, verification, scope, commit-verification, and workflow-ownership claims to the appropriate supplied sources. | PASS | final.txt:1-15 | Every dispatch-side claim class names its support: identity and scope to the dispatch and parent skills, hook/counters to the hook module, verification and gates to the hook and parent skill, commit inspection to the dispatch skill, and task execution to the upstream skill. |
| DR-I3 — Post-hook mapping | Keep the expected response's verification, counter, gate, scope, and stop claims traceable to those same supplied sources and irreducible observed state. | PASS | final.txt:3-17 | The final requirement uses the previously mapped Gate 3, T1/T2, ownership, and disclosure rules, while limiting run-specific values to the fired conditions and observed counts. One source supports multiple claims without obscuring ownership. |
| DR-I4 — Source-boundary restraint | Avoid unsupported ownership transitions or factual claims sourced only from evaluator framing. | PASS | final.txt:1-17 | The response retains subagent/orchestrator separation and grounds methodology behavior in supplied bytes; scenario-specific landed commits and observed counters are requested as runtime facts rather than invented. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer | N/A | rubric.md | The rubric grades effective research composition and traceability while rejecting exact citation syntax, phrasing, and output shape; it defines no authenticated atomic protocol. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Requested response shape | PASS | final.txt:1-17 | The provider returns only research and support-mapping requirements without dispatching an agent or editing artifacts. |
| Read-only evaluator boundary | PASS | stdout.txt; result.json | The provider only read the four supplied fixture files. It did not edit files, mutate Git, use the network, or dispatch agents; retained evidence is empty. |
| Fixture-only execution inputs | PASS | stdout.txt; result.json | Every provider command read only files inside the declared fixture inventory; no ambient installed skill or other undeclared process input was consumed. |

## Readability

| Observation | Evidence |
|---|---|
| The claim-by-claim list is thorough and source ownership is easy to audit, though it is longer than necessary for a shared research-and-mapping contract. | final.txt:1-17 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | FAIL |
| Rationale | Claim-to-source traceability passes across both the dispatch boundary and expected post-hook response, with no unsupported ownership transition. The required composition seam fails because the response never says to apply `disciplined-research` before either artifact's factual claims. Accurate mapping alone does not demonstrate that the named research method was invoked. |
| Disposition | Accepted by owner on 2026-09-05. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None in the failure: the rubric permits one shared research rule, but the response supplies no such rule anywhere. The direct source mappings are independently strong and therefore score separately rather than masking the missing composition step. |
| Scenario defects | No blocking defect. The `disciplined-research` file itself is not supplied, so the scenario can test explicit routing to that named method but not execution of its full contents. The current core-contract charter already identifies DSD-11 research criteria as candidates for separately attributed research-composition coverage. |
| Proposed methodology changes | Preserve the distinction between invoking a research method and producing an accidentally well-sourced answer. During catalog consolidation, move this cross-skill composition seam to explicitly attributed research coverage as the charter proposes. |
