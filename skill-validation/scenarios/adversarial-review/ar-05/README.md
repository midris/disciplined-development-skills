# Purpose

Apply broad durability and holistic review without requiring one predetermined valid defect selection.

# Inputs

- Prompt: canonical `skill-validation/fixtures/adversarial-review/prompts/ar-05.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only by adding the planned fixture-rooted base-skill and `subject/` paths; retained SHA-256 `0f62c02acd47bf781d762420897a9a6a14ab7a94026494dfbed71cce9de1be41`.
- Rubric: exact canonical `skill-validation/fixtures/adversarial-review/rubrics/ar-05.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `2dd2372981b9b88eff3567ce5e1c6b5b3b8c7999285400c79ab1711fe6bbfa94` and withheld from provider inputs.
- Live skills: `../../../../skills/adversarial-review/SKILL.md` → `skills/adversarial-review/SKILL.md`.
- Pinned Superpowers dependencies: exact files from tag `v6.2.0`; each source `skills/<path>` is packaged as `fixture/skills/superpowers/<path>` and supplied as `skills/superpowers/<path>`:
  - `skills/requesting-code-review/SKILL.md` — SHA-256 `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8`
  - `skills/requesting-code-review/code-reviewer.md` — SHA-256 `b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3`
- Scenario files: exact files from `/Users/simon/work/coronis/code/meeting-pipeline` at commit `b0f4511b2d43a566acdcbc5f0d61db6342a4c882`, packaged beneath `fixture/subject/` and supplied beneath `subject/`:
  - `plans/2026-06-18-recording-slice.md` — SHA-256 `1d10c2845101df73f4418c7a4db147a79d53335a6f08f5bec822073e2e180c40`
  - `swift/Steno/Sources/Steno/Events/EventEnvelope.swift` — SHA-256 `42cd5c2df5a1dadb34df0e15cafa6e36f76588661e1cb99f93f83e158488800b`
  - `swift/Steno/Sources/Steno/Events/EventLog.swift` — SHA-256 `26b7accda8f8115ef23249243512384413fb198ab702961f65a3103f0f090aa0`
  - `swift/Steno/Tests/StenoTests/EventLogTests.swift` — SHA-256 `65134b891cd8ee803c1367518ea7c3b832fca4a862fa411ed848146d656a4b52`

# Smoke

No schema `0.2` result is retained.
