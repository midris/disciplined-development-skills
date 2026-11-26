# Purpose

Keep detailed project-file prose in scope despite an accompanying brief response.

# Inputs

Prompt is the canonical `CW-18` input from `skill-validation/concise-writing.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only to prefix the three description paths and concise-writing path with `{{fixture_dir}}/`. Rubric is the canonical evaluator-withheld `CW-18` rubric from the same source. Inputs: `package-owned adversarial-review-loop frontmatter description` -> `{{fixture_dir}}/descriptions/adversarial-review-loop.txt`; `package-owned concise-writing frontmatter description` -> `{{fixture_dir}}/descriptions/concise-writing.txt`; `package-owned Superpowers 6.3.0 writing-skills frontmatter description` -> `{{fixture_dir}}/descriptions/superpowers-writing-skills.txt`; `live skills/concise-writing/SKILL.md` -> `{{fixture_dir}}/skills/concise-writing/SKILL.md`.

# Smoke

No schema `"0.2"` result is retained.
