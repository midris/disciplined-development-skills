"""Fail-closed preparation and verification for one isolated Git micro-fixture."""
from __future__ import annotations
import hashlib, json, os, stat, subprocess, sys, tempfile
from pathlib import Path, PurePosixPath
from typing import Any

__all__ = ["FixtureContractError", "prepare_fixture", "record_fixture_execution", "verify_fixture"]
_DF = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_CLOEXEC", 0)
_RF = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0) | getattr(os, "O_CLOEXEC", 0)
_GIT_HELPER = "import os,sys;fd=int(sys.argv[1]);os.fchdir(fd);os.close(fd);os.execvpe(sys.argv[2],sys.argv[2:],os.environ)"
class FixtureContractError(RuntimeError): pass
def _fail(message): raise FixtureContractError(message)
def _canon(value): return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode()
def _sha(data): return hashlib.sha256(data).hexdigest()
def _pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result: _fail("duplicate JSON key")
        result[key] = value
    return result
def _invalid_constant(value):
    _fail(f"invalid JSON constant {value}")
def _json(data, label):
    try: value = json.loads(data.decode(), object_pairs_hook=_pairs, parse_constant=_invalid_constant)
    except (UnicodeDecodeError, json.JSONDecodeError) as error: raise FixtureContractError(f"invalid {label} JSON") from error
    if _canon(value) != data: _fail(f"non-canonical {label} JSON")
    return value
def _exact(value, keys, label):
    if not isinstance(value, dict) or set(value) != keys: _fail(f"invalid {label} schema")
    return value
def _string(value, label):
    if not isinstance(value, str) or not value: _fail(f"invalid {label}")
    return value
def _rel(value, label):
    if not isinstance(value, str) or not value or value != value.strip() or "\\" in value or any(ord(char) < 32 or ord(char) > 126 or char in {'"', "'"} for char in value) or PurePosixPath(value).is_absolute() or any(x in {"", ".", ".."} for x in value.split("/")): _fail(f"unsafe {label}")
    return value
def _hash(value, label):
    value = _string(value, label)
    if len(value) != 64 or any(x not in "0123456789abcdef" for x in value): _fail(f"invalid {label}")
    return value
def _head(value, label):
    value = _string(value, label)
    if len(value) not in {40,64} or any(x not in "0123456789abcdef" for x in value): _fail(f"invalid {label}")
    return value
def _dir(path, label):
    fd = -1
    try:
        fd = os.open(path, _DF)
        if not stat.S_ISDIR(os.fstat(fd).st_mode): os.close(fd); _fail(f"{label} is not a non-symlink directory")
        return fd
    except FixtureContractError: raise
    except OSError as error:
        if fd >= 0: os.close(fd)
        raise FixtureContractError(f"cannot open {label}") from error
def _dirat(parent, name, label):
    fd = -1
    try:
        fd = os.open(name, _DF, dir_fd=parent)
        if not stat.S_ISDIR(os.fstat(fd).st_mode): os.close(fd); _fail(f"{label} is not a non-symlink directory")
        return fd
    except FixtureContractError: raise
    except OSError as error:
        if fd >= 0: os.close(fd)
        raise FixtureContractError(f"cannot open {label}") from error
def _regular(path, label):
    try:
        if not stat.S_ISREG(os.lstat(path).st_mode): _fail(f"{label} is not a regular file")
        fd = os.open(path, _RF)
        try:
            if not stat.S_ISREG(os.fstat(fd).st_mode): _fail(f"{label} is not a regular file")
            return _read_all(fd, label)
        finally: os.close(fd)
    except FixtureContractError: raise
    except OSError as error: raise FixtureContractError(f"cannot read {label}") from error
def _parent(fd, relative, label):
    parts = _rel(relative, label).split("/"); current = os.dup(fd)
    try:
        for part in parts[:-1]:
            child = _dirat(current, part, label)
            try:
                os.close(current)
            except OSError as error:
                os.close(child); current = -1
                raise FixtureContractError(f"cannot traverse {label}") from error
            current = child
        return current, parts[-1]
    except BaseException:
        if current >= 0: os.close(current)
        raise
def _readat(fd, relative, label):
    parent, name = _parent(fd, relative, label)
    try:
        if not stat.S_ISREG(os.stat(name, dir_fd=parent, follow_symlinks=False).st_mode): _fail(f"{label} is not a regular file")
        child = os.open(name, _RF, dir_fd=parent)
        try:
            if not stat.S_ISREG(os.fstat(child).st_mode): _fail(f"{label} is not a regular file")
            return _read_all(child, label)
        finally: os.close(child)
    except FixtureContractError: raise
    except OSError as error: raise FixtureContractError(f"cannot read {label}") from error
    finally: os.close(parent)
def _read_all(fd, label):
    """Read one regular immutable artifact completely; reject truncation and growth."""
    expected = os.fstat(fd).st_size; chunks = []; remaining = expected
    while remaining:
        chunk = os.read(fd, remaining)
        if not chunk: _fail(f"truncated {label}")
        chunks.append(chunk); remaining -= len(chunk)
    if os.read(fd, 1): _fail(f"growing {label}")
    return b"".join(chunks)
def _entry(fd, relative, label):
    parts = _rel(relative, label).split("/")
    current = os.dup(fd)
    try:
        for part in parts[:-1]:
            try:
                child = _dirat(current, part, label)
            except FixtureContractError as error:
                if isinstance(error.__cause__, FileNotFoundError):
                    return None
                raise
            try:
                os.close(current)
            except OSError as error:
                current = -1
                try: os.close(child)
                except OSError as child_error: raise FixtureContractError(f"cannot traverse {label}") from child_error
                raise FixtureContractError(f"cannot traverse {label}") from error
            current = child
        try:
            return os.stat(parts[-1], dir_fd=current, follow_symlinks=False)
        except FileNotFoundError:
            return None
    except OSError as error: raise FixtureContractError(f"cannot inspect {label}") from error
    finally:
        if current >= 0: os.close(current)
def _scan(fd, label, prefix="", exclude_git=False):
    files, dirs = set(), set()
    try:
        for name in os.listdir(fd):
            if exclude_git and not prefix and name == ".git": continue
            relative = f"{prefix}/{name}" if prefix else name; info = os.stat(name, dir_fd=fd, follow_symlinks=False)
            if stat.S_ISREG(info.st_mode): files.add(relative); continue
            if not stat.S_ISDIR(info.st_mode): _fail(f"unsafe {label} entry")
            child = os.open(name, _DF, dir_fd=fd)
            try:
                subfiles, subdirs = _scan(child, label, relative); files |= subfiles; dirs |= subdirs; dirs.add(relative)
            finally: os.close(child)
    except OSError as error: raise FixtureContractError(f"cannot inspect {label}") from error
    return files, dirs
def _tree(path, label):
    fd = _dir(path, label)
    try: return _scan(fd, label)
    finally: os.close(fd)
def _ancestors(paths):
    result = set()
    for path in paths:
        parent = PurePosixPath(path).parent
        while str(parent) != ".": result.add(str(parent)); parent = parent.parent
    return result
def _write(fd, name, data):
    try:
        child = os.open(name, os.O_WRONLY|os.O_CREAT|os.O_EXCL|getattr(os,"O_NOFOLLOW",0), 0o600, dir_fd=fd)
        try:
            offset = 0
            while offset < len(data):
                wrote = os.write(child, data[offset:])
                if wrote <= 0: _fail("short immutable artifact write")
                offset += wrote
            os.fsync(child); os.fchmod(child, 0o444)
        finally: os.close(child)
    except OSError as error: raise FixtureContractError(f"cannot write immutable artifact {name}") from error
def _mkdir_parent(fd, relative):
    parts = _rel(relative, "fixture member").split("/"); current = os.dup(fd)
    try:
        for part in parts[:-1]:
            try: os.mkdir(part, 0o700, dir_fd=current)
            except FileExistsError: pass
            child = _dirat(current, part, "repository directory")
            try:
                os.close(current)
            except OSError as error:
                os.close(child); current = -1
                raise FixtureContractError("cannot traverse repository directory") from error
            current = child
        return current, parts[-1]
    except BaseException:
        if current >= 0: os.close(current)
        raise
def _write_rel(fd, relative, data):
    parent, name = _mkdir_parent(fd, relative)
    try: _write(parent, name, data)
    finally: os.close(parent)
def _chmod(fd, relative, mode):
    parent, name = _parent(fd, relative, "fixture member")
    try: os.chmod(name, mode, dir_fd=parent, follow_symlinks=False)
    except OSError as error: raise FixtureContractError("cannot change fixture member mode") from error
    finally: os.close(parent)
def _contract(path):
    data = _regular(path, "external contract"); contract = _exact(_json(data, "external contract"), {"schema_version","fixture_id","source_root","members","base","execution_gate","expected","required_commands","required_milestones"}, "fixture contract")
    if type(contract["schema_version"]) is not int or contract["schema_version"] != 1: _fail("unsupported fixture schema")
    _string(contract["fixture_id"], "fixture id"); _string(contract["execution_gate"], "execution gate"); source = Path(contract["source_root"])
    if not source.is_absolute(): _fail("source root must be absolute")
    source_fd = _dir(source, "source root")
    try:
     sources, destinations, members = set(), set(), []
     if not isinstance(contract["members"], list) or not contract["members"]: _fail("members must be nonempty")
     for member in contract["members"]:
        member = _exact(member, {"source","destination","sha256","executable"}, "member"); src, dst = _rel(member["source"],"member source"), _rel(member["destination"],"member destination")
        if dst == ".git" or dst.startswith(".git/") or dst in destinations: _fail("unsafe member destination" if dst == ".git" or dst.startswith(".git/") else "duplicate destination")
        wanted = _hash(member["sha256"], "member hash")
        if type(member["executable"]) is not bool: _fail("member executable flag is invalid")
        actual = _readat(source_fd, src, "source member")
        if _sha(actual) != wanted: _fail("source member hash mismatch")
        sources.add(src); destinations.add(dst); members.append({"source":src,"destination":dst,"sha256":wanted,"executable":member["executable"],"bytes":actual})
     _source_auth_hook(source_fd)
     files, dirs = _scan(source_fd, "source root")
    finally:
     os.close(source_fd)
    if files != sources or dirs != _ancestors(sources): _fail("source root inventory mismatch")
    base = _exact(contract["base"], {"author_name","author_email","timestamp","subject","head"}, "base")
    for key in ("author_name","author_email","timestamp","subject"): _string(base[key], f"base {key}")
    _head(base["head"], "base head"); expected = _exact(contract["expected"], {"final_head","commit_count_after_base","changed_paths","required_files","forbidden_paths","clean_worktree"}, "expected"); _head(expected["final_head"],"expected final head")
    if type(expected["commit_count_after_base"]) is not int or expected["commit_count_after_base"] < 0: _fail("invalid commit count")
    if not isinstance(expected["changed_paths"],list) or len(set(expected["changed_paths"])) != len(expected["changed_paths"]): _fail("invalid changed paths")
    for item in expected["changed_paths"]: _rel(item,"changed path")
    if not isinstance(expected["required_files"],dict) or not expected["required_files"]: _fail("invalid required files")
    for name, wanted in expected["required_files"].items(): _rel(name,"required file"); _hash(wanted,"required file hash")
    if not isinstance(expected["forbidden_paths"],list) or len(set(expected["forbidden_paths"])) != len(expected["forbidden_paths"]): _fail("invalid forbidden paths")
    for item in expected["forbidden_paths"]: _rel(item,"forbidden path")
    if set(expected["required_files"]) & set(expected["forbidden_paths"]): _fail("required and forbidden paths overlap")
    if type(expected["clean_worktree"]) is not bool: _fail("invalid clean worktree flag")
    if not isinstance(contract["required_commands"],list) or not contract["required_commands"]: _fail("required commands must be nonempty")
    for item in contract["required_commands"]:
        item = _exact(item,{"command","exit_code"},"required command"); _string(item["command"],"required command")
        if type(item["exit_code"]) is not int: _fail("required command exit code is invalid")
    milestones = contract["required_milestones"]
    if not isinstance(milestones,list) or not milestones or len(set(milestones)) != len(milestones): _fail("invalid required milestones")
    for item in milestones: _string(item,"milestone")
    helper = next((member for member in members if member["destination"] == "fixture-helper"), None)
    if helper is None or not helper["executable"]:
        _fail("fixture helper is missing or nonexecutable")
    for milestone in milestones:
        parts = milestone.split(" ")
        if len(parts) != 2 or parts[0] != "./fixture-helper" or not parts[1] or any(not (char.isalnum() or char in "._-") for char in parts[1]):
            _fail("unsafe milestone command")
    return contract, data, members
def _git(fd, *args, env=None):
    environ = {k:v for k,v in os.environ.items() if not k.startswith("GIT_")} | {"GIT_CONFIG_NOSYSTEM":"1","GIT_CONFIG_GLOBAL":os.devnull,"GIT_OPTIONAL_LOCKS":"0","GIT_ATTR_NOSYSTEM":"1","GIT_NO_REPLACE_OBJECTS":"1","GIT_DIR":".git","GIT_WORK_TREE":"."} | (env or {})
    git = _trusted_git()
    try: completed = subprocess.run([sys.executable,"-I","-c",_GIT_HELPER,str(fd),git,"-C",".","-c","core.hooksPath=/dev/null","-c","commit.gpgSign=false","-c","core.fileMode=true","-c","core.fsmonitor=false","-c","core.untrackedCache=false","-c","status.showUntrackedFiles=all",*args],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False,env=environ,pass_fds=(fd,))
    except (OSError,ValueError) as error: raise FixtureContractError("cannot execute isolated Git") from error
    if completed.returncode: _fail("isolated Git inspection failed")
    try: return completed.stdout.decode().strip()
    except UnicodeDecodeError as error: raise FixtureContractError("invalid Git output") from error
def _trusted_git():
    """Use a system Git executable, never a caller-controlled PATH lookup."""
    for directory in ("/usr/bin", "/bin"):
        candidate = Path(directory) / "git"
        try:
            info = os.lstat(candidate)
        except OSError:
            continue
        if stat.S_ISREG(info.st_mode) and os.access(candidate, os.X_OK):
            return str(candidate)
    _fail("trusted Git executable is unavailable")
def _manifest(contract,members): return {"schema_version":1,"fixture_id":contract["fixture_id"],"source_root":contract["source_root"],"members":[{k:m[k] for k in ("source","destination","sha256","executable")} for m in members]}
def _static(admin, repository, path, recorded):
    contract, data, members = _contract(path); base = {"schema_version":1,"fixture_id":contract["fixture_id"],"base_head":contract["base"]["head"],"base_timestamp":contract["base"]["timestamp"],"base_subject":contract["base"]["subject"]}; expected = {"contract.json":data,"source-manifest.json":_canon(_manifest(contract,members)),"base-observation.json":_canon(base)}
    if recorded: expected |= {"events.jsonl":None,"response.bin":None,"evidence.json":None,"terminal.json":None}
    files, dirs = _scan(admin,"admin root")
    if files != set(expected) or dirs: _fail("administrative inventory mismatch")
    for name, wanted in expected.items():
        info = _entry(admin,name,"administrative artifact")
        if info is None or stat.S_IMODE(info.st_mode) != 0o444: _fail("administrative artifact is not immutable")
        if wanted is not None and _readat(admin,name,name) != wanted: _fail("static administrative artifact mismatch")
    return contract,data,members
def _commands(events, contract):
    if not events: _fail("event stream is empty")
    try: text = events.decode()
    except UnicodeDecodeError as error: raise FixtureContractError("event stream is not UTF-8") from error
    if not text.endswith("\n"): _fail("event stream is partial")
    seen, observed = set(), []
    for line in text.splitlines():
        if not line: _fail("event stream contains an empty line")
        try: event = json.loads(line,object_pairs_hook=_pairs,parse_constant=_invalid_constant)
        except (json.JSONDecodeError,FixtureContractError) as error: raise FixtureContractError("invalid event JSONL") from error
        if not isinstance(event,dict): _fail("event is not an object")
        if event.get("type") != "item.completed": continue
        item = event.get("item")
        if not isinstance(item,dict) or item.get("type") != "command_execution": continue
        command = item.get("command")
        if item.get("status") != "completed":
            proof_commands = {row["command"] for row in contract["required_commands"]} | set(contract["required_milestones"])
            if command in proof_commands: _fail("incomplete required command event")
            continue
        if not {"id","type","command","exit_code","status"} <= set(item): _fail("invalid command event shape")
        ident = _string(item["id"],"command item id")
        if ident in seen: _fail("duplicate command item id")
        seen.add(ident); command = _string(item["command"],"command event command")
        if type(item["exit_code"]) is not int: _fail("invalid command event exit code")
        observed.append({"command":command,"exit_code":item["exit_code"]})
    def subseq(need,have):
        position=0
        for item in have:
            if position<len(need) and item==need[position]: position+=1
        return position==len(need)
    required=[{"command":x["command"],"exit_code":x["exit_code"]} for x in contract["required_commands"]]
    if not subseq(required,observed): _fail("required command evidence mismatch")
    if not subseq(contract["required_milestones"],[x["command"] for x in observed]): _fail("required milestone evidence mismatch")
    return observed
def _inspect(repo, display, contract):
    gitdir = _entry(repo,".git","repository Git directory")
    if gitdir is None or stat.S_ISLNK(gitdir.st_mode) or not stat.S_ISDIR(gitdir.st_mode): _fail("repository Git directory is unsafe")
    git_fd = _dirat(repo, ".git", "repository Git directory")
    try:
        _scan(git_fd, "repository Git metadata")
        for mechanism in ("objects/info/alternates", "info/grafts", "shallow", "commondir"):
            entry = _entry(git_fd, mechanism, "repository Git metadata")
            if entry is not None:
                _fail("repository Git metadata is unsafe")
        replace = _entry(git_fd, "refs/replace", "repository Git metadata")
        if replace is not None:
            replace_fd = _dirat(git_fd, "refs/replace", "repository Git metadata")
            try:
                if os.listdir(replace_fd): _fail("repository Git metadata is unsafe")
            finally: os.close(replace_fd)
        packed = _entry(git_fd, "packed-refs", "repository Git metadata")
        if packed is not None and b"refs/replace/" in _readat(git_fd, "packed-refs", "repository Git metadata"):
            _fail("repository Git metadata is unsafe")
        config = _entry(git_fd, "config", "repository Git configuration")
        if config is None or not stat.S_ISREG(config.st_mode): _fail("repository Git configuration is unsafe")
        _readat(git_fd, "config", "repository Git configuration")
    finally:
        os.close(git_fd)
    _validate_local_git_config(repo, contract)
    expected=contract["expected"]; base=contract["base"]["head"]; deviations=[]; head=_git(repo,"rev-parse","HEAD"); count=int(_git(repo,"rev-list","--count",f"{base}..HEAD")); changed=_git(repo,"diff","--no-ext-diff","--name-only",base,"HEAD").splitlines(); status=_git(repo,"status","--porcelain=v1","--untracked-files=all"); files, dirs=_scan(repo,"repository inventory",exclude_git=True)
    wanted=({x["destination"] for x in contract["members"]}-set(expected["forbidden_paths"]))|set(expected["required_files"]); hashes={}
    for name, wanted_hash in expected["required_files"].items():
        if _entry(repo, name, "required repository file") is None:
            hashes[name] = None; deviations.append(f"required_file:{name}"); continue
        hashes[name] = _sha(_readat(repo,name,"required repository file"))
        if hashes[name] != wanted_hash: deviations.append(f"required_file:{name}")
    for name in expected["forbidden_paths"]:
        if _entry(repo,name,"forbidden repository path") is not None: deviations.append(f"forbidden_path:{name}")
    if head != expected["final_head"]: deviations.append("final_head")
    if count != expected["commit_count_after_base"]: deviations.append("commit_count")
    if changed != expected["changed_paths"]: deviations.append("changed_paths")
    if files != wanted or dirs != _ancestors(wanted): deviations.append("repository_inventory")
    clean=status==""
    if clean != expected["clean_worktree"]: deviations.append("clean_worktree")
    return {"repository":display,"base_head":base,"final_head":head,"commit_count_after_base":count,"changed_paths":changed,"repository_paths":sorted(files),"repository_directories":sorted(dirs),"file_hashes":hashes,"clean_worktree":clean,"semantic_pass":not deviations,"deviations":deviations}
def _validate_local_git_config(repo, contract):
    raw = _git(repo, "config", "--local", "--no-includes", "--null", "--list")
    expected = {
        "core.repositoryformatversion":"0","core.filemode":"true","core.bare":"false","core.logallrefupdates":"true","core.ignorecase":"false","core.precomposeunicode":"false","core.hookspath":os.devnull,"core.fsmonitor":"false","core.untrackedcache":"false",
        "user.name":contract["base"]["author_name"],"user.email":contract["base"]["author_email"],"commit.gpgsign":"false",
    }
    observed = {}
    for record in raw.split("\0"):
        if not record: continue
        if "\n" not in record: _fail("repository Git configuration is malformed")
        key, value = record.split("\n", 1)
        if key in observed: _fail("repository Git configuration is unsafe")
        observed[key] = value
    if observed != expected: _fail("repository Git configuration is unsafe")
def _evidence(repo, display, data, contract, events, response):
    commands = _commands(events, contract)
    outcomes = [next(item for item in commands if item["command"] == milestone) for milestone in contract["required_milestones"]]
    return {"schema_version":1,"fixture_id":contract["fixture_id"],"contract_sha256":_sha(data),"event_sha256":_sha(events),"response_sha256":_sha(response),"commands":commands,"required_milestone_outcomes":outcomes,**_inspect(repo,display,contract)}
def _fixture_open_hook(root, admin, repository): del root,admin,repository
def _source_auth_hook(source): del source
def _close(*fds):
    error = None
    for fd in fds:
        if fd < 0:
            continue
        try:
            os.close(fd)
        except OSError as close_error:
            if error is None:
                error = close_error
    if error is not None:
        raise FixtureContractError("cannot close fixture descriptor") from error
def prepare_fixture(contract_path: Path, root: Path) -> dict:
    rootfd=admin=repo=-1
    try:
        rootpath=Path(os.path.abspath(os.fspath(root))); broad={Path("/"),Path(tempfile.gettempdir()),Path("/private/tmp"),Path.cwd().resolve()}
        if rootpath in broad or os.path.lexists(rootpath): _fail("fixture root is unsafe or already exists")
        contract,data,members=_contract(contract_path); rootpath.mkdir(mode=0o700); rootfd=_dir(rootpath,"fixture root"); os.mkdir("admin",0o700,dir_fd=rootfd); admin=_dirat(rootfd,"admin","admin root"); os.mkdir("repository",0o700,dir_fd=rootfd); repo=_dirat(rootfd,"repository","repository root")
        for m in members: _write_rel(repo,m["destination"],m["bytes"]); _chmod(repo,m["destination"],0o555 if m["executable"] else 0o444)
        _git(repo,"init","-q","--template="); base=contract["base"]
        for key,value in (("core.fileMode","true"),("core.ignoreCase","false"),("core.precomposeUnicode","false"),("user.name",base["author_name"]),("user.email",base["author_email"]),("core.hooksPath",os.devnull),("commit.gpgSign","false"),("core.fsmonitor","false"),("core.untrackedCache","false")): _git(repo,"config",key,value)
        _git(repo,"add","--", "."); env={"GIT_AUTHOR_NAME":base["author_name"],"GIT_AUTHOR_EMAIL":base["author_email"],"GIT_COMMITTER_NAME":base["author_name"],"GIT_COMMITTER_EMAIL":base["author_email"],"GIT_AUTHOR_DATE":base["timestamp"],"GIT_COMMITTER_DATE":base["timestamp"]}; _git(repo,"commit","-q","-m",base["subject"],env=env); head=_git(repo,"rev-parse","HEAD")
        if head != base["head"]: _fail("deterministic base head mismatch")
        for m in members: _chmod(repo,m["destination"],0o755 if m["executable"] else 0o644)
        _fixture_open_hook(rootfd,admin,repo); observation={"schema_version":1,"fixture_id":contract["fixture_id"],"base_head":head,"base_timestamp":base["timestamp"],"base_subject":base["subject"]}; _write(admin,"contract.json",data); _write(admin,"source-manifest.json",_canon(_manifest(contract,members))); _write(admin,"base-observation.json",_canon(observation)); _static(admin,repo,contract_path,False)
        return {"repository":str(rootpath/"repository"),"fixture_id":contract["fixture_id"],"base_head":head,"execution_gate":contract["execution_gate"]}
    except FixtureContractError: raise
    except (OSError,TypeError,ValueError,KeyError) as error: raise FixtureContractError("cannot prepare fixture") from error
    finally: _close(repo,admin,rootfd)
def _opened(root):
    rootpath=Path(os.path.abspath(os.fspath(root))); broad={Path("/"),Path(tempfile.gettempdir()),Path("/private/tmp"),Path.cwd().resolve()}
    if rootpath in broad: _fail("fixture root is unsafe")
    rootfd=_dir(rootpath,"fixture root")
    try:
        names = set(os.listdir(rootfd))
        if names != {"admin", "repository"}: _fail("fixture root inventory mismatch")
        for name in names:
            info = os.stat(name, dir_fd=rootfd, follow_symlinks=False)
            if not stat.S_ISDIR(info.st_mode): _fail("fixture root inventory mismatch")
    except BaseException:
        os.close(rootfd); raise
    admin = repo = -1
    try:
        admin = _dirat(rootfd,"admin","admin root")
        repo = _dirat(rootfd,"repository","repository root")
        return rootpath,rootfd,admin,repo
    except BaseException:
        _close(repo, admin, rootfd)
        raise
def record_fixture_execution(contract_path: Path, root: Path, events: bytes, response: bytes) -> dict:
    rootfd=admin=repo=-1
    try:
        if not isinstance(events,bytes) or not isinstance(response,bytes) or not response: _fail("events and nonempty response must be bytes")
        rootpath,rootfd,admin,repo=_opened(root); _fixture_open_hook(rootfd,admin,repo); contract,data,_=_static(admin,repo,contract_path,False); evidence=_evidence(repo,str(rootpath/"repository"),data,contract,events,response); _write(admin,"events.jsonl",events); _write(admin,"response.bin",response); _write(admin,"evidence.json",_canon(evidence)); terminal={"schema_version":1,"fixture_id":contract["fixture_id"],"contract_sha256":_sha(data),"evidence_sha256":_sha(_canon(evidence)),"event_sha256":_sha(events),"response_sha256":_sha(response),"semantic_pass":evidence["semantic_pass"]}; _write(admin,"terminal.json",_canon(terminal)); return evidence
    except FixtureContractError: raise
    except (OSError,TypeError,ValueError,KeyError) as error: raise FixtureContractError("cannot record fixture execution") from error
    finally: _close(repo,admin,rootfd)
def verify_fixture(contract_path: Path, root: Path) -> dict:
    rootfd=admin=repo=-1
    try:
        rootpath,rootfd,admin,repo=_opened(root); _fixture_open_hook(rootfd,admin,repo); contract,data,_=_static(admin,repo,contract_path,True); events=_readat(admin,"events.jsonl","events"); response=_readat(admin,"response.bin","response")
        if not response: _fail("recorded response is empty")
        evidence=_evidence(repo,str(rootpath/"repository"),data,contract,events,response); recorded=_json(_readat(admin,"evidence.json","evidence"),"evidence")
        if _canon(recorded)!=_canon(evidence): _fail("recorded evidence mismatch")
        terminal=_json(_readat(admin,"terminal.json","terminal"),"terminal"); wanted={"schema_version":1,"fixture_id":contract["fixture_id"],"contract_sha256":_sha(data),"evidence_sha256":_sha(_canon(evidence)),"event_sha256":_sha(events),"response_sha256":_sha(response),"semantic_pass":evidence["semantic_pass"]}
        if _canon(terminal)!=_canon(wanted): _fail("terminal record mismatch")
        return evidence
    except FixtureContractError: raise
    except (OSError,TypeError,ValueError,KeyError) as error: raise FixtureContractError("cannot verify fixture") from error
    finally: _close(repo,admin,rootfd)
