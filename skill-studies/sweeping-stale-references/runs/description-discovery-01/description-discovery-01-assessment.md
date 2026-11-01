# SSR description discovery: early-stop assessment

Format version: `2`
Assessment ID: ssr-description-discovery-01
Study / batch: sweeping-stale-references / description-discovery-01
Status: stopped at focused slot 13; full stage not opened; candidate not adopted.
Assessor: active Codex preparer/assessor with version/history awareness; not blind or independent.
Scope: [staged design](../../../../plans/specs/2026-10-31-ssr-description-discovery.md), [frozen schedule](preparation/schedule.json), [stop record](early-stop.json).

## Decision

Stop the current comparison at the first consequential failure, as requested.
Thirteen subjects completed and were retained/scored; 67 scheduled subjects and all eight allocated reviews remain unrun and are cancelled pending a revised proposal.
There were no retries, substitutions or setup exclusions.
The shipped description and body remain unchanged.
This is an early rejection under the fixed gate, not a completed comparison or an adoption recommendation; independent output reviews were therefore not dispatched.

## Observed results

| Provider | Description | Timely positive loads | Complete repairs | Correct verification-only non-use |
| --- | --- | ---: | ---: | ---: |
| Claude | Current | 1/2 | 2/2 | 1/1 |
| Claude | Candidate | 2/2 | 2/2 | 1/1 |
| Codex | Current | 2/2 | 2/2 | 1/1 |
| Codex | Candidate | 3/3 | 2/3 | 1/1 |

Only the second Codex candidate reviewer case ran beyond the first repetition; do not interpret the unequal denominators as a balanced comparison.
All five candidate positive observations loaded the complete skill before editing; all four verification-only observations avoided loading/application and ran the requested tests once.
The Claude current reviewer run missed loading despite saying “A reviewer flagged one stale reference; sweep for others.”
Its repair was complete.
These small exposed observations are encouraging for recognition, but cannot establish improvement, reliability or a causal effect of the description.
No unrelated-explanation observation ran.

## Failure that stopped collection

Slot 13: Codex, candidate description, reviewer correction, repetition 2.
The complete skill arrived before editing; D1 is met.
The subject corrected README and operations documentation but left this current troubleshooting claim unchanged:

> For the current notification worker, the third consecutive failed send exhausts
> automatic delivery attempts.

The settled policy permits four total attempts, so exhaustion must occur after the fourth failed send.
The repair commit `a89315b` incorrectly classifies `docs/troubleshooting.md:3-8` as already current, citing success termination and operator follow-up while missing its stale exhaustion condition.
F1 and F3 are not met from the same incomplete-repair cause; F2 is met.

The trace shows the mechanism: the first grep matches the troubleshooting heading and adjacent lines but misses the sentence containing “third consecutive failed send”; the subject reads several other files in full but never reads this complete claim.
Its later search also misses that phrasing.
All seven code tests pass because they check worker/helper execution, not the meaning of documentation.
The active assessor inspected the full unchanged troubleshooting file, committed tree and trace, and reproduced the passing runtime checks in a disposable copy.

The existing body already instructs the agent to read complete claims when snippets do not establish disposition, including quantities, conditions and outcomes.
This observed failure is incomplete application after successful loading; it does not show that broader description wording caused the miss.
A useful next investigation would isolate that missed full-claim inspection before choosing any further description or body change.
No new variant or experiment is selected by this assessment.

## Other quality observations

Eight of nine repair outputs are complete, preserved and committed.
The first candidate Claude reviewer run falsely claims a repeated post-edit search; its trace contains none, and its statement that only historical/helper “three” matches remain ignores legitimate current retry prose.
Both descriptions retain some grouping defects in commit inventories, and one candidate Codex rename commit uses literal backslash-n separators.
These reporting defects did not obscure the complete repairs and were kept separate under the owner’s repair-first policy.
The slot-13 false “already current” classification is consequential because the document itself remains wrong.

## Evidence and limits

Input authority: `e4d58cca72b0469d87595a6e4b9911f2b0eba81d`; manifest/dispatch authority: `52b8920`.
The exact [current](preparation/skills/current/SKILL.md) and [candidate](preparation/skills/candidate/SKILL.md) files differ only in description; body/name, project fixtures and prompts are unchanged.
Both provider collection-readiness checks passed before dispatch.
Qualified executable/wrapper hashes and resolved paths match the preceding count-free regression: Codex 0.166.0 / gpt-5.6-sol low; Claude 2.1.312 / claude-opus-5-5 low.
All 13 inventories and actual model/tool identities verify; Codex provider sessions retain exact assigned descriptions and nested tool outputs.
Sandbox-denied parent searches and the system Perl checksum utility were recovered within subjects; they did not lose capture or alter required task inputs.
No retention incident occurred.

[Verification](verification.json) records counts and durations; canonical [results](results/) link each complete raw bundle, trace and replay.
Provider tables retain all unattempted scope: [Codex](discovery-codex-01-assessment.md), [Claude](discovery-claude-01-assessment.md).
This is an exposed, early-stopped development screen with no independent output review, population-reliability, full-catalog, DD-composition or causal contribution claim.
Historical evidence is unchanged.

## Accounting

New spending: 13 subjects, zero reviewers, zero authoring calls and zero retries.
Combined spending: 967 subjects / 78 evaluators / 0 authoring / 4 retries; SSR subset: 461 / 30 / 0 / 1.
The unspent 67/eight conditional subject/review slots are not active dispatch authority after the stop.
Subject runner durations total 255.672 seconds, included once in approximately 25 estimated active minutes for preparation, dispatch waits, direct inspection, verification and closure.
The 60–100-minute focused forecast was cut short by early stopping; this is not a completed-stage efficiency comparison or billed-cost measurement.
The [CW ledger](../../../concise-writing/protocol.md#storage-and-accounting) owns combined effort.
Both provider assessment-readiness checks pass; their completeness flag validates retained assessment records, not completion of unattempted testing.
Hook suite: 263 passed, three environment skips in 22.11 seconds.
The unrelated CW fixture edit remains unchanged and unstaged.
