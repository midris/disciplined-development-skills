# SSR complete-claim inspection screen

Format version: `2`
Assessment ID: ssr-complete-claim-01
Study / batch: sweeping-stale-references / complete-claim-01
Status: focused screen complete; all eight repairs and both audited output reviews pass. No adoption or full regression.
Assessor: active Codex preparer/assessor with prior/version awareness; not blind or independent.
Scope: [design](../../../../plans/specs/2026-10-31-ssr-complete-claim.md), [frozen schedule](preparation/schedule.json), SSR-count-free-1 and unchanged F1–F3/D1 criteria.

## Results

| Provider | Body | Complete repairs | Timely complete loads | Complete troubleshooting claim read before classification |
| --- | --- | ---: | ---: | ---: |
| Codex | Previous paragraph | 2/2 | 2/2 | 2/2 |
| Codex | Revised paragraph | 2/2 | 2/2 | 2/2 |
| Claude | Previous paragraph | 2/2 | 2/2 | 2/2 |
| Claude | Revised paragraph | 2/2 | 2/2 | 2/2 |

All eight executions repaired README, operations and troubleshooting consistently, including changing exhaustion from the third to the fourth failed send.
Every repair is committed, retains stopping on success and operator guidance, and preserves worker/helper behavior, historical documentation, TASK.md and .gitignore.
All eight disposable runtime checks pass seven tests; those tests support behavior preservation, not documentation correctness.
There were no setup exclusions, retries or subject replacements.

The revised wording passes this focused screen, but the previous wording also passes every fresh comparison run.
This does not demonstrate a reliability improvement, establish superiority or erase the earlier observed failure.
It supports broader validation of the exact candidate combination without further wording changes; the shipped skill remains unchanged.

## What the traces show

Both arms use the same selected draft description from description-discovery-01.
Only the agreed inspection paragraph differs: the candidate requires reading the complete claim or code block before classification instead of making that read conditional on whether a snippet seems sufficient.
Name, task/project bytes, native availability, models and low-effort settings are fixed.

All four revised-body runs receive the full troubleshooting claim before classifying it.
Codex repetition 1 uses `rg -C 4`, which delivers the missing ordinal despite its search pattern not matching that line directly.
Codex repetition 2 and both Claude repetitions read the complete troubleshooting file after searches that omit the first line of the stale sentence.
All four previous-body runs also read the complete claim, using full-file reads and, in one case, search context.
The [inspection observations](inspection-observations.json) record this diagnostic separately from scored outcomes.
It demonstrates successful inspection of this claim, not universal compliance with the revised requirement for every code/test reference; some unchanged code/test dispositions still rely on snippets.

## Consequential quality and reporting

All final operational guidance remains useful; no required correction or preservation reason is hidden by reporting defects.
Candidate Codex repetition 1 makes the minimal README edit to “at most four delivery attempts”; the operations guide supplies the three-retry framing.
The other seven READMEs state both total attempts and retries explicitly.
That small presentation difference is acceptable and does not establish a condition-level advantage.

Some inventories group different paths or omit search matches.
Claude candidate repetition 2 claims a repeated post-edit search that does not occur in the retained trace, and Claude previous-body repetition 2 performs a search but summarizes its remaining legitimate three-retry matches incorrectly.
These claims are recorded separately from independently verified repair completeness, under the owner's repair-first policy.
The candidate does not fix these broader verification/reporting weaknesses.

## Review and evidence

Two Opus-medium read-only packets cover all eight complete outputs, four per provider, with separate first-pass judgments before access to active priors.
Both reviews agree with all 24 functional factors across eight executions, with no post-prior judgment changes; these are not 24 independent tests.
See [evaluation](evaluation/README.md) for delivery audits, all functional factors, reviewer caveats and reconciliation.
The reviewer differs from the active Codex assessor and shares the Claude subjects' model family; condition labels remain visible.
Native loading and inspection order are active-session trace judgments, not independent output-review judgments.

Source authority: `c05b5f01a0fef4178b2a019dc8b502a6f29d3406`; manifest/dispatch authority: `89124ef`.
The exact [previous](preparation/skills/current/SKILL.md) and [revised](preparation/skills/candidate/SKILL.md) test copies preserve the selected draft description.
The unchanged qualified runtime is Codex 0.166.0 / gpt-5.6-sol low and Claude 2.1.312 / claude-opus-5-5 low; output reviewers use Opus medium with Read/Glob/Grep only.
All original baseline blobs, configured final files, model/tool identities, complete captures and inventories were inspected.

A reused packet-building helper refreshed Git index stat caches despite `--no-optional-locks`.
Only the eight retained `.git/index` files changed; project files, Git objects/commits, traces, outputs and review inputs were unchanged.
Exact original index bytes were restored from intact full source captures after preserving the altered copies; every complete inventory verifies again.
A disposable reproduction confirms the cause and verifies `diff.autoRefreshIndex=false` prevents it.
The [incident record](retention-incident-01.json) preserves the recovery; no model execution was repeated.

Canonical [scores](results/) and provider tables ([Codex](claim-codex-01-assessment.md), [Claude](claim-claude-01-assessment.md)) preserve all outcomes.
[Verification](verification.json) records runtime durations and integrity checks.
Both provider assessment-readiness checks pass with canonical result/index pins and reconciled invocation totals.
The hook suite passes 263 tests with three environment skips in 21.66 seconds using the runner virtualenv; the system Python lacks pytest.
The unrelated CW fixture edit remains unchanged and unstaged.

## Limits and next step

This is the owner-selected loaded-failure refactor screen: two repetitions per body/provider on one exposed native reviewer case.
It is not a no-guidance contribution experiment, a five-repetition decision stage, a complete discipline-pressure campaign, negative-selection validation or full regression.
No failed old-body run occurred in this fresh screen; the historical failure remains separate evidence under its original inputs.

The next useful scope is broader application and native-selection regression on both providers, including near-boundary non-use, using the exact revised paragraph and fixed description.
Do not add more wording to respond to a failure that did not recur here.
That broader scope needs its own frozen allocation; this screen grants neither automatic promotion nor resumption of the cancelled description schedule.

## Accounting

All eight subjects and two output reviews are spent, with no retries or authoring calls.
Combined spending is 975 subjects / 80 evaluators / 0 authoring / 4 retries; SSR subset is 469 / 32 / 0 / 1.
The remaining numeric capacity of 59 subjects/six reviews does not authorize another experiment or revive cancelled slots.
Subject and review runner durations total 444.849 seconds (193.194 + 251.655), included once in 30 estimated active minutes for diagnosis, preparation, execution, review, recovery and closure.
The [CW ledger](../../../concise-writing/protocol.md#storage-and-accounting) owns combined effort; this is a rounded estimate, not billed cost or a stopwatch measurement.
