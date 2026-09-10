# Line-count command: approved design

Build a local command for counting lines in small UTF-8 text exports.
The interface is `python3 src/linecount.py PATH` with exactly one positional path.
Use Python 3.11 or later and the standard library only.

## Behavior

Print the line count as a decimal integer followed by a newline and exit 0.
An empty file has zero lines.
Each newline ends a line; a nonempty final segment without a newline counts as one additional line.
For example, `a\nb\n` and `a\nb` each have two lines; `\n` has one.

Missing or extra arguments, a missing or unreadable file, a directory path, invalid UTF-8, or a file larger than 1 MiB must produce a concise stderr error, no stdout count, and exit 2.
The size limit is inclusive: exactly 1,048,576 bytes is allowed; 1,048,577 is rejected.
Follow the platform's normal newline translation when reading text; both LF and CRLF exports are supported.

## Scope decision

Read the validated small file into memory rather than build a streaming counter.
These internal exports fit within 1 MiB, so a bounded whole-file read keeps the first implementation simple.
Larger exports are deliberately rejected rather than partially counted; this accepts that users must split them or use another tool.
Standard input and recursive directory traversal are out of scope because the current caller supplies one exported file path.
The caller supplies completed exports that do not change during counting; coordinating with concurrent writers is outside this feature.

## Delivery

One feature branch and one PR can contain the implementation, focused tests and usage documentation.
Use `src/linecount.py` for the command, `tests/test_linecount.py` for standard-library unittest coverage, and `README.md` for usage and limitations.
Tests must precede implementation; the resulting commit must pass them and direct command checks.
No library API, packaging system, installer or network integration is required.
