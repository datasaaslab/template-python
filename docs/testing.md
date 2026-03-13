# Testing Guide

This template separates tests by intent so projects can scale coverage without losing clarity.

## Test Layers

### Unit Tests

Unit tests belong in `tests/unit`. They verify isolated logic with minimal setup and no dependency on real infrastructure. Use unit tests for pure functions, small services, validators, and contract behavior that can run quickly.

### Integration Tests

Integration tests belong in `tests/integration`. They verify interactions across boundaries such as database access, HTTP integrations, queue adapters, or multi-component coordination. These tests may require infrastructure and should be explicit about that dependency.

### Smoke Tests

Smoke tests belong in `tests/smoke`. They verify lightweight startup and baseline end-to-end paths, such as application boot, a health endpoint, or worker startup wiring.

## How To Run Tests

- `make test` runs the full suite.
- `make test-unit` runs unit tests.
- `make test-integration` runs integration tests.
- `make test-smoke` runs smoke tests.

The template also includes process-local test directories under `apps/api/tests` and `apps/worker/tests`. Those directories are part of the configured `pytest` discovery paths and can be used when a future project needs tests that are tightly coupled to application composition rather than shared behavior.

## Minimum Expectations Per Story

- Add unit tests for any new isolated logic.
- Add integration coverage when a story crosses persistence or process boundaries.
- Add or update smoke coverage when startup wiring or baseline application paths change.

## Evolving Coverage In Real Projects

Repositories created from this template should grow tests alongside product behavior. That means:

- introducing shared fixtures and factories in `packages/testing`
- keeping tests close to the behavior they verify
- resisting large piles of brittle end-to-end tests when a smaller layer would be clearer
- periodically revisiting slow integration tests to keep the suite maintainable

The test pyramid should evolve intentionally rather than by accident.
