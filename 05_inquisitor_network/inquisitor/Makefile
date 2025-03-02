all: inq1

scan:
	./network_scanner -t 172.18.0.0/24

spoof:
	./spoof -t 172.18.0.2 -g 172.18.0.3

inq1:
	./inquisitor -s 172.18.0.2 -m 02:42:ac:12:00:02 -d 172.18.0.3 -n 02:42:ac:12:00:03

inq2:
	./inquisitor -s 172.18.0.3 -m 02:42:ac:12:00:03 -d 172.18.0.2 -n 02:42:ac:12:00:02

verbose1:
	./inquisitor -s 172.18.0.2 -m 02:42:ac:12:00:02 -d 172.18.0.3 -n 02:42:ac:12:00:03 -v

verbose2:
	./inquisitor -s 172.18.0.3 -m 02:42:ac:12:00:03 -d 172.18.0.2 -n 02:42:ac:12:00:02 -v

# invalid ip address
err0:
	./inquisitor -s 172.168.0.2 -m 02:42:ac:12:00:02 -d 172.18.0.3 -n 02:42:ac:12:00:03

# invalid mac address
err1:
	./inquisitor -s 172.18.0.2 -m 02:42:ac:12:00:02 -d 172.18.0.3 -n 02:42:ac:12

conn:
	lftp -u lockdoor,password ftp://ftp_server

.PHONY: all scan spoof sniff inq1 inq2 verbose1 verbose2 err0 err1

