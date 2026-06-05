# ADR-0005: Use structlog for Structured Logging

- **Status**: accepted
- **Date**: 2026-06-05

## Context and Problem Statement

We need production-grade observability with structured logs that are
easy to search, filter, and forward to log aggregation tools. The Python
standard `logging` module is sufficient for simple text output but
requires additional plumbing to produce JSON or key/value records.

## Considered Options

1. Stick with the `logging` module and emit free-form strings.
2. Use `loguru` for ergonomic logging.
3. Use `structlog` together with the `logging` module to support both
   structured and conventional output.

## Decision Outcome

Chosen option: **3 — structlog**.

structlog supports JSON output (production) and colored console output
(local development) via a single configuration, and integrates with the
standard `logging` module so third-party libraries that use `logging`
behave consistently. It also makes context binding (request IDs, user
IDs) straightforward via `contextvars`.

### Positive Consequences

- Single, consistent log format across the application and its
  dependencies.
- JSON logs are ready for ingestion by ELK, Loki, Datadog, etc.
- Lazy initialization keeps test setup simple (`get_logger()` configures
  on first use).

### Negative Consequences

- Requires teaching contributors about context binding.
- Slight learning curve compared to plain `print()`.

## References

- structlog documentation: <https://www.structlog.org>
