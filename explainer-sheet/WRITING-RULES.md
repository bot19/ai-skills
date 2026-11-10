# Writing rules

Each rule states the pattern, then an example carrying enough context to stand on
its own. The examples come from building a DNS explainer for a general reader;
you do not need to know the topic to extract the pattern.

These rules assume the *five-year-old* or *fifteen-year-old* levels. At the two
technical levels they soften: analogies become unnecessary, jargon is the point
rather than the obstacle, and a section the reader finds hard is more likely to
be the reason they opened the sheet than a fault to cut. The structural rules —
diagrams over paragraphs, define before duplicating, delete what a diagram
replaced, connect the parts — hold at every level.

## Diagnosing failure

### Three paragraphs explaining a mechanism means it wants a diagram

Prose that fails rarely fails for lack of better sentences. When a reader says a
section does not make sense, look at its shape before rewriting its words.

> A section explained how cached answers expire: how long a copy is kept, who
> benefits from it, and why two people can see different results. Three
> paragraphs, all accurate, and the reader still asked three questions about it.
> Replacing it with a four-panel strip — first request, subsequent requests,
> expiry, next request — answered all three and took less space.

### Two failed rewrites means it is a content problem

If a third framing is tempting, stop. Usually the reader has no path into the
scenario, and no wording fixes that. Test every section: can this reader actually
end up in this situation? If not, cut it to a one-line label — enough that they
are not alarmed when they meet the term, no more.

> A section explained a mechanism that resolves a circular lookup. That
> circularity only arises when you run your own infrastructure named inside your
> own domain. The reader was buying a domain and pointing it at a hosting
> provider, a path that never produces the problem. Three rewrites failed. The
> fix was deleting the section and leaving one line: this label appears in the
> diagram, roughly why it exists, you will not need it.

### Do not let a diagram assert what it cannot show

A diagram that shows several destinations side by side implies they are
simultaneous. If the real process is sequential, the layout must say so.

> A lookup diagram put three servers in a column to the right of the client,
> each with its own arrow. The reader asked whether all three were contacted at
> once. They are strictly ordered — each reply is what makes the next question
> askable. Restacking them vertically with numbered steps fixed it without a
> word of prose.

## Language

### Define jargon in plain words on first use, or replace it

Terms feel transparent to whoever wrote them. Scan for words that are ordinary in
the field and opaque outside it. Prefer a self-explaining word over a technical
one plus a gloss.

> A sheet used "pointer" throughout for the entry a registry stores about a
> domain. That is programming vocabulary; a general reader has no meaning for it,
> and it appeared a dozen times undefined. Replacing it with "signpost" — a word
> that explains itself — removed the need for a definition at all.

### State the fact; do not frame it

Cut phrases that tell the reader how to regard a fact instead of adding to it.
They read as the author performing insight, they cost a line each, and they are
invisible while drafting because they feel like emphasis. This applies at every
reading level — plain language is not the same as chatty language, and an expert
sheet suffers from them just as much.

The test is mechanical: delete the phrase and reread. If the sentence teaches the
same thing, the phrase was filler.

> A sheet had "The part people miss: names are read right to left." Deleting the
> first four words changes nothing about what the reader learns. Elsewhere,
> "That's a normal request — hosts ask for it so they can..." became "Hosts ask
> for this so they can...", and "Nobody has the full list, and that's the point"
> lost its last four words. Each cut was a line saved and nothing lost.

Common offenders, worth searching for before fitting:

- *The part people miss / what people get wrong / the thing to understand*
- *and that's the point / that's the key / this is important*
- *it's worth noting / interestingly / notably / of course*
- *basically / essentially / simply / just*
- *that's a normal thing / don't worry / as you'd expect*

When a counter-intuitive point genuinely needs flagging, use a neutral label
rather than conversational framing: "Common trap:", "Common mistake:", "Easy to
miss:". A label states its category and stops; conversational framing performs
surprise on the reader's behalf. Use at most one or two labels per document, or
they stop signalling anything.

### Do not say it twice in one sentence

Restating a fact in different words feels like reinforcement and reads as
padding. Watch for a clause that adds no new condition.

> A sentence read: "Everything to the left of it is yours to create at no cost —
> nobody's permission required." Both halves make the same claim: it is free and
> unrestricted. The second half was cut. The giveaway is that the clause adds no
> new condition, exception or consequence — it only rephrases.

### Check words that carry two meanings

> "Pick a free name" meant *available*. The reader read *no cost*, especially
> because a nearby diagram used "free" to mean exactly that. Changed to "pick a
> name nobody has taken".

### Every scenario needs a plausible way in

Explain why someone would be in a situation before explaining what happens in it.
Otherwise the setup reads as arbitrary and the reader stalls on "how would I even
get here".

> A section described what happens when a domain bought from one company is
> pointed at another company's servers. The reader asked why anyone would have
> done that. Adding one sentence — you built your site on the second company's
> platform, and during setup they ask you to make this change — made the rest of
> the section land.

### Every abstract claim gets a concrete instance underneath

Set it in grey, smaller, directly below the claim. Use real names and real
values; placeholders teach nothing.

> A table of record types listed what each one answers. Adding a grey example
> line under each description turned it from a glossary into something the reader
> could pattern-match against their own settings screen. Real company names
> landed where "your provider" did not.

## Structure

### Define a thing before saying there are two of them

Ordering errors read to the reader as their own comprehension failure.

> A section titled "two zone files can exist" came before the section defining
> what a zone file is. Swapping them fixed a confusion that had looked like a
> writing problem.

### After adding a diagram, delete what it made redundant

A diagram usually absorbs two or three prose points. Leaving them in creates
overlap the reader must reconcile.

> A timeline showing two independent expiry clocks made a separate bullet — "why
> a change appears for you but not your friend" — unnecessary. The bullet had
> also been subtly wrong; the diagram was correct. Two bullets were deleted after
> that diagram went in, and a numbered list became shorter than its heading
> promised, which then needed retitling.

### Make the parts reference the same object

If part one builds something and part two uses it, say so explicitly at the join.
This is what turns two halves into one document.

> Part one described paying to have one line added to a registry's list. Part two
> described a server reading that line during a lookup. Naming it as the same
> line — and highlighting it in both diagrams — was the strongest single
> connection in the sheet.

### Prefer showing the actual data over describing it

When explaining what a system stores, render a few real rows.

> "Each level knows only who to ask next" was abstract until three panes showed
> the actual lists side by side, with the followed row highlighted in each, and
> the sizes noted: about 1,500 entries, about 160 million, a few dozen. The
> numbers did more persuading than the sentence did.

## Working with the reader

- Their confusion is data about the document, not about them. "I don't
  understand" almost always locates a structural fault.
- When they propose something that will not work, say so with numbers. Agreeing
  and then failing wastes a round.
- When they approve a change in passing, apply it immediately. A change agreed
  and not made will be noticed later and costs trust.
- Flag your own judgement calls as you go: what you added unasked, what you are
  unsure about, what you could not verify. It gives them the chance to correct
  course cheaply.
- Verify facts you are about to teach. A sheet is a reference; a plausible wrong
  detail is worse than an omission.
