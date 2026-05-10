---
id: cultivate_company_agent_protocol
title: Cultivate Company Agent Protocol
domain: company
last_updated: 2026-05-10
tags: [company, protocol, operating-architecture, coordination]
---
# Cultivate Company Agent Protocol

## Purpose

This protocol is the top-level operating guide for Company Agent sessions in `M:\Cultivate`.

The repo exists so Cultivate can build with continuity. Conversations should produce durable markdown artifacts: decisions, assumptions, questions, operating rules, domain status, and next steps.

## Ownership Model

### Company Owns

- Company strategy and operating model.
- Durable company memory.
- Source-of-truth routing.
- Cross-domain coordination.
- Roadmap principles and priorities.
- Decision records and recurring constraints.
- Manager-facing domain status.

### Domains Own

- Domain-specific truth and implementation detail.
- Domain status, open questions, and next actions.
- Domain-specific risks, references, and decisions.

Cultivate starts with a small domain set: Company, Product, Brand, Growth, Operations, and Research. Add domains only when a real workflow needs them.

## Routing Rules

Route work by the smallest durable home:

- `memory/`: stable company context, durable decisions, safety rules, strategy, roadmap principles, and session continuity.
- `domains/`: current status by operating area.
- `skills/`: repeatable workflows and agent playbooks.
- `docs/`: incoming reference docs and source material before absorption.
- `archive/`: superseded historical material.

## Source Of Truth

Use this hierarchy:

1. Current user direction.
2. `AGENTS.md`.
3. This protocol.
4. `memory/`.
5. Relevant `skills/`.
6. Relevant `domains/`.
7. `docs/`.
8. `archive/`.

When sources conflict, name the conflict and propose a clean update.

## Closeout

At the end of meaningful sessions:

1. Update the relevant markdown if durable context changed.
2. Keep unresolved questions in `memory/inbox.md` unless there is a better home.
3. Summarize changed files.
4. Confirm no live external systems were changed.

