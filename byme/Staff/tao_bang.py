import sqlite3


def create_connect(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None


if __name__ == '__main__':
    conn = create_connect(r"ql_nhan_vien.db")

    if conn is not None:
        f = open("tao_bang.sql", "r", encoding="UTF-8")
        script = f.read()
        conn.executescript(script)
        f.close()
    conn.close()
