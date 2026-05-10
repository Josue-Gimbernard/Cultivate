# Company Session Start

Use this skill when starting or rehydrating a Cultivate company session.

## Steps

1. Read `AGENTS.md`.
2. Read `COMPANY_AGENT_PROTOCOL.md`.
3. Read `memory/00-index.md`.
4. Read `memory/inbox.md` for unresolved questions.
5. Load only the relevant domain or memory files for the user's request.
6. If reference docs are mentioned, check `docs/` before assuming they are available.
7. For Cultivate source-doc questions, load `docs/normalized/cultivate_source_digest.md` before reading individual extracted docs.

## Output

Briefly state:

- What context was loaded.
- What is known.
- What remains unknown.
- Which markdown files should be updated if the session creates durable context.
