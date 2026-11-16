---
name: se-tag
description: Tags software engineering topics with a classification prefix (emoji, root category abbreviation, subtopic) from a fixed 13-category taxonomy. Use only when the user invokes /se-tag or asks for this skill by name; then classify every topic they send, singly or as a list, for the rest of the conversation.
metadata:
  version: "1.0"
---

# SE Tag

Prepend each software engineering topic with its place in the taxonomy below.

## Format

```
[{emoji} {ABBR} › {Subtopic}] {Topic as given}
```

- **Subtopic**: 1–3 words naming the area inside the category. Prefer the suggested subtopics below; coin a new one only when none fit.
- **Topic as given**: keep the user's wording unchanged.

## Taxonomy

| # | Emoji | Abbr | Category | Suggested subtopics |
|---|---|---|---|---|
| 1 | 🔢 | CS | Computer Science Fundamentals | DSA, Complexity, OS, Networking, Concurrency, Memory, Compilers |
| 2 | 🏗️ | ARCH | Software Design & Architecture | Patterns, SOLID, DDD, Modularity, Microservices, Event-Driven |
| 3 | 🖥️ | FE | Front-end & Client | Web, Mobile, Desktop, Rendering, State, Accessibility |
| 4 | ⚙️ | BE | Back-end & APIs | HTTP, REST, GraphQL, gRPC, Auth Flows, Jobs, Messaging |
| 5 | 🗄️ | DATA | Data & Storage | SQL, NoSQL, Modelling, Indexing, Transactions, Pipelines |
| 6 | ☁️ | DIST | Distributed Systems & Cloud | Consistency, Replication, Partitioning, Queues, Scaling, Cloud |
| 7 | 📈 | SRE | Performance, Reliability & Observability | Caching, Profiling, Load, SLOs, Incidents, Observability |
| 8 | 🚀 | OPS | DevOps & Platform Engineering | CI/CD, IaC, Containers, Orchestration, Releases, Environments |
| 9 | 🧪 | QA | Testing & Quality | Unit, Integration, E2E, Contract, TDD, Static Analysis |
| 10 | 🔒 | SEC | Security | AuthN/AuthZ, OWASP, Threat Modelling, Secrets, Supply Chain |
| 11 | 🤖 | AI | AI & ML Engineering | LLM Apps, RAG, Agents, Evals, MLOps |
| 12 | 📋 | PRAC | Engineering Practice & Process | Git Workflow, Code Review, Agile, Docs, Leadership |
| 13 | 🛠️ | TOOL | Developer Tooling & Productivity | Build, Packages, IDEs, Monorepos, AI Coding |

## Rules

1. Pick the single best-fit category: the one the topic is mainly *about*, not everything it touches.
2. **One topic sent** → output the tagged line, then one short sentence on why. If a second category is a strong runner-up, name it in a few words.
3. **List of topics** → output only the tagged lines, one per topic, in the original order. Keep the user's list markup (numbers, bullets) if present.
4. If the user adds their own guess (e.g. "DNS - 1?"), confirm or correct it in the reason.
5. Industry verticals (payments, fintech, healthcare) are not categories: tag by the engineering concern at the heart of the topic.
6. "New" tech gets no special bucket: tag it by its domain.

## Examples

Single topic: `Top 9 HTTP Request Methods`

```
[⚙️ BE › HTTP] Top 9 HTTP Request Methods
```
HTTP methods are the core vocabulary of API design.

List:

```
- [🔢 CS › Networking] DNS
- [📈 SRE › Caching] HTTP headers & caching
- [🗄️ DATA › Indexing] How B-trees power database indexes
- [🤖 AI › RAG] Chunking strategies for vector search
```
