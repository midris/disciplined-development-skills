# Expanded CW runtime qualification

Qualification date: 2026-09-27.
Authority and collection progress belong to the [protocol](../protocol.md).
No model inference was used for these checks.
The runner tree is the one committed at `52c3129`; the collection authority commit records its full revision.

| Component | Qualified installed identity | SHA-256 |
| --- | --- | --- |
| Codex | `/opt/homebrew/Caskroom/codex/0.157.1/bin/codex`, CLI 0.157.1 | `27ceb5f9b957b43a519efe4eaa3816a0bffb0a531a2c89af18840c0a3c016a7d` |
| Claude | `/opt/homebrew/Caskroom/claude-code@latest/2.1.283/claude`, CLI 2.1.283 | `d8cb1e5c79684cc12a8bfc813e3a2073406921b6245744b3009be3ab5651d21e` |
| Python | Homebrew Python 3.14.7 | `87d4df53fd91304be5bac391fb204643c36b7df2023c04a0953bcbc7d4fdf634` |
| Git | Homebrew Git 2.55.0 | `9048038886ac36210fbb616b49b0707465f63683cb04e33a2013baf95f746938` |

Thirteen installed-policy tests passed: both providers' input isolation and read-only mutation controls, Codex Git/write/network checks, login-shell Python/Git resolution and heredocs, and Claude actual-CLI shell and generic Skill delivery in both permission modes.
Two additional actual-Claude checks supplied the original and comprehensive CW snapshots through its native Skill tool.
Two Codex scripted checks used the exact native N1 configurations and captured full skill reads.
All four CW delivery checks established the complete description in the initial request, absence of the full body initially, and complete body delivery afterward.
The Codex retained sessions also preserve the catalog and read results.
Its catalog includes five built-ins alongside CW: imagegen, openai-docs, plugin-creator, skill-creator and skill-installer.
Claude's initial catalog contains the supplied CW description; inspect every collected trace for unexpected additional guidance.
Scripted endpoints establish availability and capture, not automatic selection.

Two initial Codex diagnostic attempts stopped before invocation because the adapted diagnostic placed its fixture under shared `/private/tmp`.
The production runtime correctly rejected that location.
The successful checks used the required per-user temporary root; collection must likewise use the operating system's per-user temporary directory, without a shared-TMPDIR override.
Those failed diagnostics remain in the retained evidence and cost zero model calls.

Evidence: `/Users/simon/work/personal/skill-study-private/concise-writing/development/expanded-preflight-20260927/`.
Sibling inventory SHA-256: `a53b9a83cb012db6880816013e622f4eef3f1a27a48680abe383e127e0b7e3f4`, covering 568 entries.
The evidence includes executable identities, policies, captured scripted requests/results and reproducible diagnostic scripts.
The existing owner-accepted single-host storage arrangement applies.
Never run Git inside retained bundles; inspect files read-only or use disposable copies.

## Collection controls

Request Codex `gpt-5.6-sol` and Claude `claude-sonnet-5`, both low effort, workspace-write, with the existing 900-second timeout.
The first scheduled charged attempt on each provider confirms production model availability; scripted responses do not prove it.
Check requested and reported model/effort identity, actual CLI hash, setup and capture before proceeding.
Stop on an unavailable model, unexpected identity, contamination, input drift, uncertain charge or failed preservation; do not substitute a model or retry automatically.
Include valid behavioral failures, including qualified native misses.
No historical runtime counts are pooled into these batches.

Use the [ordered schedule](schedule.json) and matching protocol tables.
Each call runs in a fresh context; preserve and verify its stopped bundle and register its charge before dispatching another.
For explicit-load skill conditions, complete CW body exposure must precede the first task edit.
For native conditions, score full-body load timing separately from the artifact; a missed or late load is an observation, not a setup exclusion.
For controls, inspect captured guidance for unexpected CW exposure.
Apply the [frozen policy copy](assessment-policy.txt) and case-specific criteria, retaining full artifacts and trace evidence for active-session judgment.
