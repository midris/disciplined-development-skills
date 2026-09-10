# CW candidate preparation

Status: QUALIFIED / FROZEN / PUSHED — no provider calls; exact-command approval remains pending.
The owner accepted all 99 CW baseline observations on 2026-09-08 and selected the existing rewritten CW next.
The [live design](/Users/simon/work/personal/disciplined-development-skills/.worktrees/cw-validation-design/plans/specs/2026-09-07-cw-validation-design.md#existing-cw-candidate-preparation) owns checkpoints.
The [candidate provenance](/Users/simon/work/personal/disciplined-development-skills/.worktrees/cw-validation-design/skill-validation/pilot/inputs/candidates/cw-rewrite/README.md) pins source commit and exact body/description hashes.
Source: `docs/comprehensive-skill-cleanup` at `13599fb7d3127334b0d07bfe468767e586ec5f9c`; only its CW file was read/copied, with source worktree untouched.

## Completed

- Copied CW byte-for-byte into a test-only input, with its exact frontmatter description as the two routing-quiz fixtures.
- Prepared 22 existing-schema configs against the same prompts/rubrics and surrounding composition; only CW and recording identities/source paths differ.
- [Input audit](input-audit.json) and its [one-shot command](input-audit-command.md) prove declared/prepared equality, protected baseline bytes, same prompt/rubric/model/effort, no symlinks and exactly one changed CW target per config.
- Recorded baseline acceptance without rescoring; accepted evidence remains in the two original scratch packages, not yet committed.
- Recorded deferred larger samples (possibly five); the proposed candidate schedule remains three per condition, 66 calls before any changed-control recollection, subject to review.
- Hook suite: `python3 -m pytest -q` from `skills/disciplined-development/hooks`: [263 passed, 3 skipped](hook-tests.txt).
- Main is clean; the shipped skill, source CW, other rewritten skills, runner and historical accepted records are unchanged.
- Work remains uncommitted on `feature/cw-validation-design`.

## Read-only change analysis

The snapshot changes the description's applicability, adds the detailed-response exception and writing-skills ownership, separates full durable-prose work from a light response-only pass, and makes lossless source/result verification explicit.
It retains the six padding patterns in a shorter form and revises the examples, including preserving the LRU exceed-versus-reach boundary.
Measured whitespace-separated word counts: baseline 860, candidate 665.
These are source differences, not evidence of better behavior.
No candidate wording was corrected or optimized against the accepted failures.

## Bounded preparation review

Inline review used because the repository requires a no-write-tool type for evaluation subagents and none is available here.
Reviewed source fidelity, full candidate diff, dependency names, all config mappings/prepared inventories, subject/evaluator separation, frozen baseline contract preservation, acceptance status and approval limits.
Round 1 found a baseline-specific rubric-comment ambiguity: CW-09/11's authoring exclusion and CW-17's absent exception must not be copied into candidate judgments.
Resolved by an evaluator-only note beside the candidate mapping, preserving both original rubrics and their unchanged target outcomes.
Acceptance-status drift was swept across the spec, runbook, catalog and both baseline summaries; original worksheet dispositions remain unchanged as scoring-time records.
Round 2: no unresolved preparation findings.
This is not native-discovery qualification, semantic skill validation, or an independent deployment review.

Final provider-free check:
```json
{
  "result": "PASS",
  "candidate_configs": 22,
  "links_checked": 178,
  "source_cw_unchanged": true,
  "main_clean": true,
  "only_declared_files_changed": true,
  "hook_tests": "263 passed, 3 skipped",
  "provider_calls": 0
}
```

## Owner-requested document review before execution

Execution paused for this review: no provider calls, qualification probes, test suites, evidence packaging, commits or pushes.
Reviewed the complete CW spec, runbook, mapping, candidate provenance and source snapshot, preparation evidence, changed acceptance notes in both baseline summaries, and linked governing decisions/navigation.
The 22 configs and their prompt/rubric hashes still match the recorded preparation audit.
This was bounded inline review, not an independent evaluation or candidate effectiveness judgment.

Three P2 finding classes were addressed:

- Freeze ordering: qualification, CLI provenance and reuse decisions now precede the final clean freeze; later input/guidance changes require affected checks and a new freeze. Candidate collection gets a separate scratch package from preparation.
- Existing-candidate versus new-authoring authority: the runbook explicitly routes this unchanged snapshot to comparison steps, while RED-before-authoring and writing-skills requirements remain for new edits. The CW spec records descriptive, criterion-level comparison without matched-repetition or automatic adoption claims.
- Stale status/navigation: the controlled-input spec and validation README now defer to the live CW design rather than claiming candidate preparation is deferred or native-discovery acceptance is still pending.

The retention gate now requires an explicit destination/contents record and byte/navigation verification independent of original scratch paths before preservation is considered complete; no layout or archival operation was performed.
Reference sweep retained original pilot checkpoint text as historical procedure evidence, historical test/fixture text as frozen inputs, and pending work for other catalogs as out of scope; none grants candidate-call authority.
Follow-up read-only verification: 280 local links/anchors resolve, all 22 candidate configs and their prompt/rubric hashes match the audit, candidate body/description hashes match, source CW is unchanged, main is clean, and only declared branch paths differ.
`git diff --check` passes.
Follow-up review found no unresolved P0/P1/P2 document findings; preservation, qualification/reuse, clean freeze and exact-command approval remain execution gates.

## Qualified candidate and preserved baseline

The owner authorized continuing after the document review.
The [provider-free qualification](qualification/summary.md) records six native-catalog checks, unchanged CLI/bootstrap bytes, local reads, owned cleanup and the mechanical reuse audit of all 99 accepted observations.
No shared authentication was accessed; only dummy private status checks under network denial were used.
Reusing the accepted 66 current-DD and 33 no-DD observations leaves the proposed fresh batch at 66 candidate calls.

The [preservation plan](preservation-plan.md) fixes the destination and whole-set policy.
[Selection audit](preservation-selection.json), [original one-shot](preserve-evidence.py), [independent verification](verify-preservation.py) and [verified result](preservation-verified.json) retain the exact scope and mechanical evidence.
The first archive restoration passed, but the final navigation check caught inline worksheet links omitted from the readable-copy selection; [stderr](preservation-stderr.txt) retains that packaging defect.
It affected convenience copies only, not archives, source evidence, scores or model execution.
Enumerating both inline and reference-style citations identified 37 missing files; the continuation copied those byte-for-byte and independently restored all archives again.
Final checks: 99 observations, 33 conditions, 22 scenario sets, 100 archives, 4,401 entries, 234 primary provenance files and 531 resolved worksheet links; every accepted count matches the prior audit.
No source scratch was deleted and the 105 historical records remain unchanged.
Fresh required hook verification: [263 passed, 3 skipped](freeze-hook-tests.txt).
Review notes and one-shot packaging tools remain scratch-only, not production runner features.

## Next

The final inline review checked 133 documents / 920 links, preserved candidate/config hashes and protected paths; no unresolved findings remain.
Verified all 938 accepted evidence files were staged, with every staged blob matching its reviewed working file and no omitted/untracked inputs.
Committed and pushed as `595f8e2bce0a62c5d4143ffebcdcf30cf8422b0d`; feature branch is clean and synchronized.
The separate [collection package](/private/tmp/skilltest-cw-candidate.L4NdO8/summary.md) contains the audited exact 66-command batch and empty attempt directories.
Wait for explicit owner approval of that command document before any provider call.
No model run, extra repetition, new test, new tool or skill deployment is approved by this preparation.

DD-VERDICT: PASS
