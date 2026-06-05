# Architecture Decision Records

This directory contains the Architecture Decision Records (ADRs) for
the project. ADRs capture the _why_ behind the technical choices we
have made. See [0001](harness/0001-record-architecture-decisions.md) for an
overview of the ADR process itself.

## Index

| Number | Title | Status |
| ------ | ----- | ------ |
| [0001](harness/0001-record-architecture-decisions.md) | Record Architecture Decisions | accepted |
| [0002](harness/0002-use-pixi-for-dependency-management.md) | Use Pixi for Dependency and Environment Management | accepted |
| [0003](harness/0003-use-ruff-for-linting-and-formatting.md) | Use Ruff for Linting and Formatting | accepted |
| [0004](harness/0004-use-pydantic-settings-for-configuration.md) | Use pydantic-settings for Configuration Management | accepted |
| [0005](harness/0005-use-structlog-for-observability.md) | Use structlog for Structured Logging | accepted |
| [0006](harness/0006-adopt-conventional-commits.md) | Adopt Conventional Commits and Automated Versioning | accepted |

## Adding a New ADR

1. Copy [`template.md`](template.md) to a new file named
   `NNNN-short-slug.md` where `NNNN` is the next available number.
2. Fill in the context, considered options, and decision outcome.
3. Open a pull request so the team can review the decision.
4. Once accepted, append a row to the index above.
