# change-to-your-name

Change to your description.

## Quick Start

1. Click **Use this template** to create a new repository
2. Clone your new repository
3. Search and replace `change-to-your-name` / `change_to_your_name` with your project name
4. Install dependencies:

```bash
pixi install
```

5. Install Git hooks:

```bash
pixi run pre-commit install
```

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
