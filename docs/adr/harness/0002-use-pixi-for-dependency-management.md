# ADR-0002: Use Pixi for Dependency and Environment Management

- **Status**: accepted
- **Date**: 2026-06-05

## Context and Problem Statement

Python projects need a reproducible, lockable dependency management story
that also doubles as a task runner for linting, testing, and documentation
builds. Existing options include `pip + venv`, Poetry, uv, and Pixi.

## Considered Options

1. `pip` + `requirements.txt` with a separate Makefile or `tox`.
2. Poetry (or uv) for Python-only dependency management.
3. Pixi, a conda-based workspace manager that supports PyPI packages.

## Decision Outcome

Chosen option: **3 — Pixi**.

Pixi is already a drop-in task runner (we use `pixi run lint`, `pixi run
test`, etc.), supports PyPI packages for libraries that are not on
conda-forge, and locks transitive dependencies via `pixi.lock`.

### Positive Consequences

- Single tool for env creation, locking, and task running.
- `pixi.lock` is committed, guaranteeing reproducible installs.
- Works with `prefix-dev/setup-pixi` in GitHub Actions.

### Negative Consequences

- The team needs to be familiar with Pixi concepts (`tasks`, `features`,
  channels).
- Some niche PyPI packages may need `--pypi` flags.

## References

- Pixi documentation: <https://pixi.sh>
