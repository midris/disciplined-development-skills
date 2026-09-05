# Skilltest Codex Input Isolation Feasibility Plan

**Status:** Deferred until the current-skill baseline campaign is complete. This
plan authorizes no runner changes, provider invocations, or changes to accepted
evidence. When activated, it begins with a throwaway scratch spike. Production
design and implementation planning occur only after the owner reviews the spike.

> **Execution:** Use `superpowers:executing-plans` when this plan is activated.
> Keep every spike artifact in scratch. Before the single integration probe,
> present the exact provider, model, effort, and command and wait for explicit
> approval.

**Goal:** Determine the smallest maintainable Codex-only boundary that excludes
undeclared host inputs, keeps authentication unavailable to model-generated
commands, and deterministically denies non-operational reads outside the declared
workspace while allowing the minimum recorded runtime dependencies.

**Architecture:** Provision a private `HOME` and `CODEX_HOME`, suppress
documented user configuration and rules discovery, and evaluate a separately
qualified filesystem boundary around the Codex process. Provision authentication
through a documented login flow rather than passing credentials to `codex exec`.
Prove allowed and denied filesystem behavior with deterministic commands before
using a provider. Treat provider transcripts as integration evidence, never as
proof of enforcement. Stop after reporting the spike outcome for owner review.

**Tech stack:** macOS, the installed Codex CLI, shell commands retained in scratch,
and the current Python skilltest runner as read-only context.

## Why this is deferred

The baseline campaign is teaching us how to audit scenarios and apply the scoring
methodology. Changing the provider boundary during that campaign would change the
approved execution policy. Under the
[baseline-set lifecycle](../specs/2026-09-03-skill-validation-baseline-design.md#accepted-baseline-set-lifecycle),
that creates a new comparison key and makes existing accepted sets unsuitable as
an arm of the new campaign.

Finish the current campaign first. Existing accepted records remain valid
historical evidence for the inputs and runner contract under which they were
collected. Do not rewrite or retroactively relabel them. Before current-skill versus
rewritten-skill comparisons, run this spike and decide whether a production
isolation boundary is feasible.

## Observed defect

The Codex adapter currently passes `env=None` to `subprocess.Popen`, so the child
inherits the controller environment. A prepared temporary workspace does not
prevent Codex from discovering inputs through the host profile. During baseline
testing, Codex read the installed `using-superpowers/SKILL.md`, which was not a
declared scenario fixture.

For the current baseline campaign, disclose such reads as fixture/task-fidelity
failures and apply the existing
[scenario verdict order](../completed/specs/2026-09-02-skill-testing-methodology-design.md#scenario-verdict).
Do not claim strict fixture-only execution. Edit and A/B effectiveness testing
remain blocked until both arms can run under the same qualified boundary.

## Scope

This plan deliberately stops before production design:

- The spike covers Codex only. Claude isolation is a separate future decision.
- The spike does not modify the runner, skills, scenarios, methodology, result
  schema, or `accepted/`.
- The spike does not design a transcript parser or a new status taxonomy.
- Prompt instructions are not an isolation boundary.
- A model's refusal, self-report, or failure to mention an outside input does not
  prove that the input was unavailable.
- A successful spike qualifies only the exact host platform, Codex version,
  authentication mechanism, and boundary policy tested. It does not establish
  universal enforcement.

## Input and evidence distinctions

- **Declared semantic inputs:** retained prompt template, rendered prompt, and
  declared fixture copies.
- **Declared operational inputs:** executable and version, model, effort, fixed
  adapter flags, network/service access, authentication mechanism, and the minimum
  environment required to operate.
- **Forbidden ambient inputs:** host project instructions, user configuration,
  rules, memories, MCP configuration, plugins, user-installed skills, and files not
  declared by the scenario.
- **Provider-bundled behavior:** functionality compiled or packaged with the pinned
  Codex release that cannot be disabled. This is an operational input, not a
  scenario fixture.
- **Host-admin input:** host-managed configuration or skills such as
  `/etc/codex/skills`. These are ambient inputs and are distinct from
  provider-bundled behavior.
- **Policy applied:** the intended launch options and filesystem policy were
  mechanically installed for this run.
- **Boundary qualified:** deterministic probes passed for the recorded platform,
  Codex version, and policy digest.
- **Transcript audit:** the observed model/tool trace was clean, showed a
  violation, or was unavailable. A clean transcript does not establish boundary
  qualification.

Codex can discover skills from repository, user, admin, system, and plugin
locations ([skills documentation](https://developers.openai.com/codex/skills)).
`codex exec` supplies `--ignore-user-config` and `--ignore-rules`
([CLI reference](https://developers.openai.com/codex/cli/reference)).
Authentication is provisioned with `codex login`, and credentials may be stored
in `CODEX_HOME/auth.json` or an OS credential store
([authentication documentation](https://developers.openai.com/codex/auth)).
`shell_environment_policy` controls what model-generated subprocesses inherit
([configuration reference](https://developers.openai.com/codex/config-reference)).
Codex permission profiles can deny reads outside workspace roots and can be selected
for direct `codex sandbox` probes
([permissions documentation](https://developers.openai.com/codex/permissions)). They
are beta, so any result is specific to the tested CLI version.
These controls must be tested together; none alone establishes full input
isolation.

## Activation gate

Do not begin the spike until all of these are true:

- [ ] All current-skill catalogs and the suite-composition catalog have completed
  the baseline campaign.
- [ ] The owner explicitly activates this deferred plan.
- [ ] The owner agrees that the spike is exploratory and scratch-only.
- [ ] The owner agrees that any later isolated campaign is a new comparison
  campaign and that both arms must use the same runner version and isolation
  policy.

## Spike questions

The spike answers only these questions:

1. Can Codex authenticate from a private runtime without passing a credential in
   the environment of `codex exec`?
2. Can documented flags and the private runtime suppress host profile, rules, and
   skill discovery?
3. Can the boundary keep credentials and credential-shaped environment values
   unavailable to model-generated commands?
4. Can a deterministic command read a declared file while direct and symlinked
   reads of a non-operational file outside the declared workspace fail?

## Task 1: Allocate a disposable spike package

Create one mode-`0700` directory under `/private/tmp` with this layout:

```text
<spike-root>/
  README.md
  commands/
  outputs/
  runtime/
    home/
    codex-home/
    tmp/
  project/
    .git/
    AGENTS.md
    workspace/
      fixture/
        allowed.txt
      outside-link
  outside/
    denied.txt
  report.md
```

- [ ] Record the plan commit, date, OS version, architecture, and installed Codex
  version in `README.md`.
- [ ] Put unique, non-secret sentinel text in `allowed.txt` and `denied.txt`.
- [ ] Make `outside-link` a symlink to `outside/denied.txt`.
- [ ] Initialize `project/` as a scratch Git repository and put a unique,
  non-secret forbidden-instruction sentinel in `project/AGENTS.md`. Run Codex from
  `project/workspace/`, making the parent file an effective project-instruction
  discovery canary rather than an instruction for the spike executor.
- [ ] Create `commands/run-private.sh` so every capability check, sandbox probe,
  debug command, private login command, and later provider command starts with an
  explicit minimal environment: `HOME=<spike-root>/runtime/home`,
  `CODEX_HOME=<spike-root>/runtime/codex-home`,
  `TMPDIR=<spike-root>/runtime/tmp`, a fixed `PATH`, and only the locale, TLS, and
  proxy variables shown to be operationally necessary. Do not source a host shell
  profile or inherit the controller environment wholesale.
- [ ] Save the non-secret environment variable names and values used by the wrapper
  in scratch. Never save authentication values or secret-bearing proxy values in
  the wrapper or its logs; inject any required secret value only at execution time.
- [ ] Leave `$CODEX_HOME/config.toml` absent. Put every spike-specific setting in
  the explicitly selected named profile or an explicit CLI override.
- [ ] Retain every command, exit status, stdout, and stderr under the spike root.
- [ ] Confirm the repository is clean before and after the spike. Do not create or
  modify repository files while running it.

## Task 2: Inventory the installed Codex contract without a provider

- [ ] Capture `codex --version`, `codex exec --help`, and
  `codex sandbox --help` through `commands/run-private.sh`.
- [ ] Run one separately labeled host-context `codex login status` preflight only
  to identify the available authentication method. This is controller inventory,
  not isolation evidence. Do not invoke a model or reuse any other host profile
  state.
- [ ] Record only the authentication method. Do not read, print, copy into the
  report, hash, or otherwise retain credential payloads.
- [ ] Determine whether the active authentication is file-backed or keyring-backed
  without exposing secrets. If `codex login status` does not name the store, check
  only whether the host `auth.json` exists and the configured
  `cli_auth_credentials_store` value; never open `auth.json`. Report
  `INCONCLUSIVE` if those metadata do not determine the store.
- [ ] Confirm support for `--ignore-user-config`, `--ignore-rules`, private
  `CODEX_HOME`, and a restrictive `shell_environment_policy`.
- [ ] Confirm that settings which must remain active with `--ignore-user-config`
  can be supplied as explicit CLI `-c` overrides.

If a required CLI control is demonstrably absent, report `BLOCKED` with the affected
spike question and stop before provider use. If the installed CLI cannot establish
whether the control exists or applies, report `INCONCLUSIVE`.

## Task 3: Qualify the outer discovery boundary deterministically

The **outer discovery boundary** surrounds the complete Codex process. It may read
the recorded executable/runtime dependencies and private runtime, but it must deny
host semantic inputs. Evaluate `codex sandbox` first because it is shipped with the
installed CLI. If it cannot express that boundary, test one minimal macOS Seatbelt
profile. Do not add container work to this spike; record it as a separately approved
alternative if the native approaches fail.

- [ ] Save the exact sandbox command and policy text in scratch.
- [ ] Run a direct command through the candidate boundary that reads
  `workspace/fixture/allowed.txt`; require the exact sentinel and exit zero.
- [ ] Run a direct command through the same boundary that reads
  `outside/denied.txt`; require a filesystem denial and nonzero exit.
- [ ] Run a direct command through the same boundary that reads
  `workspace/outside-link`; require a filesystem denial and nonzero exit.
- [ ] Run a direct command through the same boundary that reads the controlled
  parent `AGENTS.md`; require a filesystem denial and nonzero exit.
- [ ] Enumerate the effective host user-skill, plugin, and host-admin discovery
  root paths without opening file payloads. For each existing root, select one known
  non-secret file and require a direct read through the boundary to fail. For an
  absent root, record the absence and confirm that the policy grants it no explicit
  access.
- [ ] Record exact exit statuses and denial diagnostics.
- [ ] Confirm the policy surrounds the Codex process itself, not only commands that
  Codex may later generate.
- [ ] Before applying the outer boundary, run `codex debug prompt-input` from
  `project/workspace/` through `commands/run-private.sh` as a positive control and
  require the controlled parent `AGENTS.md` sentinel to appear.
- [ ] Run `codex debug prompt-input` through `commands/run-private.sh` and the exact
  outer boundary from the same directory. Require that its model-visible input list
  contains no parent
  `AGENTS.md`, host user skill, plugin, or host-admin input. Classify any unavoidable
  provider-bundled input separately and record the Codex version.

These deterministic probes qualify only the recorded platform, CLI version, and
policy. A prompt-driven canary is not a substitute. If any denied read succeeds or
the debug input contains a forbidden ambient input, report `BLOCKED` for spike
question 2 or 4, as applicable, and do not invoke a provider.

## Task 4: Qualify the inner model-command boundary and authentication

The **inner model-command boundary** is the policy Codex applies to subprocesses
requested by the model. It is distinct from the outer discovery boundary: Codex
itself must be able to use authentication, while model-generated commands must not
be able to read it. If the installed CLI cannot expose or reproduce this exact inner
policy in a provider-free command, report `INCONCLUSIVE`; do not infer it from the
outer-boundary probes.

Create `$CODEX_HOME/spike-isolation.config.toml` as a declared operational input.
It must select a permission profile named `fixture-only` that denies `:root`, reads only
`:minimal` and `:workspace_roots`, and explicitly denies `:tmpdir` and `:slash_tmp`.
It must also set `shell_environment_policy.inherit = "none"`. Retain the exact file
and digest in scratch. Do not pass legacy `--sandbox` settings, because those take
precedence over permission profiles in current Codex.

Provision the private `CODEX_HOME` with one documented method:

- API key: pipe the value on standard input to
  `codex login --with-api-key`;
- access token: pipe the value on standard input to
  `codex login --with-access-token`; or
- file-backed ChatGPT login fallback: copy only `auth.json` to the private
  `CODEX_HOME` with mode `0600`.

Never pass `OPENAI_API_KEY` or `CODEX_ACCESS_TOKEN` to the later
`codex exec` process. Select the scratch profile explicitly with
`--profile spike-isolation --ignore-user-config`. Also pass
`-c 'shell_environment_policy.inherit="none"'` so the security-relevant environment
setting is visible in the retained command rather than relying only on the selected
profile.

- [ ] Run `codex login status` against the private `CODEX_HOME` and retain only
  the method and success/failure.
- [ ] If the active login is keyring-backed and neither documented stdin login
  credential is available, report `BLOCKED` for spike question 1 and stop.
- [ ] Confirm provider-free that
  `codex sandbox --profile spike-isolation --permission-profile fixture-only`
  loads `$CODEX_HOME/spike-isolation.config.toml`. Retain
  `--profile spike-isolation --ignore-user-config` in the later `codex exec`
  command; Task 5 verifies that the provider path applies the selected profile.
- [ ] Prove provider-free configuration recognition by showing that an invalid
  `shell_environment_policy.inherit` value is rejected while `none` is accepted.
  Do not claim this proves runtime application; Task 5 observes that separately.
- [ ] Reproduce the exact named inner permission profile with
  `codex sandbox --profile spike-isolation --permission-profile fixture-only` and
  save the command and policy digest separately from the outer-boundary command and
  digest.
- [ ] Through that direct inner-profile command, read
  `project/workspace/fixture/allowed.txt`; require the exact sentinel and exit zero.
- [ ] Through that direct inner-profile command, attempt reads of
  `outside/denied.txt`, `project/workspace/outside-link`, and the private
  authentication file by exact path; require filesystem denials and nonzero exits.
- [ ] Set a unique, non-secret credential-shaped environment marker in the
  `codex exec` launch environment. Do not place it in the profile's environment
  allowlist; Task 5 will inspect the exact model-command output for its absence.
- [ ] Confirm all created credential files have mode `0600` and the runtime
  directories have mode `0700`.

A copied ChatGPT authentication cache may need to persist refreshed state. The
spike may discard such refreshes, but a later production design must either
re-provision every run or define a safe refresh lifecycle. If model-generated
commands can access any credential material, report `BLOCKED` for spike question 3
and do not invoke a provider.

## Task 5: Run one approved provider integration probe

This task is allowed only if every provider-free gate in Tasks 1-4 passes.

- [ ] Prepare `commands/provider-command.txt`,
  `commands/provider-prompt.txt`, `outputs/provider-stdout.jsonl`,
  `outputs/provider-stderr.txt`, and a draft `report.md` in scratch.
- [ ] Use the proven private runtime, boundary command, discovery opt-outs, and
  explicit restrictive shell environment policy. Apply both the qualified outer
  discovery boundary and the qualified inner model-command policy.
- [ ] Use provider `codex`, model `gpt-5.6-sol`, and effort `high`, unless the
  owner explicitly approves a different exact combination.
- [ ] Ask Codex to read the declared sentinel, attempt the direct and symlinked
  outside reads, attempt the private authentication-file read by exact path without
  printing any content, and print whether the non-secret credential-shaped marker
  is set. Do not ask it to expose real credentials.
- [ ] Present the exact provider, model, effort, and complete command to the owner.
  Do not invoke the provider until that exact command is explicitly approved.
- [ ] Apply the existing `INFRA_RETRY` procedure if the provider attempt has an
  infrastructure-only failure.
- [ ] Inspect the complete JSONL and tool trace. Record observed behavior, including
  any ambient skill or instruction exposure that the trace makes visible.
- [ ] Require the trace to show the exact probe commands, the declared sentinel,
  filesystem denials for the forbidden paths, and an absent environment marker. If
  the model changes or omits a probe, report `INCONCLUSIVE`; if a forbidden read or
  marker succeeds, report `BLOCKED` for spike question 3 or 4.

The provider result corroborates integration only. Model self-report and a clean
trace do not replace the deterministic boundary probes.

## Task 6: Classify and report the spike

Use one outcome:

- `FEASIBLE`: all four spike questions were answered yes and the approved
  integration probe behaved consistently with both qualified boundaries.
- `BLOCKED`: at least one spike question was answered no. Identify each failed
  question and retain the passing evidence; do not invent a more granular status.
- `INCONCLUSIVE`: no question was answered no, but tooling or evidence could not
  answer at least one question. Identify every unanswered question.

The report must include:

- exact platform and Codex version;
- authentication mechanism, never a secret or host credential path;
- exact non-secret commands and exit statuses;
- separate outer- and inner-boundary policies and digests;
- deterministic probe evidence;
- provider command approval and attempt count, if reached;
- integration observations; and
- the outcome with unresolved questions.

Present `report.md` to the owner. Keep it and all evidence in scratch. Do not
promote it to `accepted/`.

- [ ] After recording the report, delete the private runtime and verify deletion.
  Preserve the credential-free commands, outputs, and report elsewhere in the
  scratch root.

## Post-spike decision gate

Do not begin production implementation automatically.

- If the owner accepts `FEASIBLE`, write a Codex-only design amendment and a
  separate test-driven implementation plan. Let the methodology define comparison
  eligibility before changing the result schema or runner statuses.
- If the outcome is `BLOCKED`, propose only the smallest follow-up investigation
  for each failed question. Partial profile isolation is insufficient for strict
  fixture-only edit or A/B testing. A container or another platform boundary
  requires separate owner approval.
- If the outcome is `INCONCLUSIVE`, preserve the scratch evidence and defer the
  design.

A later production design should keep these concepts separate:

1. the requested policy identifier and Codex version;
2. whether that policy was mechanically applied;
3. whether its exact platform/version/policy combination was independently
   qualified; and
4. whether the run transcript was `CLEAN`, `VIOLATION`, or `UNAVAILABLE`.

Comparison eligibility is derived from those facts. `CLEAN` must never be treated
as proof of enforcement, and this spike does not pre-commit the eventual schema or
status names.

## Completion criteria

This deferred plan is complete when:

- the scratch spike answers each spike question or records a precise blocker;
- direct allowed, forbidden, and symlink-escape probes have exact evidence;
- authentication is provisioned through a documented private-runtime flow;
- deterministic inner-profile probes deny the tested authentication file and
  forbidden ambient sentinels, and the integration trace shows that the non-secret
  environment marker is absent;
- any provider invocation occurred only after approval of its exact command;
- the report makes claims only for the tested platform, Codex version, auth
  mechanism, and policy;
- the owner has reviewed the scratch report; and
- no runner, scenario, methodology, skill, or `accepted/` file changed.
