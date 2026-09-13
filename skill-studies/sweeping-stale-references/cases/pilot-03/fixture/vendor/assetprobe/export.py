"""Independent asset inventory utility; this is not the Relaypack CLI."""
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser(description='Export a static asset inventory.')
parser.add_argument('--output-dir', required=True)
args = parser.parse_args()
destination = Path(args.output_dir)
destination.mkdir(parents=True, exist_ok=True)
(destination / 'inventory.json').write_text(json.dumps({'format': 1, 'kind': 'asset-inventory'}) + '\n')
