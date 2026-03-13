# Development Workflow

This template assumes disciplined, bounded delivery. The goal is not just to write code that works, but to evolve repositories in a way that stays easy to review, test, and automate.

## Standard Flow

1. Create a branch for one bounded slice of work.
2. Read the relevant docs and confirm the target layer and boundary.
3. Read configuration through `packages/config/settings.py` rather than directly from the environment.
4. Implement only the behavior required for that slice.
5. Add or update tests that prove the change.
6. Update docs when architecture, contracts, or workflows change.
7. Run formatting, linting, type checking, and the relevant test suite.
8. Commit changes in coherent increments.
9. Open a pull request with clear scope and verification notes.

## Scope Discipline

- Keep each branch focused on one story or one tightly related technical slice.
- Avoid broad cleanup work unless it is the explicit goal of the change.
- If unrelated issues are discovered, capture them separately rather than folding them into the current branch.

## Local Quality Gates

Run these before opening a pull request:

- `make format`
- `make lint`
- `make typecheck`
- `make test`
- `make ci`

If only one test layer is relevant during development, run the narrow command first, then complete the full baseline before merge.

## Commit Discipline

- Make commits small enough to review.
- Use commit messages that describe the actual change.
- Do not hide architecture changes inside a generic “cleanup” commit.

## Pull Request Discipline

A pull request should explain:

- the bounded problem being solved
- the main files or layers affected
- how the change was verified
- any follow-up work or known limitations

## Agent Discipline

Coding agents operating in repositories created from this template should:

- respect the documented boundaries
- avoid inventing new architecture without an explicit request
- keep changes small and traceable
- prefer explicit typed code over clever shortcuts
- update docs when the architectural story changes
- keep the Makefile, scripts, docs, and CI workflow aligned when command conventions change
