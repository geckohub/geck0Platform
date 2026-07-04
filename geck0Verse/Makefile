.PHONY: validate test up down logs
validate:
	./validate.sh

test:
	python3 -m pytest

up:
	docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs -f --tail=200
