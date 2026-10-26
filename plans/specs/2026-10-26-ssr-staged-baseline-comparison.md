# SSR: original baseline and staged candidate comparison

Status: original baseline complete; candidate screen budgets remain pending.
The [framework](2026-09-11-model-driven-skill-testing-framework.md#cw-testing-model) governs the method; the [active plan](../2026-09-11-model-driven-skill-testing.md) owns progress and the [SSR protocol](../../skill-studies/sweeping-stale-references/protocol.md) owns dispatch authority.
This replaces the [55-subject completion proposal](2026-10-24-ssr-cw-aligned-validation.md); its draft configuration set does not implement this design.
Owner direction, 2026-10-26: “ok, let's create fresh baselines then” selects the current Codex/Opus baseline option below: 105 new subjects plus five matching retained Opus semantic originals, followed by eight bounded artifact reviews.
No candidate call, skill edit, retry or adoption is authorized.

## Settled comparison

The owner selected the original skill as the fixed baseline against which both rewrites are compared.
`original` is the preserved 1,182-word skill, SHA-256 `d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157`.
`candidate` remains the comprehensive rewrite; `finalist` remains the compact rewrite.
Keep all three bodies and their shared description unchanged during a comparison stage.

Establish baseline coverage across every active non-pilot scenario, rather than treating the semantic comparison as the full baseline.
The intended repetition targets are five baseline attempts and an initial three attempts per candidate for each selected case/provider cell.
Use the same scenario breadth for candidates; reduce repetitions first, rather than silently omitting cases that could expose a specific regression.
Put cases most likely to expose known weaknesses early and assess stopped attempts before continuing.
Review substantive failures as soon as they appear; do not wait for an entire candidate campaign to finish before presenting a repair/drop decision.

At the three-attempt checkpoint, compare both candidates against the original on complete outcomes, preservation, native selection and consequential passing-output quality.
Retain every observed failure and unknown; a minor reporting defect does not automatically eliminate a candidate, and three successes do not establish equivalence.
The owner can retain, drop or authorize a specific repair for each candidate.
An unchanged promising candidate can receive two additional attempts to reach five; that continuation requires a separately bounded allocation.
If a candidate changes, give it a new identity and repeat affected cases and relevant regression; earlier-version runs cannot complete its five-attempt cells.
Effectiveness leads; complete skill size breaks a supported tie.

## Existing original-skill coverage

These are valid-setup scored observations from the canonical [SSR batch records](../../skill-studies/sweeping-stale-references/protocol.md#results-and-decision), excluding the two legacy pilots and two excluded original attempts.
Counts describe observations, not passes; native task outcomes remain separate from whether the original skill actually loaded in time.
CLI/runtime strata and differences in repetitions remain explicit; adding counts does not create a uniform benchmark or a reliability estimate.

| Scenario | Codex Sol | Claude Sonnet | Claude Opus | Total |
| --- | ---: | ---: | ---: | ---: |
| discovery-shiv | 5 | 3 | 0 | 8 |
| semantic-delivery | 6 | 2 | 5 | 13 |
| moved-guide | 6 | 2 | 0 | 8 |
| initiating-change | 4 | 2 | 0 | 6 |
| local-change | 4 | 2 | 0 | 6 |
| pressure-repair | 2 | 2 | 0 | 4 |
| large-sweep-account | 2 | 0 | 0 | 2 |
| invocation-change | 2 | 2 | 2 | 6 |
| invocation-review | 2 | 3 | 2 | 7 |
| invocation-unrelated | 1 | 1 | 1 | 3 |
| invocation-verification | 0 | 0 | 0 | 0 |
| **Total** | **34** | **19** | **10** | **63** |

The original has observations for all ten established scenarios; only the new verification-only negative is wholly uncollected.
The two older original pilot runs remain separate historical evidence.
Two additional original attempts in core-baseline-01 were excluded: Shiv for invalid setup and semantic-delivery for insufficient exposure evidence.
Across all versions and controls, the direct SSR subject indexes contain 146 attempts: 67 original, 50 comprehensive, 16 compact and 13 no-target controls.
The protocol's 162-subject linked accounting projection also includes sixteen CW calls; it is not another SSR-only collection to add to these indexes.

## Selected baseline scope and later candidate allocation

Coverage across all scenarios is already broad, but it is not five baseline observations per scenario on the current Codex/Opus pair.
Preserve the historical observations as evidence; do not rerun them merely because the process changed or silently pool them with new runtime strata.
The owner selected five repetitions in every current Codex/Opus cell for a matched comparison; historical coverage stays separately labelled.
Only exact input/body/runtime matches may supply reused repetitions within a current cell.

All eleven non-pilot scenarios on both current providers give 22 cells per version.
Five original repetitions require 110 observations; the five matching Opus semantic originals leave **105 new baseline subjects**.
The initial candidate screens would need **63 new comprehensive and 52 new compact subjects**, provisionally reusing five comprehensive semantic and sixteen compact observations from the two completed compact batches.
That is **220 new subjects through the screen**; existing five-repetition candidate semantic cells stay complete rather than discarding observations to force three.
If both unchanged candidates continue, each needs 42 more subjects, for **304 new subjects overall**.
Only the 105-new-subject original baseline is selected; candidate counts remain planning estimates without dispatch allocation.
Recheck exact identities and inventories before booking reuse; relevant drift changes these counts and requires a revised scope.

The protocol fixes the two original-provider batches, eight ten-output repair-review packets, effort forecast, stopping rules and 773/58 ceilings.
Complete qualification, source freeze and collection readiness before dispatch; prepare later candidate allocations only after the baseline checkpoint.
Retain the reviewed separation of explicit application and native selection, case-specific accounting rules, trace-only non-use assessment and independent artifact review.
A native task success without timely complete skill delivery is not evidence of that version's application effectiveness.
No-target controls remain a separate contribution question, not the meaning of the original baseline.

The [completed original baseline](../../skill-studies/sweeping-stale-references/runs/fresh-baseline-01/fresh-baseline-01-assessment.md) supplies five observations in every declared case/provider cell and eight audited output reviews.
Its task outcomes, loading misses and accounting limitations remain separate; the candidate screen/review allocation is the next owner decision.
