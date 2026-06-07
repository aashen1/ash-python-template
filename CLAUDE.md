# CLAUDE.md — AI Agent Guide for This Template

> **This file is for AI agents (Claude, Cursor, etc.) working on a project created from `ash-python-template`.**
> After running `scripts/init.sh`, this file should be updated to reflect the actual project. If the project is no longer a template, replace or remove this file entirely.

## Template Initialization (FIRST STEP)

This project was generated from `ash-python-template`. Before doing any other work, you **must** initialize the template by replacing all placeholder names.

### How to Initialize

Run the provided script from the project root:

```bash
bash scripts/init.sh <project-name> [description] [github-owner/repo]
```

**Example:**

```bash
bash scripts/init.sh my-awesome-app "My awesome application" myorg/my-awesome-app
```

### What the Script Does

1. Renames `src/change_to_your_name/` → `src/<your_package>/`
2. Replaces all placeholder strings in source files, configs, and docs:
   - `change-to-your-name` (kebab-case) → your project name
   - `change_to_your_name` (snake_case) → your package name
   - `Change-to-your-name` (PascalCase) → your project title
3. Optionally updates description and GitHub owner/repo

### What to Do After init.sh

1. Review changes: `git diff`
2. Install dependencies: `pixi install`
3. Install Git hooks: `pixi run pre-commit install`
4. Run tests: `pixi run test`
5. **Update or replace this CLAUDE.md** to reflect the actual project context

## Project Configuration Architecture

This project uses **two separate configuration files** with distinct responsibilities:

| File | Purpose | What goes here |
|------|---------|---------------|
| `pixi.toml` | **Dependency management & task runner** | Python version, pypi-dependencies, conda dependencies, pixi tasks, environments (dev/prod) |
| `pyproject.toml` | **Tool configuration & package metadata** | Build system, project metadata (name, version, description), ruff/mypy/pytest/coverage settings |

### Key Rules

- **Adding a dependency**: Use `pixi add --feature <feature-name> --pypi <package>` or `pixi add --feature <feature-name> <package>` (for pypi or conda respectively). Always specify `--feature` to target the correct environment (e.g. `prod`, `dev`), since this template uses multi-environment config. Do NOT use `pip install`.
- **Conda vs PyPI**: Either channel is fine per-package, but pixi resolves conda dependencies **before** PyPI ones. A conda package must **never** depend on a PyPI package — if a conda dep needs something only available on PyPI, add that dep via conda too, or move both to PyPI.
- **Runtime dependencies must be declared in BOTH files**: `pixi.toml` `[feature.prod.pypi-dependencies]` and `pyproject.toml` `[project.dependencies]`. Pixi does not auto-read `pyproject.toml` dependencies.
- **Tool config changes** (ruff rules, mypy settings, pytest options): Edit `pyproject.toml` only.
- **Task changes** (new pixi tasks, environment definitions): Edit `pixi.toml` only.
- **Version pinning**: Let pixi handle version resolution. Avoid hardcoding versions in `pixi.toml` unless needed for compatibility.

## Common Commands

```bash
pixi run lint        # Ruff linter
pixi run format      # Ruff formatter
pixi run typecheck   # MyPy strict mode
pixi run test        # Pytest with coverage
pixi run security    # pip-audit vulnerability check
pixi run docs        # MkDocs dev server
```

## Environment Variables

See `.env.example` for required environment variables. Never read or commit `.env`.
