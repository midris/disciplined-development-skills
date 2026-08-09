# Pre-Task-18A DISC-01–DISC-10 evaluator-withheld rubric

This immutable table preserves the allowed sets that governed the active historical
results immediately before Task 18A. Score each complete routing artifact as a JSON
array in ascending alphabetical order with no prose outside it.

| ID | Required | Optional | Prohibited |
|---|---|---|---|
| `DISC-01` | `adversarial-review`; `disciplined-development` | `concise-writing`; `disciplined-research` | Every other local skill |
| `DISC-02` | `adversarial-review-loop`; `disciplined-development` | None | Every other local skill |
| `DISC-03` | `concise-writing`; `disciplined-development` | None | Every other local skill |
| `DISC-04` | `disciplined-development` | `disciplined-research` | Every other local skill |
| `DISC-05` | `disciplined-development`; `disciplined-research` | None | Every other local skill |
| `DISC-06` | `disciplined-development`; `dispatching-development-subagents` | None | Every other local skill |
| `DISC-07` | `disciplined-development`; `lean-plan-writing` | `concise-writing`; `disciplined-research` | Every other local skill |
| `DISC-08` | `disciplined-development`; `sweeping-stale-references` | `disciplined-research` | Every other local skill |
| `DISC-09` | `disciplined-development`; `writing-explicit-rationale` | `concise-writing`; `disciplined-research` | Every other local skill |
| `DISC-10` | `disciplined-development`; `lean-plan-writing`; `writing-explicit-rationale` | `concise-writing`; `disciplined-research`; `sweeping-stale-references` | Every other local skill |

PASS only if every required skill is present, every selected skill is required or
optional, and the output shape and order pass.
