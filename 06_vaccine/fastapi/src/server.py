from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import sqlite3
import psycopg2
import mysql.connector
import os

def insert_data(conn):
    c = conn.cursor()
    with open('MOCK_DATA.csv', 'r') as f:
        for line in f:
            if line.startswith('username'):
                continue
            username, password = line.strip().split(',')
            c.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
    conn.commit()

# sqlite3 database
if not os.path.exists('example.db'):
    with sqlite3.connect('example.db') as conn_sqlite:
        c = conn_sqlite.cursor()
        c.execute('''CREATE TABLE users (
            id INTEGER PRIMARY KEY, 
            username TEXT UNIQUE NOT NULL, 
            password TEXT NOT NULL
        )''')
        insert_data(conn_sqlite)
conn_sqlite = sqlite3.connect('example.db')

# postgres database
conn_pg = psycopg2.connect(
    dbname="fastapi",
    user="postgres",
    password="postgres",
    host="postgres",
    port="5432"
)
c = conn_pg.cursor()
c.execute("SELECT * FROM information_schema.tables WHERE table_name = 'users'")
table = c.fetchall()
if not table:
    c.execute('''CREATE TABLE users (
        id SERIAL PRIMARY KEY, 
        username TEXT UNIQUE NOT NULL, 
        password TEXT NOT NULL
    )''')
    conn_pg.commit()
    insert_data(conn_pg)

# mysql database
conn_my = mysql.connector.connect(
    host="mysql",
    user="fastapi",
    password="fastapi",
    database="fastapi"
)
c = conn_my.cursor()
c.execute("SHOW TABLES LIKE 'users'")
table = c.fetchall()
if not table:
    c.execute('''CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
    )''')
    conn_my.commit()
    insert_data(conn_my)

conn_db = {"sqlite": conn_sqlite, "postgres": conn_pg,"mysql": conn_my}

def read_user_username(db, username):
    try:
        conn = conn_db.get(db)
        if not conn:
            raise HTTPException(status_code=404, detail="not found")
        c = conn.cursor()
        query = f"SELECT id, username FROM users WHERE username='{username}';"
        c.execute(query)
        users = c.fetchall()
        if len(users) == 0:
            return {"message": "User not found"}
        response = []
        for user in users:
            response.append({"id": user[0], "username": user[1]})
        return response
    except Exception as e:
        conn.rollback()
        print(e)
        return {"message": str(e)}

app = FastAPI()

@app.get("/{db}")
async def root(db):
    if db not in ["sqlite", "postgres", "mysql"]:
        raise HTTPException(status_code=404, detail="not found")
    return FileResponse("index.html")

@app.post("/{db}")
async def post(db, Body: dict):
    username = Body.get("username")
    if not username:
        return {"message": "User not found"}
    return read_user_username(db, username)

@app.get("/{db}/{username}")
async def get(db, username):
    return read_user_username(db, username)
