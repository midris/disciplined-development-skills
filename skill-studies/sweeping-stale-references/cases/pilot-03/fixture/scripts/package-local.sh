#!/bin/sh
set -eu
cd "$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
python3 tools/relaypack.py build --manifest project.json --output-dir build/local
