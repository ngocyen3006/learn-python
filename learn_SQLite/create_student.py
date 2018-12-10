import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None


db_file = "student.db"
conn = create_connection(db_file)

if conn is not None:
    f = open('student.sql', 'r', encoding="UTF-8")
    script = f.read()
    conn.executescript(script)
    f.close()

    conn.close()
