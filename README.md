# AI Skills

My personal Claude skills. Each skill lives unpacked in its own folder in the root, with a `SKILL.md` and any supporting files, so you can read it directly.

Three folders are not part of the main list:

- [`artifacts/`](artifacts/) holds example output from my explainer skills, grouped by the skill that made them.
- `skills library/` holds skills written by other people that I currently use.
- `alternate files archive/` holds alternate versions of my own skills, including the packaged single-file versions (`.skill` and `.zip`).

## Skills

| Skill | Version | Summary |
| --- | --- | --- |
| [daily-js](daily-js/) | 1.0 | Daily JavaScript practice drill. Picks a random topic from a curated beginner-to-advanced list and generates a 5–10 minute exercise or Q&A, followed by feedback. |
| [daily-se](daily-se/) | 1.0 | Daily software-architecture refresher, about 75% front-end and 25% back-end. Runs a 5–10 minute Q&A, design-scenario or spot-the-decision drill built around the RADIO framework. |
| [daily-ts](daily-ts/) | 1.0 | Daily TypeScript practice drill. Picks a random topic from a curated foundations-to-mastery list (plus tooling) and generates a 5–10 minute exercise or Q&A, followed by feedback. |
| [explainer-artifact](explainer-artifact/) | 1.0 | House style for a published HTML page that explains a tool, system, API or concept: a short overview, then one labelled reference section holding all the depth. Built to be reopened and shared, not printed. |
| [explainer-sheet](explainer-sheet/) | 1.0 | Builds a printable explainer or cheatsheet that teaches mainly through diagrams, at a chosen reading level. Fits it to a page budget by measuring rendered pages. |
| [handoff](handoff/) | 1.0 | Compacts the current conversation into a handoff document so a fresh agent can continue the work, including suggested skills to invoke. |
| [kiss](kiss/) | 1.0 | Keep It Simple mode. Every answer is cut to the tl;dr: essentials only, cleanly spaced and easy to scan. |
| [onboard-docs](onboard-docs/) | 1.0 | Analyses a codebase and writes 1–4 skimmable onboarding docs under `/docs/onboard/`, covering topology, sequence diagrams, logic flowcharts and testing. |

## Versioning

Each skill's version is stored in its `SKILL.md` frontmatter:

```yaml
metadata:
  version: "1.0"
```

When you change a skill, bump its version here and in its frontmatter.
