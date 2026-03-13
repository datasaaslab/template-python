# Data Architecture

Postgres is the default relational database standard in this template. SQLAlchemy provides the persistence abstraction and Alembic provides schema migration management.

## Default Standard

- Postgres is the expected production-grade relational store.
- SQLAlchemy is the default ORM and SQL toolkit.
- Alembic is the migration mechanism for schema evolution.

This combination is widely supported, operationally mature, and flexible enough for most service-oriented Python projects.

## Separation Of Concerns

- `packages/db/base.py` owns SQLAlchemy metadata and declarative base definitions.
- `packages/db/session.py` owns session factory construction.
- `packages/db/models` owns persistence models.
- `packages/db/repositories` owns data access implementations.

Database access should not be embedded directly in API routes or worker startup modules.

Configuration for database connectivity still enters through `packages/config/settings.py`; database modules consume typed settings rather than reading environment variables directly.

## Migration Policy

- Treat migrations as part of the deliverable whenever a schema change is introduced.
- Keep migrations explicit and reviewable.
- Prefer forward-only, additive changes unless a controlled destructive change is intentionally planned.
- Ensure Alembic metadata stays aligned with SQLAlchemy model definitions.

## Additive Schema Change Preference

Template projects should prefer additive schema evolution because it reduces rollback risk, simplifies zero-downtime planning, and avoids forcing broad code and data rewrites into a single story. Destructive changes should be isolated, documented, and executed deliberately.
