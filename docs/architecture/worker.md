# Worker Architecture

The worker application is the baseline process for background and asynchronous execution. It exists as a separate runtime so future projects can run long-lived work independently of HTTP request handling.

## Role Of The Worker App

- start the worker process
- configure runtime concerns such as logging and settings
- host consumers that receive jobs or events
- host executors that perform bounded units of background work

The template does not choose a queue technology up front. It reserves structure for that future integration while preserving clean boundaries.

The worker entrypoint is intentionally minimal. It confirms that process-local configuration and startup logging are wired correctly without embedding queue clients or long-running polling behavior into the template.

## Runtime Boundaries

- `apps/worker/app/runtime` should own worker process setup and coordination concerns.
- `apps/worker/app/consumers` should own message intake or scheduling hooks.
- `apps/worker/app/executors` should own execution adapters that call into shared packages.

Worker modules should orchestrate execution, not absorb domain logic that belongs in reusable packages.

## No Coupling To API Internals

The worker must not import route modules, FastAPI dependencies, or other API-specific composition from `apps/api`. Shared behavior belongs in `packages/`, where both processes can depend on it safely.

## Execution Checkpoints

Future worker implementations should be structured so they can introduce:

- clear execution state transitions
- logging around job start and completion
- retries and failure handling
- idempotency boundaries

Those behaviors should be added explicitly rather than hidden inside a queue client callback.

## Cancellation And Progress

Cancellation, progress reporting, and heartbeat behavior are treated as future extensions. The template expects these concerns to be added through explicit contracts and runtime components when a product requires them, rather than being improvised in application entrypoints.
