# API Architecture

The API application uses FastAPI as the baseline HTTP framework. Its role is to expose transport-layer behavior, validate boundary inputs and outputs, and delegate work into shared packages.

## Role Of The FastAPI App

- define application startup and routing
- expose a small app factory for process startup and testing
- expose operational endpoints such as health checks
- translate HTTP concerns into typed contracts
- compose dependencies needed by route handlers

The API layer is not the place for domain orchestration, persistence decisions, or long-running execution logic.

## Thin Routes Rule

Route handlers must remain thin. A route may:

- receive request inputs
- invoke dependency-provided collaborators
- translate errors into HTTP responses
- return typed response payloads

A route must not embed business workflows, direct SQL statements, or ad hoc cross-cutting behavior.

## Dependency Injection Boundaries

FastAPI dependency functions belong in `apps/api/app/dependencies`. They may assemble configuration, sessions, or service objects from shared packages. They must not become a second business logic layer.

## Contracts

Request and response payloads should be represented with explicit Pydantic models in `packages/contracts/api` when concrete endpoints are introduced. Transport-layer contracts must stay stable, typed, and reviewable.

## Placeholder Health Endpoint Policy

The template includes a minimal `/health` endpoint to confirm application startup and provide a smoke-test target. This endpoint should stay simple and operational in nature. It is not a general-purpose status dashboard.

The template API entrypoint intentionally exposes only this route. Product routes should be added later through explicit contracts and shared-package composition.

## Business Logic Placement

Business behavior belongs in shared domain and application-specific packages, not inside route modules. The API app should be easy to reason about because it remains a composition layer rather than a product logic container.
