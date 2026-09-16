# Core baseline: batch assessment

Format version: `1`
Assessment ID: `core-baseline-01`
Study / batch: `sweeping-stale-references` / `core-baseline-01`
Status: all twelve authorized attempts collected and assessed; descriptive baseline complete with two setup exclusions.
Scope and inclusion rules: [protocol](protocol.md#core-baseline-core-baseline-01) at Git `4b5ca0cc7aa300962ceb81a031113b7fc1410225`.
Orders 2–5 apply [capture-2](protocol.md#session-evidence-amendment-capture-2) at Git `07a0baa6a4cedb36209a156d9d53c7f6d2bdba28`.
Orders 6–12 apply capture-2 plus [runtime-1](protocol.md#runtime-amendment-runtime-1) at Git `b16e4f24013d85dd5fb6f8bd70de037eaa9343af`.
Attempt index: [core-baseline-01-run-index.json](core-baseline-01-run-index.json) at Git `158839a0893e12bab2439224713a2400e46dea94`, SHA-256 `7055925db040f3a2e66baab9d07917c419e65a4163e752df332517dcf4c47004`.
Assessor: Codex active session with owner decisions, construction history and prior assessments available; not independent or blind validation.

## Coverage and execution results

All twelve planned executions were attempted and retained with complete inventories; no retry or replacement occurred. Ten have valid setup. Order 1 has insufficient skill-exposure evidence; order 5 has invalid runtime setup. Both remain charged and excluded from valid-setup aggregates.
Earlier pilots and semantic-delivery-01 remain outside this batch's denominators. Call and time accounting belong to the [protocol](protocol.md#storage-and-accounting).

| Order | Case / condition / repetition | Setup | Functional artifact outcome | Procedure |
|---:|---|---|---|---|
| [1](results/20260916T184709670Z-ssr-semantic-delivery-original-e957d242-59da-4435-8e0b-61fde0dfa606-fg7h6i02.json) | semantic-delivery / original / 1 | insufficient evidence | met | P1 met; P2 met; P3 not met |
| [2](results/20260916T204126678Z-ssr-semantic-delivery-control-0fe8996b-3cf2-48b8-920e-1672d2e0d8ac-vsj51ba0.json) | semantic-delivery / control / 1 | valid | not met | Not applicable |
| [3](results/20260916T204339538Z-ssr-pilot-02-original-5959208a-bb2d-44a8-b30a-8c3dd0e6cf04-biqxoglh.json) | moved-guide / original / 1 | valid | met | P1 met; P2 met; P3 met |
| [4](results/20260916T204533001Z-ssr-pilot-02-control-0b830a5a-18dc-4cf6-a1b0-d05f6153edd8-xpj77dfi.json) | moved-guide / control / 1 | valid | not met | Not applicable |
| [5](results/20260916T204716513Z-ssr-discovery-shiv-original-4ea35baa-b309-4e61-b7cc-7d7a0c61ae69-75y8tek9.json) | discovery-shiv / original / 1 | invalid | met | P1 met; P2 met; P3 not met |
| [6](results/20260916T211426933Z-ssr-discovery-shiv-control-b3dadb31-1aba-4780-a9fc-85907563b12e-ijmz6xm4.json) | discovery-shiv / control / 1 | valid | not met | Not applicable |
| [7](results/20260916T211634145Z-ssr-semantic-delivery-control-c2aab754-bf96-4e4d-9857-48bf7d1134c3-2pmsvp21.json) | semantic-delivery / control / 2 | valid | not met | Not applicable |
| [8](results/20260916T212056768Z-ssr-semantic-delivery-original-70c5ee60-ccdf-4d90-9892-d6d48f377aed-x3y26xvg.json) | semantic-delivery / original / 2 | valid | met | P1 met; P2 met; P3 not met |
| [9](results/20260916T212335423Z-ssr-pilot-02-control-3b771a16-a2c4-4a5b-9004-f81c7e4eddab-ds6p3tlh.json) | moved-guide / control / 2 | valid | not met | Not applicable |
| [10](results/20260916T212458466Z-ssr-pilot-02-original-61c309cf-8839-4a59-ae5d-598c15ebc2d8-js5_fmmw.json) | moved-guide / original / 2 | valid | met | P1 met; P2 met; P3 not met |
| [11](results/20260916T212735036Z-ssr-discovery-shiv-control-db99edf4-0944-4645-84c7-ece8cfaf847c-iw28zhnz.json) | discovery-shiv / control / 2 | valid | not met | Not applicable |
| [12](results/20260916T212924988Z-ssr-discovery-shiv-original-1cb8ac19-08e0-4462-81be-8adc8fa6452b-fhhj0y2r.json) | discovery-shiv / original / 2 | valid | met | P1 met; P2 met; P3 not met |

Functional artifact outcomes remain recorded for excluded attempts where inspectable; they do not undo setup exclusion or enter valid-setup counts. Order 5's functional checks are compatible-runtime controller replays, distinct from its failed subject-side verification.

| Case / condition | Planned | Attempted | Included | Invalid setup | Setup unresolved | Unattempted |
|---|---:|---:|---:|---:|---:|---:|
| semantic-delivery / original | 2 | 2 | 1 | 0 | 1 | 0 |
| semantic-delivery / control | 2 | 2 | 2 | 0 | 0 | 0 |
| moved-guide / original | 2 | 2 | 2 | 0 | 0 | 0 |
| moved-guide / control | 2 | 2 | 2 | 0 | 0 | 0 |
| discovery-shiv / original | 2 | 2 | 1 | 1 | 0 | 0 |
| discovery-shiv / control | 2 | 2 | 2 | 0 | 0 | 0 |

## Aggregate results

Each count cell is **met / not met / insufficient evidence**, not a quality scale. Counts include valid-setup executions only; `0 / 0 / 0` has no defined success fraction. F1 and F3 failures from the same missing repair count once in the functional outcome. Control procedure is descriptive, without undisclosed target requirements.

Earlier PATH includes orders 2–4 under the pre-runtime-1 configuration; order 2 used Apple Python 3.9.6. Runtime-1 includes orders 6–12 with the explicit restricted PATH selecting Homebrew Python 3.14.7. Combined counts spanning these strata are descriptive mixed-configuration observations, not fixed-runtime replication. Do not attribute a difference across strata to the skill. The model/effort and frozen case inputs remained unchanged; no immutable model revision is available.

| Case / condition / criterion | Combined M/N/U | Earlier PATH M/N/U | Runtime-1 M/N/U | Included evidence |
|---|---:|---:|---:|---|
| semantic-delivery / original / F1 | 1 / 0 / 0 | 0 / 0 / 0 | 1 / 0 / 0 | [8](results/20260916T212056768Z-ssr-semantic-delivery-original-70c5ee60-ccdf-4d90-9892-d6d48f377aed-x3y26xvg.json) |
| semantic-delivery / original / F2 | 1 / 0 / 0 | 0 / 0 / 0 | 1 / 0 / 0 | [8](results/20260916T212056768Z-ssr-semantic-delivery-original-70c5ee60-ccdf-4d90-9892-d6d48f377aed-x3y26xvg.json) |
| semantic-delivery / original / F3 | 1 / 0 / 0 | 0 / 0 / 0 | 1 / 0 / 0 | [8](results/20260916T212056768Z-ssr-semantic-delivery-original-70c5ee60-ccdf-4d90-9892-d6d48f377aed-x3y26xvg.json) |
| semantic-delivery / original / P1 | 1 / 0 / 0 | 0 / 0 / 0 | 1 / 0 / 0 | [8](results/20260916T212056768Z-ssr-semantic-delivery-original-70c5ee60-ccdf-4d90-9892-d6d48f377aed-x3y26xvg.json) |
| semantic-delivery / original / P2 | 1 / 0 / 0 | 0 / 0 / 0 | 1 / 0 / 0 | [8](results/20260916T212056768Z-ssr-semantic-delivery-original-70c5ee60-ccdf-4d90-9892-d6d48f377aed-x3y26xvg.json) |
| semantic-delivery / original / P3 | 0 / 1 / 0 | 0 / 0 / 0 | 0 / 1 / 0 | [8](results/20260916T212056768Z-ssr-semantic-delivery-original-70c5ee60-ccdf-4d90-9892-d6d48f377aed-x3y26xvg.json) |
| semantic-delivery / original / functional outcome | 1 / 0 / 0 | 0 / 0 / 0 | 1 / 0 / 0 | [8](results/20260916T212056768Z-ssr-semantic-delivery-original-70c5ee60-ccdf-4d90-9892-d6d48f377aed-x3y26xvg.json) |
| semantic-delivery / control / F1 | 0 / 2 / 0 | 0 / 1 / 0 | 0 / 1 / 0 | [2](results/20260916T204126678Z-ssr-semantic-delivery-control-0fe8996b-3cf2-48b8-920e-1672d2e0d8ac-vsj51ba0.json), [7](results/20260916T211634145Z-ssr-semantic-delivery-control-c2aab754-bf96-4e4d-9857-48bf7d1134c3-2pmsvp21.json) |
| semantic-delivery / control / F2 | 2 / 0 / 0 | 1 / 0 / 0 | 1 / 0 / 0 | [2](results/20260916T204126678Z-ssr-semantic-delivery-control-0fe8996b-3cf2-48b8-920e-1672d2e0d8ac-vsj51ba0.json), [7](results/20260916T211634145Z-ssr-semantic-delivery-control-c2aab754-bf96-4e4d-9857-48bf7d1134c3-2pmsvp21.json) |
| semantic-delivery / control / F3 | 0 / 2 / 0 | 0 / 1 / 0 | 0 / 1 / 0 | [2](results/20260916T204126678Z-ssr-semantic-delivery-control-0fe8996b-3cf2-48b8-920e-1672d2e0d8ac-vsj51ba0.json), [7](results/20260916T211634145Z-ssr-semantic-delivery-control-c2aab754-bf96-4e4d-9857-48bf7d1134c3-2pmsvp21.json) |
| semantic-delivery / control / functional outcome | 0 / 2 / 0 | 0 / 1 / 0 | 0 / 1 / 0 | [2](results/20260916T204126678Z-ssr-semantic-delivery-control-0fe8996b-3cf2-48b8-920e-1672d2e0d8ac-vsj51ba0.json), [7](results/20260916T211634145Z-ssr-semantic-delivery-control-c2aab754-bf96-4e4d-9857-48bf7d1134c3-2pmsvp21.json) |
| moved-guide / original / F1 | 2 / 0 / 0 | 1 / 0 / 0 | 1 / 0 / 0 | [3](results/20260916T204339538Z-ssr-pilot-02-original-5959208a-bb2d-44a8-b30a-8c3dd0e6cf04-biqxoglh.json), [10](results/20260916T212458466Z-ssr-pilot-02-original-61c309cf-8839-4a59-ae5d-598c15ebc2d8-js5_fmmw.json) |
| moved-guide / original / F2 | 2 / 0 / 0 | 1 / 0 / 0 | 1 / 0 / 0 | [3](results/20260916T204339538Z-ssr-pilot-02-original-5959208a-bb2d-44a8-b30a-8c3dd0e6cf04-biqxoglh.json), [10](results/20260916T212458466Z-ssr-pilot-02-original-61c309cf-8839-4a59-ae5d-598c15ebc2d8-js5_fmmw.json) |
| moved-guide / original / F3 | 2 / 0 / 0 | 1 / 0 / 0 | 1 / 0 / 0 | [3](results/20260916T204339538Z-ssr-pilot-02-original-5959208a-bb2d-44a8-b30a-8c3dd0e6cf04-biqxoglh.json), [10](results/20260916T212458466Z-ssr-pilot-02-original-61c309cf-8839-4a59-ae5d-598c15ebc2d8-js5_fmmw.json) |
| moved-guide / original / P1 | 2 / 0 / 0 | 1 / 0 / 0 | 1 / 0 / 0 | [3](results/20260916T204339538Z-ssr-pilot-02-original-5959208a-bb2d-44a8-b30a-8c3dd0e6cf04-biqxoglh.json), [10](results/20260916T212458466Z-ssr-pilot-02-original-61c309cf-8839-4a59-ae5d-598c15ebc2d8-js5_fmmw.json) |
| moved-guide / original / P2 | 2 / 0 / 0 | 1 / 0 / 0 | 1 / 0 / 0 | [3](results/20260916T204339538Z-ssr-pilot-02-original-5959208a-bb2d-44a8-b30a-8c3dd0e6cf04-biqxoglh.json), [10](results/20260916T212458466Z-ssr-pilot-02-original-61c309cf-8839-4a59-ae5d-598c15ebc2d8-js5_fmmw.json) |
| moved-guide / original / P3 | 1 / 1 / 0 | 1 / 0 / 0 | 0 / 1 / 0 | [3](results/20260916T204339538Z-ssr-pilot-02-original-5959208a-bb2d-44a8-b30a-8c3dd0e6cf04-biqxoglh.json), [10](results/20260916T212458466Z-ssr-pilot-02-original-61c309cf-8839-4a59-ae5d-598c15ebc2d8-js5_fmmw.json) |
| moved-guide / original / functional outcome | 2 / 0 / 0 | 1 / 0 / 0 | 1 / 0 / 0 | [3](results/20260916T204339538Z-ssr-pilot-02-original-5959208a-bb2d-44a8-b30a-8c3dd0e6cf04-biqxoglh.json), [10](results/20260916T212458466Z-ssr-pilot-02-original-61c309cf-8839-4a59-ae5d-598c15ebc2d8-js5_fmmw.json) |
| moved-guide / control / F1 | 0 / 2 / 0 | 0 / 1 / 0 | 0 / 1 / 0 | [4](results/20260916T204533001Z-ssr-pilot-02-control-0b830a5a-18dc-4cf6-a1b0-d05f6153edd8-xpj77dfi.json), [9](results/20260916T212335423Z-ssr-pilot-02-control-3b771a16-a2c4-4a5b-9004-f81c7e4eddab-ds6p3tlh.json) |
| moved-guide / control / F2 | 2 / 0 / 0 | 1 / 0 / 0 | 1 / 0 / 0 | [4](results/20260916T204533001Z-ssr-pilot-02-control-0b830a5a-18dc-4cf6-a1b0-d05f6153edd8-xpj77dfi.json), [9](results/20260916T212335423Z-ssr-pilot-02-control-3b771a16-a2c4-4a5b-9004-f81c7e4eddab-ds6p3tlh.json) |
| moved-guide / control / F3 | 0 / 2 / 0 | 0 / 1 / 0 | 0 / 1 / 0 | [4](results/20260916T204533001Z-ssr-pilot-02-control-0b830a5a-18dc-4cf6-a1b0-d05f6153edd8-xpj77dfi.json), [9](results/20260916T212335423Z-ssr-pilot-02-control-3b771a16-a2c4-4a5b-9004-f81c7e4eddab-ds6p3tlh.json) |
| moved-guide / control / functional outcome | 0 / 2 / 0 | 0 / 1 / 0 | 0 / 1 / 0 | [4](results/20260916T204533001Z-ssr-pilot-02-control-0b830a5a-18dc-4cf6-a1b0-d05f6153edd8-xpj77dfi.json), [9](results/20260916T212335423Z-ssr-pilot-02-control-3b771a16-a2c4-4a5b-9004-f81c7e4eddab-ds6p3tlh.json) |
| discovery-shiv / original / F1 | 1 / 0 / 0 | 0 / 0 / 0 | 1 / 0 / 0 | [12](results/20260916T212924988Z-ssr-discovery-shiv-original-1cb8ac19-08e0-4462-81be-8adc8fa6452b-fhhj0y2r.json) |
| discovery-shiv / original / F2 | 1 / 0 / 0 | 0 / 0 / 0 | 1 / 0 / 0 | [12](results/20260916T212924988Z-ssr-discovery-shiv-original-1cb8ac19-08e0-4462-81be-8adc8fa6452b-fhhj0y2r.json) |
| discovery-shiv / original / F3 | 1 / 0 / 0 | 0 / 0 / 0 | 1 / 0 / 0 | [12](results/20260916T212924988Z-ssr-discovery-shiv-original-1cb8ac19-08e0-4462-81be-8adc8fa6452b-fhhj0y2r.json) |
| discovery-shiv / original / P1 | 1 / 0 / 0 | 0 / 0 / 0 | 1 / 0 / 0 | [12](results/20260916T212924988Z-ssr-discovery-shiv-original-1cb8ac19-08e0-4462-81be-8adc8fa6452b-fhhj0y2r.json) |
| discovery-shiv / original / P2 | 1 / 0 / 0 | 0 / 0 / 0 | 1 / 0 / 0 | [12](results/20260916T212924988Z-ssr-discovery-shiv-original-1cb8ac19-08e0-4462-81be-8adc8fa6452b-fhhj0y2r.json) |
| discovery-shiv / original / P3 | 0 / 1 / 0 | 0 / 0 / 0 | 0 / 1 / 0 | [12](results/20260916T212924988Z-ssr-discovery-shiv-original-1cb8ac19-08e0-4462-81be-8adc8fa6452b-fhhj0y2r.json) |
| discovery-shiv / original / functional outcome | 1 / 0 / 0 | 0 / 0 / 0 | 1 / 0 / 0 | [12](results/20260916T212924988Z-ssr-discovery-shiv-original-1cb8ac19-08e0-4462-81be-8adc8fa6452b-fhhj0y2r.json) |
| discovery-shiv / control / F1 | 0 / 2 / 0 | 0 / 0 / 0 | 0 / 2 / 0 | [6](results/20260916T211426933Z-ssr-discovery-shiv-control-b3dadb31-1aba-4780-a9fc-85907563b12e-ijmz6xm4.json), [11](results/20260916T212735036Z-ssr-discovery-shiv-control-db99edf4-0944-4645-84c7-ece8cfaf847c-iw28zhnz.json) |
| discovery-shiv / control / F2 | 2 / 0 / 0 | 0 / 0 / 0 | 2 / 0 / 0 | [6](results/20260916T211426933Z-ssr-discovery-shiv-control-b3dadb31-1aba-4780-a9fc-85907563b12e-ijmz6xm4.json), [11](results/20260916T212735036Z-ssr-discovery-shiv-control-db99edf4-0944-4645-84c7-ece8cfaf847c-iw28zhnz.json) |
| discovery-shiv / control / F3 | 0 / 2 / 0 | 0 / 0 / 0 | 0 / 2 / 0 | [6](results/20260916T211426933Z-ssr-discovery-shiv-control-b3dadb31-1aba-4780-a9fc-85907563b12e-ijmz6xm4.json), [11](results/20260916T212735036Z-ssr-discovery-shiv-control-db99edf4-0944-4645-84c7-ece8cfaf847c-iw28zhnz.json) |
| discovery-shiv / control / functional outcome | 0 / 2 / 0 | 0 / 0 / 0 | 0 / 2 / 0 | [6](results/20260916T211426933Z-ssr-discovery-shiv-control-b3dadb31-1aba-4780-a9fc-85907563b12e-ijmz6xm4.json), [11](results/20260916T212735036Z-ssr-discovery-shiv-control-db99edf4-0944-4645-84c7-ece8cfaf847c-iw28zhnz.json) |

## Patterns, limitations and next action

Across the included observations, originals complete the functional repair in 4/4 executions; controls do so in 0/6. These pooled totals summarize different cases and runtimes; the case/criterion/runtime counts above are the comparison evidence. All ten included executions preserve protected behavior and meaning. Each control fails F1 and F3 for the same missing repairs, so six failed executions remain six failures.

The repeated control outcome is README-only repair. Both moved-guide controls (orders 4 and 9) expose all four stale consumers before editing. Semantic control 7 reads all three stale guides in full, whereas control 2's search misses the differently worded stale sentences. Shiv control 11 exposes all four stale commands; control 6 exposes README, script and CI, but not the nested Make command. Thus the evidence chiefly supports a repair-scope difference after content exposure. It does not establish a general discovery advantage or show what the model internally attended to. Successful interface/behavior tests in the controls do not establish complete documentation or consumer repair.

Originals meet P1 and P2 in all four included observations. P3 is met in 1/4: order 3's moved-guide account is accurate; order 8 counts search lines and excluded facts instead of semantic blocks and reports an inconsistent total; order 10 reports eight paths for seven distinct paths; order 12 mislabels two negative assertions as intentionally stale rather than false positives. These account defects remain non-blocking and do not change the functional results. The case-specific counting rules differ: accurate optional broad-search entries are permitted for moved-guide, while semantic-delivery and Shiv explicitly exclude specified incidental/current facts.

Orders 1 and 5 retain inspectable complete artifact repairs and account defects, but contribute to no valid-setup denominator. Order 1 lacks recoverable complete skill-response evidence; [capture diagnosis](capture-diagnosis.md) does not reconstruct that lost response. Order 5 used incompatible Python 3.9.6; compatible controller replay establishes artifact behavior, not valid subject setup. Capture-2 retained the full frozen skill responses for all later originals, and runtime-1 supplied a usable runtime to all seven resumed executions. The [runtime diagnosis](runtime-diagnosis.md) records the correction and the earlier-runtime limitation.

This is an exposed, small, descriptive baseline, with only one included semantic original and one included Shiv original. Runtime-specific repetition is still smaller; there is no reliability estimate, fixed success threshold, held-out validation, immutable model revision or exhaustive host-isolation claim. Shiv observations execute local consumers, including the CI build command; they do not establish hosted CI or the full upstream suite. No explicit remembered-upstream/API claim was observed in the resumed Shiv executions; that does not prove absence of prior familiarity. Justified-local-change coverage remains deferred.

The declared descriptive-only scope is complete, not an adoption test. The useful reconciliation behavior is supported in these cases; a broad functional rewrite is not indicated by this batch. The concrete improvement opportunity is a smaller, more reliable audit account that preserves complete reconciliation. Any such edit needs an agreed objective and fixed comparison scope; no rewrite or additional execution follows automatically.

Next: review these findings with the owner, then agree the planned document generator/validator's bounded CLI, scope and implementation/qualification effort before coding. Retain the original skill meanwhile. The protocol owns the resulting decisions and remaining capacity.
