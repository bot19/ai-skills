# Software-Engineering / Front-End Architecture Topics — Full Drill Pool

Used by the daily-se skill to pick a topic + sub-concept for each session.

Grounded in field-standard frameworks: the **RADIO** front-end system-design framework, the **roadmap.sh** front-end roadmap, **patterns.dev**, and **Feature-Sliced Design** — not any single set of personal notes.

Tags: `[FE]` front-end · `[BE]` back-end / full-stack. `RADIO:` shows which letter(s) of the framework the topic maps to. Long-run mix target ≈75% FE / 25% BE.

For any sub-concept naming a technology category, the drill makes the user **pick a concrete option and justify it** (see SKILL.md).

---

## 🧭 TIER 1 — REQUIREMENTS & ARCHITECTURE FOUNDATIONS (Topics 1–4)

### 1. Requirements → Goals → Measure  [FE] · RADIO: R
Sub-concepts: starting from the ask, not the stack ("what is this, who's it for?"); functional vs non-functional requirements; deriving the goal (conversion / activation / retention / task success) and the metric that proves it; how project *type* (marketing site / SaaS SPA / content site / internal tool) reshapes every downstream choice; surfacing constraints early (team, timeline, devices, network, scale); balancing structure / performance / scalability / team against requirements and time

### 2. Architecture Styles & High-Level Design  [FE] · RADIO: A
Sub-concepts: SPA vs MPA vs SSR-app vs static site vs islands — picking one for a brief and *why*; component-based architecture; layered/modular organisation; micro-frontends vs a modular monolith (and why the monolith usually wins); Feature-Sliced Design and other slicing conventions; Conway's law / how team shape drives architecture; the RADIO walkthrough as a repeatable method

### 3. Web Platform & Network Fundamentals  [FE] · RADIO: A/I
Sub-concepts: how the browser turns bytes into pixels (parse → DOM/CSSOM → render → paint → composite); the critical rendering path; HTTP/1.1 vs HTTP/2 vs HTTP/3 and why multiplexing matters; request lifecycle, status codes, headers; DNS/TLS/connection cost; CORS (what it actually protects); cookies and SameSite; the cost of a round-trip and why it shapes data design

### 4. Tech Stack & Tooling  [FE] · RADIO: A
Sub-concepts: framework choice (React / Vue / Svelte / Angular / Solid — and *why* for a brief); meta-framework (Next.js / Nuxt / SvelteKit / Remix / Astro); language (TS by default, and why); bundler/dev-server (Vite / webpack / Turbopack / esbuild); package manager (pnpm / npm / yarn) and monorepo tooling (Turborepo / Nx); lint/format (ESLint, Prettier, Biome); boring vs novel tech and the maintenance cost of each

---

## 🏗️ TIER 2 — CORE FRONT-END DECISIONS (Topics 5–13) — the RADIO body

### 5. Rendering & Application Strategy  [FE] · RADIO: A/O
Sub-concepts: CSR vs SSR vs SSG vs ISR vs streaming SSR — what each buys and costs; the SEO / TTFB / interactivity / infra tradeoff; hydration cost and partial/progressive hydration; islands (Astro) and React Server Components; edge vs origin rendering; when an SPA is wrong (content sites) and when SSG is wrong (per-user dynamic)

### 6. Routing & Navigation  [FE] · RADIO: A
Sub-concepts: client-side vs file-based routing; nested / dynamic / catch-all routes; route-based code splitting; layouts and shared UI; route guards / protected routes; route-tied data loading (loaders); deep linking, scroll restoration, back/forward semantics; URL as state

### 7. Component Architecture & Code Structure  [FE] · RADIO: A
Sub-concepts: atomic vs feature-based (vertical slice) organisation and when each fits; colocation; controlling coupling and dependency direction; shared-vs-feature boundaries; folder structure for a website vs a web app; barrel files and circular deps; designing component boundaries that match the data and a11y needs

### 8. Component Design Patterns  [FE] · RADIO: A/I
Sub-concepts: presentational vs container split; compound components; render props and function-as-child; higher-order components (and why hooks largely replaced them); custom hooks / composables for logic reuse; headless components; controlled vs uncontrolled; prop-drilling vs composition vs context (patterns.dev canon)

### 9. State Management  [FE] · RADIO: D
Sub-concepts: the categories — local UI, shared client, server-cache, URL, form state; not conflating server state with client state; picking a client store (Context / Zustand / Redux Toolkit / Jotai / signals) and *why*; when you need a store at all vs lifting/composition; how broad state containers cause excess re-renders; persistence (localStorage / cookies / IndexedDB) and its pitfalls

### 10. Data Fetching & Server State  [FE] · RADIO: D/I
Sub-concepts: server-cache libraries (TanStack Query / SWR / RTK Query / Apollo) and what they solve (caching, dedup, revalidation, optimistic updates); fetch-on-render vs render-as-you-fetch vs route loaders; request waterfalls vs parallelisation; cache invalidation strategy; optimistic UI + rollback; pagination/infinite scroll; loading/error as first-class states

### 11. API Contracts & Type Safety  [FE] · RADIO: I
Sub-concepts: end-to-end type safety (tRPC / GraphQL codegen / OpenAPI codegen) and tradeoffs; sharing types across FE/BE in a monorepo; runtime validation at the boundary (don't trust the network — parse with Zod/Valibot); generated vs hand-written clients; designing component prop APIs; where types give false confidence

### 12. Styling, Theming & Design Systems  [FE] · RADIO: A/O
Sub-concepts: CSS strategy (Tailwind / CSS Modules / vanilla-extract / styled-components / plain CSS) and the runtime-vs-build tradeoff; the cascade, specificity, and scaling CSS without leakage; design tokens and theming (light/dark, multi-brand); component library build vs buy (shadcn/ui / Radix / MUI / Mantine / headless + own styles); consistency and governance

### 13. Forms & Validation  [FE] · RADIO: D/I/O
Sub-concepts: controlled vs uncontrolled; form libraries (React Hook Form / Formik / native) and why; schema validation shared client+server (Zod / Yup / Valibot); client vs server validation responsibilities; accessible error messaging; multi-step / dynamic forms; submission, pending, and optimistic states

---

## 🎯 TIER 3 — CROSS-CUTTING QUALITY & UX (Topics 14–21) — the "O" in RADIO

### 14. Performance & Core Web Vitals  [FE] · RADIO: O
Sub-concepts: LCP, INP, CLS — what moves each; code splitting & lazy loading; bundle analysis and shrinking JS; image/asset optimisation (formats, responsive, lazy); preload/prefetch/priority hints; render performance (memoisation, virtualisation, avoiding re-renders); measure before optimising; performance budgets

### 15. Browser Runtime & Rendering Internals  [FE] · RADIO: O
Sub-concepts: the event loop, macro/microtasks, and why long tasks block input (INP); reflow vs repaint and layout thrashing; DOM vs virtual DOM vs fine-grained reactivity (signals); requestAnimationFrame / requestIdleCallback; memory leaks in SPAs (listeners, closures, detached nodes); web workers for offloading

### 16. Caching & Delivery  [FE] · RADIO: O
Sub-concepts: HTTP caching (Cache-Control, ETag, stale-while-revalidate); CDN and edge caching; cache busting via content hashing; service workers and offline caching strategies; asset immutability vs HTML freshness; the layered cache picture (browser → CDN → origin) and where to invalidate

### 17. Accessibility  [FE] · RADIO: O
Sub-concepts: semantic HTML first, ARIA second; keyboard navigation and focus management (trap, restore); screen-reader behaviour and live regions; colour contrast and WCAG levels (A/AA/AAA); accessible forms, modals, menus; testing (axe + manual keyboard/SR passes); a11y as a standard set at init, not bolted on

### 18. Internationalisation  [FE] · RADIO: O
Sub-concepts: i18n libraries (i18next / react-intl / FormatJS); locale routing and detection; message extraction, pluralisation, ICU; RTL layout; date/number/currency via the Intl API; bundle impact of locale data; translation workflow and fallbacks

### 19. Responsive & Cross-Device Design  [FE] · RADIO: O
Sub-concepts: mobile-first vs desktop-first; fluid layouts, container queries, modern CSS layout (grid/flex); breakpoints and the cost of device fragmentation; touch vs pointer vs keyboard input; responsive images (srcset/sizes); testing across viewports; performance on low-end devices and slow networks

### 20. SEO & Discoverability  [FE] · RADIO: O
Sub-concepts: why rendering strategy drives crawlability (CSR vs SSR/SSG); meta tags, Open Graph, structured data (JSON-LD); semantic markup and headings; sitemaps and canonical URLs; Core Web Vitals as a ranking input; when SEO matters (marketing/content) vs when it doesn't (auth'd apps)

### 21. Front-End Security  [FE] · RADIO: O
Sub-concepts: XSS (framework escaping; where `dangerouslySetInnerHTML`/`v-html` bite); CSP; CSRF and SameSite cookies; auth token storage (cookie vs localStorage tradeoffs, XSS exposure); never shipping secrets in the bundle; dependency/supply-chain risk; clickjacking and security headers

---

## 🛠️ TIER 4 — DELIVERY & OPERATIONS (Topics 22–30)

### 22. Testing Strategy  [FE] · RADIO: O
Sub-concepts: testing trophy vs pyramid for FE; unit (Vitest/Jest), component/integration (Testing Library), E2E (Playwright/Cypress); what to test at each layer; testing behaviour not implementation; mocking the network (MSW); visual regression; coverage as a signal, not a goal

### 23. CI/CD & Deployment  [FE] · RADIO: O
Sub-concepts: pipeline stages (install → lint → typecheck → test → build → deploy); CI providers (GitHub Actions / GitLab CI / CircleCI); deploy targets (Vercel / Netlify / Cloudflare / containers / S3+CDN) and why; preview/staging deploys per PR; caching CI steps; rollback strategy

### 24. Build & Bundle Architecture  [FE] · RADIO: O
Sub-concepts: tree-shaking and side-effect flags; chunking and shared vendor chunks; ESM vs CJS interop; transpile targets and browserslist; source maps in prod; analysing and budgeting bundle size; what actually ends up in the client bundle

### 25. Monitoring & Observability  [FE] · RADIO: O
Sub-concepts: error tracking (Sentry); RUM vs synthetic (Lighthouse CI); RUM for Core Web Vitals; session replay (LogRocket / FullStory) and privacy; responsible client-side logging; alert thresholds; closing the loop from production signal to a fix

### 26. Error Handling & Resilience  [FE] · RADIO: O
Sub-concepts: error boundaries and graceful degradation; retry/backoff and timeouts on network calls; fallback UI and skeletons; partial failure (one widget fails, page survives); user-facing error messaging; distinguishing expected (validation) from unexpected (bug) errors

### 27. Environment & Configuration Management  [FE] · RADIO: O
Sub-concepts: env vars and what's safe to expose to the client (public vs server-only); multi-env setup (dev/staging/prod); config validation at startup; secrets management (never in the bundle); build-time vs runtime config; 12-factor config applied to FE

### 28. Feature Flags & Experimentation  [FE] · RADIO: O
Sub-concepts: flag types (release, experiment, ops/kill-switch, permission); build-time vs runtime flags; providers (LaunchDarkly / Unleash / homegrown); flag lifecycle and debt; flags + A/B testing; avoiding flag-driven combinatorial complexity

### 29. Dependency & Version Management  [FE] · RADIO: O
Sub-concepts: semver and lockfiles; the true cost of a dependency (bundle, maintenance, supply chain); update automation (Renovate/Dependabot); auditing (npm audit, Snyk); peer-dependency conflicts; pinning vs ranges; the "should we add this at all?" decision

### 30. Collaboration, Governance & Docs  [FE] · RADIO: O
Sub-concepts: code review process and PR size; ADRs (recording *why*, not just what); Storybook / living docs / design-system governance; ownership (CODEOWNERS); linting as automated governance; the "new project tomorrow" onboarding test; keeping decisions discoverable

---

## 🗄️ TIER 5 — BACK-END & FULL-STACK FUNDAMENTALS (Topics 31–38) — enough to ship a production app

### 31. API Design  [BE] · RADIO: I
Sub-concepts: REST vs GraphQL vs RPC/tRPC vs gRPC — picking one and *why*; resource modelling and versioning; pagination, filtering, error shapes; over/under-fetching and the N+1 problem; idempotency; contract-first design; how the API shape constrains the FE data layer

### 32. Authentication & Authorization  [BE] · RADIO: I/O
Sub-concepts: sessions vs JWT and their tradeoffs; OAuth2/OIDC flows (auth code + PKCE for SPAs); where tokens live (httpOnly cookie vs storage) and the security implications; refresh tokens and rotation; RBAC vs ABAC; auth at the edge/gateway vs in the app; SSO concepts

### 33. BFF & API Gateway Patterns  [BE] · RADIO: A/I
Sub-concepts: backend-for-frontend — why a FE-shaped aggregation layer exists; gateway responsibilities (auth, rate-limiting, routing, aggregation); cutting client round-trips and hiding internal services; when a BFF is overkill; edge functions as a lightweight BFF

### 34. Server & Data Caching  [BE] · RADIO: O
Sub-concepts: caching layers (CDN → reverse proxy → app → DB); strategies (cache-aside, write-through); Redis/Memcached use cases; cache invalidation (the hard problem); read replicas and eventual consistency; idempotent cacheable GETs; how server caching changes FE assumptions

### 35. Databases & Data Modelling  [BE] · RADIO: D
Sub-concepts: relational vs document vs key-value — choosing for a use case and *why*; normalisation vs denormalisation; indexing basics and what makes a query slow; transactions / ACID vs eventual consistency; ORMs (Prisma/Drizzle) vs raw SQL; migrations; modelling for the access patterns the FE needs

### 36. Server Architecture & Scaling  [BE] · RADIO: A/O
Sub-concepts: stateless services and horizontal scaling; load balancing and sticky sessions; background jobs and queues (don't do slow work in the request); rate limiting and backpressure; monolith vs modular monolith vs microservices (and why modular monolith is the usual right answer); the cost of premature distribution

### 37. Real-time & Push  [BE] · RADIO: I/O
Sub-concepts: polling vs long-polling vs SSE vs WebSockets — picking one and *why*; scaling stateful connections; optimistic UI + server reconciliation; presence and pub/sub; when "real-time" is really just fast polling; fallbacks and reconnection

### 38. Infrastructure & Deployment Targets  [BE] · RADIO: A/O
Sub-concepts: serverless/functions vs containers vs long-running servers vs edge — tradeoffs (cold starts, statelessness, cost, control); managed platforms (Vercel/Netlify) vs cloud (AWS/GCP) vs PaaS (Render/Fly); CDN and edge compute; IaC concepts (Terraform); environments and zero-downtime deploys; the simplest infra that meets the goal
