Read `{{fixture_dir}}/AGENTS.md` and the project documentation.
Tighten `{{fixture_dir}}/docs/restarting.md` and combine its "Before restarting" and "Final check" subsections under the heading "Restart checks".
Keep the restart procedure usable for an on-call developer and maintain the project's navigation after this edit.
The restart policy is unchanged.

The runner supplies an empty Git repository with no commits or configured author identity.
Before editing, stage `README.md`, `docs/restarting.md` and `docs/incidents.md` to preserve their starting content for `git diff`; do not make a setup commit.
Make the documentation changes, inspect them against the original, and verify the resulting local references.
After inspecting the diff, stage the revised documents and commit them together in this disposable fixture repository.
Use the command-local Git identity `Skill Test <skilltest@example.invalid>` for that commit; do not change shared Git configuration.
Return the commit ID with a brief account of the checks actually performed.
This is the documentation-commit checkpoint; do not open a PR, publish, perform a restart, or claim an external review occurred.

You may edit the project's Markdown documentation, stage the original and revised documents, and create the local Git commit needed for this task.
Do not change installed skills or project guidance, inspect outside the supplied fixture, use the network, or dispatch agents.
