"""Reconstruct worked outputs and run offline checks in a new disposable directory."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import random
import shutil
import subprocess
import sys

from reader_payload import catalog_payload, payload_bytes, reader_prompt

CASES = Path(__file__).resolve().parent
PROJECT_FILES = {
    "catalog-review": {"catalog-spec.md"},
    "dispatch-hold": {"dispatch-spec.md", "morning.py", "overflow.py"},
    "scope-trim": {"launch-plan.md"},
    "quota-grace": {"quota.py", "test_quota.py"},
    "export-deferral": {"release-plan.md"},
    "helper-rename": {"quota.py", "test_quota.py"},
    "repeated-review": {"ingest.py", "labels.py", "quota.py", "test_service.py"},
}


def run(args, cwd, expect_pass=True):
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=30)
    if (result.returncode == 0) != expect_pass:
        raise RuntimeError(f"{args} exited {result.returncode}\n{result.stdout}\n{result.stderr}")
    if not expect_pass and "FAIL:" not in result.stderr and "ERROR:" not in result.stderr:
        raise RuntimeError(f"Expected a test failure, got {result.stderr}")
    return result


def replace(path, before, after):
    text = path.read_text()
    if text.count(before) != 1:
        raise ValueError(f"Ambiguous worked-example edit in {path}")
    path.write_text(text.replace(before, after))


def construct(case, variant, tree):
    source = CASES / case
    shutil.copytree(source / "fixture", tree, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
    if case == "repeated-review":
        # The attachment must describe an actual change ending at the supplied tree.
        patch = str(source / "change.patch")
        run(["git", "apply", "--check", "--reverse", patch], tree)
    if variant not in {"starting", "reply-only"}:
        args = ["git", "apply"]
        if variant == "guard-only":
            args.append("--include=ingest.py")
        run([*args, str(source / "example.patch")], tree)

    if variant == "credit-only":
        replace(tree / "catalog-spec.md", " so proof corrections line up with the room sheets. Visitors can look up titles in the index.", ".")
    elif variant == "order-reason-only":
        replace(tree / "catalog-spec.md", " Visitors can look up titles in the index.", "")
    elif variant == "wrong-authority":
        replace(tree / "catalog-spec.md", "until the lender amends it", "until the publisher amends it")
    elif variant in {"bare", "lost-policy", "handoff-only-policy", "full-copies"}:
        spec = tree / "dispatch-spec.md"
        policy, = (line for line in spec.read_text().splitlines() if line.startswith("A held parcel"))
        for name in ("morning.py", "overflow.py"):
            replace(tree / name, "    # Loaded parcels stay with their dispatcher. See dispatch-spec.md, Holds.\n",
                    f"    # {policy}\n" if variant == "full-copies" else "")
        if variant in {"lost-policy", "handoff-only-policy"}:
            replace(spec, policy, "Keep loaded parcels assigned and omit held parcels from new trips.")
    elif variant == "keyword-regression":
        path = tree / "overflow.py"
        path.write_text(path.read_text().replace("already_loaded", "assigned"))
    elif variant == "ready-only":
        replace(tree / "overflow.py", 'status not in {"manual_hold", "address_check"}', 'status == "ready"')
    elif variant == "conflicting-copy":
        replace(tree / "overflow.py", "Loaded parcels stay with their dispatcher.",
                "Remove even loaded parcels from assigned trips until the hold clears.")
    elif variant == "loaded-regression":
        replace(tree / "morning.py", "already_loaded or status not in", "status not in")
    elif variant == "local-reasons":
        for name in ("morning.py", "overflow.py"):
            replace(tree / name, "Loaded parcels stay with their dispatcher. See dispatch-spec.md, Holds.",
                    "A held parcel may change address. Leave loaded parcels assigned so their dispatcher can redirect them.")
    elif variant == "title-story":
        replace(tree / "overflow.py", 'TITLE = "Overflow dispatch"',
                '# The carrier contract mandates this exact title.\nTITLE = "Overflow dispatch"')
    elif variant in {"gate-only", "implicit-week", "lost-impact", "silent-cut"}:
        plan = tree / "launch-plan.md"
        if variant == "gate-only":
            replace(plan, "Reconsider both once Finance agrees on a close rule.",
                    "Both are deferred until Finance agrees on a close rule.")
        elif variant == "implicit-week":
            replace(plan, " by hand for such a week.", " by hand.")
        elif variant == "lost-impact":
            replace(plan, " Until then, Support may need to compare daily reports by hand for such a week.", "")
        else:
            before, rest = plan.read_text().split("## Deferred", 1)
            plan.write_text(before + "## After launch" + rest.split("## After launch", 1)[1])
    elif variant in {"collective-scope", "collective-no-count"}:
        replace(tree / "launch-plan.md", "Defer weekly reconciliation and weekly discrepancy alerts",
                "For daily reconciliation and discrepancy alerts, defer their weekly versions")
        if variant == "collective-no-count":
            replace(tree / "launch-plan.md", "Reconsider both once", "Reconsider weekly scope once")
    elif variant == "lost-weekly-alert":
        replace(tree / "launch-plan.md", "weekly reconciliation and weekly discrepancy alerts", "weekly reconciliation")
    elif variant == "firm-promise":
        replace(tree / "launch-plan.md", "Reconsider both once", "Ship both as soon as")
    elif variant == "weekly-duty":
        replace(tree / "launch-plan.md", "may need to compare daily reports by hand for such a week",
                "must compare daily reports by hand every week")
    elif variant == "summary-only-reason":
        plan = tree / "launch-plan.md"
        before, rest = plan.read_text().split("Defer weekly reconciliation", 1)
        plan.write_text(before + "Defer weekly reconciliation and weekly discrepancy alerts.\n\n"
                        + rest.split("\n\n", 1)[1])
    elif variant == "expiry-bug":
        replace(tree / "quota.py", "now < change.effective_at + 60", "now <= change.effective_at + 60")
    elif variant == "new-token-bug":
        replace(tree / "quota.py", " and issued_at < change.effective_at", "")
    elif variant == "lookup-time-bug":
        replace(tree / "quota.py", "issued_at < change.effective_at", "issued_at < now")
    elif variant == "recent-only":
        replace(tree / "quota.py", "issued_at < change.effective_at",
                "change.effective_at - 60 <= issued_at < change.effective_at")
    elif variant == "assumed-lifetime":
        replace(tree / "quota.py", "issued_at < change.effective_at",
                "issued_at < change.effective_at and now - issued_at < 300")
    elif variant == "behavior-only":
        path = tree / "quota.py"
        path.write_text("".join(line for line in path.read_text().splitlines(True)
                                if not line.lstrip().startswith("#")))
    elif variant == "pr-only":
        replace(tree / "release-plan.md",
                " XML customers must wait until the partner approves a stable schema because it is still changing.", "")
    elif variant == "invented-date":
        replace(tree / "release-plan.md", "until the partner approves a stable schema because it is still changing",
                "until our next quarterly release")
    elif variant == "rename-clutter":
        replace(tree / "quota.py", "def _normalize_units(value):",
                "# The new name is required by the billing wire protocol.\ndef _normalize_units(value):")
    elif variant == "lost-reason":
        replace(tree / "quota.py", "    # The billing feed sometimes sends negative corrections. They cannot\n"
                "    # authorize extra work, so the admission service treats them as zero.\n", "")
    elif variant == "missed-caller":
        replace(tree / "quota.py", "_normalize_units(value) - consumed", "_quota_units(value) - consumed")
    elif variant == "batch-regression":
        replace(tree / "ingest.py", "        persist(store, item)", "        ingest(store, item, False)")
    elif variant == "unnecessary-comment":
        replace(tree / "labels.py", "def _format_count(count):",
                "# The billing contract requires this exact helper name.\ndef _format_count(count):")


def qualify(output):
    output.mkdir()
    reader = output / "reader"
    reader.mkdir()
    packets = output / "first-read"
    packets.mkdir()
    # Labels reveal neither the variant nor its expected judgment in the first pass.
    samples = [
        ("quota-grace", v) for v in ("starting", "complete", "expiry-bug", "new-token-bug", "lookup-time-bug", "recent-only", "assumed-lifetime", "behavior-only")
    ] + [
        ("export-deferral", v) for v in ("complete", "pr-only", "invented-date")
    ] + [
        ("helper-rename", v) for v in ("complete", "rename-clutter", "lost-reason", "missed-caller")
    ] + [
        ("repeated-review", v) for v in ("complete", "reply-only", "guard-only", "batch-regression", "unnecessary-comment")
    ]
    samples.extend(("dispatch-hold", v) for v in
                   ("complete", "local-reasons", "conflicting-copy", "loaded-regression", "title-story",
                    "bare", "lost-policy", "handoff-only-policy", "full-copies", "ready-only", "keyword-regression"))
    samples.extend(("scope-trim", v) for v in
                   ("complete", "lost-weekly-alert", "firm-promise", "weekly-duty", "summary-only-reason",
                    "gate-only", "implicit-week", "lost-impact", "silent-cut", "collective-scope", "collective-no-count"))
    samples.extend(("catalog-review", v) for v in ("complete", "credit-only", "order-reason-only", "wrong-authority"))
    random.SystemRandom().shuffle(samples)
    # Offline configs exercise the same source-to-target classification as live runs.
    configs = output / "configs"
    configs.mkdir()
    for case, project_files in PROJECT_FILES.items():
        case_dir = CASES / case
        sources = [(case_dir / "fixture" / name, name) for name in sorted(project_files)]
        sources.append((case_dir / "task.md", "TASK.md"))
        if case == "repeated-review":
            sources.append((case_dir / "change.patch", "review-input/change.patch"))
        config = {
            "schema_version": "0.2", "id": case, "prompt": os.path.relpath(case_dir / "task.md", configs),
            "fixtures": [{"source": os.path.relpath(source, configs), "target": target} for source, target in sources],
            "execution": {"provider": "claude", "model": "claude-opus-5-5", "effort": "low"},
        }
        (configs / f"{case}.json").write_text(json.dumps(config))
    key = {}
    for number, (case, variant) in enumerate(samples, 1):
        label = f"project-{number:02}"
        tree = reader / label
        construct(case, variant, tree)
        checks = {}
        if case in {"quota-grace", "repeated-review", "helper-rename"}:
            ok = variant not in {"missed-caller", "batch-regression"}
            run([sys.executable, "-B", "-m", "unittest", "discover"], tree, ok)
            checks["project tests"] = "pass" if ok else "fail"
        if case in {"quota-grace", "repeated-review"}:
            ok = variant not in {"starting", "expiry-bug", "new-token-bug", "lookup-time-bug", "recent-only", "assumed-lifetime"}
            run([sys.executable, "-I", "-B", str(CASES / "quota-grace/replay.py"), str(tree)], tree, ok)
            checks["quota replay"] = "pass" if ok else "fail"
        if case == "dispatch-hold":
            ok = variant not in {"loaded-regression", "ready-only", "keyword-regression"}
            run([sys.executable, "-I", "-B", str(CASES / case / "replay.py"), str(tree)], tree, ok)
            checks["dispatch replay"] = "pass" if ok else "fail"
        members = {p.relative_to(tree).as_posix() for p in tree.rglob("*") if p.is_file()}
        expected = PROJECT_FILES[case]
        if members != expected:
            raise RuntimeError(f"Unexpected worked-project contents: {members ^ expected}")
        shutil.copyfile(CASES / case / "task.md", tree / "TASK.md")
        if case == "repeated-review":
            attachment = (CASES / case / "change.patch").read_bytes()
            target = tree / "review-input/change.patch"
            target.parent.mkdir()
            target.write_bytes(attachment)
        classifications = {}
        if case == "catalog-review" and variant == "credit-only":
            (tree / "reply-to-editor.md").write_text("Room order matches the proof sheets.")
            classifications["reply-to-editor.md"] = "correspondence"
        excluded = {}
        payload = payload_bytes(tree, configs / f"{case}.json", CASES / case / "fixture", exclusions=excluded)
        if case == "catalog-review":
            payload = catalog_payload(payload, classifications, excluded)
        if json.loads(payload) != {name: (tree / name).read_bytes().decode() for name in expected}:
            raise ValueError(f"Reader projection differs from final project: {label}")
        (packets / f"{label}.json").write_bytes(payload)
        prompt = reader_prompt(payload)
        (packets / f"{label}.txt").write_bytes(prompt)
        if case == "catalog-review":
            question = (CASES / case / "maintenance-question.txt").read_bytes()
            decision_dir = output / "decision-read"
            decision_dir.mkdir(exist_ok=True)
            (decision_dir / f"{label}.txt").write_bytes(question + payload)
        entry = {"case": case, "variant": variant, "checks": checks,
                 "payload_sha256": hashlib.sha256(payload).hexdigest(),
                 "prompt_sha256": hashlib.sha256(prompt).hexdigest(),
                 "excluded_paths": excluded}
        if case == "catalog-review":
            entry["response"] = ("Keep the approved credit until the lender amends the form. Room order matches the proof sheets; visitors have the title index.")
        elif case == "export-deferral":
            entry["response"] = ("CSV and JSON stay in v1. XML customers will wait until the partner "
                                 "approves a stable schema because the schema is still changing.")
        elif variant == "handoff-only-policy":
            entry["response"] = ("Held parcels can change destination. Keeping them off new trips avoids collection "
                                 "for the wrong address. Already-loaded parcels stay assigned so dispatch can redirect them.")
        elif case == "scope-trim":
            entry["response"] = ("Both weekly items await Finance's cross-period close rule. Reconsider them "
                                 "on agreement. Support may need to compare daily reports for an affected week.")
        elif variant == "reply-only":
            entry["response"] = "The shared helper serves approved batches. A third interactive caller would prompt a redesign."
        key[label] = entry
    (output / "reconciliation.json").write_text(json.dumps(key, indent=2) + "\n")
    print(f"Qualified {len(samples)} constructed outputs in {output}. Single-output first-read payloads are in {packets}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="New directory outside the checkout")
    path = parser.parse_args().output.resolve()
    repo = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], cwd=CASES, text=True).strip())
    if path == repo or repo in path.parents:
        parser.error("Choose an external scratch directory")
    qualify(path)
