"""Centralized configuration defaults for the template repository."""

from typing import Final

DEFAULT_API_HOST: Final[str] = "0.0.0.0"
DEFAULT_API_PORT: Final[int] = 8000
DEFAULT_LOG_LEVEL: Final[str] = "INFO"
DEFAULT_WORKER_POLL_INTERVAL_SECONDS: Final[int] = 5
DEFAULT_POSTGRES_USER: Final[str] = "template"
DEFAULT_POSTGRES_PASSWORD: Final[str] = "template"
DEFAULT_POSTGRES_DB: Final[str] = "template"
DEFAULT_POSTGRES_HOST: Final[str] = "localhost"
DEFAULT_POSTGRES_PORT: Final[int] = 5432
DEFAULT_DATABASE_URL: Final[str] = (
    "postgresql+psycopg://template:template@localhost:5432/template"
)
DEFAULT_SECRET_KEY: Final[str] = "change-me-for-real-projects"
