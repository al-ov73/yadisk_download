web-install:
		npm install --prefix ./web

docker-build: web-install
		docker compose -f docker-compose.yml build

docker-run:
		docker compose -f docker-compose.yml up