all:
	docker build -t ftp_server .
	docker run --rm -d -p 21:21 ftp_server

it:
	docker exec -it ftp_server sh
