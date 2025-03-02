all: mysql_get

sqlite_get:
	./vaccine.py http://fastapi:8000/sqlite

sqlite_post:
	./vaccine.py -X post http://fastapi:8000/sqlite

postgres_get:
	./vaccine.py http://fastapi:8000/postgres

postgres_post:
	./vaccine.py -X post http://fastapi:8000/postgres

mysql_get:
	./vaccine.py http://fastapi:8000/mysql

mysql_post:
	./vaccine.py -X post http://fastapi:8000/mysql

mysql_get_header:
	./vaccine.py -H User-Agent=vaccine -H hello=lockdoor http://fastapi:8000/mysql

PHONY: sqlite_get sqlite_post postgres_get postgres_post mysql_get mysql_post