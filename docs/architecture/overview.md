# Architecture Overview

This template favors an explicit, layered repository shape that keeps process entrypoints, shared code, infrastructure, and delivery documentation separate. The result is a baseline that future projects can extend with minimal ambiguity.

## Documentation As Source Of Truth

The `docs/` directory defines intended usage, architecture boundaries, workflow rules, testing expectations, and recorded decisions. Code should reflect the documented architecture, and architectural changes should be documented as part of the same bounded change.

## Applications

- `apps/api` owns the FastAPI process and API-specific composition.
- `apps/worker` owns the worker process and worker-specific composition.

These application directories should stay thin. They wire dependencies and start processes, but they do not become homes for reusable business logic.

## Shared Packages

- `packages/config` centralizes configuration and environment-driven settings.
- `packages/contracts` holds typed contracts shared at process or boundary edges.
- `packages/domain` holds domain-level behavior and domain errors.
- `packages/db` holds persistence primitives such as SQLAlchemy metadata, sessions, models, and repositories.
- `packages/testing` holds shared testing support code.

The package split makes ownership explicit and discourages direct cross-process imports between API composition and worker composition.

## Infrastructure

`infra/` contains operational baseline files, including local Docker Compose and Alembic migration wiring. Infrastructure files should stay generic and reusable and should not absorb application logic.

## Tests

- `tests/unit` verifies isolated logic.
- `tests/integration` verifies behavior across infrastructure or process boundaries.
- `tests/smoke` verifies lightweight startup and baseline end-to-end paths.

Tests should mirror the architectural boundaries they exercise.

## Boundary Rules

- Routes remain thin and delegate to shared packages.
- Worker consumers and executors coordinate work but do not own API concerns.
- Domain code does not depend on FastAPI internals.
- The worker does not depend on API-specific modules.
- Environment access is centralized in `packages/config`, with `packages/config/settings.py` acting as the canonical runtime entrypoint.
- Database setup is centralized in `packages/db/session.py` so API and worker runtimes can share the same connection construction rules.

## Why Explicit Contracts

This template prefers explicit request, response, job, and event contracts because shared boundaries are where ambiguity becomes expensive. Typed contracts improve compatibility, testability, and agentic code generation by making data shape and responsibility visible.
