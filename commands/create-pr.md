---
description: Create a GitHub pull request with intelligent analysis and programmatic workflow
---

## Context

- Session ID: !`gdate +%s%N`
- Current branch: !`git branch --show-current || echo "unknown"`
- Git status: !`git status --porcelain | wc -l | tr -d ' ' || echo "0"` uncommitted changes
- Remote status: !`git status -b --porcelain | head -1 || echo "No remote tracking"`
- Recent commits: !`git log --oneline -5 || echo "No commits found"`
- GitHub CLI auth: !`gh auth status | rg -q "Logged in" && echo "authenticated" || echo "not authenticated"`
- Existing PR: !`gh pr list --head $(git branch --show-current || echo "main") --json number,state | jq -r '.[0].number // "none"' || echo "none"`
- Arguments: $ARGUMENTS

## Your Task

### STEP 1: Initialize PR creation session and validate prerequisites

- CREATE session state: `/tmp/pr-create-$SESSION_ID.json`
- VALIDATE session ID generation and file permissions
- SET initial state:
  ```json
  {
    "sessionId": "$SESSION_ID",
    "timestamp": "$(gdate -Iseconds || date -Iseconds)",
    "branch": "$(git branch --show-current)",
    "arguments": "$ARGUMENTS",
    "phase": "validation",
    "pr_config": {},
    "validation_results": {}
  }
  ```

TRY:

- VALIDATE GitHub authentication from Context
- VALIDATE git repository presence
- VALIDATE branch state and remote tracking
- SAVE validation results to session state

**Validation Logic:**

IF GitHub auth != "authenticated":

- ERROR: "GitHub authentication required. Please run `gh auth login`."
- EXIT with error code

IF git repository not detected:

- ERROR: "Not in a git repository. Navigate to project root or run `git init`."
- EXIT with error code

IF uncommitted changes > 0:

- ERROR: "Uncommitted changes detected. Commit or stash changes before creating PR."
- EXIT with error code

CATCH (validation_failed):

- LOG specific validation failure to session state
- PROVIDE specific remediation instructions
- SAVE partial session state for recovery
- EXIT with helpful error message

### STEP 2: Parse arguments and configure PR parameters

- PARSE $ARGUMENTS for PR configuration options
- SET default values for missing parameters
- VALIDATE parameter combinations
- UPDATE session state with PR configuration

**Argument Processing:**

```bash
# Parse common argument patterns
draft_mode=$(echo "$ARGUMENTS" | rg -q "draft" && echo "true" || echo "false")
base_branch=$(echo "$ARGUMENTS" | rg -oE 'base=([^\s]+)' | cut -d'=' -f2 || echo "main")
reviewers=$(echo "$ARGUMENTS" | rg -oE 'reviewers=([^\s]+)' | cut -d'=' -f2 || echo "")
custom_title=$(echo "$ARGUMENTS" | rg -oE 'title="([^"]+)"' | sed 's/title="//;s/"$//' || echo "")
```

### STEP 3: Intelligent change analysis and PR content generation

Think deeply about the optimal PR content generation strategy based on commit history, file changes, and project conventions.

TRY:

- ANALYZE commit history for conventional commit patterns
- EXAMINE file changes for scope and impact
- GENERATE intelligent PR title and description
- DETECT related issues from branch name or commits
- IDENTIFY appropriate reviewers from CODEOWNERS or git history
- SAVE analysis results to session state

**Change Analysis Execution:**

```bash
# Get base and current branch
base_branch=$(git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@' || echo "main")
current_branch=$(git branch --show-current)

# Analyze commits and changes
commit_messages=$(git log --pretty=format:"%s" origin/$base_branch...HEAD || echo "")
file_changes=$(git diff --name-status origin/$base_branch...HEAD || echo "")
change_summary=$(git diff --stat origin/$base_branch...HEAD || echo "")

# Extract issue numbers from branch or commits
issue_numbers=$(echo "$current_branch\n$commit_messages" | rg -oE '#[0-9]+' | sort -u || echo "")

# Check for existing PR
existing_pr=$(gh pr list --head $current_branch --json number,state | jq -r '.[0].number // "none"' || echo "none")
```

**Title Generation Logic:**

IF custom_title provided:

- USE custom_title as PR title

ELSE IF single commit with conventional format:

- EXTRACT title from commit message
- VALIDATE conventional commit format

ELSE:

- ANALYZE file changes for primary scope
- GENERATE title based on change patterns
- FORMAT: "type(scope): description"

CATCH (analysis_failed):

- LOG analysis failure details
- FALLBACK to generic title generation
- CONTINUE with available information

### STEP 4: Handle existing PR or create new PR

IF existing_pr != "none":

- LOG: "PR #$existing_pr already exists for this branch"
- PROMPT: "Update existing PR or create new one? (update/new/cancel)"
- CASE user_choice:
  - "update": EXECUTE PR update workflow
  - "new": CONTINUE with new PR creation
  - "cancel": EXIT gracefully

ELSE:

- PROCEED with new PR creation

### STEP 5: Execute PR creation with intelligent content

- ENSURE branch is pushed to remote
- GENERATE PR body intelligently; keep it short and concise
- COLLECT all PR parameters (title, body, reviewers, etc.)
- EXECUTE `gh pr create` with generated content
- SAVE PR details to session state

**PR Creation Execution:**

```bash
# Ensure branch is pushed
git push -u origin $(git branch --show-current) || echo "Branch already pushed"

# Build PR creation command
gh pr create \
  --title "$generated_title" \
  --body "$(cat <<'EOF'
## Summary

$generated_summary

## Related Issues

$issue_links
EOF
)" \
  $(test "$draft_mode" = "true" && echo "--draft" || echo "") \
  $(test -n "$reviewers" && echo "--reviewer $reviewers" || echo "") \
  --base "$base_branch"
```

TRY:

- EXECUTE PR creation command with all parameters
- CAPTURE PR URL and number from output
- VALIDATE PR creation success
- UPDATE session state with PR details

CATCH (pr_creation_failed):

- LOG specific failure reason (auth, network, validation, etc.)
- PROVIDE targeted remediation steps
- SAVE session state with failure details
- OFFER retry with corrected parameters

### STEP 6: Post-creation workflow and cleanup

- DISPLAY PR creation success message with URL
- SAVE final session state with completion status
- OPTIONALLY trigger CI/CD workflows if detected
- CLEAN UP temporary session files

## Advanced Features Integration

### Issue Linking:

FOR EACH issue number detected:

- VALIDATE issue exists with `gh issue view`
- ADD appropriate linking keywords ("Closes #123", "Related to #456")
- INCLUDE issue context in PR description

### CI/CD Integration:

IF test files or deployment configs changed:

- ADD CI trigger comments to PR body
- SUGGEST appropriate test commands
- INCLUDE deployment preview requests

FINALLY:

- ARCHIVE session data: `/tmp/pr-create-archive-$SESSION_ID.json`
- REPORT completion status with metrics
- CLEAN UP temporary files (EXCEPT archived data)
- LOG session completion timestamp

## Usage Examples

- `/create-pr` - Create PR with intelligent defaults
- `/create-pr base=staging` - Target different base branch
- `/create-pr draft` - Create draft PR for work in progress
- `/create-pr reviewers=alice,bob` - Add specific reviewers
- `/create-pr title="Custom PR title"` - Override generated title

## Error Recovery

- **Branch not pushed**: Automatically pushes with tracking
- **Existing PR detected**: Offers update or new PR options
- **Network issues**: Provides retry with exponential backoff
- **Validation errors**: Specific remediation for each error type

## State Management

- Session state tracks progress through each step
- Resumable from last successful checkpoint
- Automatic cleanup of stale session files
- Comprehensive error logging for debugging
