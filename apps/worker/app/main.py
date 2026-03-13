"""Worker process entrypoint for the template repository."""

import logging

from packages.config.settings import get_settings

logger = logging.getLogger(__name__)


def main() -> None:
    """Start the worker process with baseline configuration only."""
    settings = get_settings()
    logging.basicConfig(
        level=settings.worker_log_level.upper(),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    logger.info("worker startup complete")


if __name__ == "__main__":
    main()
