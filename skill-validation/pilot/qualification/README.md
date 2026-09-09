# Codex pilot qualification reference

Qualification is separate from routine execution; use the [routine runbook](../README.md) after the required controls are established.
The [active plan](../../../plans/completed/2026-09-06-skilltest-sol-low-pilot.md) owns current execution/approval status.

Revisit only affected controls when CLI version/digest, adapter setup, skill catalog/dependencies, task tools or discovery boundaries change.
A prompt/task-fact edit using unchanged mechanisms still needs a fresh input freeze and audit; it does not automatically require replaying every canary or paid qualification call.
Record why retained evidence applies, repeat checks where it does not, and stop if a required control remains unproved.
Any necessary real qualification command needs its own exact-command approval.
New scenarios do not inherit qualification for undeclared tools or dependencies.

The concrete paths and commands below identify the retained pilot qualification.
Do not rerun its one-shot scripts or overwrite evidence; if a reference is missing, prepare and audit a fresh scratch qualification command instead.
Routine runs need the retained qualification decision and fixed CLI-reference captures, not a reread of every spike artifact.

## Provider-free: finish before requesting a qualification call

1. Capture the resolved executable, version, executable digest and relevant help in scratch; compare to the qualified harness. Current inspection reports `/opt/homebrew/bin/codex`, `codex-cli 0.153.4`.
2. Prepare the actual qualification configs through the runner's workspace/runtime helpers using only dummy file-cache authentication under verified network denial. Capture `codex debug prompt-input` with the same model/effort and relevant config overrides, without executing a prompt.
3. Require native writing-plans in both conditions and exactly the nine additional DD entries in current-DD. Record every common provider skill and compare bootstrap file hashes before runtime cleanup.
4. Compare complete diagnostic prompt content after removing only the nine exact DD catalog entries, substituting exact per-launch fixture/private-runtime paths, and removing top-level message IDs and `create_time` metadata. Any other semantic difference must be explained or the gate stays unqualified.
5. Check the accepted spike's positive-control evidence against the pinned setup; repeat its competing user skill, global/config instruction and ancestry controls where the changed setup is not covered. Use surrogate scratch profiles only, never install canaries in the real home. A canary absent from its positive control proves nothing.
6. Check the selected shell/file tools under the adapter PATH, record observed shell-startup/common-input limits, and confirm all disposable runtime cleanup. An unavailable required control stops preparation as BLOCKED or INCONCLUSIVE, not PASS.

The current scratch package retains prepared-input checks and native-catalog evidence.
The observed common catalog is `imagegen`, `openai-docs`, `plugin-creator`, `skill-creator`, `skill-installer` and the supplied `writing-plans`: six entries in no-DD, fifteen in current-DD.
All 60 private bootstrap file hashes and the remaining diagnostic prompt content matched under the normalization above.
Scratch `preflight/reconciliation.md` records reuse of the four accepted contamination controls, successful loopback policy checks, representative shell/tool reads and verified runtime removal.
The fixed CLI provenance is retained under `preflight/`; both separately approved real calls must pass before observations begin, with each result retained in the scratch summary.
`debug prompt-input` does not accept exec's `--ignore-user-config`, `--ignore-rules` or sibling `--add-dir` options and does not prove runtime enforcement, subsequent reads or hidden inputs.
The separate real qualification covers the exercised exec/read/write path; neither stage claims universal filesystem isolation.

## Provider-free command checklist

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

## Real qualification

After provider-free gates and preparation review pass, present each complete command with its prompt, configuration, provider/model/effort, working directory, output paths and required host permission.
Wait for explicit approval of that exact command before invoking it; the table and this document grant no provider-call permission.
The two qualification configs supply the union of DR-02/LP-01 task files and their condition's frozen skill inputs.
Both require actual source/skill reads and an evidence write; current-DD additionally requires the research and lean-plan skill bodies.
Neither asks the subject to implement, run tests, commit or dispatch agents.

Inspect the raw tool trace and saved `qualification.txt`: require observable reads of the requested skill bodies, all task sources and reviewer guidance, correct source-derived data, and a successful sibling evidence write.
Inspect permission denials and unexpected semantic reads; self-reported completion is insufficient.
Do not score qualification as skill effectiveness, or turn its forced-load criterion into an exclusion rule for subsequent observations.
Missing required loading/write evidence leaves qualification incomplete, even with exit 0.
