all:
	docker compose up -d

build:
	docker compose up -d --build

down:
	docker compose down

server:
	docker exec -it ftp_server sh

client:
	docker exec -it client sh

inquisitor:
	docker exec -it inquisitor sh

.PHONY: all build down server client inquisitor