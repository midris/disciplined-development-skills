"""Prospective collection guards; no provider execution."""
import importlib.util
import json
from pathlib import Path
import pytest

HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location('cw_suite_collector', HERE/'collect_one.py')
collector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(collector)


def test_same_condition_repetition_on_other_case_is_not_a_repeat():
    slot = {'case_id':'effective-briefing','condition':'original','repetition':1}
    collector.ensure_unattempted(slot,[dict(slot,case_id='agent-recommendation')])
    with pytest.raises(AssertionError,match='automatic reruns'):
        collector.ensure_unattempted(slot,[slot])


def test_previous_slot_needs_retention_and_clearance(tmp_path):
    slots=[{'global_order':1},{'global_order':2}]
    with pytest.raises(AssertionError,match='unregistered'):
        collector.check_previous(slots,2,tmp_path)
    (tmp_path/'receipts').mkdir()
    p=tmp_path/'receipts/001.json';p.write_text(json.dumps({'cleared':False}))
    with pytest.raises(AssertionError,match='inspection'):
        collector.check_previous(slots,2,tmp_path)
    p.write_text(json.dumps({'cleared':True}))
    collector.check_previous(slots,2,tmp_path)


def test_inventory_wrapper_resolves_through_real_consumer(tmp_path):
    import hashlib
    from skilltest.documents import Report
    from skilltest.documents.references import Context
    from skilltest.documents.operations import encoded
    from skilltest.documents.retention import inventory
    bundle=tmp_path/'bundle';bundle.mkdir();(bundle/'output.md').write_text('Saved output.\n')
    target=tmp_path/'bundle.inventory.json';target.write_bytes(encoded(collector.inventory_record(bundle,inventory(bundle))))
    report=Report();owner=Path(__file__).resolve()
    Context(owner,report).inventory({'path':str(bundle),'inventory':{'path':str(target),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'version':'1'}},owner)
    assert report.structurally_valid and report.complete and not report.unsupported, report.diagnostics



from collections import Counter
from skilltest.config import load_config

def test_exact_approved_schedule_and_fixed_discovery_bodies():
 slots=json.loads((HERE/'schedule.json').read_text())['slots']
 assert [s['global_order'] for s in slots]==list(range(1,151))
 assert Counter(s['kind'] for s in slots)=={'body':90,'discovery':60}
 assert Counter(s['provider'] for s in slots)=={'codex':75,'claude':75}
 cells=Counter((s['provider'],s['case_id'],s['condition']) for s in slots)
 assert len(cells)==30 and set(cells.values())=={5}
 assert all(s['kind']=='body' for s in slots[:90])
 descriptions=set();bodies=set()
 for s in slots:
  cfg=load_config(collector.ROOT/s['config'])
  skills=[f for f in cfg.fixtures if str(f.target).endswith('/SKILL.md')]
  assert bool(skills)==(s['condition']!='control')
  if s['kind']=='discovery':
   assert s['condition'].startswith('description-')
   text=skills[0].source.read_text();front,body=text.split('---',2)[1:]
   descriptions.add(front);bodies.add(body)
 assert len(descriptions)==3 and len(bodies)==1
