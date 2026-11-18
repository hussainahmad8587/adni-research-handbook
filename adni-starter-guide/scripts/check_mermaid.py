#!/usr/bin/env python3
"""Cheap static lint for Mermaid blocks (fast, no browser).

This does NOT replace real rendering (CI also renders every diagrams/*.mmd with
mermaid-cli). It catches the mistakes that break GitHub rendering most often.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__"}
KNOWN = ("flowchart", "graph", "journey", "mindmap", "timeline", "erDiagram", "stateDiagram-v2",
         "stateDiagram", "sequenceDiagram", "gantt", "pie", "classDiagram", "quadrantChart", "gitGraph")
MAX_FLOW_NODES = 18
FENCE = re.compile(r"```mermaid\n(.*?)```", re.S)
NODE = re.compile(r"\b([A-Za-z][A-Za-z0-9_]*)\s*(?:\[|\(|\{|>)")


def blocks():
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or SKIP_DIRS & set(path.relative_to(ROOT).parts):
            continue
        if path.suffix == ".mmd":
            yield path, 1, path.read_text(encoding="utf-8")
        elif path.suffix == ".md":
            text = path.read_text(encoding="utf-8")
            for m in FENCE.finditer(text):
                yield path, text.count("\n", 0, m.start()) + 1, m.group(1)


def lint(code: str) -> list[str]:
    errs = []
    lines = [l for l in code.splitlines() if l.strip() and not l.strip().startswith("%%")]
    if not lines:
        return ["empty diagram"]
    first = lines[0].strip()
    if not first.startswith(KNOWN):
        errs.append(f"unknown diagram type: '{first[:30]}'")
    if "%%{" in code:
        errs.append("init/theme directives are not allowed (break dark mode, fragile on GitHub)")
    if re.search(r"^\s*click\s", code, re.M):
        errs.append("'click' interactions are disabled on GitHub")
    if "\t" in code:
        errs.append("tab characters (use spaces)")
    for n, line in enumerate(code.splitlines(), 1):
        if line.count('"') % 2:
            errs.append(f"line {n}: unbalanced double quotes")
        if line.count("[") != line.count("]"):
            errs.append(f"line {n}: unbalanced [ ]")
        if line.count("{") != line.count("}") and "erDiagram" not in first and "classDiagram" not in first:
            errs.append(f"line {n}: unbalanced {{ }}")
    if first.startswith(("flowchart", "graph")):
        ids = set(NODE.findall(code)) - {"subgraph", "classDef", "class", "direction"}
        if len(ids) > MAX_FLOW_NODES:
            errs.append(f"{len(ids)} nodes (limit {MAX_FLOW_NODES}); split the diagram")
    return errs


def main() -> int:
    total, bad = 0, 0
    for path, line, code in blocks():
        total += 1
        for e in lint(code):
            bad += 1
            print(f"{path.relative_to(ROOT)}:{line}: {e}")
    print(f"Checked {total} Mermaid block(s); {bad} problem(s).")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
