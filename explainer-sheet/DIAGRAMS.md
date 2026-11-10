# Diagram patterns

Six patterns cover most explainer work. Pick by what the reader is confused
about, not by what looks good. All are hand-written HTML or inline SVG in the
sheet itself — no image files, so the sheet stays one portable document.

## Card flow

A row of 3–5 boxes with arrows between, each carrying a title, a real-world
example in grey, and a sentence of what it does.

**Use for:** a chain of actors or stages. Answers "who does what, in what order".

Put the role descriptions *inside* the boxes rather than in a list underneath.
A separate list forces the reader to hold the diagram in their head while
reading the definitions.

## Numbered vertical sequence

A tall box on the left representing the actor, with numbered steps stacked
vertically to its right and one arrow to each.

**Use for:** a process that must be understood as ordered. Vertical position
carries time, so the order is unmistakable.

Do not use a horizontal fan of arrows for a sequence — it implies simultaneity,
which readers do ask about. Put each step's reply in its subtitle so the diagram
shows both question and answer without doubling the arrows.

## Side-by-side data panes

Two or three panes, each showing a handful of real rows from a real data
structure, with the relevant row highlighted in each.

**Use for:** "what does this thing actually contain". The single best move for
turning an abstract claim into something concrete.

Note the size of each collection if the sizes differ dramatically — the contrast
does more explaining than a sentence would. Highlight the row being followed so
the eye traces the path across panes.

## Live-versus-ignored panes

The same pattern, but one pane is dashed, greyed, and badged as inactive.

**Use for:** situations where two plausible-looking things exist and only one has
effect. Give the panes *different* values — identical values read as a copy or a
sync rather than a trap.

## Timeline lanes

Horizontal bars on two or more lanes, a shared time axis beneath, a dashed
vertical marker for the triggering event, and a shaded band over the interval
that matters.

**Use for:** anything where independent parties hold state with independent
clocks. Explains divergence far better than prose.

## Panel strip

Four panels reading left to right, each with a timestamp, a heading, two lines of
what happens, and a status chip.

**Use for:** the lifecycle of one thing over time. Reserve one panel, styled as a
warning, for the counter-intuitive moment — often the moment where *nothing*
happens, which is exactly what readers get wrong.

## Placement and captions

- Interleave with prose. Never stack two diagrams back to back.
- A caption that repeats the diagram is wasted. Caption with what the reader
  should conclude, or the thing the diagram cannot show.
- Analogies work better aligned beneath the diagram column they describe than
  told separately a paragraph earlier.

## Sizing for print

Wrap SVG in a container with a `max-width` and let it scale. Height falls out of
the aspect ratio, so a wide flat diagram costs far less vertical space than a
tall one: restructuring a tree from vertical to horizontal cut its height by a
third with no loss of content.

Watch for dead space beside short panes in multi-column figures — a note or
caption moved into that gap is free.
