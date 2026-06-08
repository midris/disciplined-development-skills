# Checkbox discipline + nudge cadence — implementation

> **ARCHIVED — largely scrapped in favour of the hook change.** Change #2
> (discipline cadence 25→50 + checkbox-tick reminder, commit `2983139`) shipped.
> Change #1 (the `lean-plan-writing` checklist rule) was dropped in favour of
> the `session_reground` change that re-loads **dd + superpowers** on every
> session (re)start (commit `7f18453`) — the real long-session failure was
> losing those skills, not a missing plan checklist. See that commit for the fix.

Implements `2026-06-06-checkbox-discipline-and-nudge-cadence.md` (the design
doc — read it for the what/why/rationale and the two explicit non-changes).
This file carries the task order + status. One feature branch / PR
(`feature/checkbox-discipline-cadence`).

## Tasks

### Change #2 — `discipline_nudge` cadence + checkbox reminder (test-first) ✅
- [x] Bump `counters.discipline_threshold` default 25 → 50 in `lib/dd-defaults.json`
  (test_config RED first). Commit `2983139`.
- [x] Add a state-blind checkbox-tick reminder to `discipline_nudge.py`'s
  `REGROUND_TEXT` (test_discipline_nudge RED first).
- [x] Doc sweep: `dd-config.md` 25→50; `examples/dd-config.json` + `README.md`
  needed no change (key absent / no numeric cite).

### Reground re-loads dd + superpowers (added mid-flight) ✅
Not in the original design doc — added after the owner re-diagnosed the
root cause: the real long-session failure was the model losing **both** dd and
superpowers, not a missing plan checklist.
- [x] `session_reground.py` `COMMON_BODY` now names dd **and** superpowers (via
  `using-superpowers`) and warns not to assume they survived a long/compacted
  session. Test-first (`test_common_body_reloads_dd_and_superpowers`). Commit
  `7f18453`. This hook fires on `compact`/`resume` — exactly the failure moment.

### Change #1 — `lean-plan-writing` checklist requirement — DESCOPED (pending confirm)
**Dropped in favour of the reground fix above.** *Why:* the RED baseline showed
a plan written under the current skills already carries a per-deliverable
`- [ ]` checklist, because `superpowers:writing-plans` owns the checkbox
scaffold and `lean-plan-writing` doesn't override it. The real-world
zero-checkbox failure came from the model *losing* superpowers (so
`writing-plans` never ran), which the reground tweak now fixes at the root.
Adding a redundant "require checkboxes" rule to `lean-plan-writing` addresses a
symptom the reground already prevents. *Accepted:* if a future session writes a
plan without `writing-plans` loaded AND the reground is bypassed, checkboxes
could still be missed — low likelihood, revisit only on recurrence.
- [~] RED baseline run (confirmed checkboxes already appear) — evidence for the descope.
- [ ] ~~GREEN / REFACTOR / cold-read~~ — not done (descoped).

### Close-out
- [x] Full hook suite green (275 passed, 3 skipped).
- [ ] Reconcile the design doc: record the change #1 descope + the reground
  addition; fix its stale `dd_review_runner.py cold-read` line → `/dd-review cold-read`.
- [ ] Open PR; merge to main; archive this plan + the design doc to `plans/completed/`.
