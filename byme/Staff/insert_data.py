import sqlite3


def read_file_text(file):
    data_list = []
    with open(file) as f:
        line = f.readline()
        while line:
            line = line.strip()
            data_list.append(tuple(line.split(",")))
            line = f.readline()
    return data_list


def insert_phong_ban(pbTuple):
    conn.executemany("INSERT INTO PHONG_BAN(ma_phong, ten_phong) VALUES (?,?)", pbTuple)
    conn.commit()


def insert_nhan_vien(nvTuple):
    conn.executemany("INSERT INTO NHAN_VIEN(ma_so, ho_ten, ngay_sinh, gioi_tinh, luong, ma_phong) values(?,?,?,?,?,?)",
                     nvTuple)
    conn.commit()


if __name__ == '__main__':
    conn = sqlite3.connect(r"ql_nhan_vien.db")
    conn.row_factory = sqlite3.Row

    phong_ban = "SELECT * from PHONG_BAN"
    nhan_vien = "SELECT * from NHAN_VIEN"

    pbTuple = read_file_text("phong_ban.txt")
    nvTuple = read_file_text("nhan_vien.txt")

    insert_phong_ban(pbTuple)
    insert_nhan_vien(nvTuple)
