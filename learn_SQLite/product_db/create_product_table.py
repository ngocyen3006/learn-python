import sqlite3


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None


# Create product.db with non data
db_file = "product.db"
conn = create_connection(db_file)

if conn is not None:
    f = open('product.sql', 'r', encoding="UTF-8")
    script = f.read()
    conn.executescript(script)
    f.close()

    conn.close()
