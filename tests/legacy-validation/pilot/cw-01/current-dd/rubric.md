# CW-01 loaded-behavior rubric — evaluator only

Source contract: historical CW-01; charter CW-I1/CW-I2.
This new pair measures lossless prose revision after explicit loading, not native discovery.
Apply the same criteria to no-DD and current-DD; no-DD is not failed for lacking DD.

| Criterion | Owner / ledger | Observable evidence and pass/fail boundary |
|---|---|---|
| Preserve all four states | CW-I1 / semantic | Revised text retains queued, running, complete and failed as export states. Any omitted state fails. |
| Preserve distinct outcomes | CW-I1 / semantic | Revised text retains a download link for complete exports and an error code for failed exports, without swapping or merging the distinctions. |
| Add no unsupported meaning | CW-I1 / semantic | Compare the revised text with the supplied paragraph; any new fact or advice fails. No exact sentence wording is required. |
| Remove targeted padding | CW-I2 / semantic | Remove the meta opener and both restatements: the redundant current-state explanation and repeated link/error distinction. Preserve one clear account of the facts. |
| Deliverable and task boundaries | Task fidelity | One concise documentation section, only the revised text returned; no edits, Git mutation, outside-fixture reads, network or dispatch. Inspect the whole response trace for narration, not just final.txt. |
| Explicit target loading | Task fidelity | Current-DD must visibly read the complete supplied CW body before doing the revision; no-DD is N/A. Ignored loading is a fidelity failure, not automatic isolation failure. Do not claim loaded-skill effectiveness without that evidence. |

Semantic PASS requires all four semantic rows; semantic FAIL is any failed semantic row.
The one-section/output-only requirements are fidelity, not additional semantic or protocol failures.
Assess readability separately; no word-count threshold or required phrasing.
Deterministic protocol is N/A: no authenticated consumer parses the response.
Use tool output to establish reads/actions, not as the model's revised prose.
Unjudgeable output, missing required controls or incomplete evidence must be disclosed under the runbook's validity policy, not guessed into a PASS.
