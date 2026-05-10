# Cultivate Extraction And Agent Architecture Plan

## Purpose

Fully extract, organize, and operationalize the Cultivate concept docs into a markdown-first company-agent architecture.

The goal is not just to summarize the source docs. The goal is to turn the source material into a durable operating system: source docs, extracted text, normalized domain facts, memory, routing rules, skills, open questions, and recommendations.

## Current Source Set

There are now ten source PDFs and ten matching DOCX files in `docs/source/`.

The first eight came from the original concept set:

- The Glade
- The Sprout Space
- The Grove
- The Commons
- The Harvest Cafe
- Foxtail Partnership
- Cultivate Full Ecosystem Updated
- The Stepping Stones

Two newer files were added:

- Cultivate Full Ecosystem FINAL
- The Wilds Outdoor Campus

Working assumption after extraction: `09_Cultivate_Full_Ecosystem_FINAL.docx` supersedes `07_Cultivate_Full_Ecosystem_(Updated).docx` as the current ecosystem overview. The older file remains source provenance, not trash.

## Extraction Status

The PDFs did not expose plain embedded text through a basic local extraction pass. Local tools such as `pdftotext`, `tesseract`, `pdftoppm`, and ImageMagick were not available.

The DOCX files work cleanly as structured text sources. Faithful markdown extraction exists in `docs/extracted/`.

Current extraction path:

1. Keep source PDFs and DOCX files unchanged in `docs/source/`.
2. Extract DOCX files with `_system/extract_docx_sources.py`.
3. Store faithful extracted text in `docs/extracted/`.
4. Store structured source-derived facts in `docs/normalized/`.
5. Promote durable operating truth into `memory/` and `domains/`.

## Proposed Folder Architecture

```text
docs/
  source/             Original local PDF and DOCX copies
  extracted/          Faithful text extraction, one markdown file per DOCX
  normalized/         Structured source-derived fact sheets before promotion

memory/
  03-company-context.md
  04-roadmap-and-priorities.md
  07-operating-model.md
  08-ecosystem-architecture.md
  09-offers-and-experiences.md
  10-open-questions.md

domains/
  company/
  spaces/
  partnerships/
  brand/
  product/
  operations/
  growth/
  research/

skills/
  process-reference-docs/
  update-space-report/
  coordinate-ecosystem-dependencies/
  review-partnership-implications/
  extract-open-questions/
```

## Recommended Domain Model

### Company

Owns the ecosystem thesis, mission, operating model, source-of-truth rules, and cross-domain coordination.

### Spaces

Owns each named physical or experiential component:

- The Glade / The Summit
- The Sprout Space
- The Grove
- The Commons
- The Harvest Cafe
- The Stepping Stones
- The Wilds Outdoor Campus

### Partnerships

Owns Foxtail and future partner relationships, obligations, mutual value, dependencies, and boundaries.

### Product

Owns offers, programs, user journeys, experience packaging, membership/service structure, and delivery model.

### Brand

Owns voice, names, public narrative, audience language, aesthetic principles, and external promise boundaries.

### Operations

Owns physical operations, staffing implications, scheduling, facilities, cafe operations, safety/logistics, and execution cadence.

### Growth

Owns community acquisition, launch sequencing, partnerships as growth channels, revenue paths, and market learning.

### Research

Owns market/customer assumptions, evidence needs, competitor/context research, and source-doc provenance.

## Extraction Workflow

1. Copy source files into `docs/source/`.
2. Extract each DOCX into `docs/extracted/{source_name}.md`.
3. Preserve source wording before interpretation.
4. Produce a normalized fact sheet in `docs/normalized/`.
5. Promote stable company-wide truths into `memory/`.
6. Promote area-specific status into `domains/`.
7. Create skills for repeated workflows discovered during extraction.
8. Record unresolved questions in `memory/inbox.md` or `memory/10-open-questions.md`.
9. Produce recommendations after all sources are extracted.

## Normalized Data To Capture

For every concept or space:

- Name
- One-sentence purpose
- Audience/user
- Experience promise
- Physical requirements
- Program/service components
- Operating dependencies
- Staffing implications
- Revenue or business model implications
- Brand/narrative role
- Partnership dependencies
- Risks or constraints
- Open questions
- Source document and page reference

For partnerships:

- Partner name
- Mutual value
- Proposed relationship
- Dependencies
- Obligations or non-obligations
- Risks
- Open questions
- Source document and page reference

For the full ecosystem:

- Ecosystem components
- How components relate
- Customer journey
- Operating model
- Launch/build sequence
- Revenue paths
- Dependencies
- Contradictions across docs
- Open decisions

## Agent Architecture Build Plan

### Phase 1: Source Control And Extraction

- Keep all ten PDFs and ten DOCX files in `docs/source/`.
- Extract every DOCX source into `docs/extracted/`.
- Use PDFs as visual/provenance references.
- Status: complete for current source set.

### Phase 2: Source-Derived Structure

- Create `docs/normalized/`.
- Normalize each DOCX into structured markdown.
- Keep all source-derived facts traceable.
- Status: initial digest created at `docs/normalized/cultivate_source_digest.md`.

### Phase 3: Domain Architecture

- Add `domains/spaces/` and `domains/partnerships/`.
- Update `domains/README.md` to reflect the Cultivate-specific model.
- Create brief and overview files for each major domain.
- Status: initial Spaces and Partnerships domains created.

### Phase 4: Durable Memory

- Update company context, roadmap, and operating model.
- Add ecosystem architecture, offers/experiences, and open-question memory files.
- Keep assumptions labeled.

### Phase 5: Skills

- Add workflow playbooks for recurring work:
  - processing reference docs
  - updating space reports
  - coordinating ecosystem dependencies
  - reviewing partnership implications
  - extracting open questions

### Phase 6: Recommendations

After extraction and normalization, produce:

- ecosystem map
- concept-by-concept summary
- recommended domain ownership
- missing-data list
- contradictions or version conflicts
- launch/build sequence hypotheses
- highest-leverage next docs to create
- recommended agent workflow improvements

## Immediate Recommendations

1. Treat `09_Cultivate_Full_Ecosystem_FINAL.docx` as the current ecosystem anchor.
2. Keep `07_Cultivate_Full_Ecosystem_(Updated).docx` for comparison, not as the default source.
3. Add `spaces` as a first-class domain because most source docs describe named experiential/physical components.
4. Add `partnerships` as a first-class domain because Foxtail likely creates external dependency and promise boundaries.
5. Do not make public, financial, legal, launch, or partner commitments from these docs until extracted and approved.
6. Use page-referenced fact sheets before writing polished strategy summaries.

## Decisions Needed

- Whether the older ecosystem file should be considered superseded once the final file is extracted.
- Whether The Wilds replaces any earlier outdoor concept or adds a new component.
- Whether this repo should be initialized as git before extraction begins.
- Whether The Summit is the approved replacement for The Glade.
