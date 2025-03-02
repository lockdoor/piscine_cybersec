FROM python:3.12.9-alpine3.21

RUN apk add --no-cache make

RUN pip install requests

RUN pip install PyYAML

COPY ./src /app

WORKDIR /app

CMD ["/bin/sh"]