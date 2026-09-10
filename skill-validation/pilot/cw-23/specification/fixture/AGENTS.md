# Project guidance

This repository contains documentation for an internal job worker.
The approved task is an editorial update to the restart guide and its affected navigation; operational policy stays unchanged.
The source of that policy is the supplied `docs/restarting.md`.
No executable service is present, and this task does not authorize service operations.

Local Markdown links use relative paths and heading fragments.
Headings resolve to lowercase fragments with spaces replaced by hyphens.
Verify file targets and heading fragments directly from the resulting files.
There are no generated documents or external link dependencies in this fixture.

Use the empty Git repository created by the runner; do not reinitialize it or create a setup commit.
Stage the three project documents before editing so their original content remains available for a diff.
After checking the edit, stage the final documents and commit them together using the command-local identity specified in the task.
Leave project guidance and installed skills out of the commit.
Record the verification actually performed in the commit and handoff.
This task ends at the local documentation commit, before any PR or external review stage.
