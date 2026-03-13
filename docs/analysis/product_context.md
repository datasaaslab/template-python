# Product Context For Template Repositories

This repository template is intended for Python projects that combine an HTTP API, a separate background worker process, and a Postgres-backed persistence layer. It is designed to be copied into future repositories that will later gain product-specific behavior without first needing to renegotiate foundational structure.

## Intended Usage

- Start new API and worker projects from a shared baseline.
- Preserve a predictable layout for human maintainers and coding agents.
- Establish delivery and architecture conventions before product logic is introduced.

## Core Assumptions

- The future project will expose one or more HTTP interfaces through FastAPI.
- Background execution concerns will live in a separate runtime, even if initial worker behavior is minimal.
- Configuration should be typed and environment-driven.
- Persistence will default to Postgres with SQLAlchemy and Alembic.
- Projects will evolve incrementally through bounded backlog slices rather than large undifferentiated rewrites.

## Non-Goals

- This template does not define a business domain.
- This template does not implement production workflows, use cases, or repositories.
- This template does not prescribe a specific queue technology, deployment platform, or observability stack.
- This template does not replace project-specific architecture decisions once a real product exists.

## Why Strict Structure Matters

Agentic development works best when code ownership and boundaries are obvious. A strict structure reduces ambiguity about where to place code, where to look for related logic, and which modules are allowed to depend on one another. That improves:

- implementation speed for bounded changes
- review quality because changes are easier to evaluate
- automation reliability because tooling and workflows are predictable
- onboarding because the repository tells a consistent story

The purpose of the template is not to be minimal at any cost. The purpose is to be reusable, explicit, and safe to extend.
