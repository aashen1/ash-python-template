#!/usr/bin/env bash
# =============================================================================
# Template initialization script
# =============================================================================
# Usage: bash scripts/init.sh <project-name> [description] [github-owner/repo]
#
# Example:
#   bash scripts/init.sh my-awesome-app "My awesome application" myorg/my-awesome-app
#
# This script replaces all placeholder names in the template with your project
# name and optionally updates the description and GitHub owner/repo.
# =============================================================================
set -euo pipefail

# ── Arguments ────────────────────────────────────────────────────────────────
if [[ $# -lt 1 ]]; then
  echo "Usage: bash scripts/init.sh <project-name> [description] [github-owner/repo]"
  echo "  project-name      kebab-case name (e.g. my-awesome-app)"
  echo "  description       optional project description"
  echo "  github-owner/repo optional GitHub owner/repo (e.g. myorg/my-awesome-app)"
  exit 1
fi

PROJECT_KEBAB="$1"
DESCRIPTION="${2:-}"
GITHUB_REPO="${3:-}"

# Derive snake_case from kebab-case
PROJECT_SNAKE="${PROJECT_KEBAB//-/_}"

# Derive PascalCase (for docstrings)
PROJECT_PASCAL="$(echo "$PROJECT_KEBAB" | sed -E 's/(^|-)([a-z])/\U\2/g')"

OLD_KEBAB="change-to-your-name"
OLD_SNAKE="change_to_your_name"
OLD_PASCAL="Change-to-your-name"

echo "=== Initializing template ==="
echo "  kebab-case : $OLD_KEBAB -> $PROJECT_KEBAB"
echo "  snake_case : $OLD_SNAKE -> $PROJECT_SNAKE"
echo "  PascalCase : $OLD_PASCAL -> $PROJECT_PASCAL"
if [[ -n "$DESCRIPTION" ]]; then
  echo "  description: $DESCRIPTION"
fi
if [[ -n "$GITHUB_REPO" ]]; then
  echo "  GitHub repo: $GITHUB_REPO"
fi
echo ""

# ── Safety check ─────────────────────────────────────────────────────────────
if [[ "$PROJECT_KEBAB" == "$OLD_KEBAB" ]]; then
  echo "Error: project name must differ from the template placeholder."
  exit 1
fi

# ── Rename source directory ──────────────────────────────────────────────────
if [[ -d "src/$OLD_SNAKE" ]]; then
  mv "src/$OLD_SNAKE" "src/$PROJECT_SNAKE"
  echo "Renamed src/$OLD_SNAKE -> src/$PROJECT_SNAKE"
fi

# ── Replace in files ─────────────────────────────────────────────────────────
# Order matters: replace longer strings first to avoid partial matches
FILES=(
  CLAUDE.md
  pyproject.toml
  pixi.toml
  mkdocs.yml
  .env.example
  Dockerfile
  SECURITY.md
  CONTRIBUTING.md
  README.md
  docs/index.md
  docs/api.md
  src/$PROJECT_SNAKE/__init__.py
  src/$PROJECT_SNAKE/__main__.py
  src/$PROJECT_SNAKE/config.py
  src/$PROJECT_SNAKE/core/__init__.py
  src/$PROJECT_SNAKE/core/logging.py
  tests/conftest.py
  tests/test_config.py
  tests/test_example.py
  tests/test_logging.py
  tests/test_main.py
)

for f in "${FILES[@]}"; do
  if [[ -f "$f" ]]; then
    sed -i "s/$OLD_KEBAB/$PROJECT_KEBAB/g" "$f"
    sed -i "s/$OLD_SNAKE/$PROJECT_SNAKE/g" "$f"
    sed -i "s/$OLD_PASCAL/$PROJECT_PASCAL/g" "$f"
    echo "Updated: $f"
  fi
done

# ── Replace description ──────────────────────────────────────────────────────
if [[ -n "$DESCRIPTION" ]]; then
  # pyproject.toml
  if [[ -f pyproject.toml ]]; then
    sed -i "s|^description = .*|description = \"$DESCRIPTION\"|" pyproject.toml
    echo "Updated description in pyproject.toml"
  fi
  # README.md
  if [[ -f README.md ]]; then
    sed -i "1s|^# .*|# $PROJECT_KEBAB|" README.md
    sed -i "2s|^.*|$DESCRIPTION|" README.md
    echo "Updated title and description in README.md"
  fi
fi

# ── Replace GitHub owner/repo ────────────────────────────────────────────────
if [[ -n "$GITHUB_REPO" ]]; then
  if [[ -f SECURITY.md ]]; then
    sed -i "s|<owner>/<repo>|$GITHUB_REPO|g" SECURITY.md
    echo "Updated GitHub repo in SECURITY.md"
  fi
  # CONTRIBUTING.md: replace <your-username>
  GITHUB_OWNER="${GITHUB_REPO%%/*}"
  if [[ -f CONTRIBUTING.md ]]; then
    sed -i "s|<your-username>|$GITHUB_OWNER|g" CONTRIBUTING.md
    echo "Updated GitHub username in CONTRIBUTING.md"
  fi
  # .github/ISSUE_TEMPLATE/config.yml: replace <owner>.github.io/<repo>
  if [[ -f .github/ISSUE_TEMPLATE/config.yml ]]; then
    GITHUB_REPO_NAME="${GITHUB_REPO#*/}"
    sed -i "s|<owner>\.github\.io/<repo>|$GITHUB_OWNER.github.io/$GITHUB_REPO_NAME|g" .github/ISSUE_TEMPLATE/config.yml
    echo "Updated GitHub Pages URL in .github/ISSUE_TEMPLATE/config.yml"
  fi
fi

echo ""
echo "=== Done! ==="
echo "Installing Git hooks..."
pixi run pre-commit install
pixi run pre-commit install --hook-type post-merge
echo ""
echo "Next steps:"
echo "  1. Review the changes: git diff"
echo "  2. Run tests:            pixi run test"
