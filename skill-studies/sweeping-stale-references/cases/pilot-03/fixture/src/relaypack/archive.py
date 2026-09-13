"""Reproducible ZIP output and checksum-backed inspection."""
import hashlib
import json
from pathlib import Path
import zipfile
from .project import load_project


def build(manifest, destination):
    metadata, files = load_project(manifest)
    content = {target: source.read_bytes() for source, target in files}
    metadata['sha256'] = {target: hashlib.sha256(data).hexdigest()
                          for target, data in sorted(content.items())}
    content['manifest.json'] = (json.dumps(metadata, indent=2, sort_keys=True) + '\n').encode()
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / (metadata['name'] + '-' + metadata['version'] + '.zip')
    with zipfile.ZipFile(target, 'w') as archive:
        for name, data in sorted(content.items()):
            info = zipfile.ZipInfo(name, (2024, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    return target


def inspect(path):
    with zipfile.ZipFile(path) as archive:
        metadata = json.loads(archive.read('manifest.json'))
        for name, expected in metadata['sha256'].items():
            if hashlib.sha256(archive.read(name)).hexdigest() != expected:
                raise ValueError('checksum mismatch: ' + name)
        return metadata
