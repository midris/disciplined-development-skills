# Purpose

Apply the skill-authoring lens while retaining the holistic baseline.

# Inputs

- Prompt: canonical `skill-validation/fixtures/adversarial-review/prompts/ar-14.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only by adding the planned fixture-rooted base-skill and project skill paths; retained SHA-256 `02531c56c34ec74e7148730ab81388aba27cbc4d7a68d4a8577d8ac9c83c3539`.
- Rubric: exact canonical `skill-validation/fixtures/adversarial-review/rubrics/ar-14.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `3dd645611692344bd7f8a79e57b036a47eb4b658a69624ae413090bd3193827a` and withheld from provider inputs.
- Live skills: `../../../../skills/adversarial-review/SKILL.md` → `skills/adversarial-review/SKILL.md`.
- Pinned Superpowers dependencies: exact files from tag `v6.2.0`; each source `skills/<path>` is packaged as `fixture/skills/superpowers/<path>` and supplied as `skills/superpowers/<path>`:
  - `skills/requesting-code-review/SKILL.md` — SHA-256 `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8`
  - `skills/requesting-code-review/code-reviewer.md` — SHA-256 `b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3`
  - `skills/test-driven-development/SKILL.md` — SHA-256 `bf1b8216e523851a411e91d429a7c1c2a173e79d88957bc78e348218d50edd54`
  - `skills/using-superpowers/references/codex-tools.md` — SHA-256 `d3f113a8ebbd748e8ba847b09b57b7685442775ca4ee194d693ce3663f8fac68`
  - `skills/writing-skills/SKILL.md` — SHA-256 `d34db5c8aed6a4e0440132bd0613aace70a693ec7819d5637ad77481d8e10d1b`
  - `skills/writing-skills/anthropic-best-practices.md` — SHA-256 `217629b356c09c9bd11017c9788e8fc654ca1b32c92d4a51cd490e16dd65e59a`
  - `skills/writing-skills/examples/CLAUDE_MD_TESTING.md` — SHA-256 `0b379a3415e185d3c434b3ad283d8aa132f3022c2a4f210f168865b5986bcef0`
  - `skills/writing-skills/graphviz-conventions.dot` — SHA-256 `e2890a593c91370e384b42f2f67b1a6232c9e69dddea7891a0c1c46d7b20b694`
  - `skills/writing-skills/persuasion-principles.md` — SHA-256 `a51bc9bf75189ea73a27b3fb504a2fdfdb966fb1f7f1cdf03203230a216ccc03`
  - `skills/writing-skills/render-graphs.js` — SHA-256 `ccda971a87bb185f8febf81c56b556a20d026fa980c17b35fa3e8824fbb37852`
  - `skills/writing-skills/testing-skills-with-subagents.md` — SHA-256 `c711346852c911b24a84aa161e0cff06a4cd7f4e2fa9e9c0a266cead5afcbade`
- Scenario files: exact canonical files from `skill-validation/fixtures/adversarial-review/ar-14/` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged beneath `fixture/` and supplied at the matching path:
  - `project/SKILL.md` — SHA-256 `2a51181ec6e1f7f990bcd04e78f2459a88922ceaa121446c1e1b9696966c061b`

# Smoke

No schema `0.2` result is retained.
