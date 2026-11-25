# CW candidate qualification and baseline reuse

Provider-free gates PASS for the unchanged CW snapshot and the 22 declared candidate configs.
No model invocation, shared authentication access, new skill wording or rescoring occurred.
Candidate command approval remains outstanding.

## Fresh checks

- [CLI version](cli-version.txt) and [digest](cli-sha256.txt) match the baseline: `/opt/homebrew/bin/codex`, `codex-cli 0.153.4`, SHA-256 `b973d440acac501fd2594a43e7ca9ce41e0a65b9dfb28d0d7a7837c99e1261e3`.
  The retained [version stderr](version-stderr.txt) has only the previously disclosed PATH-alias permission warning.
- [Network positive/negative control](network-controls.json): loopback bind succeeds outside the policy and fails with PermissionError under the byte-identical [deny-network policy](no-network.sb).
- [Catalog audit](native/audit.json), [stdout](catalog-stdout.txt) and empty [stderr](catalog-stderr.txt): baseline/candidate native counts are 16/16 ordinary, 18/18 authoring and 7/7 description-only.
  All supplied native paths resolve inside their declared fixture, and each CW catalog entry uses that arm's exact supplied description.
  After removing the declared DD/authoring catalog entries and substituting exact disposable paths/message IDs/create-time metadata, common messages match across all six setups.
  All 60 bootstrap file hashes match across setups and the retained extension qualification.
  Required local reads, protected-input preservation and all six owned runtime cleanups pass; dummy source profiles are removed.
- [99-record reuse audit](reuse-audit.json) and [source](reuse-audit.py): all accepted observations retain exact source/config/prompt/artifact hashes, completed trace envelopes, tied CLI captures, exact adapter argv and absent owned runtimes.
  Counts reconcile to the accepted per-condition ledger; the audit checks existing judgments mechanically, without rescoring.

The catalog command, run from `/Users/simon/work/personal/disciplined-development-skills/.worktrees/cw-validation-design`, was:

```sh
/usr/bin/sandbox-exec -f /private/tmp/skilltest-cw-candidate.pITN2u/qualification/no-network.sb /Users/simon/work/personal/disciplined-development-skills/.worktrees/cw-validation-design/skill-validation/runner/.venv/bin/python /private/tmp/skilltest-cw-candidate.pITN2u/qualification/catalog-audit.py > /private/tmp/skilltest-cw-candidate.pITN2u/qualification/catalog-stdout.txt 2> /private/tmp/skilltest-cw-candidate.pITN2u/qualification/catalog-stderr.txt
```

Exit 0.
The [script](catalog-audit.py) records each diagnostic argv/cwd/private path environment, output, status and cleanup under `native/`.
It uses only dummy file-cache authentication under network denial, never `codex exec` or `skilltest run`.
The local authentication-status checks do not establish live provider authentication for later runs; the runner must perform its normal private-auth preflight for each approved call.

## Control and dependency disposition

Reuse the [accepted CW qualification](/private/tmp/skilltest-cw-catalog-qualification.YiAoRu/summary.md) and its retained private-profile, competing-user/global/config/ancestor controls, actual read/write/cleanup qualifications and CW-18 file-creation/inventory proof.
The current baseline preservation package also retains the supporting primary evidence, independent of future scratch cleanup.
The production runtime/adapter and CLI binary are unchanged; the candidate changes one CW body or description target only.
Fresh native catalogs check that changed guidance rather than treating file copying as discovery proof.
All other DD and Superpowers bytes, task tools, prompts, rubrics, protected targets and allowed outputs remain fixed.

The candidate's composition references to lean-plan-writing, writing-explicit-rationale and sweeping-stale-references resolve within the same nine DD bodies.
Authoring tasks retain writing-skills and its testing/TDD background; these remain read-only next-action decisions, not executed authoring or deployment.
Ordinary prose/scope tasks do not gain an authoring toolchain merely because CW names writing-skills as the owner of authoring.
Any genuinely required missing dependency encountered during an actual run still stops the affected collection for disposition.
Description diagnostics expose no native CW body; CW-18 discovery alone permits the clothing-swap guide.
No additional paid qualification probe is required under this scoped reuse decision.
Debug does not exercise exec-only flags, model behavior or hidden provider inputs; automatic shell startup and common-provider observability limits remain unchanged.

## Reuse disposition and next gate

Reuse all 99 accepted observations, once each with their original IDs, timestamps and input revisions, as comparison context: 66 current-DD and 33 no-DD.
The exact bundles are named in the [durable evidence index](/Users/simon/work/personal/disciplined-development-skills/.worktrees/cw-validation-design/skill-validation/accepted/concise-writing/codex-gpt-5.6-sol-medium/README.md) and original two ledgers preserved there.
The original 18 input revision is `6fb4780fce37710a76116dbbeaa832a6a42289cd`; the remaining 81 use `dfd638ce5c1ac5f654110d05ce9138e5384d6afc`.
Later acceptance/navigation and existing-candidate workflow clarifications do not alter their task or scoring contracts.
Fixed order, noncontemporaneous reuse and the baseline's laptop-sleep gap remain disclosed limits; equal repetition numbers are not matched experimental pairs.

Proposed fresh collection remains 22 candidate conditions × three repetitions = 66 Codex / gpt-5.6-sol / medium calls, without adaptive repeats or new control calls.
Preservation verification, clean recoverable freeze and explicit approval of the fully expanded command batch remain launch gates.
Any later CLI, input, guidance or required-control drift invalidates affected reuse/freeze and requires disposition before execution.
