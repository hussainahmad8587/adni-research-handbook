# 🗂️ 04 · Data Modalities

> ⏱️ 20 min · 🟡 Practical · 📍 Stage 3 of 5: **Download**

<details open>
<summary><b>⚡ TL;DR (30 seconds)</b></summary>

ADNI brings together **MRI, PET, fluid biomarkers, genetics, clinical and cognitive assessments**, and neuropathology for a subset. Some data streams cover specific phases or groups.
Download **tabular summaries first**. Raw images are huge and need preprocessing. Each modality has one classic gotcha, listed below.

</details>

<!-- verified: 2026-11-18 | source: https://adni.loni.usc.edu/quick-start-guide-asset/filetour.html | item: modality-categories -->

Use the [official file tour](https://adni.loni.usc.edu/quick-start-guide-asset/filetour.html) to find each category. Verify availability and definitions in the methods notes for your export.

| Modality | What it measures | Typical use | Format | Newcomer gotcha |
|----------|------------------|-------------|--------|-----------------|
| 🧲 **MRI** | Brain structure (and some function/perfusion/diffusion) | Atrophy, cortical thickness, hippocampal volume | DICOM images; derived CSV tables | Scanner/protocol changes across phases |
| ☢️ **PET** | Amyloid, tau, glucose metabolism | Pathology burden, metabolism | DICOM images; SUVR/Centiloid tables | Different tracers and reference regions are **not interchangeable** |
| 💧 **CSF** | Aβ42, total tau, p-tau | Biomarker positivity, prediction | CSV | Assay platform changes; censored values |
| 🩸 **Blood** | Plasma biomarkers (e.g. p-tau, NfL, Aβ ratios) | Low-cost screening biomarkers | CSV | Many assay platforms and batches; check which |
| 🧬 **Genetics** | APOE, genome-wide arrays, sequencing | Risk, polygenic scores | Tables, PLINK/VCF-style files | Extra access terms may apply |
| 🧠 **Cognition** | MMSE, MoCA, ADAS-Cog, CDR-SB, RAVLT, composites | Outcomes, staging | CSV | Many similar scores; pick one definition and cite it |
| 🩺 **Clinical** | Diagnosis, demographics, history, medications | Cohort definition, covariates | CSV | Baseline diagnosis (`DX_bl`) ≠ current diagnosis (`DX`) |
| 🔬 **Neuropathology** | Autopsy findings (subset) | Compare biomarker findings with pathology | CSV | Small, selected subset |

## Per-modality notes

<details>
<summary>🧲 <b>MRI</b></summary>

**What you get:** structural T1-weighted images (the workhorse), plus (depending on phase) T2/FLAIR, diffusion, resting-state fMRI and perfusion (ASL). Both **raw** and **pre-processed/corrected** image versions exist.

**What to download first:** the FreeSurfer-derived summary tables (e.g. hippocampal volume, cortical thickness) before touching images.

**Gotchas**
- Field strength and sequences changed over phases ([chapter 06](06-phases.md)).
- Use the **QC flags** in the derived tables. Don't silently include failed segmentations.
- Decide whether and how to account for intracranial volume (ICV) for your analysis.
- Convert DICOM → NIfTI with a tool such as `dcm2niix`, and record the version.

</details>

<details>
<summary>☢️ <b>PET (amyloid, tau, FDG)</b></summary>

**What you get:** FDG (metabolism), amyloid tracers, and from later phases a tau tracer. Raw images plus processed summary tables (SUVR; sometimes Centiloid).
<!-- verified: never | source: https://adni.loni.usc.edu/data-samples/adni-data/ | item: pet-tracers -->

**What to download first:** the PET summary tables from the PET core, not images.

**Gotchas**
- Different amyloid tracers give different SUVR scales. Use a documented, validated Centiloid conversion for the tracer and pipeline, or analyze separately.
- Reference region choice (cerebellum vs. composite) changes the numbers.
- Partial-volume correction versions exist. Report which you used.

</details>

<details>
<summary>💧 <b>CSF biomarkers</b></summary>

**What you get:** Aβ42, total tau and p-tau181 (core AD biomarkers), measured on specific assay platforms.
<!-- verified: never | source: https://adni.loni.usc.edu/data-samples/adni-data/ | item: csf-assays -->

**Gotchas**
- Earlier and later platforms are **not directly interchangeable**. Don't pool raw values across platforms.
- Values outside the assay's measuring range can appear as text such as `>1700` or `<8` (censored). Parse them deliberately.
- CSF was collected in a **subset** of participants. Expect lots of missingness.

</details>

<details>
<summary>🩸 <b>Plasma biomarkers</b></summary>

**What you get:** blood-based measures related to amyloid, tau and neurodegeneration. This is a fast-moving area.
<!-- verified: never | source: https://adni.loni.usc.edu/data-samples/adni-data/ | item: plasma-assays -->

**Gotchas**
- Platform, lab and batch effects are real. Document them and model them if you pool.
- Different tables may use different analytes and units. Read the data dictionary.

</details>

<details>
<summary>🧬 <b>Genetics</b></summary>

**What you get:** APOE genotype (small, easy table) and larger genome-wide and sequencing resources.
**What to download first:** start with the documented APOE export if your project needs that genotype. Decide how to encode it for your question.

**Gotchas**
- Genetic data can come with additional terms. Check them before planning an analysis.
- Ancestry composition of the cohort limits generalization. Account for population structure in genetic analyses.

</details>

<details>
<summary>🧠 <b>Cognition & clinical</b></summary>

**What you get:** global and domain-specific tests, functional scales, and the clinical diagnosis at each visit.

**Gotchas**
- Different phases include different batteries. Don't assume a test exists for every visit.
- Composite scores (memory, executive function) have their own derivations. Cite the source.
- Practice effects exist with repeated testing.

</details>

<details>
<summary>🔬 <b>Neuropathology</b></summary>

Autopsy-derived data exist for a **subset** of participants. Useful for validating biomarkers, but small and not random. Check sample size before designing a study around it.

</details>

> [!TIP]
> **Your first download:** choose one table that answers your question and retrieve its dictionary and methods notes. See [the download walkthrough](13-downloads.md).

---
[← 03 · Getting access](03-getting-access.md) · [🏠 Home](../README.md) · [Next → 05 · Data structure](05-data-structure.md)
