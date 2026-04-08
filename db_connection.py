import mysql.connector
import os


def get_db_connection():
    conn = mysql.connector.connect(
        host = "locahost",
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD")
        database = "products"
        )
    return conn

    

