import sqlite3


def tao_file(file_name):
    conn = sqlite3.connect(file_name)
    conn.execute('''
    CREATE TABLE PHIM(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    ten TEXT NOT NULL UNIQUE,
    nam_sx TEXT,
    the_loai TEXT,
    thoi_luong INTEGER,
    nuoc_sx TEXT)
    ''')
    conn.commit()
    conn.close()
