"""Opt-in real permission checks with local commands, no auth or model calls."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import tomllib

import pytest

from skilltest.claude_runtime import ClaudeRuntime
from skilltest.providers import ProviderRequest, _arguments


# Break: either adapter grants writes to evidence, Git or paths outside its fixture;
# shell writes and symlink aliases must obey the same boundary as file tools.
@pytest.mark.parametrize('provider', ['codex', 'claude'])
def test_read_only_sandbox_denies_mutations_and_returns_output(provider, monkeypatch):
    destination = os.environ.get('SKILLTEST_SANDBOX_EVIDENCE_DIR')
    if not destination or sys.platform != 'darwin':
        pytest.skip('set SKILLTEST_SANDBOX_EVIDENCE_DIR on macOS for retained qualification')
    executable = shutil.which(provider)
    assert executable, f'{provider} must be installed'
    root = Path(tempfile.mkdtemp(prefix=f'{provider}-read-only-', dir=destination)).resolve()
    fixture, evidence = root/'workspace/fixture', root/'workspace/evidence'
    for path in (fixture, evidence, root/'home', root/'profile', root/'tmp'):
        path.mkdir(parents=True)
    protected = [fixture/'input.txt', evidence/'trace.txt', root/'outside.txt']
    for path in protected:
        path.write_text('original\n')
    (fixture/'alias').symlink_to(root/'outside.txt')
    env = {'HOME': str(root/'home'), 'USER': 'fixture', 'CODEX_HOME': str(root/'profile'),
           'TMPDIR': str(root/'tmp'), 'PYTHONDONTWRITEBYTECODE': '1',
           'PATH': f'{Path(executable).parent}:/usr/bin:/bin:/usr/sbin:/sbin',
           'GIT_CONFIG_NOSYSTEM': '1', 'GIT_CONFIG_GLOBAL': os.devnull}
    request = ProviderRequest(fixture.parent, b'unused', root/'final.txt', provider,
                              'gpt-5.6-sol' if provider == 'codex' else 'sonnet', 'low',
                              permissions='read-only')
    argv = _arguments(request, executable=executable)
    (root/'provider-arguments.json').write_text(json.dumps(argv, indent=2)+'\n')
    runtime = None
    if provider == 'codex':
        subprocess.run(['/usr/bin/git', 'init', '--quiet', '--template=', str(fixture)],
                       env=env, check=True, capture_output=True, timeout=30)
        overrides = [argv[i+1] for i,a in enumerate(argv) if a == '-c']
        config = tomllib.loads('\n'.join(overrides))
        command = [executable, 'sandbox', '-P', config['default_permissions'], '-C', str(fixture)]
        for value in overrides:
            command.extend(['-c', value])
        command.append('--')
    else:
        for name, value in env.items():
            monkeypatch.setenv(name, value)
        monkeypatch.setattr(tempfile, 'tempdir', str(root/'tmp'))
        # Only subscription status is replaced; actual runtime policy and Git setup run.
        monkeypatch.setattr(ClaudeRuntime, '_check_login', lambda *args: None)
        runtime = ClaudeRuntime(lambda _: None, permissions='read-only')
        runtime.prepare(fixture)
        command = runtime.prefix.copy()
        env = runtime.environment | {'PYTHONDONTWRITEBYTECODE': '1'}
        (root/'policy.sb').write_bytes(Path(runtime.prefix[2]).read_bytes())
    probe = root/'probe.py'
    probe.write_text(r'''
import errno, json, subprocess, sys
from pathlib import Path
fixture, evidence, outside = map(Path, sys.argv[1:4])
for path in [fixture/'input.txt', evidence/'trace.txt', outside]:
    assert path.read_text() == 'original\n'
denied = []
def must_deny(label, action):
    try:
        action()
    except OSError as error:
        assert error.errno in (errno.EPERM, errno.EACCES), (label, repr(error))
        denied.append(label)
    else:
        raise AssertionError('write permitted: ' + label)
for path in [fixture/'input.txt', evidence/'trace.txt', outside, fixture/'alias']:
    must_deny(str(path)+' overwrite', lambda p=path: p.write_text('changed'))
    must_deny(str(path)+' delete', lambda p=path: p.unlink())
    must_deny(str(path)+' rename', lambda p=path: p.rename(p.with_name(p.name+'.moved')))
for directory in [fixture, evidence, outside.parent]:
    must_deny(str(directory)+' create', lambda d=directory: (d/'created').mkdir())
if len(sys.argv) == 5:
    scratch = Path(sys.argv[4])
    (scratch/'runtime.txt').write_text('private bookkeeping')
    (scratch/'escape').symlink_to(outside)
    must_deny('private scratch symlink escape', lambda: (scratch/'escape').write_text('changed'))
for args in [('add','input.txt'), ('config','test.write','forbidden')]:
    result = subprocess.run(['/usr/bin/git', *args], cwd=fixture, capture_output=True, text=True)
    assert result.returncode != 0, args
    assert 'permitted' in result.stderr.lower() or 'denied' in result.stderr.lower(), result.stderr
    denied.append('git ' + args[0])
print(json.dumps({'status':'PASS', 'denied':denied, 'assessment':'read evidence successfully'}))
''')
    command.extend([sys.executable, str(probe), str(fixture), str(evidence), str(root/'outside.txt')])
    if runtime:
        command.append(runtime.environment['TMPDIR'])
    (root/'sandbox-command.json').write_text(json.dumps(command, indent=2)+'\n')
    try:
        result = subprocess.run(command, cwd=fixture, env=env, capture_output=True, text=True, timeout=60)
        (root/'stdout.txt').write_text(result.stdout)
        (root/'stderr.txt').write_text(result.stderr)
        version = subprocess.run([executable, '--version'], capture_output=True, text=True, timeout=30)
        (root/'result.json').write_text(json.dumps({'exit_code':result.returncode, 'provider_calls':0,
            'version':version.stdout.strip(), 'cli_sha256':hashlib.sha256(Path(executable).read_bytes()).hexdigest()}, indent=2)+'\n')
        assert result.returncode == 0, f'{root}: {result.stderr}\n{result.stdout}'
        assert json.loads(result.stdout)['status'] == 'PASS'
        assert all(p.read_text() == 'original\n' for p in protected)
        assert not (root/'profile/auth.json').exists()
    finally:
        if runtime:
            assert runtime.cleanup() is None
    print(f'Retained read-only qualification: {root}')
