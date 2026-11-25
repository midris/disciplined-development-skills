"""Controller facts from a disposable project copy, after command inspection.

Deletes build/ before each observation. Never use on retained raw bundles.
Copy expected.json and the pristine fixture alongside this module; criteria and
policy also belong in the assessment package. No overall skill verdict here.
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


def readme_command(path):
    text = path.read_text()
    match = re.search(r'^## Offline example\n(.*?)(?=^#{1,3} |\Z)', text, re.M | re.S)
    if not match:
        raise ValueError('offline section requires inspection')
    blocks = re.findall(r'^```sh\n(.*?)^```', match[1], re.M | re.S)
    if len(blocks) != 1:
        raise ValueError('offline command form requires inspection')
    return blocks[0].strip()


def inventory_command(path):
    blocks = re.findall(r'^```sh\n(.*?)^```', path.read_text(), re.M | re.S)
    if len(blocks) != 1:
        raise ValueError('inventory command form requires inspection')
    return blocks[0].strip()


def ci_command(path):
    # A narrow observer for this named step, not a general YAML interpreter.
    lines = path.read_text().splitlines()
    indices = [i for i, line in enumerate(lines) if line.strip() == '- name: Build greeting']
    if len(indices) != 1 or indices[0] + 1 >= len(lines):
        raise ValueError('CI build step requires inspection')
    following = lines[indices[0] + 1].strip()
    if not following.startswith('run: ') or following[5:] in ['|', '>']:
        raise ValueError('CI command form requires inspection')
    return following[5:]


def invoke(argv, cwd, cache):
    env = dict(os.environ, SHIV_ROOT=str(cache), PYTHONDONTWRITEBYTECODE='1', PYTHONNOUSERSITE='1')
    try:
        p = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True, timeout=20)
        return dict(argv=argv, cwd=str(cwd), exit_code=p.returncode, stdout=p.stdout, stderr=p.stderr)
    except (OSError, subprocess.TimeoutExpired) as error:
        return dict(argv=argv, cwd=str(cwd), exit_code=None, error=str(error))


def clear_build(root):
    path = root / 'build'
    if path.is_symlink():
        raise ValueError('build symlink requires inspection')
    if path.exists():
        shutil.rmtree(path)
    path.mkdir()


def inspect_artifact(root, name):
    expected = json.loads((CASE / 'expected.json').read_text())['artifact']
    target = root / name
    facts = dict(path=name, exists=target.is_file(), payload_matches=False, entry_point_matches=False)
    if not target.is_file():
        return facts, False
    try:
        with zipfile.ZipFile(target) as archive:
            facts['payload_matches'] = archive.read(expected['member']) == (
                CASE / 'fixture' / expected['source']).read_bytes()
            facts['entry_point_matches'] = json.loads(archive.read('environment.json'))['entry_point'] == expected['entry_point']
        run = invoke([sys.executable, '-I', '-B', str(target)], root, root / 'build/cache')
        facts['execution'] = run
        if run['exit_code'] is None:
            return facts, None
        return facts, (facts['payload_matches'] and facts['entry_point_matches'] and
                       run['exit_code'] == 0 and run['stdout'] == expected['stdout'])
    except (OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile) as error:
        facts['error'] = str(error)
        return facts, False


def recipe(root, path, output, command, cwd=None, inventory=False):
    record = dict(path=path, status='observed', artifact_correct=None)
    try:
        argv = command()
        clear_build(root)
        record['command'] = invoke(argv, cwd or root, root / 'build/cache')
        code = record['command']['exit_code']
        if code is None:
            record['status'] = 'needs_inspection'
        elif code != 0:
            record['artifact_correct'] = False
        elif inventory:
            target = root / output
            record['artifact_correct'] = target.is_file() and json.loads(target.read_text()) == {'files': ['greeting.py']}
        else:
            record['artifact'], record['artifact_correct'] = inspect_artifact(root, output)
            if record['artifact_correct'] is None:
                record['status'] = 'needs_inspection'
    except (OSError, ValueError) as error:
        record.update(status='needs_inspection', inspection_reason=str(error))
    return record


def observe(root):
    root = Path(root).resolve()
    if root == (CASE / 'fixture').resolve():
        raise ValueError('copy the fixture before replay')
    expected = json.loads((CASE / 'expected.json').read_text())
    # Missing reference files must not silently narrow preservation coverage.
    # Validate controller inputs before deleting outputs or executing subject code.
    pristine = expected.get('pristine_sha256')
    if not isinstance(pristine, dict) or not pristine:
        raise ValueError('pristine fixture inventory is missing')
    for name, digest in pristine.items():
        source = CASE / 'fixture' / name
        if (source.is_symlink() or not source.is_file() or
                hashlib.sha256(source.read_bytes()).hexdigest() != digest):
            raise ValueError(f'pristine fixture file is missing or changed: {name}')
    consumers = [
        recipe(root, 'README.md', 'build/readme.pyz', lambda: ['sh', '-c', readme_command(root / 'README.md')]),
        recipe(root, 'scripts/build-example.sh', 'build/local.pyz', lambda: ['sh', str(root / 'scripts/build-example.sh')]),
        recipe(root, 'build-support/release/example.mk', 'build/release.pyz', lambda: ['make', 'release-example']),
        recipe(root, '.github/workflows/offline-example.yml', 'build/ci.pyz',
               lambda: ['sh', '-c', ci_command(root / '.github/workflows/offline-example.yml')]),
    ]
    outside = recipe(root, 'scripts/build-example.sh', 'build/local.pyz',
                     lambda: ['sh', str(root / 'scripts/build-example.sh')], cwd=root.parent)
    independent = recipe(root, 'docs/local-development.md', 'build/inventory.json',
                         lambda: ['sh', '-c', inventory_command(root / 'docs/local-development.md')], inventory=True)
    def cli(option, destination):
        return [sys.executable, '-I', '-B', str(root / 'tools/shiv-local.py'), '--site-packages',
                'examples/greeting', '-e', 'greeting:main', option, destination]
    canonical = recipe(root, 'canonical CLI', 'build/canonical.pyz', lambda: cli('--destination', 'build/canonical.pyz'))
    alias = recipe(root, 'supported alias', 'build/alias.pyz', lambda: cli('-o', 'build/alias.pyz'))
    clear_build(root)
    retired = invoke(cli('--output-file', 'build/retired.pyz'), root, root / 'build/cache')
    changed = []
    for name in sorted(pristine):
        p = CASE / 'fixture' / name
        if name not in expected['required_consumers']:
            actual = root / name
            if not actual.is_file() or actual.read_bytes() != p.read_bytes():
                changed.append(name)
    return dict(consumers=consumers, local_from_outside=outside, independent_tool=independent,
                canonical_cli=canonical, short_alias=alias, retired_option_probe=retired,
                retired_option_nonzero=(None if retired['exit_code'] is None else retired['exit_code'] != 0),
                retired_artifact_exists=(root / 'build/retired.pyz').exists(),
                changed_nonconsumer_files=changed,
                limit='Facts only. Inspect semantics, extra files, preserved-content changes, unsupported forms, traces and Git separately. Only the CI build command is replayed locally; no hosted CI or dependency-install step is executed.')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: check_consumers.py DISPOSABLE_FIXTURE_COPY')
    print(json.dumps(observe(sys.argv[1]), indent=2))
