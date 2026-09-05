# Purpose

Report unchecked encoding failure as caller-visible termination requiring a typed failure path.

# Inputs

- Prompt: canonical `skill-validation/fixtures/adversarial-review/prompts/ar-16.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only by adding the planned fixture-rooted base-skill and `project/` paths; retained SHA-256 `1513a66015109f998e8ca2bd5c0f92aa1b09f9791ec9b40abd87b71dc18d9c17`.
- Rubric: exact canonical `skill-validation/fixtures/adversarial-review/rubrics/ar-16.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `53f9a6581424dbde7b29c0975adea621b71696707e22ce0d08c30bfb67128a23` and withheld from provider inputs.
- Live skills: `../../../../skills/adversarial-review/SKILL.md` → `skills/adversarial-review/SKILL.md`.
- Pinned Superpowers dependencies: exact files from tag `v6.2.0`; each source `skills/<path>` is packaged as `fixture/skills/superpowers/<path>` and supplied as `skills/superpowers/<path>`:
  - `skills/requesting-code-review/SKILL.md` — SHA-256 `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8`
  - `skills/requesting-code-review/code-reviewer.md` — SHA-256 `b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3`
- Scenario files: exact canonical files from `skill-validation/fixtures/adversarial-review/ar-16/` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged beneath `fixture/` and supplied at the matching path:
  - `project/EventLog.swift` — SHA-256 `025c48a43595883ae06929affaccddd57f9df2b45f5fa56e409ac61c99cd9e09`
  - `project/contract.md` — SHA-256 `c5d2479b1b24c120da384a16afb12d8628fd8fec93c9c626f91fc24049949202`

# Smoke

No schema `0.2` result is retained.

# Accepted baseline

The latest accepted baseline is a `FAIL` from `codex` / `gpt-5.6-sol` / `high`, accepted on 2026-09-05.
The response correctly reports the unchecked runtime encoding failure, rejects the static-type rationale, and blocks on the missing typed caller path.
The overall result fails because the rubric explicitly forbids outside-root inspection while the provider read installed `using-superpowers/SKILL.md` and `using-superpowers/references/codex-tools.md` outside the declared fixture inventory.
The provider-facing prompt does not state that isolation restriction as explicitly as AR-13 and AR-14, which is retained as a scenario-design observation.
No authenticated deterministic `DD-PATTERN` checker was available; exact marker syntax was not scored.

Retained artifacts: `accepted/worksheet.md`, `accepted/result.json`, and `accepted/final.txt`.
No evidence files were emitted.
