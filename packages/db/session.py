"""Database engine and session factory helpers for template projects."""

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from packages.config.settings import get_settings


def create_engine_from_settings() -> Engine:
    """Create the shared SQLAlchemy engine from typed settings."""
    settings = get_settings()
    return create_engine(settings.database_url, future=True)


def create_session_factory(engine: Engine | None = None) -> sessionmaker[Session]:
    """Create a session factory for repository and service wiring."""
    resolved_engine = engine if engine is not None else create_engine_from_settings()
    return sessionmaker(bind=resolved_engine, autoflush=False, expire_on_commit=False)
