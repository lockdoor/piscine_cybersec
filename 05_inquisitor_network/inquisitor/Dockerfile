FROM python:3.12.9-alpine3.21

RUN apk add --no-cache binutils make

RUN pip install scapy pyinstaller

COPY . /inquisitor

WORKDIR /inquisitor

CMD ["/bin/sh"]
