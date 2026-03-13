# Standard Python Agent-Ready Repository Template

This repository is a reusable baseline for future Python projects that need a FastAPI service, a separate worker process, a Postgres database, and a disciplined structure that coding agents can extend safely. It is intentionally a template, not a product. The code and documents establish conventions, boundaries, and tooling rather than business behavior.

## What This Template Includes

- Python 3.12 baseline
- `uv` as the dependency and command runner standard
- FastAPI application skeleton
- Separate worker process skeleton
- Postgres as the default relational database standard
- SQLAlchemy and Alembic for persistence and migrations
- Pydantic and `pydantic-settings` for typed configuration and external contracts
- Ruff, Mypy, Pytest, and Pre-commit as the default code quality toolchain
- Docker Compose baseline for local infrastructure
- CI workflow for formatting, linting, type checking, and tests

## Repository Layout

- `docs/`: architecture, delivery rules, decisions, testing conventions, and backlog guidance
- `apps/`: process entrypoints and process-specific wiring for the API and worker
- `packages/`: reusable shared code such as config, contracts, domain, database, and testing support
- `infra/`: Docker and migration infrastructure
- `tests/`: unit, integration, and smoke test layers
- `scripts/`: shell entrypoints used by local development and CI

This split keeps process composition separate from reusable code. API-specific wiring stays in `apps/api`, worker-specific wiring stays in `apps/worker`, and shared packages remain importable without crossing application boundaries.

Environment access is centralized in `packages/config/settings.py`. Runtime code should consume typed settings rather than reading environment variables directly.

## Bootstrap A New Project From This Template

1. Create a new repository from this template.
2. Install Python 3.12 and `uv`.
3. Rename the project metadata in `pyproject.toml` and update the top-level README for the new product.
4. Copy `.env.example` to `.env` and set environment values for the local machine.
5. Run `make bootstrap`.
6. Start building one bounded slice at a time while keeping documentation and tests aligned with the evolving project.

## Local Development Commands

- `make bootstrap`: install tooling and sync dependencies with `uv`
- `make format`: apply Ruff formatting
- `make lint`: run Ruff checks
- `make typecheck`: run Mypy
- `make test`: run the full test suite
- `make test-unit`: run unit tests only
- `make test-integration`: run integration tests only
- `make test-smoke`: run smoke tests only
- `make migrate`: run Alembic migrations
- `make ci`: run the baseline local CI sequence

For direct process startup during local development:

- `uv run uvicorn apps.api.app.main:create_app --factory --reload`
- `uv run python -m apps.worker.app.main`

## Migrations And Infrastructure

- Docker Compose lives in `infra/docker/docker-compose.yml`.
- Alembic configuration lives in `infra/migrations/`.
- The default database target is Postgres.
- Runtime configuration is provided through `packages/config/settings.py` and environment variables declared in `.env.example`.
- `make migrate` applies migrations with the same `uv`-based toolchain used elsewhere in the repository.

## Notes On Intended Use

This template is intentionally generic. It should be extended into a real product repository by adding product-specific contracts, domain models, services, repositories, migrations, and tests within the existing structure. The template should not accumulate business logic of its own.
