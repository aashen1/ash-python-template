---
name: "archive-conventions"
description: "Defines conventions for archiving docs to docs/archive/. Invoke when user asks to archive documents, move completed plans/specs/reports to archive, or says '归档'."
---

# Archive Conventions

This skill defines the directory structure, naming rules, and workflow for archiving documents to `docs/archive/`.

## Directory Structure

```
docs/archive/
├── archive-log.md          # Archive operation log (append-only)
│
├── plans/                  # All plan documents
│   └── vX.Y.Z/            # Version-specific plans (optional)
│
├── reports/                # All report documents
│
└── specs/                  # All spec triplets (spec.md/checklist.md/tasks.md)
    └── <feature-name>/     # Feature-specific spec directories
```

## Classification Rules

### plans/
Any document that describes **intended work** or **how to do something**:
- Feature plans, bug fix plans, refactoring plans
- Release plans, merge plans
- Optimization plans, integration plans
- Research plans with action items

### reports/
Any document that **analyzes** or **investigates** without prescribing action:
- Deep inspection reports, analysis reports
- Merge conflict analyses, project status analyses
- Research documents without action items

### specs/
Any spec triplet directory containing `spec.md` + `checklist.md` + `tasks.md`:
- Keep the triplet together as a subdirectory
- Named by feature/issue (e.g., `fix-baseline-evaluation-issues/`)

### Standalone topic directories
Coherent topic groups that don't fit plans/reports/specs:
- Must be self-contained (all related files in one directory)

## Version Grouping

When archiving documents tied to a specific version:
- Plans → `plans/vX.Y.Z/`
- Specs → `specs/vX.Y.Z/`
- Reports stay in `reports/` (no version subdirectory needed)

## Naming Rules

1. **English only** — no Chinese characters in filenames
2. **Lowercase with hyphens** — no underscores, no spaces, no CamelCase
   - `ragas-integration-plan.md`
   - NOT `ragas_integration_plan.md`
   - NOT `Ragas_Integration_Plan.md`
3. **Spec triplet files** — always `spec.md`, `checklist.md`, `tasks.md` (no prefix)
4. **Descriptive names** — `<topic>-<type>.md` pattern for standalone files
   - `fix-evaluation-bugs.md` (not just `fix.md`)

## Archive Workflow

1. **Classify** the document: plan → `plans/`, report → `reports/`, spec → `specs/`
2. **Check version**: if tied to a specific version, place in version subdirectory
3. **Rename** if needed: Chinese → English, underscores → hyphens, spaces → hyphens
4. **Move** the file to the correct location
5. **Check for duplicates**: if the same content already exists in archive, move duplicate to `.trashbin/`
6. **Log** the operation in `archive-log.md`
7. **Commit** with message: `chore: archive <description>`

## Anti-Patterns (DO NOT)

1. **DO NOT** create new top-level directories under `docs/archive/` unless it's a standalone topic group
2. **DO NOT** use source-based directory names like `trae-documents/`, `trae-plans/`, `trae-specs/` — classify by content type, not by origin
3. **DO NOT** archive duplicate files — check for existing copies first
4. **DO NOT** use Chinese filenames — always rename to English before archiving
5. **DO NOT** use underscore or space in filenames — always use hyphens
6. **DO NOT** nest spec directories inside plans/ or reports/ — specs always go to specs/
7. **DO NOT** forget to update archive-log.md after every archive operation
