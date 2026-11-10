# Get Full Stack — C# / .NET

Notes from **Get Full Stack**, a recurring session series that walks through C#/.NET backends from a front-end engineer's point of view.

Some sessions become a reference sheet, a self-contained HTML page made with the [explainer-sheet](../../../explainer-sheet/) skill. Others aren't published here.

## Sessions

| Week | Date | Topic | Sheet |
| --- | --- | --- | --- |
| 1 | 28 Aug 2026 | Clean architecture primer | [HTML](week-01-clean-architecture-primer.html) |
| 2 | 18 Sep 2026 | Build a basic API | [HTML](week-02-build-a-basic-api-v1.0.html) |
| 3 | 09 Oct 2026 | Stripe webhooks | Not published |

### Week 1: Clean architecture primer

Four questions to ask of any backend, taught through one .NET service:

1. **Boundaries:** do we own this code, or do we only call it?
2. **Dependency direction:** which way do dependencies point?
3. **Lifetimes:** how long do things live, and who shares them?
4. **Errors:** how does a service say no?

### Week 2: Build a basic API

A recipe for building a small .NET 10 API from an empty folder: FastEndpoints, the four-project split, an in-memory repository and dependency-injection lifetimes.

## Conventions

- **File names:** `week-NN-topic.html`, optionally with a `-vX.Y` version.
- **Status:** a week with no `.html` file has no published sheet.
