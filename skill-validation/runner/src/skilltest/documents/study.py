"""Reconcile explicit protocol scopes, attempts and categorical aggregates."""

from collections import Counter
from pathlib import Path
import re
from urllib.parse import unquote

from .formats import field, headings, lines_outside_fences, parse_json
from .references import canonical, regular_bytes

LINK = re.compile(r"\[([^\]\n]+)\]\(([^)\n]+)\)")


def tables(raw):
    lines = list(lines_outside_fences(raw))
    i = 0
    while i < len(lines) - 1:
        n, line = lines[i]
        if line.startswith("|") and re.fullmatch(r"[| :\-]+", lines[i + 1][1]) and "-" in lines[i + 1][1]:
            header = [s.strip() for s in line.strip("|").split("|")]
            rows = []
            i += 2
            while i < len(lines) and lines[i][1].startswith("|"):
                rows.append(
                    (
                        lines[i][0],
                        [s.strip() for s in lines[i][1].strip("|").split("|")],
                    )
                )
                i += 1
            yield n, header, rows
        else:
            i += 1


def link_parts(destination):
    """Split URL syntax before decoding literal filename characters."""
    target, _, anchor = destination.strip("<>").partition("#")
    return unquote(target), unquote(anchor)


def linked_files(raw, path):
    for n, line in lines_outside_fences(raw):
        for _, target in LINK.findall(line):
            target = link_parts(target)[0]
            if target and "://" not in target and not target.startswith("mailto:"):
                yield n, (Path(path).parent / target).resolve()


def index(value, path, ctx):
    seen_runs = set()
    seen_results = set()
    seen_slots = set()
    prior = {}
    records = []
    for n, a in enumerate(value["attempts"], 1):
        loc = f"attempts[{n - 1}]"
        record = None
        manifest = None
        assessment_manifest = None
        configs = {}
        if a["retry_of"] is not None:
            previous = prior.get(a["retry_of"])
            if (
                previous is None
                or (a["case_id"], a["condition"], a["repetition"])
                != (previous["case_id"], previous["condition"], previous["repetition"])
                or a["attempt_number"] != previous["attempt_number"] + 1
            ):
                ctx.error(
                    path,
                    loc,
                    "retry",
                    "Retry must refer to the preceding attempt of the same repetition",
                )
            if a["allocation"]["pool"] != "retry":
                ctx.error(path, loc, "allocation", "Retries charge the retry pool")
        elif a["attempt_number"] != 1:
            ctx.error(path, loc, "retry", "Initial attempt number must be 1")
        slot = (a["case_id"], a["condition"], a["repetition"], a["attempt_number"])
        if slot in seen_slots:
            ctx.error(path, loc, "duplicate-id", "Repeated attempt slot")
        seen_slots.add(slot)
        prior[a["attempt_id"]] = a
        for key, seen in [("run_id", seen_runs)]:
            if a[key] is not None:
                if a[key] in seen:
                    ctx.error(path, loc, "duplicate-id", f"Repeated {key}")
                seen.add(a[key])
        ctx.identity(
            a["authorization"]["artifact"],
            owner=path,
            loc=loc + ".authorization",
            frozen=True,
        )
        raw = ctx.identity(a["manifest"], owner=path, loc=loc + ".manifest", frozen=True)
        if raw is not None:
            manifest = ctx.document(raw, a["manifest"]["path"], "manifest", a["manifest"].get("version"))
            if manifest is not None:
                conditions, _, configs = ctx.manifest(manifest, a["manifest"]["path"])
                if manifest["study_id"] != value["study_id"] or manifest["case_id"] != a["case_id"]:
                    ctx.error(path, loc, "identity", "Attempt and manifest study/case differ")
                if a["condition"] not in conditions:
                    ctx.error(path, loc, "condition", "Attempt condition absent from manifest")
        invoked = None
        if a["bundle"]["path"] and a["bundle"]["inventory"]:
            try:
                ctx.inventory(a["bundle"], path)
                base = Path(a["bundle"]["path"])
                mechanical = parse_json(regular_bytes(base / "result.json"))
                if mechanical.get("schema_version") not in {"0.2", "0.3", "0.4", "0.5"}:
                    ctx.error(
                        path,
                        loc,
                        "unsupported-version",
                        "Unsupported runner result version",
                        "unsupported",
                    )
                if mechanical.get("run_id") != a["run_id"]:
                    ctx.error(path, loc, "run-identity", "Runner and attempt IDs differ")
                config = configs.get(a["condition"])
                if config is not None:
                    if mechanical.get("test", {}).get("id") != config["id"]:
                        ctx.error(
                            path,
                            loc,
                            "configuration",
                            "Runner test ID differs from configuration ID",
                        )
                    if parse_json(regular_bytes(base / "config.json")) != config:
                        ctx.error(
                            path,
                            loc,
                            "configuration",
                            "Retained configuration differs from frozen input",
                        )
                invoked = mechanical.get("execution", {}).get("invocation_started")
                if type(invoked) is not bool:
                    ctx.error(
                        path,
                        loc,
                        "allocation",
                        "Invocation charge cannot be verified without runner invocation_started",
                        "incomplete",
                    )
                elif a["allocation"]["charge"] != int(invoked):
                    ctx.error(
                        path,
                        loc,
                        "allocation",
                        "Charge differs from runner invocation_started",
                    )
            except (OSError, ValueError, KeyError, TypeError) as error:
                ctx.error(path, loc, "reference", str(error))
            if not a["bundle"]["verified"]:
                ctx.error(
                    path,
                    loc,
                    "unfinished",
                    "Bundle preservation is not recorded verified",
                    "incomplete",
                )
        elif a["run_id"] is not None or a["allocation"]["charge"] != 0:
            ctx.error(
                path,
                loc,
                "unfinished",
                "Retained bundle/inventory missing",
                "incomplete",
            )
        elif not a["limitations"]:
            ctx.error(
                path,
                loc,
                "unfinished",
                "Explain the attempt without a bundle",
                "incomplete",
            )
        if a["allocation"]["charge"] is None:
            ctx.error(path, loc, "unfinished", "Resolve invocation charge", "incomplete")
        if a["result"] is None:
            if invoked is not False:
                ctx.error(
                    path,
                    loc,
                    "unfinished",
                    "Execution result is not available",
                    "incomplete",
                )
            elif not a["limitations"]:
                ctx.error(
                    path,
                    loc,
                    "unfinished",
                    "Explain unusable attempt without a result",
                    "incomplete",
                )
        else:
            raw = ctx.identity(a["result"]["record"], owner=path, loc=loc + ".result", frozen=True)
            if raw is not None:
                record = ctx.document(
                    raw, a["result"]["record"]["path"], "result", a["result"]["record"].get("version")
                )
                if record is not None:
                    rm = ctx.result(record, a["result"]["record"]["path"])
                    assessment_manifest = rm
                    if record["record_kind"] != "execution result":
                        ctx.error(
                            path,
                            loc,
                            "worked-example",
                            "Worked examples are not attempts",
                        )
                    if (
                        record["result_id"] != a["result"]["result_id"]
                        or record["condition"] != a["condition"]
                        or record["run_id"] != a["run_id"]
                    ):
                        ctx.error(
                            path,
                            loc,
                            "run-identity",
                            "Execution result identity differs from attempt",
                        )
                    if rm and manifest:
                        if (
                            rm["subject_sources"] != manifest["subject_sources"]
                            or rm["conditions"] != manifest["conditions"]
                        ):
                            ctx.error(
                                path,
                                loc,
                                "subject-identity",
                                "Reassessment changes supplied subject inputs",
                            )
                        if rm["study_id"] != manifest["study_id"] or rm["case_id"] != manifest["case_id"]:
                            ctx.error(
                                path,
                                loc,
                                "identity",
                                "Result manifest identifies another study/case",
                            )
                    if record["result_id"] in seen_results:
                        ctx.error(path, loc, "duplicate-id", "Duplicate execution result")
                    seen_results.add(record["result_id"])
        # Collection identity checks above use the actual supplied inputs;
        # aggregate criteria belong to the rule set pinned by the result.
        records.append((a, record, assessment_manifest or manifest))
    return records


def batch_sections(raw):
    hs = headings(raw, 3)
    result = {}
    for i, (n, title) in enumerate(hs):
        if ":" not in title:
            continue
        bid = title.rsplit(":", 1)[1].strip().strip("`")
        end = hs[i + 1][0] - 1 if i + 1 < len(hs) else len(raw.splitlines())
        # Only the execution-scope section supplies batch authority.
        body = "\n".join(raw.splitlines()[n:end]).split("\n## ", 1)[0]
        if field(body, "Scope") is not None:
            result[bid] = body
    return result


def scope(body, path, ctx):
    schedule = []
    for n, header, rows in tables(body):
        if header == ["Order", "Case", "Condition", "Repetition", "CONFIG"]:
            try:
                for expected, (line, row) in enumerate(rows, 1):
                    order, case, condition, rep, config = row
                    if int(order) != expected:
                        raise ValueError("Order must be consecutive from 1")
                    repetition = int(rep)
                    if repetition < 1:
                        raise ValueError("Repetition must be positive")
                    schedule.append((case, condition, repetition, canonical(config.strip("`"))))
            except ValueError as error:
                ctx.error(path, n, "scope", str(error))
                return []
    if not schedule:
        # Existing semantic-delivery v1 uses this explicit one-pair declaration.
        match = re.search(
            r"^Scope: `([^`]+)` only; `([^`]+)` then `([^`]+)`, one execution each, sequentially\.",
            body,
            re.M,
        )
        commands = re.findall(r"skilltest run (\S+)", body)
        if match and len(commands) == 2:
            schedule = [
                (match[1], condition, 1, canonical(config))
                for condition, config in zip(match.groups()[1:], commands)
            ]
        else:
            ctx.error(
                path,
                "Scope",
                "unsupported-scope",
                "Require the accepted Order/Case/Condition/Repetition/CONFIG table or explicit one-pair scope",
                "unsupported",
            )
    if len({x[:3] for x in schedule}) != len(schedule):
        ctx.error(path, "Scope", "duplicate-id", "Repeated planned case/condition/repetition")
    inclusion = bool(re.search(r"Include (?:all|every) valid-setup execution", body))
    no_retries = bool(
        re.search(
            r"No (?:automatic retry|threshold, selective replacement or automatic retry)",
            body,
            re.I,
        )
    )
    if not inclusion or not no_retries:
        ctx.error(
            path,
            "Scope",
            "unsupported-inclusion",
            "This version checks include-all-valid-setup scopes without automatic retries; review other inclusion/retry representations explicitly",
            "unsupported",
        )
    return schedule


def assessment(raw, path, ctx, planned=None, definitions=None):
    line = field(raw, "Attempt index") or ""
    links = LINK.findall(line)
    rev = re.search(r"Git `([0-9a-f]{40})`", line)
    digest = re.search(r"SHA-256 `([0-9a-f]{64})`", line)
    if len(links) != 1 or not rev or not digest:
        ctx.error(
            path,
            "Attempt index",
            "unsupported-reference",
            "Use the accepted path, full Git revision and SHA-256 index citation",
            "unsupported",
        )
        return
    index_path = (Path(path).parent / link_parts(links[0][1])[0]).resolve()
    try:
        rel = index_path.relative_to(ctx.root).as_posix()
    except ValueError:
        ctx.error(path, "Attempt index", "reference", "Index must belong to the repository")
        return
    identity = {
        "path": rel,
        "git_revision": rev[1],
        "sha256": digest[1],
        "version": "1",
    }
    data = ctx.identity(identity, owner=path, loc="Attempt index")
    if data is None:
        return
    value = ctx.document(data, rel, "index")
    if value is None:
        return
    study_batch = [x.strip().strip("`") for x in (field(raw, "Study / batch") or "").split(" / ")]
    if study_batch != [value["study_id"], value["batch_id"]]:
        ctx.error(path, "Study / batch", "identity", "Assessment and index study/batch differ")
    records = index(value, rel, ctx)
    citation = field(raw, "Scope and acceptance rules") or field(raw, "Scope and inclusion rules") or ""
    sl = LINK.findall(citation)
    sr = re.search(r"Git `([0-9a-f]{40})`", citation)
    pinned_scope = None
    if len(sl) == 1 and sr:
        sp = (Path(path).parent / link_parts(sl[0][1])[0]).resolve().relative_to(ctx.root).as_posix()
        original = ctx.git_at(ctx.root, "show", f"{sr[1]}:{sp}").decode()
        selected_scope = batch_sections(original).get(value["batch_id"])
        if selected_scope is not None:
            pinned_scope = scope(selected_scope, path, ctx)
    if pinned_scope is None:
        ctx.error(
            path,
            "Scope",
            "unsupported-scope",
            "Cannot resolve the assessment scope at its full Git revision",
            "unsupported",
        )
        return
    if planned is not None and pinned_scope != planned:
        ctx.error(
            path, "Scope", "scope-identity", "Current selected schedule differs from the assessment scope pin"
        )
    planned = pinned_scope
    planned_keys = [row[:3] for row in planned]
    actual_keys = [(a["case_id"], a["condition"], a["repetition"]) for a, _, _ in records]
    if any(a["retry_of"] is not None for a, _, _ in records):
        ctx.error(path, "Coverage", "retry", "This declared scope allows no retries")
    if actual_keys != [p for p in planned_keys if p in actual_keys]:
        ctx.error(
            path,
            "Coverage",
            "scope",
            "Actual attempts differ from declared order/membership",
        )
    groups = {(c, k) for c, k, _, _ in planned}
    expected_rows = set()
    valid = []
    order = {key: n for n, key in enumerate(planned_keys, 1)}
    for a, r, m in records:
        number = order.get((a["case_id"], a["condition"], a["repetition"]))
        case, condition = a["case_id"], a["condition"]
        if m:
            rule_path = r["manifest"]["path"] if r else a["manifest"]["path"]
            _, cards, _ = ctx.manifest(m, rule_path)
            expected_rows.update((case, condition, cid) for cid, (_, cs) in cards.items() if condition in cs)
            expected_rows.add((case, condition, "functional outcome"))
        if r and r["setup"]["status"] == "valid":
            valid.append((number, a, r))
    if definitions:
        for case, condition in groups:
            # Protocol collection definitions fill only wholly unrepresented
            # groups; they must not reintroduce superseded reassessment rules.
            if (case, condition, "functional outcome") in expected_rows:
                continue
            if case not in definitions:
                continue
            m = definitions[case]
            _, cards, _ = ctx.manifest(m, m["manifest_id"])
            expected_rows.update((case, condition, cid) for cid, (_, cs) in cards.items() if condition in cs)
            expected_rows.add((case, condition, "functional outcome"))
    elif groups - {key[:2] for key in expected_rows}:
        ctx.error(
            path,
            "Aggregate results",
            "unsupported-coverage",
            "Use protocol readiness to resolve criteria for entirely unattempted cases",
            "unsupported",
        )
    # Runtime ranges are explicit prose declarations in the retained v1 report.
    ranges = {}
    for label, first, last in re.findall(r"([A-Za-z][A-Za-z0-9 -]*) includes orders (\d+)[–-](\d+)", raw):
        first, last = int(first), int(last)
        if not 1 <= first <= last <= len(planned):
            ctx.error(
                path,
                "Aggregate results",
                "strata-coverage",
                "Runtime orders must belong to the planned schedule",
            )
            ranges[label.strip()] = set()
        else:
            ranges[label.strip()] = set(range(first, last + 1))
    aggregate_tables = [
        t for t in tables(raw) if t[1][0] in {"Case / condition / criterion", "Condition / criterion"}
    ]
    if len(aggregate_tables) != 1:
        ctx.error(
            path,
            "Aggregate results",
            "aggregate",
            "Require exactly one aggregate table",
        )
        return
    _, header, rows = aggregate_tables[0]
    if header[1:4] != ["Met", "Not met", "Insufficient evidence"]:
        strata = [
            label[:-6] for label in header[1:-1] if label.endswith(" M/N/U") and label != "Combined M/N/U"
        ]
        membership = Counter(n for label in strata for n in ranges.get(label, set()))
        if any(membership[n] != 1 for n, _, _ in valid):
            ctx.error(
                path,
                "Aggregate results",
                "strata-coverage",
                "Each valid execution must appear in exactly one runtime stratum",
            )
    seen = set()
    for line, row in rows:
        if len(row) != len(header):
            ctx.error(path, line, "table", "Malformed aggregate row")
            continue
        key = tuple(x.strip() for x in row[0].split(" / "))
        if header[0] == "Condition / criterion":
            cases = {c for c, _ in groups}
            if len(cases) != 1:
                ctx.error(
                    path,
                    line,
                    "aggregate",
                    "Single-case table requires one declared case",
                )
                continue
            key = (next(iter(cases)), *key)
        if key in seen:
            ctx.error(path, line, "duplicate-id", "Duplicate aggregate row")
        seen.add(key)
        if len(key) != 3 or key not in expected_rows:
            ctx.error(path, line, "criterion-coverage", f"Unexpected aggregate row: {key}")
            continue
        selected = [(n, a, r) for n, a, r in valid if (a["case_id"], a["condition"]) == key[:2]]

        evidence_links = LINK.findall(row[-1])
        if evidence_links:
            allowed = {(ctx.root / a["result"]["record"]["path"]).resolve() for _, a, _ in selected}
            named = {
                (Path(path).parent / link_parts(destination)[0]).resolve() for _, destination in evidence_links
            }
        else:
            allowed = {r["result_id"] for _, _, r in selected}
            named = {name.strip().strip("`") for name in row[-1].split(",") if name.strip()}
            if not selected and named == {"none"}:
                named = set()
        if not named <= allowed or (selected and not named):
            ctx.error(
                path,
                line,
                "aggregate-evidence",
                "Evidence must identify included results for this case/condition",
            )

        def counts(numbers=None):
            c = Counter()
            for n, _, r in selected:
                if numbers is not None and n not in numbers:
                    continue
                if key[2] == "functional outcome":
                    judgment = r["functional_result"]
                else:
                    judgment = next(
                        (x["judgment"] for x in r["criteria"] if x["id"] == key[2]), None
                    )
                    if judgment is None:
                        raise ValueError(f"Result {r['result_id']} has no criterion {key[2]}")
                c[judgment] += 1
            return [c[x] for x in ["met", "not met", "insufficient evidence"]]

        try:
            if header[1:4] == ["Met", "Not met", "Insufficient evidence"]:
                if list(map(int, row[1:4])) != counts():
                    ctx.error(path, line, "aggregate", f"Expected {counts()}")
            else:
                for i, label in enumerate(header[1:-1], 1):
                    if not label.endswith(" M/N/U"):
                        raise ValueError("Unsupported aggregate column")
                    group = label[:-6]
                    if group == "Combined":
                        numbers = None
                    elif group in ranges:
                        numbers = ranges[group]
                    else:
                        ctx.error(
                            path,
                            line,
                            "unsupported-strata",
                            f"No explicit order range for {group}",
                            "unsupported",
                        )
                        continue
                    got = [int(x.strip()) for x in row[i].split("/")]
                    if got != counts(numbers):
                        ctx.error(
                            path,
                            line,
                            "aggregate",
                            f"{label}: expected {counts(numbers)}",
                        )
        except ValueError as error:
            ctx.error(path, line, "aggregate", str(error))
    if seen != expected_rows:
        ctx.error(
            path,
            "Aggregate results",
            "criterion-coverage",
            f"Missing aggregate rows: {sorted(expected_rows - seen)}",
        )
    coverage = [t for t in tables(raw) if t[1][0] == "Case / condition"]
    if len(coverage) == 1:
        _, header, rows = coverage[0]
        seen = set()
        if header != [
            "Case / condition",
            "Planned",
            "Attempted",
            "Included",
            "Invalid setup",
            "Setup unresolved",
            "Unattempted",
        ]:
            ctx.error(
                path,
                "Coverage",
                "unsupported-coverage",
                "Unsupported coverage columns",
                "unsupported",
            )
            return
        for line, row in rows:
            pair = tuple(x.strip() for x in row[0].split(" / "))
            seen.add(pair)
            group = [(a, r) for a, r, _ in records if (a["case_id"], a["condition"]) == pair]
            planned_count = sum(p[:2] == pair for p in planned)
            setups = Counter(r["setup"]["status"] if r else "insufficient evidence" for _, r in group)
            want = [
                planned_count,
                len(group),
                setups["valid"],
                setups["invalid"],
                setups["insufficient evidence"],
                planned_count - len(group),
            ]
            try:
                if len(row) != 7 or list(map(int, row[1:])) != want:
                    ctx.error(path, line, "coverage", f"Expected {want}")
            except ValueError:
                ctx.error(path, line, "coverage", "Coverage counts must be integers")
        if seen != groups or len(rows) != len(groups):
            ctx.error(
                path,
                "Coverage",
                "coverage",
                "Require each planned case/condition exactly once",
            )
    elif (
        len(coverage) == 0
        and len(planned) == len(records)
        and all(r and r["setup"]["status"] == "valid" for _, r, _ in records)
    ):
        if not re.search(
            r"Uncompleted repetitions, unusable attempts and unresolved evidence: none\.",
            raw,
        ):
            ctx.error(
                path,
                "Coverage",
                "unsupported-coverage",
                "Require coverage table or explicit complete/no-gap statement",
                "unsupported",
            )
    else:
        ctx.error(
            path,
            "Coverage",
            "coverage",
            "Require a coverage table for missing or unusable attempts",
        )
    return value, records


def readiness(raw, path, ctx, stage, batch):
    sections = batch_sections(raw)
    if batch is None:
        if len(sections) != 1:
            ctx.error(
                path,
                "--batch",
                "batch-selection",
                "Select an explicit batch ID; scope is ambiguous",
                "unsupported",
            )
            return
        batch = next(iter(sections))
    if batch not in sections:
        ctx.error(path, "--batch", "batch-selection", f"Unknown batch {batch}", "unsupported")
        return
    accounting(raw, path, ctx)
    body = sections[batch]
    planned = scope(body, path, ctx)
    if not planned:
        return
    # Only manifest links inside the selected batch define its input set.
    manifests = []
    for _, target in linked_files(body, path):
        if target.suffix != ".json" or "manifest" not in target.name:
            continue
        value = ctx.document(regular_bytes(target), target, "manifest")
        if value is None:
            continue
        manifests.append(value)
        ctx.manifest(value, target)
        if stage == "collection":
            supplied = (
                value["subject_sources"]
                + [c["configuration"] for c in value["conditions"]]
                + value["authorities"]["criteria"]
                + [value["authorities"]["policy"]]
                + value["controller_only"]
            )
            from hashlib import sha256

            for ident in supplied:
                try:
                    if sha256(regular_bytes(ctx.root / ident["path"])).hexdigest() != ident["sha256"]:
                        ctx.error(
                            path,
                            ident["path"],
                            "working-input",
                            "Current dispatch input differs from frozen bytes",
                        )
                except (OSError, ValueError) as error:
                    ctx.error(path, ident["path"], "working-input", str(error))
    by_case = {m["case_id"]: m for m in manifests}
    if set(by_case) != {p[0] for p in planned}:
        ctx.error(
            path,
            "Scope",
            "manifest-coverage",
            "Selected scope must identify exactly one manifest per case",
        )
    for case, condition, _, config_path in planned:
        manifest = by_case.get(case)
        if manifest:
            condition_entry = next((c for c in manifest["conditions"] if c["id"] == condition), None)
            if condition_entry is None or condition_entry["configuration"]["path"] != config_path:
                ctx.error(
                    path,
                    "Scope",
                    "configuration",
                    "Scheduled CONFIG differs from manifest condition",
                )
    if stage == "assessment":
        targets = {
            target
            for _, target in linked_files(body, path)
            if target.suffix == ".md" and target.name.endswith("-assessment.md")
        }
        if len(targets) != 1:
            ctx.error(
                path,
                "Results",
                "assessment-reference",
                "Selected batch must link one assessment",
                "incomplete",
            )
            return
        target = targets.pop()
        text = ctx.document(regular_bytes(target), target, "assessment")
        if text is None:
            return
        ids = [x.strip().strip("`") for x in (field(text, "Study / batch") or "").split(" / ")]
        if ids != [field(raw, "Study ID"), batch]:
            ctx.error(
                target,
                "Study / batch",
                "batch-identity",
                "Assessment does not identify the selected protocol batch",
            )
        if field(text, "Format version") == "1":
            assessed = assessment(text, target, ctx, planned, by_case)
            current_paths = {p for _, p in linked_files(body, path) if p.name.endswith("run-index.json")}
            if len(current_paths) != 1:
                ctx.error(
                    path,
                    "Scope",
                    "attempt-coverage",
                    "Selected batch must identify one current attempt index",
                )
            elif assessed is not None:
                current_path = current_paths.pop()
                current = ctx.document(regular_bytes(current_path), current_path, "index")
                if current is not None:
                    # The assessment's frozen index does not validate current references.
                    index(current, current_path, ctx)
                    fields = [
                        "attempt_id",
                        "case_id",
                        "condition",
                        "repetition",
                        "attempt_number",
                        "retry_of",
                        "run_id",
                        "manifest",
                        "allocation",
                    ]
                    project = lambda index_value: [
                        [a[key] for key in fields] for a in index_value["attempts"]
                    ]
                    if (
                        current["batch_id"] != batch
                        or current["study_id"] != field(raw, "Study ID")
                        or project(current) != project(assessed[0])
                    ):
                        ctx.error(
                            path,
                            "Scope",
                            "attempt-coverage",
                            "Current actual attempts differ from the assessment index pin",
                        )


def check_links(raw, path, ctx):
    """Check local inline links and anchors; external URLs are not fetched."""
    for n, line in lines_outside_fences(raw):
        line = re.sub(r"`[^`]*`", "", line)
        for _, destination in LINK.findall(line):
            if "://" in destination or destination.startswith("mailto:"):
                continue
            target, anchor = link_parts(destination)
            resolved = (Path(path).parent / target).resolve() if target else Path(path)
            if not resolved.exists():
                ctx.error(path, n, "link", f"Missing local target: {destination}")
                continue
            if anchor and resolved.suffix == ".md":
                seen = {}
                anchors = set()
                for _, heading_line in lines_outside_fences(resolved.read_text(encoding="utf-8")):
                    m = re.match(r"^#{1,6} (.+)$", heading_line)
                    if not m:
                        continue
                    slug = re.sub(r"[^\w -]", "", m[1].lower()).replace(" ", "-")
                    count = seen.get(slug, 0)
                    seen[slug] = count + 1
                    anchors.add(slug + (f"-{count}" if count else ""))
                if anchor not in anchors:
                    ctx.error(path, n, "link", f"Missing heading anchor: {destination}")


def accounting(raw, path, ctx):
    """Check the explicit current-total paragraph, forecast table and call pools."""
    match = re.search(r"(\d+) active minutes booked; (\d+) minutes[^\n]*?([\d,]+)-minute ceiling", raw)
    remaining = None
    if match:
        spent, remaining, ceiling = [int(x.replace(",", "")) for x in match.groups()]
        if spent + remaining != ceiling:
            ctx.error(
                path,
                "Storage and accounting",
                "accounting",
                "Booked plus remaining time differs from ceiling",
            )
    else:
        ctx.error(
            path,
            "Storage and accounting",
            "unsupported-accounting",
            "No recognised current time-total paragraph",
            "unsupported",
        )
    forecasts = [t for t in tables(raw) if t[1] == ["Work", "Estimate", "Basis"]]
    if len(forecasts) != 1:
        ctx.error(
            path,
            "Storage and accounting",
            "unsupported-accounting",
            "Require one Work/Estimate/Basis forecast table",
            "unsupported",
        )
    else:
        _, _, rows = forecasts[0]
        total = 0
        declared = []
        try:
            for line, row in rows:
                if len(row) != 3:
                    raise ValueError("Malformed forecast row")
                number = int(row[1].strip("*"))
                if number < 0:
                    raise ValueError("Forecast values must be nonnegative")
                if row[0].strip("*") == "Total":
                    declared.append(number)
                else:
                    total += number
            if declared != [total]:
                ctx.error(
                    path,
                    "Storage and accounting",
                    "accounting",
                    "Forecast rows do not reconcile to one total",
                )
            if remaining is not None and total > remaining:
                ctx.error(
                    path,
                    "Storage and accounting",
                    "accounting",
                    "Forecast exceeds remaining time; review scope/authorization",
                )
        except ValueError as error:
            ctx.error(path, "Storage and accounting", "accounting", str(error))
    pools = ["subject", "evaluator", "authoring", "retry"]
    call_match = re.search(
        r"Dispatched calls are \*\*(\d+) subject, (\d+) evaluator, (\d+) authoring, (\d+) retry\*\*; remaining outer capacity is \*\*(\d+) / (\d+) / (\d+) / (\d+)\*\*",
        raw,
    )
    if not call_match:
        ctx.error(
            path,
            "Storage and accounting",
            "unsupported-accounting",
            "No recognised current call-total paragraph",
            "unsupported",
        )
        return
    numbers = list(map(int, call_match.groups()))
    actual = Counter()
    seen = set()
    targets = {p for _, p in linked_files(raw, path) if p.name.endswith("run-index.json")}
    for target in sorted(targets):
        value = parse_json(regular_bytes(target))
        if value.get("format_version") == "1":
            for a in value["attempts"]:
                identity = a["run_id"] or a["attempt_id"]
                if identity in seen:
                    ctx.error(
                        target,
                        "attempts",
                        "duplicate-id",
                        "Attempt counted in multiple accounting indexes",
                    )
                seen.add(identity)
                charge = a["allocation"]["charge"]
                pool = a["allocation"]["pool"]
                if type(charge) is not int or charge not in {0, 1} or pool not in pools:
                    ctx.error(
                        target,
                        "allocation",
                        "allocation-total",
                        "Resolve charge and pool before accounting",
                    )
                    continue
                actual[pool] += charge
        elif value.get("phase") in {"development-pilot", "process-pilot"} and "format_version" not in value:
            # Read only the retained pilot accounting projection. This does not
            # migrate or certify the historical case/result representations.
            ctx.error(
                target,
                "attempts",
                "historical-accounting",
                "Only distinct invocation accounting is checked for this historical pilot index",
                "info",
            )
            for a in value["attempts"]:
                identity = a["run_id"]
                if identity in seen:
                    ctx.error(
                        target,
                        "attempts",
                        "duplicate-id",
                        "Historical run counted twice",
                    )
                seen.add(identity)
                invoked = a["execution"]["invocation_started"]
                if type(invoked) is not bool:
                    ctx.error(
                        target,
                        "execution",
                        "allocation-total",
                        "Historical invocation charge unresolved",
                    )
                else:
                    actual["subject"] += int(invoked)
        else:
            ctx.error(
                target,
                "version",
                "unsupported-version",
                "Cannot derive accounting from this index format",
                "unsupported",
            )
    if [actual[p] for p in pools] != numbers[:4]:
        ctx.error(
            path,
            "Storage and accounting",
            "allocation-total",
            f"Indexed charges are {[actual[p] for p in pools]}",
        )
    limit_pattern = r"(\d+) subject, (\d+) evaluator, (\d+) authoring and (\d+) retry invocations"
    limits = re.search(limit_pattern, raw)
    if limits is None:
        for label, destination in LINK.findall(raw):
            if label.lower() not in {"plan", "active plan"}:
                continue
            target = (Path(path).parent / link_parts(destination)[0]).resolve()
            if target.is_file():
                limits = re.search(limit_pattern, target.read_text(encoding="utf-8"))
            if limits:
                break
    if limits is None:
        ctx.error(
            path,
            "Storage and accounting",
            "unsupported-accounting",
            "Cannot resolve explicit outer pool ceilings from protocol/plan",
            "unsupported",
        )
    elif [numbers[i] + numbers[i + 4] for i in range(4)] != list(map(int, limits.groups())):
        ctx.error(
            path,
            "Storage and accounting",
            "allocation-total",
            "Spent plus remaining calls differs from outer ceilings",
        )
