# Candidate input preparation command

One-shot provider-free preparation; do not replay into this evidence package.
Uses existing workspace helpers only; does not create an authenticated runtime or invoke a model.

```sh
TMPDIR=/private/tmp/skilltest-cw-candidate.pITN2u skill-validation/runner/.venv/bin/python - <<'PY'
from pathlib import Path
from dataclasses import replace
import hashlib,json,subprocess
from skilltest.config import load_config
from skilltest.workspace import create_run,prepare_workspace
root=Path.cwd(); base=root/'skill-validation/pilot/efforts/medium'; candidate=base/'cw-rewrite'
original=root/'skill-validation/pilot/inputs/dd/concise-writing/SKILL.md'
snapshot=root/'skill-validation/pilot/inputs/candidates/cw-rewrite/SKILL.md'
description=snapshot.with_name('description.txt')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert snapshot.read_bytes()==subprocess.check_output(['git','show','13599fb7d3127334b0d07bfe468767e586ec5f9c:skills/concise-writing/SKILL.md'])
line=next(l for l in snapshot.read_text().splitlines() if l.startswith('description: '))
assert description.read_text()==line.split(': ',1)[1][1:-1].replace("''","'")+'\n'
expected={p.name for p in base.glob('cw*.json') if '-no-dd' not in p.stem}
assert {p.name for p in candidate.glob('*.json')}==expected and len(expected)==22
rows=[]; ids=set()
for path in sorted(candidate.glob('*.json')):
 a=load_config(base/path.name);b=load_config(path)
 assert b.id not in ids and b.id!=a.id;ids.add(b.id)
 assert a.execution==b.execution and (b.execution.provider,b.execution.model,b.execution.effort)==('codex','gpt-5.6-sol','medium')
 assert a.prompt==b.prompt and a.schema_version==b.schema_version
 assert a.prompt.read_bytes()==subprocess.check_output(['git','show','dfd638ce5c1ac5f654110d05ce9138e5384d6afc:'+str(a.prompt.relative_to(root))])
 rubric=a.prompt.parent/'rubric.md'
 assert rubric.read_bytes()==subprocess.check_output(['git','show','dfd638ce5c1ac5f654110d05ce9138e5384d6afc:'+str(rubric.relative_to(root))])
 assert [f.target for f in a.fixtures]==[f.target for f in b.fixtures]
 for p in [path,b.prompt,rubric]+[f.source for f in b.fixtures]:
  assert p.is_file() and not any(x.is_symlink() for x in [p,*p.parents])
 differences=[]
 for x,y in zip(a.fixtures,b.fixtures):
  if x.source.read_bytes()!=y.source.read_bytes(): differences.append(str(x.target))
  else: assert x.source==y.source
  if str(y.target)=='.agents/skills/concise-writing/SKILL.md': assert y.source==snapshot
  elif str(y.target)=='descriptions/concise-writing.txt': assert y.source==description
  else: assert y.source.read_bytes()==subprocess.check_output(['git','show','dfd638ce5c1ac5f654110d05ce9138e5384d6afc:'+str(y.source.relative_to(root))])
 assert differences==(['descriptions/concise-writing.txt'] if 'description' in path.name else ['.agents/skills/concise-writing/SKILL.md'])
 context=create_run(b);prepared=prepare_workspace(context,b)
 actual={str(p.relative_to(context.fixture_dir)) for p in context.fixture_dir.rglob('*') if p.is_file()}
 assert actual=={str(f.target) for f in b.fixtures}
 assert not any(context.evidence_dir.iterdir())
 for f in b.fixtures: assert (context.fixture_dir/f.target).read_bytes()==f.source.read_bytes()
 rendered=a.prompt.read_text()
 for token,location in [('{{workspace_dir}}',context.workspace_dir),('{{fixture_dir}}',context.fixture_dir),('{{evidence_dir}}',context.evidence_dir)]:
  rendered=rendered.replace(token,str(location.resolve()))
 assert prepared.prompt_bytes==rendered.encode()
 rows.append(dict(config=str(path.relative_to(root)),id=b.id,baseline_config=str(a.config_path.relative_to(root)),scenario=str(a.prompt.parent.relative_to(root)),config_sha256=sha(path),prompt_sha256=sha(b.prompt),rubric_sha256=sha(rubric),changed_target=differences[0],fixture_count=len(b.fixtures),prepared_workspace=str(context.workspace_dir)))
assert subprocess.check_output(['git','diff','--name-only','dfd638ce5c1ac5f654110d05ce9138e5384d6afc','--','skills','skill-validation/runner','skill-validation/charter','skill-validation/scenarios','skill-validation/pilot/inputs/dd','skill-validation/pilot/inputs/superpowers','skill-validation/pilot/cw-01','skill-validation/pilot/cw-02','skill-validation/pilot/cw-03','skill-validation/pilot/cw-04','skill-validation/pilot/cw-05','skill-validation/pilot/cw-06','skill-validation/pilot/cw-07','skill-validation/pilot/cw-08','skill-validation/pilot/cw-09','skill-validation/pilot/cw-10','skill-validation/pilot/cw-11','skill-validation/pilot/cw-12','skill-validation/pilot/cw-13','skill-validation/pilot/cw-14','skill-validation/pilot/cw-17','skill-validation/pilot/cw-18','skill-validation/pilot/cw-19']).strip()==b''
print(json.dumps(dict(provider_calls=0,configs=len(rows),body_variants=sum('description' not in r['config'] for r in rows),description_variants=sum('description' in r['config'] for r in rows),source_revision='13599fb7d3127334b0d07bfe468767e586ec5f9c',body_sha256=sha(snapshot),description_sha256=sha(description),original_words=len(original.read_text().split()),candidate_words=len(snapshot.read_text().split()),all_checks='PASS',rows=rows),indent=2))

PY
```

Exit 0; results: [input-audit.json](input-audit.json).

