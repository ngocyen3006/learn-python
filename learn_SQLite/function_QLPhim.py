import sqlite3


def them_phim_moi(ten, nam_sx, the_loai, thoi_luong, nuoc_sx):
    conn = sqlite3.connect(r"QLPhim.db")
    sql = "select * from PHIM"
    sql = "insert into PHIM(ten,nam_sx,the_loai, thoi_luong, nuoc_sx) values(?,?,?,?,?)"
    conn.execute(sql, (ten, nam_sx, the_loai, thoi_luong, nuoc_sx))
    conn.commit()


def read_data(file_name):
    conn = sqlite3.connect(file_name)
    sql = "select * from PHIM"

    try:
        cursor = conn.execute(sql)
        for row in cursor:
            print(f"ID: {row[0]}")
            print(f"Ten: {row[1]}")
            print(f"Nam san xuat: {row[2]}")
            print(f"The loai: {row[3]}")
            print(f"Thoi luong: {row[4]}")
            print(f"Nuoc san xuat: {row[5]}")
            print('\t---------------------')
    except sqlite3.OperationalError:
        print("File null")

    conn.close()


def del_phim(id):
    conn = sqlite3.connect(r"QLPhim.db")
    sql = "delete from PHIM where ID=?"
    conn.execute(sql, (id,))
    conn.commit()
