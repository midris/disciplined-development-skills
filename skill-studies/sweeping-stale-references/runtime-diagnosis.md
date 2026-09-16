# Shiv subject runtime: diagnosis and correction

Status: correction implemented, verified offline and exercised in all seven resumed subject executions under owner approval.
Affected batch: [core-baseline-01](protocol.md#core-baseline-core-baseline-01), now complete; the protocol owns runtime-1 authority and the assessment owns outcomes/exclusions.

## Observed fault

Order 5 repaired all four consumers, but its shell selected `/usr/bin/python3` (Apple Python 3.9.6).
The supplied Click runtime uses `match` syntax that this interpreter cannot parse, so the subject's verification failed before testing the intended behavior.
Its retained session establishes the full skill read; this is separate from the repaired capture problem.
The [execution result](results/20260916T204716513Z-ssr-discovery-shiv-original-4ea35baa-b309-4e61-b7cc-7d7a0c61ae69-75y8tek9.json) records invalid setup and excludes the attempt from valid-setup aggregates.

Preparation verified the fixture under host Python 3.14 and checked runner copying, but did not qualify executable selection inside Codex's actual shell tools.
The runner supplied a restricted PATH to the CLI while `shell_environment_policy.inherit="none"` did not explicitly carry that PATH into the tools.
The resulting shell path selects Apple's Python before the compatible Homebrew interpreter.
The pinned CLI source implements `inherit=none` as an empty inherited map and applies explicit `set` values separately: `codex-rs/protocol/src/shell_environment.rs:99–146` at Git `6b9826e3aa83b1a5947db50f4332cb9c65f1b340`.

## Concrete correction

[providers.py](../../skill-validation/runner/src/skilltest/providers.py) now forwards only the private runtime's existing restricted PATH through an explicit Codex shell policy:

```text
shell_environment_policy.inherit="none"
shell_environment_policy.set={PATH="/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"}
```

The path is derived from the prepared runtime, not an inherited user shell configuration or a new case-specific setting.
This selects `/opt/homebrew/bin/python3`, Python 3.14.7, on the qualified host.
Authentication, ambient environment variables, instructions, permissions, fixtures, prompts, model/effort and criterion meanings remain unchanged.
The focused test failed before the correction and passes after it; the full offline runner suite passes 307 tests.

The credential-free localhost diagnostic uses fixed scripted tool calls and no model inference.
With the explicit PATH, all four local tests pass, all four repaired consumers build runnable greeting archives, and the script works outside the checkout.
Compatible-runtime controller replay also confirms the unchanged CLI/alias, retired-option rejection and independent inventory tool.
Those observations establish the repair's artifact quality; they cannot restore a compatible runtime to the already-completed subject attempt.

Diagnostic evidence is retained at `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/development/python-path-diagnostic-20260916/`; its sibling `.inventory.json` has SHA-256 `16c7c158affc5484e9f0f72aba3f94679755de70a11567006b68865281137dd3` (20 files, 492,151 bytes).
The existing-policy diagnostic establishes interpreter selection; its scripted response returned while tests were still running, so the actual subject session supplies the completed failure evidence.
The proposed-PATH diagnostics include complete successful tests and consumer observations. No private profiles or authentication files were retained in these diagnostic bundles.

The final production-adapter qualification (without a prototype PATH override) is retained separately at `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/development/python-path-qualification-20260916/`; its sibling `.inventory.json` has SHA-256 `27b096f4e38675fa0f2c627287f51bd9f0f949598bfb8bd6973fcf3e9f605ec6` (10 files, 179,957 bytes). It includes the exact changed adapter source and resolved Python binary hash. All four tests and consumer checks pass through the actual argument builder.

## Completed resumption

Orders 6–12 completed under the approved explicit-PATH amendment; their index entries pin the frozen runner/protocol authority. The three resumed Shiv executions used a compatible runtime, while both original setup exclusions remain charged and unreplaced. See the [batch assessment](core-baseline-01-assessment.md) for evidence and outcomes.
Orders 2–4 also retain the earlier runtime configuration. The index labels that limitation and the assessment distinguishes runtime strata; per-condition totals across strata are descriptive mixed-configuration counts. Do not treat repetition differences as a pure skill or stochastic effect. The invalid Shiv attempt remains excluded.
No skill rewrite or document generator/validator work follows from this repair.
