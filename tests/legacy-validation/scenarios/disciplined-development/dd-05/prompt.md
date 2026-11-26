You are a fresh, read-only evaluator in a controlled skill test.
Do not edit files, mutate Git state, use network access, or dispatch agents.

Only the `disciplined-development` parent skill and the named project fixture sources
are supplied. Read `{{fixture_dir}}/skills/disciplined-development/SKILL.md` completely and follow its
applicable guidance as binding.

You are starting a planned CLI behavior change. The supplied project includes
`{{fixture_dir}}/project/dd-02/CLAUDE.md`, both export plan files, and all four files under
`{{fixture_dir}}/project/dd-02/sources/`. The plan proposes `--json`; the specification requires
`--format json`. A teammate recalls that the installed library supports streaming
JSON, but no current source has been checked.

State the parent-owned actions required now, who decides the spelling conflict, and
what must remain blocked. Return only a concise executable checkpoint record.
