# 🔗 11 · Resources & FAQ

> ⏱️ Reference

## I want to…

<!-- verified: never | source: https://adni.loni.usc.edu/ | item: official-links -->
| I want to… | Go to |
|------------|-------|
| Read the official overview | <https://adni.loni.usc.edu/> |
| Apply for access | <https://adni.loni.usc.edu/data-samples/adni-data/#AccessData> |
| Download data | <https://ida.loni.usc.edu/> (after approval) |
| Check publication rules and the acknowledgment | <https://adni.loni.usc.edu/wp-content/uploads/how_to_apply/ADNI_DSP_Policy.pdf> |
| Understand a column | `DATADIC.csv` in your download |
| Convert ADNI to a standard layout (BIDS) | Clinica's ADNI converter |
| Rehearse the workflow without data | [`notebooks/01_first_analysis.ipynb`](../notebooks/01_first_analysis.ipynb) |

## Key papers to cite (verify details before citing)

<!-- verified: never | source: https://adni.loni.usc.edu/wp-content/uploads/how_to_apply/ADNI_DSP_Policy.pdf | item: key-papers -->

| Topic | Reference |
|-------|-----------|
| Clinical characterization | Petersen RC et al. *Alzheimer's Disease Neuroimaging Initiative (ADNI): Clinical characterization.* Neurology, 2010 |
| MRI methods | Jack CR Jr et al. *The Alzheimer's Disease Neuroimaging Initiative (ADNI): MRI methods.* J Magn Reson Imaging, 2008 |
| ADNI3 | Weiner MW et al. *The Alzheimer's Disease Neuroimaging Initiative 3: Continued innovation for clinical trial improvement.* Alzheimers Dement, 2017 |
| Review of findings | Veitch DP et al. *Understanding disease progression and improving Alzheimer's disease clinical trials: Recent highlights from the ADNI.* Alzheimers Dement, 2019 |

## Useful tools (not endorsed, check licenses and versions)

| Tool | For |
|------|-----|
| `dcm2niix` | DICOM → NIfTI conversion |
| FreeSurfer | Cortical/subcortical segmentation |
| ANTs, FSL, SPM, nilearn | Registration, preprocessing, ML on images |
| pandas, scikit-learn, statsmodels | Tabular analysis, grouped CV, mixed models |

## Other datasets you will hear about

| Dataset | One-liner |
|---------|-----------|
| NACC | US Alzheimer's Disease Centers' clinical dataset |
| AIBL | Australian imaging/biomarker/lifestyle study |
| OASIS | Open-access imaging datasets from WashU |
| A4 / LEARN | Preclinical AD trial and companion observational study |

## FAQ

<details>
<summary><b>I have data. Why do I have more rows than participants?</b></summary>
An export can contain multiple rows per person, including visits, scans, or assessments. Check its row grain and count unique, documented participant IDs. See [chapter 05](05-data-structure.md).
</details>

<details>
<summary><b>Can I use ChatGPT / an LLM / a cloud notebook on ADNI data?</b></summary>
Use fictional inputs for public AI tools and cloud demos. Review the DUA’s Appendix A and institutional policy before using any AI-assisted workflow with authorized data.
</details>

<details>
<summary><b>Which diagnosis column should I use?</b></summary>
First decide whether you need a fixed baseline group or diagnosis at a specific visit. Then find the documented field in your export. See [pitfall 5](07-pitfalls.md).
</details>

<details>
<summary><b>My numbers differ from a published paper. Is something wrong?</b></summary>
Compare the release version, phases, eligibility rules, QC, and measurement methods with the paper.
</details>

<details>
<summary><b>Do I need to cite this guide?</b></summary>
Please don't cite it in place of ADNI. Cite ADNI and the primary pipelines per [chapter 08](08-publication-policy.md). Citing the guide as a tutorial is optional ([CITATION.cff](../CITATION.cff)).
</details>

<details>
<summary><b>I found an error in this guide.</b></summary>
Thank you! Open an issue using the "Content error" template, or send a PR. See [chapter 12](12-contributing.md).
</details>

---
[← 10 · Glossary](10-glossary.md) · [🏠 Home](../README.md) · [Next → 12 · Contributing](12-contributing.md)
