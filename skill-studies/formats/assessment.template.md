# <Batch question>: assessment

Format version: `2-draft`
Assessment ID: <id>
Study / batch: <IDs>
Status: draft
Scope and acceptance rules: <protocol citation at full Git revision>
Attempt index: <path/hash/git_revision>
Assessor and relevant session context: <identity/context>

## Coverage and execution results

Selected cases, conditions and repetitions: <scope citation; describe departures only>
All execution-result records resolve through the attempt index; cite its accepted Git version.
Uncompleted repetitions, unusable attempts and unresolved evidence: <IDs/reasons, or none>
Retry treatment and included attempt IDs: <apply the declared scope rule; no silent replacement>
Setup or input differences affecting interpretation: <exceptions to the declared scope, or none>

## Aggregate results

One row per case, condition and applicable criterion; include a functional-outcome row per case/condition derived from each execution's functional result.
Only declared included executions with valid setup enter the met/not-met/unknown counts.
Account for every planned repetition and every actual attempt in the coverage section; an excluded or missing result is not a pass.

| Case / condition / criterion | Met | Not met | Insufficient evidence | Evidence |
|---|---:|---:|---:|---|
| <IDs; or functional outcome> | <count> | <count> | <count> | <execution-result IDs> |

When reporting a success fraction, use met / (met + not met + insufficient evidence) and show the unknown count; do not present met / known outcomes as complete coverage.
Do not combine criteria into an average: the same incomplete repair may fail more than one criterion.

Recurring failures and consequential differences: <pattern, affected result IDs, evidence pointers and uncertainty about cause>
Acceptance under the declared rule: <judgment and supporting counts, pending, or descriptive-only if no threshold was selected>
Coverage, variability and attribution limits: <text; distinguish observed frequency from population reliability>
Supported conclusion or recommendation: <text linked to these results; owner decision belongs in the protocol>

## Comparison, when applicable

Omit this section for a standalone batch assessment.
Compare this assessment with <accepted assessment citation>, or compare conditions already shown above.
Use their aggregate results; do not repeat individual judgments.
Record relevant setup/rule differences, gains and regressions, and the evidence-supported recommendation.
Include resource differences only when they affect the decision, citing accounting rather than maintaining another cost table.
The protocol owns the owner's rewrite/adoption decision and authorization.
