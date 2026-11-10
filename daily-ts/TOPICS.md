# TypeScript Topics — Full Drill Pool

Used by the daily-ts skill to randomly select a topic and sub-concept for each session.

---

## 🟢 FOUNDATIONS (Topics 1–14) — mental models + sharp basics

### 1. What TypeScript Is
Sub-concepts: TS as a superset of JS; structural type system; types are erased at runtime (not enforced); TS as a compile-time checker not a runtime; value of a separate type-check step; relationship between `.ts` and `.js` files

### 2. Type Space vs Value Space
Sub-concepts: types and values live in separate namespaces; you can have a type and a value with the same name (e.g. classes do both); types disappear at runtime so you can't `if (x instanceof MyTypeAlias)`; why `typeof` means different things in value vs type position

### 3. Structural Typing
Sub-concepts: shape-based assignability ("if it has the right shape, it fits"); duck typing; excess property checks on object literals; objects with extra properties are still assignable to narrower types when passed as variables; contrast with nominal typing in C#/Java

### 4. Type Annotations vs Inference
Sub-concepts: when TS can infer (locals, return types, callback parameters via contextual typing); when to annotate (public function parameters, exported APIs, ambiguous returns); inference at boundaries vs inside functions; the principle "annotate inputs, infer outputs"

### 5. Literal Types & Widening
Sub-concepts: string/number/boolean literal types (`'foo'` is a type); `const x = 'foo'` infers `'foo'`, `let x = 'foo'` widens to `string`; widening on assignment and in object literals; `as const` to preserve literals; how widening interacts with function returns

### 6. Arrays vs Tuples
Sub-concepts: `T[]` vs `Array<T>`; tuples `[T, U]` have fixed length and ordered types; optional tuple elements (`[T, U?]`); rest in tuples (`[string, ...number[]]`); `readonly` tuples; when a tuple is the right model vs an array

### 7. Object Types & Optional Properties
Sub-concepts: inline object types vs named types; optional properties (`?:`); index signatures (`{ [k: string]: T }`); index signatures and concrete keys together; excess property checks on literals; when to reach for `Record<K, V>` instead

### 8. Type Aliases vs Interfaces
Sub-concepts: `interface` declaration merging; `type` for unions, primitives, and computed types; extension via `extends` (interfaces) vs intersection (types); performance and error-message differences; team-style consistency

### 9. Functions
Sub-concepts: parameter type annotations; return type annotations; `void` return; contextual typing of callbacks; rest parameters typed as arrays/tuples; function type expressions vs call signatures; arrow vs regular function typing

### 10. Union & Intersection Types
Sub-concepts: `A | B` (either A or B); `A & B` (both A and B simultaneously); why unions of objects narrow the *available* properties to the common ones; why intersections of objects combine properties; mental model of unions and intersections in terms of sets of possible values

### 11. `any` vs `unknown` vs `never` vs `void`
Sub-concepts: `any` opts out of checking (top of the lattice but also unsafe); `unknown` is the safe top type (must narrow before use); `never` is the bottom type (empty set, unreachable code); `void` means "no useful return"; why `any` is contagious and `unknown` isn't

### 12. Type Assertions (`as`)
Sub-concepts: telling TS "trust me, it's this type"; assertions don't change runtime; `as unknown as X` for impossible casts; `<T>x` syntax (avoid in JSX); when assertions hide real bugs; assertions vs `satisfies` vs annotation

### 13. `as const`
Sub-concepts: makes literals stay narrow; makes object properties readonly; turns arrays into readonly tuples; pairs with `typeof` to derive types from data; common pattern for config objects, action types, and route definitions

### 14. Enums
Sub-concepts: numeric enums (with reverse mappings); string enums; const enums (inlined, no runtime object); runtime cost of regular enums; isolatedModules and const enums; why many teams prefer `as const` unions instead

---

## 🟡 CORE PATTERNS (Topics 15–30) — daily work

### 15. Narrowing
Sub-concepts: `typeof` narrowing (primitives); `instanceof` narrowing (classes); `in` operator narrowing (checking properties); truthiness narrowing; equality narrowing (`===`, `!==`); how TS tracks narrowing through control flow; how reassignment widens again

### 16. Discriminated Unions
Sub-concepts: a common literal property (the discriminant, e.g. `kind` or `type`); narrowing on the discriminant in `switch` or `if`; exhaustive switch with `never` default to catch missing cases; well-typed reducer pattern

### 17. Type Predicates & Assertion Functions
Sub-concepts: user-defined type guards (`function isFoo(x): x is Foo`); assertion functions (`function assertFoo(x): asserts x is Foo`); when each is appropriate; pitfalls of unsound predicates that don't actually check what they claim

### 18. `keyof` & Indexed Access (`T[K]`)
Sub-concepts: `keyof T` produces the union of T's keys; `T[K]` produces the type of property K; `T[keyof T]` produces the union of T's value types; the `K extends keyof T` pattern in generic helpers

### 19. `typeof` in Type Position
Sub-concepts: getting the type of a runtime value; typing existing JS objects (config, constants); combining `typeof` with `keyof` and indexed access; deriving types from a single source of truth in data

### 20. Optional vs `| undefined`
Sub-concepts: `x?: T` allows the property to be missing entirely; `x: T | undefined` requires the property but allows undefined; `exactOptionalPropertyTypes` makes these meaningfully different; interaction with `Partial<T>` and object spread

### 21. Generics: the basics
Sub-concepts: generic functions; type parameter inference from arguments; generic interfaces and type aliases; the mental model of generics as "functions over types"; when generics actually pay off (relating two values) vs when they're noise

### 22. Generic Constraints (`extends`)
Sub-concepts: constraining T to have a shape (`T extends { id: string }`); the `K extends keyof T` pattern for safe property access; default constraints; constraints as "T can be anything that satisfies this"

### 23. Default Type Parameters
Sub-concepts: `<T = string>` syntax; ordering — defaulted params come after non-defaulted; defaults with constraints (`<T extends Foo = Foo>`); when defaults reduce friction at call sites

### 24. Utility Types: Shape Manipulation
Sub-concepts: `Partial<T>` (all optional); `Required<T>` (all required); `Readonly<T>`; `Pick<T, K>` (subset of keys); `Omit<T, K>` (everything but K); composing these for API request/response types

### 25. Utility Types: Set Operations
Sub-concepts: `Record<K, V>` (object with K keys and V values); `Exclude<T, U>` (remove members from a union); `Extract<T, U>` (keep matching members); `NonNullable<T>` (strip null/undefined); thinking in terms of union sets

### 26. Utility Types: Function Introspection
Sub-concepts: `ReturnType<F>` (extract return type); `Parameters<F>` (extract param tuple); `ConstructorParameters<C>`; `Awaited<P>` (recursively unwrap Promises); when to derive vs declare types

### 27. Function Overloads
Sub-concepts: multiple overload signatures + one implementation signature; the implementation signature isn't directly callable from outside; when overloads beat unions (different param→return relationships); pitfalls (overlap, ordering)

### 28. Class Typing
Sub-concepts: `abstract` classes and methods; access modifiers `public`/`private`/`protected`; `#private` true private fields (runtime-enforced); parameter properties shorthand; `implements` vs `extends`; class as type vs class as value

### 29. Error Handling in TS
Sub-concepts: `catch (err: unknown)` (default since TS 4.4); narrowing with `instanceof Error`; `useUnknownInCatchVariables`; typed Result patterns (`{ ok: true, value } | { ok: false, error }`); throwing typed errors

### 30. Async & Promises
Sub-concepts: `Promise<T>` inference; `async` functions always return Promises; `await` unwraps one level; `Awaited<T>` recursively unwraps; common gotcha: forgetting `await` and getting `Promise<T>` where you expected `T`

---

## 🔴 TYPE SYSTEM MASTERY (Topics 31–42) — the compounding tier

### 31. Conditional Types
Sub-concepts: `T extends U ? X : Y`; reading conditional types as type-level if-statements; building helpers that branch on input type; common patterns (`IsArray<T>`, `IsNever<T>`)

### 32. `infer` Keyword
Sub-concepts: extracting types inside conditional types; `infer R` in a return position to extract return type; multiple `infer`s; `infer extends` for constrained inference; inferring element types from arrays

### 33. Distributive Conditional Types
Sub-concepts: when the type parameter is naked, the conditional distributes over unions; `[T] extends [U]` (wrapped) prevents distribution; when distribution helps (mapping a union) vs hurts (testing the whole union as a set)

### 34. Mapped Types
Sub-concepts: `{ [K in keyof T]: ... }` iterates keys at the type level; transforming property types; modifiers `+?`/`-?` (add/remove optional); `+readonly`/`-readonly`; building `Partial` and `Required` from scratch

### 35. Key Remapping (`as` in mapped types)
Sub-concepts: `{ [K in keyof T as NewKey]: ... }`; filtering keys by mapping to `never`; renaming keys via template literals (e.g. `on${Capitalize<K>}`); building event-handler types from data shapes

### 36. Template Literal Types
Sub-concepts: concatenation in type position (`` `${A}-${B}` ``); `Uppercase`/`Lowercase`/`Capitalize`/`Uncapitalize`; inferring substrings from patterns (`` `${infer Head}-${infer Tail}` ``); typing string-shaped APIs (CSS units, route paths)

### 37. Recursive Types
Sub-concepts: types that reference themselves (e.g. JSON, tree structures); recursive conditional types; depth/instantiation limits (~50 deep historically); tail-recursive patterns to avoid hitting limits

### 38. `satisfies` Operator
Sub-concepts: check a value conforms to a type without widening it; vs `as` (which can widen or narrow unsoundly); vs annotation (which widens to the annotation); the "validate but keep narrow" pattern for config objects

### 39. Branded / Nominal Types
Sub-concepts: TS is structural by default — any two types with the same shape are interchangeable; branding via intersection with a phantom property (`type UserId = string & { __brand: 'UserId' }`); opaque type pattern; when nominal helps (IDs, currency, units)

### 40. Const Type Parameters (`<const T>`)
Sub-concepts: preserving literal types through generic calls without `as const` at the call site; effect on inference for object and array arguments; when to reach for it (DSLs, type-level config)

### 41. Variance
Sub-concepts: covariance (return types — narrower is fine); contravariance (parameter types — wider is fine); bivariance in TS for method parameters by default (with the `strictFunctionTypes` exception); the classic example `Dog[]` vs `Animal[]` and why it can be unsound

### 42. `this` Types & Polymorphic `this`
Sub-concepts: explicit `this` parameter in function signatures; `this` as a return type for fluent/builder APIs; how polymorphic `this` lets subclass methods return the subclass type; comparison with manually returning a generic

---

## 🔧 TOOLING & ECOSYSTEM (Topics 43–50) — what persists

### 43. Type Checking vs Transpilation
Sub-concepts: `tsc` does both type-checking and emitting JS; `esbuild`/`swc`/Babel only strip types (no checking); why teams typically split it: bundler builds, `tsc --noEmit` checks in CI; speed vs correctness trade-off

### 44. `tsconfig.json` — the keys that matter
Sub-concepts: `target` (output JS version, e.g. `ES2022`); `module` (output module format, e.g. `ESNext`); `moduleResolution` (how imports resolve); `lib` (which built-in APIs are available); `jsx`; `outDir`/`rootDir`; `include`/`exclude`/`files`

### 45. Strict Mode
Sub-concepts: `strict: true` as an umbrella flag; `strictNullChecks` (null/undefined as separate types you must handle); `noImplicitAny`; `strictFunctionTypes`; `noUncheckedIndexedAccess` (array/index access returns `T | undefined`); `noImplicitOverride`; why these flags pay off long-term

### 46. Declaration Files (`.d.ts`)
Sub-concepts: declaration files describe types without implementation; `@types/*` packages and DefinitelyTyped community; ambient declarations for globals; when you'd write your own `.d.ts` (untyped JS dependencies, declaring `window` extensions, asset modules)

### 47. Module Resolution
Sub-concepts: `node` (legacy CommonJS-style resolution); `node16`/`nodenext` (modern Node with package.json `exports`); `bundler` (recommended for FE with Vite/webpack/etc.); how TS walks `node_modules`; `paths` aliases (and that bundlers need their own alias config to match)

### 48. `isolatedModules` & `verbatimModuleSyntax`
Sub-concepts: `isolatedModules` enforces that each file can be compiled independently (required by esbuild/swc/Babel); `verbatimModuleSyntax` makes import elision explicit; why type-only imports (`import type`) matter when these are on; common errors and fixes

### 49. Module Augmentation & Ambient Declarations
Sub-concepts: `declare module 'lib-name'` to extend third-party module types; `declare global` to add to global scope (e.g. `Window` extensions); augmenting existing interfaces (interface merging across files); typing asset imports (`*.svg`, `*.css`)

### 50. TS with React (conceptual)
Sub-concepts: typing props (interface vs type, optional props, default values); typing children (`ReactNode` vs `ReactElement` vs `JSX.Element`); event handler types (`ChangeEvent`, `MouseEvent`, etc.); ref typing concepts; the *concepts* persist even as APIs (forwardRef, etc.) shift between React versions
