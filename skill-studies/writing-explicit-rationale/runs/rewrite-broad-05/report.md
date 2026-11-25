# Frozen 599-word WER candidate at five repetitions

Each cell counts valid outputs meeting every applicable functional criterion. Codex candidate sessions used the apps-disabled boundary. The matching shipped column uses the same boundary. The pooled column includes earlier valid Codex shipped sessions. Claude used the same settings throughout.

| Scenario | Codex candidate | Codex shipped, apps disabled | Codex shipped, pooled | Claude candidate | Claude shipped |
|---|---:|---:|---:|---:|---:|
| export-deferral | 5/5 | 3/3 | 5/5 | 5/5 | 5/5 |
| quota-grace | 5/5 | 3/3 | 5/5 | 5/5 | 5/5 |
| repeated-review | 5/5 | 2/3 | 4/5 | 5/5 | 5/5 |
| catalog-review | 5/5 | 3/3 | 4/4 | 5/5 | 5/5 |
| helper-rename | 5/5 | 4/4 | 5/5 | 5/5 | 5/5 |
| scope-trim | 4/5 | 4/4 | 4/5 | 5/5 | 5/5 |
| dispatch-hold | 5/5 | 4/4 | 5/5 | 5/5 | 5/5 |

| Dimension | Candidate | Shipped, pooled | No-skill control, pooled |
|---|---:|---:|---:|
| All applicable criteria | 69/70 | 67/69 | 42/69 |
| Task correctness | 69/70 | 68/69 | 66/69 |
| Rationale and restraint | 70/70 | 68/69 | 44/69 |

The pooled baseline retains its two invalid Codex catalog attempts outside the functional denominators. The [shipped benchmark](../application-topup-01/report.md) explains the setup change. The [first five Codex repeated-review outputs](../../protocol.md#five-run-candidate-checkpoint) and the five broader batches supply the candidate observations. The [final subject assessments](assessment.json) and [reader decisions](decision-readings.json) link the evidence for this top-up.

## Outcome and limits

All 26 final subjects met every criterion. All 30 newly allocated sessions had valid setups and were retained without replacement. The 20 applicable original-test and private replay suites passed. Over all five repetitions on both models, the one candidate miss was Codex scope-trim repetition 2: the project dated the launch to Monday when the source dated only the handoff. It retained the complete Finance and Support rationale. Both new Codex outputs avoided the scheduling error.

All ten repeated-review projects recovered the second quota rationale from the submitted change. Four of five Codex projects stated future factoring more firmly than the agreement to reconsider. All five Claude projects kept that decision open in the code, but four suggested replies or summaries strengthened it; the fifth used reconsideration in both places. Four of five Codex quota-grace projects left the potential rejection of old-token work implicit in describing why to protect it. Every project identified the eligible work and bounded higher allowance.

All ten catalog readers retained accession order, explained its use in matching corrections to room sheets, and identified the title index. The shipped readers with valid setups did the same in 9/9 cases. Some candidate readers inferred physical sheet order or that every correction would require manual lookup. The source establishes a dependency and added difficulty. All ten dispatch projects attributed the new queue status to the carrier although the source establishes this only for manual holds. That inference does not change the scheduling action. One new Codex export plan described the alternative as an incompatible v1 format, a more definite consequence than schema churn establishes.

The frozen size measure gives 752 candidate tokens and 1,963 shipped tokens, saving 1,211 tokens (61.7%) per full skill delivery under o200k_base. These are explicit-application results on seven known development fixtures, with five candidate observations per cell. They support retaining the candidate for an independent, whole-output comparison before adoption. They do not establish a population-level improvement or native discovery performance for this revision.
