# CW purpose-separation batch

Input review: owner's “please continue” after the committed prompt/rubric handoff is treated as acceptance of those inputs and permission for provider-free qualification.
Exact provider batch approval: owner replied “approved” to the complete four-command request on 2026-09-07. Execute only those commands once in the frozen order, subject to the runbook's stop/retry rules.
Current batch state: all four approved commands completed once, in order, with runner/provider exit 0 and no retries or unresolved cleanup. Worksheets are complete; owner acceptance is pending. The first run's model-catalog refresh warning remains disclosed under the owner's [non-blocking disposition](refresh-warning.md); the other three provider stderr captures are empty.
This is a four-observation procedure batch, not effectiveness sampling, skill-authoring RED/GREEN acceptance or activation of the broader catalog repair.
Project checkpoint remains in [the active plan](/Users/simon/work/personal/disciplined-development-skills/plans/2026-09-06-skilltest-sol-low-pilot.md); no further provider command, skill edit or broader catalog work is queued.

## Frozen provenance and qualification

Working directory: `/Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike`.
Recoverable input and evaluator revision: `f28ea6569b7eb5b65245e77635a5ff7d12fc1082`.
Provider/model/effort: Codex / gpt-5.6-sol / low for all four commands.
Inputs and withheld scoring boundaries: [runbook](/Users/simon/work/personal/disciplined-development-skills/skill-validation/pilot/README.md#cw-purpose-separated-inputs), the four linked prompt/config/rubric sets, and [preparation audit](input-audit.json).
Fixed qualified CLI reference remains [the extension preflight](../extension.xWS8Q2/preflight/reconciliation.md); do not replace that reference with each new capture.
The fresh [CLI version](preflight/cli-version.txt) and [digest](preflight/cli-sha256.txt) match it; [version stderr](preflight/version-stderr.txt) retains the previously documented PATH-alias permission warning.
The warning concerns the controller's alias setup; the run uses the pinned absolute executable and declared PATH, with runtime behavior independently exercised by the retained real qualification. It is not evidence that exec controls pass on its own.

Affected qualification: PASS for the scoped availability/observation boundary, by unchanged-mechanism reuse and fresh provider-free comparisons.
The [exact audit command](preflight/reconciliation-audit-command.txt) exited 0 with [these results](preflight/reconciliation-audit-output.json).
[Repository checks](preflight/repository-checks.json) exited 0: clean feature tree, frozen inputs/evaluator files unchanged, and runner production source identical to the original real-qualification checkpoint.
Main is clean at its tracking revision `ca14bbe24f8aea957dbcfeece3511226e929243d`; no work was performed there.

| Control | Evidence and disposition |
|---|---|
| Prepared task and evaluator inputs | All twelve files match the committed preparation audit; four exact prepared fixture inventories and source hashes match. No-DD has four guidance files, current-DD thirteen; no task files, evaluator files or hooks added. |
| Native catalog and readable CW body | Reuse [extension catalog audit](../extension.xWS8Q2/preflight/catalog-v3/catalog-audit.json) and its current-DD shell check: seven/sixteen native entries, including the CW alias resolving under fixture .agents/skills. Fresh comparison proves all CW guidance targets/bytes identical to those qualified. The only removed fixtures are ordinary AR project files; inline task changes add no discovery source or tool. |
| Common input and automatic body injection | Retained paired normalized diagnostic content and all sixty bootstrap hashes match. Inspection of the raw retained diagnostics finds the CW description/path, not its skill body. Same pinned binary, runtime, native files and options; no new debug call is needed for a task-only change. The September 6→7 incidental date difference from original qualification remains explicitly dispositioned in the extension reconciliation, not silently removed. |
| User skills, global/config instructions and parent ancestry | Reuse the individual surrogate controls and dispositions in the [extension reconciliation](../extension.xWS8Q2/preflight/reconciliation.md): unchanged private-profile creation, fixed invocation controls and fresh fixture Git boundary. No host canaries or credentials inspected. |
| Observable trace capability | Re-inspected original current-DD qualification raw stdout: ten parseable events, thread/turn start, every started item completed, successful command with three full supplied skill bodies, three model-authored messages and terminal turn completion; saved final matches its last message. Same unfiltered stdout capture and CLI JSON mode. This proves the exercised event/read path, not hidden provider cognition or an arbitrary future trace's completeness. |
| Scope and cleanup | Retained catalog runtimes still absent; prior real loading/read/write qualification reused with unchanged source/options. No new runtime or credential copy created during these checks. |

Each discovery run still needs full raw-trace inspection: check start/end, completed tool events, returned body coverage and timing, all model-authored messages, final consistency, errors, truncation and opaque/ambiguous access.
Unknown or missing coverage prevents a negative PASS; a visible selection can still establish the frozen negative FAIL.
Catalog descriptions are not body loading; prior forced-load qualification does not answer whether CW will be selected on these tasks.
No additional paid qualification call is required under this unchanged read-only mechanism.
Automatic shell-startup reads and hidden provider inputs retain the accepted observability limits: this is scoped no-observed-selection evidence, never proof of hidden non-use or universal filesystem isolation.

## Approved order and commands

One run of each row, sequentially in this order.
Judgeable failures stay in the record; do not add repetitions or raise effort.
The routine runbook's drift, cleanup and unchanged-command INFRA_RETRY gates apply.
Before each first launch create its exact attempt directory once (without -p), capture CLI provenance, check frozen files and validate scratch paths.
The scratch root, runs directory and attempt parent already exist; per-attempt directories are intentionally not created until first launch.
Include `skill-validation/charter/core-contracts.md` and `plans/completed/specs/2026-09-02-skill-testing-methodology-design.md` alongside the runbook's pilot/runner/spec paths in each frozen-input diff.

| Order | Attempt | Purpose | Approval / execution | Bundle / worksheet |
|---|---|---|---|---|
| 1 | cw01-no-dd | CW-01 behavior control / no-DD | Approved / completed, runner exit 0; warning accepted as non-blocking | [Bundle](/private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/runs/skilltest-runs/20260907T213143642Z-pilot-cw-01-no-dd-9da0992f-c087-4fc9-9eb0-d11111a00562-6rjoy_ux) / [worksheet](attempts/cw01-no-dd/worksheet.md) / [CLI](attempts/cw01-no-dd/cli-version.txt) / [command output](attempts/cw01-no-dd/command-stdout.txt) |
| 2 | cw01-current-dd | CW-01 explicitly loaded behavior / current-DD | Approved / completed, runner exit 0 | [Bundle](/private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/runs/skilltest-runs/20260907T220811560Z-pilot-cw-01-current-dd-1beecd65-6338-45d9-b3b0-5193bf194596-9vu_90p4) / [worksheet](attempts/cw01-current-dd/worksheet.md) / [CLI](attempts/cw01-current-dd/cli-version.txt) / [command output](attempts/cw01-current-dd/command-stdout.txt) |
| 3 | cw01-discovery | CW-01 native positive discovery / current-DD | Approved / completed, runner exit 0 | [Bundle](/private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/runs/skilltest-runs/20260907T221102301Z-pilot-cw-01-discovery-18f4ea8c-55ef-41fd-94e4-30972ca01730-gpsd_wn6) / [worksheet](attempts/cw01-discovery/worksheet.md) / [CLI](attempts/cw01-discovery/cli-version.txt) / [command output](attempts/cw01-discovery/command-stdout.txt) |
| 4 | cw17-discovery | CW-17 native non-trigger / current-DD | Approved / completed, runner exit 0 | [Bundle](/private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/runs/skilltest-runs/20260907T221237430Z-pilot-cw-17-discovery-3ad8794d-a5be-4f23-a458-c88202bb1894-w2cdz0w5) / [worksheet](attempts/cw17-discovery/worksheet.md) / [CLI](attempts/cw17-discovery/cli-version.txt) / [command output](attempts/cw17-discovery/command-stdout.txt) |

### 1. cw01-no-dd

```sh
/usr/bin/env TMPDIR=/private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/runs PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/runner/.venv/bin/skilltest run /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/pilot/cw-01/no-dd/test.json > /private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/attempts/cw01-no-dd/command-stdout.txt 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/attempts/cw01-no-dd/command-stderr.txt
```

### 2. cw01-current-dd

```sh
/usr/bin/env TMPDIR=/private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/runs PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/runner/.venv/bin/skilltest run /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/pilot/cw-01/current-dd/test.json > /private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/attempts/cw01-current-dd/command-stdout.txt 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/attempts/cw01-current-dd/command-stderr.txt
```

### 3. cw01-discovery

```sh
/usr/bin/env TMPDIR=/private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/runs PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/runner/.venv/bin/skilltest run /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/pilot/cw-01/discovery/test.json > /private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/attempts/cw01-discovery/command-stdout.txt 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/attempts/cw01-discovery/command-stderr.txt
```

### 4. cw17-discovery

```sh
/usr/bin/env TMPDIR=/private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/runs PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/runner/.venv/bin/skilltest run /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/pilot/cw-17/discovery/test.json > /private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/attempts/cw17-discovery/command-stdout.txt 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/attempts/cw17-discovery/command-stderr.txt
```

The config supplies provider/model/effort and prompt to the unchanged runner; the runner owns private HOME/CODEX_HOME/TMPDIR, authentication preflight, project boundary, sandbox flags and cleanup.
Host/network approval may be required for the exact approved command; do not broaden the subject sandbox or change shared authentication.
Score and validate each result before the next approved command; record all judgment in its worksheet and retain only links/status here.
The repository stayed clean during collection; the handoff reconciles active/deferred input-review status, coverage claims and the approved warning policy in one documentation unit.
Handoff verification: four worksheets preserve generated mechanical fields; all 209 local links/anchors across eleven documents resolve; the four exact approved commands and 169 prior extension evidence files are unchanged; protected runner/skill/scenario/input diffs are empty; hooks pass 263 tests with three skips.
Prior runner verification (231 passing tests at the unchanged test-boundary checkpoint) remains applicable unless code/environment changes or a failure invalidates it.
No results are promoted to accepted baselines, and no skill edits or broader runs follow automatically.
