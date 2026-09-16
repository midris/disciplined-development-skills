# Core baseline: partial assessment

Format version: `1`
Assessment ID: `core-baseline-01`
Study / batch: `sweeping-stale-references` / `core-baseline-01`
Status: paused before order 6 because the Shiv subject runtime is incompatible with its supplied dependency; batch incomplete.
Scope and descriptive inclusion rules: [protocol](protocol.md#core-baseline-core-baseline-01) at Git `4b5ca0cc7aa300962ceb81a031113b7fc1410225`.
Orders 2–5 additionally apply the prospective [capture-2 amendment](protocol.md#session-evidence-amendment-capture-2) at Git `07a0baa6a4cedb36209a156d9d53c7f6d2bdba28`.
Attempt index: [core-baseline-01-run-index.json](core-baseline-01-run-index.json) at Git `b16e4f24013d85dd5fb6f8bd70de037eaa9343af`, SHA-256 `147e417223d193edb30874971cc68c56cba42e9863b458599e3b80c037041a22`.
Assessor: Codex active session with owner decisions, construction history and prior assessments available; not independent or blind validation.

## Coverage and execution results

Five of twelve planned executions were attempted and retained with complete inventories; no retry or replacement occurred. Three have valid setup. Order 1 has insufficient skill-exposure evidence; order 5 has invalid runtime setup. Both remain charged and excluded from valid-setup aggregates.
Earlier pilots and semantic-delivery-01 remain outside this batch's denominators.

| Order | Case / condition / repetition | Setup | Functional artifact outcome | Procedure |
|---:|---|---|---|---|
| [1](results/20260916T184709670Z-ssr-semantic-delivery-original-e957d242-59da-4435-8e0b-61fde0dfa606-fg7h6i02.json) | semantic-delivery / original / 1 | insufficient evidence | met | P1 met; P2 met; P3 not met |
| [2](results/20260916T204126678Z-ssr-semantic-delivery-control-0fe8996b-3cf2-48b8-920e-1672d2e0d8ac-vsj51ba0.json) | semantic-delivery / control / 1 | valid | not met | Not applicable |
| [3](results/20260916T204339538Z-ssr-pilot-02-original-5959208a-bb2d-44a8-b30a-8c3dd0e6cf04-biqxoglh.json) | moved-guide / original / 1 | valid | met | P1 met; P2 met; P3 met |
| [4](results/20260916T204533001Z-ssr-pilot-02-control-0b830a5a-18dc-4cf6-a1b0-d05f6153edd8-xpj77dfi.json) | moved-guide / control / 1 | valid | not met | Not applicable |
| [5](results/20260916T204716513Z-ssr-discovery-shiv-original-4ea35baa-b309-4e61-b7cc-7d7a0c61ae69-75y8tek9.json) | discovery-shiv / original / 1 | invalid | met | P1 met; P2 met; P3 not met |

Functional artifact outcomes are retained for excluded attempts where inspectable; they do not undo setup exclusion or enter the following valid-setup counts.
Order 5's functional checks are compatible-runtime controller replays, explicitly distinct from its failed subject-side verification.

| Case / condition | Planned | Attempted | Included | Invalid setup | Setup unresolved | Unattempted |
|---|---:|---:|---:|---:|---:|---:|
| semantic-delivery / original | 2 | 1 | 0 | 0 | 1 | 1 |
| semantic-delivery / control | 2 | 1 | 1 | 0 | 0 | 1 |
| moved-guide / original | 2 | 1 | 1 | 0 | 0 | 1 |
| moved-guide / control | 2 | 1 | 1 | 0 | 0 | 1 |
| discovery-shiv / original | 2 | 1 | 0 | 1 | 0 | 1 |
| discovery-shiv / control | 2 | 0 | 0 | 0 | 0 | 2 |

## Aggregate results

Counts below include valid-setup executions only. A zero denominator has no defined success fraction. Control procedure is descriptive, without undisclosed target requirements. F1 and F3 failures caused by the same missing repair count once at execution level.

| Case / condition / criterion | Met | Not met | Insufficient evidence | Included evidence |
|---|---:|---:|---:|---|
| semantic-delivery / original / F1 | 0 | 0 | 0 | No included execution |
| semantic-delivery / original / F2 | 0 | 0 | 0 | No included execution |
| semantic-delivery / original / F3 | 0 | 0 | 0 | No included execution |
| semantic-delivery / original / P1 | 0 | 0 | 0 | No included execution |
| semantic-delivery / original / P2 | 0 | 0 | 0 | No included execution |
| semantic-delivery / original / P3 | 0 | 0 | 0 | No included execution |
| semantic-delivery / original / functional outcome | 0 | 0 | 0 | No included execution |
| semantic-delivery / control / F1 | 0 | 1 | 0 | [2](results/20260916T204126678Z-ssr-semantic-delivery-control-0fe8996b-3cf2-48b8-920e-1672d2e0d8ac-vsj51ba0.json) |
| semantic-delivery / control / F2 | 1 | 0 | 0 | [2](results/20260916T204126678Z-ssr-semantic-delivery-control-0fe8996b-3cf2-48b8-920e-1672d2e0d8ac-vsj51ba0.json) |
| semantic-delivery / control / F3 | 0 | 1 | 0 | [2](results/20260916T204126678Z-ssr-semantic-delivery-control-0fe8996b-3cf2-48b8-920e-1672d2e0d8ac-vsj51ba0.json) |
| semantic-delivery / control / functional outcome | 0 | 1 | 0 | [2](results/20260916T204126678Z-ssr-semantic-delivery-control-0fe8996b-3cf2-48b8-920e-1672d2e0d8ac-vsj51ba0.json) |
| moved-guide / original / F1 | 1 | 0 | 0 | [3](results/20260916T204339538Z-ssr-pilot-02-original-5959208a-bb2d-44a8-b30a-8c3dd0e6cf04-biqxoglh.json) |
| moved-guide / original / F2 | 1 | 0 | 0 | [3](results/20260916T204339538Z-ssr-pilot-02-original-5959208a-bb2d-44a8-b30a-8c3dd0e6cf04-biqxoglh.json) |
| moved-guide / original / F3 | 1 | 0 | 0 | [3](results/20260916T204339538Z-ssr-pilot-02-original-5959208a-bb2d-44a8-b30a-8c3dd0e6cf04-biqxoglh.json) |
| moved-guide / original / P1 | 1 | 0 | 0 | [3](results/20260916T204339538Z-ssr-pilot-02-original-5959208a-bb2d-44a8-b30a-8c3dd0e6cf04-biqxoglh.json) |
| moved-guide / original / P2 | 1 | 0 | 0 | [3](results/20260916T204339538Z-ssr-pilot-02-original-5959208a-bb2d-44a8-b30a-8c3dd0e6cf04-biqxoglh.json) |
| moved-guide / original / P3 | 1 | 0 | 0 | [3](results/20260916T204339538Z-ssr-pilot-02-original-5959208a-bb2d-44a8-b30a-8c3dd0e6cf04-biqxoglh.json) |
| moved-guide / original / functional outcome | 1 | 0 | 0 | [3](results/20260916T204339538Z-ssr-pilot-02-original-5959208a-bb2d-44a8-b30a-8c3dd0e6cf04-biqxoglh.json) |
| moved-guide / control / F1 | 0 | 1 | 0 | [4](results/20260916T204533001Z-ssr-pilot-02-control-0b830a5a-18dc-4cf6-a1b0-d05f6153edd8-xpj77dfi.json) |
| moved-guide / control / F2 | 1 | 0 | 0 | [4](results/20260916T204533001Z-ssr-pilot-02-control-0b830a5a-18dc-4cf6-a1b0-d05f6153edd8-xpj77dfi.json) |
| moved-guide / control / F3 | 0 | 1 | 0 | [4](results/20260916T204533001Z-ssr-pilot-02-control-0b830a5a-18dc-4cf6-a1b0-d05f6153edd8-xpj77dfi.json) |
| moved-guide / control / functional outcome | 0 | 1 | 0 | [4](results/20260916T204533001Z-ssr-pilot-02-control-0b830a5a-18dc-4cf6-a1b0-d05f6153edd8-xpj77dfi.json) |
| discovery-shiv / original / F1 | 0 | 0 | 0 | No included execution |
| discovery-shiv / original / F2 | 0 | 0 | 0 | No included execution |
| discovery-shiv / original / F3 | 0 | 0 | 0 | No included execution |
| discovery-shiv / original / P1 | 0 | 0 | 0 | No included execution |
| discovery-shiv / original / P2 | 0 | 0 | 0 | No included execution |
| discovery-shiv / original / P3 | 0 | 0 | 0 | No included execution |
| discovery-shiv / original / functional outcome | 0 | 0 | 0 | No included execution |
| discovery-shiv / control / F1 | 0 | 0 | 0 | No included execution |
| discovery-shiv / control / F2 | 0 | 0 | 0 | No included execution |
| discovery-shiv / control / F3 | 0 | 0 | 0 | No included execution |
| discovery-shiv / control / functional outcome | 0 | 0 | 0 | No included execution |

## Runtime strata

Orders 2–4 are valid observations under the pre-runtime-1 shell PATH. Order 2 used Apple Python 3.9.6 for its tests; orders 3–4 used the same earlier runner configuration. Orders 6–12 will explicitly receive the restricted PATH selecting Homebrew Python 3.14.7. These remain distinct runtime strata even for non-Shiv cases: case/condition totals spanning them are descriptive mixed-configuration counts, not fixed-runtime replication. Report stratum-specific counts alongside totals; neither a repetition difference nor an original/control difference across strata establishes a skill effect. Orders 1 and 5 remain separately excluded.

## Patterns, limitations and next action

The included moved-guide original repairs all four consumers and meets all three procedural criteria; its control repairs only README. The control's retained search exposed every stale consumer before the edit, so the observed difference is repair scope after exposure, not an established discovery advantage.
The included semantic-delivery control also repairs only README. Its search exposes nearby headings but misses the differently worded stale sentences, and it explicitly narrows the task to the named defect. No included semantic original is available yet, so this batch cannot supply a paired semantic comparison.
All included executions preserve protected material. These are single observations per included case/condition, not consistency or population-reliability estimates.

The excluded first original made a complete semantic repair with a non-blocking accounting defect. The [capture diagnosis](capture-diagnosis.md) establishes how the CLI can omit a prefix delivered to the model, but that invocation's complete response is unrecoverable. Its original exclusion stands.
The excluded Shiv original repairs and commits all four commands and correctly preserves unrelated material. Its account claims ten matches where its entries total nine, and misclassifies two negative assertions under the fixed accounting rule. This is a visible non-blocking defect, not a functional failure.
Its subject-side checks fail because Python 3.9.6 cannot parse the supplied Click runtime. Compatible controller replay verifies all repaired consumers, including outside-directory script use, CLI/alias behavior, retired-option rejection and independent inventory output. That replay does not validate the subject's setup.
Preparation qualified the case under a compatible host interpreter but missed the actual Codex shell's executable selection. The [runtime diagnosis and correction](runtime-diagnosis.md) records the evidence and offline-verified explicit-PATH remedy.

Capture-2 retained complete skill responses for both resumed originals and usable action evidence for every resumed execution. The first attempt's older capture mode and the Shiv runtime fault remain explicit exclusions. Missing-guidance searches in the resumed controls/subjects found no additional guidance; the traces do not establish exhaustive host-wide isolation or an immutable model revision.
Acceptance remains descriptive and incomplete, with seven executions unattempted. No rewrite objective or adoption decision is supported by this partial batch.
Next: the owner accepted runtime-1 after review; resume orders 6–12 under its frozen authority without retries or replacements. The document generator/validator remains later work after baseline assessment and separate scope agreement.
