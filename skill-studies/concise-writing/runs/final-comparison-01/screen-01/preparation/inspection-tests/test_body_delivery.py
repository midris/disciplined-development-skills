from pathlib import Path
import sys
import pytest
H=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(H))
from body_delivery import body_delivered
SOURCE="---\nname: concise-writing\ndescription: Use when editing.\n---\n\n# Concise writing\n\nKeep useful framing.\nPreserve the why.\n"
BODY=SOURCE.split("\n---\n",1)[1].strip()

@pytest.mark.parametrize("output,expected",[
    (SOURCE,True),
    ("Base directory for this skill: /fixture/.claude/skills/concise-writing\n\n"+BODY,True),
    ("\n".join(f"{i}→{line}" for i,line in enumerate(BODY.splitlines(),1)),True),
    (BODY.splitlines()[0],False),
    (SOURCE.split("\n---\n",1)[0],False),
    (BODY.replace("Preserve the why.","Drop the why."),False),
])
def test_complete_body_delivery(output,expected):
    assert body_delivered(SOURCE,output) is expected
