#!/usr/bin/env python3
"""Check the freshness of volatile facts.

Every volatile fact in the guide carries a machine-readable tag:

    <!-- verified: 2026-11-18 | source: https://example.org | item: access-steps -->

or, before a human has checked it:

    <!-- verified: never | source: https://example.org | item: access-steps -->

Usage:
    python scripts/check_verified.py                 # warn on stale or never-verified
    python scripts/check_verified.py --strict        # exit 1 on stale or never-verified
    python scripts/check_verified.py --max-age 183   # staleness threshold in days
    python scripts/check_verified.py --newest        # print newest verified date (for badges)
    python scripts/check_verified.py --markdown      # print a VERIFICATION.md-style table
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TAG = re.compile(
    r"<!--\s*verified:\s*(?P<date>\d{4}-\d{2}-\d{2}|never)\s*"
    r"\|\s*source:\s*(?P<source>\S+)"
    r"(?:\s*\|\s*item:\s*(?P<item>[\w-]+))?\s*-->"
)
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__"}
FENCE = re.compile(r"```.*?```", re.S)


def blank_fences(text: str) -> str:
    """Blank out fenced code blocks (keeping line numbers) so documentation examples are not counted."""
    return FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), text)


def iter_tags():
    for path in sorted(ROOT.rglob("*.md")):
        if SKIP_DIRS & set(path.parts):
            continue
        text = blank_fences(path.read_text(encoding="utf-8"))
        for m in TAG.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            yield path.relative_to(ROOT), line, m.group("date"), m.group("source"), m.group("item") or "-"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--max-age", type=int, default=183, help="days before a fact is stale (default 183)")
    ap.add_argument("--strict", action="store_true", help="exit 1 if anything is stale or never verified")
    ap.add_argument("--newest", action="store_true", help="print the newest verified date and exit")
    ap.add_argument("--markdown", action="store_true", help="print a markdown table of all tags and exit")
    args = ap.parse_args()

    tags = list(iter_tags())
    if not tags:
        print("No verification tags found. Add <!-- verified: ... --> tags next to volatile facts.")
        return 1 if args.strict else 0

    if args.markdown:
        print("| Item | File | Line | Last verified | Source |")
        print("|------|------|-----:|---------------|--------|")
        for path, line, d, src, item in tags:
            print(f"| `{item}` | `{path}` | {line} | {d} | {src} |")
        return 0

    dated = [datetime.strptime(d, "%Y-%m-%d").date() for _, _, d, _, _ in tags if d != "never"]
    if args.newest:
        print(max(dated).isoformat() if dated else "never")
        return 0

    today = date.today()
    never, stale, fresh = [], [], 0
    for path, line, d, src, item in tags:
        if d == "never":
            never.append((path, line, item))
            continue
        age = (today - datetime.strptime(d, "%Y-%m-%d").date()).days
        if age > args.max_age:
            stale.append((path, line, item, d, age))
        else:
            fresh += 1

    print(f"Verification tags: {len(tags)} total | {fresh} fresh | {len(stale)} stale | {len(never)} never verified")
    for path, line, item, d, age in stale:
        print(f"  STALE  {path}:{line}  [{item}]  verified {d} ({age} days ago, limit {args.max_age})")
    for path, line, item in never:
        print(f"  NEVER  {path}:{line}  [{item}]")
    if (stale or never) and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
