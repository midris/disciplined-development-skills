"""Continuation bounds and assessment gates; no provider invocation."""
from pathlib import Path
import json,os,sys,types
import pytest
H=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(H))

@pytest.fixture
def controller():
    source=Path(os.environ.get('CW_TEST_CONTROLLER',str(H/'collect_one.py'))).read_text()
    module=types.ModuleType('cw_topup_guard_probe');module.__file__=str(H/'collect_one.py')
    exec(compile(source,module.__file__,'exec'),module.__dict__)
    return module

@pytest.mark.parametrize('number',[0,13])
def test_rejects_outside_twelve_authorized_slots(controller,monkeypatch,number):
    monkeypatch.setattr(sys,'argv',['collect_one.py',str(number)])
    def forbidden(*args,**kwargs):
        pytest.fail('guard allowed provider dispatch')
    monkeypatch.setattr(controller,'run_once',forbidden)
    with pytest.raises(AssertionError,match='approved twelve-subject handoff'):
        controller.main()

def test_rejects_already_attempted_repetition(controller):
    slot=dict(case_id='comments-explicit',condition='original-body',repetition=4)
    with pytest.raises(AssertionError,match='no automatic reruns'):
        controller.ensure_unattempted(slot,[dict(slot)])

@pytest.mark.parametrize('cleared,result,expected',[(False,None,'needs inspection'),(True,None,'score the prior')])
def test_blocks_uninspected_or_unassessed_prior_subject(controller,monkeypatch,tmp_path,cleared,result,expected):
    slot=dict(global_order=1,batch_id='test',case_id='comments-explicit',condition='original-body',repetition=4)
    store=tmp_path/'store';(store/'receipts').mkdir(parents=True)
    (store/'receipts/001.json').write_text(json.dumps(dict(cleared=cleared)))
    (tmp_path/'test-run-index.json').write_text(json.dumps(dict(attempts=[dict(slot,result=result)])))
    monkeypatch.setattr(controller,'COLLECTION',tmp_path)
    with pytest.raises(AssertionError,match=expected):
        controller.check_previous([slot],2,store)

@pytest.mark.parametrize('exitcode',[1,2])
def test_failed_readiness_blocks_before_previous_checks_claims_and_dispatch(controller,monkeypatch,tmp_path,exitcode):
    import subprocess
    (tmp_path/'schedule.json').write_text(json.dumps(dict(slots=[dict(global_order=1,batch_id='codex-final-examples-screen-01')])))
    monkeypatch.setattr(controller,'HERE',tmp_path)
    monkeypatch.setattr(sys,'argv',['collect_one.py','1'])
    def readiness(command,**kwargs):
        assert command[-4:]==['--ready-for','collection','--batch','codex-final-examples-screen-01']
        assert kwargs.get('check') is True
        raise subprocess.CalledProcessError(exitcode,command)
    def forbidden(*args,**kwargs):
        pytest.fail('readiness failure fell through to collection')
    monkeypatch.setattr(controller.subprocess,'run',readiness)
    monkeypatch.setattr(controller,'check_previous',forbidden)
    monkeypatch.setattr(controller,'run_once',forbidden)
    with pytest.raises(subprocess.CalledProcessError):controller.main()
