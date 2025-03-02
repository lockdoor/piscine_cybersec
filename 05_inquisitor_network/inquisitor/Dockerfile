FROM python:3.12.9-alpine3.21

RUN apk add --no-cache binutils make

RUN pip install scapy pyinstaller

COPY . /inquisitor

WORKDIR /inquisitor

# RUN pyinstaller -y inquisitor.py

# RUN pyinstaller -y network_scanner.py

# RUN pyinstaller -y sniffer.py

# RUN cp dist/inquisitor/inquisitor ./

# RUN cp dist/network_scanner/network_scanner ./

# RUN cp dist/sniffer/sniffer ./

CMD ["/bin/sh"]
