docker-build:
	docker compose -f docker-compose.yml build

docker-run:
	docker compose -f docker-compose.yml up