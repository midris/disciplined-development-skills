# Checkbox discipline + nudge cadence — implementation

Implements `2026-06-06-checkbox-discipline-and-nudge-cadence.md` (the design
doc — read it for the what/why/rationale and the two explicit non-changes).
This file carries only the task order + status. One feature branch / PR
(`feature/checkbox-discipline-cadence`).

## Tasks

### Change #2 — `discipline_nudge` cadence + checkbox reminder (test-first)
- [x] Bump `counters.discipline_threshold` default 25 → 50 in
  `lib/dd-defaults.json`; update `test_config` expectation first (RED), then
  the default.
- [x] Add a checkbox-tick reminder line to `discipline_nudge.py`'s fixed
  `REGROUND_TEXT` (flip completed checkboxes in the active plan before
  continuing) — stays state-blind. Update `test_discipline_nudge` first (assert
  the new line present), then the hook.
- [x] Sweep the threshold default in docs: `dd-config.md`,
  `examples/dd-config.json` (no change — key absent), and `README.md` (no
  change — no numeric cite).
- [x] One commit: config + hook + docs + tests together (hook-stack rule).

### Change #1 — `lean-plan-writing` checklist requirement (writing-skills TDD)
- [ ] RED: dispatch a subagent to write an implementation plan WITHOUT the
  requirement; confirm it omits a real task checklist (or emits heading-style
  "tasks" that aren't checkboxes). Capture rationalizations verbatim.
- [ ] GREEN: add the requirement to `lean-plan-writing/SKILL.md` —
  implementation plans MUST carry a one-checkbox-per-deliverable task
  checklist; specs / discussion / deferred docs are exempt.
- [ ] REFACTOR: re-test with a fresh subagent; close loopholes found
  ("headings are basically checkboxes", "too small to need them") with
  rationalization-table rows.
- [ ] Cold-read the staged skill change (`/dd-review cold-read`) before commit
  — no automated test catches a worse instruction (CLAUDE.md substitute).

### Close-out
- [ ] Full hook suite green (`cd disciplined-development/hooks && pytest -q`).
- [ ] Reconcile: tick the design doc's resolution if needed; archive both this
  plan and the design doc to `plans/completed/` after merge.
- [ ] Open PR; merge to main.

## Notes
- The design doc's "Next step" cites `dd_review_runner.py cold-read` for the
  cold-read substitute — stale since the engine rename (the engine takes only
  `pre-pr` directly now); the correct invocation is `/dd-review cold-read`.
  Corrected here; fix the design doc line in close-out if it's load-bearing.
