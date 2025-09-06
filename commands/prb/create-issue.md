---
allowed-tools: Bash(gh:*)
argument-hint: [owner/repo] [description]
description: Create a GitHub issue with automatic labeling using standard label set
---

# Create GitHub Issue with Auto-Labeling

Create a new GitHub issue in the specified repository and automatically apply appropriate labels based on the issue content.

## Arguments

- **$1** - Repository (required) - Format: "owner/repo" e.g., "PaulRBerg/dotfiles", "sablier-labs/lockup"
- **$ARGUMENTS** - Natural language description (required) - Describe the issue in your own words

## Standard Labels

The following labels are used across repositories:

### Effort Labels
- `effort: epic` - Multi-stage task that may require multiple PRs
- `effort: high` - Large or difficult task
- `effort: medium` - Default level of effort
- `effort: low` - Easy or tiny task that takes less than a day

### Priority Labels
- `priority: 0` - Do this first before everything else. Critical and nothing works without this
- `priority: 1` - Important. Should be dealt with shortly
- `priority: 2` - We will do our best to deal with this
- `priority: 3` - Nice-to-have. Willing to ship without this

### Type Labels
- `type: bug` - Something isn't working
- `type: build` - Changes that affect the build system or external dependencies
- `type: chore` - Maintenance work
- `type: ci` - Changes to CI configuration files and scripts
- `type: docs` - Changes to documentation
- `type: feature` - New feature or request
- `type: perf` - Change that improves performance or user experience
- `type: refactor` - Change that neither fixes a bug nor adds a feature
- `type: style` - Changes that do not affect the meaning of the code
- `type: test` - Adding, updating, or removing tests

### Work Labels (Cynefin Framework)
- `work: chaotic` - Act-sense-respond. No clear relationship between cause and effect
- `work: complex` - Probe-sense-respond. The relationship between cause and effect can only be perceived in retrospect
- `work: complicated` - Sense-analyze-respond. The relationship between cause and effect requires analysis or expertise
- `work: clear` - Sense-categorize-respond. The relationship between cause and effect is clear

### Scope Labels (sablier-labs/command-center repository only)
- `scope: backend` - Backend development task
- `scope: business` - Business development task
- `scope: data` - Data engineering task
- `scope: devops` - DevOps task
- `scope: evm` - EVM development task
- `scope: frontend` - Frontend development task
- `scope: integrations` - Integration with a third-party service
- `scope: marketing` - Marketing task
- `scope: other` - Task that doesn't fit in any other scope
- `scope: solana` - Solana development task

### Miscellaneous Labels
- `duplicate` - This issue or pull request already exists
- `good first issue` - Good for newcomers
- `help` - Extra information is needed
- `stale` - Inactive for a long time

## Instructions

1. **Parse the natural language description** to extract:
   - **Issue Title**: Create a clear, concise title (5-10 words) that summarizes the main issue
   - **Issue Body**: If the description is detailed enough, create a structured body with context and details
   - If the description is brief, use it as both title and body

2. **Analyze the parsed content** to determine appropriate labels:

   **Type Label Selection:**
   - Look for keywords like "bug", "error", "broken", "crash" → `type: bug`
   - Look for "add", "new", "implement", "create" → `type: feature`
   - Look for "update", "improve", "optimize", "enhance" → `type: perf`
   - Look for "docs", "documentation", "readme" → `type: docs`
   - Look for "test", "testing", "spec" → `type: test`
   - Look for "refactor", "cleanup", "restructure" → `type: refactor`
   - Look for "build", "dependency", "package" → `type: build`
   - Look for "ci", "workflow", "pipeline" → `type: ci`
   - Look for "maintenance", "chore", "housekeeping" → `type: chore`
   - Look for "style", "formatting", "lint" → `type: style`

   **Work Label Selection:**
   - Clear requirements and known solution → `work: clear`
   - Requires analysis or expertise but solution is findable → `work: complicated`
   - Experimental, research needed, unclear outcome → `work: complex`
   - Crisis mode, immediate response needed → `work: chaotic`

   **Priority Label Selection:**
   - Production down, critical blocker → `priority: 0`
   - Important feature or significant bug → `priority: 1`
   - Standard issue, part of regular work → `priority: 2`
   - Nice to have, low impact → `priority: 3`

   **Effort Label Selection:**
   - Multiple PRs, weeks of work → `effort: epic`
   - Several days of work → `effort: high`
   - Standard task, 1-3 days → `effort: medium`
   - Quick fix, less than a day → `effort: low`

   **Scope Label Selection (only for sablier-labs/command-center repository):**
   - Frontend UI work → `scope: frontend`
   - Backend API work → `scope: backend`
   - Smart contract work → `scope: evm` or `scope: solana`
   - Data pipeline work → `scope: data`
   - CI/CD infrastructure → `scope: devops`
   - Third-party integrations → `scope: integrations`
   - Marketing content → `scope: marketing`
   - Business strategy → `scope: business`
   - Other → `scope: other`

3. **Create the GitHub issue** using the `gh` CLI:
   ```bash
   gh issue create --repo $1 --title "EXTRACTED_TITLE" --body "EXTRACTED_BODY" --label "label1,label2,label3"
   ```

4. **Output summary** showing:
   - Extracted title and body
   - Created issue URL
   - Applied labels and reasoning
   - Repository name

## Usage Examples

```bash
# Bug report with natural language
/prb:create-issue "PaulRBerg/dotfiles" "There's a bug in my zsh configuration that causes startup errors on macOS when using tmux. The error shows up every time I open a new terminal window and it's really annoying."

# Simple feature request
/prb:create-issue "sablier-labs/core" "We need withdrawal batching functionality so users can save on gas fees"

# Feature for command-center (gets scope labels automatically)
/prb:create-issue "sablier-labs/command-center" "The app needs a dark mode toggle for better accessibility and user experience, especially for users working in low-light environments"

# Quick documentation fix
/prb:create-issue "PaulRBerg/my-project" "The README installation steps are outdated and missing the new dependency requirements"

# Performance issue
/prb:create-issue "company/api-service" "The API response times are getting really slow, especially for the user endpoints. It's taking 3-5 seconds which is unacceptable for production"
```

## Task

Based on the provided repository ($1) and natural language description ($ARGUMENTS):

1. Parse the natural language description to extract a clear title and structured body
2. Analyze the parsed content to determine appropriate labels
3. Check if repository is `sablier-labs/command-center` to decide on scope labels
4. Create the GitHub issue in the specified repository with extracted title and body
5. Apply the determined labels automatically
6. Provide a summary showing extracted content, created issue URL, and applied labels
