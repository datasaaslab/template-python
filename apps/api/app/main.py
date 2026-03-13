"""FastAPI application entrypoint for the template repository."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Final

from fastapi import FastAPI
from pydantic import BaseModel

from packages.config.settings import get_settings

APP_TITLE: Final[str] = "Template API"


class HealthResponse(BaseModel):
    """Minimal operational response model for smoke checks."""

    status: str


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    """Load application settings during startup without embedding product logic."""
    get_settings()
    yield


async def health() -> HealthResponse:
    """Provide a minimal operational health response for smoke checks."""
    return HealthResponse(status="ok")


def create_app() -> FastAPI:
    """Create the FastAPI application with template-only routes."""
    application = FastAPI(title=APP_TITLE, lifespan=lifespan)
    application.add_api_route(
        "/health",
        health,
        methods=["GET"],
        response_model=HealthResponse,
        tags=["operational"],
    )
    return application


app = create_app()
