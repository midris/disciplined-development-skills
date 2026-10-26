# Candidate screen progress

Owner-approved scope: 115 new subjects and ten complete-output reviews; immutable invocation authority `eb1761bb7014034a174877d548898417ac4d2030`.
The active plan owns the remaining checklist; this note records the current evidence boundary.

## Resumption after authentication stop

All dispatch stopped at slot 56 on 2026-10-26 after Claude returned HTTP 401: OAuth access token expired.
The runner recorded `INFRA_ERROR`, exit 1, with no timeout or cleanup error.
No subject tool call or actual model output occurred; all twelve supplied files remain unchanged.
The complete error capture and invalid-setup assessment are retained in the Claude index; absence of skill loading is not scored as successful non-use.
The invocation started, so its one subject charge is retained even though the provider reported zero tokens/cost.
No retry, replacement or reviewer was launched before the stop.

The owner re-authenticated Claude and approved exactly one retry on 2026-10-26; production authentication and unchanged runtime hashes were verified.
The [retry authorization](retry-56-authorization.md) governs distinct retry registration and full-index checks.
Slot 57 is the next unattempted slot; preserve slot 56 as invalid and do not silently replace it.
Run the approved retry of slot 56 before slot 57, retaining its parent; no additional retry is authorized.
There are 59 unattempted subject slots and ten unattempted reviewers.
Do not repeat slots 1–55 or make any second retry of slot 56. Check private claims/outcomes and indexes before dispatch.
The invocation guard must select the valid, scored approved retry for slot 56 before further dispatch, without weakening other setup or functional-stop checks.

## Retained outcomes

Slots 1–55 are valid and scored; all 42 repair outcomes meet F1–F3.
Thirteen valid accounting/non-use observations have no functional denominator.
All 21 native D1 observations meet their case-specific criteria (twelve positive and nine negative).
Valid P3 judgments: eighteen met, ten not met and six insufficient evidence.
Reporting defects and inherited Shiv category uncertainty remain separate from functional outcomes; no candidate has reached a functional early-stop trigger.
The partial screen supports no adoption or final comparative verdict; ten planned complete-output reviews remain unrun.

Runtime, immutable input and prior-score checks preceded every invocation.
The checkpoint audit verifies all 56 retained captures, private/canonical score equality and pinned evidence hashes, separating the one invalid setup from 55 valid outcomes.
Whole-artifact and ordered-trace inspections support unchanged fixed cards; independent runtime replay covers all repair cases.
No skill edit or new criterion was introduced; the separate retry allocation does not change scoring rules.
Raw evidence stays in the approved external candidate-screen-01 store.
The user CW fixture hash remains `a15c5e668af77a1dfef81dd01c5524ae4ce742542cc63f4f6d55e740ee0ac488` and its edit remains unstaged.

Execution effort through this stop is estimated at 85 active minutes, including model waits, approval/freeze/readiness, direct assessment and stop documentation; combined accounting is in the CW protocol.
