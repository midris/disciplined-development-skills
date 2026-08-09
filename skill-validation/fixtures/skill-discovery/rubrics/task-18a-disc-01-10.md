# Task 18A DISC-01–DISC-10 evaluator-withheld rubrics

Score each complete routing artifact independently.
Every artifact must be a JSON array in ascending alphabetical order with no prose outside it.

| ID | Required | Optional | Prohibited |
|---|---|---|---|
| `DISC-01` | `adversarial-review`; `disciplined-development`; `disciplined-research` | `concise-writing` | Every other local skill |
| `DISC-02` | `adversarial-review-loop`; `disciplined-development`; `disciplined-research` | None | Every other local skill |
| `DISC-03` | `concise-writing`; `disciplined-development`; `disciplined-research` | None | Every other local skill |
| `DISC-04` | `disciplined-development`; `disciplined-research` | None | Every other local skill |
| `DISC-05` | `disciplined-development`; `disciplined-research` | None | Every other local skill |
| `DISC-06` | `disciplined-development`; `disciplined-research`; `dispatching-development-subagents` | None | Every other local skill |
| `DISC-07` | `disciplined-development`; `disciplined-research`; `lean-plan-writing` | `concise-writing` | Every other local skill |
| `DISC-08` | `disciplined-development`; `disciplined-research`; `sweeping-stale-references` | None | Every other local skill |
| `DISC-09` | `disciplined-development`; `disciplined-research`; `writing-explicit-rationale` | `concise-writing` | Every other local skill |
| `DISC-10` | `disciplined-development`; `disciplined-research`; `lean-plan-writing`; `writing-explicit-rationale` | `concise-writing`; `sweeping-stale-references` | Every other local skill |

PASS only if every required skill is present, every selected skill is required or optional, and the output shape and order pass.
