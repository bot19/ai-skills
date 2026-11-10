---
name: explainer-artifact
description: House style for building a published HTML artifact that explains a tool, system, API, codebase or concept the user is trying to understand — a living reference page they will reopen and share, not a printable sheet. Use this whenever the user asks you to explain, document, map out, break down or "help me understand" something and the answer wants to be a page rather than a chat reply, and whenever they ask for an artifact, write-up, guide, field guide, primer, cheat sheet or reference on a topic. Also use it when revising such a page. Prefer it over an unstyled artifact even if the user does not mention style, layout or artifacts by name.
metadata:
  version: "1.0"
---

# Explainer artifact

An explainer artifact is a page someone opens to understand a thing, then reopens
later to check a detail. Those two jobs pull in opposite directions: the first
wants brevity, the second wants completeness. Most explainers fail by splitting
the difference — every section half-deep, nothing scannable, the same fact stated
three times in three voices.

This skill resolves it with one move: **a short, even overview, then one clearly
labelled reference section carrying all the depth.** Everything below serves that
shape.

## When this applies

Use it for: explaining a tool, library, API, protocol, codebase, config format,
workflow or concept as a page the user will keep.

Don't use it for: a question answered in a few sentences (answer in chat), a
printable page-budgeted sheet (that's `explainer-sheet`), or a document the user
wants as a file format they named, such as .docx or .pptx.

## Before writing

Load the `artifact-design` skill first. It owns the page contract — title,
libraries, theming, dark mode, size, responsive layout. This skill adds house
style on top and never contradicts it.

## The shape

```
┌─────────────────────────────────────────────┐
│  Title + one-line definition                │
├─────────────────────────────────────────────┤
│  1  The big picture      ┐                  │
│  2  Everyday use          │ short, even,    │
│  3  How it really works   │ roughly equal   │
│  4  Setup & gotchas      ┘                  │
├─────────────────────────────────────────────┤
│  5  The details                             │
│     5A ... 5B ... 5C ...   all the depth    │
└─────────────────────────────────────────────┘
```

Three to five overview parts. Exactly one reference part, last. If an overview
part is outgrowing its siblings, the surplus belongs in the reference part with a
one-line pointer left behind.

## Rule 1 — Define the thing in the first screen

Before any diagram, answer "what is this?" in one sentence of the form
*X is a &lt;category&gt; that &lt;does what&gt;*. Name the category honestly — a
reader who mis-categorises the thing misreads everything after it.

> A load balancer is a **reverse proxy that spreads incoming requests across
> several backends**, so no single one is saturated and a failed one can be taken
> out of rotation.

Pair it with an "it is / it isn't" block when the thing is commonly confused with
a neighbour. The "isn't" column is often the most valuable thing on the page.

## Rule 2 — Cut fluff

Fluff is any clause that announces a fact instead of stating it. It reads as
padding and costs scanning time. Three families:

| Family | Looks like |
|---|---|
| **Preamble** | "What you need to know about…", "It's worth noting that…", "The easiest thing to get wrong here is…", "Let's dive into…" |
| **Superlative / editorial** | "The single biggest reason…", "the few things that trip people up", "the one thing to be clear about" |
| **Hedge / intensifier** | "deliberately", "simply", "basically", "in its own right", "in practice" when it adds nothing |

**The deletion test:** remove the clause. Did a fact disappear? If not, it goes.

| Fluff | Tight |
|---|---|
| "Its own tagline is the shortest version: *ship early*." | "Tagline: *ship early*." |
| "The easiest thing to assume wrongly: nothing validates the payload." | "Nothing validates the payload." |
| "The single biggest reason to add an index here." | "Add an index here." |
| "A one-time setup, then the few things that catch people out." | "One-time setup, then the common mistakes." |
| "The retry runs three times, deliberately." | "The retry runs three times." |

This applies to headings too. *"Deeper guides, built in"* → *"Built-in guides"*.
*"What one ordinary request costs"* → *"What a request costs"*.

## Rule 3 — Show, don't narrate

Prefer a diagram, a table or a list to a paragraph. Reach for prose only when the
relationship between facts is the point. A wall of text in an explainer is a
failure of form, not a sign of thoroughness.

Good candidates for a table: anything with a repeated shape — options and their
effects, stages and what guards them, errors and their causes, "I want to… / do
this".

## Rule 4 — Label and space the reference subsections

A long reference section read as one continuous scroll is unusable. Give each
subsection a short label, a large heading, and real separation.

- Label: `5A`, `5B`, `5C` — a chip beside the heading, so cross-references from
  the overview ("…named in 5A") are followable.
- Heading: noticeably larger than the overview's inline headings.
- Separation: a rule plus generous padding above each subsection.

**Heading layout is identical in every subsection: the label chip and heading on
one row, the description on its own line below.** Flex wrapping lets a short
heading pull the description up alongside it, so the subsections stop matching
each other. Use a grid, which cannot drift:

```css
.sub > .subhead{display:grid;grid-template-columns:auto 1fr;align-items:center;gap:6px 12px}
.sub > .subhead .lab{grid-column:1}        /* 5A */
.sub > .subhead h3 {grid-column:2}         /* heading */
.sub > .subhead p  {grid-column:1 / -1}    /* description, always its own row */
```

After publishing, open the page and check two or three subsections render
identically. Layout bugs of this kind are invisible in source and obvious on screen.

## Rule 5 — Say it once

Each fact lives in exactly one place. When the overview and the reference section
both want it, the overview gets the one-line version plus a pointer, and the
reference gets the full version. Before publishing, scan for the same idea
appearing in two sections — it usually means the overview is doing the reference's
job.

## Rule 6 — Verify against the primary source

Never write facts about a tool from memory or from its marketing page. Run the
thing: its `--help`, its subcommands, its config file, the actual source. For a
concept, read the spec or the canonical docs.

This routinely changes the content. Treat a surprise as the most valuable thing
you found, and say so plainly in the page — a reader's existing wrong belief is
worth correcting explicitly.

> **Resolution order is not what the docs imply.** The environment variable is
> checked fifth, after the config file and the CLI flag, so exporting it rarely
> has the effect people expect.

When revising an existing page, re-verify rather than trusting what's written
there, including your own earlier draft.

## Rule 7 — One living page

A topic gets one artifact. Update it in place at the same URL so the link the user
saved keeps working and corrections land in one place. Don't publish a v2
alongside a v1; if an older page exists, say it is superseded and stop maintaining
it.

## Rule 8 — Publish; export only on request

Publishing the artifact is the deliverable. Don't generate HTML or PDF exports on
every revision — it's noise during iteration. Offer them once the user says the
content is settled, or when they ask.

## Before you publish

- [ ] A one-sentence definition appears in the first screen.
- [ ] Overview parts are short and roughly equal; all depth is in the reference part.
- [ ] Every reference subsection is labelled, large-headed, and separated.
- [ ] Every subsection heading uses the same layout — description below, never beside.
- [ ] Deletion test run over all prose: no clause survives that carries no fact.
- [ ] No fact stated in two sections.
- [ ] Every claim traced to the primary source, not memory.
- [ ] Rendered and eyeballed, not just validated as markup.

## Worked example

`references/worked-example.md` applies all of this to an unrelated topic (a job
queue's retry behaviour), showing a weak draft and the revision beside it. Read it
when you want a concrete model of the voice and the overview/reference split.
