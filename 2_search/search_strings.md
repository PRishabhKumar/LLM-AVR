# Search strings (Section 4.1, Table 2)

All six databases were searched on **16 November 2026** for publications from **2018 to 2026**.

## Master query

```
(vulnerab* OR CVE OR CWE OR "security patch")
AND (repair OR fix OR patch* OR remediat*)
AND ("large language model" OR LLM OR "language model")
```

## Database adaptations

| Database | Query adaptation | Records |
|---|---|---|
| IEEE Xplore | Master query, All Metadata | 346 |
| Scopus | `TITLE-ABS-KEY(master query)` | 590 |
| SpringerLink | Master query in Keywords | 785 |
| ScienceDirect | Wildcards removed; query split across two fields | 1,147 |
| Web of Science | `TS=(master query)` | 305 |
| arXiv | Three Boolean search groups | 707 |
| **Total records identified** | | **3,880** |

De-duplication by DOI and normalised title removed 1,164 duplicates, leaving 2,716 unique records for screening.

Google Scholar and the ACM Digital Library were consulted only for an overview of publication trends; their results were not exported or screened (see Section 4.1 for the ACM coverage check).

## Raw exports

Place the exported metadata files (RIS, BibTeX or CSV) for each database in `raw_exports/`, together with the de-duplicated list of 2,716 records.
