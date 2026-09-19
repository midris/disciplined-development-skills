# Owner-requested review of the mechanical study tools

Scope: all changes in `43060c8`, their runner/schema/document consumers and the governing [tool spec](../plans/specs/2026-09-18-study-mechanical-tools.md) and [active plan](../plans/2026-09-11-model-driven-skill-testing.md).
Method: active-session review plus a fresh code-review subagent, followed by the same reviewer's verification of fixes; no subject or scoring invocations.
This follow-up corrects the initial review's missed validation boundaries.

## Findings and fixes

| Finding | Resolution |
|---|---|
| P1: retention compared the copied bundle only with its current source, so evidence deleted or modified after runner capture could be certified. | Validate the shared runner schema and compare recorded file/directory artifacts with the source inventory before copying. Respect legitimately absent artifacts. Retention fixtures now use the actual result producer. |
| P1: a primary timeout, exit or preparation error could hide cleanup failure. | Runner result 0.5 records `execution.cleanup_error` independently. Retention rejects unresolved cleanup and failed legacy 0.4 records that cannot establish it; completed 0.4 records remain supported. Historical records and read-only study interpretation are unchanged. |
| P1: a fixture mounted as `@prompt` could overwrite the prompt entry in paired comparison. | Reserve that target during paired checking and fail explicitly before producing a manifest. |
| P2: generated URL-encoded result links failed downstream validation, particularly with spaces or `#` in filenames. | All document link consumers split URL fragments before decoding path characters. A regression exercises generated tables through the assessment validator. |

The corrections address the shared boundary between a producer's declared facts and a consumer's checks, rather than adding more scoring or workflow layers.
The result schema is packaged once with the CLI; version 0.5 makes the added cleanup requirement explicit while preserving historical 0.4 schema validation.
No automatic migration, model dispatch, retry, semantic judgment or baseline change was introduced.
The reviewer rechecked capture, cleanup/version handling, schema packaging, URL decoding, paired checks and documentation and returned no findings.

## Verification

- Reproduced all four failure classes before fixes; added 12 mechanical-tool regression cases and one result-producer case.
- Full offline runner suite: 425 passed. Hook suite: 263 passed, three existing skips. Format suite: nine passed.
- Reviewer focused suite: 181 passed; a separate nested-directory/regular-file/ordinary-symlink/dangling-symlink retention probe passed.
- Built the wheel offline; confirmed packaged schema bytes match the canonical schema. Executed retention and index checking using the wheel, with the expected unassessed-result limitation.
- Read-only comparison of all eight retained CW comparison bundles with their recorded captures passed. No historical evidence changed.
- Both CW assessment-readiness checks and the documentation/reference sweep passed.

No findings.

DD-VERDICT: PASS
