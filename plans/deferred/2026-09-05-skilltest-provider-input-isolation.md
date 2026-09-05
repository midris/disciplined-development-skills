# Skilltest Provider Input Isolation Implementation Plan

**Status:** Deferred until the current-skill baseline campaign is complete. This
plan records a post-baseline implementation boundary; it does not authorize runner
changes, provider invocations, or changes to existing accepted evidence.

> **Execution:** Use `superpowers:executing-plans` when this plan is activated.
> Keep its test-first checkpoints and obtain the owner's approval for every real
> provider command before invoking it.

**Goal:** Make skill-effectiveness runs attributable to declared scenario inputs by
preventing automatic discovery of host user configuration, rules, plugins, and
skills; detect any remaining outside-workspace reads; and refuse comparison use
when the input-isolation contract is violated.

**Architecture:** Give each provider invocation a private, short-lived runtime home
outside the retained run bundle. Launch Codex with a minimal allowlisted environment,
an isolated `HOME` and `CODEX_HOME`, and its supported user-config and rules opt-outs.
Pass authentication into that runtime without retaining credentials. Treat the
provider's filesystem sandbox as the enforcement boundary and transcript inspection
as defense-in-depth evidence, not proof of containment. If the existing Codex
workspace sandbox cannot deny an explicit outside-root read, stop after the
lightweight isolation work and select an external OS/container boundary before
claiming strict fixture-only execution.

**Tech stack:** Python 3.11, `subprocess`, `tempfile`, `pathlib`, pytest,
JSON Schema draft 2020-12, Codex CLI.

## Why this is deferred

The baseline campaign is currently teaching us how to audit scenarios and apply the
scoring methodology. Changing the provider boundary during that campaign would
change the approved execution policy and runner result contract. Under the
[baseline-set lifecycle](../specs/2026-09-03-skill-validation-baseline-design.md#accepted-baseline-set-lifecycle),
those changes create a new comparison key and make existing accepted sets stale for
the new campaign.

Finish the current campaign first. Its accepted records remain valid historical
evidence for the inputs and runner contract under which they were collected; do not
rewrite their worksheets or retroactively relabel their verdicts. Before any
current-skill versus rewritten-skill comparison, activate this plan and collect both
arms under the same isolated runner contract.

## Observed defect and contract

Today the Codex adapter passes `env=None` to `subprocess.Popen`, so the child inherits
the controller's complete environment. The provider runs in a prepared temporary
workspace, but Codex can still discover user-level skills and plugins through the
inherited home/profile. During baseline testing it read the installed
`using-superpowers/SKILL.md`, which was not a declared scenario fixture.

For the current campaign, disclose such a read as a task/fixture-fidelity failure.
It may remain a judgeable qualified result when it does not prevent semantic or
protocol judgment, following the existing
[verdict order](../completed/specs/2026-09-02-skill-testing-methodology-design.md#scenario-verdict).
That accommodation ends before edit or A/B effectiveness testing.

The post-baseline input contract is:

- **Declared semantic inputs:** retained prompt template, rendered prompt, and
  declared fixture copies.
- **Withheld evaluation input:** the rubric, which remains unavailable to the
  subject provider.
- **Declared operational inputs:** executable and version, model, effort, fixed
  adapter flags, network/service access, minimal locale/TLS/proxy variables, and
  authentication material.
- **Forbidden ambient inputs:** host project instructions, user configuration,
  rules, memories, MCP configuration, plugins, user-installed skills, and files not
  declared by the scenario.
- **Bundled provider behavior:** provider-owned built-ins that cannot be disabled
  are part of the pinned runtime contract, not scenario fixtures. Record the Codex
  version so a provider upgrade changes the comparison key.

Official Codex documentation supports the proposed boundary: Codex discovers skills
from repository, user, admin, system, and plugin locations
([skills documentation](https://developers.openai.com/codex/skills)); `codex exec`
provides `--ignore-user-config` and `--ignore-rules`; and cached credentials may live
in `CODEX_HOME/auth.json` or an OS credential store
([authentication documentation](https://developers.openai.com/codex/auth)). The
normal `workspace-write` sandbox limits writes but is not, by itself, evidence that
all outside-workspace reads are denied
([agent approvals and security](https://learn.chatgpt.com/codex/agent-approvals-security)).

## Activation gate

Do not begin implementation until all of these are true:

- [ ] All current-skill catalogs and the suite-composition catalog have completed
  the baseline campaign.
- [ ] The owner explicitly activates this plan as a new implementation boundary.
- [ ] The owner agrees that isolated runs start a new comparison campaign and that
  current and rewritten arms must use the same runner version and isolation policy.

## Task 1: Lock the isolation and authentication design with failing tests

**Files:**

- Modify: `skill-validation/runner/tests/test_providers.py`
- Modify: `skill-validation/runner/tests/test_run.py`
- Modify: `skill-validation/runner/tests/conftest.py`
- Test: `skill-validation/runner/tests/test_providers.py`

- [ ] Add a provider-boundary test proving Codex receives an explicit environment
  instead of inherited `os.environ`.
- [ ] Assert that an arbitrary host marker, host `HOME`, and host `CODEX_HOME` do not
  reach the provider, while the executable path and approved operational variables
  do.
- [ ] Assert that the Codex invocation contains `--ignore-user-config` and
  `--ignore-rules` after `exec`.
- [ ] Add an end-to-end test proving the runtime home is outside the retained run
  directory and no runtime profile or credential file appears in the artifact
  inventory.
- [ ] Add failure-path tests proving the runtime directory is removed after success,
  launch failure, timeout, nonzero exit, and artifact-write failure.
- [ ] Keep fake-provider controls test-only: inject them through a monkeypatched
  environment builder rather than adding `SKILLTEST_*` variables to the production
  allowlist.

Run:

```bash
cd skill-validation/runner
uv run pytest tests/test_providers.py tests/test_run.py -q
```

Expected: the new tests fail because Codex still inherits the host environment and
has no private runtime home or cleanup lifecycle.

## Task 2: Implement the private runtime home and minimal environment

**Files:**

- Modify: `skill-validation/runner/src/skilltest/providers.py`
- Modify: `skill-validation/runner/src/skilltest/runner.py`
- Modify: `skill-validation/runner/src/skilltest/workspace.py`
- Modify: `skill-validation/runner/tests/test_providers.py`
- Modify: `skill-validation/runner/tests/test_run.py`

- [ ] Add a provider-runtime context that allocates a mode-`0700` temporary
  directory outside `RunContext.run_dir` and removes it in a `finally` path.
- [ ] Set both `HOME` and `CODEX_HOME` to directories inside that private runtime.
  Do not place `.agents`, `skills`, `plugins`, `.codex/config.toml`, hooks, rules, or
  memories there.
- [ ] Build the child environment from an explicit operational allowlist. Start with
  `PATH`, `TMPDIR`, locale variables, `CODEX_CA_CERTIFICATE`/`SSL_CERT_FILE`, and the
  proxy variables required by the host. Add no variable merely because it exists in
  the controller environment.
- [ ] Preserve the existing fixed Claude baseline, but apply the same private-home
  and allowlist principles to Claude or document and test a provider-specific reason
  for any difference. The result contract must identify the actual isolation mode.
- [ ] Add `--ignore-user-config` and `--ignore-rules` to the fixed Codex adapter
  arguments. Do not claim that these flags alone disable skill discovery.
- [ ] Make runtime preparation failure return `PREPARATION_FAILED` without invoking
  the provider.

Run:

```bash
cd skill-validation/runner
uv run pytest tests/test_providers.py tests/test_run.py -q
```

Expected: all provider and orchestration tests pass, including cleanup on every
terminal path.

## Task 3: Stage authentication without retaining credentials

**Files:**

- Modify: `skill-validation/runner/src/skilltest/providers.py`
- Modify: `skill-validation/runner/src/skilltest/runner.py`
- Modify: `skill-validation/runner/tests/test_providers.py`
- Modify: `skill-validation/runner/tests/test_run.py`
- Modify: `skill-validation/runner/README.md`

- [ ] At activation time, run `codex login status` as a read-only preflight and
  record only the authentication method, never a token or credential payload.
- [ ] Support environment-controlled automation credentials first: pass through
  `OPENAI_API_KEY` or `CODEX_ACCESS_TOKEN` only when already present and selected by
  the operator. Never log, hash, or serialize its value.
- [ ] For an existing ChatGPT login backed by `CODEX_HOME/auth.json`, copy only that
  file into the private `CODEX_HOME` with mode `0600`. Do not copy the rest of the
  host Codex directory. Delete the private copy with the runtime directory in the
  guaranteed cleanup path.
- [ ] If the active login is keyring-backed and cannot be used with the isolated
  home, stop with `PREPARATION_FAILED` and an actionable message. Do not silently
  fall back to the host profile. The operator may deliberately choose API-key,
  access-token, or file-backed authentication before retrying.
- [ ] Test that error text and every retained artifact are secret-free using sentinel
  credential values.

Run:

```bash
cd skill-validation/runner
uv run pytest tests/test_providers.py tests/test_run.py -q
```

Expected: authentication is available inside the temporary profile, credentials are
absent from the retained bundle and diagnostics, and unsupported auth storage fails
closed before provider invocation.

## Task 4: Add an auditable isolation result contract

**Files:**

- Modify: `skill-validation/runner/result.schema.json`
- Modify: `skill-validation/runner/src/skilltest/results.py`
- Modify: `skill-validation/runner/src/skilltest/runner.py`
- Modify: `skill-validation/runner/tests/test_results.py`
- Modify: `skill-validation/runner/tests/test_run.py`
- Modify: `skill-validation/runner/README.md`

- [ ] Bump the result schema from `0.2` to `0.3`.
- [ ] Add an `input_isolation` record containing the fixed policy identifier,
  runtime kind, provider version, and status: `ENFORCED`, `VIOLATED`, or
  `NOT_VERIFIED`.
- [ ] Record only non-secret metadata. Runtime-home paths and credential-source paths
  must not be retained because they disclose host structure and are not stable
  comparison inputs.
- [ ] Parse Codex JSONL only enough to identify explicit filesystem operations and
  normalize their resolved paths. Mark an observed read outside the prepared
  workspace `VIOLATED`. Treat incomplete or unparseable telemetry as
  `NOT_VERIFIED`, never as `ENFORCED`.
- [ ] Make `VIOLATED` and `NOT_VERIFIED` mechanically completed runs that are
  ineligible for scoring or promotion, rather than provider infrastructure errors.
  The methodology update in Task 6 will name their disposition.
- [ ] Update schema fixtures and exact-record tests for all terminal states.

Run:

```bash
cd skill-validation/runner
uv run pytest tests/test_results.py tests/test_run.py -q
```

Expected: schema `0.3` accepts all tested records, rejects missing or contradictory
isolation fields, and no transcript parser outcome is overstated as enforcement.

## Task 5: Prove whether the boundary actually denies outside reads

**Files:**

- Add: `skill-validation/runner/acceptance/fixtures/provider-isolation/fixture/allowed.txt`
- Add: `skill-validation/runner/acceptance/fixtures/provider-isolation/prompt.md`
- Add: `skill-validation/runner/acceptance/fixtures/provider-isolation/codex.json`
- Add: `skill-validation/runner/acceptance/test_provider_input_isolation.py`
- Modify: `skill-validation/runner/README.md`

- [ ] Add an offline acceptance check that prepares the canary package without
  invoking a provider.
- [ ] Make the real canary request two reads: the declared `allowed.txt` and one
  sentinel file outside the prepared workspace whose content is unique but not
  sensitive. Create the sentinel in a namespaced scratch directory immediately
  before the approved run.
- [ ] Present the exact provider, model, effort, and `skilltest run` command for owner
  approval. Do not invoke Codex before that approval.
- [ ] Inspect the bundle and classify the result:
  - the declared read succeeds and the outside read is denied: the runtime may be
    marked `ENFORCED` for that tested platform and Codex version;
  - the outside read succeeds: keep the bundle scratch-only, mark the lightweight
    boundary insufficient, and proceed to the external-boundary decision below;
  - telemetry cannot establish the attempted/read path: mark `NOT_VERIFIED` and do
    not use the runner for comparisons.

Run before the provider approval gate:

```bash
cd skill-validation/runner
uv run pytest acceptance/test_provider_input_isolation.py -q
```

Expected: provider-free preparation passes. The real canary has no expected result
until the owner approves and the tested runtime supplies evidence.

### External-boundary decision

If Codex can read the sentinel outside the workspace, do not add more prompt wording
or treat transcript scanning as containment. Choose one host-supported boundary that
mounts only the prepared workspace plus the minimum executable/runtime libraries and
injects authentication ephemerally:

1. a disposable container when the provider CLI and authentication can run there; or
2. an OS-level sandbox profile maintained and tested for each supported platform.

Implement only the selected boundary, rerun the same negative canary, and do not mark
the policy `ENFORCED` until the outside read is denied. If neither boundary is
maintainable, document that the runner cannot offer strict fixture-only comparisons
and keep edit/A/B testing blocked.

## Task 6: Align methodology, lifecycle, and operator documentation

**Files:**

- Modify: `skill-validation/runner/README.md`
- Modify: `plans/completed/specs/2026-09-02-skill-testing-methodology-design.md`
- Modify: `plans/specs/2026-09-03-skill-validation-baseline-design.md`
- Modify: `skill-validation/scenarios/README.md`

- [ ] Define declared semantic inputs, declared operational inputs, forbidden
  ambient inputs, and bundled provider behavior in the runner contract.
- [ ] Add isolation policy identifier and provider version to the stable comparison
  key. State that pre-isolation accepted evidence remains historical but is not an
  arm in the new isolated comparison campaign.
- [ ] Add a verdict disposition named `INPUT_ISOLATION_INVALID`: scratch-only,
  unscored, and used when a mechanically completed run is `VIOLATED` or
  `NOT_VERIFIED`. Keep it separate from `INFRA_RETRY` and from scenario defects.
- [ ] Require the worksheet to show isolation status and policy identifier before
  scoring begins; update worksheet generation and its tests if this changes the
  mechanical worksheet contract.
- [ ] Document credential handling, cleanup guarantees, the canary, and the existing
  exact-command owner-approval gate.
- [ ] State explicitly that scenario prompts do not establish containment. Audit
  prompt/rubric wording individually during later scenario work rather than applying
  a bulk prompt rewrite here.

## Task 7: Verify the new campaign boundary

**Files:**

- Test: `skill-validation/runner/tests/`
- Test: `skill-validation/runner/acceptance/`
- Verify: repository Markdown and link checks

- [ ] Run the complete runner suite:

```bash
cd skill-validation/runner
uv run pytest -q
```

- [ ] Run all provider-free acceptance checks:

```bash
cd skill-validation/runner
uv run pytest acceptance -q
```

- [ ] From the repository root, run the repository's documented Markdown and link
  checks.
- [ ] Run `git diff --check` and inspect the complete diff for credential values,
  absolute runtime paths, accidental accepted-evidence edits, and unrelated changes.
- [ ] Present the implementation and provider-free verification to the owner.
- [ ] Only after a separately approved exact command, run the negative isolation
  canary once. Do not run a skill scenario until the canary is `ENFORCED`.
- [ ] Start a new isolated comparison campaign. Never compare a rewritten-skill run
  to a current-skill run produced under schema `0.2` or another isolation policy.

## Completion criteria

This plan is complete only when:

- provider processes do not inherit user/project/plugin discovery state;
- credentials are usable but never retained or disclosed;
- an explicit outside-workspace read is denied by the tested execution boundary;
- every completed result states the provider version and isolation policy/status;
- isolation violations are scratch-only and cannot be scored or promoted;
- tests cover success and every cleanup/failure path;
- operator and methodology documents agree on the new comparison key; and
- a real provider is invoked only after approval of its exact command.
