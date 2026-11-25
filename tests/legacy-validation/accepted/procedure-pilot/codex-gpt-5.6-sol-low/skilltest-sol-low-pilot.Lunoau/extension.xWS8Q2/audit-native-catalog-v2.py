"""One-shot network-denied native-catalog audit; dummy credentials only."""
import copy, hashlib, json, os, re, subprocess, tempfile
from pathlib import Path
from skilltest.config import load_config
from skilltest.codex_runtime import CodexRuntime, check_inputs
from skilltest.workspace import create_run, prepare_workspace
ROOT=Path("/private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2")
OUT=ROOT/"preflight/catalog-v2"
OUT.mkdir()
REPO=Path("/Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike")
PILOT=REPO/"skill-validation/pilot"
os.umask(0o077)
TMP=OUT/"catalog-tmp"
TMP.mkdir()
profile=TMP/"dummy-profile"
profile.mkdir()
auth=profile/"auth.json"
with auth.open("x") as f: f.write('{"OPENAI_API_KEY":"dummy-provider-free-not-a-secret"}')
os.environ["CODEX_HOME"]=str(profile)
os.environ["PATH"]="/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
tempfile.tempdir=str(TMP)
DD={p.parent.name for p in (PILOT/"inputs/dd").glob("*/SKILL.md")}
COMMON={"imagegen","openai-docs","plugin-creator","skill-creator","skill-installer","writing-plans","requesting-code-review"}
records=[]
normal=[]
bootstrap_maps=[]
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def normalize(messages, replacements, drop_names):
    result=copy.deepcopy(messages)
    drops=[]
    for m in result:
        m.pop("id",None)
        m.get("internal_chat_message_metadata_passthrough",{}).pop("create_time",None)
        for c in m.get("content",[]):
            if "text" not in c: continue
            lines=[]
            for line in c["text"].splitlines(keepends=True):
                if any(line.startswith("- "+name+":") and "(file: " in line for name in drop_names):
                    drops.append(line.rstrip("\n")); continue
                for source,target in replacements: line=line.replace(source,target)
                lines.append(line)
            c["text"]="".join(lines)
    assert len(drops)==len(drop_names),(drops,drop_names)
    return result,drops
try:
    for arm in ("no-dd","current-dd"):
        config=load_config(PILOT/"ar-03"/arm/"test.json")
        context=create_run(config)
        prepare_workspace(context,config)
        before=check_inputs(context,config)
        assert not any(p.is_symlink() for p in context.fixture_dir.rglob("*"))
        runtime=CodexRuntime(lambda message: logs.append(message))
        logs=[]
        record={"arm":arm,"fixture":str(context.fixture_dir),"prelaunch_hashes":before}
        records.append(record)
        try:
            runtime.prepare(context.fixture_dir)
            assert runtime.executable=="/opt/homebrew/bin/codex"
            assert set(runtime.environment)=={"HOME","CODEX_HOME","TMPDIR","PATH"}
            command=[runtime.executable,"debug","prompt-input","-c",'model="gpt-5.6-sol"',"-c",'model_reasoning_effort="low"',"-c",'shell_environment_policy.inherit="none"',"-c",'cli_auth_credentials_store="file"',"-c",'approval_policy="never"',"Pilot provider-free catalog inspection."]
            (OUT/(arm+"-catalog-command.json")).write_text(json.dumps({"argv":command,"cwd":str(context.fixture_dir),"env":runtime.environment},indent=2)+"\n")
            child=subprocess.Popen(command,cwd=context.fixture_dir,env=runtime.environment,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=True)
            stdout,stderr,timed_out=runtime.communicate(child,None,30)
            (OUT/(arm+"-prompt-input.json")).write_bytes(stdout)
            (OUT/(arm+"-catalog-stderr.txt")).write_bytes(stderr)
            record.update(exit_code=child.returncode,timed_out=timed_out,runtime=str(runtime.root))
            assert child.returncode==0 and not timed_out
            messages=json.loads(stdout)
            all_text="\n".join(c.get("text","") for m in messages for c in m.get("content",[]))
            entries=[l for l in all_text.splitlines() if l.startswith("- ") and "(file: " in l]
            names=[l[2:].split(":",1)[0] for l in entries]
            assert set(names)==COMMON | (DD if arm=="current-dd" else set()),names
            assert len(names)==len(set(names))
            assert "/Users/simon" not in all_text and "/etc/codex" not in all_text
            for name in {"writing-plans","requesting-code-review"} | (DD if arm=="current-dd" else set()):
                line=next(l for l in entries if l.startswith("- "+name+":"))
                roots=dict(re.findall(r"^- `(r[0-9]+)` = `([^`]+)`$",all_text,re.MULTILINE))
                ref=re.search(r"\\(file: ([^)]+)\\)$",line).group(1)
                alias,relative=ref.split("/",1)
                resolved=Path(ref) if ref.startswith("/") else Path(roots[alias])/relative
                assert resolved==context.fixture_dir/".agents/skills"/name/"SKILL.md",(line,roots)
            bootstrap=runtime.root/"codex/skills/.system"
            hashes={str(p.relative_to(bootstrap)):sha(p) for p in bootstrap.rglob("*") if p.is_file()}
            assert hashes
            bootstrap_maps.append(hashes)
            normalized,dropped=normalize(messages,[(str(context.fixture_dir),"<FIXTURE>"),(str(runtime.root),"<RUNTIME>")],DD if arm=="current-dd" else set())
            normal.append(normalized)
            (OUT/(arm+"-normalized.json")).write_text(json.dumps(normalized,sort_keys=True,indent=2)+"\n")
            # Check the new task and guidance files with the previously observed shell wrapper, not a model call.
            files=[str(f.target) for f in config.fixtures]
            shell=["/bin/zsh","-lc",'cd "$1" || exit; shift; command -v cat || exit; cat "$@" >/dev/null',"extension-tool-check",str(context.fixture_dir)]+files
            child=subprocess.Popen(shell,cwd=context.fixture_dir,env=runtime.environment,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=True)
            sout,serr,stime=runtime.communicate(child,None,30)
            (OUT/(arm+"-shell-check.json")).write_text(json.dumps({"argv":shell,"cwd":str(context.fixture_dir),"exit_code":child.returncode,"timed_out":stime,"stdout":sout.decode(),"stderr":serr.decode()},indent=2)+"\n")
            assert child.returncode==0 and not stime and sout.strip()==b"/bin/cat" and not serr
            assert check_inputs(context,config)==before
            assert not list(context.evidence_dir.iterdir())
            record.update(native_entries=entries,bootstrap=hashes,dropped_entries=dropped,shell_read_files=files)
        finally:
            cleanup=runtime.cleanup()
            record.update(cleanup=cleanup,runtime_absent=runtime.root is not None and not os.path.lexists(runtime.root))
            (OUT/(arm+"-runtime.log")).write_text("\n".join(logs)+f"\ncleanup: {cleanup!r}\n")
            assert cleanup is None and record["runtime_absent"]
    assert normal[0]==normal[1],"common diagnostic content mismatch"
    assert bootstrap_maps[0]==bootstrap_maps[1],"bootstrap file mismatch"
    old_records=json.loads((ROOT.parent/"audit.json").read_text())
    old_bootstrap=next(r["bootstrap"] for r in old_records if "bootstrap" in r)
    old_command=json.loads((ROOT.parent/"no-dd-command.json").read_text())
    old_fixture=old_command["cwd"]
    old_runtime=str(Path(old_command["env"]["CODEX_HOME"]).parent)
    old_messages=json.loads((ROOT.parent/"no-dd-prompt-input.json").read_text())
    old_norm,_=normalize(old_messages,[(old_fixture,"<FIXTURE>"),(old_runtime,"<RUNTIME>")],set())
    new_without_review,dropped=normalize(normal[0],[],{"requesting-code-review"})
    comparison={"common_pair_equal":True,"bootstrap_pair_equal":True,"bootstrap_file_count":len(bootstrap_maps[0]),"prior_bootstrap_equal":old_bootstrap==bootstrap_maps[0],"prior_common_equal_except_review_entry":old_norm==new_without_review,"new_common_entry":dropped}
    (OUT/"prior-common-normalized.json").write_text(json.dumps(old_norm,sort_keys=True,indent=2)+"\n")
    (OUT/"extension-common-without-review.json").write_text(json.dumps(new_without_review,sort_keys=True,indent=2)+"\n")
    (OUT/"catalog-comparison.json").write_text(json.dumps(comparison,indent=2)+"\n")
    assert comparison["prior_bootstrap_equal"],"prior bootstrap changed; review required"
    assert comparison["prior_common_equal_except_review_entry"],"additional prior/common difference; review required"
    print("PASS: native catalogs 7/16; nine DD additions only; equal common content and bootstrap; prior common differs only by requesting-code-review; both shell reads and runtime cleanup pass.")
finally:
    auth.unlink()
    profile.rmdir()
    (OUT/"catalog-audit.json").write_text(json.dumps(records,indent=2)+"\n")
