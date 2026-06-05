# change-to-your-name

Change to your description.

> **Template positioning**: This template is designed for production-grade web services/applications (5000+ lines). It ships with pydantic-settings, structlog, Docker, MkDocs, and ADR out of the box. If you need a library or CLI template, you may want to remove some dependencies.

## Quick Start

1. Click **Use this template** to create a new repository
2. Clone your new repository
3. Replace all project name placeholders (see checklist below)
4. Install dependencies:

```bash
pixi install
```

5. Install Git hooks:

```bash
pixi run pre-commit install
```

### Replacement Checklist

After creating your repo from this template, search and replace the following:

| # | File | What to replace | Old value | New value |
|---|------|----------------|-----------|-----------|
| 1 | `pyproject.toml` | `name`, `description`, `authors` | `change-to-your-name` | your project name |
| 2 | `pixi.toml` | `name`, `authors`, `version` | `change-to-your-name` | your project name |
| 3 | `src/change_to_your_name/` | **Rename directory** | `change_to_your_name` | your package name |
| 4 | `.env.example` | `APP_NAME` | `change-to-your-name` | your project name |
| 5 | `SECURITY.md` | `<owner>/<repo>` | `<owner>/<repo>` | your GitHub owner/repo |
| 6 | `CONTRIBUTING.md` | `<your-username>` | `<your-username>` | your GitHub username |
| 7 | `Dockerfile` | `CMD` module path | `change_to_your_name` | your package name |
| 8 | `src/.../__init__.py` | docstring | `Change-to-your-name` | your project name |
| 9 | `src/.../__main__.py` | `app=` value | `change-to-your-name` | your project name |
| 10 | `src/.../config.py` | `app_name` default | `change-to-your-name` | your project name |
| 11 | `pyproject.toml` | `known-first-party` | `change_to_your_name` | your package name |
| 12 | `pyproject.toml` | coverage `source` | `src/change_to_your_name` | `src/your_package` |
| 13 | `pixi.toml` | pypi-dependencies key | `change-to-your-name` | your project name |
| 14 | `mkdocs.yml` | `site_name` | `change-to-your-name` | your project name |
| 15 | `docs/index.md` | title | `change-to-your-name` | your project name |
| 16 | `docs/api.md` | mkdocstrings reference | `change_to_your_name` | your package name |

> **Tip**: You can also run `bash scripts/init.sh <your-project-name>` to automate all replacements.

## Available Tasks

| Task | Command | Description |
|------|---------|-------------|
| Lint | `pixi run lint` | Run ruff linter |
| Format | `pixi run format` | Run ruff formatter |
| Typecheck | `pixi run typecheck` | Run mypy type checker |
| Test | `pixi run test` | Run pytest with coverage |
| Security | `pixi run security` | Run pip-audit vulnerability check |
| Docs | `pixi run docs` | Start MkDocs dev server |
| Docs Build | `pixi run docs-build` | Build documentation site |

## Project Structure

```
src/change_to_your_name/   # Source code
tests/                      # Test suite
docs/                       # Documentation
```

## License

MIT
