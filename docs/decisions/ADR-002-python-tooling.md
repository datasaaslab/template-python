# ADR-002: Standard Python Tooling

## Status

Accepted

## Context

The template needs a consistent default toolchain for formatting, linting, typing, testing, configuration management, and local automation.

## Decision

The standard toolchain is:

- `uv` for dependency management and command execution
- Ruff for formatting and linting
- Mypy for static type checking
- Pytest for testing
- Pre-commit for local hook automation
- Pydantic with `pydantic-settings` for typed settings and boundary models

## Rationale

- Ruff provides fast, unified formatting and linting with a small operational footprint.
- Mypy reinforces explicit contracts and catches boundary mistakes early.
- Pytest is flexible enough for unit, integration, and smoke testing layers.
- Pre-commit helps teams enforce baseline checks before code reaches CI.
- Pydantic settings make environment-driven configuration explicit and typed.

## Consequences

- New repositories should preserve this baseline unless they have a strong reason to change it.
- CI, shell scripts, Makefile targets, and README command examples are aligned around this toolchain.
- Template users inherit a practical default that supports both human maintainers and coding agents.
