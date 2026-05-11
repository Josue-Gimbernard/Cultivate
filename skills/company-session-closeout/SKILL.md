---
name: company-session-closeout
description: Close a meaningful Cultivate company session by promoting durable context into markdown, updating web-domain summaries when web work changed, tracking unresolved Brooke/owner questions, checking repo status, and reporting changed files, verification, unchanged systems, and unresolved questions.
---
# Company Session Closeout

Use this skill when closing a meaningful Cultivate company session.

## Steps

1. Decide whether new context should become durable memory.
2. Update the smallest correct markdown file.
3. Put unresolved questions in `memory/inbox.md`.
4. Use `memory/10-open-questions.md` for durable launch, naming, compliance, facility, business model, or partnership questions.
5. If work touched `M:\Cultivate_Web`, also update `domains/web/web_overview.md`, `domains/web/web_brief.md`, and `memory/11-repo-and-git-operations.md` when web status, commits, repo auth, or deploy state changed.
6. Read changed docs end to end.
7. List changed files.
8. Confirm no live systems, databases, public materials, or external commitments changed.
9. Confirm unresolved Brooke/owner questions are still tracked as pending rather than inferred.
10. If Brooke handoff materials changed in the web repo, record that Brooke does not need repo access and that Claude attachment flow is the expected handoff.
11. If the Railway link or deploy state changed, mirror only the stable status and link into `domains/web/`; keep implementation details in `M:\Cultivate_Web`.

## Closeout Format

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
