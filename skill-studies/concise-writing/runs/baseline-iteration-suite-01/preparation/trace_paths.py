"""Collection-specific target-write recognition; does not edit captured data."""
from pathlib import PurePath


def is_target_path(value):
    # Claude's retained Write call may end in a newline; the tool delivered the
    # normalized declared file. Keep raw evidence intact and inspect that target.
    return PurePath(str(value).rstrip('\r\n')).name in {'report.md','settings.toml','uploader.py'}
