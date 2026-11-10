# CLAUDE.md

## Rule 1: every commit is scrubbed

This repo is public. Everything committed (skills, artifacts, archives, this file) must be **clean**: a stranger can read it without learning who the owner works for, who they work with, or anything from a private system.

Scrub every file before staging it:

| Sensitive | Replace with |
| --- | --- |
| Employer, client, product or internal project names | `Acme`, `Example App` |
| Real people's names, emails, handles | `Jane Doe`, `user@example.com` |
| Internal URLs, hostnames, IPs, repo names | `example.com`, `internal-service` |
| Jira / Confluence / Slack / Figma links and ticket IDs | `PROJ-123`, or drop the link |
| API keys, tokens, passwords, env values | `<REDACTED>` |
| Local paths containing a username (`/Users/<name>/…`) | `~/…` |
| Proprietary code, data or screenshots | a generic rewritten example, or remove |

**Artifacts are the highest risk**: they are generated from real work. Scrub the source, not just the visible page: HTML/SVG comments, `<meta>` tags, `<title>`, embedded `data:` URIs, JSON blobs, and text inside images.

Unscrubbed originals live in `X LOCAL only/` (gitignored). Keep them there.

**Done** means:

1. `git diff --cached` read line by line, every sensitive hit replaced.
2. The user told what was scrubbed (or that nothing needed it).
3. Anything borderline raised with the user before the commit, not after.

### The pre-commit hook

`.githooks/pre-commit` admits only Claude Code sessions (`CLAUDECODE=1`), then scans staged files for generic leaks: `/Users/<name>` paths, non-`example.com` emails, token and private-key formats. It holds no private terms, so names and companies are still on you; the scrub above is the real check. When the hook blocks, fix the hit, re-stage, and commit again through the hook.

New clone? Enable it once: `git config core.hooksPath .githooks`.

## Conventions

- Skill versions: follow the "Versioning" section of `README.md`.
