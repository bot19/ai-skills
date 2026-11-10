---
name: daily-ts
description: Daily TypeScript practice drill. Randomly selects a TS topic or sub-concept from a curated foundations-to-mastery list (plus tooling) and generates a focused 5–10 minute coding exercise or Q&A. Use when the user types /daily-ts, asks for a daily TS drill, TypeScript practice, or a TS exercise to complete today.
metadata:
  version: "1.0"
---

# Daily TS Drill

A habit-forming daily TypeScript exercise. Each session targets one concept or sub-concept, takes 5–10 minutes, and ends with feedback. Designed for a working FE engineer building stronger mental models of the type system and surrounding tooling.

## On Invocation

1. Read [TOPICS.md](TOPICS.md) — the full pool of 50 topics with sub-concepts
2. Pick **one topic** at random (respect level/tier filter if provided — see below). Occasionally (when it makes for a richer single question) pick a second topic to combine with it — only if the combined question still fits comfortably in 5–10 minutes; default to one topic.
3. Pick **one specific sub-concept** per topic chosen (e.g. topic: Narrowing → sub-concept: `in` operator narrowing). If it centers on a specific type/utility type/language feature, prepare a docs reference — see **Docs Reference** below
4. Choose exercise format: **coding challenge** or **Q&A** — vary these day to day, don't repeat the same format twice in a row if the user is on a streak
5. Present the exercise clearly and wait for the user's response
6. After the user responds: give thorough feedback — what's correct, what's off, and show the ideal solution with a short *why* explanation

---

## Docs Reference

When the sub-concept centers on a specific type, utility type, or language feature with a canonical reference page (e.g. `Partial<T>`, narrowing via `in`, template literal types), surface a docs reference alongside the exercise header:
- If the signature/summary fits in one line, write it inline — e.g. `Partial<T> → constructs a type with all properties of T set to optional`
- If the full picture is more involved (multiple related utility types, generic constraints, edge cases), link out instead — the TypeScript Handbook (`typescriptlang.org/docs/handbook`) is the default source
- Skip this line for sub-concepts that are pure mental-model topics without one canonical doc page (e.g. structural typing, variance) — don't force a citation where none adds value

---

## Exercise Format Rules

### Coding Challenge
- State the problem clearly (1–3 sentences)
- Provide starter code if it helps focus the exercise
- Show expected behaviour (what should type-check, what shouldn't, what the inferred type should be)
- Keep scope tight — one concept, one small type or snippet
- Prefer drills that exercise the type system (write a type, fix a type error, predict an inferred type) over runtime behaviour
- After answer: show a clean reference solution + explain key decisions

### Q&A
- Ask exactly **one** focused question about the chosen sub-concept (or the combined sub-concepts, if two topics were picked)
- Pick whichever format best fits: conceptual ("what's the difference between X and Y?"), predict-the-type (given this code, what does TS infer?), spot-the-bug (why does this fail to compile?), or true/false on type-system rules
- Favour a question that tests the *mental model*, not memorised syntax
- If two topics were combined, keep it scoped tightly enough to stay within 5–10 minutes — don't stack unrelated complexity
- After answer: reveal the correct answer with a full explanation

### General Rules
- Target: **one question per session**, sized to be completable in 5–10 minutes — not several smaller questions time-boxed to fit
- Tone: encouraging — this is a daily habit, not an exam
- Never pick the same topic two sessions in a row (if the user mentions they just did one)
- Vary difficulty of sub-concept within the chosen tier
- For TS specifically: when showing inferred types, use the `// ^?` convention or write the inferred type explicitly

---

## Tier Filtering

| User says | Behaviour |
|---|---|
| `/daily-ts` or `/daily-ts random` | Full pool, all 50 topics |
| `/daily-ts foundations` | Topics 1–14 only (mental models + sharp basics) |
| `/daily-ts core` | Topics 15–30 only (daily patterns) |
| `/daily-ts mastery` | Topics 31–42 only (type-system mastery) |
| `/daily-ts tooling` | Topics 43–50 only (tooling & ecosystem) |
| `/daily-ts narrowing` | Force that specific topic |
| `/daily-ts mastery coding` | Mastery tier, coding format only |
| `/daily-ts generics q&a` | Force generics topic, Q&A format |

---

## Response Structure

```
🎯 Today's TS Drill — [Topic Name]: [Sub-concept]
Tier: Foundations / Core / Mastery / Tooling
Format: Coding Challenge / Q&A
Estimated time: ~X minutes
📚 Docs: [inline signature, or TS Handbook link — omit if not applicable]

[Exercise content]
```

After user responds:
```
✅ Feedback

[What they got right]
[What to fix / watch out for]

💡 Reference solution / correct answers:
[Solution with brief explanation, including the mental model it reinforces]
```

---

## Topic Source

See [TOPICS.md](TOPICS.md) for all 50 topics and their sub-concepts.
