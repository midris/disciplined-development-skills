"""One-shot CW input audit; uses existing preparation helpers, never a provider."""
from pathlib import Path
import hashlib
import json
import subprocess
import tempfile

from skilltest.config import load_config
from skilltest.workspace import create_run, prepare_workspace

repo = Path.cwd()
scratch = Path(__file__).resolve().parent
prepared_root = scratch / "prepared"
prepared_root.mkdir(exist_ok=True)
tempfile.tempdir = str(prepared_root)
pilot = repo / "skill-validation/pilot"
labels = ["cw-01/no-dd", "cw-01/current-dd", "cw-01/discovery", "cw-17/discovery"]
configs = {label: load_config(pilot / label / "test.json") for label in labels}
digest = lambda data: hashlib.sha256(data).hexdigest()
inventory = lambda config: {str(f.target): digest(f.source.read_bytes()) for f in config.fixtures}
maps = {label: inventory(config) for label, config in configs.items()}
reference = load_config(pilot / "dr-05/current-dd/test.json")
reference_map = {target: value for target, value in inventory(reference).items() if target.startswith(".agents/skills/")}
assert maps["cw-01/current-dd"] == maps["cw-01/discovery"] == maps["cw-17/discovery"] == reference_map
common = {str(f.target): digest(f.source.read_bytes()) for f in reference.fixtures if "/superpowers/" in str(f.source)}
assert maps["cw-01/no-dd"] == common and len(common) == 4
assert len(reference_map) == 13
dd = [f for f in reference.fixtures if "/inputs/dd/" in str(f.source)]
assert len(dd) == 9
for fixture in dd:
    relative = str(fixture.source.relative_to(repo))
    assert fixture.source.read_bytes() == subprocess.check_output(["git", "show", "f39d721:" + relative])
    assert fixture.source.read_bytes() == subprocess.check_output(["git", "show", "ca14bbe:skills/" + fixture.source.parent.name + "/SKILL.md"])
for fixture in reference.fixtures:
    if "/inputs/superpowers/" in str(fixture.source):
        relative = str(fixture.source.relative_to(repo))
        assert fixture.source.read_bytes() == subprocess.check_output(["git", "show", "f39d721:" + relative])
prefix = "Read {{fixture_dir}}/.agents/skills/concise-writing/SKILL.md completely and follow it as binding guidance for this task.\n\n"
base = configs["cw-01/no-dd"].prompt.read_text()
assert configs["cw-01/current-dd"].prompt.read_text() == prefix + base
assert configs["cw-01/discovery"].prompt.read_text() == base
assert (pilot / "cw-01/no-dd/rubric.md").read_bytes() == (pilot / "cw-01/current-dd/rubric.md").read_bytes()
source = (repo / "skill-validation/scenarios/concise-writing/cw-01/prompt.md").read_text().split("Tighten this reader-facing", 1)[1].rstrip()
assert ("Tighten this reader-facing" + source) in base
request = (repo / "skill-validation/scenarios/concise-writing/cw-17/prompt.md").read_text().split("User request: ", 1)[1].strip()
assert configs["cw-17/discovery"].prompt.read_text().startswith(request + "\n")
for label in ("cw-01/discovery", "cw-17/discovery"):
    prompt = configs[label].prompt.read_text().lower()
    assert not any(token in prompt for token in ("skill", ".agents", ".claude", "routing", "cw-"))
report = {"kind": "provider-free CW preparation, not qualification or a model observation",
          "source_head_before_freeze": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
          "configs": {}}
for label, config in configs.items():
    assert (config.execution.provider, config.execution.model, config.execution.effort) == ("codex", "gpt-5.6-sol", "low")
    assert all(not f.source.is_symlink() and f.source.is_relative_to(pilot / "inputs") for f in config.fixtures)
    assert all(str(f.target).startswith(".agents/skills/") for f in config.fixtures)
    context = create_run(config)
    prepared = prepare_workspace(context, config)
    actual = {str(p.relative_to(context.fixture_dir)): digest(p.read_bytes()) for p in context.fixture_dir.rglob("*") if p.is_file()}
    assert actual == maps[label]
    assert not any(context.evidence_dir.iterdir())
    assert not context.final_output_path.exists() and not context.result_path.exists()
    rendered = config.prompt.read_text().replace("{{fixture_dir}}", str(context.fixture_dir.resolve())).encode()
    assert prepared.prompt_bytes == rendered
    report["configs"][label] = {
        "fixture_hashes": actual,
        "config_sha256": digest(config.config_bytes),
        "prompt_sha256": digest(config.prompt.read_bytes()),
        "rubric_sha256": digest((pilot / label / "rubric.md").read_bytes()),
        "rendered_prompt_sha256": digest(prepared.prompt_bytes),
        "prepared_fixture": str(context.fixture_dir),
        "withholding": "exact fixture inventory; no rubric, evaluator docs, hooks or credentials",
    }
print(json.dumps(report, indent=2, sort_keys=True))
