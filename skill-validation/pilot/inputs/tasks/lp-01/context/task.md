# JSON report CLI change

Existing project facts:

- `src/report_cli.py` owns argument parsing and report rendering.
- `tests/test_report_cli.py` owns CLI contract tests.
- `report PATH` currently emits text.
- `report --format text PATH` is accepted.

Required change:

- Accept `--format json` as well as `text`.
- JSON output is an object with string field `path` and integer field `line_count`.
- An unsupported format writes `unsupported format` to stderr and exits with status 2.
- The default remains text.
- No other command behavior changes.
