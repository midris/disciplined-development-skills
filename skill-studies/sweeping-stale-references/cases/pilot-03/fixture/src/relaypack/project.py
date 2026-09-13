"""Load project metadata and validate files before producing an archive."""
import json
from pathlib import Path, PurePosixPath
import re
from packaging.version import Version, InvalidVersion


def load_project(path):
    path = Path(path).resolve()
    value = json.loads(path.read_text())
    name = value['name']
    if not isinstance(name, str) or not re.fullmatch(r'[a-z][a-z0-9-]*', name):
        raise ValueError('invalid project name')
    try:
        version = str(Version(value['version']))
    except (InvalidVersion, TypeError) as error:
        raise ValueError('invalid project version') from error
    entries = []
    destinations = {'manifest.json'}
    for item in value['files']:
        source = (path.parent / item['source']).resolve()
        target = PurePosixPath(item['target'])
        if not source.is_relative_to(path.parent) or not source.is_file():
            raise ValueError('source must be a file inside the project')
        if target.is_absolute() or '..' in target.parts or str(target) in destinations:
            raise ValueError('invalid or duplicate archive path')
        destinations.add(str(target))
        entries.append((source, str(target)))
    if not entries:
        raise ValueError('project has no files')
    return {'name': name, 'version': version}, entries
