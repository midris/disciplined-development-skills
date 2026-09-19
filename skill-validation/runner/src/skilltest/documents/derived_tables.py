"""Render checked observations and arithmetic; never infer semantic judgments."""

import os
import posixpath
import subprocess
from collections import Counter
from pathlib import Path
from urllib.parse import quote

from . import Report
from .formats import field
from .operations import (
    definitions,
    membership,
    publish,
    read_document,
    require,
    selected,
)
from .references import Context
from .study import batch_sections, scope
from .study import index as check_index


def cell(value):
    return str(value).replace("|", "&#124;").replace("\n", " ")


def table(header, rows):
    return "\n".join(
        "| " + " | ".join(map(cell, r)) + " |"
        for r in [header, ["---"] * len(header), *rows]
    )


def link(path, output, label):
    return (
        f"[{cell(label)}]({quote(os.path.relpath(path, output.parent), safe='/.-_')})"
    )


def word_count(raw):
    raw.decode("utf-8")  # Reject binary/ambiguous encodings instead of guessing.
    return int(
        subprocess.run(
            ["wc", "-w"], input=raw, capture_output=True, check=True, timeout=30
        ).stdout
    )


def generate(args):
    path, output, ip = map(
        lambda x: Path(x).absolute(), [args.protocol, args.output, args.index]
    )
    if bool(args.source_target) != bool(args.output_evidence):
        raise ValueError(
            "Length measurement requires both --source-target and --output-evidence"
        )
    ctx = Context(path, Report())
    text, body, planned = selected(path, args.batch, ctx)
    value = read_document(ip, "index", ctx)
    if (value["study_id"], value["batch_id"]) != (field(text, "Study ID"), args.batch):
        raise ValueError("Index belongs to another study/batch")
    records = check_index(value, ip, ctx)
    require(ctx.report, complete=False)
    membership(planned, records)
    # A working protocol cannot silently redefine the scope of retained attempts.
    for a, _, _ in records:
        raw = ctx.read(a["authorization"]["artifact"]).decode()
        pinned = batch_sections(raw).get(args.batch)
        if pinned is None or scope(pinned, path, ctx) != planned:
            raise ValueError("Working scope differs from attempt authority")
    require(ctx.report, complete=False)
    # Read fallback definitions in a separate context: absent results are expected.
    defs_ctx = Context(path, Report())
    defs = definitions(body, path, defs_ctx)
    pairs = list(dict.fromkeys(p[:2] for p in planned))
    has_unmeasured = any(r and r["functional_result"] == "not measured" for _, r, _ in records)
    outcomes = ["met", "not met", "insufficient evidence"] + (["not measured"] if has_unmeasured else [])
    coverage, aggregates, executions, lengths = [], [], [], []
    for pair in pairs:
        group = [
            (a, r, m) for a, r, m in records if (a["case_id"], a["condition"]) == pair
        ]
        statuses = Counter(
            r["setup"]["status"] if r else "insufficient evidence" for _, r, _ in group
        )
        n = sum(p[:2] == pair for p in planned)
        coverage.append(
            [
                " / ".join(pair),
                n,
                len(group),
                statuses["valid"],
                statuses["invalid"],
                statuses["insufficient evidence"],
                n - len(group),
            ]
        )
        assessed = [(a, r, m) for a, r, m in group if r]
        if assessed:
            m = assessed[0][2]

            # Same criterion IDs can conceal changed definitions. Compare policy
            # and criterion bytes as well as applicability before pooling.
            def rules(manifest):
                auth = manifest["authorities"]
                return (
                    [x["sha256"] for x in auth["criteria"]],
                    auth["policy"]["sha256"],
                )

            if any(rules(other) != rules(m) for _, _, other in assessed):
                raise ValueError(f"Mixed scoring policies in {pair}; report separately")
        else:
            if pair[0] not in defs:
                raise ValueError(f"No fallback criteria for {pair}")
            m = defs[pair[0]][0]
        rule_ctx = Context(path, Report())
        conditions, cards, _ = rule_ctx.manifest(m, m["manifest_id"])
        require(rule_ctx.report)
        if pair[1] not in conditions:
            raise ValueError(f"Unknown scheduled condition: {pair}")
        valid = [(a, r) for a, r, _ in group if r and r["setup"]["status"] == "valid"]
        criteria = [cid for cid, (_, cs) in cards.items() if pair[1] in cs]
        for cid in [*criteria, "functional outcome"]:
            counts = Counter(
                r["functional_result"]
                if cid == "functional outcome"
                else next(c["judgment"] for c in r["criteria"] if c["id"] == cid)
                for _, r in valid
            )
            evidence = (
                ", ".join(
                    link(
                        ctx.root / a["result"]["record"]["path"], output, r["result_id"]
                    )
                    for a, r in valid
                )
                or "none"
            )
            aggregates.append(
                [
                    " / ".join((*pair, cid)),
                    *[counts[k] for k in outcomes],
                    evidence,
                ]
            )
    by_slot = {
        (a["case_id"], a["condition"], a["repetition"]): (a, r, m)
        for a, r, m in records
    }
    for order, (case, condition, rep, _) in enumerate(planned, 1):
        a, r, m = by_slot.get((case, condition, rep), (None, None, None))
        status = (
            "unattempted"
            if a is None
            else "unassessed"
            if r is None
            else r["setup"]["status"]
        )
        if r and status != "valid":
            status += " (excluded)"
        evidence = (
            link(ctx.root / a["result"]["record"]["path"], output, r["result_id"])
            if r
            else "none"
        )
        executions.append(
            [
                order,
                case,
                condition,
                rep,
                status,
                r["functional_result"] if r else "not assessed",
                evidence,
            ]
        )
        if args.source_target:
            if r is None:
                lengths.append(
                    [order, "unavailable", "unavailable", "unavailable", status, "none"]
                )
                continue
            rc = Context(path, Report())
            _, _, configs = rc.manifest(m, m["manifest_id"])
            require(rc.report)
            config = configs[condition]
            fixture = next(
                (f for f in config["fixtures"] if f["target"] == args.source_target),
                None,
            )
            ev = next(
                (e for e in r["evidence"] if e["id"] == args.output_evidence), None
            )
            if fixture is None or ev is None:
                lengths.append(
                    [
                        order,
                        "unavailable",
                        "unavailable",
                        "unavailable",
                        "source/evidence not declared",
                        "none",
                    ]
                )
                continue
            cp = next(
                c["configuration"]["path"]
                for c in m["conditions"]
                if c["id"] == condition
            )
            name = posixpath.normpath(
                posixpath.join(posixpath.dirname(cp), fixture["source"])
            )
            source = next(s for s in m["subject_sources"] if s["path"] == name)
            sw = word_count(rc.read(source, m["source_revision"]))
            ow = word_count(rc.read(ev["artifact"]))
            label = "shorter" if ow < sw else "same" if ow == sw else "longer (flag)"
            lengths.append(
                [
                    order,
                    sw,
                    ow,
                    f"{ow - sw:+d}",
                    label,
                    link(ctx.root / ev["artifact"]["path"], output, "whole output"),
                ]
            )
    content = (
        "Generated tables only; judgments and conclusions remain with the assessor.\n\n"
    )
    content += table(
        [
            "Case / condition",
            "Planned",
            "Attempted",
            "Included",
            "Invalid setup",
            "Setup unresolved",
            "Unattempted",
        ],
        coverage,
    )
    content += "\n\n" + table(
        [
            "Order",
            "Case",
            "Condition",
            "Repetition",
            "Setup / coverage",
            "Recorded outcome",
            "Evidence",
        ],
        executions,
    )
    content += "\n\n" + table(
        [
            "Case / condition / criterion",
            "Met",
            "Not met",
            "Insufficient evidence",
            *(["Not measured"] if has_unmeasured else []),
            "Evidence",
        ],
        aggregates,
    )
    if has_unmeasured:
        content += "\n\nUse assessment format 2. Not measured is separate from functional met/not met/insufficient evidence and excluded from functional success denominators. No functional success rate exists when all outcomes are not measured. Coverage above retains excluded and unassessed attempts.\n"
    if args.source_target:
        content += "\n\nWhole-file UTF-8 word counts (`wc -w`); flags do not determine pass/fail.\n\n"
        content += table(
            [
                "Order",
                "Source words",
                "Output words",
                "Change",
                "Length flag",
                "Evidence",
            ],
            lengths,
        )
    publish(output, (content + "\n").encode())
    return output
