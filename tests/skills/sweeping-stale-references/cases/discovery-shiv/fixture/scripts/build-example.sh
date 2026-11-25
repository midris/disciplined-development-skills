#!/bin/sh
set -eu
cd "$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
mkdir -p build
python3 -I tools/shiv-local.py --site-packages examples/greeting -e greeting:main --output-file build/local.pyz
