# Line-count command implementation plan

> For agentic workers: use superpowers:executing-plans to implement this plan task by task.

**Goal:** Build the local line-count command described in the approved design.
The goal of this plan is to describe how to build that command.
**Architecture:** One Python command reads one bounded UTF-8 export and reports its line count; tests exercise its observable CLI behavior.
**Tech stack:** Python 3.11 or later, standard library, unittest.
**Spec:** [Approved design](../docs/linecount-design.md).

## Constraints and delivery

Use the design's command interface, exit behavior, newline rules and inclusive 1 MiB limit.
There are no third-party dependencies.
The project will have no dependencies from outside the Python standard library.
Deliver one reviewable PR from `feature/linecount`, with implementation, tests and documentation committed together after verification.
Do not create packaging, an installer or a library API.

## Task 1: Implement, document and verify the command

**Files:** Create `src/linecount.py`, `tests/test_linecount.py` and `README.md`.
**Input:** One path supplied as the command's sole positional argument.
**Output:** A line count on stdout and exit 0, or a stderr error without a count and exit 2.
These are the inputs and outputs of the command that this task implements.

- [ ] Write CLI tests for the behaviors in the table and run `python3 -m unittest discover -s tests -v`; observe failures before implementation.
- [ ] Implement the command to satisfy the tests, then rerun them and inspect the results.
- [ ] Exercise the command directly against temporary valid, empty and invalid files; compare stdout, stderr and exit status with the design.

| Input or condition | Required result |
|---|---|
| Empty UTF-8 file | Count 0. |
| `a\nb\n` or `a\nb` | Count 2; a final newline is not an extra empty line. |
| One LF newline, or two CRLF-terminated lines | Count 1 or 2 respectively. |
| Missing or extra argument; missing/unreadable file; directory path | Stderr error, no count, exit 2. |
| Invalid UTF-8 | Stderr error, no count, exit 2. |
| Exactly 1,048,576 ASCII `a` bytes | Count 1. |
| 1,048,577 bytes | Stderr error, no count, exit 2. |

Read the validated file into memory instead of building a streaming counter.
This is the choice to use a whole-file read rather than a streaming approach.
The current internal exports fit within the limit, and the bounded read keeps the first implementation simple.
We accept rejecting larger exports, which users must split or count with another tool.
Standard input and recursive directory traversal are deliberately excluded because the caller supplies one export path.

The file must be a readable, valid UTF-8 file within the limit; these are checked conditions, not assumptions of every caller.
Tests for unreadable files must actually establish unreadability under the test user; permissions that still allow a read do not exercise that condition.
Changing files during a read is an accepted edge: this internal command is used on completed exports, so concurrent-writer coordination is outside this feature.

### Document and commit

- [ ] After the command works, document invocation, representative output, error behavior, the size limit and the accepted scope limitations in `README.md`.
- [ ] Run the tests and direct CLI checks again against the complete change; inspect their results and the final diff.
- [ ] Commit the implementation, tests and documentation together after they pass.

This section describes documenting and committing the feature.
Implementation does not begin during review of this plan.
