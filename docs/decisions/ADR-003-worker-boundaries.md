# ADR-003: Worker Runtime Must Remain Separate From API Runtime

## Status

Accepted

## Context

Projects built from this template are expected to support HTTP request handling and background execution. These concerns have different runtime profiles and should not be collapsed into one application layer by default.

## Decision

The worker runtime remains structurally separate from the API runtime. Shared logic belongs in `packages/`, while process-specific composition stays in `apps/api` and `apps/worker`.

## Rationale

- API request handling and background execution scale differently.
- Worker concerns such as retries, long-running tasks, cancellation, and checkpointing should evolve independently of route handling.
- Structural separation prevents API modules from becoming a hidden dependency for non-HTTP execution paths.
- Clear runtime boundaries make code generation and maintenance safer for agents.

## Consequences

- Worker code must not import API-specific modules.
- Shared domain and contract code must be placed in reusable packages.
- Future queue integrations should attach to worker modules rather than route handlers or API startup hooks.
- The template worker entrypoint remains a startup placeholder rather than a hidden product runtime.
