# Core baseline: partial assessment

Format version: `1`
Assessment ID: `core-baseline-01`
Study / batch: `sweeping-stale-references` / `core-baseline-01`
Status: paused after the first attempt; setup evidence unresolved, batch incomplete.
Scope and acceptance rules: [protocol](protocol.md#core-baseline-core-baseline-01) at Git `4b5ca0cc7aa300962ceb81a031113b7fc1410225`.
Attempt index: [core-baseline-01-run-index.json](core-baseline-01-run-index.json) at Git `13a12403f97458cd2b105b8026f0c9a14f56db7e`, SHA-256 `53e0edee2c23bbb8f21c5c9375e1691d13a527e4e4a92e312f8d3bd2522dbfef`.
Assessor: Codex active session with owner decisions, construction history and prior assessments available; not independent or blind validation.

## Coverage and execution results

The approved scope is three cases × original/control × two executions each, in the fixed protocol order. Only order 1 was attempted; its complete bundle and inventory are retained at the index's absolute paths. No retry or replacement occurred.
[Execution result](results/20260916T184709670Z-ssr-semantic-delivery-original-e957d242-59da-4435-8e0b-61fde0dfa606-fg7h6i02.json) records functional outcomes separately from unresolved setup attribution.
Included attempts: none. The actual attempt `core-baseline-01-semantic-delivery-original-1-1` has setup status `insufficient evidence` and is excluded under the declared valid-setup inclusion rule.

| Case / condition | Planned | Attempted | Setup unresolved | Not attempted |
|---|---:|---:|---:|---:|
| semantic-delivery / original | 2 | 1 | 1 | 1 |
| semantic-delivery / control | 2 | 0 | 0 | 2 |
| moved-guide / original | 2 | 0 | 0 | 2 |
| moved-guide / control | 2 | 0 | 0 | 2 |
| discovery-shiv / original | 2 | 0 | 0 | 2 |
| discovery-shiv / control | 2 | 0 | 0 | 2 |

Inputs/settings and the initial tree match the frozen configuration; the skill is present with its pinned hash. Trace line 5 records a successful command requesting the complete skill, but the captured output omits its text. The next message summarizes the procedure accurately. This supports an attempted read without resolving exactly what full content reached the subject; it is not proof of skill omission or a behavioral failure.
The omission is already present in retained raw CLI stdout. Runner code uses subprocess byte capture and writes those bytes without event filtering; its provider/run/result tests pass (155 offline tests). The successful command, unchanged skill file and subject summary do not recover the missing output. No separate retained provider-event stream was found; the private ephemeral runtime was cleaned up normally. The cause within or before CLI event emission remains unverified.
Collection paused under the existing setup stop rule before order 2. Eleven approved calls remain unspent; do not substitute attempts, change input/capture settings or relax the setup rule silently.

## Aggregate results

All valid-setup counts are zero because no execution is included. The setup-unresolved attempt is accounted for above, not relabelled as a criterion failure or counted as a pass. No success fraction is defined with a zero denominator.

| Case / condition / criterion | Met | Not met | Insufficient evidence | Evidence |
|---|---:|---:|---:|---|
| semantic-delivery / original / F1 | 0 | 0 | 0 | No included execution |
| semantic-delivery / original / F2 | 0 | 0 | 0 | No included execution |
| semantic-delivery / original / F3 | 0 | 0 | 0 | No included execution |
| semantic-delivery / original / P1 | 0 | 0 | 0 | No included execution |
| semantic-delivery / original / P2 | 0 | 0 | 0 | No included execution |
| semantic-delivery / original / P3 | 0 | 0 | 0 | No included execution |
| semantic-delivery / original / functional outcome | 0 | 0 | 0 | No included execution |
| semantic-delivery / control / F1 | 0 | 0 | 0 | No included execution |
| semantic-delivery / control / F2 | 0 | 0 | 0 | No included execution |
| semantic-delivery / control / F3 | 0 | 0 | 0 | No included execution |
| semantic-delivery / control / functional outcome | 0 | 0 | 0 | No included execution |
| moved-guide / original / F1 | 0 | 0 | 0 | No included execution |
| moved-guide / original / F2 | 0 | 0 | 0 | No included execution |
| moved-guide / original / F3 | 0 | 0 | 0 | No included execution |
| moved-guide / original / P1 | 0 | 0 | 0 | No included execution |
| moved-guide / original / P2 | 0 | 0 | 0 | No included execution |
| moved-guide / original / P3 | 0 | 0 | 0 | No included execution |
| moved-guide / original / functional outcome | 0 | 0 | 0 | No included execution |
| moved-guide / control / F1 | 0 | 0 | 0 | No included execution |
| moved-guide / control / F2 | 0 | 0 | 0 | No included execution |
| moved-guide / control / F3 | 0 | 0 | 0 | No included execution |
| moved-guide / control / functional outcome | 0 | 0 | 0 | No included execution |
| discovery-shiv / original / F1 | 0 | 0 | 0 | No included execution |
| discovery-shiv / original / F2 | 0 | 0 | 0 | No included execution |
| discovery-shiv / original / F3 | 0 | 0 | 0 | No included execution |
| discovery-shiv / original / P1 | 0 | 0 | 0 | No included execution |
| discovery-shiv / original / P2 | 0 | 0 | 0 | No included execution |
| discovery-shiv / original / P3 | 0 | 0 | 0 | No included execution |
| discovery-shiv / original / functional outcome | 0 | 0 | 0 | No included execution |
| discovery-shiv / control / F1 | 0 | 0 | 0 | No included execution |
| discovery-shiv / control / F2 | 0 | 0 | 0 | No included execution |
| discovery-shiv / control / F3 | 0 | 0 | 0 | No included execution |
| discovery-shiv / control / functional outcome | 0 | 0 | 0 | No included execution |

Observable outcomes in the excluded attempt: all three current documents are repaired and committed, protected files retain their supplied bytes, and seven controller runtime observations match. Search/triage and one-commit grouping are supported. The non-blocking account defect counts one historical semantic block twice and includes an excluded current code fact; functional repair remains complete.
Acceptance: pending collection; descriptive-only with no threshold. No within-condition frequency, original/control difference or skill benefit can be estimated from this batch. Earlier baseline/pilot observations remain outside its denominator.
Recommendation: investigate the missing CLI command output using existing evidence and offline checks before further dispatch. Preserve the fixed criteria and original skill; the evidence does not justify a skill rewrite. Any change to collection inputs/capture mechanics needs a concrete reviewed scope, and any retry/replacement needs separate authorization. The document generator/validator remains later work, distinct from this observed evidence-capture issue.
