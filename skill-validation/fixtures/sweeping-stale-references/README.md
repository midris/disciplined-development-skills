# Sweeping stale references replay artifacts

These files split the `SSR-01` end-to-end rename into two atomic Task 18A
behaviors. Evaluators receive the current complete skill context and project
fixture, but never the matching rubric.

The current `sweeping-stale-references` SHA-256 is
`d92afd5dc74681d3037b1d5ab2543276698d9cd7b7c0fafc858cfe6b709b5609`.
Its final focused `SSR-01` restart requires the intended new prose-form search as
well as the intended new symbol search.

| ID | Isolated behavior | Prompt SHA-256 | Rubric SHA-256 |
|---|---|---|---|
| `SSR-06` | Exact three-update inventory across symbol and prose encodings, followed by truthful verification | `d9de7958ba1a54e0b36288e16f9d854b9418e41ec26656173a28bb8f8799ffb8` | `286a3a8eab4c9aac655454036fa1b590856f230bf11f0db97841a6d2d0040ccb` |
| `SSR-07` | Preserve the actual causal constraint and accepted tradeoff while renaming the prose form | `41d26783e7b85d33164bd5f3983e52b607aa716e90464768e808ae40f35b2646` | `cf1d686418a9791137c14f539494041b91f32e855c3858ca757dc1f432ce24b7` |

`SSR-01` remains the composite smoke test. It must compose both atomic behaviors
with effective old/new searches, reconciliation, durable `References swept:`
bookkeeping, and observed verification; it must not replace either atomic result.
