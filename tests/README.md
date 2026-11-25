# Testing a skill

Start with the [study workflow](methodology/README.md) and [governing framework](methodology/framework.md).
Read the shipped skill and agree on the behavior a future user needs before choosing cases or drafting a revision.
The [format contracts](methodology/formats/README.md) and [runner guide](runner/README.md) cover frozen inputs, collection, retention and assessment.

## Walk through a study offline

From a clean checkout with Git, uv and Python 3.11 or later, run the following commands in one shell.
The runner tests create disposable repositories and synthetic subjects.
The walkthrough leaves the example under a new temporary directory for inspection.

```sh
cd tests/runner
uv sync --locked
study_tmp=$(mktemp -d)
uv run --locked --offline pytest -q tests/process_smoke/test_study_walkthrough.py \
  --basetemp "$study_tmp/walkthrough"
protocol=$(find "$study_tmp/walkthrough" -type f -name protocol.md | head -1)
uv run --locked --offline skilltest docs check "$protocol" --ready-for assessment --batch example
cat "$(dirname "$protocol")/example-assessment.md"
```

The walkthrough freezes a two-attempt study in Git, runs both slots through the installed CLI with a local stand-in for Codex, and checks the resulting bundles and judgments at collection and assessment readiness.
Inspect its protocol, manifest, attempt index and results beside the assessment.
Expect two included attempts, one met and one not met, with both results cited.
Changing a recorded judgment without reconciling its aggregate should fail the readiness check.
Run the full offline suite with `uv run --locked --offline pytest -q` from the same directory.

## Promoting a skill

Use one PR per adopted skill. Put its protocol, runnable cases, assessment rules and adoption results under `tests/skills/<skill>/` and install the exact tested bytes under `skills/<skill>/`.
Use the existing manifest, attempt index and assessment to identify the candidate digest, case set, runner revision, provider settings, results and evidence inventories.
Include every attempt and the bounds of the comparison. Where the broader suite used a different text, identify that text.
Keep reserved inputs and raw private transcripts in the controlled evidence store. Record a durable locator, hash and retrieval instructions for authorized reviewers.
Verify the installed bytes, evidence references and offline checks in a clean checkout before merging.

The maintained runner lives under `tests/runner/`. The historical path `skill-validation/runner/` points to that same implementation for existing shell commands.
Read historical scores with the criteria and runner revision recorded at collection. The [legacy validation records](../skill-validation/README.md) retain those identities.
