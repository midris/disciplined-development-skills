We maintain a reference skill used by development agents.
Its main `SKILL.md` points agents to `references/export-command.md`, a shipped reference containing this passage:

> `export-records --output PATH` writes the export to PATH.
> The `--output` argument identifies the destination file.
> If PATH already exists, the command stops without changing that file.
> Use `--replace` only when you intend to overwrite an existing destination.
> The `--replace` option permits replacing the file at PATH; without it, an existing file is preserved.

The maintainer wants this reference shorter and easier to use while leaving the main `SKILL.md` unchanged.
This is part of the skill's instructions for agents looking up the command, not ordinary project documentation.

Before changing it, inspect the available guidance and briefly identify which guidance you would apply to this edit.
If you inspect guidance that you decide does not apply, distinguish that from the guidance you selected.
This checkpoint is only guidance selection; do not draft the replacement, run the command, or carry out validation or publication.

Work read-only within the supplied fixture.
Do not edit files, change Git state, inspect outside the fixture, use the network, or dispatch agents.
