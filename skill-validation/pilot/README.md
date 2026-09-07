# Sol-low procedure pilot

Status: both conditions passed scoped qualification; all four approved observations are complete and scored, awaiting owner review.
The [pilot handoff](../../plans/2026-09-06-skilltest-sol-low-pilot.md#pilot-handoff--owner-acceptance-pending) and scratch summary record outcomes and limitations.
The procedure below records the executed sequence; do not rerun completed rows without new approval.
Use the [implementation plan](../../plans/2026-09-06-skilltest-sol-low-pilot.md), [charter](../charter/core-contracts.md) and [methodology](../../plans/completed/specs/2026-09-02-skill-testing-methodology-design.md).
This is an agent-followed runbook, not a campaign program or an effectiveness baseline.
Claude work remains deferred.

## Fixed inputs and conditions

Run Codex / `gpt-5.6-sol` / `low`, with fresh runtime state for every invocation and no DD hooks.
Current-DD supplies all nine unchanged DD skills; no-DD supplies none.
Both receive Superpowers 6.3.0 `writing-plans/SKILL.md` and its referenced `plan-document-reviewer-prompt.md`.
This is the declared Superpowers subset for response-only planning, not the entire plugin: execution, implementation, review dispatch and skill authoring are outside these tasks.
Mentions of those later workflows in supplied skills do not authorize executing them or reading installed dependencies.
No skill text has been rewritten for this pilot.

DD bytes are frozen from main `ca14bbe24f8aea957dbcfeece3511226e929243d`; they match the audited pre-rewrite skill baseline at `ac45ab2`.
Task files and rubric bytes come from the existing DR-02 and LP-01 packages at that same main revision.
Superpowers files were copied from the installed 6.3.0 package; its MIT notice is retained at `inputs/superpowers/LICENSE`, outside subject fixtures.
Use these checked-in copies, never mutable installed skill paths, for execution.

The six `test.json` files enumerate every supplied source and native target.
Their source paths stay inside this pilot directory; neither this runbook nor any rubric, worksheet, accepted output, host configuration or credential is supplied.

| Frozen files beneath `inputs/` | Target beneath `workspace/fixture/` | Conditions |
|---|---|---|
| `dd/adversarial-review/SKILL.md` | `.agents/skills/adversarial-review/SKILL.md` | Current-DD |
| `dd/adversarial-review-loop/SKILL.md` | `.agents/skills/adversarial-review-loop/SKILL.md` | Current-DD |
| `dd/concise-writing/SKILL.md` | `.agents/skills/concise-writing/SKILL.md` | Current-DD |
| `dd/disciplined-development/SKILL.md` | `.agents/skills/disciplined-development/SKILL.md` | Current-DD |
| `dd/disciplined-research/SKILL.md` | `.agents/skills/disciplined-research/SKILL.md` | Current-DD |
| `dd/dispatching-development-subagents/SKILL.md` | `.agents/skills/dispatching-development-subagents/SKILL.md` | Current-DD |
| `dd/lean-plan-writing/SKILL.md` | `.agents/skills/lean-plan-writing/SKILL.md` | Current-DD |
| `dd/sweeping-stale-references/SKILL.md` | `.agents/skills/sweeping-stale-references/SKILL.md` | Current-DD |
| `dd/writing-explicit-rationale/SKILL.md` | `.agents/skills/writing-explicit-rationale/SKILL.md` | Current-DD |
| `superpowers/writing-plans/SKILL.md` | `.agents/skills/writing-plans/SKILL.md` | Both |
| `superpowers/writing-plans/plan-document-reviewer-prompt.md` | `.agents/skills/writing-plans/plan-document-reviewer-prompt.md` | Both |
| `tasks/dr-02/sources/city-museum-rfp.md` | `sources/city-museum-rfp.md` | Both DR-02 and qualification |
| `tasks/dr-02/sources/city-museum-addendum-2.md` | `sources/city-museum-addendum-2.md` | Both DR-02 and qualification |
| `tasks/dr-02/sources/friends-newsletter.md` | `sources/friends-newsletter.md` | Both DR-02 and qualification |
| `tasks/lp-01/context/task.md` | `context/task.md` | Both LP-01 and qualification |

The runner owns the fresh `.git` boundary, private profile, authentication preflight, copied-input checks and cleanup; do not reproduce that setup around real calls.
Use the [Codex adapter contract](../runner/README.md#codex), including its limited PATH and sibling evidence write grant.
Both conditions use the same native shell/file tools; no additional tool integration is introduced.

## Scenario contracts

DR-02 retains the procurement question and three source documents, and explicitly requests writing the same two-line response to `workspace/evidence/deadline-note.md`.
That is its sole permitted edit; fixture files and Git state remain unchanged.
Use source paths relative to the fixture root when checking citation resolution; the original rubric's `bundle-relative` wording is not an exact-string protocol.
The only prompt difference between conditions is the current-DD research-skill loading instruction.

LP-01 retains the JSON-report task and response-only boundary.
Both prompts require reading writing-plans; current-DD additionally requires lean-plan-writing with its stated override.
The complete nine-skill DD catalog is available in that condition, but no new requirement forces every skill to be loaded.

Each condition's `rubric.md` is byte-identical to its original scenario rubric.
For DR-02, record the added evidence-note requirement separately under task fidelity; do not add it to the semantic rubric or rescore the historical baseline.
For LP-01, separate lean-plan behavior from writing-plans composition, and assess each rubric clause in its proper ledger.
No-DD is a control, not an automatic RED verdict; judge its output against the same criteria.

## Preparation and freeze

Work only from `/Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike` on `spike/skilltest-input-isolation`.
Do not inspect the unrelated rewrite worktree.
Before collection, review and commit the prepared pilot inputs and record that full commit as `PILOT_INPUT_REVISION` in the scratch summary.
Require a clean worktree, and retain `git show --stat`, all input hashes and the source-revision comparison with the preparation evidence.
The recorded commit makes prompt, rubric, config and dependency bytes recoverable; hashes alone do not.

From the worktree root, verify the installed runner without a provider:

```sh
git status --short
git rev-parse HEAD
skill-validation/runner/.venv/bin/skilltest --help
git diff ca14bbe24f8aea957dbcfeece3511226e929243d -- skills
```

The retained `inspect-inputs.py` used `load_config`, `create_run`, `prepare_workspace` and `check_inputs` for all six configs; inspect its source and `audit.json` with the commands below.
Do not call `run_once` merely to validate a config: it invokes the provider.
Verify byte equality against the frozen sources, the exact source/target inventory, no symlinks, no evaluator files, and no DD sources or loading instructions in no-DD.
Compare prompts by condition: only the documented skill-loading line may differ; common task/tool/output requirements must match.
Compare each rubric to its original source bytes and verify worksheet generation against the frozen copy using synthetic evidence, not an accepted baseline mutation.

Current preparation evidence lives at `/private/tmp/skilltest-sol-low-pilot.Lunoau/`.
Retain its credential-free audit commands and outputs through owner review; do not commit scratch merely to accumulate history.
Create `attempts/` and `runs/` beneath that package before any real command.
Use `mkdir /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts /private/tmp/skilltest-sol-low-pilot.Lunoau/runs` once; on resume verify those existing directories instead of reallocating the package.
Initialize one `summary.md` with the input revision, CLI provenance, qualification state, table below, deviations and next resumable action.
Update that summary after every attempt, including failures and interruptions.

## Qualification gates

### Provider-free: finish before requesting a model call

1. Capture the resolved executable, version, executable digest and relevant help in scratch; compare to the qualified harness. Current inspection reports `/opt/homebrew/bin/codex`, `codex-cli 0.153.4`.
2. Prepare the actual qualification configs through the runner's workspace/runtime helpers using only dummy file-cache authentication under verified network denial. Capture `codex debug prompt-input` with the same model/effort and relevant config overrides, without executing a prompt.
3. Require native writing-plans in both conditions and exactly the nine additional DD entries in current-DD. Record every common provider skill and compare bootstrap file hashes before runtime cleanup.
4. Compare complete diagnostic prompt content after removing only the nine exact DD catalog entries, substituting exact per-launch fixture/private-runtime paths, and removing top-level message IDs and `create_time` metadata. Any other semantic difference must be explained or the gate stays unqualified.
5. Check the accepted spike's positive-control evidence against the pinned setup; repeat its competing user skill, global/config instruction and ancestry controls where the changed setup is not covered. Use surrogate scratch profiles only, never install canaries in the real home. A canary absent from its positive control proves nothing.
6. Check the selected shell/file tools under the adapter PATH, record observed shell-startup/common-input limits, and confirm all disposable runtime cleanup. An unavailable required control stops preparation as BLOCKED or INCONCLUSIVE, not PASS.

Prepared-input checks and the first native-catalog comparison pass in the current scratch package.
The observed common catalog is `imagegen`, `openai-docs`, `plugin-creator`, `skill-creator`, `skill-installer` and the supplied `writing-plans`: six entries in no-DD, fifteen in current-DD.
All 60 private bootstrap file hashes and the remaining diagnostic prompt content matched under the normalization above.
Provider-free qualification now passes; scratch `preflight/reconciliation.md` records reuse of the four accepted contamination controls, successful loopback policy checks, representative shell/tool reads and verified runtime removal.
The fixed CLI provenance is retained under `preflight/`; both separately approved real calls must pass before observations begin, with each result retained in the scratch summary.
`debug prompt-input` does not accept exec's `--ignore-user-config`, `--ignore-rules` or sibling `--add-dir` options and does not prove runtime enforcement, subsequent reads or hidden inputs.
The separate real qualification covers the exercised exec/read/write path; neither stage claims universal filesystem isolation.

### Provider-free command checklist

Run from the feature-worktree root; retain each command, stdout, stderr and exit status in `preflight/` beneath the existing scratch package.
Create that directory once with `mkdir /private/tmp/skilltest-sol-low-pilot.Lunoau/preflight`; on resume inspect existing evidence, never overwrite it.
The commands use `PILOT_SCRATCH=/private/tmp/skilltest-sol-low-pilot.Lunoau` and `PILOT_SPIKE=/private/tmp/skilltest-controlled-inputs.MTAyGQ` as path abbreviations, not HOME overrides.
Expand them in retained command records.

```sh
PILOT_SCRATCH=/private/tmp/skilltest-sol-low-pilot.Lunoau
PILOT_SPIKE=/private/tmp/skilltest-controlled-inputs.MTAyGQ
/opt/homebrew/bin/codex --version
/usr/bin/shasum -a 256 /opt/homebrew/bin/codex
/opt/homebrew/bin/codex exec --help
/opt/homebrew/bin/codex debug prompt-input --help
cat "$PILOT_SCRATCH/inspect-inputs.py" "$PILOT_SCRATCH/verify-preparation.py" "$PILOT_SCRATCH/no-network.sb"
cat "$PILOT_SCRATCH/audit.json" "$PILOT_SCRATCH/preparation-checks.json"
cat "$PILOT_SCRATCH/no-dd-command.json" "$PILOT_SCRATCH/current-dd-command.json"
cmp "$PILOT_SCRATCH/no-dd-normalized.json" "$PILOT_SCRATCH/current-dd-normalized.json"
cat "$PILOT_SPIKE/commands/run-private.sh" "$PILOT_SPIKE/commands/spike.py"
cat "$PILOT_SPIKE/outputs/control-debug/command.json" "$PILOT_SPIKE/outputs/control-debug/status.json"
cat "$PILOT_SPIKE/outputs/parent-debug/command.json" "$PILOT_SPIKE/outputs/parent-debug/status.json"
rg -o 'CI_(COMPETITOR|GLOBAL|CONFIG)_MTAyGQ' "$PILOT_SPIKE/outputs/control-debug/stdout"
rg -o 'CI_PARENT_MTAyGQ' "$PILOT_SPIKE/outputs/parent-debug/stdout"
```

Record the first four outputs as `preflight/cli-version.txt`, `cli-sha256.txt`, `exec-help.txt` and `debug-help.txt`, with separate stderr/status evidence.
Require successful captures, the documented exec options, all three distinct contamination markers and the ancestry marker in their successful positive controls.
Inspect the raw pilot `no-dd-prompt-input.json` and `current-dd-prompt-input.json` against their normalized copies: require the stated six/fifteen catalogs, exact normalization and matching 60-file bootstrap maps, not just a successful `cmp`.
The retained preparation scripts are one-shot evidence, not resume commands: they allocate fixed paths and publish outputs, so rerunning them would collide with or overwrite evidence.
If prepared files are missing or changed, stop and pin a fresh scratch preparation command before regenerating; never substitute `skilltest run` for this check.

In `preflight/reconciliation.md`, disposition each control separately: competing user skill, global instructions, config instructions and parent ancestry.
Compare the recorded old/new commands and setup sources: private homes contain no user skills/config/instructions, native targets remain `.agents/skills/`, and the fixture root has a fresh Git boundary.
Explicitly account for high→low effort, new fixture/prompt content, file-auth/approval overrides, and debug's lack of the exec-only options; the two real qualification calls cover the changed exec/read/write path.
Reuse old controls only where that comparison supports the same discovery mechanism; version equality alone is not sufficient.
If any control needs repeating, leave it unqualified and stop to specify its exact surrogate-profile command before execution; do not install host canaries or infer success from an absent marker.

Check the network-denial policy with a loopback-only positive/negative pair; no provider is involved:

```sh
/opt/homebrew/bin/python3 -c 'import socket; s=socket.socket(); s.bind(("127.0.0.1", 0)); s.close(); print("BIND_OK")'
/usr/bin/sandbox-exec -f "$PILOT_SCRATCH/no-network.sb" /opt/homebrew/bin/python3 -c 'import socket; s=socket.socket(); s.bind(("127.0.0.1", 0)); s.close(); print("BIND_OK")'
```

Retain `preflight/network-positive.*` and `network-denied.*`: require exit 0/`BIND_OK` outside the policy and a network-operation permission denial inside it.
A sandbox-launch failure or failed positive control is INCONCLUSIVE, not proof of network denial; request the necessary host permission for the unchanged provider-free command if needed.
This probes enforcement of the retained deny-network policy, not every network operation or filesystem isolation.

For the shell check, set `PILOT_QUAL_FIXTURE` to the existing `qualification`/`no-dd` row's verified `run_dir` from `audit.json`, followed by `/workspace/fixture`.
Create empty scratch-only profiles, then use the accepted spike's observed shell wrapper and adapter PATH:

```sh
mkdir -m 700 "$PILOT_SCRATCH/preflight/home" "$PILOT_SCRATCH/preflight/codex" "$PILOT_SCRATCH/preflight/tmp"
/usr/bin/env -i HOME="$PILOT_SCRATCH/preflight/home" CODEX_HOME="$PILOT_SCRATCH/preflight/codex" TMPDIR="$PILOT_SCRATCH/preflight/tmp" PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin /bin/zsh -lc 'cd "$1" || exit; for tool in cat sed rg; do command -v "$tool" || exit; done; cat .agents/skills/writing-plans/SKILL.md sources/city-museum-rfp.md sources/city-museum-addendum-2.md sources/friends-newsletter.md context/task.md >/dev/null' pilot-tool-check "$PILOT_QUAL_FIXTURE"
rmdir "$PILOT_SCRATCH/preflight/home" "$PILOT_SCRATCH/preflight/codex" "$PILOT_SCRATCH/preflight/tmp"
```

Retain `preflight/shell-tools.*`; require exit 0, tool paths inside the declared PATH and successful empty-directory removal.
Do not dump the environment or enable shell tracing: startup code may expose secrets.
Record automatic login-shell reads as an observability limit, not as proved absent; unexpected output, tool paths or leftover files require inspection and an explicit disposition before qualification.
This checks representative tool availability/reads; real qualification must still demonstrate Codex's actual wrapper and sibling evidence write.
Check both retained `*-runtime.log` files for cleanup errors and verify each logged private-runtime path is absent without opening its contents.
After all provider-free checks pass, record that decision and the exact CLI version/digest evidence in the summary; those two capture files become the fixed qualification reference below and must not be refreshed per attempt.

### Real qualification: two separately approved calls

After provider-free gates and preparation review pass, present each complete command with its prompt, configuration, provider/model/effort, working directory, output paths and required host permission.
Wait for explicit approval of that exact command before invoking it; the table and this document grant no provider-call permission.
The two qualification configs supply the union of DR-02/LP-01 task files and their condition's frozen skill inputs.
Both require actual source/skill reads and an evidence write; current-DD additionally requires the research and lean-plan skill bodies.
Neither asks the subject to implement, run tests, commit or dispatch agents.

Inspect the raw tool trace and saved `qualification.txt`: require observable reads of the requested skill bodies, all task sources and reviewer guidance, correct source-derived data, and a successful sibling evidence write.
Inspect permission denials and unexpected semantic reads; self-reported completion is insufficient.
Do not score qualification as skill effectiveness, or turn its forced-load criterion into an exclusion rule for subsequent observations.
Missing required loading/write evidence leaves qualification incomplete, even with exit 0.

## Exact run sequence and command procedure

Use the following order; the two completed qualifications are separate from the four observations.
Run each condition once per scenario to exercise the minimal workflow; repetitions and order balancing wait for later campaign design, so this pilot establishes neither repeatability nor effectiveness.
Every row is a fresh `skilltest run`, never a resumed session or overwritten bundle.

| Attempt label | Config beneath `skill-validation/pilot/` | Purpose |
|---|---|---|
| `q-no-dd` | `qualification/no-dd/test.json` | Qualification |
| `q-current-dd` | `qualification/current-dd/test.json` | Qualification |
| `dr-01` | `dr-02/no-dd/test.json` | No-DD observation |
| `dr-02` | `dr-02/current-dd/test.json` | Current-DD observation |
| `lp-01` | `lp-01/no-dd/test.json` | No-DD observation |
| `lp-02` | `lp-01/current-dd/test.json` | Current-DD observation |

Before every attempt, create its nonexisting scratch attempt directory, verify the recorded input revision is unchanged, and capture CLI version/digest from the same executable immediately before the run.
Read `PILOT_INPUT_REVISION` from the retained summary, not the then-current HEAD; run `git diff --exit-code "$PILOT_INPUT_REVISION" -- skill-validation/pilot skill-validation/runner` and require `git status --short` to be empty.
Run the version/digest commands individually and stop if either fails; do not continue to the provider merely because the output files exist.
Compare both fresh captures byte-for-byte with the fixed provider-free qualification references before every invocation, including retries.
Missing/empty reference files or any mismatch stop the comparison for harness requalification; do not replace the reference with the new capture to make it match.
The commands below illustrate the first qualification row, not permission to run it:

```sh
cd /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike
/opt/homebrew/bin/codex --version > /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/q-no-dd/cli-version.txt 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/q-no-dd/version-stderr.txt
/usr/bin/shasum -a 256 /opt/homebrew/bin/codex > /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/q-no-dd/cli-sha256.txt
test -s /private/tmp/skilltest-sol-low-pilot.Lunoau/preflight/cli-version.txt && test -s /private/tmp/skilltest-sol-low-pilot.Lunoau/preflight/cli-sha256.txt
cmp /private/tmp/skilltest-sol-low-pilot.Lunoau/preflight/cli-version.txt /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/q-no-dd/cli-version.txt
cmp /private/tmp/skilltest-sol-low-pilot.Lunoau/preflight/cli-sha256.txt /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/q-no-dd/cli-sha256.txt
/usr/bin/env TMPDIR=/private/tmp/skilltest-sol-low-pilot.Lunoau/runs PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/runner/.venv/bin/skilltest run /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/pilot/qualification/no-dd/test.json > /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/q-no-dd/command-stdout.txt 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/q-no-dd/command-stderr.txt
```

Run each pre-launch check separately and require exit 0 before proceeding; this block is an agent procedure, not a paste-and-continue shell script.
For each later row, replace only the table's config and attempt label, keeping the qualification-reference paths fixed, then show the fully expanded command for approval.
Record command text, exit status, working directory and final stdout bundle path in the scratch summary; associate the immediately preceding version capture with that exact run ID.
Inspect `runner.log` to confirm the actual absolute Codex executable and fixed adapter argv match the approved setup.
When the controller sandbox requires host execution, obtain that permission for the same approved command; keep Codex's own workspace-write sandbox.
Do not silently change authentication, model, effort, tools, fixtures or flags to make an attempt work.

After both qualifications pass, obtain approval for the four observation commands before running them in order.
Medium is a separately approved diagnostic for an identified mechanics problem, never an automatic replacement for a low-effort FAIL.

## Scoring, recovery and handoff

For each judgeable observation, use `skilltest worksheet` from the worktree root, with the corresponding `skill-validation/pilot/dr-02/current-dd` (or other table condition) scenario path, its retained bundle, and a nonexisting `attempts/<label>/worksheet.md` output.
Resolve those actual paths before invocation; the worksheet must use the matching frozen `rubric.md`, not an original scenario or later edited rubric.
For `dr-01`, set `RUN_BUNDLE` to the verified absolute bundle path recorded in that attempt's final stdout line, then run:

```sh
skill-validation/runner/.venv/bin/skilltest worksheet skill-validation/pilot/dr-02/no-dd "$RUN_BUNDLE" --output /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/dr-01/worksheet.md
```

Check its recorded rubric hash and fill every assessment section, including the CLI-version row with version and tied evidence reference.
Keep fixture hashes labeled as final-state inventories; the runner log holds pre-launch hashes.

Inspect raw stdout/tool traces, final answer and filesystem evidence independently.
DR-02 needs the saved note, answer agreement and controlling-source support; LP-01 needs plan/composition assessment, not claims that the outlined implementation was executed.
Separate semantic behavior, actual deterministic protocol, task fidelity, readability and infrastructure; requested prose shape alone is not machine protocol.
Inspect that protected fixture bytes remain unchanged, allowing only the runner-owned `.git` metadata and each scenario's explicitly authorized evidence writes.
An available skill not used during an observation is behavior to score, not automatically an isolation failure.
Retain all judgeable observations, including FAILs, and report conditions separately without a pooled effectiveness estimate.

Use the [failure/drift policy](../../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-failure-and-drift-policy):

- Required control unavailable before launch: stop without calling the model.
- Contamination, version/input drift or missing CLI provenance: retain and explain the attempt outside valid comparison evidence; do not assign an automatic skill FAIL or rerun everything.
- Understood infrastructure-only failure with no evaluable response: mark `INFRA_RETRY` in the summary and keep scratch-only. Before retrying the exact unchanged approved command, move its existing capture/version files into a unique retry-evidence subdirectory and update their summary references. Capture a fresh version record, then rerun with the same config and command, including redirections; retain the new unique bundle separately.
- Cleanup failure with an evaluable response: preserve it and its actual exit/output, stop for recovery and owner review; no automatic infrastructure retry.
- Interrupted attempt: follow the recovery checks below; never log out or delete a shared profile.

For recovery, obtain `RUN_BUNDLE` from the retained launch evidence, not a newest-directory guess; inspect `rg -n 'private Codex runtime|cleanup' "$RUN_BUNDLE/runner.log"`.
Copy its exact private-runtime path into `PILOT_RUNTIME`, validate that it belongs to this attempt beneath the configured scratch `runs/` directory, and check `test ! -e "$PILOT_RUNTIME" && test ! -L "$PILOT_RUNTIME"` without reading its contents.
An absent path confirms directory removal only; a missing recovery record, cleanup error or unknown process outcome after an uncatchable kill remains unresolved until explained.
The runner does not retain process-group IDs, so a leftover directory after an interrupted/killed runner does not provide enough evidence to identify and stop its processes safely.
In that case stop, retain the private runtime in place (do not archive its credential-bearing contents), record `cleanup unresolved` with the attempt/path and request owner-assisted recovery.
Do not infer ownership from a process name, use broad `pkill`, or delete the runtime merely because the runner or a similarly named process is absent.
Resume only after owned-process termination and exact-path cleanup are established; if that requires a manual destructive command, resolve its targets and present that exact command first.
This stop-and-retain fallback avoids adding process-management machinery solely for the pilot's exceptional recovery path.

Exercise failure/recovery and later edit-test bookkeeping with synthetic or retained evidence; do not spend provider calls manufacturing failures or author a candidate skill.
The summary must link every planned/completed attempt, its approval, input revision, bundle, version capture, worksheet, exclusion/deviation and cleanup state, plus remaining rows and the next action.
Present the complete pilot and procedure findings for owner review, then stop.
Do not promote pilot results into an effectiveness baseline, modify the 105 accepted historical records, delete evidence, reorganize validation directories or begin rewritten-skill comparisons automatically.
