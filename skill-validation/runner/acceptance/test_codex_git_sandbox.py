"""Opt-in installed-Codex sandbox qualification; no auth or model invocation."""

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import tomllib

import pytest

from skilltest.providers import ProviderRequest, _arguments


# Break: the adapter's actual policy blocks Git, expands the grant beyond the
# fixture, loses evidence access, or permits command network access.
def test_fixture_git_commit_preserves_protected_paths_and_network():
    destination = os.environ.get("SKILLTEST_SANDBOX_EVIDENCE_DIR")
    if not destination:
        pytest.skip("set SKILLTEST_SANDBOX_EVIDENCE_DIR to retain provider-free qualification")
    if sys.platform != "darwin":
        pytest.skip("this installed sandbox qualification targets macOS")
    executable = shutil.which("codex")
    assert executable, "Codex must be installed"
    root = Path(tempfile.mkdtemp(prefix="codex-git-", dir=destination)).resolve()
    fixture, evidence = root / "workspace/fixture", root / "workspace/evidence"
    for path in (fixture, evidence, root / "home", root / "profile", root / "tmp"):
        path.mkdir(parents=True)
    environment = {
        "HOME": str(root / "home"), "CODEX_HOME": str(root / "profile"),
        "TMPDIR": str(root / "tmp"),
        "PATH": f"{Path(executable).parent}:/usr/bin:/bin:/usr/sbin:/sbin",
        "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
    }
    sources = {
        "README.md": "[Guide](docs/guide.md#old-heading)\n",
        "docs/guide.md": "# Old heading\n\nCheck the queue before restarting.\n",
        "docs/incidents.md": "[Restart](guide.md#old-heading)\n",
    }
    for name, content in sources.items():
        path = fixture / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    protected = [fixture / ".codex/marker", fixture / ".agents/marker", evidence / ".git/marker"]
    for path in protected:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("protected\n")
    subprocess.run(["/usr/bin/git", "init", "--quiet", "--template=", str(fixture)],
                   env=environment, check=True, capture_output=True, timeout=30)
    request = ProviderRequest(fixture.parent, b"unused", root / "final.txt", "codex", "gpt-5.6-sol", "medium")
    arguments = _arguments(request, executable=executable)
    overrides = [arguments[i+1] for i, arg in enumerate(arguments) if arg == "-c"]
    config = tomllib.loads("\n".join(overrides))
    (root / "provider-arguments.json").write_text(json.dumps(arguments, indent=2) + "\n")
    assert "--sandbox" not in arguments, "legacy sandbox would override the explicit profile"
    # Select the same default and pass every emitted config override unchanged.
    # No separately reconstructed test policy may stand in for the adapter's policy.
    command = [executable, "sandbox", "-P", config["default_permissions"], "-C", str(fixture)]
    for value in overrides:
        command.extend(["-c", value])
    inner = r'''
import errno, json, socket, subprocess, sys
from pathlib import Path
fixture, evidence = Path.cwd(), Path(sys.argv[1])
sources = ["README.md", "docs/guide.md", "docs/incidents.md"]
operations = []
def git(*args):
    result = subprocess.run(["/usr/bin/git", *args], capture_output=True, text=True, timeout=15)
    operations.append({"argv": list(args), "exit_code": result.returncode,
                       "stdout": result.stdout, "stderr": result.stderr})
    assert result.returncode == 0, operations[-1]
    return result.stdout
try:
    git("add", "--", *sources)
    assert git("show", ":docs/guide.md") == "# Old heading\n\nCheck the queue before restarting.\n"
    for name in sources:
        path = fixture / name
        path.write_text(path.read_text().replace("Old heading", "Restart").replace("old-heading", "restart"))
    difference = git("diff", "--", *sources)
    assert "-# Old heading" in difference and "+# Restart" in difference
    assert "docs/guide.md#restart" in (fixture / "README.md").read_text()
    assert "guide.md#restart" in (fixture / "docs/incidents.md").read_text()
    assert (fixture / "docs/guide.md").read_text().startswith("# Restart\n")
    (evidence / "probe.txt").write_text("evidence write\n")
    denied = []
    for path in [fixture / ".codex/marker", fixture / ".agents/marker", evidence / ".git/marker"]:
        try:
            path.write_text("unexpected write\n")
        except OSError as error:
            assert error.errno in (errno.EPERM, errno.EACCES), (str(path), repr(error))
            denied.append(str(path.relative_to(fixture.parent)))
        else:
            raise AssertionError("protected path writable: " + str(path))
    with socket.socket() as probe:
        try:
            probe.bind(("127.0.0.1", 0))
        except OSError as error:
            assert error.errno in (errno.EPERM, errno.EACCES), repr(error)
        else:
            raise AssertionError("network bind unexpectedly permitted")
    git("add", "--", *sources)
    git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
        "-c", "commit.gpgsign=false", "commit", "--quiet", "-m", "Reconcile guide links")
    assert git("rev-list", "--count", "HEAD").strip() == "1"
    assert sorted(git("ls-tree", "-r", "--name-only", "HEAD").splitlines()) == sorted(sources)
    assert git("diff", "HEAD", "--", *sources) == ""
    print(json.dumps({"status": "PASS", "protected_writes_denied": denied,
                      "network_bind_denied": True, "root_commit": git("rev-parse", "HEAD").strip()}))
finally:
    (evidence / "operations.json").write_text(json.dumps(operations, indent=2) + "\n")
'''
    (root / "probe.py").write_text(inner)
    command.extend(["--", sys.executable, str(root / "probe.py"), str(evidence)])
    (root / "sandbox-command.json").write_text(json.dumps(command, indent=2) + "\n")
    result = subprocess.run(command, cwd=fixture, env=environment, capture_output=True, text=True, timeout=60)
    (root / "stdout.txt").write_text(result.stdout)
    (root / "stderr.txt").write_text(result.stderr)
    version = subprocess.run([executable, "--version"], env=environment, capture_output=True, text=True, timeout=30)
    record = {"exit_code": result.returncode, "provider_calls": 0, "cli_version": version.stdout.strip(),
              "cli_sha256": hashlib.sha256(Path(executable).read_bytes()).hexdigest()}
    (root / "result.json").write_text(json.dumps(record, indent=2) + "\n")
    assert result.returncode == 0, f"{root}: {result.stderr}\n{result.stdout}"
    assert json.loads(result.stdout)["status"] == "PASS"
    assert all(path.read_text() == "protected\n" for path in protected)
    assert (evidence / "probe.txt").read_text() == "evidence write\n"
    assert not (root / "profile/auth.json").exists()
    print(f"Retained sandbox qualification: {root}")
