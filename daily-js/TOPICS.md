# JavaScript Topics — Full Drill Pool

Used by the daily-js skill to randomly select a topic and sub-concept for each session.

---

## 🟢 BEGINNER (Topics 1–14)

### 1. What is JavaScript
Sub-concepts: how browsers execute JS, the JS engine (V8), role of JS in the web (HTML/CSS/JS), client-side vs server-side JS, the browser console, `<script>` tag placement

### 2. Variables
Sub-concepts: `var`, `let`, `const`; declaration vs initialisation; naming conventions (camelCase); mutability; when to use `let` vs `const`; reassignment errors

### 3. Data Types
Sub-concepts: primitive types (string, number, bigint, boolean, null, undefined, symbol); reference types (objects, arrays, functions); `typeof` operator; difference between `null` and `undefined`

### 4. Operators
Sub-concepts: arithmetic (`+`, `-`, `*`, `/`, `%`, `**`); comparison (`==`, `===`, `!=`, `!==`, `>`, `<`); logical (`&&`, `||`, `!`); assignment (`=`, `+=`, `-=`, etc.); ternary (`? :`); operator precedence

### 5. Type Coercion & Conversion
Sub-concepts: implicit coercion (e.g. `"5" + 2`); explicit conversion (`Number()`, `String()`, `Boolean()`, `parseInt()`, `parseFloat()`); truthy vs falsy values; `==` vs `===` and coercion traps

### 6. Template Literals
Sub-concepts: backtick syntax; string interpolation (`${}`); multi-line strings; expression evaluation inside `${}`; tagged template literals (intro)

### 7. Conditionals
Sub-concepts: `if`, `else if`, `else`; `switch` with `case`, `break`, `default`; nested conditionals; ternary as shorthand; short-circuit as conditional

### 8. Loops
Sub-concepts: `for` (init, condition, increment); `while`; `do...while`; `for...of` (iterables); `for...in` (object keys); `break`; `continue`; nested loops; loop performance basics

### 9. Functions
Sub-concepts: declarations vs expressions; parameters vs arguments; return values; default parameters; function scope; calling functions; void functions; named vs anonymous functions

### 10. Arrays
Sub-concepts: creation and indexing; `length`; `push`, `pop`, `shift`, `unshift`; `splice`, `slice`; `concat`; `indexOf`, `includes`; `join`; `reverse`; `sort`; array of arrays

### 11. Objects
Sub-concepts: key-value pairs; dot notation vs bracket notation; adding, updating, deleting properties; nested objects; object methods; `this` in object methods; `Object.keys()`, `Object.values()`, `Object.entries()`

### 12. DOM Manipulation
Sub-concepts: `getElementById`, `querySelector`, `querySelectorAll`; `textContent` vs `innerHTML`; changing styles; `classList.add`, `remove`, `toggle`, `contains`; `createElement`, `appendChild`, `removeChild`; `getAttribute`, `setAttribute`

### 13. Events
Sub-concepts: `addEventListener`; `click`, `input`, `submit`, `keydown`, `mouseover` events; event object (`e.target`, `e.type`); `e.preventDefault()`; `e.stopPropagation()`; event bubbling vs capturing; removing listeners

### 14. Debugging
Sub-concepts: `console.log`, `console.warn`, `console.error`, `console.table`, `console.group`; browser DevTools; breakpoints and stepping through code; reading stack traces; common error types (TypeError, ReferenceError, SyntaxError)

---

## 🟡 INTERMEDIATE (Topics 15–32)

### 15. Scope
Sub-concepts: global scope; function scope; block scope; lexical scope; variable shadowing; the scope chain; why `var` leaks out of blocks

### 16. Hoisting
Sub-concepts: how `var` declarations are hoisted (but not initialised); `let`/`const` in the temporal dead zone (TDZ); function declaration hoisting vs function expression hoisting; hoisting gotchas

### 17. The `this` Keyword
Sub-concepts: `this` in global context; `this` in object methods; `this` in event handlers; `call()`, `apply()`, `bind()`; losing `this`; `this` in arrow functions vs regular functions

### 18. Arrow Functions
Sub-concepts: syntax (single param, single expression, block body); implicit return; no own `this`; no `arguments` object; can't be used as constructors; when to use vs regular functions

### 19. Array Methods (Higher-Order)
Sub-concepts: `map` (transform each element); `filter` (return subset); `reduce` (accumulate to single value); `find` / `findIndex`; `forEach` (side effects); `some` / `every`; `flat` / `flatMap`; chaining methods

### 20. Destructuring
Sub-concepts: array destructuring (position-based); object destructuring (key-based); default values in destructuring; renaming variables; nested destructuring; destructuring in function parameters; swapping variables

### 21. Spread & Rest
Sub-concepts: spread `...` to copy arrays; spread to merge arrays; spread to copy/merge objects; spread in function calls; rest parameters (`...args`) in function definitions; rest vs arguments object

### 22. Short-Circuit & Nullish Operators
Sub-concepts: `&&` for conditional execution; `||` for default values; nullish coalescing `??` (only `null`/`undefined`, not falsy); optional chaining `?.` for safe property access; combining `?.` with `??`

### 23. ES6 Modules
Sub-concepts: named exports; default exports; `import` syntax; mixing named and default imports; module scope (not global); `<script type="module">`; dynamic `import()`; circular dependencies

### 24. Classes
Sub-concepts: `class` declaration syntax; `constructor` method; instance methods; static methods and properties; `extends` for inheritance; `super()` in constructor; `super.method()`; getters and setters; private fields (`#`)

### 25. Prototypes & Prototype Chain
Sub-concepts: every object has a prototype; `Object.getPrototypeOf()`; `__proto__`; how method lookup travels the chain; `hasOwnProperty`; `Object.create()`; prototype vs class syntax; `instanceof`

### 26. Closures
Sub-concepts: inner functions accessing outer scope; closures retaining reference (not value); practical uses (data privacy, factory functions, partial application); closure pitfalls (`var` in loops); IIFE as closure

### 27. Higher-Order Functions & Callbacks
Sub-concepts: passing functions as arguments; returning functions from functions; callback patterns; synchronous callbacks; callback hell intro; why callbacks came before Promises

### 28. Error Handling
Sub-concepts: `try/catch/finally`; the `Error` object (`message`, `name`, `stack`); `TypeError`, `RangeError`, `ReferenceError`; creating custom error classes; throwing errors; re-throwing; handling errors from async code

### 29. JSON
Sub-concepts: what JSON is; `JSON.stringify()` (object → string); `JSON.parse()` (string → object); handling nested data; `null` values in JSON; replacer and reviver functions; JSON vs JS object literals

### 30. Web Storage
Sub-concepts: `localStorage` vs `sessionStorage`; `setItem`, `getItem`, `removeItem`, `clear`; storage limits; storing objects (must JSON-serialise); reading on page load; storage events

### 31. Fetch API & REST
Sub-concepts: `fetch(url)`; Promises returned by fetch; `.json()` to parse response; HTTP methods (GET, POST, PUT, DELETE); request options (`method`, `headers`, `body`); handling 4xx/5xx errors; CORS basics

### 32. Promises
Sub-concepts: creating with `new Promise(resolve, reject)`; `.then()` chaining; `.catch()` for errors; `.finally()`; `Promise.all()` (all or nothing); `Promise.race()`; `Promise.allSettled()`; `Promise.any()`; returning Promises from functions

---

## 🔴 ADVANCED (Topics 33–48)

### 33. Async / Await
Sub-concepts: `async` function always returns a Promise; `await` pauses execution inside async function; `try/catch` for async errors; `await Promise.all([...])` for parallel tasks; sequential vs parallel execution; top-level `await`

### 34. Event Loop
Sub-concepts: call stack; heap; web APIs; callback (task) queue; microtask queue; why Promises run before `setTimeout`; `queueMicrotask()`; understanding non-blocking JS; starvation of the task queue

### 35. Generators & Iterators
Sub-concepts: the iterator protocol (`next()`, `{ value, done }`); `Symbol.iterator`; making objects iterable; generator functions (`function*`); `yield`; lazy evaluation; infinite sequences; `yield*` delegating to another generator

### 36. Symbols
Sub-concepts: `Symbol()` creates unique value; using symbols as object keys; symbols not in `for...in` or `Object.keys()`; `Symbol.for()` global registry; well-known symbols (`Symbol.iterator`, `Symbol.toPrimitive`, `Symbol.hasInstance`)

### 37. Map & Set
Sub-concepts: `Map` (any type as key, ordered, iterable) vs plain objects; `Map` methods (`set`, `get`, `has`, `delete`, `size`); iterating Maps; `Set` for unique values; `Set` methods; converting between Map/Set and arrays; `WeakMap` and `WeakSet` (non-iterable, no strong reference)

### 38. Proxy & Reflect
Sub-concepts: `new Proxy(target, handler)`; traps: `get`, `set`, `has`, `deleteProperty`, `apply`; `Reflect` as companion API; use cases: validation, logging, reactive/observable data; revocable proxies

### 39. Functional Programming
Sub-concepts: pure functions (no side effects, same input = same output); immutability; avoiding mutation with spread/map/filter; function composition; `pipe` and `compose` patterns; first-class functions; referential transparency

### 40. Currying & Partial Application
Sub-concepts: currying (transforming `f(a,b)` → `f(a)(b)`); implementing a `curry()` helper; partial application (pre-filling arguments with `bind`); practical uses (reusable utility builders); difference between currying and partial application

### 41. Memoization
Sub-concepts: caching return values of pure functions; implementing a `memoize()` wrapper; using a `Map` as cache; trade-offs (memory vs speed); when memoization helps (expensive pure computations); memoization in React (`useMemo`, `useCallback` conceptually)

### 42. Design Patterns
Sub-concepts: Module pattern (IIFE encapsulation); Factory pattern (object creation functions); Singleton (ensuring one instance); Observer / Pub-Sub (event-driven communication); Strategy pattern (swappable algorithms); when to use each

### 43. Memory Management
Sub-concepts: how the garbage collector works; reference counting; mark-and-sweep; common memory leaks (detached DOM nodes, forgotten `setInterval`, closures holding large data); `WeakRef` and `FinalizationRegistry`; profiling memory in DevTools

### 44. Timers & Scheduling
Sub-concepts: `setTimeout` / `clearTimeout`; `setInterval` / `clearInterval`; minimum delay quirks; `requestAnimationFrame` for smooth animations; debouncing (delay execution until calm); throttling (limit execution rate); implementing debounce/throttle from scratch

### 45. Regular Expressions
Sub-concepts: regex literal syntax (`/pattern/flags`); flags (`g`, `i`, `m`, `s`); character classes (`\d`, `\w`, `\s`, `.`); quantifiers (`*`, `+`, `?`, `{n,m}`); anchors (`^`, `$`); groups and capturing (`()`); `test()`, `match()`, `matchAll()`, `replace()`, `split()`; lookaheads (`(?=...)`) and lookbehinds (`(?<=...)`)

### 46. Performance Optimisation
Sub-concepts: avoiding layout thrashing (batch DOM reads/writes); debouncing and throttling events; lazy loading images/modules; code splitting; minimising reflows and repaints; `DocumentFragment` for batch DOM insertions; profiling with DevTools Performance tab; `will-change` CSS hint

### 47. TypeScript Basics
Sub-concepts: static typing and type annotations; primitive types (`string`, `number`, `boolean`); interfaces vs type aliases; `any` vs `unknown` vs `never`; generics (`<T>`); union and intersection types; how TypeScript compiles to JS; type inference

### 48. Tooling & Build Systems
Sub-concepts: npm / yarn basics; `package.json` (scripts, dependencies, devDependencies); semantic versioning; module bundlers (Webpack, Vite — what they do); transpilation with Babel; linting with ESLint; environment variables (`.env`); tree shaking; source maps
