# Round-9 findings and resolution

Scope: external review of commits `6c0976a` through `8603fae`; active-session verification, correction and self-review.
The quoted owner approvals are present in the conversation: ten expansion calls/ceiling 56 and the two-provider isolation correction.
No new provider calls, scoring changes, case changes or production permission grants were made.

## Findings addressed

- **Probe interpreter:** reproduced six Claude smoke failures with `uv run pytest -q -m process_smoke` outside the controller sandbox.
  Caller PATH selected the home-installed uv interpreter, which the production policy correctly denies.
  All five probe/interpreter selection sites now resolve Python only through `/opt/homebrew/bin:/usr/bin:/bin`, the existing tool roots; the caller's virtual environment is not a sandbox dependency.
  Production permissions remain unchanged.
- **Original result selector:** the original's line 62 is its final assistant message, not the control's contaminated tool response.
  Corrected that selector without changing its artifact hash, scores or setup judgment; update the result → index → assessment references in dependency order.
  The control retains its correct line-62 exposure citation.
- **Historical evidence:** the targeted audit below replaces the previous untested assumption with a recorded check and explicit capture limits.
- **Standalone partial assessment:** reproduced the unsupported-coverage notice plus thirteen spurious unexpected-row errors.
  Rows belonging to declared groups whose criteria cannot be resolved without the protocol now retain the unsupported notice without invented criterion errors.
  Duplicate/malformed rows, unknown groups, known-criterion errors and protocol readiness remain checked.
  The regression test covers standalone unsupported coverage and protocol detection of a genuinely missing row.

## Historical trace audit

Audited every indexed attempt: 46 preceding the expansion, plus the two new attempts as negative/positive controls.
All 48 selected trace hashes match their retained inventories; versioned inventory-file hashes were also checked where the index uses external inventories.
For each attempt, use `provider-session.jsonl` when retained, otherwise `stdout.txt` events.

| Earlier scope | Attempts | Full sessions | Stdout-only traces | Targeted marker matches |
|---|---:|---:|---:|---:|
| SSR | 30 | 23 | 7 | 0 |
| CW | 16 | 16 | 0 | 0 |
| Total | 46 | 39 | 7 | 0 |

Searches covered the private evidence and backup-store paths, repository checkout path, `~/.claude/projects` path, the observed `claude-501` scratch namespace and encoded project-directory name, `round5.py`, the broader `round[0-9]+\.py` pattern, and every other indexed run's unique directory name (excluding the current run).
The new original has no such matches; the excluded control matches at lines 61–62, including the preceding original's run directory, confirming detection of the known incident.

Six earlier full sessions contain `cd /tmp` for the moved-guide export check: four originals and two candidates.
One older original stdout trace contains the same check, making seven earlier attempts in total.
Inspection of their commands found subshell-scoped directory changes or an explicit return to the fixture before subsequent work; none searched from `/tmp`.
The audit's per-attempt rows retain their exact trace paths, hashes and line numbers.

**Limits:** this is a targeted literal/pattern sweep of retained evidence, not proof of exhaustive historical isolation.
Seven early attempts lack full model-facing sessions; their stdout events may omit or truncate delivered tool output.
Other aliases, unknown controller filenames, encoded content, unlogged access or exposure without one of these markers are not ruled out.
The earlier runtime did permit broader reads; the audit does not retroactively establish an enforced boundary or upgrade invalid/unresolved setups.
Earlier outcome judgments remain unchanged with these observation limits made explicit.

Reproducible script and full audit record are retained at `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/development/round9-trace-audit/`:

| Artifact | SHA-256 |
|---|---|
| `round9-audit.py` | `b3972daceea6ab055fc3e541436e3536e5f8002735eb276719d084ee2aae6b1d` |
| `round9-audit.json` | `6649fb04e11d73161684c650da31d7ce4f97349bb15389d4114a225ae20de9df` |
| `round9-audit-summary.txt` | `8b97684a81e4ff584a45cd44ddd84b39e7168bb2166bcb994cb8b1021474987c` |

These files use the already accepted same-host retention arrangement; no backup claim is added.

## Verification and self-review

Review checked caller-PATH dependencies across offline and acceptance probes, selector/run identity, historical trace availability, unknown versus invalid criterion handling, reference-pin propagation and accounting.
The historical audit corrected the external review's capture generalization: 39 full earlier sessions plus seven stdout traces, not 46 full sessions.
No further blocking finding remains identified.
Verification: `uv run pytest -q` passed all 458 runner tests; the seven installed-policy acceptance checks also passed under `uv run` with no model calls.
Hooks passed 263 tests with three existing skips.
Standalone checking now reports only the designed unsupported-coverage notice; protocol readiness remains the complete check for this partial batch.
The corrected result, index and assessment references were updated in dependency order; all six batch readiness checks passed after the final pin update.
`git diff --check` passed.

DD-VERDICT: PASS
