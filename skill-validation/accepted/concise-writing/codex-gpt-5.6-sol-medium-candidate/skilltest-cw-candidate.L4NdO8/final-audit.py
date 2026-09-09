import hashlib,json,re,subprocess,sys
from pathlib import Path
from collections import defaultdict

root=Path.cwd(); s=Path('/private/tmp/skilltest-cw-candidate.L4NdO8')
assert hashlib.sha256((s/'approval-commands.md').read_bytes()).hexdigest()=='21b35b9dc5ea062f9f31af3fe92e0d8bc8186769f680070fb992a1fec6625c6b'
rows=json.loads((s/'command-rows.json').read_text()); assert len(rows)==66
ledger=(s/'summary.md').read_text(); assert '| NOT RUN |' not in ledger
assert not subprocess.check_output(['git','status','--porcelain'])
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()=='595f8e2bce0a62c5d4143ffebcdcf30cf8422b0d'
out=s/'final-audit'; out.mkdir(exist_ok=True)
counts=defaultdict(lambda:dict(PASS=0,FAIL=0,INCONCLUSIVE=0,fidelity_fail=0))
records=[]; bundles=set(); links=0
for row in rows:
 a=s/'attempts'/row['attempt']; b=Path((a/'command-stdout.txt').read_text().strip())
 assert b not in bundles; bundles.add(b)
 r=subprocess.run([sys.executable,str(s/'audit-run.py'),row['attempt']],capture_output=True,text=True)
 (out/(row['attempt']+'.txt')).write_text(r.stdout+r.stderr)
 assert r.returncode==0,(row['order'],r.stderr)
 w=(a/'worksheet.md').read_text()
 verdict=re.search(r'^\| Overall verdict \| (PASS|FAIL|INCONCLUSIVE) \|$',w,re.M)[1]
 assert '| Provider CLI version | codex-cli 0.153.4' in w
 assert '| Scenario purpose |  |' not in w
 for section in ['Semantic behavior','Deterministic protocol','Task fidelity','Readability']:
  assert '## '+section+'\n' in w
 fidelity=w.split('## Task fidelity\n',1)[1].split('\n## ',1)[0]
 ff=bool(re.search(r'\| FAIL \|',fidelity))
 assert f'[Primary {verdict}; fidelity '+('FAIL' if ff else 'PASS')+f'](attempts/{row["attempt"]}/worksheet.md)' in ledger
 for target in re.findall(r'\]\(([^)]+)\)',w)+re.findall(r'^\[[^\]]+\]: (.+)$',w,re.M):
  target=target.strip('<>').split('#',1)[0]
  if not target or '://' in target:continue
  target=re.sub(r':\d+$','',target)
  assert (a/target).exists(),(row['attempt'],target)
  links+=1
 for tag in re.findall(r'\]\[([^\]]+)\]',w):assert re.search(r'^\['+re.escape(tag)+r'\]: ',w,re.M)
 counts[row['id']][verdict]+=1; counts[row['id']]['fidelity_fail']+=ff
 records.append(dict(order=row['order'],attempt=row['attempt'],id=row['id'],repetition=row['repetition'],bundle=str(b),primary=verdict,fidelity='FAIL' if ff else 'PASS',worksheet_sha256=hashlib.sha256(w.encode()).hexdigest()))
assert {p for p in (s/'runs/skilltest-runs').iterdir()}==bundles
assert {p.name for p in (s/'runs').iterdir()}=={'skilltest-runs'}
assert all(c['PASS']+c['FAIL']+c['INCONCLUSIVE']==3 for c in counts.values()) and len(counts)==22
baseline=root/'skill-validation/accepted/concise-writing/codex-gpt-5.6-sol-medium'
hashcheck=subprocess.run(['shasum','-a','256','-c','SHA256SUMS'],cwd=baseline,capture_output=True,text=True)
(out/'accepted-archive-hashes.txt').write_text(hashcheck.stdout+hashcheck.stderr)
assert hashcheck.returncode==0
baseline_counts={}
for p in sorted(baseline.glob('*/summary.md')):
 baseline_counts[p.parent.name]={}
 for condition,pa,fa,inc,ev,ff in re.findall(r'^\| ([a-z-]+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$',p.read_text(),re.M):
  baseline_counts[p.parent.name][condition]=dict(PASS=int(pa),FAIL=int(fa),INCONCLUSIVE=int(inc),evaluable=int(ev),fidelity_fail=int(ff))
assert len(baseline_counts)==22
assert sum(v['evaluable'] for cs in baseline_counts.values() for v in cs.values())==99
print(json.dumps(dict(status='PASS',fresh_observations=len(records),conditions=len(counts),worksheet_links=links,counts=counts,records=records,accepted_baseline_counts=baseline_counts),indent=2))
