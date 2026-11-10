# Worked example — "how our job queue retries"

A concrete model of the voice and the overview/reference split, on a topic
unrelated to any particular tool. Read the weak draft, then the revision.

## 1. The definition line

**Weak**

> In this guide we'll take a look at the retry system, which is a really
> important part of how the queue works. Understanding it is key to debugging
> stuck jobs, so let's dive in.

Nothing here is a fact. "Guide", "take a look", "really important", "key to",
"let's dive in" — the deletion test removes the whole paragraph.

**Revised**

> Retry is a **back-off loop the worker runs around a failed job**, re-queueing
> it with a growing delay until it succeeds or exhausts its attempts.
>
> | | |
> |---|---|
> | **It is** | A per-job loop, owned by the worker that picked the job up |
> | **It isn't** | A queue-level feature. The broker never retries anything, and a dead worker's job is recovered by the lease timeout, not by retry |

One sentence names the category. The "isn't" column pre-empts the common
mis-model, which is usually the highest-value content on the page.

## 2. Splitting overview from reference

The temptation is to explain the full back-off formula where it first comes up.
Resist it: that detail belongs in the reference section, and putting it in the
overview unbalances the part and buries the shape.

**Overview (part 2) — short, with a pointer**

> Four attempts by default, with the delay growing each time. The exact formula
> and every setting that changes it are in [6B](#b).
>
> ```
> attempt 1 ──10s──▶ attempt 2 ──40s──▶ attempt 3 ──160s──▶ attempt 4 ──▶ dead letter
> ```

**Reference (6B) — the depth**

> | Setting | Default | Effect |
> |---|---|---|
> | `max_attempts` | 4 | Total tries, including the first |
> | `base_delay` | 10s | The first gap |
> | `factor` | 4 | Multiplier per attempt |
> | `jitter` | `full` | Randomises each delay across `[0, computed]` |
> | `max_delay` | 1h | Ceiling the formula is clamped to |
>
> Delay is `min(base_delay × factor^(n-1), max_delay)`, then jittered. Jitter is
> on by default because synchronised retries from many workers re-create the
> outage that caused the failure.

The same fact is not in both places — the overview has the shape, the reference
has the numbers, and the pointer joins them.

## 3. Fluff, before and after

| Weak | Revised |
|---|---|
| "It's worth noting that jitter is applied deliberately." | "Jitter is applied by default." |
| "The single biggest reason jobs get stuck is a missing ack." | "Jobs get stuck most often from a missing ack." |
| "A one-time setup, then the few gotchas that catch people out." | "One-time setup, then the common mistakes." |
| "What one ordinary retry cycle costs you" *(heading)* | "What a retry cycle costs" *(heading)* |
| "This is reviewed in its own right." | "This is itself reviewed." |

## 4. Prose that should have been a table

**Weak**

> If a job throws a transient error it will be retried, but if it throws a
> permanent error it goes straight to the dead letter queue, and if it times out
> the behaviour depends on whether the lease expired first, in which case another
> worker may already have picked it up.

**Revised**

> | Outcome | What happens | Retried? |
> |---|---|---|
> | `TransientError` | Re-queued with back-off | Yes |
> | `PermanentError` | Straight to dead letter | No |
> | Timeout, lease still held | Worker marks it failed, re-queues | Yes |
> | Timeout, lease expired | Another worker already has it; this result is discarded | n/a |

Four cases in a sentence is a reading task. Four cases in a table is a lookup.

## 5. Surfacing a correction

Verification against the source turned up something the docs imply but don't
state. Say it in the page rather than quietly writing the correct version:

> **`max_attempts` counts the first try.** Setting it to `1` disables retry
> entirely rather than allowing one retry — a common off-by-one when migrating
> from systems that count retries instead of attempts.

## 6. The resulting shape

```
Title + definition + is/isn't
 1  The big picture      — what retry is, who owns it, the diagram
 2  Everyday use         — the defaults, the four-attempt shape, pointers
 3  How it really works  — lease, ack, the failure classes
 4  Setup & gotchas      — config location, the off-by-one, poison jobs
 5  The details
     5A  Every setting, with defaults and effects
     5B  The back-off formula and jitter modes
     5C  Failure classes and where each one lands
     5D  Operating it — draining, replaying dead letters, metrics
```

Parts 1–4 are each roughly a screen. Part 5 is as long as it needs to be, and is
the part the reader returns to.
