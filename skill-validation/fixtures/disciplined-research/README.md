# disciplined-research Task 18A replay artifacts

These files freeze the exact evaluator prompts, evaluator-withheld rubrics, and task fixtures for `DR-04` and `DR-05`.
Evaluators receive the matching prompt and immutable read-only bundle, never the rubric or this manifest.

## Supplied contexts

Both controls use `skills/disciplined-research/SKILL.md` from control commit `4296647f0dff48a9e77b979ef07e813bf1f66db2` at SHA-256 `a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50`.
`DR-04` adds `project/payments/retry_policy.py`; `DR-05` adds `sources/nimbus-support-matrix.md`.
The canonical bundle-manifest hashes are recorded in the owning [validation record](../../disciplined-research.md#task-18a-contract-freeze-2026-08-09).

## Run policy

Each control requires five fresh `gpt-5.6-sol` repetitions at high effort and five at low effort under the shared read-only, no-agents transport with maximum concurrency three.
The orchestrator owns execution, scoring, and repetition-level result metadata.
