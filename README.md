# Large Language Models for Automated Vulnerability Repair: A Systematic Literature Review — replication package

This repository holds the data and materials behind the article *Large Language Models for Automated Vulnerability Repair: A Systematic Literature Review* (submitted to *Information and Software Technology*). Every count, table and figure in the article can be traced to a file here.

**Review in brief:** PRISMA 2020 and Kitchenham and Charters guidelines; six databases searched on 16 November 2026; 3,880 records identified, 2,716 screened and 125 candidates assessed; backward and forward snowballing; 75 core studies assessed in full text and 13 sensitivity-set studies supported only by abstracts.

## Contents

| Folder | Content | Article section |
|---|---|---|
| `1_protocol/` | Supplementary Material S1: protocol, research questions, eligibility criteria (IC1–IC6, EC1–EC12), PRISMA 2020 checklist, quality rubric, extraction codebook, archetype rules, snowballing, retrieval and verification logs | 4 |
| `2_search/` | Search strings, database adaptations and record counts; raw exports | 4.1 |
| `3_screening/` | Title-and-abstract screening log and LLM screening set-up | 4.3 |
| `4_selection/` | Full-text decisions for the 125 candidates, snowballing and second-retrieval candidates, removals at final verification, verification log and selection flow | 4.3, Figure 1 |
| `5_quality/` | Quality scores, the independent re-coding of 29 studies with agreement statistics, and the adjudication | 4.4, 4.5, 10 |
| `6_extraction/` | Supplementary Data S2 (workbook) and CSV copies of the extraction matrix, sensitivity-set coding, codebook and the Summary sheet, which computes every number in the article | 4.5–9 |
| `7_analysis/` | Script that draws Figures 1–4 from Supplementary Data S2, and the figures | 5–9 |
| `8_references/` | BibTeX for the 75 core studies (S1–S75) and the 13 sensitivity-set studies (R1–R13) | Appendix A |

## How to trace a number

1. Open `6_extraction/Supplementary_Data_S2.xlsx`, sheet **Summary**. Each row names the article section it supports and computes its count with a formula over `Extraction_Core75` or `Sensitivity_Set13`.
2. The meaning of every coded field is in sheet **Codebook** (also in `6_extraction/csv/Codebook.csv`).
3. To redraw the figures, run `python 7_analysis/make_figures.py 6_extraction/Supplementary_Data_S2.xlsx out/`. This needs Python 3 with `openpyxl` and `matplotlib`.

## Study identifiers

Core studies are numbered S1–S75 and sensitivity-set studies R1–R13, as in Appendix A of the article. Candidate records keep their screening identifiers (`REC_xxxxx`, `SBxx`, `FSxx`); the `SID` column links them to S-numbers.

## Use of AI tools

An LLM produced provisional screening decisions, and a reviewer checked every one. Quality scores and extraction for 29 studies were first drafted with an AI tool, then re-coded independently by two authors, with disagreements adjudicated by a fourth author. Only the human values are used. Details are in `5_quality/README.md` and Sections 4.3–4.5 of the article.

## Copyright

Full texts of the primary studies are not included; use the DOIs in `8_references/`.

## Licence and citation

Data and documents: CC BY 4.0. Code: MIT. If you use this package, please cite the article and the archived version of this repository (DOI: *to be added after archiving*).
