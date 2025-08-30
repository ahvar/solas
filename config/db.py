import psycopg2
import functools
from os import environ

def connect_db(func):
    @functools.wraps(func)
    def repo_function(*args, **kwargs):
        conn = psycopg2.connect(
            host=environ.get('DB_HOST'),
            database=environ.get('DB_NAME'),
            port=environ.get('DB_PORT'),
            user=environ.get('DB_USER'),
            password=environ.get('DB_PASS'))
        resp = func(conn, *args, **kwargs)
        conn.commit()
        conn.close()
        return resp
    return repo_function

