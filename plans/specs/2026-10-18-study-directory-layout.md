# Separate study guidance from collected evidence

Status: implemented and verified for both studies; [migration review and inventory](../../reviews/2026-10-18-study-directory-layout.md) record preservation and checks.
Authority: the owner answered “Approve both CW and SSR” to the complete core/runs layout proposal and its 60–90-minute estimate; no model tests were authorized.
The owner requested separating core study documents from assessment runs and results after the CW reassessment.
This design covers the current CW and SSR directories, not the superseded frameworks under skill-validation.
It supplies no model-call authorization and does not change scenarios, scores, skill bodies or evidence-retention policy.

## Proposed layout

Keep a small reader-facing entry surface and put completed collection material under named run directories:

```text
skill-studies/
  README.md
  formats/
  concise-writing/
    README.md
    protocol.md
    testing-audit.md
    assessment-policy.txt
    cases/
    drafts/
    runs/
      contribution-baseline-01/
      comprehensive-comparison-01/
      suite-2026-09-27/
      baseline-iteration-e-01/
      cross-model-evaluation-01/
      contact-reassessment-01/
  sweeping-stale-references/
    README.md
    protocol.md
    HANDOFF.md
    cases/
    drafts/
    runs/
      pilot-01/
      pilot-02/
      core-baseline-01/
      ...
```

The exact run names above are controller proposals, not owner-selected names.
Each run directory contains its batch assessments, attempt indexes, structured results, collection-specific preparation/qualification and evaluator material.
Keep provider-specific batch IDs and recognizable filenames; the current readiness reader discovers assessments through filenames ending in `-assessment.md` and indexes ending in `run-index.json`.
One collection may contain several provider/batch records: the CW expanded suite and its native supplement share preparation, while the E diagnostic has its own preparation and two Opus reviews.
Cross-collection retrospective reviews and reassessments get their own run directories, with links to the observations they cover.

## Document ownership

The study README is a short navigation page: core documents, candidate drafts and a collection table linking each run's summary.
The protocol remains the authority for current decisions, scoring interpretation, coverage and spending; it is not replaced by another status document.
The active plan remains the checklist authority.
The existing CW testing audit remains the coverage/design audit; do not duplicate it in README.
Keep shared cases, fixture bytes, preserved skill snapshots and current authoring drafts at stable locations where possible.
Move run-specific material out of `drafts/baseline-iteration/testing/`; drafts should expose the candidate bodies and design, while the completed E execution belongs under runs.
The shared format contracts stay under formats; add a root README linking the two studies and these formats.
Do not reorganize private raw bundles or turn them into checked-in data.

## Migration and preservation

Inventory tracked files and produce an explicit old-to-new map before moving them.
Map each structured result through its attempt index, not a guessed timestamp or filename substring.
Group shared preparation with its collection rather than duplicating it per provider.
Classify the remaining qualification, diagnosis and worked-example files individually; unused drafts remain labelled undispatched rather than presented as completed runs.

Git-qualified identities retain their original revision, path and hash: moving the current file does not relocate its historical bytes in an earlier commit.
Update current Markdown links, unqualified working-tree references and navigation separately from historical identities.
Do not rewrite an old hash to conceal a changed file or repoint a recorded subject at new input bytes.
Configs resolve fixture/prompt paths relative to their own location; preserve shared executable input locations unless a new current config is deliberately derived and checked against the original supplied bytes.
No skill/fixture change is permitted as a side effect of moving assessment material.

Assessment Markdown also pins the accepted attempt index's Git location.
Freeze the new index locations before repinning those reports: first add the relocated index copies in a preservation commit while the current protocol still resolves the existing layout, then switch links/pins and remove old working-tree locations in the final migration commit.
This temporary publication sequence avoids an accepted commit whose report refers to an index path absent from its cited revision.
Final layout has one current location per artifact, without root-level redirect files or symlink aliases.
The migration map records any Markdown-link or explicit metadata edits; original accepted bytes remain retrievable from their existing Git identities.

## Acceptance

- Core entry pages lead directly to the current contract, coverage, candidates and results without scanning dozens of batch files.
- Every current artifact has one classified location and every moved path is accounted for.
- All eighteen existing CW/SSR batch readiness checks still pass through the real document CLI.
- The thirteen superseding E results and the 58-entry reassessment map still resolve their original and current evidence correctly.
- Check every current local Markdown link in the affected studies and every referring repository document; distinguish intentionally historical Git paths from broken working-tree links.
- Every moved inventory/index/result preserves run IDs, conditions, repetitions, charges and judgments; counts do not grow because of temporary copies.
- Skills, source fixtures, private evidence paths and inventories remain unchanged; recheck affected fixture/config consumers and the hook suite.
- No inference calls, schema redesign, generic migration framework or automatic historical rerun is part of this cleanup.

Controller estimate: 60–90 active minutes, including mapping, two publication commits, link/identity correction, readiness and review.
This is a mechanical evidence migration; it does not include preparing or running the remaining CW comparison.
The remaining CW tests are A/B/C followed by N1–N4, with E reused only while draft/input/runtime conditions remain qualified.
