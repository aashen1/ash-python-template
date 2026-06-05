# ADR-0004: Use pydantic-settings for Configuration Management

- **Status**: accepted
- **Date**: 2026-06-05

## Context and Problem Statement

The application needs typed, validated configuration loaded from
environment variables and `.env` files. Hard-coding values, reading
`os.environ` directly, or scattering `getenv` calls across the codebase
makes it impossible to validate types, document defaults, or test
configuration in isolation.

## Considered Options

1. `os.environ` access scattered through modules.
2. A custom settings module that reads environment variables manually.
3. `pydantic-settings` (a pydantic extension) with a typed `Settings`
   class and `get_settings()` cached singleton.

## Decision Outcome

Chosen option: **3 — `pydantic-settings`**.

Pydantic provides automatic type validation, default values, and IDE
auto-completion. `pydantic-settings` adds `.env` file support, layered
priority (process env > `.env` > defaults), and integrates seamlessly
with FastAPI, Typer, and other frameworks.

### Positive Consequences

- All configuration is documented in a single class with type hints.
- Misconfiguration is caught at startup rather than at the point of use.
- `get_settings()` is cached, so tests can override values via
  `monkeypatch.setenv` and re-call the function.

### Negative Consequences

- Adds a runtime dependency on pydantic.
- Settings classes can become large; we mitigate this with `model_config`
  defaults and split classes if needed.

## References

- pydantic-settings documentation: <https://docs.pydantic.dev/latest/concepts/pydantic_settings/>
