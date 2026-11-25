import ast,hashlib,json,os,re,subprocess,sys
from pathlib import Path
from skilltest.config import load_config
from skilltest.providers import ProviderRequest,_arguments
root=Path.cwd(); scratch=Path('/private/tmp/skilltest-cw-candidate.L4NdO8')
attempt=scratch/'attempts'/sys.argv[1]
bundle=Path((attempt/'command-stdout.txt').read_text().strip())
assert bundle.is_relative_to(scratch/'runs/skilltest-runs') and bundle.is_dir()
row=next(x for x in json.loads((scratch/'command-rows.json').read_text()) if x['attempt']==sys.argv[1])
cfgpath=root/row['config']
cfg=load_config(cfgpath)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert not subprocess.check_output(['git','status','--porcelain'])
for p in [cfgpath,cfg.prompt,cfg.prompt.parent/'rubric.md']+[f.source for f in cfg.fixtures]:
 assert subprocess.check_output(['git','show','595f8e2bce0a62c5d4143ffebcdcf30cf8422b0d:'+str(p.relative_to(root))])==p.read_bytes()
r=json.loads((bundle/'result.json').read_text()); e=r['execution']
assert r['status']=='COMPLETED' and r['infrastructure_error'] is None
assert e['exit_code']==0 and e['invocation_started'] and not e['timed_out']
assert (e['provider'],e['model'],e['effort'])==('codex','gpt-5.6-sol','medium')
assert r['test']['id']==cfg.id and (bundle/'config.json').read_bytes()==cfg.config_bytes
for a in r['artifacts'].values():
 if 'entries' in a:
  actual=set()
  for p in (bundle/a['path']).rglob('*'):
   assert not p.is_symlink()
   actual.add(str(p.relative_to(bundle/a['path'])))
  assert actual=={f['path'] for f in a['entries']}
  for f in a['entries']:
   assert f['type'] in ('file','directory')
   if f['type']=='file': assert sha(bundle/a['path']/f['path'])==f['sha256']
 else: assert sha(bundle/a['path'])==a['sha256']
assert (bundle/'prompt-template.txt').read_bytes()==cfg.prompt.read_bytes()
for f in cfg.fixtures: assert (bundle/'workspace/fixture'/f.target).read_bytes()==f.source.read_bytes()
log=(bundle/'runner.log').read_text()
hashes=json.loads(next(l.split('pre-launch input SHA-256: ',1)[1] for l in log.splitlines() if 'pre-launch input SHA-256: ' in l))
for rel,digest in hashes.items(): assert sha(bundle/rel)==digest
runtime=Path(next(l.split('manual recovery if interrupted): ',1)[1] for l in log.splitlines() if 'manual recovery if interrupted): ' in l))
assert runtime.parent==scratch/'runs' and not os.path.lexists(runtime)
assert 'cleanup failed' not in log and log.rstrip().endswith('COMPLETED')
argv=ast.literal_eval(next(l.split('provider arguments: ',1)[1] for l in log.splitlines() if 'provider arguments: ' in l))
req=ProviderRequest(bundle/'workspace',(bundle/'prompt.txt').read_bytes(),bundle/'final.txt',e['provider'],e['model'],e['effort'])
assert argv==_arguments(req,executable='/opt/homebrew/bin/codex')
files={f['path'] for f in r['artifacts']['fixture']['entries'] if f['type']=='file'}
expected={str(f.target) for f in cfg.fixtures}|{'.git/HEAD','.git/config'}
if 'cw18-discovery' in sys.argv[1]: expected.add('clothing-swap-guide.md')
assert files==expected,(files-expected,expected-files)
assert r['artifacts']['evidence']['empty']
events=[json.loads(l) for l in (bundle/'stdout.txt').read_text().splitlines() if l.strip()]
assert events[0]['type']=='thread.started' and events[-1]['type']=='turn.completed'
assert not any(x['type'] in ('turn.failed','error') for x in events)
messages=[x['item']['text'] for x in events if x['type']=='item.completed' and x['item']['type']=='agent_message']
assert messages[-1].strip()==(bundle/'final.txt').read_text().strip()
for name in ['cli-version.txt','cli-sha256.txt']:
 assert (attempt/name).read_bytes()==(Path('/private/tmp/skilltest-cw-candidate.pITN2u/qualification')/name).read_bytes()
print(json.dumps({'checks':'PASS','bundle':str(bundle),'runtime_absent':str(runtime),'fixture_files':len(cfg.fixtures),'events':len(events),'duration_seconds':r['duration_seconds']},indent=2))
print('FULL TRACE (exact supplied-file text replaced by a hash marker; every other byte/event retained below):')
for event in events:
 event=json.loads(json.dumps(event))
 item=event.get('item',{})
 if item.get('type')=='command_execution' and item.get('aggregated_output'):
  proofs=[]
  declared={str(f.target):f for f in cfg.fixtures}
  for start,end,path in re.findall(r"sed -n '([0-9]+),([0-9]+)p' '?(\.agents/skills/[A-Za-z0-9_./-]+)",item.get('command','')):
   if path not in declared: continue
   lines=declared[path].source.read_text().splitlines(keepends=True)
   part=''.join(lines[int(start)-1:int(end)])
   exact=bool(part) and part in item['aggregated_output']
   proofs.append(dict(path=path,first=int(start),last=min(int(end),len(lines)),total=len(lines),exact_returned=exact))
   if exact: item['aggregated_output']=item['aggregated_output'].replace(part,'<EXACT SUPPLIED LINES '+start+'-'+str(min(int(end),len(lines)))+' '+path+'>\n')
  if proofs: item['verified_read_ranges']=proofs
  for f in sorted(cfg.fixtures,key=lambda f:len(f.source.read_bytes()),reverse=True):
   content=f.source.read_text()
   if content and content in item['aggregated_output']:
    item['aggregated_output']=item['aggregated_output'].replace(content,'<FULL SUPPLIED FILE '+str(f.target)+' SHA256='+sha(f.source)+'>\n')
 print(json.dumps(event,ensure_ascii=False))
print('PROVIDER STDERR:');print((bundle/'stderr.txt').read_text())
print('COMMAND STDERR:');print((attempt/'command-stderr.txt').read_text())
