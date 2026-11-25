# Four-observation approval request

Status: OWNER APPROVED all four exact commands on 2026-09-07: “got it, approved, let's continue”. Execution outcomes are tracked per attempt in summary.md.
Provider: codex. Model: gpt-5.6-sol. Effort: low.
Input revision: e537c03909eb2b4f1986e4170a3f1b662d29a719.
Working directory for every command: /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike.
Qualified executable: /opt/homebrew/bin/codex, CLI 0.153.4.
Fixed executable digest: b973d440acac501fd2594a43e7ca9ce41e0a65b9dfb28d0d7a7837c99e1261e3.

Run sequentially in the order below, one observation per condition/scenario.
DR-02 reads the three supplied procurement sources and writes the two-line deadline note; LP-01 reads its supplied task/planning guidance and returns a plan without edits.
Current-DD supplies all nine frozen DD skills; no-DD supplies none. Both retain the declared Superpowers files and no DD hooks.
These are procedure-pilot observations, not official effectiveness runs; score all judgeable results, including FAILs.

Before each approved launch, create the nonexisting attempt directory, require a clean worktree and unchanged pinned inputs, capture CLI version/digest from the same executable and compare to the fixed preflight references.
Do not refresh reference evidence to hide drift.
Request host execution/network permission for the exact approved command when required; retain the provider's workspace-write sandbox.
The runner privately copies only existing file-backed authentication and owns cleanup; never print or retain credentials or alter shared authentication.
Stop on required-control failure, drift or unresolved cleanup. Only understood infrastructure-only failures permit an unchanged-command retry under the existing runbook policy.
Raw model bundles go beneath runs/skilltest-runs; command captures and subsequent worksheets go in the per-label attempt directory.
Approval covers these four commands, not additional repetitions, a different model/effort, qualification reruns or expanded skill work.

## dr-01: dr-02/no-dd

```sh
/usr/bin/env TMPDIR=/private/tmp/skilltest-sol-low-pilot.Lunoau/runs PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/runner/.venv/bin/skilltest run /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/pilot/dr-02/no-dd/test.json > /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/dr-01/command-stdout.txt 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/dr-01/command-stderr.txt
```

## dr-02: dr-02/current-dd

```sh
/usr/bin/env TMPDIR=/private/tmp/skilltest-sol-low-pilot.Lunoau/runs PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/runner/.venv/bin/skilltest run /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/pilot/dr-02/current-dd/test.json > /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/dr-02/command-stdout.txt 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/dr-02/command-stderr.txt
```

## lp-01: lp-01/no-dd

```sh
/usr/bin/env TMPDIR=/private/tmp/skilltest-sol-low-pilot.Lunoau/runs PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/runner/.venv/bin/skilltest run /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/pilot/lp-01/no-dd/test.json > /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/lp-01/command-stdout.txt 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/lp-01/command-stderr.txt
```

## lp-02: lp-01/current-dd

```sh
/usr/bin/env TMPDIR=/private/tmp/skilltest-sol-low-pilot.Lunoau/runs PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/runner/.venv/bin/skilltest run /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/pilot/lp-01/current-dd/test.json > /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/lp-02/command-stdout.txt 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/lp-02/command-stderr.txt
```

