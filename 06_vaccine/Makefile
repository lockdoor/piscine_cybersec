all:
	docker compose up -d --build

down:
	docker compose down

dev:
	docker compose -f docker-compose-dev.yaml up --build

dev_down:
	docker compose -f docker-compose-dev.yaml down

run:
	docker exec -it vaccine /bin/sh

clean:
	rm -rf ./fastapi/src/__pycache__
	rm -f ./fastapi/src/example.db
	rm -f ./vaccine/src/output.tar
	rm -rf ./vaccine/src/output
	docker image prune -f

fclean: clean
	docker image rm -f lockdoor/vaccine
	docker image rm -f lockdoor/fastapi
	docker image rm -f postgres:13.20-alpine3.20
	docker image rm -f mysql

PHONY: all down dev dev_down run clean fclean
