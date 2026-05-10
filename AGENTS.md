# Cultivate Company - Codex Agent Entry Point

## What This Repo Is

`M:\Cultivate` is the company operations and coordination vault for Cultivate. It owns durable company memory, operating protocol, strategy notes, domain coordination, decision records, and session continuity.

Codex is the primary operating interface for this repo. The goal is to avoid thread dependency: if something matters beyond the current exchange, it should be captured in markdown.

## Active Architecture

- `AGENTS.md` contains hard operating rules, startup behavior, source-of-truth order, write policy, and closeout expectations.
- `COMPANY_AGENT_PROTOCOL.md` contains the company-level operating protocol.
- `memory/` contains durable context, decisions, safety rules, roadmap notes, and session continuity.
- `domains/` contains manager-facing domain reports and brief status files.
- `domains/company/current_recommendations.md` and `domains/company/buildout_roadmap.md` are the current buildout entry points.
- `skills/` contains repeatable workflow playbooks.
- `_system/` contains lightweight agent/system notes. Add scripts only when they remove real repeated work.
- `docs/` is for incoming reference docs or longer-form source material before it is absorbed into memory, domains, or skills.
- `docs/source/` contains source PDFs and DOCX files.
- `docs/extracted/` contains faithful extracted source text.
- `docs/normalized/` contains structured fact bases derived from source docs.
- `archive/` is for superseded historical material only.
- `memory/11-repo-and-git-operations.md` contains the repo split, GitHub remotes, SSH account strategy, and commit/push rules.

## Startup Sequence

1. Read `AGENTS.md`.
2. Read `COMPANY_AGENT_PROTOCOL.md`.
3. Read `memory/00-index.md`.
4. Read the smallest relevant `memory/*.md` files for the request.
5. Read relevant `domains/*/*` files when the request touches company area status.
6. Read relevant `skills/*/SKILL.md` files when a repeatable workflow applies.
7. Use `docs/extracted/` for exact source wording.
8. Use `docs/normalized/` for structured source-derived facts.
9. For launch-scope work, read `skills/review-launch-viability/SKILL.md`.

## Source Of Truth

Use this hierarchy when sources disagree:

1. User direction in the current session.
2. `AGENTS.md` for hard operating rules.
3. `COMPANY_AGENT_PROTOCOL.md` for company-level protocol.
4. `memory/` for durable company context, strategy, decisions, constraints, and source-of-truth rules.
5. Relevant `skills/*/SKILL.md` playbooks for active workflow rules.
6. `domains/` for domain status and manager-facing summaries.
7. `docs/normalized/` for structured facts derived from source docs.
8. `docs/extracted/` for faithful extracted source text.
9. `docs/source/` for original source files.
10. `archive/` for historical reference only.

Chat history and private model memory are never durable source of truth.

## Company Safety Rules

- Do not invent company commitments, launch targets, pricing, legal decisions, financial commitments, investor/sponsor obligations, or public promises.
- Keep current state, planned state, proposed changes, and aspirational ideas separate.
- Treat missing founder input as unknown, not as permission to infer.
- Capture open questions instead of silently filling strategic gaps.
- Do not move or delete reference docs unless explicitly asked.
- Do not change live systems, databases, websites, payment systems, accounts, or public materials unless explicitly asked.
- Treat the Foxtail partnership material as a concept for discussion, not a commitment.
- Treat The Summit as the current teen-space name while preserving The Glade as earlier-source provenance unless the founder decides otherwise.
- Treat optional family contribution discounts as the current model while preserving earlier volunteer-day language as provenance unless the founder decides otherwise.

## Write Policy

For docs in this repo, proceed after stating what files will change. Keep edits scoped. Preserve user changes.

Ask explicit approval before:

- Deleting, moving, or overwriting source/reference material.
- Initializing git, committing, pushing, or changing remotes.
- Creating public commitments or external-facing materials.
- Any live system, database, payment, legal, account, or production change.

## Verification

For documentation-only work:

- Read every new or changed doc end to end.
- Run `git diff --name-only` or summarize changed files clearly.
- Run `git status --short --branch`.
- Confirm no live systems, databases, public materials, or external commitments changed.

## Session Closeout

Close company sessions with:

```markdown
Changed files:
- path

Verification:
- check performed

Not changed:
- live systems/database/public materials/etc.

Unresolved questions:
- item or "None"
```
