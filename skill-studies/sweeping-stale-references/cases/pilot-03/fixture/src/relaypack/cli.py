"""Command-line interface for archive production and inspection."""
import argparse
import json
import sys
import zipfile
from .archive import build, inspect


def main(argv=None):
    parser = argparse.ArgumentParser(description='Build a reproducible Relay release archive.')
    actions = parser.add_subparsers(dest='action', required=True)
    builder = actions.add_parser('build')
    builder.add_argument('--manifest', required=True)
    builder.add_argument('--destination', required=True)
    inspector = actions.add_parser('inspect')
    inspector.add_argument('archive')
    args = parser.parse_args(argv)
    try:
        if args.action == 'build':
            print(build(args.manifest, args.destination))
        else:
            print(json.dumps(inspect(args.archive), sort_keys=True))
    except (OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0
