# Accepted procedure-pilot evidence — Codex / Sol low

The owner accepted the evidence as valid on 2026-09-09, while explicitly leaving further evaluation and decisions open.
These 14 observations exercised the collection, scoring and handoff procedure; their original judgments and caveats remain unchanged.
They are not effectiveness estimates, authoring RED/GREEN acceptance or additional controls for the accepted CW baseline.

- [Initial pilot: four DR-02/LP-01 observations](skilltest-sol-low-pilot.Lunoau/summary.md).
- [Extension: six DR-05/LP-05/AR-03 observations](skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/summary.md).
- [CW procedure: four loaded/discovery observations](skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/summary.md).

Two original real qualification calls are retained separately from the 14 scored observations.
All three batches used Codex / gpt-5.6-sol / low; original per-run CLI provenance, input revisions, command approvals and disclosed warnings remain attached to each observation.

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

Preservation restored 16 complete bundles (14 observations and two qualification calls) and supporting evidence from the archive, verifying 571 file hashes and permissions and 335 explicit directory entries against the sources.
All 375 readable copies match their archived source bytes.
