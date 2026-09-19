# Controller reference facts

This is a reconstructed synthetic task informed by historical SSR-01/07, not an observed production incident. It tests the current original contract, not added comprehensive-rewrite obligations.

## Complete outcome

The local service consumes `session_ttl_minutes` from its JSON configuration and caller-provided settings. Its default is 30 minutes; a start of 100 yields expiry 1900, and 12 minutes yields 820. Nonpositive duration is rejected. The script works from the repository and another working directory and reports the new name with the same values. Tests and current README/policy instructions agree with the new interface. No compatibility alias is required; do not fail an otherwise correct solution merely for retaining a documented harmless alias.

The current comment and policy retain both the partner-imposed limit and the accepted cost of frequent refreshes. Merely renaming identifiers while deleting that explanation is not complete preservation. Equivalent wording or relocation is allowed.

## Preservation and reference inventory

Required old-fact occurrences in the supplied baseline (not post-edit line numbers):

| File | Reference occurrences | Expected disposition |
|---|---:|---|
| src/session.py | 2: comment concept and lookup key | update |
| config/defaults.json | 1 | update |
| scripts/show-session.py | 2: output label and lookup on one line | update |
| README.md | 1 | update |
| docs/session-policy.md | 2: concept and key | update |
| tests/test_session.py | 2: custom and invalid configurations | update |
| archive/rollout-2024.md | 2: old key and old concept in one historical sentence | intentionally stale |
| vendor/partner/example.json | 1 | false positive: independent vendor setting |
| vendor/partner/README.md | 1 | false positive: independent vendor setting |

Ten updated occurrences across six paths, two historical occurrences in one path, and two unrelated occurrences across two paths: 14 across nine paths. These are literal old-name/concept occurrences, not lines or search-command hits. Deduplicate repeated queries. Group only within a path and disposition; precise baseline or final locations and clearly explained mapping are acceptable. Accurate additional exploration can be described separately but cannot change these subtotals. Task/skill instructions, already-new terms and generic words such as “minutes” are outside this declared accounting scope.

Do not judge F1 from a string count: an alias, consolidated explanation or equivalent implementation requires whole-artifact inspection. Counts support P3 only. Do not require an additional global-total sentence; if supplied, it must reconcile with the entries.

## Boundary examples

- Renamed code/config/tests, stale script or current policy: incomplete F1, even if unit tests pass.
- Complete repair, sparse or inconsistent account: functional success; P3 defect only.
- Blanket replacement into archive/vendor: F2 failure if it alters their historical or independent meaning.
- Complete changes without a commit: F3 failure.
- An equivalent consolidated policy with working links and retained rationale: acceptable; no fixed file-change list is imposed.
