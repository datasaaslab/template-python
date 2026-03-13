"""Typed enums and shared types for application configuration."""

from enum import StrEnum


class AppEnvironment(StrEnum):
    """Allowed application runtime environments."""

    LOCAL = "local"
    TEST = "test"
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
