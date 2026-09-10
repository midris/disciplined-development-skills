# Accepted CW evidence preservation

Destination: `skill-validation/accepted/concise-writing/codex-gpt-5.6-sol-medium/` in `.worktrees/cw-validation-design`.
This is storage for the owner-accepted 99 observations, not a runner capability, a scenario migration or a change to the 105 historical records.
Each purpose-separated scenario has one directory containing all declared conditions and three repetitions each.
Whole scenario/provider/model/effort sets are the replacement unit; later owner-accepted sets replace them together, with superseded evidence in Git history.

For each observation preserve the original attempt captures and an archive of the complete original run bundle, including fixture Git metadata.
Keep the worksheet-cited final response, full trace and any clothing-swap guide directly readable at their original relative paths beside the archive; these are byte-identical convenience copies, not separately scored results.
The archive is necessary to retain nested fixture `.git` files without introducing nested repositories into the checkout.
Keep original IDs, timestamps, mechanical fields, scores and scoring-time dispositions unchanged; the top-level acceptance note records the later owner decision.

Retain the two original collection summaries/approval and verification records and selected primary qualification evidence under `provenance.tar.gz`, with scratch-relative paths and a source inventory.
That evidence supports current accepted conclusions; do not copy unrelated experiments, unused fixture preparations, runtime profiles, authentication files or review transcripts.
Provide a short navigation summary and per-scenario counts derived from the accepted worksheets, not new scoring.
Retain archive checksums using standard SHA-256 records.

Before committing, restore every archive into fresh disposable scratch and compare every file and directory against the selected originals, verify readable copies and worksheet links, and reconcile exactly 99 unique observations / 33 conditions / 22 scenarios with the existing accepted count audit.
Refuse existing destinations, symlinks, archive traversal and authentication/runtime files; do not overwrite or remove source evidence.
Verify all retained content is explicitly staged and recoverable before marking preservation complete.
