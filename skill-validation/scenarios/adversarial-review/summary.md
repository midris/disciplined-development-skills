# Adversarial Review Scenario Audit

## Status

The scenario-by-scenario audit and first current-main observations were completed
on 2026-09-05. All 15 scenarios remain in the catalog, and no scenario contract
was repaired during this audit. The accepted set contains one judgeable
high-effort run per scenario: eight `PASS` results and seven `FAIL` results. These
observations are intended to develop the scoring method and test process, not to
measure skill effectiveness.

The audited subject was `main` at
`ac45ab2f3d467f5df0a49c543d8b3242423789b1`. The supplied
`skills/adversarial-review/SKILL.md` had SHA-256
`9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c`.
All accepted runs used Codex `gpt-5.6-sol` at high effort and completed without an
infrastructure retry. This is a human-authored audit record, not a generated
manifest.

## Scenario decisions

| Scenario | Decision | Coverage and rationale | Evidence disposition |
|---|---|---|---|
| [AR-01](ar-01/README.md) | Keep | Exercises direct review, severity, output, and composition over a complete bundle. | The [accepted observation](ar-01/accepted/worksheet.md) is a judgeable `PASS`. It identifies and locates the zero-divisor contract violation, grades it P1, blocks, and stays read-only. |
| [AR-02](ar-02/README.md) | Keep | Tests P3-only handling and separates a quoted verdict token from the operative final verdict. | The [accepted observation](ar-02/accepted/worksheet.md) is a judgeable `PASS`. It preserves the sole P3 finding and location, adds no defect, and emits the required P3-only pass verdict. |
| [AR-03](ar-03/README.md) | Keep | Requires complete caller enumeration, rationale verification, and blocking treatment of a nonlocal invariant. | The [accepted observation](ar-03/accepted/worksheet.md) is a judgeable `FAIL`. It finds the unsorted retry path and rejects the supplied rationale, but names only `retry_batch`; `validate_batch` and `bulk_normalize` are collapsed into “other call sites.” |
| [AR-04](ar-04/README.md) | Keep | Maps the always-on holistic baseline and additive specialized lenses by artifact kind. | The [accepted observation](ar-04/accepted/worksheet.md) is a judgeable `PASS`. It applies the baseline globally and selects the consistency, executability, skill-authoring, and durability lenses only where applicable. |
| [AR-05](ar-05/README.md) | Keep | Applies broad durability and holistic review without requiring one predetermined valid defect selection. | The [accepted observation](ar-05/accepted/worksheet.md) is a judgeable `FAIL`. It finds supported mutation, replay/framing, and independent holistic defects, but none requires the explicit construction- or recovery-level remedy demanded by the rubric. |
| [AR-06](ar-06/README.md) | Keep | Pressures whole-artifact review beyond the patch through absent, malformed, and out-of-scale paths. | The [accepted observation](ar-06/accepted/worksheet.md) is a judgeable `PASS`. It reaches unchanged helper behavior and explains the absent-resource, malformed-boundary, and documented large-file failures. |
| [AR-07](ar-07/README.md) | Keep | Tests whether producer ordering is treated as an unresolved construction invariant rather than assumed or documented away. | The [accepted observation](ar-07/accepted/worksheet.md) is a judgeable `PASS`. It identifies the index-zero assumption, leaves the plain-array construction boundary unresolved, and blocks without accepting a documentation- or test-only remedy. The malformed patch fixture and one ambiguous extra finding do not prevent judgment of the focused behavior. |
| [AR-08](ar-08/README.md) | Keep | Tests positive shared-cause synthesis across API, queue, and file adapters. | The [accepted observation](ar-08/accepted/worksheet.md) is a qualified judgeable `FAIL`. It reports supported defects in all three adapters but omits the required explicit shared-cause synthesis. An undeclared installed-skill read separately limits attribution to the pinned inputs. |
| [AR-10](ar-10/README.md) | Keep | Challenges unsupported duplicate state while preserving the required user-facing feature. | The [accepted observation](ar-10/accepted/worksheet.md) is a qualified judgeable `PASS`. It rejects and removes the duplicate database using the existing source-of-truth and resend contract while preserving email delivery. An undeclared installed-skill read limits attribution. |
| [AR-12](ar-12/README.md) | Keep | Tests whether activity or proxy success is rejected when it does not measure the governing outcome. | The [accepted observation](ar-12/accepted/worksheet.md) is a qualified judgeable `PASS`. It rejects wizard completion as evidence of reduced signup-to-successful-export time and requires measurement of the actual outcome. An undeclared installed-skill read limits attribution. |
| [AR-13](ar-13/README.md) | Keep | Provides the negative polarity for pattern synthesis: independently caused findings must not be assigned a generic shared cause. | The [accepted observation](ar-13/accepted/worksheet.md) is a judgeable `FAIL`. It reports both defects and invents no pattern, but it does not use the supplied provenance to state that the causes are independent; silent omission is not an evidence-backed rejection. The transcript is fixture-only. |
| [AR-14](ar-14/README.md) | Keep | Applies the skill-authoring lens while retaining the holistic baseline and angle composition. | The [accepted observation](ar-14/accepted/worksheet.md) is a judgeable `FAIL`. It catches the missing watched-pressure evidence and performs the other required review work, but does not identify the open rationalization path or missing concrete excuses and counters. The transcript is fixture-only. |
| [AR-15](ar-15/README.md) | Keep | Provides a clean bounded control in which the reviewer must not invent a blocker or shared cause. | The [accepted observation](ar-15/accepted/worksheet.md) is a qualified judgeable `PASS`. It accepts the supported display-only proposal without adding a defect, dependency, or pattern. An undeclared installed-skill read limits attribution. |
| [AR-16](ar-16/README.md) | Keep | Tests whether unchecked encoding is recognized as caller-visible termination requiring a typed failure path. | The [accepted observation](ar-16/accepted/worksheet.md) is a judgeable `FAIL`. Every focused defect criterion passes, but the run reads two installed process-instruction files outside the isolated root, violating an explicit rubric criterion. The provider-facing prompt does not state that hidden restriction. |
| [AR-17](ar-17/README.md) | Keep | Tests whether interior empty records are recognized as exact-replay corruption rather than normalized away. | The [accepted observation](ar-17/accepted/worksheet.md) is a judgeable `FAIL`. Every focused replay-defect criterion passes, but the run reads an installed process-instruction file outside the isolated root, violating an explicit rubric criterion. The provider-facing prompt does not state that hidden restriction. |

## Catalog assessment

The catalog covers all four adversarial-review charter invariants:

- AR-I1 is exercised through ordinary defect, severity, disposition, and clean-work
  behavior in AR-01, AR-02, and AR-15.
- AR-I2 is exercised through complete caller enumeration, generated absent and
  malformed cases, out-of-scale behavior, and fragile construction or replay
  invariants in AR-03, AR-05 through AR-07, AR-16, and AR-17.
- AR-I3 is exercised through rationale verification, necessity challenges, and
  rejection of activity or proxy value in AR-03, AR-10, and AR-12.
- AR-I4 is exercised through lens routing, positive and negative pattern
  synthesis, skill-authoring pressure, and clean-work restraint in AR-04, AR-08,
  and AR-13 through AR-15.

The failures expose several different seams rather than one catalog-wide weakness.
AR-03, AR-08, AR-13, and AR-14 show that pointing in the correct direction is not
enough when the contract requires explicit enumeration, synthesis, rejection, or
the complete halves of a conjunctive rule. AR-05 separates finding a durability
defect from demanding a remedy at the layer that constructs or recovers durable
state. AR-16 and AR-17 substantively identify their intended defects but fail a
separate explicit isolation criterion.

The positive and negative controls are both useful. AR-08 requires a supported
shared cause, while AR-13 requires an evidence-backed statement that superficially
similar findings are independently caused. AR-15 demonstrates one clean run in
which the reviewer does not manufacture a defect or external dependency. These
single observations establish judgeability, not repeatable effectiveness.

No authenticated deterministic checker was available for scenarios whose rubrics
refer to `DD-PATTERN` syntax. Exact marker spelling and adjacency therefore remain
`N/A`; the manual verdicts score whether the response performs or rejects semantic
pattern synthesis, not whether it satisfies an unavailable parser.

## Execution-process observation

Correct fixture packaging did not guarantee runtime read isolation. AR-08, AR-10,
AR-12, AR-15, AR-16, and AR-17 read an installed `using-superpowers` skill outside
the declared fixture inventory; AR-16 also read its `codex-tools` reference. For
AR-08, AR-10, AR-12, and AR-15, the read is recorded as a task/input-fidelity
failure that limits causal attribution without changing the independently
judgeable semantic verdict. For AR-16 and AR-17, it changes the overall verdict
because their rubrics explicitly make outside-root inspection a pass/fail
criterion.

AR-13 and AR-14 explicitly prohibit outside-root skill inspection in the
provider-facing prompt and produced fixture-only transcripts. AR-16 and AR-17 put
the same restriction only in the withheld rubric. This small sample does not prove
causation, but it identifies two process corrections needed before controlled
effectiveness comparisons: align provider-facing prompts with scored isolation
requirements, and establish a runtime read boundary or otherwise disclose and
classify undeclared inputs consistently.

## Later effectiveness campaign

Once scenario coverage and scoring methodology are stable, effectiveness testing
should use multiple independent runs for each selected model-and-effort
configuration. The intended first matrix is `gpt-5.6-sol` at high, medium, and low
effort. A later `gpt-5.6-terra` high-effort arm may help determine whether a
different model is a useful baseline subject. Repetition counts, acceptance
thresholds, aggregation, and comparison rules remain deliberately undecided;
these 15 single runs do not answer those questions.

## Next actions

1. Continue with the next skill catalog using the same scenario-by-scenario
   current-main audit and single-run process-development exercise.
2. Before controlled comparisons, align isolation instructions and scoring, and
   decide how runtime reads outside the fixture inventory will be prevented or
   classified.
3. Authenticate and supply the referenced `DD-PATTERN` checker, or remove the
   claimed deterministic contract, before exact pattern syntax is scored.
4. Do not begin rewrite comparison, model-matrix execution, or rewrite work until
   the current scenario portfolio and scoring process are sufficiently established.
