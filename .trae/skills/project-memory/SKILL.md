---
name: "project-memory"
description: "Project memory system guide. Invoke when a new session starts, when you need to understand project state, or when writing work results into project memory."
---

# Project Memory — Cross-Session Project Memory System

This skill teaches AI sessions how to correctly use the project's documentation system as a **project-specific memory system**, enabling cross-session continuity for stateless AI agents.

## Core Concepts

1. **Documentation = Project Memory**
   - The docs system serves dual purposes: human-readable documentation AND AI-readable project state
   - It is the project's "evolution rings" (年轮) — every session's work is deposited here
   - Without reading docs first, a new session is completely blind to project history

2. **Sessions are Stateless**
   - Every AI session starts from zero — no memory of previous conversations
   - The ONLY continuity mechanism is the documentation system
   - What you don't write down is lost forever

3. **Read-Write Separation**
   - **Read memory** to understand current state before acting
   - **Write memory** to preserve your work for future sessions
   - Both operations are equally important — skipping either breaks the chain

4. **Docs are Intent Source Code**
   - "文档是意图源码，代码是编译产物" — documentation captures WHY, code captures HOW
   - Design decisions must be documented, not just implemented
   - Future sessions need to understand intent, not just output

## Reading Memory: New Session Startup Checklist

When a new session starts, follow this ordered reading sequence:

### Essential (always read first)

| Order | File | Purpose |
|-------|------|---------|
| 1 | `README.md` | Project identity, quick start, available tasks |
| 2 | `CHANGELOG.md` | Version evolution — understand how we got here |
| 3 | `pyproject.toml` / `pixi.toml` | Project config, dependencies, tasks |
| 4 | `.env.example` | Environment configuration reference |

### Contextual (read based on task)

| Order | File | Purpose |
|-------|------|---------|
| 5 | `docs/adr/` | Architecture Decision Records — understand why choices were made |
| 6 | `docs/api.md` | API reference documentation |
| 7 | `.trae/specs/<feature>/progress.md` | Feature completion status (if specs exist) |
| 8 | `.trae/specs/<feature>/spec.md` | Feature requirements and design decisions (if specs exist) |

> **Living Spec Rule**: Feature specs use the "living document" pattern (4-file set). Read progress.md "当前状态" FIRST — it is the single source of truth. Never read Changelog/Decision Log before Current State.

### Reading Anti-Patterns

- Starting to code without reading project docs first
- Reading only code and ignoring docs when investigating an issue
- Assuming you understand the project from the task description alone
- Reading numbered snapshot subdirectories (0-xxx/, 1-xxx/) instead of living spec files
- Quoting stale completion status from old snapshots instead of progress.md "当前状态"
- Reading Changelog/Decision Log before reading Current State — historical info biases judgment

## Writing Memory: Session Output Checklist

Before ending a session (or after completing a logical work unit), ensure:

### Code Changes

| Change Type | Memory Action |
|-------------|---------------|
| New feature | Update `docs/` and `CHANGELOG.md` |
| Bug fix (non-trivial) | Document root cause and fix in `CHANGELOG.md` |
| Config change | Update `.env.example` and `README.md` |
| API change | Update `docs/api.md` + `CHANGELOG.md` |
| Architecture decision | Add ADR in `docs/adr/` |
| Refactoring | Update affected docs |

### Decision Documentation

| Decision Type | Memory Action |
|---------------|---------------|
| Architecture choice | Record ADR: options considered, choice made, rationale |
| Technology selection | Record ADR: alternatives, trade-offs, why this one |
| Scope change | Update README.md + CHANGELOG.md |

### Progress Preservation

| Situation | Memory Action |
|-----------|---------------|
| Incomplete work | Leave progress note with current state |
| Blocked task | Document blocker + what's needed to unblock |
| Partial implementation | Document what's done, what's remaining, and any gotchas |

## Cross-Session Relay Principles

1. **Commit + Document atomically** — every logical work unit gets both a commit AND a doc update
2. **Never assume implicit understanding** — if a future session needs to know something, write it down
3. **Design decisions must be documented** — code comments are NOT sufficient for cross-session continuity
4. **Keep docs honest** — if something is outdated, mark it `<!-- status: needs-update -->` rather than leaving stale info

## Anti-Patterns (Forbidden)

| Anti-Pattern | Why It's Harmful |
|-------------|-----------------|
| Not reading docs before coding | Repeats past mistakes, contradicts existing design |
| Changing code without updating docs | Future sessions can't understand your changes |
| Leaving stale info without marking it | Misleads future sessions into wrong assumptions |
| Assuming "the next AI will know why I did this" | They won't — sessions are stateless |
| Keeping important context only in conversation | Conversation dies when session ends |
| Writing verbose docs when concise would suffice | Wastes future sessions' context budget |
| Creating numbered snapshot subdirectories in spec dirs | Stale snapshots mislead AI; use living spec pattern instead |

## When to Invoke This Skill

1. **New conversation starts** — read the startup checklist to orient yourself
2. **About to make significant changes** — re-read relevant docs to avoid conflicts
3. **Completing a work session** — run the output checklist to preserve your work
4. **Feeling uncertain about project state** — re-read essential docs for grounding
