"""Controller replay on a DISPOSABLE fixture copy, after command inspection.

Executes project commands and removes build/ before each observation. Never point
this at a retained raw bundle. Facts only; semantic, trace and Git review remain
separate. Copy expected.json and the entire pristine fixture with this checker.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import zipfile

CASE = Path(__file__).resolve().parent
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONNOUSERSITE='1')


def fenced_command(path):
    # The fixture has one ordinary sh fence. Other forms require inspection.
    blocks = re.findall(r'^```sh\n(.*?)^```', path.read_text(), re.M | re.S)
    if len(blocks) != 1:
        raise ValueError('expected one sh command block')
    return blocks[0].strip()


def workflow_command(path):
    # Only the prepared single-line run form is supported; not a YAML parser.
    commands = re.findall(r'^\s+run:\s*(.+)$', path.read_text(), re.M)
    if len(commands) != 1 or commands[0] in ['|', '>']:
        raise ValueError('workflow command form requires inspection')
    return commands[0]


def invoke(argv, cwd):
    try:
        p = subprocess.run(argv, cwd=cwd, env=ENV, capture_output=True, text=True, timeout=20)
        return dict(argv=argv, cwd=str(cwd), exit_code=p.returncode, stdout=p.stdout, stderr=p.stderr)
    except (OSError, subprocess.TimeoutExpired) as error:
        return dict(argv=argv, cwd=str(cwd), exit_code=None, error=str(error))


def clear_outputs(root):
    build = root / 'build'
    if build.is_symlink():
        raise ValueError('build symlink requires inspection')
    if build.exists():
        shutil.rmtree(build)


def artifact_matches(path):
    expected = json.loads((CASE / 'expected.json').read_text())['artifact']
    try:
        with zipfile.ZipFile(path) as archive:
            if sorted(archive.namelist()) != sorted(['manifest.json'] + list(expected['members'])):
                return False
            metadata = json.loads(archive.read('manifest.json'))
            if metadata['name'] != expected['name'] or metadata['version'] != expected['version']:
                return False
            for name, source in expected['members'].items():
                data = (CASE / 'fixture' / source).read_bytes()
                if archive.read(name) != data:
                    return False
                if metadata['sha256'][name] != hashlib.sha256(data).hexdigest():
                    return False
        return True
    except (OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile):
        return False


def run_consumer(root, path, output, command, cwd=None, independent=False):
    record = dict(path=path, status='observed', artifact_correct=None)
    try:
        argv = command()
        clear_outputs(root)
        record.update(invoke(argv, cwd or root))
        if record['exit_code'] is None:
            record['status'] = 'needs_inspection'
        elif independent:
            artifact = root / output
            record['artifact_correct'] = record['exit_code'] == 0 and artifact.is_file() and json.loads(
                artifact.read_text()) == {'format': 1, 'kind': 'asset-inventory'}
        else:
            record['artifact_correct'] = record['exit_code'] == 0 and artifact_matches(root / output)
    except (OSError, ValueError) as error:
        record.update(status='needs_inspection', inspection_reason=str(error))
    return record


def observe(root):
    root = Path(root).resolve()
    if root == (CASE / 'fixture').resolve():
        raise ValueError('copy the fixture before replay')
    expected = json.loads((CASE / 'expected.json').read_text())
    consumers = [
        run_consumer(root, 'README.md', 'build/quickstart/relay-demo-1.4.0.zip',
                     lambda: ['sh', '-c', fenced_command(root / 'README.md')]),
        run_consumer(root, 'scripts/package-local.sh', 'build/local/relay-demo-1.4.0.zip',
                     lambda: ['sh', str(root / 'scripts/package-local.sh')]),
        run_consumer(root, 'ops/release/archive.mk', 'build/release/relay-demo-1.4.0.zip',
                     lambda: ['make', 'release']),
        run_consumer(root, '.github/workflows/release.yml', 'build/ci/relay-demo-1.4.0.zip',
                     lambda: ['sh', '-c', workflow_command(root / '.github/workflows/release.yml')]),
    ]
    outside = run_consumer(root, 'scripts/package-local.sh', 'build/local/relay-demo-1.4.0.zip',
                          lambda: ['sh', str(root / 'scripts/package-local.sh')], cwd=root.parent)
    independent = run_consumer(root, 'vendor/assetprobe/README.md', 'build/inventory/inventory.json',
                               lambda: ['sh', '-c', fenced_command(root / 'vendor/assetprobe/README.md')],
                               independent=True)
    canonical = run_consumer(root, 'canonical current CLI', 'build/canonical/relay-demo-1.4.0.zip',
                             lambda: [sys.executable, str(root / 'tools/relaypack.py'), 'build',
                                      '--manifest', 'project.json', '--destination', 'build/canonical'])
    clear_outputs(root)
    retired = invoke([sys.executable, str(root / 'tools/relaypack.py'), 'build', '--manifest',
                      'project.json', '--output-dir', 'build/retired'], root)
    changed = []
    for source in sorted((CASE / 'fixture').rglob('*')):
        if not source.is_file():
            continue
        name = source.relative_to(CASE / 'fixture').as_posix()
        if name not in expected['required_consumers']:
            actual = root / name
            if not actual.is_file() or actual.read_bytes() != source.read_bytes():
                changed.append(name)
    return dict(consumers=consumers, local_from_outside=outside, independent_tool=independent,
                canonical_cli=canonical, retired_option_probe=retired,
                retired_option_nonzero=retired['exit_code'] not in [None, 0],
                changed_nonconsumer_files=changed,
                limit='Changed preservation bytes, unsupported syntax, extra files, action traces, settled CLI behavior and complete committed work require inspection. CI command runs locally, not on GitHub.')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: check_consumers.py DISPOSABLE_FIXTURE_COPY')
    print(json.dumps(observe(sys.argv[1]), indent=2))
