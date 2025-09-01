# Bump Release

1. Update the `CHANGELOG.md` file with all changes since the last version release.
2. Bump the version in `package.json`
3. Commit the changes with a message like "docs: release <version>"
4. Create a new git tag by running `git tag -a v<version> -m "<version>"`

## Tasks

## Process

1. **Review git history** - Examine commits since the last tagged release
2. **Follow format** - Use [Common Changelog](https://common-changelog.org/) specification
3. **Check version** - Get current version from `package.json`
4. **Bump version** - If unchanged since last release, increment per [Semantic Versioning](https://semver.org/) rules:
   - **PATCH** (x.x.X) - Bug fixes, documentation updates
   - **MINOR** (x.X.x) - New features, backward-compatible changes
   - **MAJOR** (X.x.x) - Breaking changes

## Output

In the `CHANGELOG.md` file, generate changelog entries categorizing changes in this order:

- **Changed** - Changes in existing functionality
- **Added** - New functionality
- **Removed** - Removed functionality
- **Fixed** - Bug fixes

## Inclusion Criteria

- **Production changes only** - Exclude test changes, CI/CD workflows, and development tooling
- **Reference pull requests** - Link to PRs when available for context
- **Net changes only** - Skip commits that revert changes made after the last release
- **Only dependencies and peerDependencies changes** - Exclude changes to devDependencies
