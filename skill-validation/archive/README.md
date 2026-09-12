# Legacy Skill Validation Records

> **Abandoned testing process — historical reference only (2026-09-11).**
> Testing-framework instructions, approvals and pending work below are no longer current. Follow the [new framework spec](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md) and [new testing plan](../../plans/2026-09-11-model-driven-skill-testing.md).
> The original text is preserved as history; this notice does not retire existing runner tooling or core skills.


This directory holds the validation records that previously lived at the
`skill-validation/` root. The move is organizational: it does not activate the
deferred baseline design, change recorded results, or retire an existing validation
gate.

## Transitional authority

Until the owner explicitly approves a replacement for a skill catalog, its file in
`skill-records/` remains the validation record that `CLAUDE.md` requires updating
after a non-trivial skill change. After an approved catalog cutover, that legacy
record becomes read-only historical evidence.

Files in `shared-records/` preserve validation evidence that spans skills or records
an earlier shared evaluation protocol. They are not standalone replacement catalogs.

## Layout

- `skill-records/` contains one legacy validation record for each repository skill.
- `shared-records/` contains the three legacy cross-skill records.
