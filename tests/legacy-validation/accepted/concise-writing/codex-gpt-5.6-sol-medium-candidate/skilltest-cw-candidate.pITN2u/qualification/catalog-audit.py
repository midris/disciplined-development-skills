"""One-shot provider-free catalog and local file-path qualification."""
import copy, hashlib, json, os, re, subprocess, tempfile
from pathlib import Path
from skilltest.config import load_config
from skilltest.codex_runtime import CodexRuntime, check_inputs
from skilltest.workspace import create_run, prepare_workspace
from skilltest.results import _directory_artifact
OUT=Path("/private/tmp/skilltest-cw-candidate.pITN2u/qualification")
REPO=Path("/Users/simon/work/personal/disciplined-development-skills/.worktrees/cw-validation-design")
PILOT=REPO/"skill-validation/pilot"
os.umask(0o077)
work=OUT/"native"; work.mkdir()
profile=work/"dummy-profile"; profile.mkdir()
auth=profile/"auth.json"; auth.write_text('{"OPENAI_API_KEY":"dummy-provider-free-not-a-secret"}')
os.environ["CODEX_HOME"]=str(profile)
os.environ["PATH"]="/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
tempfile.tempdir=str(work)
DD={p.parent.name for p in (PILOT/"inputs/dd").glob("*/SKILL.md")}
COMMON={"imagegen","openai-docs","plugin-creator","skill-creator","skill-installer","writing-plans","requesting-code-review"}
AUTHOR={"writing-skills","test-driven-development"}
records=[]; normals={}; bootstraps={}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,value): (work/name).write_text(json.dumps(value,indent=2)+"\n")
def normalized(messages,fixture,runtime,drop):
    result=copy.deepcopy(messages); removed=[]
    for m in result:
        m.pop("id",None)
        m.get("internal_chat_message_metadata_passthrough",{}).pop("create_time",None)
        for c in m.get("content",[]):
            if "text" not in c: continue
            lines=[]
            for line in c["text"].splitlines(keepends=True):
                if any(line.startswith("- "+n+":") and "(file: " in line for n in drop):
                    removed.append(line); continue
                lines.append(line.replace(str(fixture),"<FIXTURE>").replace(str(runtime),"<RUNTIME>"))
            c["text"]="".join(lines)
    assert len(removed)==len(drop)
    return result
def run(runtime,name,argv,cwd):
    save(name+"-command.json",{"argv":argv,"cwd":str(cwd),"env":runtime.environment})
    child=subprocess.Popen(argv,cwd=cwd,env=runtime.environment,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=True)
    out,err,timed=runtime.communicate(child,None,30)
    (work/(name+"-stdout.txt")).write_bytes(out)
    (work/(name+"-stderr.txt")).write_bytes(err)
    save(name+"-status.json",{"exit_code":child.returncode,"timed_out":timed})
    assert child.returncode==0 and not timed,(name,child.returncode)
    return out
try:
    cases=[("ordinary","cw18-discovery.json",COMMON|DD,DD),
           ("ordinary-candidate","cw-rewrite/cw18-discovery.json",COMMON|DD,DD),
           ("author-current-dd","cw13-current-dd.json",COMMON|AUTHOR|DD,AUTHOR|DD),
           ("author-candidate","cw-rewrite/cw13-current-dd.json",COMMON|AUTHOR|DD,AUTHOR|DD),
           ("description","cw09-description.json",COMMON,set()),
           ("description-candidate","cw-rewrite/cw09-description.json",COMMON,set())]
    for label,filename,expected,drop in cases:
        cfg=load_config(PILOT/"efforts/medium"/filename)
        context=create_run(cfg); prepare_workspace(context,cfg)
        before=check_inputs(context,cfg)
        logs=[]; runtime=CodexRuntime(logs.append)
        record={"case":label,"config":str(cfg.config_path) if hasattr(cfg,"config_path") else filename,"fixture":str(context.fixture_dir),"prelaunch":before}
        records.append(record)
        try:
            runtime.prepare(context.fixture_dir)
            assert runtime.executable=="/opt/homebrew/bin/codex"
            assert set(runtime.environment)=={"HOME","CODEX_HOME","TMPDIR","PATH"}
            argv=[runtime.executable,"debug","prompt-input","-c",'model="gpt-5.6-sol"',"-c",'model_reasoning_effort="medium"',"-c",'shell_environment_policy.inherit="none"',"-c",'cli_auth_credentials_store="file"',"-c",'approval_policy="never"',"Provider-free catalog inspection."]
            raw=run(runtime,label+"-catalog",argv,context.fixture_dir)
            messages=json.loads(raw)
            alltext="\n".join(c.get("text","") for m in messages for c in m.get("content",[]))
            entries=[l for l in alltext.splitlines() if l.startswith("- ") and "(file: " in l]
            names=[l[2:].split(":",1)[0] for l in entries]
            assert len(names)==len(set(names)) and set(names)==expected,names
            roots=dict(re.findall(r"^- `(r[0-9]+)` = `([^`]+)`$",alltext,re.M))
            for line in entries:
                name=line[2:].split(":",1)[0]
                if name not in (DD|AUTHOR|{"writing-plans","requesting-code-review"}): continue
                ref=line.rsplit("(file: ",1)[1][:-1]
                if ref.startswith("/"): actual=Path(ref)
                else:
                    alias,relative=ref.split("/",1); actual=Path(roots[alias])/relative
                assert actual==context.fixture_dir/".agents/skills"/name/"SKILL.md"
            assert "/Users/simon" not in alltext and "/etc/codex" not in alltext
            if "description" not in label:
                body=(context.fixture_dir/".agents/skills/concise-writing/SKILL.md").read_text()
                description=next(l.split(": ",1)[1] for l in body.splitlines() if l.startswith("description: "))
                if description.startswith("'"): description=description[1:-1].replace("''","'")
                elif description.startswith('"'): description=json.loads(description)
                entry=next(l for l in entries if l.startswith("- concise-writing:"))
                assert ": "+description+" (file: " in entry,(label,"CW catalog description differs from supplied body")
                record["cw_catalog_entry"]=entry
            bootstrap=runtime.root/"codex/skills/.system"
            bootstraps[label]={str(p.relative_to(bootstrap)):sha(p) for p in bootstrap.rglob("*") if p.is_file()}
            normals[label]=normalized(messages,context.fixture_dir,runtime.root,drop)
            save(label+"-normalized.json",normals[label])
            shell=["/bin/zsh","-lc",'cd "$1" || exit; shift; cat "$@" >/dev/null',"cw-tools",str(context.fixture_dir)]+[str(f.target) for f in cfg.fixtures]
            run(runtime,label+"-reads",shell,context.fixture_dir)
            assert check_inputs(context,cfg)==before
            record.update(names=names,bootstrap=bootstraps[label],runtime=str(runtime.root))
        finally:
            cleanup=runtime.cleanup()
            record.update(cleanup=cleanup,runtime_absent=runtime.root is not None and not os.path.lexists(runtime.root))
            (work/(label+"-runtime.log")).write_text("\n".join(logs)+"\n")
            save("audit.json",records)
            assert cleanup is None and record["runtime_absent"]
    assert all(n==normals["ordinary"] for n in normals.values()),"undeclared common diagnostic difference"
    assert all(b==bootstraps["ordinary"] for b in bootstraps.values()),"bootstrap differs across setups"
    old=json.loads(Path("/private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/preflight/catalog-v3/catalog-audit.json").read_text())[0]["bootstrap"]
    assert old==bootstraps["ordinary"],"bootstrap differs from retained qualification"
    print("PASS: baseline/candidate native catalogs 16/16, 18/18, 7/7; CW descriptions match each supplied body; normalized common inputs equal; historical bootstrap bytes equal; local reads and cleanup verified. CW18 write reuses retained qualification.")
finally:
    auth.unlink(); profile.rmdir()
    save("audit.json",records)
