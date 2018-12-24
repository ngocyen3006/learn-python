# Cau 3
import sqlite3
from SINH_VIEN import khoi_tao_danh_sach_sinh_vien
import os.path
from SINH_VIEN import SINH_VIEN, in_tieu_de


def lay_danh_sach_sinh_vien():
    # lay du lieu sinh vien
    danh_sach_sinh_vien = []
    data = khoi_tao_danh_sach_sinh_vien()
    for sinh_vien in data:
        ho_ten = sinh_vien.ho_ten
        ngay_sinh = sinh_vien.ngay_sinh
        gioi_tinh = sinh_vien.gioi_tinh
        diem_trung_binh = sinh_vien.diem_trung_binh
        ma_khoa = sinh_vien.ma_khoa
        danh_sach_sinh_vien.append(
            (ho_ten, ngay_sinh, gioi_tinh, diem_trung_binh, ma_khoa))
    return danh_sach_sinh_vien


def tao_bang_sinh_vien():
    # tao file "QLSinhVien.db"
    danh_sach_sinh_vien = lay_danh_sach_sinh_vien()
    conn = sqlite3.connect("QLSinhVien.db")
    f = open("SinhVien.sql", "r", encoding="UTF-8")
    conn.executescript(f.read())
    f.close()

    sql = "insert into SINH_VIEN(ho_ten,ngay_sinh,gioi_tinh,diem_trung_binh,ma_khoa) values(?,?,?,?,?)"
    conn.executemany(sql, danh_sach_sinh_vien)
    conn.commit()
    conn.close()


def check_file_exist():
    # Kiem tra file co ton tai chua?
    if os.path.isfile("QLSinhVien.db") == False:
        tao_bang_sinh_vien()


def lay_sv_Toan_diem_giam_dan():
    # Loc sinh vien khoa Toan, sap xep diem trung binh giam dan
    conn = sqlite3.connect("QLSinhVien.db")
    conn.row_factory = sqlite3.Row
    sql = "select * from SINH_VIEN where ma_khoa='TO' order by diem_trung_binh DESC"
    cur = conn.execute(sql)
    rows = cur.fetchall()
    for sinh_vien in rows:
        id = sinh_vien['id']
        ho_ten = sinh_vien['ho_ten']
        ngay_sinh = sinh_vien['ngay_sinh']
        gioi_tinh = sinh_vien['gioi_tinh']
        diem_trung_binh = sinh_vien['diem_trung_binh']
        ma_khoa = sinh_vien['ma_khoa']
        SV = SINH_VIEN(id, ho_ten, ngay_sinh, gioi_tinh,
                       diem_trung_binh, ma_khoa)
        SV.in_thong_tin()
    conn.close()
    pass


def lay_sv_nam_khoa_Toan():
    # Loc sinh vien nam trong khoa Toan
    conn = sqlite3.connect("QLSinhVien.db")
    conn.row_factory = sqlite3.Row
    sql = "select * from SINH_VIEN where ma_khoa='TO' and gioi_tinh=1"
    cur = conn.execute(sql)
    rows = cur.fetchall()
    for sinh_vien in rows:
        id = sinh_vien['id']
        ho_ten = sinh_vien['ho_ten']
        ngay_sinh = sinh_vien['ngay_sinh']
        gioi_tinh = sinh_vien['gioi_tinh']
        diem_trung_binh = sinh_vien['diem_trung_binh']
        ma_khoa = sinh_vien['ma_khoa']
        SV = SINH_VIEN(id, ho_ten, ngay_sinh, gioi_tinh,
                       diem_trung_binh, ma_khoa)
        SV.in_thong_tin()
    conn.close()
    pass


def lay_sv_loai_gioi():
    # Loc sinh vien co diem trung binh >= 8.0, sap xep tang theo diem trung binh
    conn = sqlite3.connect("QLSinhVien.db")
    conn.row_factory = sqlite3.Row
    sql = "select * from SINH_VIEN where diem_trung_binh >= 8.0 order by diem_trung_binh ASC"
    cur = conn.execute(sql)
    rows = cur.fetchall()
    for sinh_vien in rows:
        id = sinh_vien['id']
        ho_ten = sinh_vien['ho_ten']
        ngay_sinh = sinh_vien['ngay_sinh']
        gioi_tinh = sinh_vien['gioi_tinh']
        diem_trung_binh = sinh_vien['diem_trung_binh']
        ma_khoa = sinh_vien['ma_khoa']
        SV = SINH_VIEN(id, ho_ten, ngay_sinh, gioi_tinh,
                       diem_trung_binh, ma_khoa)
        SV.in_thong_tin()
    conn.close()
    pass


if __name__ == '__main__':
    # tao bang SINH_VIEN trong file "QLSinhVien.db"
    check_file_exist()

    # Loc sinh vien khoa Toan, sap xep diem trung binh giam dan
    print('\n')
    print("--Sinh viên khoa Toán, điểm trung bình giảm dần--")
    in_tieu_de()
    lay_sv_Toan_diem_giam_dan()
    print('\n')

    # Loc sinh vien nam trong khoa Toan
    print("--Sinh viên nam khoa Toán--")
    in_tieu_de()
    lay_sv_nam_khoa_Toan()
    print('\n')

    # Loc sinh vien co diem trung binh >= 8.0, sap xep tang theo diem trung binh
    print("--Sinh viên loại giỏi, điểm trung bình tăng dần--")
    in_tieu_de()
    lay_sv_loai_gioi()
