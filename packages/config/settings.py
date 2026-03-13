"""Typed runtime settings for template applications."""

from functools import lru_cache

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from packages.config.constants import (
    DEFAULT_API_HOST,
    DEFAULT_API_PORT,
    DEFAULT_DATABASE_URL,
    DEFAULT_LOG_LEVEL,
    DEFAULT_POSTGRES_DB,
    DEFAULT_POSTGRES_HOST,
    DEFAULT_POSTGRES_PASSWORD,
    DEFAULT_POSTGRES_PORT,
    DEFAULT_POSTGRES_USER,
    DEFAULT_SECRET_KEY,
    DEFAULT_WORKER_POLL_INTERVAL_SECONDS,
)
from packages.config.enums import AppEnvironment


class Settings(BaseSettings):
    """Typed application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_env: AppEnvironment = Field(default=AppEnvironment.LOCAL, alias="APP_ENV")
    log_level: str = Field(default=DEFAULT_LOG_LEVEL, alias="LOG_LEVEL")
    api_host: str = Field(default=DEFAULT_API_HOST, alias="API_HOST")
    api_port: int = Field(default=DEFAULT_API_PORT, alias="API_PORT")
    worker_log_level: str = Field(default=DEFAULT_LOG_LEVEL, alias="WORKER_LOG_LEVEL")
    worker_poll_interval_seconds: int = Field(
        default=DEFAULT_WORKER_POLL_INTERVAL_SECONDS,
        alias="WORKER_POLL_INTERVAL_SECONDS",
    )
    database_url: str = Field(default=DEFAULT_DATABASE_URL, alias="DATABASE_URL")
    alembic_database_url: str = Field(default=DEFAULT_DATABASE_URL, alias="ALEMBIC_DATABASE_URL")
    secret_key: SecretStr = Field(default=SecretStr(DEFAULT_SECRET_KEY), alias="SECRET_KEY")
    postgres_user: str = Field(default=DEFAULT_POSTGRES_USER, alias="POSTGRES_USER")
    postgres_password: str = Field(default=DEFAULT_POSTGRES_PASSWORD, alias="POSTGRES_PASSWORD")
    postgres_db: str = Field(default=DEFAULT_POSTGRES_DB, alias="POSTGRES_DB")
    postgres_host: str = Field(default=DEFAULT_POSTGRES_HOST, alias="POSTGRES_HOST")
    postgres_port: int = Field(default=DEFAULT_POSTGRES_PORT, alias="POSTGRES_PORT")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return cached settings so all callers share one configuration object."""
    return Settings()
