# Disciplined Development Scenario Audit

## Status

The scenario-by-scenario audit and first current-main observations were completed
on 2026-09-05. All nine scenarios remain in the catalog, and no scenario contract
required repair during this audit. The accepted set contains one judgeable
high-effort run per scenario: four `PASS` results and five `FAIL` results. These
observations are intended to develop the scoring method and test process, not to
measure skill effectiveness.

The audited subject was `main` at
`ac45ab2f3d467f5df0a49c543d8b3242423789b1`. The supplied
`skills/disciplined-development/SKILL.md` had SHA-256
`1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec`.
All accepted runs used Codex `gpt-5.6-sol` at high effort and completed without an
infrastructure retry. This is a human-authored audit record, not a generated
manifest.

## Scenario decisions

| Scenario | Decision | Coverage and rationale | Evidence disposition |
|---|---|---|---|
| [DD-01](dd-01/README.md) | Keep | Tests parent selection across eight modes and checkpoints while separating behavior, terminology, task shape, and companion-skill procedure. | The [accepted observation](dd-01/accepted/worksheet.md) is a judgeable `FAIL`. Rows C through G passed, but brainstorming omitted fresh source reading and owner selection, plan writing omitted the evidence/accepted-edge analysis and full planning block, and documentation editing omitted the evidence-bounded scope constraint. Task fidelity and the parent/child scoring boundary passed. |
| [DD-02](dd-02/README.md) | Keep | Tests the full Gate 1–5 chain and whether every parent artifact, owner seam, blocked transition, and invalidation rule survives one compressed workflow. | The [accepted observation](dd-02/accepted/worksheet.md) is a judgeable `FAIL`. The first three seams and the clean-review-to-PR seam passed. Whole-branch discovery and restart semantics failed because safeguard remediation did not explicitly invalidate and rerun the complete affected suffix, including fresh Gate 3 evidence and a reread of changed governing scope. |
| [DD-03](dd-03/README.md) | Keep | Isolates Principle 7's implementation threshold across reachable accepted omission, malformed representable input, and unsupported scale. | The [accepted observation](dd-03/accepted/worksheet.md) is a judgeable `PASS`. All five semantic criteria and task fidelity passed: the response handled the contract and invariant cases, recorded the speculative scale edge without implementing it, and chose only minimal actions. |
| [DD-04](dd-04/README.md) | Keep | Tests parent selection of load-bearing factual verification while reserving source selection and verification procedure for `disciplined-research`. | The [accepted observation](dd-04/accepted/worksheet.md) is a judgeable `FAIL`. Verification timing, the deployment block, the corrected target, support mapping, and task fidelity passed. The parent/companion ownership seam failed because the response performed the research behavior without assigning its procedure to the companion skill. |
| [DD-05](dd-05/README.md) | Keep | Tests fresh governing-source reads, owner resolution of a plan/spec conflict, correction of a recalled capability, and fail-closed planning and implementation transitions. | The [accepted observation](dd-05/accepted/worksheet.md) is a judgeable `FAIL`. Source reading, owner resolution, capability correction, and task fidelity passed, but the response explicitly blocked implementation without also explicitly blocking implementation planning before resolution. |
| [DD-06](dd-06/README.md) | Keep | Tests Gate 2's complete durable-scope artifact and approval boundary before implementation planning, delegation, or coding. | The [accepted observation](dd-06/accepted/worksheet.md) is a judgeable `FAIL`. The correct signed artifact and JSON spelling passed, but the XML deferral omitted the unstable-schema reason and the generic implementation block did not unambiguously include planning and delegation. Task fidelity passed. |
| [DD-07](dd-07/README.md) | Keep | Tests bounded delegation, directly observed RED before production edits, and retained parent acceptance and integration authority. | The [accepted observation](dd-07/accepted/worksheet.md) is a judgeable `PASS`. All four semantic criteria and task fidelity passed: the delegate remained inside signed scope, reports and green-only evidence could not substitute for observed RED, and downstream gates remained parent-owned. |
| [DD-08](dd-08/README.md) | Keep | Tests rejection of unsigned work before direct runtime verification, effective reference reconciliation, truthful sweep bookkeeping, and one coherent green commit. | The [accepted observation](dd-08/accepted/worksheet.md) is a judgeable `PASS`. All five semantic criteria and task fidelity passed. The response removed the unsigned rename, required real CLI evidence, reconciled all applicable surfaces, and kept the single commit blocked until the final staged tree was verified. |
| [DD-09](dd-09/README.md) | Keep | Tests whole-tree discovery immediately before PR creation, owner-authorized scope resolution, evidence restart, review boundaries, durable smoke, and branch finishing. | The [accepted observation](dd-09/accepted/worksheet.md) is a judgeable `PASS`. All five semantic criteria and task fidelity passed: the orphaned safeguard blocked progress, remediation required owner authorization, affected evidence and reviews restarted, and only the parent or user could complete Gate 5 and open the PR. |

## Catalog assessment

The catalog intentionally combines broad and focused pressure:

- DD-01 samples parent behavior across modes, while DD-02 tests whether the full
  development sequence remains coherent when compressed into one record.
- DD-05 through DD-09 isolate the same major boundaries that DD-02 composes:
  source resolution, approved written scope, test-first delegation, verified and
  reconciled commit acceptance, and whole-branch review through PR creation.
- DD-03 and DD-04 isolate two parent principles whose companion procedures must
  not be absorbed into the parent score: evidence-bounded simplicity and factual
  grounding.

Together the scenarios cover all five gates and the parent-owned portions of the
skill's principles. Gate 1 and Gate 2 receive both focused and composed coverage;
Gate 3 and Gate 4 are joined at the candidate-acceptance boundary; and Gate 5 is
tested both as an end-to-end seam and as a focused pre-PR checkpoint. DD-04 and
DD-07 make opposite ownership boundaries visible: companion methodology must be
selected without being rescored as parent behavior, while acceptance, integration,
review, smoke, finishing, and PR authority stay with the parent.

The five failures share a useful pattern. They generally point in the correct
direction but omit one part of a fail-closed contract: an owner boundary, a named
blocked transition, a rationale component, or the complete invalidated suffix of
the workflow. Correct labels and later gates do not repair those omissions. The
four passes show that the current skill can also produce precise threshold,
delegation, acceptance, and pre-PR behavior in focused scenarios.

All nine outputs passed task fidelity, and none has an authenticated deterministic
consumer. Tables, row counts, ordering, concise-record constraints, and similar
shape requirements therefore remain on the task-fidelity ledger rather than
changing the semantic verdict. DD-01 additionally demonstrates the value of a
separate advisory terminology ledger: a correct gate or principle label cannot
supply missing behavior, and a label difference need not fail equivalent behavior.

## Later effectiveness campaign

Once scenario coverage and scoring methodology are stable, effectiveness testing
should use multiple independent runs for each selected model-and-effort
configuration. The intended first matrix is `gpt-5.6-sol` at high, medium, and low
effort. A later `gpt-5.6-terra` high-effort arm may help determine whether a
different model is a useful baseline subject. Repetition counts, acceptance
thresholds, aggregation, and comparison rules remain deliberately undecided;
these nine single runs do not answer those questions.

## Next actions

1. Select the next skill catalog for the same scenario-by-scenario current-main
   audit and single-run process-development exercise.
2. Do not begin rewrite comparison, model-matrix execution, or rewrite work until
   the current scenario portfolio and scoring process are sufficiently established.
