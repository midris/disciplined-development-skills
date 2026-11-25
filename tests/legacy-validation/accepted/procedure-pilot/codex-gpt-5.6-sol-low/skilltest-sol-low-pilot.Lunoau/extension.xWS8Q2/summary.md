# Behavior extension evidence

Project status and next checkpoint: [active plan](/Users/simon/work/personal/disciplined-development-skills/plans/2026-09-06-skilltest-sol-low-pilot.md#post-pilot-workflow-amendment).
Input freeze revision: `f39d72102b72d3bea9fdcd5a3f9c92c50c14f67c` on `spike/skilltest-input-isolation`.
The later completed runs used checkpoint `864c94aec2fe78a5dc62fa866318927092aeb231` for routine whole-directory prelaunch checks: its only pilot/runner difference from the original freeze is the owner's two-line full-response scoring clarification in pilot/README.md.
All subject prompts/configs/fixtures, withheld rubrics, scoring interpretation and runner code remain byte-identical to the original freeze; the documentation-only checkpoint does not require new setup qualification or recollection.
Provider/model/effort for completed observations: Codex / gpt-5.6-sol / low.
All six separately owner-approved observations completed once and are scored below. The procedure is at the owner-review checkpoint; no further provider command is queued or authorized.

## Provider-free input preparation

Working directory: `/Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike`.
Scratch allocated with `mktemp -d /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.XXXXXX`, exit 0.
Created the exact `preflight/`, `runs/`, `attempts/` and `preflight/prepared/` directories beneath this package with one `mkdir` command, exit 0.
The one-shot [audit](audit-inputs.py) only loads configs, compares source/pair bytes and calls existing workspace preparation helpers; no CLI/authentication/native discovery is involved.

Exact audit command (exit 0; stderr empty):

```sh
/Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/runner/.venv/bin/python /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/audit-inputs.py > /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/preflight/input-audit.json 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/preflight/input-audit.stderr
```

Result: [input-audit.json](preflight/input-audit.json); [stderr](preflight/input-audit.stderr).
It retains source/dependency hashes, verified Superpowers 6.3.0 manifest hash, prompt/rubric hashes, pair inventories and all six prepared-fixture paths.
Its source_revision is the pre-freeze HEAD; the committed input revision above, not that field alone, establishes the new files' recoverable provenance.
Prepared workspaces are provider-free copies, not model attempts or skill results.

## Observation inventory

| Label | Scenario / condition | Approved command | Bundle / CLI / worksheet |
|---|---|---|---|
| dr05-no-dd | DR-05 / no-DD | Owner approved the exact command below; runner/provider exit 0, 18.777 s, no retry | [Bundle](runs/skilltest-runs/20260907T191522229Z-pilot-dr-05-no-dd-00dee944-508f-4d62-a142-71456e279f26-8bnwraib/result.json), [CLI](attempts/dr05-no-dd/cli-version.txt), [worksheet](attempts/dr05-no-dd/worksheet.md): PASS |
| dr05-current-dd | DR-05 / current-DD | Owner approved the exact command below; runner/provider exit 0, 22.207 s, no retry | [Bundle](runs/skilltest-runs/20260907T192426298Z-pilot-dr-05-current-dd-7ba863a0-4f67-4bd0-81fb-0f20656abdeb-eslqwrxz/result.json), [CLI](attempts/dr05-current-dd/cli-version.txt), [worksheet](attempts/dr05-current-dd/worksheet.md): semantic PASS, protocol N/A, fidelity FAIL (narration) |
| lp05-no-dd | LP-05 / no-DD | Owner approved the exact command below; runner/provider exit 0, 123.723 s, no retry | [Bundle](runs/skilltest-runs/20260907T193716419Z-pilot-lp-05-no-dd-aeb3537a-cf4a-4d90-9980-2208fd1b53bc-cl705gzm/result.json), [CLI](attempts/lp05-no-dd/cli-version.txt), [worksheet](attempts/lp05-no-dd/worksheet.md): semantic FAIL, protocol N/A, fidelity PASS |
| lp05-current-dd | LP-05 / current-DD | Owner approved the exact command below; runner/provider exit 0, 132.494 s, no retry | [Bundle](runs/skilltest-runs/20260907T194610855Z-pilot-lp-05-current-dd-2b4ef775-8a6c-4a11-9269-239de13414fd-wfe2avwf/result.json), [CLI](attempts/lp05-current-dd/cli-version.txt), [worksheet](attempts/lp05-current-dd/worksheet.md): semantic FAIL (missing test command), protocol N/A, fidelity PASS |
| ar03-no-dd | AR-03 / no-DD | Owner approved the exact command below; runner/provider exit 0, 107.637 s, no retry | [Bundle](runs/skilltest-runs/20260907T195413155Z-pilot-ar-03-no-dd-5832d6a2-f81b-4119-aba8-fb139400c072-inlaq2fp/result.json), [CLI](attempts/ar03-no-dd/cli-version.txt), [worksheet](attempts/ar03-no-dd/worksheet.md): targeted semantic PASS, protocol N/A, fidelity PASS; extra-claim caveat retained |
| ar03-current-dd | AR-03 / current-DD | Owner approved the exact command below; runner/provider exit 0, 61.393 s, no retry | [Bundle](runs/skilltest-runs/20260907T200233864Z-pilot-ar-03-current-dd-7cecbcbe-a128-4c7b-abe8-30a81619dfda-ro0sycwm/result.json), [CLI](attempts/ar03-current-dd/cli-version.txt), [worksheet](attempts/ar03-current-dd/worksheet.md): semantic FAIL (missing explicit bulk sorting account), protocol N/A, fidelity PASS |

Any real qualification calls are separately approved/counted, not included in these six observations.
Provider-free qualification and reuse disposition: [preflight/reconciliation.md](preflight/reconciliation.md), including the retained audit errors and historical date difference.
Fixed CLI reference for the extension: `preflight/cli-version.txt` and `preflight/cli-sha256.txt`; both match the original qualified captures and must not be refreshed to hide drift.
The documented reuse decision requires no additional paid qualification call; provider command approval remains separate.
Retain this scratch through owner review; do not overwrite earlier pilot evidence or treat this preparation as discovery/effectiveness evidence.

## First observation — approved, completed and scored

DR-05 / no-DD; Codex / gpt-5.6-sol / low; cwd is the feature-worktree root above.
Owner reply: `approved`, following presentation of this complete command. No other command is covered by that reply.
Prelaunch repository check: clean `c781113`; no difference from frozen input revision `f39d72102b72d3bea9fdcd5a3f9c92c50c14f67c` under `skill-validation/pilot` or `skill-validation/runner`.

```sh
/usr/bin/env TMPDIR=/private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/runs PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/runner/.venv/bin/skilltest run /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/pilot/dr-05/no-dd/test.json > /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/attempts/dr05-no-dd/command-stdout.txt 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/attempts/dr05-no-dd/command-stderr.txt
```

## Second observation — approved, completed and scored

DR-05/current-DD; Codex / gpt-5.6-sol / low; same working directory and frozen input revision.
Owner reply: `approved`, following presentation of this complete command. This covers only the current-DD command, not later observations.
Prelaunch: clean HEAD `02daca6`; pilot/runner inputs still match frozen revision `f39d72102b72d3bea9fdcd5a3f9c92c50c14f67c`.

```sh
/usr/bin/env TMPDIR=/private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/runs PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/runner/.venv/bin/skilltest run /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/pilot/dr-05/current-dd/test.json > /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/attempts/dr05-current-dd/command-stdout.txt 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/attempts/dr05-current-dd/command-stderr.txt
```

## Third observation — approved, completed and scored

LP-05/no-DD; Codex / gpt-5.6-sol / low; same working directory and frozen input revision.
Owner reply: “please continue. have we seen anything so far that would indicate the process needs any changes?” following the exact-command approval request; continuation approves this one command only.
Prelaunch repository check: clean HEAD `8c3900e`; pilot/runner inputs match frozen revision `f39d72102b72d3bea9fdcd5a3f9c92c50c14f67c`.

```sh
/usr/bin/env TMPDIR=/private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/runs PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/runner/.venv/bin/skilltest run /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/pilot/lp-05/no-dd/test.json > /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/attempts/lp05-no-dd/command-stdout.txt 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/attempts/lp05-no-dd/command-stderr.txt
```

## Process observations for owner handoff

Per-run judgments and limitations remain in the linked worksheets; the accepted operational improvements now live in the [design amendment](/Users/simon/work/personal/disciplined-development-skills/plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-bounded-batch-operation).

## Fourth observation — approved, completed and scored

LP-05/current-DD; Codex / gpt-5.6-sol / low; same feature-worktree root and frozen input revision.
Owner reply: `approved`, following presentation of this complete command. This covers only LP-05/current-DD, not either AR-03 command.
Prelaunch: clean HEAD `864c94aec2fe78a5dc62fa866318927092aeb231`; pilot/runner inputs match that checkpoint, with subject inputs unchanged from the original freeze.

```sh
/usr/bin/env TMPDIR=/private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/runs PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/runner/.venv/bin/skilltest run /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/pilot/lp-05/current-dd/test.json > /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/attempts/lp05-current-dd/command-stdout.txt 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/attempts/lp05-current-dd/command-stderr.txt
```

## Fifth observation — approved, completed and scored

AR-03/no-DD; Codex / gpt-5.6-sol / low; same feature-worktree root and frozen subject inputs.
Owner reply: `approved`, following presentation of this complete command. This covers only AR-03/no-DD, not current-DD.
Prelaunch: clean HEAD `f39ecde`; pilot/runner inputs match checkpoint `864c94aec2fe78a5dc62fa866318927092aeb231`.

```sh
/usr/bin/env TMPDIR=/private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/runs PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/runner/.venv/bin/skilltest run /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/pilot/ar-03/no-dd/test.json > /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/attempts/ar03-no-dd/command-stdout.txt 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/attempts/ar03-no-dd/command-stderr.txt
```

## Sixth observation — approved, completed and scored

AR-03/current-DD; Codex / gpt-5.6-sol / low; same feature-worktree root and frozen subject inputs.
Owner reply: `approved`, following presentation of this complete command. This covers the final planned observation only; no further runs or campaign work are authorized.
Prelaunch: clean HEAD `6a8fb17`; pilot/runner inputs match checkpoint `864c94aec2fe78a5dc62fa866318927092aeb231`.

```sh
/usr/bin/env TMPDIR=/private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/runs PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/runner/.venv/bin/skilltest run /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/pilot/ar-03/current-dd/test.json > /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/attempts/ar03-current-dd/command-stdout.txt 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/attempts/ar03-current-dd/command-stderr.txt
```

## Owner handoff — acceptance pending

The inventory above is complete: six planned observations, six successful provider exits, no retries/exclusions or unresolved cleanup, and one worksheet per observation. No evidence is promoted into accepted/.
All ran with Codex / gpt-5.6-sol / low, CLI 0.153.4 and unchanged executable digest; task/skill/rubric inputs stayed frozen.
Retain this scratch package and the original pilot evidence; the active plan owns the next project checkpoint. Policy approval is not permission to rerun these completed commands.
Final provider-free handoff audit reconciled exactly six bundles and six populated worksheets, preserving generated identity/input/rubric hashes, tied CLI provenance and removed runtimes; all 65 local links/anchors resolve.
Fresh offline verification: runner 231 passed; hooks 263 passed with three skips; git diff --check clean and protected pilot/runner/scenario/skill inputs unchanged. No-write-tool review type is unavailable, so the bounded handoff review was inline; no additional provider or reviewer call was made.
