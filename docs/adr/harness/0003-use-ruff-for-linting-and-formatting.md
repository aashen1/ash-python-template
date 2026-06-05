# ADR-0003: Use Ruff for Linting and Formatting

- **Status**: accepted
- **Date**: 2026-06-05

## Context and Problem Statement

We need a fast, opinionated linter and formatter that can replace Black,
isort, flake8, and pyupgrade in a single tool, while integrating with
pre-commit.

## Considered Options

1. Black + isort + flake8 (or ruff for linting) — multiple tools.
2. Ruff only — single Rust-based tool that covers all of the above.

## Decision Outcome

Chosen option: **2 — Ruff**.

Ruff is dramatically faster than the alternatives, has a familiar
configuration surface (we reuse `[tool.ruff]`), and is widely adopted in
the Python ecosystem. It also ships Pylint-style complexity and size
rules (C90, PL) out of the box.

### Positive Consequences

- Linting runs in milliseconds, even on large codebases.
- One configuration file (`pyproject.toml`) governs formatting, linting,
  and import sorting.
- A single `pre-commit` hook handles both `check --fix` and `format`.

### Negative Consequences

- Some niche rules behave slightly differently from Pylint.
- We need to keep the rule set under review as Ruff evolves.

## References

- Ruff documentation: <https://docs.astral.sh/ruff>
