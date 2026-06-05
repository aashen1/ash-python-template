# ADR-0001: Record Architecture Decisions

- **Status**: accepted
- **Date**: 2026-06-05

## Context and Problem Statement

We need to record the architectural decisions made on this project to provide
context for future contributors, to avoid revisiting settled debates, and to
document the trade-offs we deliberately accepted.

## Considered Options

1. Keep all context in chat logs and pull request descriptions.
2. Maintain a single `ARCHITECTURE.md` document that grows over time.
3. Use lightweight Architecture Decision Records (ADRs), one per decision,
   stored under `docs/adr/harness/`.

## Decision Outcome

Chosen option: **3 — Use lightweight ADRs under `docs/adr/harness/`**.

ADRs are easy to discover, immutable once accepted, and align with the
"document the why, not the what" philosophy.

### Positive Consequences

- New contributors can read the rationale behind the current stack.
- Decisions are reviewable via pull requests.
- The directory doubles as a historical log of the project's evolution.

### Negative Consequences

- Adds a small amount of process overhead for non-trivial decisions.
- Requires discipline to keep records up to date.

## References

- Michael Nygard, _Documenting Architecture Decisions_.
