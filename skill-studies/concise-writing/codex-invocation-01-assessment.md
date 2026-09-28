# Codex native CW comparison: assessment

Format version: `2`
Assessment ID: cw-codex-invocation-01
Study / batch: concise-writing / codex-invocation-01
Status: complete; all sixteen authorized attempts retained and assessed
Scope and acceptance rules: [protocol](protocol.md) at Git `4dc370648a6a915546035847b2823a4bc5d57325`, batch codex-invocation-01; CW-expanded-1 and the four native case cards.
Attempt index: [codex-invocation-01-run-index.json](codex-invocation-01-run-index.json) at Git `cffe34821cf70e6a1d231c2364dcb79cf5e9bf52`, SHA-256 `3aef69b7f28a8832eac9a8d9d39d797cf7ce5a6ebcef9d9b332019127d041ff2`.
Assessor and relevant session context: active Codex session that prepared and inspected these exposed development cases; not independent, blind or held out.

## Coverage and execution results

| Case | Original timely/appropriate selection | Rewrite timely/appropriate selection | Original functional | Rewrite functional |
| --- | --- | --- | --- | --- |
| N1: tightening | 2/2 | 2/2 | 2/2 | 2/2 |
| N2: new update | 2/2 | 2/2 | 2/2 | 2/2 |
| N3: numeric only | 2/2 avoided loading | 1/2 avoided loading | Not measured | Not measured |
| N4: code comments | 2/2 | 2/2 | 2/2 | 2/2 |

All sixteen setups are valid, with no retries, exclusions, replacements, insufficient-evidence judgments or unattempted slots.
All twelve positive tasks load the complete assigned body before first writing and meet F1–F3.
Numeric-only task correctness is recorded separately and cannot establish CW effectiveness.
The frozen rotated schedule was used without randomization.
All attempts used Codex CLI 0.157.1, gpt-5.6-sol, low effort, workspace-write and the 900-second limit; actual session/turn records confirm identity, CLI, model and effort.
CLI SHA-256: `27ceb5f9b957b43a519efe4eaa3816a0bffb0a531a2c89af18840c0a3c016a7d`.
The native catalog contains the assigned CW description plus imagegen, openai-docs, plugin-creator, skill-creator and skill-installer.
The qualified catalog supplies no CW body initially; the tasks never request loading it.
No immutable backend model revision is available.
Original and candidate descriptions differ, so whole-version observations do not isolate a description or body effect.

## Aggregate results

Positive selection and functional outcomes are each 6/6 per version, with separate denominators.
Negative selection is 2/2 for original and 1/2 for candidate.
All four numeric outputs preserve every byte except the requested number and reply literally Done.; functional CW outcomes remain unmeasured.
These small exposed-case observations are diagnostic, not reliability estimates or an adoption decision.

## Interpretation and limitations

Candidate order 6 reads the complete skill before reading TASK.md and fails negative selection.
The second candidate numeric attempt avoids loading, as do both originals.
This is observed premature selection after catalog exposure, not automatic full-body injection or an invalid setup.
Successful numeric work does not erase that selection failure.

N1 preserves evidence, bounded pilot, staffing, stop/retention rationale and separate expansion decision while removing padding.
N2 produces coherent updates preserving approval, staffed-window fallback, untested risks and diagnostic evidence.
N4 adds the missing maintenance guidance and preserves executable tokens and syntax in all four outputs.
The controller used check_fixture.py --compare without executing subject code.
Original order 15 connects an already successful send to exactly-once acknowledgement and no resend; other outputs use accepted-batch or explicit duplication wording.
These convey the rationale in code context without requiring a preferred phrase.

| Case / version | Source words | Output words in repetition order | Interpretation |
| --- | ---: | --- | --- |
| N1 original | 625 | 214, 218 | Shorter, with F1–F3 preserved |
| N1 rewrite | 625 | 254, 244 | Shorter, with F1–F3 preserved |
| N2 original | 199 | 218, 219 | Notes-to-report length is descriptive |
| N2 rewrite | 199 | 247, 207 | Notes-to-report length is descriptive |
| N4 original | 20 | 42, 35 | Comment words excluding markers; added rationale, no shortening preference |
| N4 rewrite | 20 | 51, 37 | Comment words excluding markers; added rationale, no shortening preference |

All sixteen inventories, forty protected input copies and complete structured results verify.
Complete artifacts and raw traces are retained; no Git commands were run inside retained bundles.
Some subjects recover from rejected duplicate-target patches, a denied parent-directory search, an unavailable python alias, a read-only shell variable or denied cache removal.
These are captured within-call process observations, not repeated calls or exclusions.
Runner duration totals 748.348 seconds, included once in the 35 estimated minutes booked for native Codex collection and assessment.
[Runtime qualification](preparation/runtime-qualification.md) and [collection review](../../reviews/2026-09-27-cw-expanded-collection-review.md) establish the execution and review record.
Keep this batch separate from explicit-load outcomes, Claude and historical runtimes.
Response-only applicability, orchestration and causal attribution to individual instructions remain untested.

## Mechanical tables and evidence

| Case / condition | Planned | Attempted | Included | Invalid setup | Setup unresolved | Unattempted |
| --- | --- | --- | --- | --- | --- | --- |
| invocation-tighten / original | 2 | 2 | 2 | 0 | 0 | 0 |
| invocation-tighten / candidate-comprehensive | 2 | 2 | 2 | 0 | 0 | 0 |
| invocation-write / candidate-comprehensive | 2 | 2 | 2 | 0 | 0 | 0 |
| invocation-write / original | 2 | 2 | 2 | 0 | 0 | 0 |
| invocation-nonprose / original | 2 | 2 | 2 | 0 | 0 | 0 |
| invocation-nonprose / candidate-comprehensive | 2 | 2 | 2 | 0 | 0 | 0 |
| invocation-comments / candidate-comprehensive | 2 | 2 | 2 | 0 | 0 | 0 |
| invocation-comments / original | 2 | 2 | 2 | 0 | 0 | 0 |

| Order | Case | Condition | Repetition | Setup / coverage | Recorded outcome | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | invocation-tighten | original | 1 | valid | met | [codex-invocation-01-invocation-tighten-original-1](results/20260928T000714703Z-cw-prep-codex-invocation-tighten-original-a36d3f60-050d-4e71-9743-405e763443c3-0jknpesu.json) |
| 2 | invocation-tighten | candidate-comprehensive | 1 | valid | met | [codex-invocation-01-invocation-tighten-candidate-comprehensive-1](results/20260928T000919413Z-cw-prep-codex-invocation-tighten-candidate-0997826a-025b-4085-a6a7-e9edb44ec0fe-j7v6rgin.json) |
| 3 | invocation-write | candidate-comprehensive | 1 | valid | met | [codex-invocation-01-invocation-write-candidate-comprehensive-1](results/20260928T001043635Z-cw-prep-codex-invocation-write-candidate-5469587f-b2e4-4ab1-b1be-d71e072a11c6-xz74yx8o.json) |
| 4 | invocation-write | original | 1 | valid | met | [codex-invocation-01-invocation-write-original-1](results/20260928T001150965Z-cw-prep-codex-invocation-write-original-f210cc75-3aa0-4495-a479-c81f7b91eb8d-gb44qr_3.json) |
| 5 | invocation-nonprose | original | 1 | valid | not measured | [codex-invocation-01-invocation-nonprose-original-1](results/20260928T001302672Z-cw-prep-codex-invocation-nonprose-original-5b6c8f02-1ec9-4edc-8621-55b0dc863a60-jfz2rpuu.json) |
| 6 | invocation-nonprose | candidate-comprehensive | 1 | valid | not measured | [codex-invocation-01-invocation-nonprose-candidate-comprehensive-1](results/20260928T001353442Z-cw-prep-codex-invocation-nonprose-candidate-4325f069-78cf-42a4-b941-02edb545e3b0-vxx6v5m4.json) |
| 7 | invocation-comments | candidate-comprehensive | 1 | valid | met | [codex-invocation-01-invocation-comments-candidate-comprehensive-1](results/20260928T001506239Z-cw-prep-codex-invocation-comments-candidate-f6535e8d-dc71-4c1d-b0e2-885279fcba05-c6tcnht6.json) |
| 8 | invocation-comments | original | 1 | valid | met | [codex-invocation-01-invocation-comments-original-1](results/20260928T001626384Z-cw-prep-codex-invocation-comments-original-510bd97c-c20e-4071-9d99-68b2d55d0e48-y5r0ib05.json) |
| 9 | invocation-tighten | candidate-comprehensive | 2 | valid | met | [codex-invocation-01-invocation-tighten-candidate-comprehensive-2](results/20260928T001853585Z-cw-prep-codex-invocation-tighten-candidate-478035f4-ef58-4139-8113-238e4c705f27-ld97fg79.json) |
| 10 | invocation-tighten | original | 2 | valid | met | [codex-invocation-01-invocation-tighten-original-2](results/20260928T002016583Z-cw-prep-codex-invocation-tighten-original-1dc9fe36-52e6-4ca3-84e5-bce0141944c0-w63p16vj.json) |
| 11 | invocation-write | original | 2 | valid | met | [codex-invocation-01-invocation-write-original-2](results/20260928T002514707Z-cw-prep-codex-invocation-write-original-85e25a1a-e7f8-4568-845c-0164de9135e5-gvty2x69.json) |
| 12 | invocation-write | candidate-comprehensive | 2 | valid | met | [codex-invocation-01-invocation-write-candidate-comprehensive-2](results/20260928T002616621Z-cw-prep-codex-invocation-write-candidate-3f28527e-9a49-4cc7-94c5-b1abbe19c6cf-0kkely4l.json) |
| 13 | invocation-nonprose | candidate-comprehensive | 2 | valid | not measured | [codex-invocation-01-invocation-nonprose-candidate-comprehensive-2](results/20260928T002717009Z-cw-prep-codex-invocation-nonprose-candidate-d3fc04a6-248b-43e0-ab21-9f4a2c686bd5-54plbx8s.json) |
| 14 | invocation-nonprose | original | 2 | valid | not measured | [codex-invocation-01-invocation-nonprose-original-2](results/20260928T002758617Z-cw-prep-codex-invocation-nonprose-original-b8ce70c7-7d4b-423c-9c0b-99d76611e8ed-pzvsjo5b.json) |
| 15 | invocation-comments | original | 2 | valid | met | [codex-invocation-01-invocation-comments-original-2](results/20260928T002849686Z-cw-prep-codex-invocation-comments-original-d0bcc9ca-cdb0-47a6-8b00-bebee6b9af3c-9e7koxx_.json) |
| 16 | invocation-comments | candidate-comprehensive | 2 | valid | met | [codex-invocation-01-invocation-comments-candidate-comprehensive-2](results/20260928T003013128Z-cw-prep-codex-invocation-comments-candidate-04ec0025-0e52-457e-bcaf-d0aa276479ce-zddhbmy4.json) |

| Case / condition / criterion | Met | Not met | Insufficient evidence | Not measured | Evidence |
| --- | --- | --- | --- | --- | --- |
| invocation-tighten / original / F1 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-tighten-original-1](results/20260928T000714703Z-cw-prep-codex-invocation-tighten-original-a36d3f60-050d-4e71-9743-405e763443c3-0jknpesu.json), [codex-invocation-01-invocation-tighten-original-2](results/20260928T002016583Z-cw-prep-codex-invocation-tighten-original-1dc9fe36-52e6-4ca3-84e5-bce0141944c0-w63p16vj.json) |
| invocation-tighten / original / F2 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-tighten-original-1](results/20260928T000714703Z-cw-prep-codex-invocation-tighten-original-a36d3f60-050d-4e71-9743-405e763443c3-0jknpesu.json), [codex-invocation-01-invocation-tighten-original-2](results/20260928T002016583Z-cw-prep-codex-invocation-tighten-original-1dc9fe36-52e6-4ca3-84e5-bce0141944c0-w63p16vj.json) |
| invocation-tighten / original / F3 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-tighten-original-1](results/20260928T000714703Z-cw-prep-codex-invocation-tighten-original-a36d3f60-050d-4e71-9743-405e763443c3-0jknpesu.json), [codex-invocation-01-invocation-tighten-original-2](results/20260928T002016583Z-cw-prep-codex-invocation-tighten-original-1dc9fe36-52e6-4ca3-84e5-bce0141944c0-w63p16vj.json) |
| invocation-tighten / original / D1 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-tighten-original-1](results/20260928T000714703Z-cw-prep-codex-invocation-tighten-original-a36d3f60-050d-4e71-9743-405e763443c3-0jknpesu.json), [codex-invocation-01-invocation-tighten-original-2](results/20260928T002016583Z-cw-prep-codex-invocation-tighten-original-1dc9fe36-52e6-4ca3-84e5-bce0141944c0-w63p16vj.json) |
| invocation-tighten / original / functional outcome | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-tighten-original-1](results/20260928T000714703Z-cw-prep-codex-invocation-tighten-original-a36d3f60-050d-4e71-9743-405e763443c3-0jknpesu.json), [codex-invocation-01-invocation-tighten-original-2](results/20260928T002016583Z-cw-prep-codex-invocation-tighten-original-1dc9fe36-52e6-4ca3-84e5-bce0141944c0-w63p16vj.json) |
| invocation-tighten / candidate-comprehensive / F1 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-tighten-candidate-comprehensive-1](results/20260928T000919413Z-cw-prep-codex-invocation-tighten-candidate-0997826a-025b-4085-a6a7-e9edb44ec0fe-j7v6rgin.json), [codex-invocation-01-invocation-tighten-candidate-comprehensive-2](results/20260928T001853585Z-cw-prep-codex-invocation-tighten-candidate-478035f4-ef58-4139-8113-238e4c705f27-ld97fg79.json) |
| invocation-tighten / candidate-comprehensive / F2 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-tighten-candidate-comprehensive-1](results/20260928T000919413Z-cw-prep-codex-invocation-tighten-candidate-0997826a-025b-4085-a6a7-e9edb44ec0fe-j7v6rgin.json), [codex-invocation-01-invocation-tighten-candidate-comprehensive-2](results/20260928T001853585Z-cw-prep-codex-invocation-tighten-candidate-478035f4-ef58-4139-8113-238e4c705f27-ld97fg79.json) |
| invocation-tighten / candidate-comprehensive / F3 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-tighten-candidate-comprehensive-1](results/20260928T000919413Z-cw-prep-codex-invocation-tighten-candidate-0997826a-025b-4085-a6a7-e9edb44ec0fe-j7v6rgin.json), [codex-invocation-01-invocation-tighten-candidate-comprehensive-2](results/20260928T001853585Z-cw-prep-codex-invocation-tighten-candidate-478035f4-ef58-4139-8113-238e4c705f27-ld97fg79.json) |
| invocation-tighten / candidate-comprehensive / D1 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-tighten-candidate-comprehensive-1](results/20260928T000919413Z-cw-prep-codex-invocation-tighten-candidate-0997826a-025b-4085-a6a7-e9edb44ec0fe-j7v6rgin.json), [codex-invocation-01-invocation-tighten-candidate-comprehensive-2](results/20260928T001853585Z-cw-prep-codex-invocation-tighten-candidate-478035f4-ef58-4139-8113-238e4c705f27-ld97fg79.json) |
| invocation-tighten / candidate-comprehensive / functional outcome | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-tighten-candidate-comprehensive-1](results/20260928T000919413Z-cw-prep-codex-invocation-tighten-candidate-0997826a-025b-4085-a6a7-e9edb44ec0fe-j7v6rgin.json), [codex-invocation-01-invocation-tighten-candidate-comprehensive-2](results/20260928T001853585Z-cw-prep-codex-invocation-tighten-candidate-478035f4-ef58-4139-8113-238e4c705f27-ld97fg79.json) |
| invocation-write / candidate-comprehensive / F1 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-write-candidate-comprehensive-1](results/20260928T001043635Z-cw-prep-codex-invocation-write-candidate-5469587f-b2e4-4ab1-b1be-d71e072a11c6-xz74yx8o.json), [codex-invocation-01-invocation-write-candidate-comprehensive-2](results/20260928T002616621Z-cw-prep-codex-invocation-write-candidate-3f28527e-9a49-4cc7-94c5-b1abbe19c6cf-0kkely4l.json) |
| invocation-write / candidate-comprehensive / F2 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-write-candidate-comprehensive-1](results/20260928T001043635Z-cw-prep-codex-invocation-write-candidate-5469587f-b2e4-4ab1-b1be-d71e072a11c6-xz74yx8o.json), [codex-invocation-01-invocation-write-candidate-comprehensive-2](results/20260928T002616621Z-cw-prep-codex-invocation-write-candidate-3f28527e-9a49-4cc7-94c5-b1abbe19c6cf-0kkely4l.json) |
| invocation-write / candidate-comprehensive / F3 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-write-candidate-comprehensive-1](results/20260928T001043635Z-cw-prep-codex-invocation-write-candidate-5469587f-b2e4-4ab1-b1be-d71e072a11c6-xz74yx8o.json), [codex-invocation-01-invocation-write-candidate-comprehensive-2](results/20260928T002616621Z-cw-prep-codex-invocation-write-candidate-3f28527e-9a49-4cc7-94c5-b1abbe19c6cf-0kkely4l.json) |
| invocation-write / candidate-comprehensive / D1 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-write-candidate-comprehensive-1](results/20260928T001043635Z-cw-prep-codex-invocation-write-candidate-5469587f-b2e4-4ab1-b1be-d71e072a11c6-xz74yx8o.json), [codex-invocation-01-invocation-write-candidate-comprehensive-2](results/20260928T002616621Z-cw-prep-codex-invocation-write-candidate-3f28527e-9a49-4cc7-94c5-b1abbe19c6cf-0kkely4l.json) |
| invocation-write / candidate-comprehensive / functional outcome | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-write-candidate-comprehensive-1](results/20260928T001043635Z-cw-prep-codex-invocation-write-candidate-5469587f-b2e4-4ab1-b1be-d71e072a11c6-xz74yx8o.json), [codex-invocation-01-invocation-write-candidate-comprehensive-2](results/20260928T002616621Z-cw-prep-codex-invocation-write-candidate-3f28527e-9a49-4cc7-94c5-b1abbe19c6cf-0kkely4l.json) |
| invocation-write / original / F1 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-write-original-1](results/20260928T001150965Z-cw-prep-codex-invocation-write-original-f210cc75-3aa0-4495-a479-c81f7b91eb8d-gb44qr_3.json), [codex-invocation-01-invocation-write-original-2](results/20260928T002514707Z-cw-prep-codex-invocation-write-original-85e25a1a-e7f8-4568-845c-0164de9135e5-gvty2x69.json) |
| invocation-write / original / F2 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-write-original-1](results/20260928T001150965Z-cw-prep-codex-invocation-write-original-f210cc75-3aa0-4495-a479-c81f7b91eb8d-gb44qr_3.json), [codex-invocation-01-invocation-write-original-2](results/20260928T002514707Z-cw-prep-codex-invocation-write-original-85e25a1a-e7f8-4568-845c-0164de9135e5-gvty2x69.json) |
| invocation-write / original / F3 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-write-original-1](results/20260928T001150965Z-cw-prep-codex-invocation-write-original-f210cc75-3aa0-4495-a479-c81f7b91eb8d-gb44qr_3.json), [codex-invocation-01-invocation-write-original-2](results/20260928T002514707Z-cw-prep-codex-invocation-write-original-85e25a1a-e7f8-4568-845c-0164de9135e5-gvty2x69.json) |
| invocation-write / original / D1 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-write-original-1](results/20260928T001150965Z-cw-prep-codex-invocation-write-original-f210cc75-3aa0-4495-a479-c81f7b91eb8d-gb44qr_3.json), [codex-invocation-01-invocation-write-original-2](results/20260928T002514707Z-cw-prep-codex-invocation-write-original-85e25a1a-e7f8-4568-845c-0164de9135e5-gvty2x69.json) |
| invocation-write / original / functional outcome | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-write-original-1](results/20260928T001150965Z-cw-prep-codex-invocation-write-original-f210cc75-3aa0-4495-a479-c81f7b91eb8d-gb44qr_3.json), [codex-invocation-01-invocation-write-original-2](results/20260928T002514707Z-cw-prep-codex-invocation-write-original-85e25a1a-e7f8-4568-845c-0164de9135e5-gvty2x69.json) |
| invocation-nonprose / original / D1 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-nonprose-original-1](results/20260928T001302672Z-cw-prep-codex-invocation-nonprose-original-5b6c8f02-1ec9-4edc-8621-55b0dc863a60-jfz2rpuu.json), [codex-invocation-01-invocation-nonprose-original-2](results/20260928T002758617Z-cw-prep-codex-invocation-nonprose-original-b8ce70c7-7d4b-423c-9c0b-99d76611e8ed-pzvsjo5b.json) |
| invocation-nonprose / original / functional outcome | 0 | 0 | 0 | 2 | [codex-invocation-01-invocation-nonprose-original-1](results/20260928T001302672Z-cw-prep-codex-invocation-nonprose-original-5b6c8f02-1ec9-4edc-8621-55b0dc863a60-jfz2rpuu.json), [codex-invocation-01-invocation-nonprose-original-2](results/20260928T002758617Z-cw-prep-codex-invocation-nonprose-original-b8ce70c7-7d4b-423c-9c0b-99d76611e8ed-pzvsjo5b.json) |
| invocation-nonprose / candidate-comprehensive / D1 | 1 | 1 | 0 | 0 | [codex-invocation-01-invocation-nonprose-candidate-comprehensive-1](results/20260928T001353442Z-cw-prep-codex-invocation-nonprose-candidate-4325f069-78cf-42a4-b941-02edb545e3b0-vxx6v5m4.json), [codex-invocation-01-invocation-nonprose-candidate-comprehensive-2](results/20260928T002717009Z-cw-prep-codex-invocation-nonprose-candidate-d3fc04a6-248b-43e0-ab21-9f4a2c686bd5-54plbx8s.json) |
| invocation-nonprose / candidate-comprehensive / functional outcome | 0 | 0 | 0 | 2 | [codex-invocation-01-invocation-nonprose-candidate-comprehensive-1](results/20260928T001353442Z-cw-prep-codex-invocation-nonprose-candidate-4325f069-78cf-42a4-b941-02edb545e3b0-vxx6v5m4.json), [codex-invocation-01-invocation-nonprose-candidate-comprehensive-2](results/20260928T002717009Z-cw-prep-codex-invocation-nonprose-candidate-d3fc04a6-248b-43e0-ab21-9f4a2c686bd5-54plbx8s.json) |
| invocation-comments / candidate-comprehensive / F1 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-comments-candidate-comprehensive-1](results/20260928T001506239Z-cw-prep-codex-invocation-comments-candidate-f6535e8d-dc71-4c1d-b0e2-885279fcba05-c6tcnht6.json), [codex-invocation-01-invocation-comments-candidate-comprehensive-2](results/20260928T003013128Z-cw-prep-codex-invocation-comments-candidate-04ec0025-0e52-457e-bcaf-d0aa276479ce-zddhbmy4.json) |
| invocation-comments / candidate-comprehensive / F2 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-comments-candidate-comprehensive-1](results/20260928T001506239Z-cw-prep-codex-invocation-comments-candidate-f6535e8d-dc71-4c1d-b0e2-885279fcba05-c6tcnht6.json), [codex-invocation-01-invocation-comments-candidate-comprehensive-2](results/20260928T003013128Z-cw-prep-codex-invocation-comments-candidate-04ec0025-0e52-457e-bcaf-d0aa276479ce-zddhbmy4.json) |
| invocation-comments / candidate-comprehensive / F3 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-comments-candidate-comprehensive-1](results/20260928T001506239Z-cw-prep-codex-invocation-comments-candidate-f6535e8d-dc71-4c1d-b0e2-885279fcba05-c6tcnht6.json), [codex-invocation-01-invocation-comments-candidate-comprehensive-2](results/20260928T003013128Z-cw-prep-codex-invocation-comments-candidate-04ec0025-0e52-457e-bcaf-d0aa276479ce-zddhbmy4.json) |
| invocation-comments / candidate-comprehensive / D1 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-comments-candidate-comprehensive-1](results/20260928T001506239Z-cw-prep-codex-invocation-comments-candidate-f6535e8d-dc71-4c1d-b0e2-885279fcba05-c6tcnht6.json), [codex-invocation-01-invocation-comments-candidate-comprehensive-2](results/20260928T003013128Z-cw-prep-codex-invocation-comments-candidate-04ec0025-0e52-457e-bcaf-d0aa276479ce-zddhbmy4.json) |
| invocation-comments / candidate-comprehensive / functional outcome | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-comments-candidate-comprehensive-1](results/20260928T001506239Z-cw-prep-codex-invocation-comments-candidate-f6535e8d-dc71-4c1d-b0e2-885279fcba05-c6tcnht6.json), [codex-invocation-01-invocation-comments-candidate-comprehensive-2](results/20260928T003013128Z-cw-prep-codex-invocation-comments-candidate-04ec0025-0e52-457e-bcaf-d0aa276479ce-zddhbmy4.json) |
| invocation-comments / original / F1 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-comments-original-1](results/20260928T001626384Z-cw-prep-codex-invocation-comments-original-510bd97c-c20e-4071-9d99-68b2d55d0e48-y5r0ib05.json), [codex-invocation-01-invocation-comments-original-2](results/20260928T002849686Z-cw-prep-codex-invocation-comments-original-d0bcc9ca-cdb0-47a6-8b00-bebee6b9af3c-9e7koxx_.json) |
| invocation-comments / original / F2 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-comments-original-1](results/20260928T001626384Z-cw-prep-codex-invocation-comments-original-510bd97c-c20e-4071-9d99-68b2d55d0e48-y5r0ib05.json), [codex-invocation-01-invocation-comments-original-2](results/20260928T002849686Z-cw-prep-codex-invocation-comments-original-d0bcc9ca-cdb0-47a6-8b00-bebee6b9af3c-9e7koxx_.json) |
| invocation-comments / original / F3 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-comments-original-1](results/20260928T001626384Z-cw-prep-codex-invocation-comments-original-510bd97c-c20e-4071-9d99-68b2d55d0e48-y5r0ib05.json), [codex-invocation-01-invocation-comments-original-2](results/20260928T002849686Z-cw-prep-codex-invocation-comments-original-d0bcc9ca-cdb0-47a6-8b00-bebee6b9af3c-9e7koxx_.json) |
| invocation-comments / original / D1 | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-comments-original-1](results/20260928T001626384Z-cw-prep-codex-invocation-comments-original-510bd97c-c20e-4071-9d99-68b2d55d0e48-y5r0ib05.json), [codex-invocation-01-invocation-comments-original-2](results/20260928T002849686Z-cw-prep-codex-invocation-comments-original-d0bcc9ca-cdb0-47a6-8b00-bebee6b9af3c-9e7koxx_.json) |
| invocation-comments / original / functional outcome | 2 | 0 | 0 | 0 | [codex-invocation-01-invocation-comments-original-1](results/20260928T001626384Z-cw-prep-codex-invocation-comments-original-510bd97c-c20e-4071-9d99-68b2d55d0e48-y5r0ib05.json), [codex-invocation-01-invocation-comments-original-2](results/20260928T002849686Z-cw-prep-codex-invocation-comments-original-d0bcc9ca-cdb0-47a6-8b00-bebee6b9af3c-9e7koxx_.json) |

Use assessment format 2. Not measured is separate from functional met/not met/insufficient evidence and excluded from functional success denominators. No functional success rate exists when all outcomes are not measured. Coverage above retains excluded and unassessed attempts.

## Disposition

This batch is complete; current authorized work and owner decisions live at the [protocol opening](protocol.md).
Adoption and skill edits remain deferred pending cross-provider coverage review.
