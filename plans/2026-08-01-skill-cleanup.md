# Skill cleanup plan

## Goal

Resolve the six cleanup areas identified in the 2026-07-31 skill audit, preserving pressure-tested behavior while reducing ambiguity and cruft.

## Locked decisions

- [x] **Superpowers review-loop boundary:** upstream plan-execution skills own per-task review loops. `adversarial-review-loop` owns cadence, Gate-5, whole-branch, and external review remediation, including its three-cycle cap and cold-read escape.
- [x] **Report compatibility:** retain the local out-of-scope disclosure contract without depending on an upstream heading, status vocabulary, or report shape.
- [x] Record the RED/GREEN boundary scenario in the affected validation records and update README/architecture descriptions in the same change.

## Later cleanup

- [ ] Repair stale and missing validation records.
- [ ] Reconcile Principle 7 and the commit-body example.
- [ ] Tighten skill descriptions to trigger-only metadata.
- [ ] Consolidate redundant skill prose after a working GREEN baseline exists.
- [ ] Move deferred design material out of shipped skill directories and remove ignored workspace cruft.

## Verification for the first slice

- Pressure-test the per-task versus whole-branch routing scenario against the edited skills.
- Run the hook, installer, and research test suites.
- Review the resulting diff against this plan before marking the first slice complete.
