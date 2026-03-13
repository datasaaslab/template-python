# ADR-001: Postgres As The Default Database

## Status

Accepted

## Context

The template needs a single default relational database standard so future projects do not spend early setup cycles re-evaluating basic persistence choices.

## Decision

Postgres is the default database standard for repositories created from this template.

## Rationale

- It is mature, widely deployed, and well supported in Python ecosystems.
- It works well with SQLAlchemy and Alembic.
- It supports transactional workloads, indexing strategies, and schema evolution patterns commonly needed in service applications.
- It keeps the template opinionated enough to be useful without overfitting to a narrow use case.

## Consequences

- Local development and infrastructure examples assume Postgres.
- Schema migrations are written with Postgres as the primary target.
- Environment examples and settings defaults are aligned around Postgres connection strings.
- Future projects may choose a different datastore, but changing that standard should be an explicit architectural decision rather than an accidental drift.
