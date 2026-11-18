#!/usr/bin/env python3
"""Guard against committing ADNI participant-level data.

The ADNI Data Use Agreement prohibits redistribution of ADNI data. This script
is a *safety net*, not a guarantee: it catches the common accidents.

Checks
  1. Forbidden file types (images, volumes, tables, archives, binary dumps)
  2. Jupyter notebooks must have no outputs and no execution counts
  3. Text files must not contain strings shaped like real ADNI subject IDs
     (three digits, "_S_", four digits)
  4. Text files must not contain long comma-separated runs of integers
     (a typical pasted list of RIDs)

Suppress a single line with the marker:  adni-guard: ignore-line
Exit code 1 on any violation.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", ".pytest_cache", ".ipynb_checkpoints"}

FORBIDDEN_SUFFIXES = {
    ".nii", ".dcm", ".mgz", ".mgh", ".img", ".hdr", ".parquet", ".feather", ".rds", ".rdata",
    ".rda", ".xlsx", ".xls", ".sav", ".dta", ".h5", ".hdf5", ".npy", ".npz", ".pkl", ".pickle",
    ".svg", ".pdf", ".zip", ".gz", ".tgz", ".tar", ".7z", ".csv", ".tsv", ".sqlite", ".db",
}
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".tif", ".tiff", ".bmp", ".webp"}
# Files that may be tabular by explicit decision. Keep this list tiny and reviewed.
ALLOWED_PATHS: set[str] = set()

PTID = re.compile(r"\b\d{3}_S_\d{4}\b")  # adni-guard: ignore-line
INT_RUN = re.compile(r"(?:\b\d{2,6}\s*,\s*){12,}")
IGNORE = "adni-guard: ignore-line"
TEXT_SUFFIXES = {".md", ".py", ".ipynb", ".yml", ".yaml", ".txt", ".toml", ".cff", ".json", ".mmd", ".mjs", ".js", ".cfg"}


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def main() -> int:
    problems: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or SKIP_DIRS & set(path.relative_to(ROOT).parts):
            continue
        r = rel(path)
        suffix = path.suffix.lower()
        name = path.name.lower()
        if name.endswith(".nii.gz"):
            suffix = ".nii"

        if r in ALLOWED_PATHS:
            continue
        if suffix in FORBIDDEN_SUFFIXES:
            problems.append(f"{r}: forbidden file type '{suffix}' (possible ADNI data)")
            continue
        if suffix in IMAGE_SUFFIXES:
            problems.append(f"{r}: image file (use Mermaid diagrams)")
            continue

        if suffix == ".ipynb":
            try:
                nb = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                problems.append(f"{r}: invalid notebook JSON ({e})")
                continue
            for i, cell in enumerate(nb.get("cells", [])):
                if cell.get("cell_type") == "code" and (cell.get("outputs") or cell.get("execution_count")):
                    problems.append(f"{r}: cell {i} has outputs or an execution count (run nbstripout)")
                    break

        if suffix in TEXT_SUFFIXES or path.name in {"LICENSE", ".gitignore", "CODEOWNERS"}:
            try:
                lines = path.read_text(encoding="utf-8").splitlines()
            except UnicodeDecodeError:
                problems.append(f"{r}: unreadable as UTF-8 text")
                continue
            for n, line in enumerate(lines, 1):
                if IGNORE in line:
                    continue
                if PTID.search(line):
                    problems.append(f"{r}:{n}: looks like a real ADNI subject ID (use XXX_S_NNNN in docs)")
                if INT_RUN.search(line):
                    problems.append(f"{r}:{n}: long list of integers (a pasted RID list?)")

    if problems:
        print("DATA GUARD FAILED. The ADNI DUA prohibits redistributing participant data.\n")
        for p in problems:
            print("  -", p)
        print(f"\n{len(problems)} problem(s). If you committed data already, see docs/12-contributing.md (incident response).")
        return 1
    print("Data guard passed: no forbidden files, notebook outputs or subject-ID patterns found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
