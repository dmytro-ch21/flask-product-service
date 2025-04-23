import psycopg2
from flask import g, current_app

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            dbname="flask_postgres_db",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
