set allow-duplicate-variables := true
set allow-duplicate-recipes := true
set shell := ["bash", "-euo", "pipefail", "-c"]

# ---------------------------------------------------------------------------- #
#                                 DEPENDENCIES                                 #
# ---------------------------------------------------------------------------- #

# Claude Code
claude := require("claude")

# Ni: https://github.com/antfu-collective/ni
nlx := require("nlx")

# Rsync
rsync := require("rsync")

# ---------------------------------------------------------------------------- #
#                                   CONSTANTS                                  #
# ---------------------------------------------------------------------------- #

CLAUDE_DIR := "$HOME/.claude"

# ---------------------------------------------------------------------------- #
#                                    SCRIPTS                                   #
# ---------------------------------------------------------------------------- #

# Show available commands
default:
    @just --list

# Check Prettier formatting
[group("lint")]
prettier-check:
    nlx prettier --check "**/*.{json,jsonc,md,yaml,yml}"
alias pc := prettier-check

# Format using Prettier
[group("lint")]
prettier-write:
    nlx prettier --write "**/*.{json,jsonc,md,yaml,yml}"
alias pw := prettier-write
