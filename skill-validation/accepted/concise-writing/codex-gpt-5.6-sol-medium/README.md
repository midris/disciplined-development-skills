# Accepted CW baseline — Codex / Sol medium

Owner-accepted on 2026-09-08: 99 observations, 33 conditions, 22 purpose-separated scenarios; three observations per condition.
Provider/model/effort: `codex / gpt-5.6-sol / medium`.
Actual CLI: `codex-cli 0.153.4`; executable `/opt/homebrew/bin/codex`, SHA-256 `b973d440acac501fd2594a43e7ca9ce41e0a65b9dfb28d0d7a7837c99e1261e3`.
These are the accepted current-DD/no-DD baselines, not results for the rewritten candidate.
All scores and original worksheet dispositions remain byte-for-byte unchanged; this later owner acceptance supersedes their scoring-time pending status.

## Results and evidence

Each scenario directory is a complete provider/model/effort replacement unit, including all declared conditions, repetitions and failures.
`loaded` means the explicitly loaded task variant: CW-07 is transport, CW-13/14 are composition decisions, and the remaining loaded variants test prose.
Discovery, description and contract variants retain their separate meanings.
Each scenario summary links unchanged worksheets and complete bundle archives; worksheet-cited final responses, full traces and any written guide are directly readable at the original relative paths.

- [cw-01-discovery](cw-01-discovery/summary.md)
- [cw-01-loaded](cw-01-loaded/summary.md)
- [cw-02-loaded](cw-02-loaded/summary.md)
- [cw-03-loaded](cw-03-loaded/summary.md)
- [cw-04-loaded](cw-04-loaded/summary.md)
- [cw-05-loaded](cw-05-loaded/summary.md)
- [cw-06-loaded](cw-06-loaded/summary.md)
- [cw-07-loaded](cw-07-loaded/summary.md)
- [cw-08-loaded](cw-08-loaded/summary.md)
- [cw-09-description](cw-09-description/summary.md)
- [cw-10-contract](cw-10-contract/summary.md)
- [cw-11-description](cw-11-description/summary.md)
- [cw-12-contract](cw-12-contract/summary.md)
- [cw-13-discovery](cw-13-discovery/summary.md)
- [cw-13-loaded](cw-13-loaded/summary.md)
- [cw-14-discovery](cw-14-discovery/summary.md)
- [cw-14-loaded](cw-14-loaded/summary.md)
- [cw-17-contract](cw-17-contract/summary.md)
- [cw-17-discovery](cw-17-discovery/summary.md)
- [cw-18-contract](cw-18-contract/summary.md)
- [cw-18-discovery](cw-18-discovery/summary.md)
- [cw-19-loaded](cw-19-loaded/summary.md)

Report primary outcomes separately from fidelity, readability and infrastructure; there is no pooled catalog score or automatic GREEN/deployment threshold.
Three observations are small descriptive samples.
Repetitions across arms are not matched experimental pairs.
The fixed-order, noncontemporaneous sampling and laptop-sleep gap remain disclosed in the original complete-set summary; no provider retry was needed.
Body reads were checked against full traces; hidden provider inputs and automatic shell startup remain observability limits.

## Recoverable provenance

81 observations used input revision `dfd638ce5c1ac5f654110d05ce9138e5384d6afc`, from scratch package `skilltest-cw-baseline.bOn8Dx`.
The other 18 used `6fb4780fce37710a76116dbbeaa832a6a42289cd`, from `skilltest-cw-baseline.ksDeiD`: CW-08/CW-19 loaded no-DD/current-DD and CW-01/CW-17 discovery, three each.
Recover evaluator rubrics and linked guidance from the observation's input revision, not a later checkout.
Every archive also retains that run's actual config, prompt, complete input/output inventory, full trace and runner log.

[Supporting provenance](provenance.tar.gz) preserves the original collection summaries, approval records, audits and selected primary qualification evidence with paths relative to `/private/tmp`.
This is evidence supporting the current accepted set, not an archive of unrelated or superseded experiments.
After extracting it to a fresh directory, the original complete-set ledger is `skilltest-cw-baseline.bOn8Dx/summary.md`; the original 18-row ledger is `skilltest-cw-baseline.ksDeiD/summary.md`.
Their scratch paths and historical pending/approval statements are original provenance, not instructions to rerun exhausted commands.
Original absolute scratch references map to the same suffix below the extraction directory.
The live [CW runbook](../../../pilot/cw-runbook.md) and [design](../../../../plans/completed/specs/2026-09-07-cw-validation-design.md) own future execution gates.

## Inspect or restore

From this directory, `shasum -a 256 -c SHA256SUMS` verifies all archives.
Extract a selected `bundle.tar.gz` into a fresh scratch directory with `tar -xzf ARCHIVE -C DESTINATION`; its top-level directory is the original run ID.
Do not extract over a retained record or existing repository.
Bundle archives preserve nested fixture `.git` metadata without checking nested repositories into this checkout.
The directly readable copies must remain byte-identical to their archived counterparts.

Preservation verification restored all 100 archives (99 observations plus shared provenance), checked 4401 entries, matched all source bytes, verified 531 worksheet links and reconciled counts against the accepted 99-record audit.
No original scratch evidence was deleted and none of the 105 historical accepted records was changed.
Replace only owner-accepted complete sets; recover superseded accepted sets from Git history rather than adding dated directories.
