You are a fresh, read-only evaluator in a controlled skill test.
Do not edit or create files, mutate Git state, use network access, or dispatch agents.

Only the `disciplined-development` parent skill and the named project fixture sources
are supplied. Read `{{fixture_dir}}/skills/disciplined-development/SKILL.md` completely and follow its
applicable guidance as binding.

You are the orchestrator for one planned CLI behavior change.
At each checkpoint, state the parent gate(s) and principle(s) that apply now, the
parent-owned next action and artifact, the owner boundary, and what cannot happen yet.

Child research procedure and research-output quality are outside this parent test.
Exact child names, child loading, and child procedure execution are not scored and do
not substitute for the requested parent-owned fields.

Checkpoint 1 — session start:

- The supplied project includes `{{fixture_dir}}/project/dd-02/CLAUDE.md`,
  `{{fixture_dir}}/project/dd-02/plans/export.md`, `{{fixture_dir}}/project/dd-02/plans/specs/export.md`,
  `{{fixture_dir}}/project/dd-02/sources/cli-schema.md`,
  `{{fixture_dir}}/project/dd-02/sources/library-api.md`,
  `{{fixture_dir}}/project/dd-02/sources/vendor-schema-status.md`, and
  `{{fixture_dir}}/project/dd-02/sources/git-history.md`.
- The plan says the new spelling is `--json`; the spec says `--format json`.
- A teammate recalls that the installed library supports streaming JSON, but no current source has been checked.

Checkpoint 2 — after the user resolves the conflict in favor of `--format json`:

- The implementation scope is not yet written or signed off.
- XML export is deliberately deferred because the vendor schema is unstable; XML consumers must wait for schema approval.

Checkpoint 3 — after the written plan diff is approved:

- The approved scope is limited to this behavior change, and no dispatch has occurred.
- No failing regression test has been written, run, or observed.
- No production implementation edit, candidate diff, or commit exists.

Checkpoint 4 — after the bounded implementation returns a green candidate diff:

- Unit tests pass, but nobody has invoked the CLI.
- The change renamed the load-bearing schema key `output_mode` to `format`; code, schema, examples, and documentation encode it.
- No commit has been created.

Checkpoint 5 — before PR creation:

- The current diff is limited to JSON export.
- The active plan also mandates `confirm_overwrite()` on destructive export, but a refactor three commits ago orphaned that safeguard; it is outside the current diff.
- No whole-branch self-review, external review, or smoke pass has run.

Return only one Markdown table with at least these columns (additional columns are allowed):

`Checkpoint | Parent gates/principles due now | Parent-owned action/artifact | Owner boundary | Blocked next action`

Use one row per checkpoint in order.
Do not narrate beyond the table.
