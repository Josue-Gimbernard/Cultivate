# Process Reference Docs

Use this skill when new Cultivate source docs arrive or existing docs are revised.

## Steps

1. Copy source files into `docs/source/` without changing the originals.
2. If DOCX exists, treat DOCX as the primary text extraction source.
3. Run `_system/extract_docx_sources.py`.
4. Read the extracted markdown in `docs/extracted/`.
5. Update `docs/normalized/cultivate_source_digest.md` with source-derived facts.
6. Promote durable changes into `memory/` and relevant `domains/`.
7. Record unresolved questions in `memory/10-open-questions.md` or `memory/inbox.md`.

## Rules

- Preserve source wording before interpretation.
- Keep older versions as provenance unless the founder explicitly asks to archive or remove them.
- Do not turn concept language into legal, financial, launch, or partner commitments.

