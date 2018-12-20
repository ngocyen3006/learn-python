from tkinter import *
import sqlite3


class NhanVien:
    def __init__(self, ma_so, ho_ten, ngay_sinh, gioi_tinh, luong, ma_phong):
        self.ma_so = ma_so
        self.ho_ten = ho_ten
        self.ngay_sinh = format_date(ngay_sinh)
        self.gioi_tinh = format_gt(gioi_tinh)
        self.luong = format_currency(luong)
        self.ma_phong = ma_phong


def read_file_db(file):
    data = []
    conn = sqlite3.connect(file)
    conn.row_factory = sqlite3.Row
    nhan_vien = conn.execute("SELECT * from NHAN_VIEN")
    nhan_vien = nhan_vien.fetchall()
    for i in nhan_vien:
        element = NhanVien(i['ma_so'], i['ho_ten'], i['ngay_sinh'], i['gioi_tinh'],
                           i['luong'], i['ma_phong'])
        data.append(element)
    conn.close()
    return data


def format_gt(gt):
    if gt == '1':
        return "Nam"
    return "Nữ"


def format_date(d):
    d = d.split('-')
    return d[2] + '/' + d[1] + '/' + d[0]


def format_currency(c):
    if isinstance(c, str):
        return c
    return f"{c:,.0f} đ"


def makeGUI():
    window = Tk()
    window.title('Danh sách nhân viên')

    title = ['Mã số', 'Họ tên', 'Ngày sinh', 'Giới tính', 'Lương', 'Mã phòng']

    for i in range(6):
        Label(window, text=title[i], font=("Helvetica", "12", "bold")).grid(row=0, column=i)

    nhan_vien = read_file_db(r"ql_nhan_vien.db")
    x = 5
    y = 3
    r = 0
    for j in nhan_vien:
        r += 1
        Label(window, text=j.ma_so, relief=RAISED, width=5).grid(row=r, column=0, padx=x, pady=y, sticky=W + E)
        Label(window, text=j.ho_ten, relief=RAISED, anchor=W, width=20).grid(row=r, column=1, padx=x, pady=y,
                                                                             sticky=W + E)
        Label(window, text=j.ngay_sinh, relief=RAISED, width=10).grid(row=r, column=2, padx=x, pady=y, sticky=W + E)
        Label(window, text=j.gioi_tinh, relief=RAISED, anchor=W, width=8).grid(row=r, column=3, padx=x, pady=y,
                                                                               sticky=W + E)
        Label(window, text=j.luong, relief=RAISED, width=13).grid(row=r, column=4, padx=x, pady=y, sticky=W + E)
        Label(window, text=j.ma_phong, relief=RAISED, width=8).grid(row=r, column=5, padx=x, pady=y, sticky=W + E)

    window.mainloop()


if __name__ == '__main__':
    makeGUI()
