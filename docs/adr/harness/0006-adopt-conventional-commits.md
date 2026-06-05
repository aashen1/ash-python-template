# ADR-0006: Adopt Conventional Commits

- **Status**: accepted
- **Date**: 2026-06-05

## Context and Problem Statement

Commit messages are inconsistent without enforced conventions, making the git
history hard to read and machine-parse. We need a commit message standard that
works well with AI-assisted development workflows.

## Considered Options

1. Continue with ad-hoc commit messages.
2. Adopt Conventional Commits and generate the changelog from categorized
   commit fragments (Towncrier) and PR titles.
3. Adopt Conventional Commits only, with `release-please` doing the
   full release automation.
4. Adopt Conventional Commits only, without automated release tooling.

## Decision Outcome

Chosen option: **4 — Conventional Commits only**.

We enforce Conventional Commits via a `commit-msg` hook (using
`conventional-pre-commit`). This gives us machine-parseable commit messages
without the overhead of automated release tooling.

### Why not Towncrier?

Towncrier requires maintaining fragment files in a `changes/` directory for
each change. This does not fit AI-assisted development workflows where the
AI does not automatically create fragment files. The manual overhead outweighs
the benefit of auto-generated changelogs.

### Why not release-please?

release-please automatically creates Release PRs on every push to main that
contains a conventional commit. Since AI-assisted commits use various labels
(`chore:`, `style:`, `refactor:`, etc.), this would trigger frequent
unnecessary release PRs. The noise would be disruptive.

### Positive Consequences

- Commit messages are machine-parseable and consistent.
- `commit-msg` failures are caught locally via pre-commit.
- No automated release tooling to maintain or debug.
- Simple workflow: manual version bump, manual tag, manual GitHub Release.

### Negative Consequences

- Contributors need to learn the Conventional Commits spec.
- Squash-merged PRs must keep their conventional title.
- Changelogs must be written manually for each release.

## References

- Conventional Commits: <https://www.conventionalcommits.org>
