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
    nlx prettier --check "**/*.{md,yaml,yml}"
alias pc := prettier-check

# Format using Prettier
[group("lint")]
prettier-write:
    nlx prettier --write "**/*.{md,yaml,yml}"
alias pw := prettier-write

# ---------------------------------------------------------------------------- #
#                                  FRAMEWORKS                                  #
# ---------------------------------------------------------------------------- #

# Disable existing frameworks
[confirm("Are you sure? This will disable all frameworks (y/N)")]
disable-frameworks:
    #!/usr/bin/env sh
    set -euo pipefail

    frameworks=(
        "cy" # https://github.com/wcygan/dotfiles
        "ho" # https://github.com/wshobson/commands
        "sc" # https://github.com/SuperClaude-Org/SuperClaude_Framework
    )

    # Delete existing FRAMEWORK.md file
    if [ -f ./FRAMEWORK.md ]; then
        rm ./FRAMEWORK.md
        touch ./FRAMEWORK.md
    else
        touch ./FRAMEWORK.md
    fi

    # Delete existing commands
    for framework in "${frameworks[@]}"; do
        rm -f ./commands/${framework}
    done

    # Delete existing agents
    if [ -d ./agents ]; then
        rm -f ./agents
    fi

    echo "✅ All frameworks disabled successfully"


# Use a framework for Claude Code
[confirm("Are you sure? This will update the agents and commands directories (y/N)")]
use-framework framework:
    #!/usr/bin/env sh
    set -euo pipefail

    frameworks=(
        "cy" # https://github.com/wcygan/dotfiles
        "ho" # https://github.com/wshobson/commands
        "sc" # https://github.com/SuperClaude-Org/SuperClaude_Framework
    )

    if ! [[ "${frameworks[@]}" =~ {{ framework }} ]]; then
        echo "Error: Unknown framework {{ framework }}"
        exit 1
    fi

    # Disable existing frameworks
    just --yes disable-frameworks 1>/dev/null

    # Reference CLAUDE.md file or create an empty one
    framework_dir=./frameworks/{{ framework }}
    if [ -f $framework_dir/CLAUDE.md ]; then
        source=$framework_dir/CLAUDE.md
        target=./FRAMEWORK.md
        if [ -f $target ]; then
            rm $target
        fi
        ln -s $source $target
        echo "FRAMEWORK.md symlinked"
    fi

    # Symlink agents
    if [ -d $framework_dir/agents ]; then
        source={{ CLAUDE_DIR }}/$framework_dir/agents
        target={{ CLAUDE_DIR }}/agents
        ln -s $source $target
        echo "Agents symlinked"
    fi

    # Symlink commands
    if [ -d $framework_dir/commands ]; then
        source={{ CLAUDE_DIR }}/$framework_dir/commands
        target={{ CLAUDE_DIR }}/commands/{{ framework }}
        ln -s $source $target
        echo "Commands with /{{ framework }} prefix symlinked"
    fi

    echo "✅ Framework {{ framework }} installed successfully"
