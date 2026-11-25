"""Independent file-list report utility, not the archive builder."""
import argparse
import json
from pathlib import Path
parser = argparse.ArgumentParser(description='Write an inventory of input files.')
parser.add_argument('source', type=Path)
parser.add_argument('--output-file', required=True, type=Path)
args = parser.parse_args()
files = sorted(p.relative_to(args.source).as_posix() for p in args.source.rglob('*') if p.is_file())
args.output_file.parent.mkdir(parents=True, exist_ok=True)
args.output_file.write_text(json.dumps({'files': files}) + '\n')
