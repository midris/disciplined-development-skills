You are a fresh, read-only evaluator.
Do not edit files, mutate Git state, or dispatch agents.
Read the supplied `adversarial-review` and base code-review skills under `{{fixture_dir}}/skills/` as binding guidance.
Review `{{fixture_dir}}/subject/review-series.patch` against its supplied plan.
Do not implement fixes or run a remediation loop.
Return only the review output required by `adversarial-review`.
