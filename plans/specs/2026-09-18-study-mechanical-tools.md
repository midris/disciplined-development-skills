# Mechanical study tools

Status: implemented and qualified; extends existing `skilltest docs` commands and version-1 formats.
Authority: owner requested the three proposed tools and process improvements after agreeing that deterministic and repetitive operations belong in tools.
The [active plan](../2026-09-11-model-driven-skill-testing.md) owns progress; the [framework spec](2026-09-11-model-driven-skill-testing-framework.md) retains model judgment and authorization boundaries.

## Commands and responsibilities

- `docs retain PROTOCOL BUNDLE --batch ID --order N --index INDEX --store DIRECTORY --revision FULL_COMMIT` selects one scheduled slot from the committed protocol, verifies the corresponding frozen manifest and runner configuration, copies a stopped bundle, verifies its complete inventory and registers the attempt. Create an empty index if absent; preserve existing entries. Derive charge from the runner's invocation-started flag, never from success. Do not score, dispatch or retry. Initial attempts only under the existing no-retry scope representation; unsupported cases fail explicitly.
- `docs tables PROTOCOL --batch ID --index INDEX --output FILE` produces Markdown tables for coverage, recorded judgments and functional outcomes, with evidence links. It includes invalid/unresolved/unassessed attempts and unattempted slots explicitly. Optional `--source-target TARGET --output-evidence ID` measures complete UTF-8 source/output files with `wc -w`, including signed changes and source-relative length flags; callers select what constitutes the source and delivered evidence, rather than the tool guessing. It writes a new fragment, never overwrites narrative or assigns judgments.
- `docs manifest MANIFEST --output FILE [--revision FULL_COMMIT] [--compare CONDITION CONDITION --allow-difference TARGET ...]` fills the existing manifest representation from its declared configuration/authority/controller paths. Enumerate the exact prompt/fixture union and derive hashes. Without revision, generate a checked working-tree draft; with revision, require matching committed bytes and generate a frozen manifest. Optional parity checks compare mounted files, prompt and execution settings, allowing only explicitly named differing targets (`@prompt` names the prompt). Preserve the original manifest and refuse output overwrite.

Preparation checks use the existing scope parser and manifest validator before the commit freeze. Add `docs check PROTOCOL --ready-for preparation --batch ID` for working inputs, scope and criterion applicability; it makes no frozen-readiness or authorization claim. Missing future index/assessment links do not block preparation, but missing actual inputs, malformed scope and unknown conditions do.

## Boundaries and failures

Use existing schemas and reference resolution rather than introducing a recipe format, workflow engine or new evidence layers. No provider, automatic Git mutation, semantic scoring or silent evidence repair.
All new output creation is exclusive. Retention stages a copy, checks source stability and destination equality, publishes the bundle and inventory, then atomically updates the index under an exclusive operation lock. A copy/verification failure never marks an attempt preserved. A publication or index-write failure may leave an explicitly reported unregistered bundle; retain it for inspection, refuse subsequent overwrite, and never silently adopt it. Existing index bytes remain intact on failure. A terminated operation can leave its lock/staging directory; inspect these manually rather than guessing whether another operation is alive.
Validate terminal runner metadata and reject unresolved cleanup, identity/configuration mismatches, duplicate slots/runs, missing invocation charges, malformed inputs and source/destination nesting. A terminal result plus stable inventory is evidence of a stopped bundle, not OS-level proof that arbitrary external writers cannot exist; the caller must wait for the runner to exit.
Copy hidden files, permissions and symlink targets without following links. Reject special files. Keep raw evidence outside repository history; tests and qualification use disposable copies only.
Tables validate referenced results/manifests/evidence and derive arithmetic; missing assessment stays unassessed, not failed. A malformed or mismatched record is an error, not an omitted row. Do not pool differing criterion sets into misleading counts. Existing supported no-retry batches are the scope; more elaborate inclusion/retry policies require explicit extension.

## Verification and process changes

Test before implementation: representative success and failure paths for each command, actual temporary Git identities, missing/malformed inputs, no-overwrite behavior, copy and index-write failures, duplicate registration, source mutation, source/control separation, unexpected paired differences, missing/unknown/invalid assessments, and length measurement. Exercise real CLI commands offline on disposable study/evidence fixtures. Existing historical records remain unchanged.
Use tools for mechanical operations; retain complete-document inspection and written reasons in the active session. Check draft structure, scope and parity before committing inputs; then freeze in dependency order and verify collection readiness. Generate tables only after recording judgments. Reuse qualified runtime mechanics and recheck relevant changes instead of repeating qualification by default.
Keep progress in the plan, decisions/accounting in the protocol, and conclusions in the assessment. Reduce handoff narrative to navigation and exceptional unresolved constraints. Do not remove provenance layers merely to reduce commit count.

Initial implementation/verification estimate: 150 active minutes within the remaining study-time allowance; no model invocations. Revise the forecast if concrete failures change remaining work.

Implementation is kept together because the commands share validation/publication helpers and CLI wiring; splitting those foundations into separately incomplete command commits would weaken reviewability.
Verification and resolved review findings: [tooling review](../../reviews/2026-09-18-study-mechanical-tools-review.md).

## Review correction: recorded capture and cleanup

Retention validates the runner schema and its recorded file/directory artifacts before certifying a copy, respecting artifacts recorded absent after a failed run.
Result version 0.5 records cleanup failure independently because version 0.4's primary timeout/exit error can hide it.
The retention command accepts 0.5 and completed 0.4 bundles; failed 0.4 bundles require manual inspection/preservation, with existing historical records unchanged.
This versioned producer correction supplies a fact the approved retention contract needs; it does not change study scoring or authorize subject runs.
Paired checking reserves `@prompt` so a fixture cannot shadow the prompt; generated links and all document consumers decode URL paths consistently.

Follow-up verification: [review and corrections](../../reviews/2026-09-18-study-tools-followup-review.md).
