# SSR rewrite: focused diagnosis and proposed next experiment

This is a development diagnosis and proposal, not an adopted skill or collection authorization.
The [protocol opening](protocol.md) owns the current decision.
The owner selected the comprehensive rewrite as the development base; the original remains a historical control.
The tested rewrite remains unchanged at [its frozen snapshot](cases/skill-candidate-comprehensive/SKILL.md), SHA-256 `15992341f7ab2fb1e4d8a775092199d7d4e6a9de1167895dbe5a805aeafbd38c`.
Any accepted edits must go in a separate candidate, preserving that snapshot and all existing manifests and scores.

## Evidence and limits

Inspected public text, tool calls and results in twelve retained bundles: Sonnet orders 18, 19, 25, 26, 29–32 and Opus orders 5–8.
Every file listed in those bundles' inventories matched its recorded hash; the inventory hashes also matched the indexes.
No Git commands were run in retained bundles and no evidence was modified.
Line references below refer to each bundle's `stdout.txt`, resolved through the [Sonnet index](claude-comparison-01-run-index.json) or [Opus index](claude-opus-invocation-01-run-index.json).
These are exposed development cases, inspected by the same active session; no independent, blind or held-out claim follows.
No new model calls were made.

| Observation | Evidence | Supported diagnosis |
| --- | --- | --- |
| Loaded rewrite leaves troubleshooting stale | Opus 6, lines 9–15: search returns troubleshooting line 4, but the stale ordinal is on line 3. The subject reads operations in full, edits README and operations, and never reads the complete troubleshooting claim. Post-edit search omits `third`. | A search hit identified the relevant file without exposing the complete claim. The procedure did not ensure contextual inspection before disposition. |
| Paired rewrite run completes the repair | Opus 7, lines 9–14: its first search also shows troubleshooting line 4; it then reads both operations and troubleshooting in full and repairs all three current claims. | Context reading distinguishes this success from the failed pair. This is a plausible mechanism, not proof that a wording change will reliably cause success. |
| Both local rewrite runs use n/a | Sonnet 18, lines 21–45; Sonnet 19, lines 20–41: searches find correct new-form references elsewhere. Order 19 explicitly says they are already correct, then chooses n/a because only the heading needs editing. | The subject substitutes “one file needs an edit” for “all matches are in one file.” The triage list has no outcome for a correct reference to the same fact. |
| Recognition occurs without loading | Opus 5 and 8, line 5: “Stale-reference task; I'll sweep all mentions” and “Stale-reference sweep fits here.” Neither loads SSR; both repair all three docs. | At least these misses are not simply failure to recognize the task type. Recognition and selecting the Skill tool are distinct observable steps. |
| Sonnet misses can also misinterpret read claims | Sonnet 29, line 41 says troubleshooting has no specific count; Sonnet 31, lines 13–16 reads the docs but calls their old policy current. Both omit SSR. | Reading context is necessary for the observed Opus gap but does not guarantee correct interpretation. Compare each complete claim with the settled fact. |
| Successful native runs explicitly select SSR | Sonnet 26, lines 8–15; Sonnet 30, line 36; Sonnet 32, lines 26–27; Opus 7, lines 5–6. | The catalog/tool path works in these cases. Successes do not identify why other calls skipped it. |

The [Sonnet assessment](claude-comparison-01-assessment.md#findings-and-interpretation) also records an original pressure failure after reading the relevant documents and a rewrite success that claimed a post-edit search it had not performed.
The [Opus assessment](claude-opus-invocation-01-assessment.md#findings-and-interpretation) records the successful paired run's search occurring after its commit claimed it had run.
Retain these as separate semantic-interpretation and verification-timing observations, not additional independent functional failures.

## Draft edits for review

The [combined draft](drafts/context-accounting/SKILL.md) applies both proposed body changes to the preserved rewrite.
The owner explicitly requested drafting with writing-skills and concise-writing before new model testing; this authorizes an unvalidated draft, not collection or adoption.
Concise-writing normally excludes skill authoring; its compression pass is applied here at the owner's explicit request, retaining the behavioral requirements.
The description is byte-identical to the tested rewrite.
No existing run configuration points to the draft.
The first proposed experiment still isolates contextual reconciliation: prepare a context-only candidate from the frozen rewrite before freezing inputs; do not dispatch the combined draft in that comparison.

The objective is complete semantic reconciliation and accurate accounting, not additional brevity.
Writing-skills 6.4.1 informs the form: a concrete reading/comparison step, a structural `already current` outcome and template row, and an observable condition for `n/a`.
Concision removes duplicate post-edit timing from Search and gives it one procedural home in Reconcile.
The added wording describes general claims, quantities, conditions and outcomes; it does not teach fixture-specific retry numbers or filenames.

| Draft change | Intended improvement |
| --- | --- |
| Read complete claims or code blocks and compare their meaning before triage | Catch stale facts omitted from search snippets and avoid treating read-but-misunderstood claims as current. |
| Repeat old/new searches and inspect claims after editing, before committing | Check the repaired state before recording verification. |
| Add `already current` to triage and the output template | Account for correct references to the same fact without calling them false positives. |
| Count all four triage outcomes in the single-file boundary | Preserve the accepted `n/a` rule even when an outside-file match is already current, historical or unrelated. |
| Exclude only navigation/context that neither matches an old/new form nor encodes the fact | Keep incidental context out without silently discarding genuine false-positive matches. |

An outside-file old-name match in an unrelated helper therefore requires a positive inventory with a false-positive entry.
A generic heading encountered only while navigating to the changed file does not by itself prevent `n/a`.
The accounting change still requires prospective controller criteria before testing; historical scores remain unchanged, and reporting defects remain procedural.
This draft has received a text/contract review only; it has no new model-validation evidence.

**Invocation:** leave the description unchanged in these body experiments.
Both tested versions use byte-identical descriptions, and the body cannot explain selection differences before it is loaded.
The traces do not expose complete initial production requests or establish a causal explanation for skipping selection.
A description experiment remains possible later, but a new description is not yet justified as the remedy for these observed misses.
Do not insert “load this skill” into native task prompts and call that automatic invocation improvement.

## Recommended allocation: first stage only

Request **15 additional subject calls**, raising the spent/authorized ceiling from 136 to at most 151 if approved.
Use the existing semantic-delivery fixture/task with Claude Opus 5.5 low effort: it is the explicit-load counterpart of the failed native repair.
Use five fresh contexts each for no SSR, the unchanged tested rewrite, and the contextual-reconciliation candidate.
Only the full-load instruction and skill availability differ in the no-SSR arm; keep task, fixture, permissions and common setup identical.
Both skill arms explicitly load the complete body, isolating execution from discovery.
Do not include the original baseline in this experiment: the question is whether the proposed change improves the selected rewrite.

Run the five no-SSR controls first, before freezing or dispatching a candidate.
The owner's explicit draft request changes the authoring order; it does not satisfy writing-skills' no-guidance validation requirement.
If none exhibits incomplete reconciliation, stop at five calls and report that the new control does not supply the required RED; do not manufacture a failure or dispatch the remaining ten automatically.
If the control exposes the target failure, freeze the accepted candidate and run five unchanged-rewrite and five revised-rewrite trials, alternating their order across repetitions.
Retain every attempt; no retries or replacements are allocated.
Setup problems stop dispatch for diagnosis rather than consuming an undeclared replacement pool.

Keep existing F1–F3 complete-repair, preservation and committed-outcome criteria.
Record context reading, comparison of claims and verification timing as declared procedural observations, not extra functional successes or failures.
Inspect the whole final project and actual command outputs; passing runtime tests cannot establish documentation correctness.
Five repetitions support descriptive comparison only.
Candidate 5/5 complete repairs with preservation and a weaker unchanged-rewrite result supports progression; a tie supplies no demonstrated improvement, and any candidate functional failure requires inspection before progression.
Neither result authorizes adoption or establishes population reliability.

Pin the actual available CLI/model settings and runner revision before dispatch, repeat the installed Claude/Git/isolation preflight and existing fixture checks, and do not pool with earlier runtime versions.
Estimate 45 active minutes for preparation, up to 15 calls, evidence inspection and close; time remains a guideline.
Model availability and runtime pins remain preflight facts, not assumptions imported from the historical batch.

Later work is conditional and unallocated: a five-per-arm accounting comparison needs its own no-guidance interpretation (an unprompted control cannot fail SSR-specific reporting rules), and the semantic change needs pressure/application regression coverage before adoption.
Reconsider the existing facet map for affected ordinary cases at that point; a micro-test does not replace full relevant application/pressure testing.
Invocation testing remains a separate native-availability experiment with timely loading as its primary measure.
No extra scenario suite, authoring model, evaluator model or broad comparison is requested now.
