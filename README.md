# Claude Code config

PRB's `.claude` directory.

## Context

Modular configuration system for Claude Code with structured context inheritance:

```
context/
├── BASE.md                 # Core behavioral instructions
├── CRITICAL_THINKING.md    # Analytical approach guidelines
├── DELEGATION.md           # Task orchestration patterns
├── REPORTS.md              # Output formatting standards
├── SENIOR_PROGRAMMER.md    # Expert-level coding approach
├── languages/
│   ├── SHELL.md            # Shell and CLI tool preferences
│   ├── TYPESCRIPT.md       # TypeScript conventions
│   └── TYPESCRIPT_REACT.md # React-specific patterns
├── mcp/                    # MCP server integration guides
│   ├── MCP_Context7.md     # Documentation lookup patterns
│   ├── MCP_Magic.md        # UI component generation
│   ├── MCP_Serena.md       # Semantic code operations
│   └── ...                 # Additional MCP configs
└── tools/
    ├── JUST.md             # Command runner preferences
    └── NODE.md             # Node.js ecosystem setup
```

Each context module is composable via `@` references, creating layered behavioral instructions.

## Commands

Streamlined command system focused on semantic analysis and programmatic workflows:

```
commands/
├── bump-release.md    # Automated version management and releases
├── commit.md          # Semantic commit generation with --short flag
├── create-command.md  # Command scaffolding utilities
├── create-issue.md    # GitHub issue creation with auto-labeling
├── create-pr.md       # Semantic PR generation with smart defaults
├── create-worktrees.md # Git worktree workflow automation
└── docs.md           # Documentation generation helpers
```

**Key Features**:
- **commit**: Analyzes staged changes semantically, generates conventional commit messages. Supports `--short` for single-line commits and natural argument parsing (`/commit fix auth bug`)
- **create-pr**: Reads actual code changes to understand purpose, auto-detects issues/reviewers, updates existing PRs instead of creating duplicates

## Architecture

Commands are designed for autonomous execution with minimal user intervention:

- **Semantic analysis**: Commands read actual code changes to understand intent, not just filenames
- **Natural argument parsing**: Flexible interpretation of flags and parameters (e.g., `/commit fix auth --short`)
- **Smart defaults**: Auto-detect reviewers from CODEOWNERS, stage changes automatically, update existing PRs
- **Programmatic workflows**: Stateless execution without complex session tracking or interactive prompts
- **Conventional commits**: Automatic type/scope detection following [conventionalcommits.org](https://conventionalcommits.org)

### MCP Servers

- [ContainerUse](https://container-use.com): Sandboxed development environment
- [Context7](https://github.com/oraios/context7): Curated documentation lookup and pattern guidance
- [Serena](https://github.com/oraios/serena): Semantic code understanding with project memory and session persistence
- [Magic](https://github.com/oraios/magic): Modern UI generation from [21st.dev](https://21st.dev) patterns
- [Morphllm](https://github.com/oraios/morphllm): Optimized pattern-based code editing engine transformations
- [Playwright](https://github.com/oraios/playwright): Real browser automation and testing
- [Sequential](https://github.com/oraios/sequential): Structured multi-step reasoning and hypothesis testing

### Nice to Have

Some nice-to-have utilities:

- **[ccnotify](https://github.com/dazuiba/CCNotify)**: Custom notifications for Claude Code
- **[ccstatusline](https://github.com/sirmalloc/ccstatusline)**: Custom status line for Claude Code
- **[claude-code-docs](https://github.com/ericbuess/claude-code-docs)**: Local mirror of Claude Code documentation from
  Anthropic

## License

This project is licensed under MIT.
