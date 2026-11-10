---
name: daily-js
description: Daily JavaScript practice drill. Randomly selects a JS topic or sub-topic from a curated beginner-to-advanced list and generates a focused 5–10 minute coding exercise or Q&A. Use when the user types /daily-js, asks for a daily JS drill, JavaScript practice, or a JS exercise to complete today.
metadata:
  version: "1.0"
---

# Daily JS Drill

A habit-forming daily JavaScript exercise. Each session targets one concept or sub-concept, takes 5–10 minutes, and ends with feedback.

## On Invocation

1. Read [TOPICS.md](TOPICS.md) — the full pool of 48 topics with sub-concepts
2. Pick **one topic** at random (respect level filter if provided — see below). Occasionally (when it makes for a richer single question) pick a second topic to combine with it — only if the combined question still fits comfortably in 5–10 minutes; default to one topic.
3. Pick **one specific sub-concept** per topic chosen (e.g. topic: Loops → sub-concept: `for...of`). If it centers on a specific built-in method/API, prepare a docs reference — see **Docs Reference** below
4. Choose exercise format: **coding challenge** or **Q&A** — vary these day to day, don't repeat the same format twice in a row if the user is on a streak
5. Present the exercise clearly and wait for the user's response
6. After the user responds: give thorough feedback — what's correct, what's off, and show the ideal solution with a short *why* explanation

---

## Docs Reference

When the sub-concept centers on a specific built-in method, operator, or syntax feature (e.g. `Array.prototype.reduce`, optional chaining, `Promise.allSettled`), surface a docs reference alongside the exercise header:
- If the signature/summary fits in one line, write it inline — e.g. `reduce(callbackFn, initialValue?) → reduces the array to a single value`
- If the full picture is more involved (multiple overloads, edge cases, related methods), link out instead — MDN (`developer.mozilla.org`) is the default source
- Skip this line for sub-concepts that are pure language mechanics or mental models without one canonical doc page (e.g. hoisting, the event loop, `this` binding rules) — don't force a citation where none adds value

---

## Exercise Format Rules

### Coding Challenge
- State the problem clearly (1–3 sentences)
- Provide starter code if it helps focus the exercise
- Show expected output or behaviour
- Keep scope tight — one concept, one small function or snippet
- After answer: show a clean reference solution + explain key decisions

### Q&A
- Ask exactly **one** focused question about the chosen sub-concept (or the combined sub-concepts, if two topics were picked)
- Pick whichever format best fits: conceptual ("what does X do?"), predict-the-output, spot-the-bug, or true/false
- If two topics were combined, keep it scoped tightly enough to stay within 5–10 minutes — don't stack unrelated complexity
- After answer: reveal the correct answer with a full explanation

### General Rules
- Target: **one question per session**, sized to be completable in 5–10 minutes — not several smaller questions time-boxed to fit
- Tone: encouraging — this is a daily habit, not an exam
- Never pick the same topic two sessions in a row (if the user mentions they just did one)
- Vary difficulty of sub-concept within the chosen level tier

---

## Level Filtering

| User says | Behaviour |
|---|---|
| `/daily-js` or `/daily-js random` | Full pool, all 48 topics |
| `/daily-js beginner` | Topics 1–14 only |
| `/daily-js intermediate` | Topics 15–32 only |
| `/daily-js advanced` | Topics 33–48 only |
| `/daily-js loops` | Force that specific topic |
| `/daily-js advanced coding` | Advanced tier, coding format only |
| `/daily-js closures q&a` | Force closures topic, Q&A format |

---

## Response Structure

```
🎯 Today's JS Drill — [Topic Name]: [Sub-concept]
Level: Beginner / Intermediate / Advanced
Format: Coding Challenge / Q&A
Estimated time: ~X minutes
📚 Docs: [inline signature, or MDN link — omit if not applicable]

[Exercise content]
```

After user responds:
```
✅ Feedback

[What they got right]
[What to fix / watch out for]

💡 Reference solution / correct answers:
[Solution with brief explanation]
```

---

## Topic Source

See [TOPICS.md](TOPICS.md) for all 48 topics and their sub-concepts.
