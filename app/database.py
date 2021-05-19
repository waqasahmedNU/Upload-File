import sqlite3
from sqlite3 import Error
from flask_restful import current_app as app


class Database:

    def __init__(self):
        pass

    def create(self, db_file):
        try:
            db_connection = sqlite3.connect(db_file)
            CREATE_DATASET = """ CREATE TABLE IF NOT EXISTS dataset (
                                                    id integer PRIMARY KEY,
                                                    name text NOT NULL,
                                                    path VARCHAR(250) NOT NULL
                                                ); """
            cur = db_connection.cursor()
            cur.execute(CREATE_DATASET)
            db_connection.close()
        except Error as e:
            return e

    def connect(self):
        try:
            return sqlite3.connect(app.config['DB_FILE'])
        except Error as e:
            return e

    def close(self, db_connection):
        db_connection.close()

    def add(self, db_connection, data):
        INSERT = """ INSERT INTO dataset(name, path) VALUES(?,?) """
        try:
            cur = db_connection.cursor()
            cur.execute(INSERT, data)
            db_connection.commit()
            return cur.lastrowid
        except Error as e:
            return e

    def get(self, db_connection):
        GET = """SELECT * FROM dataset"""
        try:
            data = []
            cur = db_connection.cursor()
            cur.execute(GET)
            rows = cur.fetchall()
            if len(rows) > 0:
                for data_row in rows:
                    data.append({
                        'name': data_row[1],
                        'path': data_row[2]
                    })
            return data
        except Error as e:
            return e
