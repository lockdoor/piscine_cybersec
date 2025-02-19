all:
	python3 inquisitor.py -t

scan:
	./dist/network_scanner/network_scanner -t 172.18.0.0/24

spoof:
	./dist/spoof/spoof -t 172.18.0.2 -g 172.18.0.3
#python3 spoof.py -t 172.18.0.2 -g 172.168.0.3

sniffer:
	python3 sniffer.py -i eth0

inq1:
	python3 inquisitor.py -s 172.18.0.2 -m 02:42:ac:12:00:02 -d 172.18.0.3 -n 02:42:ac:12:00:03

inq2:
	python3 inquisitor.py -s 172.18.0.3 -m 02:42:ac:12:00:03 -d 172.18.0.2 -n 02:42:ac:12:00:02

verbose1:
	python3 inquisitor.py -s 172.18.0.2 -m 02:42:ac:12:00:02 -d 172.18.0.3 -n 02:42:ac:12:00:03 -v

verbose2:
	python3 inquisitor.py -s 172.18.0.3 -m 02:42:ac:12:00:03 -d 172.18.0.2 -n 02:42:ac:12:00:02 -v

# invalid ip address
err0:
	python3 inquisitor.py -s 172.168.0.2 -m 02:42:ac:12:00:02 -d 172.18.0.3 -n 02:42:ac:12:00:03

# invalid mac address
err1:
	python3 inquisitor.py -s 172.18.0.2 -m 02:42:ac:12:00:02 -d 172.18.0.3 -n 02:42:ac:12

.PHONY: all scan spoof sniff
