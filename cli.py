from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator


def _load_json(path: Path) -> object:
try:
return json.loads(path.read_text(encoding="utf-8"))
except FileNotFoundError:
raise FileNotFoundError(f"File not found: {path}")
except json.JSONDecodeError as e:
raise ValueError(f"Invalid JSON in {path}: {e.msg} (line {e.lineno}, col {e.colno})")


def _load_schema(repo_root: Path) -> dict:
schema_path = repo_root / "schema" / "v1.json"
schema = _load_json(schema_path)
if not isinstance(schema, dict):
raise ValueError(f"Schema must be a JSON object: {schema_path}")
return schema


def validate(spec_path: Path) -> int:
repo_root = Path(__file__).resolve().parents[1]
schema = _load_schema(repo_root)
spec = _load_json(spec_path)

validator = Draft202012Validator(schema)
errors = sorted(validator.iter_errors(spec), key=lambda e: list(e.absolute_path))

if not errors:
return 0

print("INVALID: document does not conform to schema/v1.json", file=sys.stderr)
for err in errors:
path = "$"
if err.absolute_path:
path += "." + ".".join(str(p) for p in err.absolute_path)
print(f"- {path}: {err.message}", file=sys.stderr)

return 1


def main(argv: list[str] | None = None) -> None:
parser = argparse.ArgumentParser(
prog="gse",
description="Validate a JSON spec against schema/v1.json. Structure only. No semantics.",
)
sub = parser.add_subparsers(dest="command", required=True)

v = sub.add_parser("validate", help="Validate a JSON document against schema/v1.json")
v.add_argument("path", type=str, help="Path to the JSON file to validate")

args = parser.parse_args(argv)

if args.command == "validate":
code = validate(Path(args.path))
raise SystemExit(code)

raise SystemExit(2)


if __name__ == "__main__":
main()
