---
title: Repo And Git Operations
last_updated: 2026-05-10
---
# Repo And Git Operations

## Repo Split

Cultivate uses two GitHub repos:

| Local path | GitHub repo | Purpose |
|---|---|---|
| `M:\Cultivate` | `git@github.com:Josue-Gimbernard/Cultivate.git` | Company framework, source docs, extracted docs, domains, skills, and durable company memory |
| `M:\Cultivate_Web` | `git@github.com:Josue-Gimbernard/Cultivate_Web.git` | Flask website, private owner preview, UI system, Railway files, tests, and web memory |

Keep this split. Do not merge the website app into the company framework repo unless the founder explicitly requests a repo architecture change.

## GitHub Account Strategy

The machine's global Git identity still belongs to miniBIOTA:

- Global name: `miniBIOTA`
- Global email: `josue@minibiota.com`

Do not change the global identity for Cultivate work. The Cultivate repos use repo-local Git identity and repo-local SSH configuration:

- Repo-local name: `Josue-Gimbernard`
- Repo-local email: `Josue-Gimbernard@users.noreply.github.com`
- SSH key path: `C:/Users/gimbo/.ssh/id_ed25519_josue_github`
- Repo-local `core.sshCommand`: `ssh -i C:/Users/gimbo/.ssh/id_ed25519_josue_github -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new`

This lets Cultivate push as `Josue-Gimbernard` without disturbing miniBIOTA credentials.

## Initial Commits

Initial pushes completed on 2026-05-10:

- `M:\Cultivate`: `ed1dbd5 Initial Cultivate company framework`
- `M:\Cultivate_Web`: `3d3c7dc Initial Cultivate web preview`

Both local `main` branches track `origin/main`.

## Operating Rules

- Before committing, run relevant tests or document why they were not run.
- For `M:\Cultivate_Web`, run:
  - `python -m compileall app.py`
  - `python -m unittest discover -s tests`
  - `npm.cmd run lint:colors`
  - `node --check static\js\main.js`
- Do not commit real `.env` files, secrets, cache folders, logs, or generated runtime artifacts.
- Do not change remotes or SSH identity unless the founder explicitly asks.
- Keep commits focused and use clear messages.

