# ADR-0006: Adopt Conventional Commits and Automated Versioning

- **Status**: accepted
- **Date**: 2026-06-05

## Context and Problem Statement

Release notes, semver bumps, and `CHANGELOG.md` entries are currently
generated manually. Without enforced conventions, commit messages are
inconsistent and changelogs fall out of date.

## Considered Options

1. Continue with ad-hoc commit messages and manual changelog updates.
2. Adopt Conventional Commits and generate the changelog from
   categorized commit fragments (Towncrier) and PR titles.
3. Adopt Conventional Commits only, with `release-please` doing the
   full release automation.

## Decision Outcome

Chosen option: **2 — Conventional Commits + Towncrier**.

We already have Towncrier configured; combining it with a
`commit-msg` hook that enforces Conventional Commits gives us free
linting of commit messages while preserving the existing release flow.
`release-please` is a great option for many projects, but it would
require a deeper refactor of our release workflow.

### Positive Consequences

- Commit messages are machine-parseable.
- `CHANGELOG.md` is generated from fragment files in `changes/`.
- `commit-msg` failures are caught locally via pre-commit.

### Negative Consequences

- Contributors need to learn the Conventional Commits spec.
- Squash-merged PRs must keep their conventional title.

## References

- Conventional Commits: <https://www.conventionalcommits.org>
- Towncrier: <https://towncrier.readthedocs.io>
