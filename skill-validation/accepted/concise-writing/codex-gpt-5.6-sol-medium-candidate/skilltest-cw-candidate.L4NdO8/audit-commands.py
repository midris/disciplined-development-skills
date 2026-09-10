"""Provider-free finite-command audit; allocates empty attempt directories only."""
from pathlib import Path
from collections import Counter
import hashlib,json,re,shlex,subprocess
from skilltest.config import load_config
ROOT=Path('/Users/simon/work/personal/disciplined-development-skills/.worktrees/cw-validation-design')
SCRATCH=Path('/private/tmp/skilltest-cw-candidate.L4NdO8')
REVISION='595f8e2bce0a62c5d4143ffebcdcf30cf8422b0d'
rows=json.loads((SCRATCH/'command-rows.json').read_text())
document=(SCRATCH/'approval-commands.md').read_text()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT).decode().strip()==REVISION
assert not subprocess.check_output(['git','status','--porcelain'],cwd=ROOT)
assert subprocess.check_output(['git','rev-list','--left-right','--count','HEAD...origin/feature/cw-validation-design'],cwd=ROOT).decode().strip()=='0\t0'
assert len(rows)==66 and [r['order'] for r in rows]==list(range(1,67))
assert re.findall(r'```sh\n([^`]+)\n```',document)==[r['command'] for r in rows]
mapping=(ROOT/'skill-validation/pilot/cw-catalog.md').read_text()
order=re.findall(r'\[candidate\]\((efforts/medium/cw-rewrite/[^)]+)\)',mapping)
assert len(order)==22
assert [r['config'] for r in rows]==['skill-validation/pilot/'+p for p in order]*3
assert Counter(r['config'] for r in rows)==Counter({r['config']:3 for r in rows})
attempts=[]
for n,row in enumerate(rows):
    assert row['repetition']==n//22+1
    config=load_config(ROOT/row['config']); attempt=SCRATCH/'attempts'/row['attempt']
    assert attempt.parent==SCRATCH/'attempts' and not attempt.exists()
    assert config.id==row['id'] and 'candidate' in config.id
    assert (config.execution.provider,config.execution.model,config.execution.effort)==('codex','gpt-5.6-sol','medium')
    assert config.prompt.parent==ROOT/row['scenario']
    for path,key in [(config.config_path,'config_sha256'),(config.prompt,'prompt_sha256'),(config.prompt.parent/'rubric.md','rubric_sha256')]:
        assert sha(path)==row[key]
        assert path.read_bytes()==subprocess.check_output(['git','show',REVISION+':'+str(path.relative_to(ROOT))],cwd=ROOT)
    for f in config.fixtures:
        assert f.source.read_bytes()==subprocess.check_output(['git','show',REVISION+':'+str(f.source.relative_to(ROOT))],cwd=ROOT)
    expected=['/usr/bin/env','TMPDIR='+str(SCRATCH/'runs'),'PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin',str(ROOT/'skill-validation/runner/.venv/bin/skilltest'),'run',str(ROOT/row['config']),'>',str(attempt/'command-stdout.txt'),'2>',str(attempt/'command-stderr.txt')]
    assert shlex.split(row['command'])==expected
    attempts.append(attempt)
assert len(set(attempts))==66 and not list((SCRATCH/'runs').iterdir())
for attempt in attempts: attempt.mkdir()
print(json.dumps(dict(result='PASS',provider_calls=0,commands=66,conditions=22,repetitions=3,provider='codex',model='gpt-5.6-sol',effort='medium',revision=REVISION,clean_and_pushed=True,empty_attempt_directories=66,approval_document_sha256=sha(SCRATCH/'approval-commands.md')),indent=2))
