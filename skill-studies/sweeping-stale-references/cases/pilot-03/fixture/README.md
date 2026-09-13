# Relaypack

Relaypack builds a reproducible ZIP for a static-site support handoff.
It validates project versions, records SHA-256 digests and can inspect an archive.
Run from this checkout with Python 3.12 or later; dependencies are vendored.

## Quick start

```sh
python3 tools/relaypack.py build --manifest project.json --output-dir build/quickstart
```

The result is `build/quickstart/relay-demo-1.4.0.zip`.
Use `python3 tools/relaypack.py inspect build/quickstart/relay-demo-1.4.0.zip` to inspect it.

## Development

Run `python3 -m unittest discover -s tests` for the CLI behavior tests.
`make help` lists developer commands. The project manifest defines the release contents.
See [project manifests](docs/manifests.md), [archive format](docs/archive-format.md),
[releases](docs/releases.md), and [vendored dependencies](vendor/README.md).
