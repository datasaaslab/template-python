"""Shared domain exception types for template projects."""


class DomainError(Exception):
    """Base exception for domain-level failures."""


class ValidationDomainError(DomainError):
    """Raised when a domain invariant or validation rule is violated."""
