# ⚠️ 07 · Pitfalls & Gotchas

> ⏱️ 15 min · 🟠 Intermediate · 📍 Stage 4 of 5: **Clean**

## Start with the symptom

| What you notice | First check |
|---|---|
| The row count doubled | [Check duplicate keys and join cardinality](05-data-structure.md). |
| A scan seems missing | [Check the date window, QC and matching rule](14-build-a-cohort.md). |
| My PET subgroup looks different | Compare modality availability and exclusions by phase and diagnosis. |
| Validation looks unusually good | Check participant overlap, label-defining features, and preprocessing fitted before the split. |

<details open>
<summary><b>⚡ TL;DR (30 seconds)</b></summary>

Count people and rows separately. Check phase, tracer, and assay definitions. Decide when diagnosis is measured, apply documented QC, and record the exact export.

</details>

<details>
<summary><b>1 · Treating repeated visits as independent samples (leakage)</b></summary>

**Why:** one participant contributes many rows. A random train/test split puts the same person on both sides, so the model "recognizes" individuals and your accuracy is inflated.
**Avoid:** split by `RID` (`GroupKFold`, `GroupShuffleSplit`), do all preprocessing and feature selection **inside** the training fold, and assert that participant IDs are disjoint. For a site-transfer question, design the evaluation around unseen sites.

</details>

<details>
<summary><b>2 · Joining on the wrong key (or the wrong visit code)</b></summary>

**Why:** `VISCODE` conventions differ by phase; some tables have duplicates, unscheduled visits or screening rows; joining on dates misses near-misses.
**Avoid:** document the participant and visit mapping or date-window rule, use `merge(validate=...)`, compare row counts before/after, and inspect unmatched rows. See [chapter 05](05-data-structure.md).

</details>

<details>
<summary><b>3 · Mixing phases, scanners and protocols without harmonizing</b></summary>

> [!WARNING]
> Pooling 1.5T and 3T volumes, or different acquisition protocols, creates scanner-related differences that look like biology.

**Why:** hardware and sequences changed across phases ([chapter 06](06-phases.md)).
**Avoid:** include field strength/phase as covariates, restrict to a homogeneous subset, or use a harmonization method (and say which). Always report it.

</details>

<details>
<summary><b>4 · Mismatched PET tracers and pipelines</b></summary>

> [!WARNING]
> Different amyloid tracers, reference regions and processing pipelines give different SUVR scales. A single "positivity threshold" does not transfer.

**Why:** tracers bind differently and have different dynamic ranges.
**Avoid:** analyze tracers separately, or convert to a common scale (e.g. Centiloid) with documented methods, and use thresholds derived for *your* tracer and pipeline.

</details>

<details>
<summary><b>5 · Confusing baseline diagnosis with current diagnosis</b></summary>

**Why:** A baseline group stays fixed in the analysis. A visit-level diagnosis can change over time. Check how your export encodes each.
**Avoid:** decide whether your question needs a *fixed* baseline group or a *time-varying* diagnosis, and use the right column. Don't define "stable CN" from baseline alone without checking follow-up.

</details>

<details>
<summary><b>6 · Skipping MRI QC and ICV adjustment</b></summary>

**Why:** automated segmentations fail on some scans; head size drives volume.
**Avoid:** apply the QC flags in the derived tables, inspect outliers, adjust for intracranial volume (proportion or regression), and state the FreeSurfer version/pipeline.

</details>

<details>
<summary><b>7 · CSF/plasma assay platform changes and censored values</b></summary>

**Why:** different platforms produce different scales; values outside the measuring range may be stored as text like `>1700` or `<8`. Reading the column as a number silently drops or breaks them.
**Avoid:** keep platform as a variable, don't pool across platforms, parse censored values explicitly, and decide deliberately how to treat them.

</details>

<details>
<summary><b>8 · Ignoring attrition and informative missingness</b></summary>

**Why:** Attrition and biomarker availability may be related to health, recruitment, or the protocol.
**Avoid:** report who has data at each visit, use methods that accommodate missing data (mixed models, multiple imputation where appropriate), and be careful with "complete-case" analyses.

</details>

<details>
<summary><b>9 · Over-generalizing from a volunteer research cohort</b></summary>

**Why:** ADNI is not population-representative (education, ancestry, access to research centers).
**Avoid:** describe your sample's composition, avoid population-level claims, and discuss generalizability in limitations. Check the current composition in the official data statistics.

</details>

<details>
<summary><b>10 · Not recording which data release you used</b></summary>

**Why:** tables are re-released and corrected; merged tables can lag primary ones; results change.
**Avoid:** log download date, file names, and any version fields; keep a manifest; re-run key analyses on new releases and say so.

</details>

<details>
<summary><b>Bonus · Computing time from visit labels instead of dates</b></summary>

`m12` is nominal. Compute time since the defined index using the actual assessment or acquisition date.

</details>

---
[← 06 · Phases](06-phases.md) · [🏠 Home](https://github.com/hussainahmad8587/adni-research-handbook/blob/main/adni-starter-guide/README.md) · [Next → 08 · Publication policy](08-publication-policy.md)
