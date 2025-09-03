### TypeScript

A collection of TypeScript rules.

- These instructions also apply to JavaScript.
- These are not hard-and-fast rules. If you have a good reason not to apply a rule, do so.

#### Alphabetical Order

Maintain alphabetical order for better readability and consistency:

- **Function parameters** - Order by parameter name
- **Object literal fields** - Sort by key name
- **Type definitions** - Arrange fields alphabetically
- **Class properties** - Order by property name

##### Exceptions

###### Nesting depth

Group by nesting depth before alphabetical sorting.

**Example:**

```json
{
  "id": "12345", // depth 0 - comes first alphabetically
  "name": "Sample Item", // depth 0 - comes second alphabetically
  "details": {
    // depth 1 - comes last despite "d" < "i"
    "description": "...",
    "status": "active"
  }
}
```

#### BiomeJS

Use BiomeJS for linting and formatting JavaScript and TypeScript code. Look for a `biome.jsonc` file and, if it's not
present, create it.

Exception: project already uses ESLint and Prettier.

#### Prefer TypeScript over JavaScript

Use TypeScript for all new code.

#### Prefer `type` instead of `interface`

Use `type` instead of `interface` for declaring types.

#### Typechecking

Run `just tsc-check` (if a `justfile` is available) or `nlx tsc --noEmit` to type check the code.
