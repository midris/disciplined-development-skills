# Skilltest Codex Controlled-Input Feasibility Plan

**Status:** Completed and owner-accepted on 2026-09-06 for the scoped Codex
controlled-input claim. The result and limits are recorded below. This document
is the only repository change; runner, methodology, scenario, skill, schema and
accepted-evidence files remain unchanged. Production design and implementation
are separate follow-up work.

> **Execution:** Use `superpowers:executing-plans` in the existing isolated
> `.worktrees/skilltest-input-isolation-spike` worktree. Retain every spike artifact
> in a fresh scratch package. Before any integration call, show the exact provider,
> model, effort, prompt and complete command; wait for explicit owner approval.

**Goal:** Establish an auditable harness in which the assigned skill version is
the only intended semantic difference between comparison arms.

**Architecture:** Fresh private HOME, CODEX_HOME, temporary directory and scratch
Git project for each launch; explicit environment/configuration; declared-file
manifests and observable model-input comparisons. Use synthetic A/B skills and
positive contamination controls before one approved integration probe.

**Tech stack:** Codex CLI in iTerm2 on macOS, shell/Python scratch probes, installed
CLI help and debug capabilities. This is an experiment-control feasibility spike,
not production implementation or an effectiveness study.

## Change of objective and historical result

The original plan required outer filesystem enforcement and an inner boundary
protecting credentials from model commands. The first spike at base commit
`c39fd41d0009370282b6ac9773c38cf5ad70852c` returned BLOCKED: the candidate profile
allowed outside-file, symlink and parent-instruction reads. Preserve that result
at `/private/tmp/skilltest-input-isolation.xAqAqY/report.md`. Its references to an
application sandbox mean the CLI session's execution sandbox; this session runs in
iTerm2, not the Codex desktop app. The cause of its profile failure remains unknown.

The owner now authorizes the narrower experiment-control goal. Strict read denial
and proof that arbitrary model commands cannot read credentials are not prerequisites
for this experiment. Do not imply that this amendment repaired filesystem isolation.

The eventual supportable claim is “B performs differently from A under this
recorded harness.” Common provider instructions may interact with the edits, so
results do not establish effectiveness independently of those instructions.

## Scope and controls

- The 105 accepted baseline observations remain historical evidence; never reopen,
  rescore, replace or use them as an arm of a new controlled-input campaign.
- Do not inspect the comprehensive-skill-cleanup worktree.
- Do not modify production code, repository skills, scenarios, methodology or accepted/.
  Synthetic scratch skills are discovery instruments, not rewritten-skill tests.
- No containers, custom Seatbelt work or credential-exposure probes in this spike.
- Keep ordinary sandboxing for integration. Never print, hash or retain credentials
  in evidence, prompts, command arguments or the later exec environment.
- Every provider invocation still needs approval of its exact command; use
  codex / gpt-5.6-sol / high unless the owner explicitly approves otherwise.
- Debug output establishes observed discovery, not filesystem inaccessibility or
  equivalence to exec. Integration and subsequent trace audit remain required.

Use fresh processes/runtimes; never resume sessions or reuse conversation history,
memory, caches or task modifications. Set env -i with private HOME, CODEX_HOME,
TMPDIR, fixed PATH and only established operational additions. Clean runtimes have
no base config.toml. Later exec uses --ignore-user-config, --ignore-rules,
--ephemeral and explicit -c settings.

Declared inputs are the common prompt, project instructions, fixture, assigned skill,
launch options and observable common provider inputs. The same-name skill must occupy
the same project-relative path in both arms; only its file may differ. Give each
variant distinct description and body markers to distinguish discovery from loading.

Enumerate stable provider-bundled inputs. Identify host-admin/ambient inputs separately;
never silently label them bundled. An unexplained or competing target skill fails the
gate. Deliberately admitting any common ambient input needs owner review before design.

### Predetermined audit rules

- Preserve raw outputs. Normalize only exact per-launch root paths, separately
  recorded session/date metadata, and the intended A/B marker. Never discard whole
  instruction blocks to force equality.
- Require exactly one assigned skill catalog entry, pointing inside its declared
  project, without opposite-arm or contamination markers in a clean launch.
- Compare all other observable prompt content and common fixture hashes. Fail on
  unexplained differences; missing observations produce INCONCLUSIVE.
- Unexpected semantic-file reads invalidate an integration observation. Do not
  silently drop contaminated arms or retry for a better verdict. Later campaigns
  must report contamination by arm and assess differential exclusions.
- An omitted exact integration read is INCONCLUSIVE; self-report is not provenance.
- Infrastructure-only attempts follow existing INFRA_RETRY handling: scratch-only
  evidence and retry only the exact unchanged approved command.

## Task 1: Allocate and record the package

- [x] Allocate mode-0700 `/private/tmp/skilltest-controlled-inputs.XXXXXX` with
  README.md, report.md, commands/, outputs/, fixtures/ and runtime/.
- [x] Record base commit and amended-plan SHA-256, platform/CLI version, launcher
  context, non-secret environment and initial repository state.
- [x] Create a recorder retaining argv, cwd, stdout, stderr and exit status with
  unique labels; never overwrite earlier attempts.
- [x] Retain synthetic A/B SKILL.md files named discovery-probe, shared AGENTS.md,
  allowed.txt and task prompt. Manifest their hashes.
- [x] Create a scratch-only ambient home with a same-name competitor skill,
  global-instruction canary and config-instruction canary. Never install host canaries.
- [x] Give each scratch project its own .git root and no skill symlinks. Put a
  parent AGENTS.md canary outside the projects to check ancestry discovery.

## Task 2: Inventory controls and contamination detection

- [x] Capture version, exec help and debug prompt-input help through the private wrapper.
- [x] Enumerate actual user/admin/plugin discovery root existence without opening
  host instruction or credential payloads. Record the clean debug catalog separately.
- [x] Run debug prompt-input under the deliberately contaminated scratch home.
  Require the competing-skill, global and config markers to be observed.
- [x] Run from a nested directory under a controlled parent AGENTS.md as a separate
  positive control. Require the clean project-root launch to exclude the outside parent.
- [x] All required positive-control canaries were observed; no alternate-path
  investigation was needed. An ineffective canary would not prove suppression.

## Task 3: Compare four fresh synthetic launches

- [x] Launch A, B, B, A with fresh runtimes/projects. This order checks carryover;
  it is not effectiveness sampling or a sufficient randomization scheme.
- [x] Require equal common-file manifests and only the assigned skill difference.
  Reject symlinked skills and cross-arm references.
- [x] Require one assigned skill entry at the declared path in every launch, no
  competitor/opposite marker and no parent/global/config canary.
- [x] Retain raw JSON and normalized comparisons using the rules above. Inventory
  every common skill and provider instruction block.
- [x] Hash private bootstrap skill files for equality across launches. Never hash auth.
- [x] Report debug blind spots (exec rules, tool connections, subsequent body reads);
  do not declare overall FEASIBLE before integration.

Stop provider preparation if a required discovery control fails: BLOCKED for a
demonstrated failure, INCONCLUSIVE for unavailable evidence. Do not substitute a
filesystem-enforcement requirement for this experiment-control gate.

## Task 4: Prepare one integration probe after provider-free gates pass

- [x] Use a fifth fresh synthetic A launch with the same declared inputs, explicit
  exec controls and normal sandbox restrictions.
- [x] Provision auth only when needed via documented stdin login or explicitly
  file-backed private auth-cache copy, mode 0600. Retain only method and success/failure.
  Do not inspect secrets to determine the store. If unavailable, report INCONCLUSIVE.
- [x] Prepare complete command, prompt and output paths. Prompt requests
  $discovery-probe and exact reads of declared SKILL.md and allowed.txt, then their
  non-secret markers. Do not request host/credential reads.
- [x] Show provider codex, model gpt-5.6-sol, effort high, complete command including
  environment/cwd/redirections, and prompt. Wait for explicit approval.
- [x] Run once after approval, subject to unchanged INFRA_RETRY. Inspect complete
  JSONL/tool trace for actual assigned-skill/fixture reads and unexpected semantic
  inputs. Record exec/debug differences.

This is one-arm wiring corroboration, not an A/B result. Later implementation must
verify both arms. While awaiting approval, retain only an unauthenticated runtime
or recreate and re-audit a fresh one later; do not leave copied credentials.

## Task 5: Report and stop

- [x] FEASIBLE requires all provider-free gates and approved integration to pass;
  BLOCKED means a demonstrated control failure; INCONCLUSIVE means missing evidence,
  pending approval or unavailable authentication.
- [x] Report checklist, version/environment, manifests, normalizations, exact
  commands/statuses, comparisons, contamination controls, approval/attempt counts,
  common provider inputs and unresolved blind spots.
- [x] After recording the report, delete the exact private runtime directories and
  verify absence. Preserve credential-free commands, fixtures, outputs and report.
- [x] Verify main unchanged and feature worktree diff limited to this plan. Present
  the scratch report and stop for owner review.

## Accepted result: controlled-input harness is feasible

The owner accepted the final result with “that is great, document that” after
reviewing the successful integration summary. This is acceptance of the scoped
feasibility finding, not authorization to implement the production runner or
begin effectiveness/rewrite comparisons.

| Check | Retained finding |
| --- | --- |
| Platform | Codex CLI 0.153.4, macOS 26.6.2 (25G83), arm64; iTerm2 |
| Contamination detection | Scratch competitor skill, global/config instructions and parent instruction controls were observed |
| Four fresh launches | A/B/B/A each discovered exactly one assigned skill at its declared path |
| Input comparison | Complete debug inputs equal after exact runtime-path, assigned marker, message-ID and creation-time normalization |
| Fixture/bootstrap comparison | Common files and all 60 bootstrap files matched; only assigned skill differed |
| Authentication | Private file-backed ChatGPT cache validated, mode 0600; no credential in exec environment |
| Approved integration | codex / gpt-5.6-sol / high; one attempt, exit 0, empty stderr |
| Model-issued command | Exact requested cat of assigned SKILL.md and fixture; output matched both retained files |
| Other visible tool actions | None |
| Cleanup | All private runtimes and copied authentication removed; scratch evidence retained |

The observed model command was:

```sh
/bin/zsh -lc '/bin/cat .agents/skills/discovery-probe/SKILL.md fixture/allowed.txt'
```

It returned the assigned `CI_BODY_A_MTAyGQ` and `CI_FIXTURE_MTAyGQ` markers.
Provider approval was explicit: “approved, let's try it”. No INFRA_RETRY occurred.

The tested pre-result plan digest was
`8b55c012534715db62846e34a68133f7f5d7e981413b70413903139839111352`;
the base commit was `c39fd41d0009370282b6ac9773c38cf5ad70852c`. This completion
record changes the document digest; it does not change which plan was tested.

The durable result is this section. Detailed evidence remains disposable scratch,
not accepted scenario evidence, and may disappear if the host clears /private/tmp:

- Final report: `/private/tmp/skilltest-controlled-inputs.MTAyGQ/report.md`.
- Exact invocation/prompt: `commands/provider-command.sh`, `commands/provider-prompt.txt`.
- Deterministic evidence: `outputs/audit.json`, `outputs/manifests.json`,
  per-launch raw/normalized inputs and diffs.
- Integration evidence: `outputs/provider-approval.json`,
  `outputs/provider-attempt.json`, `outputs/provider-stdout.jsonl`,
  `outputs/provider-stderr.txt`, `outputs/integration-audit.json`.
- Cleanup evidence: `outputs/cleanup-final.json`.

### Limits carried into production design

- The original strict filesystem-isolation result remains BLOCKED.
- Five common bootstrap skills remained: imagegen, openai-docs, plugin-creator,
  skill-creator and skill-installer. Results are conditional on that common harness.
- Debug JSON and exec traces do not expose the full provider request or every
  automatic runtime read. Login-shell startup reads were not independently audited.
- Private local runtimes do not clear remote prompt caching. The integration
  reported 28,442 input tokens, 24,576 cached input tokens and 136 output tokens.
  Record and consider caching in later comparisons; distinguish it from reused
  local session state.
- Only synthetic arm A was provider-tested. Both production arms and actual
  scenarios still need verification; these observations are not effectiveness data.
- No existing baseline was reopened and no rewritten skills were evaluated.

## Claude capability assessment: available, not yet qualified

This section records the initial assessment.
The separate [Claude spike](2026-09-06-skilltest-claude-controlled-inputs.md#accepted-scope-and-next-checkpoint) subsequently reached owner-accepted scoped feasibility.
Its evidence and limits are independently established, not inferred from the Codex result.

Provider-free inventory on 2026-09-06 confirmed installed Claude Code 2.1.261.
The existing runner already accepts provider `claude`, model and effort and invokes
noninteractive runs with session persistence disabled. Its current environment
inherits the controller environment plus baseline overrides; it is not yet a
qualified controlled-input adapter.

The installed help exposes `--setting-sources`, `--settings`,
`--strict-mcp-config`, `--no-session-persistence`, `--output-format stream-json`,
`--debug-file`, explicit model/effort and tool/permission controls.
These are sufficient to justify a separate feasibility investigation, not to
declare Claude qualified from the Codex result.

Prefer investigating fresh private HOME/CLAUDE_CONFIG_DIR, an explicitly selected
project skill, controlled settings/MCP sources, contamination controls and a trace
audit. Keep native skill discovery/invocation in scope. Simply disabling all
skills or pasting a skill into the system prompt would test a different mechanism.

The installed `--bare` help says it skips several automatic inputs including
CLAUDE.md and keychain reads, still resolves explicit /skill-name invocation, and
requires API-key/helper authentication for Anthropic rather than OAuth/keychain.
Do not select it without checking that authentication and skill invocation match
the intended experiment. Managed settings also require inventory.

An equivalent to Codex's provider-free `debug prompt-input` command was not
identified in the inspected top-level help. This does not prove one is unavailable.
A Claude spike must establish an observable discovery/provenance check or report
that evidence limitation before integration.

Raw installed version/help and explicit private inventory environment are retained
at `/private/tmp/skilltest-claude-inventory.J5v2CW/outputs/`. Only version/help were
invoked; no Claude model or authentication was invoked. Current
[CLI documentation](https://code.claude.com/docs/en/cli-reference) and
[programmatic usage](https://code.claude.com/docs/en/headless) were consulted;
installed-version observations take precedence over assuming identical behavior.

A Claude spike is separate follow-up work. Select its exact model, effort and
authentication approach during planning; present every proposed integration command
for explicit approval. Do not silently carry Codex model names or the existing
Claude pin expectations into a new comparison.

## Post-spike decision

After owner acceptance of FEASIBLE, prepare a design amendment and separate
test-driven implementation plan; do not implement automatically. Before effectiveness
runs, reconcile the methodology's strict-isolation language with this scoped claim:
comparison eligibility, contamination handling, common-input manifests and invalidation.

Then plan repeated randomized/interleaved within-scenario comparisons: Sol high,
medium and low as separate strata; Terra high as a possible separate baseline-model
comparison. Define sample sizes, metrics and stopping rules before collecting data.
Account for provider drift and contamination by arm. No rewritten-skill comparisons
until the harness and methodology are owner-accepted.

## References

- [Baseline lifecycle](specs/2026-09-03-skill-validation-baseline-design.md#accepted-baseline-set-lifecycle)
- [Existing verdict order](completed/specs/2026-09-02-skill-testing-methodology-design.md#scenario-verdict)
- [Codex skills](https://developers.openai.com/codex/skills)
- [CLI reference](https://developers.openai.com/codex/cli/reference)
- [Authentication](https://developers.openai.com/codex/auth)

Installed-version evidence governs the spike; documentation is context, not proof.
