set allow-duplicate-variables := true
set allow-duplicate-recipes := true
set shell := ["bash", "-euo", "pipefail", "-c"]


# ---------------------------------------------------------------------------- #
#                                 DEPENDENCIES                                 #
# ---------------------------------------------------------------------------- #

# Ni: https://github.com/antfu-collective/ni
nlx := require("nlx")

# Rsync
rsync := require("rsync")

# ---------------------------------------------------------------------------- #
#                                    RECIPES                                   #
# ---------------------------------------------------------------------------- #

# Show available commands
default:
    @just --list

# Check Prettier formatting
[group("lint")]
prettier-check:
    nlx prettier --check "**/*.{md,yaml,yml}"
alias pc := prettier-check

# Format using Prettier
[group("lint")]
prettier-write:
    nlx prettier --write "**/*.{md,yaml,yml}"
alias pw := prettier-write

# ---------------------------------------------------------------------------- #
#                                    AGENTS                                    #
# ---------------------------------------------------------------------------- #


# See https://github.com/contains-studio/agents/pull/9
sync-agents-contains-studio:
    #!/usr/bin/env sh
    rm -rf ./agents
    git clone https://github.com/ericdum/agents agents-repo
    cd ./agents-repo
    rm -rf .git .gitignore README.md
    cd ..
    rsync --archive --recursive ./agents-repo/ ./agents/
    rm -rf ./agents-repo

sync-agents-lst97:
    #!/usr/bin/env sh
    rm -rf ./agents
    git clone https://github.com/lst97/claude-code-sub-agents agents-repo
    rsync --archive --recursive ./agents-repo/agents/ ./agents/
    rm -rf ./agents-repo

sync-agents-wshobson:
    #!/usr/bin/env sh
    rm -rf ./agents
    git clone https://github.com/wshobson/agents agents-repo
    cd agents-repo
    rm -rf .git .github .gitignore LICENSE README.md
    cd ..
    rsync --archive --recursive ./agents-repo/ ./agents/
    rm -rf ./agents-repo

    # Agents I don't need
    cd ./agents
    rm elixir-pro.md
    rm flutter-expert.md
    rm java-pro.md
    rm minecraft-bukkit-pro.md
    rm php-pro.md
    rm ruby-pro.md
    rm scala-pro.md
    rm unity-developer.md
