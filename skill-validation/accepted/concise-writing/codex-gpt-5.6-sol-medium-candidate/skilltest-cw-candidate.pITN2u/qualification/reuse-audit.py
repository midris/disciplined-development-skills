import json,sys,re,hashlib,subprocess
from pathlib import Path
from collections import defaultdict
source="import ast,hashlib,json,os,subprocess,sys\nfrom pathlib import Path\nfrom skilltest.config import load_config\nfrom skilltest.providers import ProviderRequest,_arguments\nroot=Path.cwd(); scratch=Path('/private/tmp/skilltest-cw-baseline.bOn8Dx')\nattempt=scratch/'attempts'/sys.argv[1]\nbundle=Path((attempt/'command-stdout.txt').read_text().strip())\nassert bundle.is_relative_to(scratch/'runs/skilltest-runs') and bundle.is_dir()\ncfgpath=root/'skill-validation/pilot/efforts/medium'/(sys.argv[1].split('-',2)[2]+'.json')\ncfg=load_config(cfgpath)\nsha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()\nfor p in [cfgpath,cfg.prompt,cfg.prompt.parent/'rubric.md']+[f.source for f in cfg.fixtures]:\n assert subprocess.check_output(['git','show','dfd638ce5c1ac5f654110d05ce9138e5384d6afc:'+str(p.relative_to(root))])==p.read_bytes()\nr=json.loads((bundle/'result.json').read_text()); e=r['execution']\nassert r['status']=='COMPLETED' and r['infrastructure_error'] is None\nassert e['exit_code']==0 and e['invocation_started'] and not e['timed_out']\nassert (e['provider'],e['model'],e['effort'])==('codex','gpt-5.6-sol','medium')\nassert r['test']['id']==cfg.id and (bundle/'config.json').read_bytes()==cfg.config_bytes\nfor a in r['artifacts'].values():\n if 'entries' in a:\n  actual=set()\n  for p in (bundle/a['path']).rglob('*'):\n   assert not p.is_symlink()\n   actual.add(str(p.relative_to(bundle/a['path'])))\n  assert actual=={f['path'] for f in a['entries']}\n  for f in a['entries']:\n   assert f['type'] in ('file','directory')\n   if f['type']=='file': assert sha(bundle/a['path']/f['path'])==f['sha256']\n else: assert sha(bundle/a['path'])==a['sha256']\nassert (bundle/'prompt-template.txt').read_bytes()==cfg.prompt.read_bytes()\nfor f in cfg.fixtures: assert (bundle/'workspace/fixture'/f.target).read_bytes()==f.source.read_bytes()\nlog=(bundle/'runner.log').read_text()\nhashes=json.loads(next(l.split('pre-launch input SHA-256: ',1)[1] for l in log.splitlines() if 'pre-launch input SHA-256: ' in l))\nfor rel,digest in hashes.items(): assert sha(bundle/rel)==digest\nruntime=Path(next(l.split('manual recovery if interrupted): ',1)[1] for l in log.splitlines() if 'manual recovery if interrupted): ' in l))\nassert runtime.parent==scratch/'runs' and not os.path.lexists(runtime)\nassert 'cleanup failed' not in log and log.rstrip().endswith('COMPLETED')\nargv=ast.literal_eval(next(l.split('provider arguments: ',1)[1] for l in log.splitlines() if 'provider arguments: ' in l))\nreq=ProviderRequest(bundle/'workspace',(bundle/'prompt.txt').read_bytes(),bundle/'final.txt',e['provider'],e['model'],e['effort'])\nassert argv==_arguments(req,executable='/opt/homebrew/bin/codex')\nfiles={f['path'] for f in r['artifacts']['fixture']['entries'] if f['type']=='file'}\nexpected={str(f.target) for f in cfg.fixtures}|{'.git/HEAD','.git/config'}\nif 'cw18-discovery' in sys.argv[1]: expected.add('clothing-swap-guide.md')\nassert files==expected,(files-expected,expected-files)\nassert r['artifacts']['evidence']['empty']\nevents=[json.loads(l) for l in (bundle/'stdout.txt').read_text().splitlines() if l.strip()]\nassert events[0]['type']=='thread.started' and events[-1]['type']=='turn.completed'\nassert not any(x['type'] in ('turn.failed','error') for x in events)\nmessages=[x['item']['text'] for x in events if x['type']=='item.completed' and x['item']['type']=='agent_message']\nassert messages[-1].strip()==(bundle/'final.txt').read_text().strip()\nfor name in ['cli-version.txt','cli-sha256.txt']:\n assert (attempt/name).read_bytes()==(Path('/private/tmp/skilltest-cw-catalog-qualification.YiAoRu')/name).read_bytes()\n"
seen=set(); groups=defaultdict(lambda:dict(PASS=0,FAIL=0,INCONCLUSIVE=0,evaluable=0,fidelity_fail=0))
total=0
for package,expected in [('/private/tmp/skilltest-cw-baseline.ksDeiD',18),('/private/tmp/skilltest-cw-baseline.bOn8Dx',81)]:
 p=Path(package); attempts=sorted(p.glob('attempts/*/worksheet.md'))
 assert len(attempts)==expected
 records=[]
 for w in attempts:
  aid=w.parent.name; sys.argv=['audit',aid]
  ns={}
  exec(compile(source.replace('/private/tmp/skilltest-cw-baseline.bOn8Dx',package),'<per-record-audit>','exec'),ns)
  bundle=ns['bundle']; record=ns['r']; assert bundle not in seen;seen.add(bundle)
  records.append(record)
  body=w.read_text(); verdict=re.search(r'\| Overall verdict \| (PASS|FAIL|INCONCLUSIVE) \|',body)[1]
  fidelity=body.split('## Task fidelity')[1].split('## Readability')[0]
  label=aid.split('-',2)[2]; g=groups[label];g[verdict]+=1;g['evaluable']+=verdict!='INCONCLUSIVE';g['fidelity_fail']+='| FAIL |' in fidelity
  for target in re.findall(r'^\[[^\]]+\]: (.+)$',body,re.M): assert (w.parent/target).exists()
  for target in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',body):
   if '://' not in target: assert (w.parent/target.split('#')[0]).exists(),target
  total+=1
 records.sort(key=lambda r:r['started_at'])
 assert all(a['finished_at']<=b['started_at'] for a,b in zip(records,records[1:]))
 assert set((p/'runs/skilltest-runs').iterdir())=={Path((w.parent/'command-stdout.txt').read_text().strip()) for w in attempts}
 assert not list((p/'runs').glob('skilltest-codex-*'))
assert total==99 and len(groups)==33 and all(sum(g[k] for k in ['PASS','FAIL','INCONCLUSIVE'])==3 for g in groups.values())
s=Path('/private/tmp/skilltest-cw-baseline.bOn8Dx')
assert hashlib.sha256((s/'approval-commands.md').read_bytes()).hexdigest()=='49c8b1e389600e1aa7a9ea31c8930d92adac0a77060106bc93bdf915982a6c2f'
assert subprocess.check_output(['git','rev-parse','HEAD']).decode().strip()=='dfd638ce5c1ac5f654110d05ce9138e5384d6afc'
print(json.dumps(dict(observations=total,conditions=len(groups),groups=dict(sorted(groups.items())),all_artifact_hashes_and_protected_inputs=True,exact_invocations_and_cli_captures=True,complete_traces=True,serial_execution=True,owned_cleanup=True,approval_document_unchanged=True,frozen_subject_inputs_unchanged=True),indent=2))

