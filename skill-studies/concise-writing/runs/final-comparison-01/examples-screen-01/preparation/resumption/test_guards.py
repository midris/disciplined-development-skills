"""One owner-approved authentication replacement, with no provider calls."""
from pathlib import Path
import json,types,pytest
P=Path(__file__).with_name('collect_one.py')
@pytest.fixture
def controller():
 m=types.ModuleType('examples_resume');m.__file__=str(P);exec(compile(P.read_text(),str(P),'exec'),m.__dict__);return m
@pytest.mark.parametrize('value',[0,1,6,7,13,'retry-8'])
def test_rejects_unapproved_resumption_slot(controller,value):
 with pytest.raises(AssertionError,match='approved replacement or remaining slots'):controller.selected_slot(str(value))
@pytest.mark.parametrize('value,number,retry',[('retry-7',7,True),('8',8,False),('12',12,False)])
def test_allows_only_explicit_retry_and_remaining_slots(controller,value,number,retry):
 assert controller.selected_slot(value)==(number,retry)
def test_pool_count_does_not_transfer_retry_to_subject(controller):
 assert controller.pool_spending([{'allocation':{'pool':'subject','charge':1}},{'allocation':{'pool':'retry','charge':1}}])=={'subject':1,'retry':1}
def test_retry_requires_its_own_scored_receipt(controller,tmp_path,monkeypatch):
 store=tmp_path/'store';(store/'receipts').mkdir(parents=True);slot=dict(global_order=7,batch_id='claude-final-examples-screen-01',case_id='long-handoff',condition='original-examples',repetition=1)
 (store/'receipts/007.json').write_text(json.dumps(dict(cleared=False,run_id='failed')))
 (tmp_path/(slot['batch_id']+'-run-index.json')).write_text(json.dumps(dict(attempts=[dict(slot,run_id='failed',result={'x':1}),dict(slot,run_id='replacement',result=None)])))
 monkeypatch.setattr(controller,'COLLECTION',tmp_path)
 with pytest.raises(AssertionError,match='replacement receipt'):controller.check_previous([slot],2,store)
 (store/'receipts/007.retry-2.json').write_text(json.dumps(dict(cleared=True,run_id='replacement')))
 with pytest.raises(AssertionError,match='score the prior'):controller.check_previous([slot],2,store)
