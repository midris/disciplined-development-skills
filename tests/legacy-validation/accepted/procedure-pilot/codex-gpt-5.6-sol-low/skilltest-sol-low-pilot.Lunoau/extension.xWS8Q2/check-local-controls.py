"""One-shot local capability/network check; no model execution."""
from pathlib import Path
import json, subprocess
ROOT=Path("/private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2")
OLD=ROOT.parent/"preflight"
OUT=ROOT/"preflight"
REPO=Path("/Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike")
def capture(label, argv):
    assert not (OUT/(label+".txt")).exists(), label
    result=subprocess.run(argv,cwd=REPO,capture_output=True,timeout=30)
    (OUT/(label+".txt")).write_bytes(result.stdout)
    (OUT/(label+"-stderr.txt")).write_bytes(result.stderr)
    (OUT/(label+"-status.json")).write_text(json.dumps({"argv":argv,"cwd":str(REPO),"exit_code":result.returncode},indent=2)+"\n")
    return result
for label, argv in [
("cli-version",["/opt/homebrew/bin/codex","--version"]),
("cli-sha256",["/usr/bin/shasum","-a","256","/opt/homebrew/bin/codex"]),
("exec-help",["/opt/homebrew/bin/codex","exec","--help"]),
("debug-help",["/opt/homebrew/bin/codex","debug","prompt-input","--help"])]:
    r=capture(label,argv)
    assert r.returncode==0,label
    if label in ("cli-version","cli-sha256"): assert r.stdout==(OLD/(label+".txt")).read_bytes(), "CLI drift: "+label
for flag in ("--ignore-user-config","--ignore-rules","--add-dir"):
    assert flag in (OUT/"exec-help.txt").read_text()
probe=["/opt/homebrew/bin/python3","-c",'import socket; s=socket.socket(); s.bind(("127.0.0.1", 0)); s.close(); print("BIND_OK")']
positive=capture("network-positive",probe)
assert positive.returncode==0 and positive.stdout.strip()==b"BIND_OK","positive control inconclusive"
denied=capture("network-denied",["/usr/bin/sandbox-exec","-f",str(ROOT/"no-network.sb")]+probe)
assert denied.returncode!=0 and b"PermissionError" in denied.stderr and b"BIND_OK" not in denied.stdout,"network denial inconclusive"
print("PASS: CLI version/digest unchanged; required options present; loopback positive/denied controls pass.")
