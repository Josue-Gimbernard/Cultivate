---
title: Source Of Truth Rules
last_updated: 2026-05-10
---
# Source Of Truth Rules

## Hierarchy

1. Current founder direction.
2. `AGENTS.md`.
3. `COMPANY_AGENT_PROTOCOL.md`.
4. `memory/`.
5. `skills/`.
6. `domains/`.
7. `docs/`.
8. `archive/`.

## Documentation Rule

If context matters beyond the current session, capture it in markdown.

## Source Doc Rule

Incoming reference docs should land in `docs/source/`. DOCX files are the preferred text source when available. Extracted text belongs in `docs/extracted/`. Structured source-derived facts belong in `docs/normalized/`.

After review, durable conclusions should be promoted into `memory/`, `domains/`, or `skills/`, while the source doc remains available for exact lookup.
