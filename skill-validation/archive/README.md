# Legacy Skill Validation Records

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
