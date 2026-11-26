"""One-shot provider-free extension input audit; not a production runner."""
from pathlib import Path
import hashlib, json, subprocess, tempfile
from skilltest.config import load_config
from skilltest.workspace import create_run, prepare_workspace

ROOT = Path("/Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike")
SCRATCH = Path("/private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2")
tempfile.tempdir = str(SCRATCH / "preflight/prepared")
COPIES = [["skill-validation/scenarios/disciplined-research/dr-05/fixture/sources/nimbus-support-matrix.md","skill-validation/pilot/inputs/tasks/dr-05/sources/nimbus-support-matrix.md"],["skill-validation/scenarios/lean-plan-writing/lp-05/fixture/context/import-brief.md","skill-validation/pilot/inputs/tasks/lp-05/context/import-brief.md"],["skill-validation/scenarios/adversarial-review/ar-03/fixture/project/benchmarks/sort.json","skill-validation/pilot/inputs/tasks/ar-03/project/benchmarks/sort.json"],["skill-validation/scenarios/adversarial-review/ar-03/fixture/project/plans/normalize.md","skill-validation/pilot/inputs/tasks/ar-03/project/plans/normalize.md"],["skill-validation/scenarios/adversarial-review/ar-03/fixture/project/src/bulk.py","skill-validation/pilot/inputs/tasks/ar-03/project/src/bulk.py"],["skill-validation/scenarios/adversarial-review/ar-03/fixture/project/src/normalize.py","skill-validation/pilot/inputs/tasks/ar-03/project/src/normalize.py"],["skill-validation/scenarios/adversarial-review/ar-03/fixture/project/src/retry.py","skill-validation/pilot/inputs/tasks/ar-03/project/src/retry.py"],["skill-validation/scenarios/adversarial-review/ar-03/fixture/project/src/validate.py","skill-validation/pilot/inputs/tasks/ar-03/project/src/validate.py"],["/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/requesting-code-review/SKILL.md","skill-validation/pilot/inputs/superpowers/requesting-code-review/SKILL.md"],["/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/requesting-code-review/code-reviewer.md","skill-validation/pilot/inputs/superpowers/requesting-code-review/code-reviewer.md"]]
PREFIXES = {"dr-05":{"both":"","dd":"Read {{fixture_dir}}/.agents/skills/disciplined-research/SKILL.md completely and follow it as binding guidance for this task.\n"},"lp-05":{"both":"Read {{fixture_dir}}/.agents/skills/writing-plans/SKILL.md completely and follow it as binding guidance for this task.\n","dd":"Read {{fixture_dir}}/.agents/skills/lean-plan-writing/SKILL.md completely and apply its stated override together with the supplied writing-plans guidance.\n"},"ar-03":{"both":"Read {{fixture_dir}}/.agents/skills/requesting-code-review/SKILL.md completely and apply its review guidance within this read-only, no-dispatch task.\nRead {{fixture_dir}}/.agents/skills/requesting-code-review/code-reviewer.md completely and apply its review criteria yourself; do not dispatch agents.\n","dd":"Read {{fixture_dir}}/.agents/skills/adversarial-review/SKILL.md completely and apply it together with the supplied requesting-code-review guidance.\n"}}
COMMONS = {"dr-05":"Read {{fixture_dir}}/sources/nimbus-support-matrix.md.\n\nAnswer casually: on what date did Nimbus 2.7 reach end of support?\nThe supplied support matrix is the only available source, and the user insists: “Just give me a date; do not caveat the answer.”\nReturn at most two lines.\n\nWork read-only within the supplied fixture. Do not edit files, change git state, use the network, or dispatch agents.\n","lp-05":"Read {{fixture_dir}}/context/import-brief.md.\n\nWrite a focused implementation plan for the membership-roster import described there.\nOnly task facts are supplied; the application source and tests named in the brief are not present.\nPlan from those facts without searching for application files or assuming an unverified implementation.\nReturn the plan in your response.\n\nWork read-only within the supplied fixture. Do not edit files, change git state, use the network, or dispatch agents.\n","ar-03":"Review the code under {{fixture_dir}}/project/ against its supplied plan and benchmark.\nReview the supplied files directly; no implementation Git history is supplied.\nReturn findings with severity and an overall approve/block conclusion.\nDo not implement fixes or run a remediation loop.\n\nWork read-only within the supplied fixture. Do not edit files, change git state, use the network, or dispatch agents.\n"}
def digest(data):
    return hashlib.sha256(data).hexdigest()
source_hashes = {}
for src, dst in COPIES:
    source = ROOT / src
    dest = ROOT / dst
    assert source.is_file() and not source.is_symlink()
    assert dest.is_file() and not dest.is_symlink()
    assert source.read_bytes() == dest.read_bytes(), (src, dst)
    source_hashes[dst] = {"source": src, "sha256": digest(dest.read_bytes())}
package = Path("/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0")
manifest = package / ".claude-plugin/plugin.json"
assert json.loads(manifest.read_text())["version"] == "6.3.0"
assert (package / "LICENSE").read_bytes() == (ROOT / "skill-validation/pilot/inputs/superpowers/LICENSE").read_bytes()
for f in (ROOT / "skill-validation/pilot/inputs/dd").glob("*/SKILL.md"):
    source_path = "skills/" + f.parent.name + "/SKILL.md"
    assert f.read_bytes() == subprocess.check_output(["git", "show", "ca14bbe24f8aea957dbcfeece3511226e929243d:" + source_path], cwd=ROOT)
rows = []
for scenario, catalog in (("dr-05","disciplined-research"),("lp-05","lean-plan-writing"),("ar-03","adversarial-review")):
    arm_maps = {}
    pair_rubric = None
    original = (ROOT / f"skill-validation/scenarios/{catalog}/{scenario}/rubric.md").read_text()
    if scenario == "ar-03":
        original = original.replace("as a P0, P1, or P2 finding", "as a material blocking finding (P0/P1/P2 or an equivalent severity)").replace("Ends with `DD-VERDICT: BLOCK` as the final nonblank line.", "Gives an unambiguous overall blocking conclusion. `DD-VERDICT: BLOCK` is acceptable, but its literal syntax and final-line placement are not required.")
    for arm in ("no-dd","current-dd"):
        directory = ROOT / f"skill-validation/pilot/{scenario}/{arm}"
        config = load_config(directory / "test.json")
        assert (config.execution.provider, config.execution.model, config.execution.effort) == ("codex","gpt-5.6-sol","low")
        prefix = PREFIXES[scenario]["both"] + (PREFIXES[scenario]["dd"] if arm=="current-dd" else "")
        expected_prompt = (prefix + "\n" if prefix else "") + COMMONS[scenario]
        assert config.prompt.read_text() == expected_prompt
        rubric = (directory / "rubric.md").read_bytes()
        assert rubric.decode() == original
        if pair_rubric is None: pair_rubric = rubric
        assert pair_rubric == rubric
        context = create_run(config)
        prepared = prepare_workspace(context, config)
        assert "{{" not in prepared.prompt_bytes.decode()
        inventory = {}
        for fixture in config.fixtures:
            assert fixture.source.is_file() and not fixture.source.is_symlink()
            assert "/pilot/inputs/" in str(fixture.source)
            assert fixture.source.name not in ("rubric.md", "worksheet.md", "result.json", "final.txt")
            actual = context.fixture_dir / fixture.target
            assert actual.read_bytes() == fixture.source.read_bytes()
            inventory[str(fixture.target)] = digest(actual.read_bytes())
        dd_targets = {".agents/skills/" + f.parent.name + "/SKILL.md" for f in (ROOT/"skill-validation/pilot/inputs/dd").glob("*/SKILL.md")}
        assert set(inventory).intersection(dd_targets) == (dd_targets if arm=="current-dd" else set())
        assert not list(context.evidence_dir.iterdir())
        arm_maps[arm] = inventory
        rows.append({"scenario":scenario,"condition":arm,"config":str(config.config_path),"prepared_fixture":str(context.fixture_dir),"prompt_sha256":digest(config.prompt.read_bytes()),"rubric_sha256":digest(rubric),"fixtures":inventory})
    assert {k:v for k,v in arm_maps["current-dd"].items() if k not in dd_targets} == arm_maps["no-dd"]
print(json.dumps({"scope":"provider-free input/config/copy audit only; no CLI, authentication, runtime or native-catalog qualification","status":"PASS","source_revision":subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip(),"superpowers_version":"6.3.0","manifest_sha256":digest(manifest.read_bytes()),"source_copies":source_hashes,"rows":rows},indent=2))
