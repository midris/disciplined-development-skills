"""No-model regression for the shell failures observed in SSR expansion order 3."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import tomllib

import pytest

from skilltest.providers import ProviderRequest, _arguments


@pytest.mark.parametrize('login', [False, True])
def test_shell_git_and_heredoc_use_private_runtime(login):
    destination = os.environ.get('SKILLTEST_SANDBOX_EVIDENCE_DIR')
    if not destination or sys.platform != 'darwin':
        pytest.skip('set SKILLTEST_SANDBOX_EVIDENCE_DIR on macOS')
    root = Path(tempfile.mkdtemp(prefix='codex-shell-', dir=tempfile.gettempdir())).resolve()
    fixture = root/'workspace/fixture'
    for p in (fixture, root/'workspace/evidence', root/'tmp', root/'profile'):
        p.mkdir(parents=True)
    executable = shutil.which('codex')
    request = ProviderRequest(fixture.parent, b'unused', root/'final.txt', 'codex', 'unused', 'low')
    argv = _arguments(request, executable=executable, scratch_dir=root/'tmp', shell_path='/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin')
    overrides = [argv[i+1] for i,a in enumerate(argv) if a == '-c']
    cfg = tomllib.loads('\n'.join(overrides))
    shell_env = cfg['shell_environment_policy']['set']
    command = [executable, 'sandbox', '-P', cfg['default_permissions'], '-C', str(fixture)]
    for value in overrides:
        command += ['-c', value]
    # sandbox executes a raw argv, unlike exec's model shell tool. Feed that
    # tool's emitted environment explicitly; do not inherit test-only Git fixes.
    script = '''set -e
git init --quiet --template=
git config --local user.name Fixture
git config --local user.email fixture@example.invalid
cat <<'EOF' > output.txt
heredoc succeeded
EOF
git add output.txt
git commit --quiet -m probe
git status --porcelain
print -r -- "HOME=$HOME TMPDIR=$TMPDIR TMPPREFIX=$TMPPREFIX"
'''
    command += ['--', '/usr/bin/env', '-i', *[f'{k}={v}' for k,v in shell_env.items()], '/bin/zsh', '-lc' if login else '-c', script]
    result = subprocess.run(command, env={'HOME':str(root/'tmp'), 'CODEX_HOME':str(root/'profile'), 'PATH':shell_env['PATH']}, capture_output=True, text=True, timeout=60)
    (root/'command.json').write_text(json.dumps(command, indent=2)+'\n')
    (root/'result.json').write_text(json.dumps({'returncode':result.returncode, 'stdout':result.stdout, 'stderr':result.stderr, 'provider_calls':0}, indent=2)+'\n')
    shutil.copytree(root, Path(destination)/root.name)
    assert result.returncode == 0, f'{root}: {result.stderr}'
    # Apple Git selected by a login profile can warn about its denied optional
    # xcrun cache. Successful Git operations above establish task usability.
    assert "fatal:" not in result.stderr and "here document" not in result.stderr
    assert (fixture/'output.txt').read_text() == 'heredoc succeeded\n'
    assert f'HOME={root}/tmp' in result.stdout
    assert f'TMPPREFIX={root}/tmp/zsh' in result.stdout
