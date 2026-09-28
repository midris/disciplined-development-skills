# Claude native CW third repetition: assessment

Format version: `2`
Assessment ID: cw-claude-invocation-02
Study / batch: concise-writing / claude-invocation-02
Status: complete; all eight authorized third repetitions retained and assessed
Scope and acceptance rules: [protocol](protocol.md) at Git `d944aa7df0c1e4fc99e3c5e887fdea64bd4a2636`, batch claude-invocation-02; unchanged CW-expanded-1 and the four native case cards.
Attempt index: [claude-invocation-02-run-index.json](claude-invocation-02-run-index.json) at Git `8bfab1c0552ea64a0ee2d2bc35733dde986887ea`, SHA-256 `0d9e4d8a31f24f6563b354d867fa0ede28fbc61544b09ac617e664d44e668b34`.
Assessor and relevant session context: active Codex session that prepared and inspected these exposed development cases; not independent, blind or held out.

## Coverage and execution results

This batch adds repetition 3 to the [first two repetitions](claude-invocation-01-assessment.md), without changing their records or scores.
Every provider/case/version cell received its scheduled observation regardless of prior results.
The schedule reverses the second rotation and matches the first; three repetitions cannot fully balance two-condition order.
All eight setups are valid, with no retries, replacements, exclusions, unresolved judgments or unattempted slots.
Only the assigned description is initially available; native tasks do not request loading CW.
Full-body delivery before first task writing determines positive selection, independently of F1–F3.
N3 tests non-selection only; numeric correctness is descriptive, with no functional CW outcome.
Models and skill bytes match the earlier qualified batches; the third repetitions were collected later, rather than prospectively interleaved with them.
Original and rewrite descriptions differ, so these whole-version comparisons cannot isolate description and body effects.
No immutable backend model revision is available.

| Case | Original timely/appropriate selection | Rewrite timely/appropriate selection | Original functional | Rewrite functional |
| --- | --- | --- | --- | --- |
| N1: tightening | 1/1 | 1/1 | 1/1 | 1/1 |
| N2: new update | 0/1 | 1/1 | 0/1 | 1/1 |
| N3: numeric only | 1/1 avoided loading | 1/1 avoided loading | Not measured | Not measured |
| N4: code comments | 0/1 | 0/1 | 1/1 | 1/1 |

## Aggregate results

original: timely positive selection 1/3; functional outcomes 2/3.
candidate-comprehensive: timely positive selection 2/3; functional outcomes 3/3.
These small exposed-case counts are diagnostic, not reliability estimates or an adoption decision.
The [protocol](protocol.md#results-and-decision) reports the combined three-repetition evidence, keeping provider and native/explicit-load strata separate.

## Interpretation and limitations

Claude CLI 2.1.283 ran claude-sonnet-5, with low effort requested through the runner, workspace-write and a 900-second timeout.
Init and assistant events confirm the CLI/model; effort is recorded in runner settings, not independently exposed by init.
Executable SHA-256 is `d8cb1e5c79684cc12a8bfc813e3a2073406921b6245744b3009be3ab5651d21e`.
The catalog contains CW plus deep-research, dataviz, update-config, verify, debug, code-review, simplify, batch, fewer-permission-prompts, doctor, loop, schedule, claude-api, workflow-authoring, run and run-skill-generator.

Timely loads occur in N1 original/rewrite and N2 rewrite.
N2 original and both N4 runs never load CW; there are no partial or late loads.
Both N3 runs avoid loading and make the exact numeric edit.
Their final.txt files say Done., but both traces contain extra pre-edit status messages; the entire visible response therefore violates the Done-only request.
That task-compliance observation is unscored for CW functionality and does not turn appropriate non-selection into a failure.
The original numeric run lists the skill path and attempts to cat its directory; the returned content contains no CW body.

Both N1 outputs preserve the complete bounded decision and remove the detached implementation repeat and filler.
Useful staging qualifications and action reminders remain; their contextual role distinguishes them from purposeless repetition.
N2 rewrite is faithful and actionable, with no unsupported production-scale validation claim.
N2 original adds “reliable at staging scale and handles interruption correctly” to the supplied sixty jobs and two recoveries.
That conclusion generalizes finite observations into a broader reliability claim; explicit production limits do not confine interruption correctness to the two observed recoveries.
F1 fails; F2 remains met because the three-workspace limit, approval, both-person staffing, investigation and separate expansion decision remain actionable.
The staffing fallback names Ali, but also requires both people to be present; it does not license starting without Bea.
No new criterion or sentence-matching requirement is imposed.

Both N4 outputs provide correct retry/acknowledgement boundaries and the double-upload rationale despite missing the skill load.
Both pass controller parse/token comparison without executing subject code.
Comments reinforce the exhaustion and acknowledgement traps at their relevant code sites; added explanation does not fail on length alone.

| Case / version | Source words | Third output words | Interpretation |
| --- | ---: | ---: | --- |
| N1 original | 625 | 324 | Shorter; F1–F3 preserved |
| N1 rewrite | 625 | 300 | Shorter; F1–F3 preserved |
| N2 original | 199 | 255 | Unsupported reliability claim; F1 fails |
| N2 rewrite | 199 | 198 | Faithful generation; length descriptive |
| N4 original | 20 | 68 | Comment words excluding markers; useful added explanation |
| N4 rewrite | 20 | 70 | Comment words excluding markers; useful added explanation |

All eight inventories, twenty protected-input comparisons and complete structured results verify.
Raw artifacts were read without running Git in retained bundles.
Runner duration totals 171.913 seconds, included once in the estimated active minutes booked in the protocol.
[Runtime qualification](preparation/runtime-qualification.md) and the [supplemental review](../../reviews/2026-09-27-cw-native-third-review.md) retain qualification and verification evidence.
O4 remains unscored; no qualifying O5 uncertainty is established.
Response-only applicability, full orchestration and instruction-level causal effects remain untested.

## Mechanical tables and evidence

Generated tables only; judgments and conclusions remain with the assessor.

| Case / condition | Planned | Attempted | Included | Invalid setup | Setup unresolved | Unattempted |
| --- | --- | --- | --- | --- | --- | --- |
| invocation-tighten / original | 1 | 1 | 1 | 0 | 0 | 0 |
| invocation-tighten / candidate-comprehensive | 1 | 1 | 1 | 0 | 0 | 0 |
| invocation-write / candidate-comprehensive | 1 | 1 | 1 | 0 | 0 | 0 |
| invocation-write / original | 1 | 1 | 1 | 0 | 0 | 0 |
| invocation-nonprose / original | 1 | 1 | 1 | 0 | 0 | 0 |
| invocation-nonprose / candidate-comprehensive | 1 | 1 | 1 | 0 | 0 | 0 |
| invocation-comments / candidate-comprehensive | 1 | 1 | 1 | 0 | 0 | 0 |
| invocation-comments / original | 1 | 1 | 1 | 0 | 0 | 0 |

| Order | Case | Condition | Repetition | Setup / coverage | Recorded outcome | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | invocation-tighten | original | 3 | valid | met | [claude-invocation-02-invocation-tighten-original-3](results/20260928T011757062Z-cw-prep-claude-invocation-tighten-original-8872c4a0-80fa-4521-86ff-1ef185c98e11-6h0dva0a.json) |
| 2 | invocation-tighten | candidate-comprehensive | 3 | valid | met | [claude-invocation-02-invocation-tighten-candidate-comprehensive-3](results/20260928T011843805Z-cw-prep-claude-invocation-tighten-candidate-a7611382-b798-468b-bfff-dda335a5e3a7-ym6suo4n.json) |
| 3 | invocation-write | candidate-comprehensive | 3 | valid | met | [claude-invocation-02-invocation-write-candidate-comprehensive-3](results/20260928T011938667Z-cw-prep-claude-invocation-write-candidate-ee32f2ff-47b7-42b5-b2a2-c9ac8ba4f87f-kyfcwulb.json) |
| 4 | invocation-write | original | 3 | valid | not met | [claude-invocation-02-invocation-write-original-3](results/20260928T012104354Z-cw-prep-claude-invocation-write-original-10ea5c1c-6ed8-4eeb-960b-5ad34ef8ad2e-gx77xlvv.json) |
| 5 | invocation-nonprose | original | 3 | valid | not measured | [claude-invocation-02-invocation-nonprose-original-3](results/20260928T012208212Z-cw-prep-claude-invocation-nonprose-original-18f874de-b271-48a5-b5f8-498cc980b76e-xst9nmcl.json) |
| 6 | invocation-nonprose | candidate-comprehensive | 3 | valid | not measured | [claude-invocation-02-invocation-nonprose-candidate-comprehensive-3](results/20260928T012250115Z-cw-prep-claude-invocation-nonprose-candidate-b9785bfc-6cb1-4f49-8627-9de82448c578-9jlkxuxv.json) |
| 7 | invocation-comments | candidate-comprehensive | 3 | valid | met | [claude-invocation-02-invocation-comments-candidate-comprehensive-3](results/20260928T012323047Z-cw-prep-claude-invocation-comments-candidate-cc071aac-9539-49ac-af3f-7733fcd50ff6-7iv4bfn1.json) |
| 8 | invocation-comments | original | 3 | valid | met | [claude-invocation-02-invocation-comments-original-3](results/20260928T012410542Z-cw-prep-claude-invocation-comments-original-3a64ec2e-67eb-44bd-a437-4ad03ded0655-tgrdbc2n.json) |

| Case / condition / criterion | Met | Not met | Insufficient evidence | Not measured | Evidence |
| --- | --- | --- | --- | --- | --- |
| invocation-tighten / original / F1 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-tighten-original-3](results/20260928T011757062Z-cw-prep-claude-invocation-tighten-original-8872c4a0-80fa-4521-86ff-1ef185c98e11-6h0dva0a.json) |
| invocation-tighten / original / F2 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-tighten-original-3](results/20260928T011757062Z-cw-prep-claude-invocation-tighten-original-8872c4a0-80fa-4521-86ff-1ef185c98e11-6h0dva0a.json) |
| invocation-tighten / original / F3 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-tighten-original-3](results/20260928T011757062Z-cw-prep-claude-invocation-tighten-original-8872c4a0-80fa-4521-86ff-1ef185c98e11-6h0dva0a.json) |
| invocation-tighten / original / D1 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-tighten-original-3](results/20260928T011757062Z-cw-prep-claude-invocation-tighten-original-8872c4a0-80fa-4521-86ff-1ef185c98e11-6h0dva0a.json) |
| invocation-tighten / original / functional outcome | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-tighten-original-3](results/20260928T011757062Z-cw-prep-claude-invocation-tighten-original-8872c4a0-80fa-4521-86ff-1ef185c98e11-6h0dva0a.json) |
| invocation-tighten / candidate-comprehensive / F1 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-tighten-candidate-comprehensive-3](results/20260928T011843805Z-cw-prep-claude-invocation-tighten-candidate-a7611382-b798-468b-bfff-dda335a5e3a7-ym6suo4n.json) |
| invocation-tighten / candidate-comprehensive / F2 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-tighten-candidate-comprehensive-3](results/20260928T011843805Z-cw-prep-claude-invocation-tighten-candidate-a7611382-b798-468b-bfff-dda335a5e3a7-ym6suo4n.json) |
| invocation-tighten / candidate-comprehensive / F3 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-tighten-candidate-comprehensive-3](results/20260928T011843805Z-cw-prep-claude-invocation-tighten-candidate-a7611382-b798-468b-bfff-dda335a5e3a7-ym6suo4n.json) |
| invocation-tighten / candidate-comprehensive / D1 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-tighten-candidate-comprehensive-3](results/20260928T011843805Z-cw-prep-claude-invocation-tighten-candidate-a7611382-b798-468b-bfff-dda335a5e3a7-ym6suo4n.json) |
| invocation-tighten / candidate-comprehensive / functional outcome | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-tighten-candidate-comprehensive-3](results/20260928T011843805Z-cw-prep-claude-invocation-tighten-candidate-a7611382-b798-468b-bfff-dda335a5e3a7-ym6suo4n.json) |
| invocation-write / candidate-comprehensive / F1 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-write-candidate-comprehensive-3](results/20260928T011938667Z-cw-prep-claude-invocation-write-candidate-ee32f2ff-47b7-42b5-b2a2-c9ac8ba4f87f-kyfcwulb.json) |
| invocation-write / candidate-comprehensive / F2 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-write-candidate-comprehensive-3](results/20260928T011938667Z-cw-prep-claude-invocation-write-candidate-ee32f2ff-47b7-42b5-b2a2-c9ac8ba4f87f-kyfcwulb.json) |
| invocation-write / candidate-comprehensive / F3 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-write-candidate-comprehensive-3](results/20260928T011938667Z-cw-prep-claude-invocation-write-candidate-ee32f2ff-47b7-42b5-b2a2-c9ac8ba4f87f-kyfcwulb.json) |
| invocation-write / candidate-comprehensive / D1 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-write-candidate-comprehensive-3](results/20260928T011938667Z-cw-prep-claude-invocation-write-candidate-ee32f2ff-47b7-42b5-b2a2-c9ac8ba4f87f-kyfcwulb.json) |
| invocation-write / candidate-comprehensive / functional outcome | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-write-candidate-comprehensive-3](results/20260928T011938667Z-cw-prep-claude-invocation-write-candidate-ee32f2ff-47b7-42b5-b2a2-c9ac8ba4f87f-kyfcwulb.json) |
| invocation-write / original / F1 | 0 | 1 | 0 | 0 | [claude-invocation-02-invocation-write-original-3](results/20260928T012104354Z-cw-prep-claude-invocation-write-original-10ea5c1c-6ed8-4eeb-960b-5ad34ef8ad2e-gx77xlvv.json) |
| invocation-write / original / F2 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-write-original-3](results/20260928T012104354Z-cw-prep-claude-invocation-write-original-10ea5c1c-6ed8-4eeb-960b-5ad34ef8ad2e-gx77xlvv.json) |
| invocation-write / original / F3 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-write-original-3](results/20260928T012104354Z-cw-prep-claude-invocation-write-original-10ea5c1c-6ed8-4eeb-960b-5ad34ef8ad2e-gx77xlvv.json) |
| invocation-write / original / D1 | 0 | 1 | 0 | 0 | [claude-invocation-02-invocation-write-original-3](results/20260928T012104354Z-cw-prep-claude-invocation-write-original-10ea5c1c-6ed8-4eeb-960b-5ad34ef8ad2e-gx77xlvv.json) |
| invocation-write / original / functional outcome | 0 | 1 | 0 | 0 | [claude-invocation-02-invocation-write-original-3](results/20260928T012104354Z-cw-prep-claude-invocation-write-original-10ea5c1c-6ed8-4eeb-960b-5ad34ef8ad2e-gx77xlvv.json) |
| invocation-nonprose / original / D1 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-nonprose-original-3](results/20260928T012208212Z-cw-prep-claude-invocation-nonprose-original-18f874de-b271-48a5-b5f8-498cc980b76e-xst9nmcl.json) |
| invocation-nonprose / original / functional outcome | 0 | 0 | 0 | 1 | [claude-invocation-02-invocation-nonprose-original-3](results/20260928T012208212Z-cw-prep-claude-invocation-nonprose-original-18f874de-b271-48a5-b5f8-498cc980b76e-xst9nmcl.json) |
| invocation-nonprose / candidate-comprehensive / D1 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-nonprose-candidate-comprehensive-3](results/20260928T012250115Z-cw-prep-claude-invocation-nonprose-candidate-b9785bfc-6cb1-4f49-8627-9de82448c578-9jlkxuxv.json) |
| invocation-nonprose / candidate-comprehensive / functional outcome | 0 | 0 | 0 | 1 | [claude-invocation-02-invocation-nonprose-candidate-comprehensive-3](results/20260928T012250115Z-cw-prep-claude-invocation-nonprose-candidate-b9785bfc-6cb1-4f49-8627-9de82448c578-9jlkxuxv.json) |
| invocation-comments / candidate-comprehensive / F1 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-comments-candidate-comprehensive-3](results/20260928T012323047Z-cw-prep-claude-invocation-comments-candidate-cc071aac-9539-49ac-af3f-7733fcd50ff6-7iv4bfn1.json) |
| invocation-comments / candidate-comprehensive / F2 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-comments-candidate-comprehensive-3](results/20260928T012323047Z-cw-prep-claude-invocation-comments-candidate-cc071aac-9539-49ac-af3f-7733fcd50ff6-7iv4bfn1.json) |
| invocation-comments / candidate-comprehensive / F3 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-comments-candidate-comprehensive-3](results/20260928T012323047Z-cw-prep-claude-invocation-comments-candidate-cc071aac-9539-49ac-af3f-7733fcd50ff6-7iv4bfn1.json) |
| invocation-comments / candidate-comprehensive / D1 | 0 | 1 | 0 | 0 | [claude-invocation-02-invocation-comments-candidate-comprehensive-3](results/20260928T012323047Z-cw-prep-claude-invocation-comments-candidate-cc071aac-9539-49ac-af3f-7733fcd50ff6-7iv4bfn1.json) |
| invocation-comments / candidate-comprehensive / functional outcome | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-comments-candidate-comprehensive-3](results/20260928T012323047Z-cw-prep-claude-invocation-comments-candidate-cc071aac-9539-49ac-af3f-7733fcd50ff6-7iv4bfn1.json) |
| invocation-comments / original / F1 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-comments-original-3](results/20260928T012410542Z-cw-prep-claude-invocation-comments-original-3a64ec2e-67eb-44bd-a437-4ad03ded0655-tgrdbc2n.json) |
| invocation-comments / original / F2 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-comments-original-3](results/20260928T012410542Z-cw-prep-claude-invocation-comments-original-3a64ec2e-67eb-44bd-a437-4ad03ded0655-tgrdbc2n.json) |
| invocation-comments / original / F3 | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-comments-original-3](results/20260928T012410542Z-cw-prep-claude-invocation-comments-original-3a64ec2e-67eb-44bd-a437-4ad03ded0655-tgrdbc2n.json) |
| invocation-comments / original / D1 | 0 | 1 | 0 | 0 | [claude-invocation-02-invocation-comments-original-3](results/20260928T012410542Z-cw-prep-claude-invocation-comments-original-3a64ec2e-67eb-44bd-a437-4ad03ded0655-tgrdbc2n.json) |
| invocation-comments / original / functional outcome | 1 | 0 | 0 | 0 | [claude-invocation-02-invocation-comments-original-3](results/20260928T012410542Z-cw-prep-claude-invocation-comments-original-3a64ec2e-67eb-44bd-a437-4ad03ded0655-tgrdbc2n.json) |

Use assessment format 2. Not measured is separate from functional met/not met/insufficient evidence and excluded from functional success denominators. No functional success rate exists when all outcomes are not measured. Coverage above retains excluded and unassessed attempts.


## Disposition

This eight-call supplement is complete; current owner decisions live at the [protocol opening](protocol.md).
No skill edit or adoption follows from these observations alone.
