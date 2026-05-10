# Extracted Source Text

This folder contains faithful text extractions from the DOCX source files in `docs/source/`.

Extraction was performed with `_system/extract_docx_sources.py` using DOCX XML parsing. The DOCX files are now the primary extraction source because they expose structured text cleanly. PDFs remain visual/provenance references.

## Extracted Files

| Source | Extracted markdown |
|---|---|
| `01_The_Glade.docx` | `01_The_Glade.md` |
| `02_The_Sprout_Space.docx` | `02_The_Sprout_Space.md` |
| `03_The_Grove.docx` | `03_The_Grove.md` |
| `04_The_Commons.docx` | `04_The_Commons.md` |
| `05_The_Harvest_Cafe.docx` | `05_The_Harvest_Cafe.md` |
| `06_Foxtail_Partnership.docx` | `06_Foxtail_Partnership.md` |
| `07_Cultivate_Full_Ecosystem_(Updated).docx` | `07_Cultivate_Full_Ecosystem_(Updated).md` |
| `08_The_Stepping_Stones.docx` | `08_The_Stepping_Stones.md` |
| `09_Cultivate_Full_Ecosystem_FINAL.docx` | `09_Cultivate_Full_Ecosystem_FINAL.md` |
| `10_The_Wilds_Outdoor_Campus.docx` | `10_The_Wilds_Outdoor_Campus.md` |

## Use Rule

When exact wording matters, use the extracted markdown or the original DOCX. When operating decisions matter, use `docs/normalized/`, `memory/`, and `domains/`.

