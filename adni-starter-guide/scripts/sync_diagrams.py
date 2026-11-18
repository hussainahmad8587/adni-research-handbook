#!/usr/bin/env python3
"""Keep diagrams in chapters in sync with diagrams/*.mmd (the single source of truth).

GitHub cannot transclude files, so chapters embed copies between markers:

    <!-- diagram:journey:start -->
    ...generated, do not edit by hand...
    <!-- diagram:journey:end -->

Usage:
    python scripts/sync_diagrams.py           # rewrite chapters
    python scripts/sync_diagrams.py --check   # exit 1 if any chapter is out of sync (CI)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIAGRAMS = ROOT / "diagrams"
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__"}
BLOCK = re.compile(r"(<!-- diagram:(?P<name>[\w-]+):start -->\n)(.*?)(<!-- diagram:(?P=name):end -->)", re.S)


def render(name: str) -> str:
    src = (DIAGRAMS / f"{name}.mmd").read_text(encoding="utf-8").rstrip("\n")
    return f"```mermaid\n{src}\n```\n"


def main() -> int:
    check = "--check" in sys.argv
    stale, errors, used = [], [], set()
    for path in sorted(ROOT.rglob("*.md")):
        if SKIP_DIRS & set(path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8")

        def repl(m: re.Match) -> str:
            name = m.group("name")
            if not (DIAGRAMS / f"{name}.mmd").exists():
                errors.append(f"{path.relative_to(ROOT)}: no diagrams/{name}.mmd")
                return m.group(0)
            used.add(name)
            return m.group(1) + render(name) + m.group(4)

        new = BLOCK.sub(repl, text)
        if new != text:
            stale.append(path.relative_to(ROOT))
            if not check:
                path.write_text(new, encoding="utf-8")

    unused = sorted(p.stem for p in DIAGRAMS.glob("*.mmd") if p.stem not in used)
    for e in errors:
        print("ERROR:", e)
    for u in unused:
        print(f"WARN: diagrams/{u}.mmd is not embedded anywhere")
    if check and stale:
        print("Out of sync (run: python scripts/sync_diagrams.py):")
        for s in stale:
            print("  -", s)
    elif stale:
        print("Updated:", ", ".join(str(s) for s in stale))
    else:
        print("All embedded diagrams are in sync.")
    return 1 if errors or (check and stale) else 0


if __name__ == "__main__":
    sys.exit(main())
