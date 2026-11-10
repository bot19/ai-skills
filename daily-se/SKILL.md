---
name: daily-se
description: Daily software-engineering architecture refresher with a front-end specialisation (≈75% FE, 25% BE). Randomly selects an architecture topic and sub-concept and generates a focused 5–10 minute Q&A, design-scenario, or spot-the-decision drill, structured around the RADIO framework. Use when the user types /daily-se, asks for a daily architecture/front-end refresher, a daily SE drill, or wants to rehearse front-end architecture and core full-stack concepts.
metadata:
  version: "1.0"
---

# Daily SE Drill — Front-End Architecture

A habit-forming daily refresher for a working front-end engineer who needs to keep the *whole* mental model of front-end architecture warm — the foundational areas that get neglected when day-to-day work narrows onto specific problems. The goal: if the user had to start a new project tomorrow, they shouldn't need long to recall the full picture.

This is a full-stack drill with a front-end specialisation: **≈75% front-end, ≈25% back-end**. The back-end portion is scoped to what a front-end specialist must reason about to ship a working production app (APIs, auth, caching, data contracts, deployment) plus enough server/data fundamentals to make sound system-level calls.

This drill is **less code, more reasoning** — it rehearses *decisions and tradeoffs*, not syntax.

The topic pool ([TOPICS.md](TOPICS.md)) is grounded in field-standard frameworks rather than any one person's notes: the **RADIO** front-end system-design framework (GreatFrontEnd / Front End Interview Handbook), the **roadmap.sh** front-end roadmap, **patterns.dev**, and **Feature-Sliced Design**.

## On Invocation

1. Read [TOPICS.md](TOPICS.md) — the full pool of topics with sub-concepts and an FE/BE tag
2. Pick **one topic** at random (respect any tier / area / topic filter — see Filtering). Occasionally (when it makes for a richer single question) pick a second topic to combine with it — only if the combined question still fits comfortably in 5–10 minutes; default to one topic.
3. Pick **one specific sub-concept** per topic chosen
4. Choose an exercise format — **Q&A**, **Design scenario**, or **Spot-the-decision** — and vary it day to day (don't repeat the same format twice in a row if the user is on a streak). Default weighting: Q&A ~50%, Design scenario ~30%, Spot-the-decision ~20%
5. Present the exercise clearly and wait for the user's response
6. After the user responds: give thorough feedback — what's correct, what's off, what they missed — then reveal the model answer with a short *why*

---

## Docs Reference (when applicable)

Most daily-se topics are judgment calls without one canonical doc page — don't force a citation. But when a sub-concept centers on a concrete, documented spec, browser API, or named framework feature (e.g. an HTTP caching header, the Web Animations API, React Server Components), surface a brief docs reference alongside the exercise header the same way daily-js/daily-ts do:
- Inline one-liner if it fits, otherwise a link to the primary source — MDN for web-platform/HTTP topics, the framework's own docs for framework-specific features
- Skip it for topics that are inherently about tradeoffs (most Design scenario and Spot-the-decision exercises, and general architecture Q&A) — there's no single doc page for "which caching strategy fits this goal"

---

## The RADIO framework (the spine of this skill)

RADIO is the field-standard checklist for front-end system design. Use it as the structure for every **Design scenario**, and weave its vocabulary into Q&A and feedback so the user internalises it:

- **R — Requirements.** Clarify before designing. Functional + non-functional requirements, target users, the *goal*, scale/traffic, constraints (team, time, devices, network). Always start here. (This is the user's "ask → goal → measure".)
- **A — Architecture.** High-level component/module breakdown and how they interact; rendering and app shape; data flow direction; where logic lives.
- **D — Data Model.** What data exists, who owns it, client vs server state, normalisation, how state is shared and updated.
- **I — Interface.** The contracts — component APIs/props *and* network APIs (REST/GraphQL/RPC), event flow, error/loading shapes.
- **O — Optimizations.** Performance, scalability, accessibility, security, i18n, resilience, and the tradeoffs. In real interviews this is weighted heaviest — spend the most depth here.

Treat RADIO as a checklist, not rigid steps: lead with R and A, then dive wherever the complexity is. Most topics in the pool map to one or more RADIO letters.

---

## The "name a technology and justify it" rule

This is a core habit the skill builds. Whenever a topic touches concrete technology choices (frameworks, state libraries, bundlers, hosting, databases, etc.), the user should be expected to **name a specific option and briefly justify it** — not stay abstract.

- When asking: prompt for a pick *and* a reason ("Which framework here, and why that one over the alternatives?").
- When giving feedback: if the user named a tool without a reason, push for the reason. If they stayed generic ("a state library"), ask them to commit to one.
- In the model answer: name a concrete default (e.g. "React, for ecosystem depth and hiring pool"), acknowledge a credible alternative and when it would win (e.g. "Svelte if bundle size is critical and the team is small"), and keep the justification to 1–3 sentences. There is rarely one right answer — reward sound reasoning over naming the "expected" tool.

---

## Exercise Format Rules

### Q&A (core, ~50%)
- Ask exactly **one** focused question on the chosen sub-concept (or the combined sub-concepts, if two topics were picked)
- Pick whichever format best fits: conceptual ("what does X buy you?"), compare-and-justify ("X vs Y here — which and why?"), tradeoff ("what do you give up by choosing Z?"), or true/false on a common belief
- Favour a question that tests the *mental model and tradeoffs*, not memorised API surface
- If two topics were combined, keep it scoped tightly enough to stay within 5–10 minutes
- After answer: reveal the model answer with a short *why*

### Design scenario (~30%)
- Open with a one-line brief in the **ask → goal → measure** shape (e.g. "Marketing site for a product launch. Goal: conversions. How would you measure success?")
- Ask the user to make **one** RADIO-grounded decision for *that* brief — not a walk through the whole checklist. Tie the decision back to the goal and constraints (team size, timeline, scale, devices)
- Keep scope tight: 1 brief, 1 decision (a tightly-coupled cluster, like "pick a rendering strategy and justify it," still counts as one decision — a walk through multiple RADIO letters does not)
- After answer: give a reference answer for that decision, name whether the brief actually forced it or left it open, and name concrete tech with justification

### Spot-the-decision (~20%)
- Describe a short architecture or a set of choices someone made (3–6 sentences)
- Ask the user to identify what's wrong, risky, or mismatched to the stated goal — and what they'd change
- After answer: list the issues (and any red herrings), ranked by severity, with the fix and the reasoning

### General Rules
- Target: **one question per session**, sized to be completable in 5–10 minutes — not several smaller questions time-boxed to fit
- Tone: encouraging — this is a daily habit, not an interview
- Never pick the same topic two sessions in a row (if the user mentions they just did one)
- Keep the long-run FE/BE ratio roughly 75/25; if recent sessions skewed one way, lean the other
- Always connect a decision back to *why it matters for the goal/users/team* — the point is judgement, not trivia

---

## Filtering

| User says | Behaviour |
|---|---|
| `/daily-se` or `/daily-se random` | Full pool, all topics, format per default weighting |
| `/daily-se foundations` | Requirements & architecture foundations (Topics 1–4) |
| `/daily-se core` | Core FE decisions — the RADIO body (Topics 5–13) |
| `/daily-se quality` | Cross-cutting quality & UX — the "O" (Topics 14–21) |
| `/daily-se ops` | Delivery & operations (Topics 22–30) |
| `/daily-se backend` | Back-end / full-stack fundamentals (Topics 31–38) |
| `/daily-se rendering` | Force that specific topic |
| `/daily-se scenario` | Force the Design-scenario format |
| `/daily-se spot` | Force the Spot-the-decision format |
| `/daily-se state q&a` | Force State Management topic, Q&A format |

---

## Response Structure

```
🎯 Today's SE Drill — [Topic Name]: [Sub-concept]
Area: Foundations / Core FE / Quality / Ops / Back-end   ·   RADIO: [R/A/D/I/O]
Format: Q&A / Design scenario / Spot-the-decision
Estimated time: ~X minutes
📚 Docs (if applicable): [inline signature, or link to the primary source]

[Exercise content]
```

After the user responds:
```
✅ Feedback

[What they got right]
[What to sharpen / what they missed]

💡 Model answer:
[Answer, with concrete tech named + 1–3 sentence justifications, and the tradeoff it reinforces]
```

---

## Topic Source

See [TOPICS.md](TOPICS.md) for all topics, sub-concepts, RADIO mapping, and FE/BE tags.
