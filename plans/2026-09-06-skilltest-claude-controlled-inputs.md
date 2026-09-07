# Claude Controlled-Input Feasibility Spike

**Status:** Completed and owner-accepted on 2026-09-06 for the scoped FEASIBLE finding.
The owner authorized documenting acceptance and reviewing the next steps one at a time.
The initial INCONCLUSIVE integration checkpoint and later provider-free catalog PASS remain historical evidence below.
Full real-provider request equality is not claimed.
Production implementation and new model calls are not authorized by acceptance.
Use `superpowers:executing-plans` in the existing isolated feature worktree.
During the spike, this plan and its result summary were the only new repository changes.
Post-acceptance documentation also links the Codex finding and opens the design amendment.
Retain commands, policies, fixtures, raw requests and traces in disposable scratch.

## Accepted scope and next checkpoint

Claude's recorded controlled native-discovery/loading harness is feasible for developing skill-edit comparisons.
The accepted evidence combines contamination controls, mock request/native-A/B checks, one approved real arm-A load, and matching subscription-context A/B/B/A initialization metadata.
Provider features may remain as recorded common experimental inputs: equality between comparison arms matters, not equality between subscription and mock authentication modes.
This accepts the documented observability limits, not unknown host instructions or uncontrolled provider drift.
Real arm-B loading, representative scenario toolsets and repeated effectiveness runs remain unqualified.
The original strict filesystem-isolation failure is unchanged.

Acceptance does not alter the 105 historical baseline verdicts or evidence sets, and they will not serve as an arm of a new controlled-input comparison.
Raw spike evidence remains disposable scratch; the findings and limitations in this document are the durable record.
No scratch runtime or copied credential remains, and shared Claude authentication was never logged out.

The next work is the [controlled-input methodology and runner design amendment](specs/2026-09-06-skilltest-controlled-inputs-design.md).
Review methodology first, runner design second, then a separate test-driven implementation plan.
Implementation, provider qualification and repeated effectiveness campaigns each follow their own approval checkpoints.
Historical references below to pending owner review describe the state when that evidence was collected; this acceptance section governs current status.

**Goal:** Determine whether fresh Claude launches can discover only an assigned
skill version while all other observed experimental inputs remain controlled.

**Contract:** Follow the scoped experimental claim and contamination rules in
[the accepted Codex plan](2026-09-05-skilltest-provider-input-isolation.md).
Claude is independently qualified; neither strict filesystem isolation nor skill
effectiveness is being claimed. Do not modify runner, skills, scenarios, methodology
or accepted evidence, and do not inspect the unrelated rewrite worktree.

## Task 1: Establish observable provider-free requests

- [x] Allocate mode-0700 `/private/tmp/skilltest-claude-controlled.XXXXXX`; record
  base commit, plan digest, version/platform, environment and before/after git state.
- [x] Capture installed help/version using private HOME and CLAUDE_CONFIG_DIR.
  Use explicit minimal environment and non-secret dummy authentication only.
- [x] Evaluate a localhost-only mock Messages endpoint using the documented
  ANTHROPIC_BASE_URL override. It returns fixed synthetic text, never invokes a
  model and never forwards requests. Reject unexpected auth without retaining it.
- [x] Surround only the mock CLI process with a network policy denying non-loopback
  connections. Qualify loopback success and deterministic non-loopback denial before
  starting mock CLI requests. This is a provider-free guard, not filesystem isolation.
- [x] Retain complete non-secret request bodies, CLI output, commands, exit codes
  and network policy. Give every attempt a unique directory; never overwrite logs.
- [x] If local capture is unavailable, inspect documented local diagnostics. Do
  not treat missing evidence as passing; report INCONCLUSIVE if discovery remains
  unobservable. No real model request without exact-command approval.

## Task 2: Test controlled native skill discovery

- [x] Prepare synthetic same-name A/B skills under project `.claude/skills/`, common
  CLAUDE.md and fixture. Manifests may differ only at the assigned skill file.
- [x] Preserve native skill discovery; do not use --safe-mode or disable all skills.
  Start with private HOME/CLAUDE_CONFIG_DIR, --setting-sources project,
  --strict-mcp-config with an empty server map, no-session-persistence and explicit
  memory/connection settings. Record any additional switches necessary to operate.
- [x] Create positive controls for competing user skills and global instructions
  exclusively in a disposable surrogate user profile. Test controlled ancestor
  instructions too. Do not create canaries in the actual host profile.
- [x] Enumerate host/admin discovery root existence without opening payloads.
  Any unaccounted ambient semantic input in a clean request fails the gate.
- [x] Capture A/B/B/A requests from independent runtimes. Compare assigned skill
  catalogs and complete system/messages/tool definitions. Normalize only exact
  launch-root paths, intended skill markers and explicitly recorded incidental
  IDs/timestamps/request metadata. Preserve and explain every normalization.
- [x] A canary not observed in its positive control proves nothing about suppression.
  If ancestor instructions remain discoverable, a clean ancestry manifest can be
  evaluated as a scoped control; record both results without claiming read denial.
- [x] Do not silently accept unstable prompt content. Investigate bounded operational
  differences; if they cannot be pinned or declared, report INCONCLUSIVE.

## Task 3: Private authentication and real integration preparation

- [x] After discovery gates pass, inspect only safe authentication status and
  credential-store metadata. Never dump credential payloads or keychain secrets.
- [x] Establish an authentication route compatible with controlled discovery.
  Authentication available only via an unavailable/private store is INCONCLUSIVE,
  not permission to copy whole profiles or expose credentials.
- [x] Prepare one native-skill integration prompt requiring actual assigned skill
  and fixture reads. Use the owner's selected Claude model/effort and explicit CLI
  controls; do not infer approval from the Codex command.
- [x] Present the full provider command, model, effort, prompt, authentication
  mechanism and differences from the local mock (endpoint/auth/network). Wait for
  explicit owner approval before contacting a real model endpoint.
- [x] After approval, require native assigned-skill loading and exact fixture markers
  in complete stream-json/tool trace; unexpected semantic inputs invalidate the
  observation. Apply unchanged-command INFRA_RETRY only for understood infrastructure
  failures; retain all attempts and do not retry a contaminated behavioral result.

## Task 4: Report and cleanup

- [x] FEASIBLE requires deterministic discovery evidence plus approved integration;
  BLOCKED means a demonstrated failure of the candidate; INCONCLUSIVE means missing
  evidence, unavailable authentication or pending approval. Report the precise scope.
- [x] Preserve raw evidence in scratch; record a concise result summary in this plan
  after owner review. Do not promote spike artifacts into accepted/.
- [x] Delete exact disposable runtimes and any copied credentials after reporting;
  while waiting for approval retain only unauthenticated fixtures/runtime if needed.
- [x] Verify main unchanged, repository diff limited to this plan, and stop for
  owner review before production design, implementation or effectiveness runs.

## Questions to answer explicitly

Does the native skill catalog contain only the intended version? Can controlled
contamination be detected? Are the remaining request inputs stable under the recorded
normalizations? Does private authentication work without importing semantic profile
state? Does one approved real run load the intended skill and fixture? What differs
between mock/API-key and real subscription/API-key behavior, including managed inputs?

## References

- [CLI reference](https://code.claude.com/docs/en/cli-reference)
- [Environment variables](https://code.claude.com/docs/en/env-vars)
- [Programmatic usage](https://code.claude.com/docs/en/headless)
- [Skills](https://code.claude.com/docs/en/skills)

Installed-version evidence governs; help and documentation are not enforcement proof.

## Provider-free checkpoint, 2026-09-06

Codex documentation committed as `eb9e54baa6abb613a580b4f3f6b93444e8a92836`.
The Claude spike used installed 2.1.261 on macOS 26.6.2 arm64; the local sonnet
alias resolved to `claude-sonnet-5`, with high effort in every captured request.

The localhost stub plus qualified non-loopback network denial made actual request
assembly observable without invoking a model. All four fresh A/B/B/A requests
matched after exact runtime-path, intended skill-marker and metadata device/session
normalization. Complete system/message/tool content was retained and compared.

Positive controls detected competing user skill and global instructions. The user
skill displaced the project variant in the deliberately contaminated case. Claude
also read an ancestor CLAUDE.md outside the project Git root. Clean launches used
verified empty ancestry, not an assumption that .git stops instruction discovery.

Fixed mock responses then invoked the native Skill and Read tools in fresh A and B
projects. Both loaded the corresponding declared skill body and fixture. The complete
three-request sequences matched after the declared A/B body-marker normalization.
These are deterministic tool-wiring observations, not model-behavior observations.

Nine mock CLI launches produced thirteen locally served Messages requests. All CLI
launches passed; no real model call, real API charge or credential forwarding occurred.
The shared built-in skill catalog remains a declared provider input. Only Read and
Skill were exposed; MCP servers and plugins were absent in observed init records.

Host execution of auth status confirmed an active claude.ai login; private-profile
status reported no login. No reusable file cache or supplied API/OAuth environment
credential was available. The earlier sandbox-context status false result was not
mistaken for absence of the host login. No keychain payload was read or extracted.

A separate private subscription login was initially proposed at this checkpoint,
but is superseded by the existing-login investigation below. The prepared
`private-login.sh` invokes documented `claude auth login --claudeai`; it requires
the owner's browser sign-in. No login has been started. If it creates a
private-profile keychain entry, use documented logout for that exact private profile
before final runtime deletion; never log out the host profile.

Evidence and prepared commands remain at
`/private/tmp/skilltest-claude-controlled.cvOybM/`:

- `report.md`: findings, limits, task status and auth prerequisite.
- `outputs/request-audit.json`, raw/normalized request files and empty diffs.
- `outputs/native-audit.json`: both native skill-body/fixture checks.
- `outputs/*auth*.json`: sanitized status and metadata only.
- `private-login.sh`: browser sign-in preparation, not executed.
- `provider-command.sh`: proposed Sonnet 5/high integration, not approved or executed.
- `outputs/checkpoint.json`: cleanup and repository verification.

Ten mock/inventory runtimes are removed at this checkpoint; only the unauthenticated
integration runtime is retained. No copied credentials, production code changes or
accepted-evidence changes occurred. Full real-provider qualification and owner review
remain pending. The proposed model/effort will be confirmed with the exact command;
the local alias resolution is not itself model-call approval.

## Existing-login follow-up, 2026-09-06

The owner asked to reuse the signed-in subscription before attempting another login,
and to avoid affecting running Claude sessions. No separate login was started.

Read-only controls found that the minimal environment had omitted USER. Normal HOME
without USER reported no login; normal HOME plus USER=simon reported an active
claude.ai subscription. Private HOME or private CLAUDE_CONFIG_DIR still did not
reuse the login. Therefore the replacement candidate keeps normal HOME/USER and
separates semantic discovery with explicit settings plus a child-only policy.

The candidate denies writes beneath the real home and reads of the listed user
instruction/config/skill/plugin/agent/history roots, while keeping authentication
identity state readable. It is not a general filesystem-isolation requirement.
An offline auth-status check under that policy succeeded. No credential value was
extracted, copied, hashed, logged or placed in the proposed exec environment.

Four fresh native A/B/B/A sequences against the local stub matched completely after
the declared trial-path, assigned description/body marker and metadata-ID
normalizations. All loaded the assigned project skill and fixture. An explicit
user-discovery positive control exposed competing skill/global instruction canaries;
the matching read-denied case suppressed them. Direct surrogate probes confirmed
EPERM for installed-skill reads and home writes. Initial project-only controls that
did not expose canaries were retained and not misclassified as passing controls.

All policy/environment changes applied only to child processes. No running session
was resumed, stopped or signed out. No host configuration was edited. A future real
call would share subscription usage limits; the filesystem guard does not exclude
normal token maintenance by keychain services. Never use logout to clean up this
shared-auth candidate.

Detailed findings are in
`/private/tmp/skilltest-claude-controlled.cvOybM/reuse-report.md`;
`outputs/reuse-audit.json` records passed checks and `outputs/reuse-checkpoint.json`
records cleanup and exact policy/command digests. The replacement proposal is
`provider-reuse-command.sh`, retaining Sonnet 5/high, native Read/Skill, project-only
settings, strict empty MCP and disabled persistence. It removes the local stub and
dummy key only for the future separately approved real invocation. The old
`private-login.sh` and `provider-command.sh` are superseded and must not be run.

The reuse runtimes and surrogate home are removed after this report; only the
unauthenticated integration fixture is retained. Real subscription request behavior
remained to be checked at this checkpoint, because local gateway/API-key behavior may
differ in managed and provider inputs. The checks did not themselves authorize a call.

## Approved integration checkpoint: awaiting owner review

The owner subsequently approved the exact `provider-reuse-command.sh` with “approved”.
One Claude / claude-sonnet-5 / high invocation reused the existing subscription and
exited 0 with empty stderr. No separate login, logout, credential copy, host settings
edit or running-session manipulation occurred. Shared subscription usage applies;
normal keychain token maintenance is not excluded by the home-write policy.

The complete thirteen-event trace showed exactly Skill(discovery-probe) followed by
Read of the declared fixture. The loaded skill body and returned fixture matched
their retained sources exactly. Both arm-A markers appeared in the final answer.
No other tool calls, permission denials, MCP servers or plugins were observed.
One CLI invocation made two provider requests, with no INFRA_RETRY.

However, the real catalog added a `schedule` skill relative to the local mock, plus
`schedule`, `usage-credits` and `extra-usage` slash commands. These differences were
not discarded. Their provenance and A/B stability are not qualified, and the full
real request is not exposed by stream-json. Therefore native loading/subscription
reuse PASS, but overall controlled-input qualification is INCONCLUSIVE. This is not
a demonstrated A/B failure; owner review is needed before admitting or controlling
the additional provider input. The run cannot count as a clean qualification result
under the unexpected-input rule. Do not retry it for a different verdict.

The scratch report is `/private/tmp/skilltest-claude-controlled.cvOybM/final-report.md`.
Exact approval/attempt records, raw trace and checks are in
`outputs/provider-reuse-approval.json`, `outputs/provider-reuse-attempt.json`,
`outputs/provider-reuse-stdout.jsonl` and `outputs/integration-reuse-audit.json`.
No production work or effectiveness comparisons have begun. A durable accepted
result summary remains pending owner review.

The final integration runtime and its empty parent were removed without logout;
source fixtures and retained evidence remain. `outputs/reuse-cleanup-final.json`
confirms main clean at c39fd41 and feature HEAD eb9e54b, with only this new plan
untracked. No accepted evidence or production file was modified.

## Approved catalog follow-up, 2026-09-06

**Goal:** Qualify the observable surrounding inputs across subscription-authenticated
A/B arms, rather than require a subscription catalog to equal an API-key mock.
**Architecture:** Preserve the existing native-discovery controls and shared-login
policy. Attribute the observed catalog delta, then compare fresh subscription-context
A/B/B/A launches. Prefer a no-inference initialization interface under verified
network denial; never send real authentication to a mock endpoint.
**Tech stack:** Installed Claude Code 2.1.261, read-only executable inspection,
stream-json control protocol if available, macOS child policy and scratch Python.
**Spec:** The scoped experimental contract above and the owner's approved follow-up.
Use `superpowers:executing-plans` inline in the current feature worktree.

Only this plan changes in the repository. Create scripts, policies, manifests,
commands and results in `/private/tmp/skilltest-claude-catalog.2hg9Ed/`. Preserve all
prior results, including the first integration's INCONCLUSIVE qualification.
No login/logout, account changes, credential extraction/copy/hash or interception.
No change to running sessions, host settings, production files or accepted evidence.

### C1: Attribute catalog differences and qualify observability

- [x] Record controller-context git state, platform, executable identity/hash and
  amended-plan digest. Inspect installed executable strings for the three additional
  commands and their authentication/feature gates; retain bounded relevant excerpts.
- [x] Check documentation and installed initialization protocol for catalog reporting
  without user prompts/inference. If available, use only initialization requests,
  fresh scratch fixtures, the same semantic-read/home-write guards and network denial.
- [x] Qualify network denial with a deterministic socket probe, then test the
  initialization interface. No auth payload inspection or forwarding to localhost.
  Retain exact argv/env/stdin, raw output, stderr, timeout and exit status.
- [x] Distinguish executable provenance, advertised catalog, model-visible description
  and loaded body. Do not substitute a command-menu list for full prompt equality.

### C2: Compare fresh subscription-context A/B/B/A catalogs

- [x] Prepare four fresh projects from the retained synthetic A/B source fixtures.
  Verify clean ancestry, no symlinks and common manifests differing only at SKILL.md.
  Keep model claude-sonnet-5, effort high and all other controls fixed.
- [x] If no-inference initialization works, compare the complete returned command
  metadata, agents, models and other observable common configuration. Normalize only
  exact launch paths, assigned description markers and recorded incidental IDs.
  Require the intended skill description exactly once, no opposite/host canaries and
  a stable surrounding catalog. Separately compare with the previous real init.
- [x] Determine whether offline authentication/feature-cache behavior differs from
  real startup. Missing evidence stays INCONCLUSIVE; do not infer full-request parity.
- [x] If model calls are needed, prepare a bounded fresh A/B/B/A integration sequence
  and show every complete command, prompt, provider/model/effort for approval before
  invocation. No real calls are authorized by approval of this amendment alone.
  Audit native skill and fixture loading, catalogs and every visible tool action.
  **Disposition:** No new model calls needed for this catalog question. The prior
  real arm-A native-loading trace remains corroboration only; no real arm-B or full
  real-request-equality claim is added by initialization.

### C3: Report the scoped conclusion and stop

- [x] Stable, attributed provider features may be proposed as recorded common inputs
  for both arms. Do not silently admit unexplained host/admin sources or discard
  differing semantic blocks. Record provider drift and unavailable observability.
- [x] Report PASS only for established checks; overall FEASIBLE needs the stated
  subscription-context evidence plus native integration coverage, with limits explicit.
  A new follow-up result does not retroactively rescore the previous observation.
- [x] Remove exact disposable runtimes without logout, retain credential-free evidence
  and report in scratch, verify main unchanged and only this plan changed, then stop
  for owner review. No production implementation or effectiveness run follows automatically.

### Catalog follow-up result: owner review pending

Six network-denied initialization-only processes completed: a subscription pilot,
four fresh subscription A/B/B/A launches and a dummy API-key control. Each received
only an `initialize` control request and returned one successful response, idle,
exit 0. There were no new model prompts or provider calls. Deterministic probes
verified both loopback and non-loopback connection denial before Claude launched.

All four complete subscription initialization payloads matched after normalizing
only the assigned skill description marker and recorded process ID. Exact per-trial
runtime paths were the only launch-record normalization. There were 44 common
commands plus one assigned project skill. Returned descriptions/aliases, agents,
model catalog, account metadata and configuration were compared. All 45 command
names matched the previous approved real run, as did agent names and output style.
Common fixture manifests matched; only assigned SKILL.md content differed by arm.

Installed executable code attributes `schedule` to a provider skill with subscription
and remote-policy gates. It defines `usage-credits` and its `extra-usage` compatibility
name as local commands enabled by account/billing state. The offline API-key control
excluded those three and also `heapdump`, a provider local command gated by
allow_heap_dump. That fourth control difference was retained and attributed without
claiming to resolve its full policy path. It was not an original added skill and did
not differ across subscription arms. Shared API/subscription command metadata matched;
model/account fields differed with auth mode. The API control's auth-precedence
warning was retained. No command was invoked merely to determine its availability.

The recommendation is FEASIBLE for this recorded controlled native-discovery/loading
harness, combining the new catalog evidence with prior contamination checks, mock
request/native-A/B comparisons and approved real arm-A loading. Initialization is
not a full real request capture; only arm A has real model-loading evidence. Future
online feature/account drift and scenario toolsets require checks during production
design/qualification. Record stable provider features as common inputs only after
owner acceptance; compare per-run catalogs and pause/flag unexplained drift. Findings
remain conditional on the recorded harness, not provider-independent effectiveness.

The previous INCONCLUSIVE checkpoint is preserved, not retroactively rewritten.
The new report is `/private/tmp/skilltest-claude-catalog.2hg9Ed/report.md`, with exact
commands/raw responses, binary excerpts and `outputs/catalog-audit.json`. Executable
SHA-256 is `5efecaff231b798be3c66def9be54183623b328b80eaef17f93c43987024e82a` for
Claude Code 2.1.261 on macOS 26.6.2 arm64. No login/logout, credential extraction/copy,
host settings edit or running-session manipulation occurred. No production changes
or effectiveness observations were made. Owner review remains the next checkpoint.

All six follow-up runtimes and their empty parent were removed without logout.
Source fixtures and retained evidence remain. `outputs/cleanup-final.json` records
main clean at c39fd41, with only this plan untracked in the feature worktree.
