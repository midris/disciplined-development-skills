# Provider-free qualification reconciliation

PASS for the runbook's provider-free gates; real exec qualification is still NOT RUN.
Reviewed runner: e8e25eb84b54a73fc1e54aa7d4950d2cdfe8ff35.
No new model calls, real authentication, host canaries or shared-profile changes were used.

## Recorded controls

Old evidence root: /private/tmp/skilltest-controlled-inputs.MTAyGQ.
New evidence root: /private/tmp/skilltest-sol-low-pilot.Lunoau.
Inspected old commands/run-private.sh and commands/spike.py, the four fixtures/ambient files, control-debug and parent-debug commands/status/output, and all four A1/B1/B2/A2 clean debug outputs.
Inspected new inspect-inputs.py, verify-preparation.py, no-network.sb, both command/runtime records, audit.json, preparation-checks.json and both raw/normalized diagnostic pairs.
retained-evidence-audit.json retains the exact read-only verification command and its successful output.

| Control | Positive evidence and comparison | Disposition |
|---|---|---|
| Competing user skill | CI_COMPETITOR_MTAyGQ appears from the surrogate HOME/.agents/skills in control-debug. Clean old arms and new private homes do not supply that user path; native project targets remain .agents/skills. | Reuse the demonstrated discovery control; new catalogs independently contain exactly the declared six/fifteen entries. |
| Global instructions | CI_GLOBAL_MTAyGQ appears from surrogate CODEX_HOME/AGENTS.md in control-debug. Old clean profiles and the new auth-only profile omit this file. | Reuse; private-profile construction is unchanged in purpose and no global file is copied. |
| Config instructions | CI_CONFIG_MTAyGQ appears from surrogate CODEX_HOME/config.toml in control-debug. New profile has no config.toml; fixed auth/approval overrides add no instructions. | Reuse; debug shows the actual new common context. Exec additionally ignores user config, but that flag is not credited as proved enforcement here. |
| Parent ancestry | CI_PARENT_MTAyGQ appears when running below its project-local placement in parent-debug, but not outside the fresh Git boundaries in the four clean trials. New fixture cwd has its own fresh .git boundary. | Reuse the root-boundary control; both prepared qualification fixtures retain that boundary. |

The same absolute CLI reports codex-cli 0.153.4; new fixed digest is b973d440acac501fd2594a43e7ca9ce41e0a65b9dfb28d0d7a7837c99e1261e3.
Version equality alone is not the reuse rationale: the paths, private-profile sources, project boundaries and positive/negative discovery evidence above were compared.
High-to-low effort, new task content and the full nine-DD composition are declared changes; the actual low-effort diagnostic catalogs were inspected rather than assuming the old synthetic skill represented them.
Both low conditions have identical 60-file bootstrap maps; exact raw-to-normalized reconstruction succeeds after only the declared nine catalog-line removals, exact fixture/runtime substitutions, message IDs and create_time removal.
All sixteen frozen source hashes and every saved prelaunch hash for six prepared configs remain unchanged.
No preparation script was rerun or earlier output overwritten.

## Network and shell checks

network-positive-sandboxed.json and network-denied-sandboxed.json record controller restrictions: positive bind denied, nested sandbox launch denied. These attempts are INCONCLUSIVE.
Unchanged commands under approved host execution give BIND_OK/exit 0 outside the policy and PermissionError/exit 1 inside it (network-positive-host.json, network-denied-host.json).
This establishes the retained deny-network policy's loopback operation control, not universal filesystem isolation.

shell-tools.json records the exact private-profile env -i /bin/zsh -lc command.
It returned exit 0, empty stderr, /bin/cat, /usr/bin/sed and /opt/homebrew/bin/rg, and successfully read the supplied writing-plans body plus all four task files.
The three empty preflight profile directories were removed successfully with the runbook's exact rmdir command; no credential file was created.
Both logged diagnostic runtime roots are absent, including symlink checks, and both runtime logs report cleanup: None.

## Limits and next gate

The CLI help/version captures succeeded with a controller PATH-alias permission warning; this does not establish actual exec behavior and is not silently erased.
The fixed references are cli-version.txt and cli-sha256.txt; compare fresh per-attempt captures to these, never refresh them to hide drift.
Debug lacks exec's ignore-user-config, ignore-rules and sibling add-dir options. It cannot prove enforcement, all subsequent reads or the full provider request.
The shell probe reproduces the accepted spike's observed login-shell wrapper, but does not trace its automatic startup reads or prove the final PATH contains no extra entries. The observed task-tool paths are all in the declared adapter PATH.
Keep those automatic/common-input limits explicit; actual Codex tool invocation and sibling evidence writing remain the two separately approved real qualifications' job.
Native bootstrap skills remain common inputs, not absence-of-all-guidance controls. No skill effectiveness conclusion follows.
Next freeze the documentation checkpoint, record its commit for the runbook's revision guard, and obtain exact-command approval for q-no-dd; q-current-dd remains separately gated.
