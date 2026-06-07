# ADR-0002: Use Pixi for Dependency and Environment Management

- **Status**: accepted
- **Date**: 2026-06-05
- **Updated**: 2026-06-07

## Context and Problem Statement

Python projects need a reproducible, lockable dependency management story
that also doubles as a task runner for linting, testing, and documentation
builds. Existing options include `pip + venv`, Poetry, uv, and Pixi.

Additionally, we need to decide where to declare runtime dependencies:
`pyproject.toml [project.dependencies]`, `pixi.toml`, or both.

## Considered Options

1. `pip` + `requirements.txt` with a separate Makefile or `tox`.
2. Poetry (or uv) for Python-only dependency management.
3. Pixi, a conda-based workspace manager that supports PyPI packages.

### Dependency Declaration Location

1. **Dual-file**: Declare runtime dependencies in both `pyproject.toml` and `pixi.toml`.
   - Pro: wheel metadata is correct; `pip install` works standalone.
   - Con: duplication, easy to get out of sync, confuses AI agents.
2. **pyproject.toml only**: Use `[tool.pixi.*]` in `pyproject.toml` so pixi auto-reads dependencies.
   - Pro: single source of truth.
   - Con: mixes pixi config into Python packaging file; less flexible for multi-environment setups.
3. **pixi.toml only**: Declare all dependencies in `pixi.toml`; `pyproject.toml` has no `[project.dependencies]`.
   - Pro: single source of truth; clean separation of concerns.
   - Con: `pip install *.whl` won't auto-install runtime deps (not a concern for web service deployment).

## Decision Outcome

Chosen option: **3 — Pixi**, with **pixi.toml only** for dependency declaration.

Pixi is already a drop-in task runner (we use `pixi run lint`, `pixi run
test`, etc.), supports PyPI packages for libraries that are not on
conda-forge, and locks transitive dependencies via `pixi.lock`.

Runtime dependencies are declared exclusively in `pixi.toml`
(`[feature.prod.pypi-dependencies]`). The default environment combines
`["dev", "prod"]` features so runtime deps are available during development
without duplication. `pyproject.toml` contains only build system config,
package metadata, and tool settings (ruff, mypy, pytest, coverage).

This is appropriate because this template targets **web service deployment**
where the project is never published to PyPI and all environments are
managed by pixi (local dev) or Docker (production, built via pixi).

### Positive Consequences

- Single tool for env creation, locking, and task running.
- `pixi.lock` is committed, guaranteeing reproducible installs.
- Works with `prefix-dev/setup-pixi` in GitHub Actions.
- Single source of truth for dependencies — no cross-file duplication.
- Clean separation: `pixi.toml` = dependencies & tasks, `pyproject.toml` = tool config.

### Negative Consequences

- The team needs to be familiar with Pixi concepts (`tasks`, `features`,
  channels).
- Some niche PyPI packages may need `--pypi` flags.
- `pip install *.whl` won't auto-install runtime deps (acceptable for
  web service deployment; would need to add `[project.dependencies]` if
  publishing to PyPI).
- If `pixi-build-python`'s automatic PyPI dependency mapping stabilizes
  in the future, we may reconsider using `pyproject.toml` as the single
  source instead.

## References

- Pixi documentation: <https://pixi.sh>
- pixi-build-python automatic mapping: <https://pixi.prefix.dev/latest/build/backends/pixi-build-python/#automatic-pypi-dependency-mapping>
