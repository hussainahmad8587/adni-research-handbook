# Contributing to the ADNI Starter Guide

## 🚫 Rule zero: no ADNI data. Ever.

The ADNI Data Use Agreement prohibits redistributing participant data. Do **not** commit or paste:

- CSV/Excel excerpts, images, scans, or derived participant-level files
- Screenshots of tables or plots built from real data
- Real subject IDs (the `XXX_S_NNNN` format) or lists of RIDs / image IDs
- Notebook outputs (the repo strips them with `nbstripout`, and CI rejects them)

Use obviously fake examples (`SYN_0001`) and label them *synthetic*. CI (`scripts/check_no_data.py`) catches common accidents but is only a safety net. If you slip, follow the incident steps in [chapter 12](docs/12-contributing.md).

## What we need most

1. **Corrections** with a link to an official source (highest value).
2. **Verification passes**: re-check tagged facts and update the date (see below).
3. Glossary terms, FAQ entries, pitfalls you have personally hit.
4. Domain review (imaging, fluid biomarkers, genetics, biostatistics).

## Setup

```bash
cd adni-starter-guide
pip install -r requirements-dev.txt
pre-commit install
python scripts/check_no_data.py
```

## Writing style

- Newcomer first: a 30-second TL;DR at the top of every chapter, plain language, define acronyms on first use.
- Diagram first, prose second. Every diagram has a **Text version** beneath it.
- Prefer linking to official pages over restating policy. Say "⚠ verify" instead of guessing.
- Alerts: `[!NOTE]` context · `[!TIP]` shortcuts · `[!WARNING]` data-quality traps · `[!IMPORTANT]` DUA/legal only · `[!CAUTION]` at most once per chapter.
- No claims about individuals, and no ADNI logos (the guide is unofficial).

## Verifying facts (the freshness system)

Volatile facts carry a tag next to them:

```markdown
<!-- verified: 2026-11-18 | source: https://adni.loni.usc.edu/data-samples/adni-data/#AccessData | item: access-steps -->
```

To verify: open the `source`, compare, fix the text if needed, set the date to today. `never` means nobody has checked yet.

```bash
python scripts/check_verified.py            # report
python scripts/check_verified.py --strict   # fail on stale/never (used monthly in CI)
python scripts/check_verified.py --markdown # refresh the table in VERIFICATION.md

```

## Diagrams

Edit `diagrams/*.mmd`, then `python scripts/sync_diagrams.py`. See [diagrams/README.md](diagrams/README.md).

## Releases

Calendar versioning: `v2026.1`, `v2026.2`, … Update [CHANGELOG.md](CHANGELOG.md) and the coverage notes in the phase chapter first.

## Conduct

Be kind and assume good faith. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
