from body_delivery import body_delivered
from pathlib import Path
import json,sys,re,hashlib
from skilltest.config import load_config
from trace_paths import is_target_path
from skilltest.documents.retention import inventory
root=Path.cwd();store=Path('/Users/simon/work/personal/skill-study-private/concise-writing/final-comparison-20261021/screen-02');n=int(sys.argv[1]);p=store/'receipts'/f'{n:03}.json';receipt=json.loads(p.read_text());slot=receipt['slot'];bundle=Path(receipt['bundle']);cfg=load_config(root/slot['config'])
from skilltest.documents import Report
from skilltest.documents.references import Context
from skilltest.documents.capture import verify_capture
index_path=Path(__file__).resolve().parent.parent/f'{slot["batch_id"]}-run-index.json'
record=next(a for a in json.loads(index_path.read_text())['attempts'] if a['run_id']==receipt['run_id'])
report=Report();Context(index_path,report).inventory(record['bundle'],index_path)
assert report.structurally_valid and report.complete and not report.unsupported,report.diagnostics
verify_capture(json.loads((bundle/'result.json').read_text()),inventory(bundle))
def strings(x):
 if isinstance(x,str):
  yield x
  if x[:1] in '{[':
   try:yield from strings(json.loads(x))
   except (ValueError,RecursionError):pass
 elif isinstance(x,dict):
  for v in x.values():yield from strings(v)
 elif isinstance(x,list):
  for v in x:yield from strings(v)
if slot['provider']=='codex':
 events=[json.loads(l) for l in (bundle/'provider-session.jsonl').read_text().splitlines()]
 turns=[e['payload'] for e in events if e.get('type')=='turn_context'];assert turns and all(t['model']=='gpt-5.6-sol' and t.get('effort')=='low' for t in turns)
 meta=next(e['payload'] for e in events if e.get('type')=='session_meta');assert meta['cli_version']=='0.163.0'
 calls=[(i,e['payload']) for i,e in enumerate(events) if e.get('type')=='response_item' and e.get('payload',{}).get('type') in ['function_call','custom_tool_call']]
 edits=[i for i,e in calls if 'apply_patch' in str(e.get('input',e.get('arguments',''))) and ('***' in str(e) or 'report.md' in str(e) or 'settings.toml' in str(e) or 'uploader.py' in str(e))]
 assert edits,'task edit shape needs manual inspection'
 outputs=[(i,'\n'.join(strings(e['payload'].get('output','')))) for i,e in enumerate(events) if e.get('type')=='response_item' and e.get('payload',{}).get('type') in ['function_call_output','custom_tool_call_output']]
 guidance='\n'.join(s for e in events if e.get('type')=='response_item' and e.get('payload',{}).get('role')=='developer' for s in strings(e['payload'].get('content',[])))
else:
 events=[json.loads(l) for l in (bundle/'stdout.txt').read_text().splitlines() if l.strip()]
 init=next(e for e in events if e.get('type')=='system' and e.get('subtype')=='init');assert init['model']=='claude-sonnet-5' and init['claude_code_version']=='2.1.305'
 models={e.get('message',{}).get('model') for e in events if e.get('type')=='assistant' and e.get('message',{}).get('model')};assert models=={'claude-sonnet-5'},models
 edits=[i for i,e in enumerate(events) for c in e.get('message',{}).get('content',[]) if isinstance(c,dict) and c.get('type')=='tool_use' and c.get('name') in ['Write','Edit'] and is_target_path(c.get('input',{}).get('file_path',''))]
 assert edits,'task edit shape needs manual inspection'
 outputs=[(i,'\n'.join(strings(e.get('message',{}).get('content',[])))) for i,e in enumerate(events) if e.get('type')=='user']
 guidance=json.dumps(init)
native=slot['kind']=='discovery'
if slot['condition']=='control':
 assert 'concise-writing' not in guidance,'unexpected CW control catalog'
 assert not any('name: concise-writing' in s for _,s in outputs),'unexpected CW control body'
 exposure='No CW catalog/body exposure'
else:
 skill=next(f for f in cfg.fixtures if str(f.target).endswith('/SKILL.md')).source.read_text().strip()
 def normalize(s):return '\n'.join(re.sub(r'^\s*\d+[→\t|]','',line) for line in s.splitlines()).strip()
 before=[(i,s) for i,s in outputs if i<min(edits)]
 matches=[i for i,s in before if body_delivered(skill,s)]
 if native:
  assert 'concise-writing' in guidance, 'native availability absent; setup needs inspection'
  source_skill=next(f for f in cfg.fixtures if str(f.target).endswith('/SKILL.md')).source.read_text()
  description=re.search(r'^description: (.*)$',source_skill,re.M).group(1).strip("'\"")
  assert description in guidance, 'exact native descriptor absent'
  assert skill not in guidance, 'body exposed in initial guidance'
  exposure=f'Native skill available; complete assigned body before first edit: {bool(matches)}'
 else:
  assert matches,'complete body before edit needs manual inspection'
  exposure=f'Complete assigned teaching body in tool output {matches[0]} before first task edit {min(edits)}'
for f in cfg.fixtures:
 if str(f.target) != slot['output']:assert (bundle/'workspace/fixture'/f.target).read_bytes()==f.source.read_bytes()

receipt['native_body_before_edit']=bool(matches) if native else None;receipt['complete_body_any_time']=any(body_delivered(skill,s) for _,s in outputs) if slot['condition']!='control' else False;receipt['cleared']=True;receipt['clearance']=f'Fixed provider/model/CLI and retained inventory verified. {exposure}. Protected input bytes unchanged.';p.write_text(json.dumps(receipt,indent=2)+'\n')
print(n,slot['provider'],slot['condition'],slot['repetition'],receipt['status'],exposure,flush=True)
