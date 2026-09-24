"""Installed-policy login-shell runtime selection; no model calls or real auth."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import tomllib

import pytest

from skilltest.codex_runtime import CodexRuntime
from skilltest.providers import ProviderRequest, _arguments


@pytest.mark.parametrize('mode', ['workspace-write', 'read-only'])
def test_login_shell_preserves_prepared_python_and_git(mode, monkeypatch):
    destination = os.environ.get('SKILLTEST_SANDBOX_EVIDENCE_DIR')
    if not destination or sys.platform != 'darwin':
        pytest.skip('set SKILLTEST_SANDBOX_EVIDENCE_DIR on macOS')
    with tempfile.TemporaryDirectory(prefix='login-shell-') as folder:
        root = Path(folder).resolve()
        fixture = root / 'workspace/fixture'
        fixture.mkdir(parents=True)
        (root / 'workspace/evidence').mkdir()
        profile = root / 'auth'
        profile.mkdir()
        (profile / 'auth.json').write_text('{"test":"surrogate"}')
        monkeypatch.setenv('CODEX_HOME', str(profile))
        monkeypatch.setattr(CodexRuntime, '_check_login', lambda *args: None)
        runtime = CodexRuntime(lambda _: None)
        try:
            runtime.prepare(fixture)
            request = ProviderRequest(fixture.parent, b'unused', root/'final.txt', 'codex', 'unused', 'low', permissions=mode)
            argv = _arguments(request, executable=runtime.executable,
                              scratch_dir=runtime.root/'tmp', shell_path=runtime.environment['PATH'])
            overrides = [argv[i+1] for i, value in enumerate(argv) if value == '-c']
            config = tomllib.loads('\n'.join(overrides))
            env = runtime.environment | config['shell_environment_policy']['set']
            command = [runtime.executable, 'sandbox', '-P', config['default_permissions'], '-C', str(fixture)]
            for override in overrides:
                command += ['-c', override]
            command += ['--', '/bin/zsh', '-lc', 'command -v python3; python3 --version; command -v git; git --version']
            result = subprocess.run(command, cwd=fixture, env=env, capture_output=True, text=True, timeout=60)
            expected = {name: shutil.which(name, path=runtime.environment['PATH']) for name in ('python3', 'git')}
            evidence = Path(destination) / f'login-shell-{mode}.json'
            evidence.parent.mkdir(parents=True, exist_ok=True)
            evidence.write_text(json.dumps(dict(command=command, expected=expected,
                stdout=result.stdout, stderr=result.stderr, returncode=result.returncode, provider_calls=0), indent=2)+'\n')
            assert result.returncode == 0, result.stderr
            lines = result.stdout.splitlines()
            assert lines[0] == expected['python3'], result.stdout
            assert lines[2] == expected['git'], result.stdout
            assert tuple(map(int, lines[1].split()[1].split('.')[:2])) >= (3, 11), result.stdout
        finally:
            assert runtime.cleanup() is None
