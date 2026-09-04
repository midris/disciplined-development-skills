# Writing Explicit Rationale Scenario Audit

## Status

The scenario-by-scenario audit and first current-main observations were completed
on 2026-09-04. All six scenarios remain in the catalog, and no scenario contract
required repair during this audit. The accepted set contains one judgeable run per
scenario and is intended to develop the scoring method and test process, not to
measure skill effectiveness.

The audited subject was `main` at
`ac45ab2f3d467f5df0a49c543d8b3242423789b1`. The supplied
`skills/writing-explicit-rationale/SKILL.md` had SHA-256
`97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe`.
This is a human-authored audit record, not a generated manifest.

The first three accepted runs used Codex `gpt-5.6-sol` at low effort because that
was the catalog's inherited execution configuration. After reviewing that choice,
the owner selected Sol-high as the process-development default, and all six current
scenario configurations changed to high effort in `2e41384`. WER-06 through WER-08
therefore use high effort. The mixed-effort accepted set is valid as a record of
these manual process exercises, but its scenario outcomes are not directly
comparable and do not form an effectiveness estimate.

## Scenario decisions

| Scenario | Decision | Coverage and rationale | Evidence disposition |
|---|---|---|---|
| [WER-01](wer-01/README.md) | Keep | Tests a direct release-plan descope that must preserve selected scope, cause, accepted impact, and adjacent rationale. Exact item shape is task fidelity rather than deterministic protocol. | The [accepted low-effort observation](wer-01/accepted/worksheet.md) is a judgeable `PASS`. WER-I1, WER-I2, and task fidelity passed; WER-I3 and WER-I4 were not independently pressured. |
| [WER-02](wer-02/README.md) | Keep | Tests whether repeated review triggers a batched audit across consequential decisions and a consequence-free choice while retaining one rationale home. | The [accepted low-effort observation](wer-02/accepted/worksheet.md) is a judgeable `FAIL`. WER-I1, WER-I2, WER-I4, and task fidelity passed. WER-I3 failed because the response proposed complete rationale copies in both interactive handlers instead of one authoritative home and a reference from the other. |
| [WER-05](wer-05/README.md) | Keep | Tests reference-not-repeat behavior when a complete authoritative rationale already exists and the user asks for duplication in code and a commit message. | The [accepted low-effort observation](wer-05/accepted/worksheet.md) is a judgeable `FAIL`. WER-I1 and task fidelity passed. WER-I2 and WER-I3 failed because neither returned block referenced the architecture section and both reproduced its complete explanation. WER-I4 was not independently pressured. |
| [WER-06](wer-06/README.md) | Keep | Tests retaining only historical context that constrains current correctness: exact serialized bytes govern signature verification, while the migration year and implementation language do not. | The [accepted high-effort observation](wer-06/accepted/worksheet.md) is a judgeable `PASS`. WER-I1, WER-I2, and task fidelity passed; WER-I3 and WER-I4 were not independently pressured. |
| [WER-07](wer-07/README.md) | Keep | Tests WER-owned rationale behavior alongside separately owned research, lean-plan, and parent-development composition. The telemetry choice must remain an arbitrary tie-break rather than gain an invented preference. | The [accepted high-effort observation](wer-07/accepted/worksheet.md) has a judgeable WER `PASS` and a separate composition-owner `PASS`. WER-I1, WER-I2, source acquisition and mapping, plan-table completeness, proportionality, and task fidelity passed. WER-I3 and WER-I4 were not independently pressured. |
| [WER-08](wer-08/README.md) | Keep | Tests the broad-domain boundary by moving a repeatedly requested cause from chat into the durable nonprofit policy rather than minutes or a newsletter. | The [accepted high-effort observation](wer-08/accepted/worksheet.md) is a judgeable `PASS`. WER-I1 through WER-I3 and task fidelity passed; WER-I4 was not independently pressured. The response unnecessarily repeated existing controls and added acceptance framing, recorded as a non-blocking task-fidelity observation under the rubric. |

## Catalog assessment

The apparent overlaps preserve distinct rationale boundaries:

- WER-01, WER-06, and WER-08 exercise rationale in a plan item, a code comment,
  and a non-software policy.
- WER-02 and WER-05 distinguish creating missing durable rationale after repeated
  review from referencing rationale that already has an authoritative home.
- WER-07 tests composition while keeping the WER owner verdict separate from the
  research, lean-plan, and parent-development verdict.

Together the scenarios exercise all four charter invariants. WER-I1 and WER-I2
have broad positive coverage. WER-I3 is directly pressured by WER-02, WER-05, and
WER-08; the two code-and-document cases produced judgeable failures while the
non-software authoritative-home case passed. WER-I4 is directly exercised only by
WER-02, which successfully triggered a batched audit but failed the independent
single-home invariant. That one-scenario boundary should remain visible when later
effectiveness evidence is interpreted.

WER-07's rubric requires two owner ledgers. Its worksheet therefore adds a manual
composition-owner section rather than blending child behavior into the WER verdict.
Future multi-owner scenarios should follow that pattern; the generic worksheet
generator does not need to change during this manual process-development pass.

None of the scenarios has an authenticated deterministic consumer. Markdown tables,
line counts, required columns, comment syntax, response-only constraints, and similar
shape requirements remain task fidelity. Non-material surplus can be recorded as a
task-fidelity observation without changing an owning semantic verdict when the
scenario rubric explicitly establishes that boundary.

## Later effectiveness campaign

Once scenario coverage and scoring methodology are stable, effectiveness testing
should use multiple independent runs for each selected model-and-effort configuration.
The intended first matrix is `gpt-5.6-sol` at high, medium, and low effort. A later
`gpt-5.6-terra` high-effort arm may help determine whether a different model is a
useful baseline subject. Repetition counts, acceptance thresholds, aggregation, and
comparison rules remain deliberately undecided; these six single runs do not answer
those questions.

## Next actions

1. Select the next skill catalog for the same scenario-by-scenario current-main
   audit and single-run process-development exercise.
2. Do not begin rewrite comparison, model-matrix execution, or rewrite work until
   the current scenario portfolio and scoring process are sufficiently established.
