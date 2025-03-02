# should prepare before run this makefile

all:
	if [ ! -f "./inquisitor/inquisitor" ]; then $(MAKE) prepare; fi
	docker compose up -d

prepare:
	docker compose up -d --build
	docker exec -it inquisitor sh -c "pyinstaller --onefile -y inquisitor.py"
	docker exec -it inquisitor sh -c "pyinstaller --onefile -y network_scanner.py"
	docker exec -it inquisitor sh -c "pyinstaller --onefile -y spoof.py"
	docker cp inquisitor:/inquisitor/dist/inquisitor ./inquisitor
	docker cp inquisitor:/inquisitor/dist/network_scanner ./inquisitor
	docker cp inquisitor:/inquisitor/dist/spoof ./inquisitor
	docker compose down

down:
	docker compose down

server:
	docker exec -it ftp_server sh

client:
	docker exec -it client sh

inquisitor:
	docker exec -it inquisitor sh

clean:
	docker compose down
	rm -f ./inquisitor/inquisitor
	rm -f ./inquisitor/inquisitor.spec
	rm -f ./inquisitor/network_scanner
	rm -f ./inquisitor/network_scanner.spec
	rm -f ./inquisitor/spoof
	rm -f ./inquisitor/spoof.spec
	rm -rf ./inquisitor/dist
	rm -rf ./inquisitor/build

fclean: clean
	docker image rm inquisitor/inquisitor
	docker image rm inquisitor/client
	docker image rm inquisitor/ftp_server
	docker image prune -f


.PHONY: all build down server client inquisitor
