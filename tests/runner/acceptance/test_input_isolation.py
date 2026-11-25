"""Shared installed-provider filesystem contract; no model calls or real credentials."""
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


@pytest.mark.parametrize('provider', ['codex', 'claude'])
@pytest.mark.parametrize('mode', ['workspace-write', 'read-only'])
def test_subject_cannot_read_controller_or_other_attempts(provider, mode, monkeypatch):
    # Break: broad inherited reads or an alias exposes another run; mutation modes
    # must still permit the actual Git/Python task and protect supplied evidence.
    destination = os.environ.get('SKILLTEST_SANDBOX_EVIDENCE_DIR')
    if not destination or sys.platform != 'darwin':
        pytest.skip('set SKILLTEST_SANDBOX_EVIDENCE_DIR on macOS')
    executable = shutil.which(provider)
    assert executable
    root = Path(tempfile.mkdtemp(prefix=f'{provider}-input-isolation-', dir=tempfile.gettempdir())).resolve()
    fixture, evidence = root/'workspace/fixture', root/'workspace/evidence'
    for p in (fixture, evidence, root/'home', root/'profile', root/'tmp', root/'other-run'):
        p.mkdir(parents=True)
    shared = Path(tempfile.mkdtemp(prefix="skilltest-outside-", dir="/private/tmp"))
    var_shared = Path(tempfile.mkdtemp(prefix="skilltest-outside-", dir="/private/var/tmp"))
    for directory in (shared, var_shared):
        (directory/"outside.txt").write_text("UNDECLARED_STUDY_MARKER")
    blocked = [root/'controller.txt', root/'other-run/final.txt', root/'home/private.txt', root/'home/.claude/settings.json',
               root/'home/Library/Keychains/other.txt']
    for p in blocked:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text('UNDECLARED_STUDY_MARKER')
    (fixture/'escape').symlink_to(root/'other-run', target_is_directory=True)
    (fixture/'input.txt').write_text('declared input')
    (evidence/'input.txt').write_text('declared evidence')
    env = {'HOME':str(root/'home'), 'USER':'fixture', 'CODEX_HOME':str(root/'profile'),
           'TMPDIR':str(root/'tmp'), 'PATH':f'{Path(executable).parent}:/usr/bin:/bin:/usr/sbin:/sbin',
           'GIT_CONFIG_NOSYSTEM':'1', 'GIT_CONFIG_GLOBAL':os.devnull, 'PYTHONDONTWRITEBYTECODE':'1'}
    runtime = None
    if provider == 'codex':
        subprocess.run(['/usr/bin/git','init','--quiet','--template=',str(fixture)],env=env,check=True)
        request = ProviderRequest(fixture.parent,b'unused',root/'final.txt',provider,'unused','low',permissions=mode)
        argv = _arguments(request,executable=executable,scratch_dir=root/"tmp", shell_path=env["PATH"])
        overrides = [argv[i+1] for i,a in enumerate(argv) if a=='-c']
        cfg = tomllib.loads('\n'.join(overrides))
        command = [executable,'sandbox','-P',cfg['default_permissions'],'-C',str(fixture)]
        for value in overrides:command += ['-c',value]
        command += ['--']
    else:
        for k,v in env.items():monkeypatch.setenv(k,v)
        monkeypatch.setattr(tempfile,'tempdir',str(root/'tmp'))
        monkeypatch.setattr(ClaudeRuntime,'_check_login',lambda *args:None)
        runtime = ClaudeRuntime(lambda _:None,permissions=mode)
        runtime.prepare(fixture)
        command = runtime.prefix.copy()
        env = runtime.environment | {'PYTHONDONTWRITEBYTECODE':'1'}
        (root/'policy.sb').write_bytes(Path(runtime.prefix[2]).read_bytes())
    # Inline code travels as argv, not through an undeclared controller file.
    probe = r'''
import errno,json,os,subprocess,sys
from pathlib import Path
fixture,evidence,root=map(Path,sys.argv[1:4]);mode=sys.argv[4];shared,var_shared=map(Path,sys.argv[5:7])
scratch=Path(os.environ['TMPDIR'])
(scratch/'bookkeeping.txt').write_text('private scratch')
assert (scratch/'bookkeeping.txt').read_text()=='private scratch'
assert (fixture/'input.txt').read_text()=='declared input'
assert (evidence/'input.txt').read_text()=='declared evidence'
denied=[]
paths=[root/'controller.txt',root/'other-run/final.txt',root/'home/private.txt',fixture/'escape/final.txt',shared/'outside.txt',var_shared/'outside.txt',root/'home/.claude/settings.json',root/'home/Library/Keychains/other.txt']
for p in list(paths):
 if str(p).startswith(('/private/tmp/', '/private/var/tmp/')):
  paths.append(Path(str(p).removeprefix('/private')))
for p in paths:
 try:p.read_text()
 except OSError as e:
  assert e.errno in (errno.EPERM,errno.EACCES), (str(p),repr(e));denied.append(str(p))
 else:raise AssertionError('outside read permitted: '+str(p))
 try:p.write_text('forbidden mutation')
 except PermissionError:pass
 else:raise AssertionError('outside write permitted: '+str(p))
# Reproduce cwd drift: broad search from the shared temp ancestor cannot return
# the marker from a sibling, regardless of whether traversal itself is rejected.
for outside in (root/'other-run', shared, var_shared):
 p=subprocess.run(['/usr/bin/grep','-R','UNDECLARED_STUDY_MARKER',str(outside)],cwd='/tmp',capture_output=True,text=True)
 assert p.returncode!=0 and 'UNDECLARED_STUDY_MARKER' not in p.stdout,p.stdout
if mode=='workspace-write':
 (fixture/'output.txt').write_text('correct edit');(evidence/'output.txt').write_text('observation')
 for args in [('add','input.txt','output.txt'),('-c','user.name=Fixture','-c','user.email=fixture@example.invalid','commit','--quiet','-m','fixture')]:
  p=subprocess.run(['/usr/bin/git',*args],cwd=fixture,capture_output=True,text=True);assert p.returncode==0,p.stderr
else:
 for p in (fixture/'input.txt',evidence/'input.txt'):
  try:p.write_text('mutation')
  except PermissionError:pass
  else:raise AssertionError('read-only write permitted')
print(json.dumps({'status':'PASS','denied_reads':denied,'mode':mode}))
'''
    command += [str(Path(shutil.which('python3', path='/opt/homebrew/bin:/usr/bin:/bin')).resolve()),'-c',probe,str(fixture),str(evidence),str(root),mode,str(shared),str(var_shared)]
    (root/'command.json').write_text(json.dumps(command,indent=2)+'\n')
    try:
        p=subprocess.run(command,cwd=fixture,env=env,capture_output=True,text=True,timeout=60)
        (root/'stdout.txt').write_text(p.stdout);(root/'stderr.txt').write_text(p.stderr)
        (root/'result.json').write_text(json.dumps({'returncode':p.returncode,'provider_calls':0})+'\n')
        assert p.returncode==0,f'{root}: {p.stderr}\n{p.stdout}'
    finally:
        if runtime:assert runtime.cleanup() is None
        shutil.rmtree(shared)
        shutil.rmtree(var_shared)
        shutil.copytree(root, Path(destination)/root.name, symlinks=True)
    print(f'Qualification evidence: {Path(destination)/root.name}')
