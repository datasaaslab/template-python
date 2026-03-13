UV := uv

.PHONY: bootstrap format lint typecheck test test-unit test-integration test-smoke migrate ci

bootstrap:
	./scripts/bootstrap.sh

format:
	./scripts/format.sh

lint:
	./scripts/lint.sh

typecheck:
	$(UV) run mypy .

test:
	./scripts/test.sh

test-unit:
	./scripts/test.sh tests/unit -m "not integration and not smoke"

test-integration:
	./scripts/test.sh tests/integration -m integration

test-smoke:
	./scripts/test.sh tests/smoke -m smoke

migrate:
	$(UV) run alembic -c infra/migrations/alembic.ini upgrade head

ci:
	$(UV) run ruff format --check .
	$(UV) run ruff check .
	$(UV) run mypy .
	$(UV) run pytest
