# TypeScript

These instructions also apply to JavaScript.

## BiomeJS

Use BiomeJS for linting and formatting JavaScript and TypeScript code. Look for a `biome.jsonc` file. If it's not
present, create it.

The only exception to this rule is if the project already uses ESLint and Prettier.

## Prefer `type` instead of `interface`

Unless there is a good reason to do otherwise, use `type` instead of `interface` for declaring types.

## Typechecking

Run `just tsc-check` (if a `justfile` is available) or `nlx tsc --noEmit` to type check the code.
