"""Read-only study conformance checks and exclusive draft generation."""

from dataclasses import asdict, dataclass, field as dcfield
from datetime import datetime
from pathlib import Path
import json
import re

from .formats import TEMPLATES, blanks, field, headings, json_errors, kind_of, template, supported_versions


@dataclass
class Diagnostic:
    file: str
    location: str
    rule: str
    message: str
    severity: str = "error"


@dataclass
class Report:
    diagnostics: list = dcfield(default_factory=list)
    kind: str | None = None
    structurally_valid: bool = True
    complete: bool = True
    unsupported: bool = False

    def add(self, path, location, rule, message, severity="error"):
        self.diagnostics.append(Diagnostic(str(path), str(location), rule, message, severity))
        if severity == "error":
            self.structurally_valid = False
        if severity in {"error", "incomplete", "unsupported"}:
            self.complete = False
        if severity == "unsupported":
            self.unsupported = True

    def code(self, ready_for=None):
        if self.unsupported:
            return 2
        return int(not self.structurally_valid or (ready_for is not None and not self.complete))


def structural(raw, path, report):
    kind, value, version = kind_of(raw)
    if version not in supported_versions(kind):
        report.add(
            path,
            "version",
            "unsupported-version",
            f"Unsupported {kind} version {version!r}; supported: {sorted(supported_versions(kind))}",
            "unsupported",
        )
        return kind, value
    if isinstance(value, dict):
        missing = list(blanks(value))
        for error in json_errors(value, kind, bool(missing)):
            report.add(
                path,
                "$" + "".join(f"[{p}]" if isinstance(p, int) else f".{p}" for p in error.path),
                "schema",
                error.message,
            )
        for loc in missing:
            report.add(path, loc, "unfinished", "Supply the required value", "incomplete")
        if kind == "manifest" and "$.created_at" not in missing:
            try:
                datetime.fromisoformat(value["created_at"])
            except (ValueError, TypeError, KeyError):
                report.add(path, "$.created_at", "date", "Use an ISO date or datetime")
        for key in [
            "conditions",
            "attempts",
            "criteria",
            "evidence",
            "subject_sources",
            "controller_only",
        ]:
            items = value.get(key, [])
            if not isinstance(items, list):
                continue
            seen = set()
            for i, item in enumerate(items):
                if not isinstance(item, dict):
                    continue
                ident = item.get("id", item.get("attempt_id", item.get("path")))
                if isinstance(ident, str) and ident:
                    if ident in seen:
                        report.add(
                            path,
                            f"$.{key}[{i}]",
                            "duplicate-id",
                            f"Duplicate identity {ident}",
                        )
                    seen.add(ident)
    else:
        expected = [h for _, h in headings(template(kind)) if h != "Comparison, when applicable"]
        actual = [h for _, h in headings(raw)]
        positions = []
        for name in expected:
            if actual.count(name) != 1:
                report.add(
                    path,
                    "heading",
                    "required-section",
                    f"Require exactly one section: {name}",
                )
            else:
                positions.append(actual.index(name))
        if positions != sorted(positions):
            report.add(
                path,
                "heading",
                "section-order",
                "Keep required sections in template order",
            )
        keys = {
            "protocol": ["Study ID", "Status"],
            "case": ["Study ID", "Case ID", "Definition version", "Status"],
            "assessment": ["Assessment ID", "Study / batch", "Status"],
        }[kind]
        if kind == "assessment":
            for alternatives in [
                ("Scope and acceptance rules", "Scope and inclusion rules"),
                ("Attempt index",),
                ("Assessor and relevant session context", "Assessor"),
            ]:
                if not any(field(raw, name) is not None for name in alternatives):
                    report.add(path, alternatives[0], "required-field", f"Missing {alternatives[0]}")
        for key in keys:
            if field(raw, key) is None:
                report.add(path, key, "required-field", f"Missing {key}")
            elif not field(raw, key):
                report.add(path, key, "unfinished", f"Supply {key}", "incomplete")
        if re.match(r"(?:draft|pending)(?:$|[ ;,.])", field(raw, "Status") or "", re.I):
            report.add(path, "Status", "unfinished", "Document is explicitly unfinished", "incomplete")
        for n, line in enumerate(raw.splitlines(), 1):
            if re.search(r"<[^>\n]+>", re.sub(r"`[^`]*`", "", line)):
                report.add(
                    path,
                    n,
                    "unfinished",
                    "Replace the template placeholder",
                    "incomplete",
                )
        if kind == "case":
            required = [
                m[1]
                for m in re.finditer(
                    r"^([A-Z][^:\n]+):",
                    template(kind).split("## Criteria")[1].split("## Limits")[0],
                    re.M,
                )
            ]
            cards = re.split(
                r"^### ",
                raw.split("## Criteria", 1)[-1].split("## Limits", 1)[0],
                flags=re.M,
            )[1:]
            seen = set()
            if not cards:
                report.add(
                    path,
                    "Criteria",
                    "required-criteria",
                    "At least one criterion card is required",
                )
            for card in cards:
                cid = card.split(":", 1)[0]
                if cid in seen:
                    report.add(path, cid, "duplicate-id", "Duplicate criterion ID")
                seen.add(cid)
                for key in required:
                    if field(card, key) is None:
                        report.add(path, cid, "required-field", f"Missing criterion {key}")
                    elif not field(card, key):
                        report.add(path, cid, "unfinished", f"Supply criterion {key}", "incomplete")
                dimension = field(card, "Dimension")
                if dimension and "<" not in dimension and dimension not in {"functional", "procedural"}:
                    report.add(path, cid, "dimension", "Use functional or procedural")
    return kind, value


def check(path, ready_for=None, batch=None):
    path = Path(path).absolute()
    report = Report()
    try:
        raw = path.read_text(encoding="utf-8")
        if ready_for == "preparation":
            from .manifest_tools import preparation

            preparation(path, raw, report, batch)
            return report
        report.kind, value = structural(raw, path, report)
        if ready_for and report.kind != "protocol":
            report.add(
                path,
                "--ready-for",
                "protocol-required",
                "Whole-study checks require a protocol file",
                "unsupported",
            )
        if batch and not ready_for:
            report.add(path, "--batch", "usage", "--batch requires --ready-for", "unsupported")
        if report.structurally_valid and report.complete:
            from .references import Context

            context = Context(path, report)
            try:
                if isinstance(value, str):
                    from .study import check_links

                    check_links(raw, path, context)
                if report.kind == "manifest":
                    context.manifest(value, path)
                elif report.kind == "result":
                    context.result(value, path)
                elif report.kind == "index":
                    from .study import index

                    index(value, path, context)
                elif report.kind == "assessment":
                    from .study import assessment

                    assessment(raw, path, context)
                if ready_for and report.kind == "protocol":
                    from .study import readiness

                    readiness(raw, path, context, ready_for, batch)
            except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
                report.add(path, "$", "reference", str(error))
        return report
    except (OSError, UnicodeError, ValueError, RecursionError, KeyError, TypeError, AttributeError) as error:
        report.add(path, "$", "invalid-document", str(error))
        return report


def configure(parser):
    commands = parser.add_subparsers(dest="docs_command", required=True)
    from .operations import configure as configure_operations

    configure_operations(commands)
    new = commands.add_parser("new")
    new.add_argument("kind", choices=TEMPLATES)
    new.add_argument("--output", required=True)
    new.add_argument("--format-version", default="1")
    check_parser = commands.add_parser("check")
    check_parser.add_argument("path")
    check_parser.add_argument("--ready-for", choices=["preparation", "collection", "assessment"])
    check_parser.add_argument("--batch")
    check_parser.add_argument("--json", action="store_true")


def run(args):
    if args.docs_command in {"retain", "tables", "manifest"}:
        from .operations import run as run_operation

        return run_operation(args)
    if args.docs_command == "new":
        if args.format_version not in supported_versions(args.kind):
            print(f"Unsupported {args.kind} version; supported: {sorted(supported_versions(args.kind))}")
            return 2
        try:
            content = template(args.kind, args.format_version)
            with Path(args.output).open("x", encoding="utf-8") as output:
                output.write(content)
        except OSError as error:
            print(f"Cannot generate draft: {error}")
            return 1
        print(str(Path(args.output).absolute()))
        return 0
    report = check(args.path, args.ready_for, args.batch)
    if args.json:
        print(json.dumps(asdict(report), ensure_ascii=False))
    else:
        for d in report.diagnostics:
            print(f"{d.file}:{d.location}: {d.severity} [{d.rule}] {d.message}")
        print(
            f"Structure: {'valid' if report.structurally_valid else 'invalid'}; completeness: {'checked' if report.complete else 'unresolved'}. Semantic judgments and owner consent require review."
        )
    return report.code(args.ready_for)
