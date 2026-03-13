# Backlog Conventions

This template expects backlog execution to happen through bounded stories that can be implemented, reviewed, tested, and merged independently.

## Story-By-Story Execution

- One user story should produce one bounded slice of behavior.
- A story should be small enough to understand end to end without requiring a repository-wide rewrite.
- Large initiatives should be split into epics and then into independently shippable stories.

## Include And Exclude Scope Rules

Each story should declare:

- what is included
- what is explicitly excluded
- what dependencies must already exist
- what blocks completion

This prevents accidental scope expansion and makes handoff clearer for both humans and coding agents.

## Dependencies And Blocks

- If a story depends on another change, state the dependency directly.
- If infrastructure, schema, or contract work is blocking progress, capture that as a separate bounded prerequisite when practical.
- Do not hide blockers inside mixed implementation stories.

## Test Requirements

Every story must define the minimum verification expected for completion. That usually includes:

- unit tests for new isolated logic
- integration tests when crossing a database or process boundary
- smoke coverage when startup or baseline wiring changes
- documentation updates when the story changes architecture, contracts, or operating workflow

## Handoff Rules

Completion notes for a story should identify:

- what was changed
- which tests were run
- what follow-up work remains
- any assumptions or deferred risks

## Review Checklist Expectations

Reviewers should be able to confirm:

- scope matches the story
- boundaries remain intact
- tests match the behavior introduced
- docs are updated when architecture or workflow changed
- unrelated refactors are absent

## No Large Mixed Stories

- Do not combine migrations, infrastructure redesign, refactors, and multiple feature slices in one story unless the work is truly inseparable.
- Do not use feature stories as cover for broad cleanups.
- Keep mechanical refactors separate from behavior changes whenever possible.

## Recommended YAML Convention

When a project using this template tracks stories in YAML, prefer a structure similar to:

```yaml
id: STORY-001
title: Add bounded capability
status: ready
summary: Short statement of intended outcome
includes:
  - Concrete behavior in scope
excludes:
  - Explicitly out-of-scope behavior
dependencies:
  - STORY-000
acceptance_criteria:
  - Observable outcome
tests:
  - unit
  - integration
handoff:
  risks: []
  follow_ups: []
```

The exact tracker format may evolve, but the bounded-slice discipline should not.
