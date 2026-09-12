"""Claude runtime setup uses real scratch files and mocked process boundaries."""
import json
import os
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from skilltest import providers
from skilltest.runtime import PreparationError
from skilltest.providers import ProviderRequest, invoke_provider


@pytest.fixture
def setup(tmp_path, monkeypatch):
    runtime_type = getattr(providers, 'ClaudeRuntime', None)
    assert runtime_type is not None, 'Claude needs its controlled runtime'
    from skilltest import claude_runtime
    monkeypatch.setattr(claude_runtime.sys, 'platform', 'darwin')
    monkeypatch.setattr(claude_runtime.shutil, 'which', lambda name, **kw: '/stub/bin/' + name)
    login = Mock()
    monkeypatch.setattr(runtime_type, '_check_login', login)
    process = Mock(returncode=0, stdin=None, stdout=None, stderr=None)
    popen = Mock(return_value=process)
    monkeypatch.setattr(claude_runtime.subprocess, 'Popen', popen)
    communicate = Mock(return_value=(b'', b'', False))
    monkeypatch.setattr(runtime_type, 'communicate', communicate)
    workspace = tmp_path / 'workspace'
    (workspace / 'fixture').mkdir(parents=True)
    (workspace / 'evidence').mkdir()
    return SimpleNamespace(type=runtime_type, workspace=workspace, login=login,
                           popen=popen, communicate=communicate)


def test_runtime_preserves_shared_home_but_excludes_ambient_inputs(tmp_path, setup, monkeypatch):
    monkeypatch.setenv('ANTHROPIC_API_KEY', 'dummy-must-not-propagate')
    monkeypatch.setenv('CLAUDE_CONFIG_DIR', '/foreign-profile')
    monkeypatch.setenv('BASH_ENV', '/foreign-shell')
    home = Path(os.environ['HOME'])
    (home / '.claude').mkdir()
    settings = home / '.claude/settings.json'
    settings.write_text('host settings')
    roots = []
    for _ in range(2):
        runtime = setup.type(lambda _: None)
        try:
            runtime.prepare(setup.workspace / 'fixture')
            roots.append(runtime.root)
            env = runtime.environment
            assert env['HOME'] == str(home) and env['USER'] == os.environ['USER']
            assert env['GIT_CONFIG_NOSYSTEM'] == '1' and env['GIT_CONFIG_GLOBAL'] == os.devnull
            assert not {'ANTHROPIC_API_KEY', 'CLAUDE_CONFIG_DIR', 'BASH_ENV', 'CODEX_HOME'} & env.keys()
            assert 'CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT' not in env
            assert 'CLAUDE_CODE_DISABLE_BUNDLED_SKILLS' not in env
            assert runtime.root.stat().st_mode & 0o777 == 0o700
            assert Path(env['TMPDIR']).is_relative_to(runtime.root)
            assert not runtime.root.is_relative_to(setup.workspace)
            policy = Path(runtime.prefix[2]).read_text()
            assert '(deny file-write* (subpath ' + json.dumps(str(home)) + '))' in policy
            for path in ['CLAUDE.md', 'settings.json', 'settings.local.json', 'skills', 'commands', 'plugins', 'agents', 'projects']:
                assert json.dumps(str(home / '.claude' / path)) in policy
            assert not list(runtime.root.rglob('*auth*'))
            assert setup.popen.call_args.args[0] == ['/stub/bin/git', 'init', '--quiet', '--template=', str(setup.workspace / 'fixture')]
            assert setup.popen.call_args.kwargs['env']['GIT_CONFIG_GLOBAL'] == os.devnull
            setup.communicate.assert_called_with(setup.popen.return_value, None, 30)
        finally:
            assert runtime.cleanup() is None
        assert not runtime.root.exists() and settings.read_text() == 'host settings'
    assert roots[0] != roots[1]


@pytest.mark.parametrize('entry', ['CLAUDE.md', 'CLAUDE.local.md', '.claude/CLAUDE.md', '.claude/skills/ambient/SKILL.md'])
def test_ancestor_instructions_block_preparation_without_reading_contents(setup, entry):
    path = setup.workspace / entry
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('ambient must not enter subject')
    request = ProviderRequest(setup.workspace, b'prompt', setup.workspace.parent/'final.txt', 'claude', 'chosen', 'low')
    result = invoke_provider(request)
    assert result.preparation_error and not result.invocation_started
    setup.popen.assert_not_called()
    setup.login.assert_not_called()
    assert path.read_text() == 'ambient must not enter subject'


def test_existing_git_is_preserved_and_no_login_attempted(setup):
    git = setup.workspace / 'fixture/.git'
    git.write_text('owned by fixture')
    with pytest.raises(PreparationError):
        setup.type(lambda _: None).prepare(setup.workspace / 'fixture')
    assert git.read_text() == 'owned by fixture'
    setup.login.assert_not_called()


@pytest.mark.parametrize('failure', ['unsupported', 'missing-cli', 'login', 'git'])
def test_failed_setup_stops_before_model_and_cleans_runtime(tmp_path, setup, monkeypatch, failure):
    from skilltest import claude_runtime
    if failure == 'unsupported':
        monkeypatch.setattr(claude_runtime.sys, 'platform', 'linux')
    elif failure == 'missing-cli':
        monkeypatch.setattr(claude_runtime.shutil, 'which', lambda *a, **kw: None)
    elif failure == 'login':
        setup.login.side_effect = PreparationError('not logged in')
    else:
        setup.popen.return_value.returncode = 1
    request = ProviderRequest(setup.workspace, b'prompt', tmp_path/'final.txt', 'claude', 'chosen', 'low')
    result = invoke_provider(request)
    assert result.preparation_error and not result.invocation_started
    assert result.cleanup_error is None
    assert setup.popen.call_count <= 1
    assert not list(tmp_path.glob('skilltest-claude-*'))


@pytest.mark.parametrize('data, expected', [
    (b'{"loggedIn":true,"authMethod":"claude.ai"}', True),
    (b'{"loggedIn":false,"authMethod":"claude.ai"}', False),
    (b'{"loggedIn":"true","authMethod":"claude.ai"}', False),
    (b'{"loggedIn":true,"authMethod":"api_key"}', False),
    (b'[]', False), (b'not-json', False),
])
def test_auth_status_requires_subscription_without_retaining_payload(data, expected):
    from skilltest.claude_runtime import authenticated
    assert authenticated(bytearray(data)) is expected


# Break: HOME containment no longer stops before authentication and Git setup.
@pytest.mark.parametrize('inside_home', ['runtime', 'fixture'])
def test_home_containment_is_rejected_before_authentication(setup, monkeypatch, inside_home):
    import tempfile
    home = Path(os.environ['HOME'])
    fixture = setup.workspace/'fixture'
    if inside_home == 'runtime':
        monkeypatch.setattr(tempfile, 'tempdir', str(home))
    else:
        fixture = home/'fixture'
        fixture.mkdir()
    runtime = setup.type(lambda _: None, permissions='read-only')
    try:
        with pytest.raises(PreparationError, match='outside HOME'):
            runtime.prepare(fixture)
        setup.login.assert_not_called()
        setup.popen.assert_not_called()
    finally:
        assert runtime.cleanup() is None
