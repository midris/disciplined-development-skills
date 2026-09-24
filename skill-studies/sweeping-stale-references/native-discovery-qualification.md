# SSR native discovery qualification

Status: scripted Codex catalog/capture qualification complete. Subsequent production-model selection is measured separately in the [comparison assessment](comprehensive-comparison-02-assessment.md); this record preserves the zero-model mechanism check.
Date: 2026-09-23 America/New_York (retained timestamps are 2026-09-24 UTC).
Runner revision: `7cec98a`; installed Codex CLI: `0.156.0`, binary SHA-256 `6b42db4d33fd53516162bd76a0e2d07e0567287c44e036d4e4c06cb555a432f9`.
This runtime must not be silently pooled with historical Codex 0.154.0 observations.

## Codex mechanism check

Both original and comprehensive candidate used actual draft invocation-change inputs, runtime preparation and argument generation, including strict configuration, ignored user configuration/rules, private profile, filesystem isolation and corrected login-shell setup.
Only authentication preflight and transport were substituted: surrogate auth, a localhost scripted Responses endpoint, disabled request compression/telemetry and no external model inference.
The endpoint requested a fixed skill read and then returned a fixed completion; it did not choose whether SSR applied.

Both initial requests contained SSR's complete description and an aliased load path resolving to the supplied skill.
Neither initial request contained the full body.
Both scripted reads delivered the complete supplied body, and retained session events matched the catalog and full read.
Original SHA-256: `d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157`.
Candidate SHA-256: `15992341f7ab2fb1e4d8a775092199d7d4e6a9de1167895dbe5a805aeafbd38c`.
No provider-adapter behavior change was necessary for discovery.

The native catalog also lists five built-in skills: imagegen, openai-docs, plugin-creator, skill-creator and skill-installer.
SSR is the sole supplied project skill, not the sole catalog entry.
The qualification establishes SSR readability only; it does not establish access to every built-in body or behavior if a subject selects another skill.
Inspect the actual catalog and trace in each collected invocation; unexpected context, unreadable SSR, missing capture or changed CLI identity stops collection for inspection.
The localhost substitution does not establish production-model behavior, authentication or automatic selection reliability.

Evidence and reproducible diagnostic: `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/development/native-discovery-20260923/`.
Sibling inventory SHA-256: `4b237ad871dfaaf9a4720e3d01b3d7a31c7f06c1655c34d392cfbd43ceebb335`.
Raw evidence stays external; zero model calls were charged.

## Claude documentation cross-check

Official documentation describes project skills under `.claude/skills`, description-led automatic selection, and body loading on invocation.
`disable-model-invocation: true` blocks automatic use; neither SSR version sets it.
Descriptions can be shortened by the catalog budget, so verify delivered text rather than infer availability from files.
See [Claude skills](https://code.claude.com/docs/en/skills).

The CLI exposes setting-source selection, Skill tool controls, and a flag that disables all skills.
Our adapter uses project settings, enables/allows Skill and does not disable skills; strict MCP configuration governs MCP, not proof of skill isolation.
See [Claude CLI reference](https://code.claude.com/docs/en/cli-reference).

The installed Claude CLI reports `2.1.280`; the website describes evolving behavior and is not installed-runtime evidence.
Current SSR drafts place skills under `.agents/skills`, so they are Codex configurations and must not be relabeled Claude runs.
A Claude comparison requires `.claude/skills` materialization, model/effort selection, native catalog and Skill-event capture qualification, plus its own allocation.
Before any Claude subject pass, add and pass an installed-policy assertion of Python and Git resolution through the actual Bash shell invocation.
This remains unimplemented: the Codex login-shell test covers Codex only, and the shared isolation probe invokes Python by absolute path.
The completed comparison is Codex-only; Claude subject collection is blocked until its own shell check passes.
Claude documentation checking does not authorize or qualify additional Claude model runs.
