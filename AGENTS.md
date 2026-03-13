# Repository Governance

This repository is the standard Python agent-ready repository template. It is a reusable baseline for future API and worker projects, not a product codebase. Every change made in this repository must preserve template quality, generic applicability, and scaffold friendliness.

## Purpose

- Provide a clean starting point for Python 3.12 services that expose an HTTP API and run a separate worker process.
- Establish a consistent repository layout that future projects and coding agents can extend without redesigning fundamentals.
- Centralize repository rules so implementation work stays bounded, reviewable, and automatable.

## Architecture Boundaries

- `apps/api` contains only the FastAPI application entrypoint, route wiring, API dependencies, and API-specific composition.
- `apps/worker` contains only worker process startup, runtime coordination, consumer wiring, and executor composition.
- `packages/config` owns configuration models, configuration types, constants, and environment access.
- `packages/contracts` owns typed API, job, and event schemas shared across process boundaries.
- `packages/domain` owns domain models, domain services, and domain-level errors. Domain code must remain independent of FastAPI and worker runtime details.
- `packages/db` owns SQLAlchemy base metadata, session management, database models, and repository implementations.
- `packages/testing` owns shared testing helpers, fixtures, and factories.
- `infra` owns Docker and migration infrastructure only.
- `docs` is the source of truth for architectural intent, delivery rules, and operating conventions.
- Entry points in `apps/` may compose shared code from `packages/`, but shared code must not depend on application entrypoints in return.

## Mandatory Development Rules

- Keep implementation bounded to the requested slice. Do not widen scope to opportunistic refactors.
- Prefer explicit modules and typed interfaces over hidden magic.
- Add or update documentation when a change affects architecture, delivery rules, or operating assumptions.
- Preserve the repository split between API, worker, domain, contracts, config, database, testing, and infra layers.
- Favor additive changes over destructive redesigns.
- Keep placeholder baseline code generic. Do not embed product-specific business concepts in the template.
- Preserve import safety. Template modules must be importable without requiring product-only environment setup or infrastructure availability.

## Rules For Future Coding Agents

- Read this file and the relevant `docs/` pages before introducing structural changes.
- Do not invent new top-level directories or alternate architectural layers unless the user explicitly asks for them.
- Do not move logic across layer boundaries to “simplify” local implementation.
- Do not place business logic in entrypoints, route handlers, migration files, or scripts.
- Do not create broad helper modules that mix unrelated concerns.
- Do not silently rewrite conventions already established by this template.
- Keep changes small, traceable, and aligned with the backlog slice being implemented.
- When changing tooling or runtime conventions, update the matching docs, scripts, Makefile targets, and CI workflow in the same slice.

## Python Coding Standards

- Target Python 3.12 features and standard library behavior.
- Write clear, typed, readable code that favors straightforward control flow.
- Add module docstrings to baseline modules when they clarify purpose or ownership.
- Prefer small modules with explicit imports over large files with implicit coupling.
- Raise domain-specific exceptions from `packages/domain/errors.py` or feature-local error modules when needed.
- Keep side effects near application boundaries and keep pure logic isolated where practical.

## Typing Requirements

- All new Python modules must use type annotations for public functions, methods, return values, and key variables where clarity is improved.
- Mypy must pass in strict mode as configured in `pyproject.toml`.
- Avoid `Any` unless it is truly unavoidable at a boundary. Narrow types quickly after boundary parsing.
- Shared contracts must be represented with explicit typed models instead of anonymous dictionaries.

## Pydantic Usage Policy

- Use Pydantic and `pydantic-settings` for configuration and external data contracts.
- Keep configuration models inside `packages/config`.
- Use Pydantic models in `packages/contracts` for request, response, job, and event payloads when those payloads become concrete.
- Do not use Pydantic models as a substitute for database models or for arbitrary internal convenience containers.

## Config Policy

- All environment variable reads must be centralized in `packages/config`.
- Application code outside `packages/config` must not call `os.getenv`, `os.environ[...]`, or equivalent environment readers directly.
- `packages/config/settings.py` is the canonical environment entrypoint for runtime code.
- Prefer a single settings entrypoint that composes environment-driven defaults into typed configuration objects.
- Keep constant names, environment variable names, and default values explicit.

## Testing Policy

- Put fast isolated tests in `tests/unit`.
- Put database, network, or process-boundary tests in `tests/integration`.
- Put lightweight end-to-end startup and contract checks in `tests/smoke`.
- Use shared fixtures and factories from `packages/testing` instead of duplicating setup logic.
- Every delivered story must include the minimum set of tests needed to verify the behavior introduced by that story.

## Backlog Execution Policy

- Execute backlog work story by story.
- One story must represent one bounded, reviewable slice with a clear outcome.
- Each story must state included scope, excluded scope, dependencies, and verification expectations.
- Do not combine unrelated refactors, architecture redesign, and feature implementation in the same story.

## Scope Discipline

- Keep implementation aligned to the requested behavior and supporting tests only.
- Do not mix “nice to have” improvements into a bounded change.
- If a larger structural issue is discovered, document it and isolate it from the current slice unless explicitly in scope.

## Lifecycle State Centralization

- Centralize lifecycle states, status enums, and workflow constants in explicit modules rather than scattering string literals.
- Do not redefine the same status vocabulary in API routes, worker executors, and persistence layers independently.
- Shared lifecycle states belong in `packages/contracts`, `packages/domain`, or `packages/config/constants.py`, depending on ownership.

## No Broad Utils Dumping

- Do not introduce catch-all files such as `utils.py`, `helpers.py`, or `common.py` for unrelated logic.
- Utility code is only acceptable when it has a narrow, coherent purpose and a clear owner.
- Shared test-only helpers belong in `packages/testing/helpers.py` or adjacent testing modules, not production packages.

## Worker Independence

- The worker must not depend on API application modules for business execution.
- `apps/worker` may use shared packages such as `packages/config`, `packages/contracts`, `packages/domain`, and `packages/db`.
- `apps/worker` must not import route modules, FastAPI dependency functions, or other API-specific composition from `apps/api`.
- Worker runtime code must stay placeholder-friendly. Do not embed queue-vendor clients, polling loops, or product workflows into the template baseline.

## Command Conventions

- Use `make bootstrap` to install and sync the local development environment.
- Use `make format` to apply formatting.
- Use `make lint` to run Ruff checks.
- Use `make typecheck` to run Mypy.
- Use `make test`, `make test-unit`, `make test-integration`, and `make test-smoke` for test execution.
- Use `make migrate` to run Alembic migrations.
- Use `make ci` to run the same baseline checks enforced in continuous integration.
- Commands must remain aligned across the Makefile, `scripts/`, README examples, and `.github/workflows/ci.yml`.
