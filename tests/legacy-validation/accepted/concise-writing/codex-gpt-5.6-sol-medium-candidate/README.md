# Accepted CW candidate evidence — Codex / Sol medium

The owner accepted the evidence as valid on 2026-09-09, while explicitly leaving further evaluation and decisions open.
Acceptance covers the complete 66-observation comparison: 22 candidate conditions, three observations each, Codex / gpt-5.6-sol / medium.
It does not adopt the rewritten skill, establish an overall effectiveness result or authorize additional calls.
The unchanged [99-observation baseline](../codex-gpt-5.6-sol-medium/README.md) remains separate.

The [original comparison and ledger](skilltest-cw-candidate.L4NdO8/summary.md) link all scored worksheets and report improvements, failures and limitations under the frozen criteria.
The [final audit](skilltest-cw-candidate.L4NdO8/final-audit.json) reconciles all 66 observations and 267 worksheet links.
The [qualification and reuse record](skilltest-cw-candidate.pITN2u/qualification/summary.md) documents the reused controls and their limits.
No infrastructure retry occurred; three observations per condition remain descriptive, and narration failures remain separate from primary verdicts.
The collection revision is `595f8e2bce0a62c5d4143ffebcdcf30cf8422b0d`; the candidate body digest and source revision remain in the original comparison.

## Preservation and recovery

[evidence.tar.gz](evidence.tar.gz) retains complete run bundles, including fixture Git metadata, and selected supporting approval, qualification and audit records.
The original summaries, worksheets, traces and outputs have directly readable, byte-identical copies alongside it.
`SHA256SUMS` covers the archive and every copied file; run `shasum -a 256 -c SHA256SUMS` from this directory.
Extract the archive only into a fresh scratch directory with `tar -xzf ARCHIVE -C DESTINATION`.
Archive paths are relative to `/private/tmp`; map an original absolute scratch reference to the same suffix beneath the extraction directory.
Repository references identify the recorded input revision; recover those inputs from Git rather than substituting current files.
Original pending-acceptance statements, worktree status, paths and exhausted command approvals are historical provenance; the acceptance note above supersedes their pending status only.
No original worksheet, score, trace, input or scratch package was changed or deleted.
Private runtime profiles, authentication files, unrelated experiments and review transcripts are excluded.
Earlier shared control evidence remains recoverable from the [accepted baseline provenance](../../concise-writing/codex-gpt-5.6-sol-medium/provenance.tar.gz).

Preservation restored 66 complete bundles and supporting evidence from the archive, verifying 2,251 file hashes and permissions and 1,560 explicit directory entries against the sources.
All 1,249 readable copies match their archived source bytes; candidate worksheet hashes and recorded verdicts match the original final audit without rescoring.
