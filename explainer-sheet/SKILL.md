---
name: explainer-sheet
description: Build a printable, diagram-led explainer or cheatsheet on a topic at a chosen reading level, then fit it to a page budget by measurement. Only use when the user invokes /explainer-sheet or asks for this skill by name. Do NOT trigger on mentions of cheatsheets, one-pagers, printable documents, A4, page counts, or requests to explain a topic simply — those are ordinary requests and should be handled normally.
metadata:
  version: "1.0"
---

# Explainer sheet

Produces a printable explainer that teaches through diagrams and concrete examples
rather than prose. The hard parts are not writing — they are agreeing scope before
building, replacing failed prose with pictures, and fitting to pages by measuring
instead of guessing.

## Workflow

1. **Establish the brief before writing anything.** Ask: purpose, audience,
   reading level (see below), page budget, and how it will be printed. Purpose
   changes the document type entirely — "refresh my mental model" produces stories
   and diagrams; "reference while I work" produces tables and commands. Printing
   method matters: 2-up on one landscape sheet reduces each page to about 71%,
   making type size the real constraint rather than page count.

2. **Agree a content inventory.** Present a numbered list of proposed sections.
   Say which you added unprompted, which you left out, and which you are unsure
   about. Get agreement before drafting.

3. **Build in HTML only.** One self-contained file: inline CSS, inline SVG, no
   external assets. Do not produce a PDF until content is settled — fitting work
   done before then is wasted.

4. **Revise against the reader.** Expect several rounds. When they say a section
   does not make sense, diagnose the structure before rewriting sentences.

5. **Run a filler pass, then fit by measurement.** Before touching layout, reread
   for framing phrases and restated clauses (see WRITING-RULES.md) — on one sheet
   this recovered a full page that three rounds of layout work had not. Then add
   the print stylesheet, run the script, and report real numbers.

## Reading level

Ask which of these, and hold it consistently — it governs vocabulary, how much
gets explained, and what counts as a failed section.

- **Five-year-old.** One idea per sentence. Every noun is something they can
  picture. No numbers, no product names, no acronyms. Diagrams carry nearly all
  the meaning; text labels them.

- **Fifteen-year-old / high schooler.** Short sentences. A concrete anchor before
  the proper name ("a list of who runs each part" *then* "registry"). Jargon in
  brackets after the plain version, never instead of it. Real company names and
  real values. One analogy per mechanism, not per paragraph. Assume no field
  knowledge but full general reasoning.

- **Technical, new to this topic.** They read code and understand systems, just
  not this one. Skip analogies for basic mechanics. Spend the space on the
  domain's own vocabulary, real commands, real data, how things fail, and what
  the docs assume you already know.

- **Expert wanting a refresher.** No fundamentals. Dense tables, exact
  terminology, edge cases, and the details people misremember. Diagrams for
  structure and relationships, not for teaching.

The level also decides what to do with a section that will not land. Below the
technical levels, cut it — see the "no path into the scenario" rule. For an
expert, the same section may be exactly what they opened the sheet for.

## Writing rules

Full rules with self-contained worked examples: [WRITING-RULES.md](WRITING-RULES.md).
Diagram patterns and when each applies: [DIAGRAMS.md](DIAGRAMS.md).

- Three paragraphs explaining a mechanism means it wants a diagram.
- Two failed rewrites means it is a content problem, not a wording problem.
- Define jargon in plain words on first use, or replace it with a self-explaining
  word.
- Every scenario needs a plausible way in.
- State the fact; do not frame it. Cut "the part people miss", "and that's the
  point", "it's worth noting" — at every reading level, plain is not chatty.
- Every abstract claim gets a concrete instance underneath, in grey.
- After adding a diagram, delete what it made redundant.

## Fitting to pages

Never estimate, and never agree something will fit because the user hopes it will
— report the arithmetic.

```
python scripts/measure_pages.py sheet.html                      # per-section heights
python scripts/measure_pages.py sheet.html --sweep 1.0 1.1 1.2  # largest type that fits
```

Over budget: give a table of section heights and a ranked cut list with the pixels
each option saves, then let the user choose. Under budget: spend the room on type
size, not more content. Always render the PDF, rasterize the pages, and look at
them for split diagrams, stranded headings, and trailing blanks.
