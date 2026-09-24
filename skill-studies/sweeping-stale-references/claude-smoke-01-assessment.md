# Claude testing path smoke: assessment

Format version: `2`
Assessment ID: ssr-claude-smoke-01
Study / batch: sweeping-stale-references / claude-smoke-01
Status: complete; both authorized attempts retained and assessed
Scope and acceptance rules: [protocol](protocol.md) at Git `c3ce25292ba9f4fd9e049f8b7e084fdf70d705ec`, batch claude-smoke-01; fixed Shiv and invocation-review criteria under SSR policy 3.
Attempt index: [claude-smoke-01-run-index.json](claude-smoke-01-run-index.json) at Git `06dcf069a64d0055dc8a2308305b693df1d6fafb`, SHA-256 `a13230a0283027d24275f54c927a772d6f2672917348543775a65d8a4c6c02b1`.
Assessor and relevant session context: Codex active session that prepared the runner and inspected these exposed cases; not independent or blind.

The runner completes authenticated Claude model sessions and retains usable evidence.
Explicit-load Shiv repair succeeds; automatic SSR invocation fails in the reviewer-triggered smoke, which leaves two current documentation claims stale.
These are separate findings: transport/execution viability is established for these observations, while automatic invocation is not reliable enough to claim success from this smoke.

## Coverage and execution results

Both planned attempts used original SSR, Claude Code 2.1.280 and `claude-sonnet-5`, low effort, workspace-write, in the declared order.
Both have valid setup, complete terminal traces, clean final Git trees and no unresolved cleanup.
No retries, replacements, exclusions or unattempted slots exist.
All execution-result records resolve through the pinned index.
Provider adaptations are limited to `.claude/skills` placement, the explicit-read path and the ignored skill-directory name.
The original skill body and project/task content are unchanged.
Both production native init events list SSR plus sixteen bundled skills, with no plugins or MCP servers.
Catalog names are captured in production; complete initial request payloads are not. Same-CLI scripted qualification separately proves description delivery and full body delivery after Skill invocation.

| Case / condition | Planned | Attempted | Included | Invalid setup | Setup unresolved | Unattempted |
| --- | --- | --- | --- | --- | --- | --- |
| discovery-shiv / original | 1 | 1 | 1 | 0 | 0 | 0 |
| invocation-review / original | 1 | 1 | 1 | 0 | 0 | 0 |

| Order | Case | Condition | Repetition | Setup / coverage | Recorded outcome | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | discovery-shiv | original | 1 | valid | met | [claude-smoke-01-discovery-shiv-original-1](results/20260924T054817624Z-ssr-claude-smoke-discovery-shiv-501b800a-6002-4d2b-b8d0-27071722df77-b6w3iym1.json) |
| 2 | invocation-review | original | 1 | valid | not met | [claude-smoke-01-invocation-review-original-1](results/20260924T055130021Z-ssr-claude-smoke-invocation-review-616e70a7-4aa3-4f58-af10-9776e72becf6-sa7ut8hv.json) |


## Aggregate results

| Case / condition / criterion | Met | Not met | Insufficient evidence | Not measured | Evidence |
| --- | --- | --- | --- | --- | --- |
| discovery-shiv / original / F1 | 1 | 0 | 0 | 0 | [claude-smoke-01-discovery-shiv-original-1](results/20260924T054817624Z-ssr-claude-smoke-discovery-shiv-501b800a-6002-4d2b-b8d0-27071722df77-b6w3iym1.json) |
| discovery-shiv / original / F2 | 1 | 0 | 0 | 0 | [claude-smoke-01-discovery-shiv-original-1](results/20260924T054817624Z-ssr-claude-smoke-discovery-shiv-501b800a-6002-4d2b-b8d0-27071722df77-b6w3iym1.json) |
| discovery-shiv / original / F3 | 1 | 0 | 0 | 0 | [claude-smoke-01-discovery-shiv-original-1](results/20260924T054817624Z-ssr-claude-smoke-discovery-shiv-501b800a-6002-4d2b-b8d0-27071722df77-b6w3iym1.json) |
| discovery-shiv / original / P1 | 1 | 0 | 0 | 0 | [claude-smoke-01-discovery-shiv-original-1](results/20260924T054817624Z-ssr-claude-smoke-discovery-shiv-501b800a-6002-4d2b-b8d0-27071722df77-b6w3iym1.json) |
| discovery-shiv / original / P2 | 1 | 0 | 0 | 0 | [claude-smoke-01-discovery-shiv-original-1](results/20260924T054817624Z-ssr-claude-smoke-discovery-shiv-501b800a-6002-4d2b-b8d0-27071722df77-b6w3iym1.json) |
| discovery-shiv / original / P3 | 0 | 1 | 0 | 0 | [claude-smoke-01-discovery-shiv-original-1](results/20260924T054817624Z-ssr-claude-smoke-discovery-shiv-501b800a-6002-4d2b-b8d0-27071722df77-b6w3iym1.json) |
| discovery-shiv / original / functional outcome | 1 | 0 | 0 | 0 | [claude-smoke-01-discovery-shiv-original-1](results/20260924T054817624Z-ssr-claude-smoke-discovery-shiv-501b800a-6002-4d2b-b8d0-27071722df77-b6w3iym1.json) |
| invocation-review / original / F1 | 0 | 1 | 0 | 0 | [claude-smoke-01-invocation-review-original-1](results/20260924T055130021Z-ssr-claude-smoke-invocation-review-616e70a7-4aa3-4f58-af10-9776e72becf6-sa7ut8hv.json) |
| invocation-review / original / F2 | 1 | 0 | 0 | 0 | [claude-smoke-01-invocation-review-original-1](results/20260924T055130021Z-ssr-claude-smoke-invocation-review-616e70a7-4aa3-4f58-af10-9776e72becf6-sa7ut8hv.json) |
| invocation-review / original / F3 | 0 | 1 | 0 | 0 | [claude-smoke-01-invocation-review-original-1](results/20260924T055130021Z-ssr-claude-smoke-invocation-review-616e70a7-4aa3-4f58-af10-9776e72becf6-sa7ut8hv.json) |
| invocation-review / original / D1 | 0 | 1 | 0 | 0 | [claude-smoke-01-invocation-review-original-1](results/20260924T055130021Z-ssr-claude-smoke-invocation-review-616e70a7-4aa3-4f58-af10-9776e72becf6-sa7ut8hv.json) |
| invocation-review / original / functional outcome | 0 | 1 | 0 | 0 | [claude-smoke-01-invocation-review-original-1](results/20260924T055130021Z-ssr-claude-smoke-invocation-review-616e70a7-4aa3-4f58-af10-9776e72becf6-sa7ut8hv.json) |

## Findings and interpretation

Shiv: every required consumer builds and executes the correct greeting archive; the script works from either directory, current long option and short alias work, the retired option is rejected and the independent inventory tool remains functional.
Only the four consumers change after baseline, in one commit.
The explicit SSR read is complete and precedes repair searches/edits.
P3 retains the known category mismatch: the subject calls the two deliberate negative assertions “intentionally stale”, while frozen expected facts call them false positives.
No separate numerical inconsistency was found; this recorded procedural failure does not establish a new skill defect or affect functional success.

Native review: SSR appears in the catalog, but there is no Skill invocation or SSR body read anywhere in the complete trace.
Claude reads the other current documents and then changes only README.
Operations still permits two further tries, and troubleshooting still exhausts after the third failed send, both contradicting the worker's four total attempts.
The unchanged seven behavior tests pass; they do not test documentation meaning.
F1 and F3 fail from the same incomplete repair, F2 passes, and D1 fails independently of task correctness.
One observed miss supports investigation, not an estimated invocation failure rate or a causal claim that loading SSR would necessarily have prevented this outcome.

Both smokes recover from denied zsh heredoc temporary-file creation; Shiv also recovers from a built-in Write restriction on a `.git` path by using a normal workspace file.
Neither restriction prevents the final task commit or the observed pre-edit content access.
The later `TMPPREFIX` runner correction passes actual-CLI regression tests in both permission modes without additional model calls.
These live observations remain pinned to their original runtime revision; they are not claimed as live validation of that later correction.

Acceptance under the declared rule: descriptive-only, one functional success and one functional failure; native invocation failed its single observation.
The requested minimal Claude testing exercise is complete. No further model calls or skill edits are selected.
The next substantive decision is whether to investigate the native invocation miss; candidate adoption remains deferred.
Resource accounting is in [CW accounting](../concise-writing/protocol.md#storage-and-accounting): two calls, combined 92/92; no extra calls were spent on scripted qualification.
