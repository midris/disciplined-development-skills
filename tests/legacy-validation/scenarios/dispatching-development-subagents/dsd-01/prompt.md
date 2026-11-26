You are a fresh, read-only evaluator in a controlled skill test.
Do not edit or create files, mutate Git state, use network access, or dispatch agents.
The complete composition bundle is available.
Invoke `dispatching-development-subagents` directly.
Read `{{fixture_dir}}/skills/dispatching-development-subagents/SKILL.md` and `{{fixture_dir}}/skills/disciplined-development/SKILL.md` completely, load every applicable supplied parent companion, and follow all applicable guidance as binding.

The supplied project includes `{{fixture_dir}}/project/dsd-01/AGENTS.md`,
`{{fixture_dir}}/project/dsd-01/plans/pagination.md`, and
`{{fixture_dir}}/project/dsd-01/reviews/pagination.md`.

You are the orchestrator preparing one development-subagent dispatch for this reviewer finding:

`[P2] src/pagination.py:74 — calculate_pages drops the final page when total_items is an exact multiple of page_size.`

The requested implementation is a focused fix in `src/pagination.py` plus a regression test in `tests/test_pagination.py`.
Before work, the subagent must re-read `AGENTS.md` and `plans/pagination.md`.
The public function signature and dependency set are locked.
The governing files impose no additional out-of-scope policy beyond the supplied skills.
The upstream execution skill is installed, but its report headings, status vocabulary, and report-file shape are not stable or supplied.

Return only the exact prompt you would send to the implementation subagent.
Do not dispatch it.
