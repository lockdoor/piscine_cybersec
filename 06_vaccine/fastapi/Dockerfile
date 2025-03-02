FROM python:3.12.9-alpine3.21

RUN pip install "fastapi[standard]"
RUN pip install psycopg2-binary
RUN pip install mysql-connector-python

COPY ./src /app
WORKDIR /app

EXPOSE 8000

CMD ["fastapi", "run", "server.py"]
