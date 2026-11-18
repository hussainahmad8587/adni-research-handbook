# 🔤 10 · Glossary & Cheat Sheet

> ⏱️ Reference · 🟢 Beginner

> [!TIP]
> Spot a missing term? Open a PR. Glossary entries are a great **first contribution** (label: `good first issue`).

> [!TIP]
> A **participant** is a person. A **visit** is an encounter. A **scan** is an acquisition. Decide which one you are counting before you join tables.

## Cheat sheet

| Question | Answer |
|----------|--------|
| Where do I apply? | Official ADNI access page → [chapter 03](03-getting-access.md) |
| Where do I download? | LONI IDA after approval |
| What is one row? | A visit (or a measurement at a visit), **not** a person |
| Primary participant key? | `RID` |
| How do I join tables? | `RID` + harmonized visit code, with `merge(validate=...)` |
| How do I get time since baseline? | From `EXAMDATE`, not from `m12` |
| How do I split train/test? | By `RID` (grouped) |
| Can I share data? | No. See [chapter 08](08-publication-policy.md) |

## Terms

| Term | Expansion | Meaning | You will meet it in |
|------|-----------|---------|---------------------|
| **Aβ / Abeta** | Amyloid-beta | Peptide that forms plaques; measured in CSF, blood, PET | CSF and PET tables |
| **AD** | Alzheimer's disease / dementia | Also a diagnostic group label (`DX_bl = AD`) | Diagnosis columns |
| **ADAS-Cog** | Alzheimer's Disease Assessment Scale, Cognitive subscale | Cognitive test; higher = worse | Cognition tables |
| **ADNI** | Alzheimer's Disease Neuroimaging Initiative | The study | Everywhere |
| **ADNIMERGE** | | Merged convenience table of key variables | Quickstart |
| **ADNI-GO** | ADNI Grand Opportunities | Second phase | `PHASE`, `COLPROT` |
| **APOE4** | Apolipoprotein E ε4 allele | Strongest common genetic risk factor | Genetics tables |
| **ASL** | Arterial spin labeling | MRI perfusion method | MRI collections |
| **Attrition** | | Participants leaving the study | Missing-data analysis |
| **bl** | Baseline | Visit code | `VISCODE` |
| **CDR / CDR-SB** | Clinical Dementia Rating / Sum of Boxes | Staging scale; higher = worse | Cognition tables |
| **Centiloid** | | Standardized amyloid PET scale across tracers | PET analysis |
| **CN** | Cognitively normal | Diagnostic group | `DX`, `DX_bl` |
| **COLPROT / ORIGPROT** | Collection / original protocol | Phase in which visit was collected / participant enrolled | Many tables |
| **CSF** | Cerebrospinal fluid | Fluid sampled by lumbar puncture | Biomarker tables |
| **DATADIC** | Data dictionary | File describing columns | LONI IDA |
| **DICOM** | | Standard medical image format | Raw images |
| **DPC** | Data and Publications Committee | Reviews access and publications | Access/publications |
| **DTI** | Diffusion tensor imaging | MRI of white-matter microstructure | Advanced MRI |
| **DUA** | Data Use Agreement | The terms you accept for access | Application |
| **DX / DX_bl** | Diagnosis / baseline diagnosis | Current vs. baseline label | ADNIMERGE |
| **EMCI / LMCI** | Early / late mild cognitive impairment | MCI subtypes | `DX_bl` |
| **EXAMDATE** | Exam date | Date of the visit's exam | Many tables |
| **FAQ** | Functional Activities Questionnaire | Functional scale | Cognition tables |
| **FDG** | Fluorodeoxyglucose | PET tracer for glucose metabolism | PET |
| **FreeSurfer** | | Software to segment MRI and measure thickness/volume | `UCSFFS…` tables |
| **ICV** | Intracranial volume | Head-size proxy for volume adjustment | MRI tables |
| **IDA** | Image & Data Archive | The download system at LONI | Access |
| **LONI** | Laboratory of Neuro Imaging (USC) | Hosts the archive | Access |
| **MCI** | Mild cognitive impairment | Intermediate diagnostic group | `DX` |
| **MMSE** | Mini-Mental State Examination | Brief cognitive screen (max 30) | Cognition |
| **MoCA** | Montreal Cognitive Assessment | Cognitive screen | Cognition |
| **MPRAGE** | | Common T1-weighted MRI sequence | MRI |
| **NfL** | Neurofilament light | Marker of neuro-axonal injury | Fluid biomarkers |
| **NIA** | National Institute on Aging | Primary funder | Acknowledgment |
| **NIfTI** | | Common neuroimaging analysis format | After DICOM conversion |
| **PHASE** | | Which ADNI phase | Many tables |
| **PTID** | Participant ID | Site-based string ID | Many tables |
| **p-tau** | Phosphorylated tau | Tau pathology marker (CSF, blood) | Biomarkers |
| **RAVLT** | Rey Auditory Verbal Learning Test | Memory test | Cognition |
| **RID** | Roster ID | Numeric participant key | Everywhere |
| **Rollover** | | Participant continuing from one phase to the next | Phase analysis |
| **SMC** | Significant memory concern | Group added in later phases | `DX_bl` |
| **SUVR** | Standardized uptake value ratio | PET uptake relative to a reference region | PET tables |
| **Tau PET** | | PET imaging of tau tangles | Check tracer and phase in the methods document |
| **VISCODE / VISCODE2** | Visit code / harmonized visit code | Visit labels | Many tables |
| **xMAP / Elecsys** | Luminex-based / Roche assay platforms | Different CSF assay platforms | Check the assay documentation |

---
[← 09 · First analysis](09-first-analysis.md) · [🏠 Home](../README.md) · [Next → 11 · Resources & FAQ](11-resources-faq.md)
