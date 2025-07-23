import time
import psycopg2
from psycopg2 import OperationalError

import os

DB_NAME = os.environ.get("POSTGRES_DB", "theatre_db")
DB_USER = os.environ.get("POSTGRES_USER", "postgres")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "postgres")
DB_HOST = os.environ.get("DB_HOST", "db")
DB_PORT = os.environ.get("DB_PORT", "5432")


def wait_for_db():
    print("Waiting for database...")
    while True:
        try:
            conn = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT,
            )
            conn.close()
            print("Database is ready!")
            break
        except OperationalError:
            print("Database not ready yet, waiting 1 second...")
            time.sleep(1)


if __name__ == "__main__":
    wait_for_db()
