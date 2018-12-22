'''
Yêu cầu:
1. Đọc file employees.text
2. Tạo file employees.db (sqlite)
3. Đọc table Employees để in danh sách nhân viên.
4. Tạo màn hình để in danh sách (tkinter)

'''
import sqlite3
from tkinter import *
import os.path
from pprint import pprint


class NhanVien:
    def __init__(self, ID, ten, luong, ngay_lam):
        self.ID = ID
        self.ten = ten
        self.luong = luong
        self.ngay_lam = ngay_lam


def doc_file_text():
    danh_sach_nv = []
    with open("employees.txt") as file:
        line = file.readline()
        while line:
            line = line.split(',')
            ten = line[0].strip() + " " + line[1].strip()
            luong = float(line[2].strip())
            ngay_lam = line[3].strip()
            nhan_vien = (ten, luong, ngay_lam)
            danh_sach_nv.append(nhan_vien)
            line = file.readline()
    file.close()
    return danh_sach_nv


def tao_file_db():
    data = doc_file_text()
    conn = sqlite3.connect("Employees.db")
    f = open('nhan_vien.sql', 'r', encoding='UTF-8')
    conn.executescript(f.read())
    f.close()

    conn.executemany(
        'insert into EMPLOYEES(Ten, Luong, Ngay_vao_lam) values(?,?,?) ', data)
    conn.commit()
    conn.close()


def read_file_db():
    ds_nhan_vien = []
    conn = sqlite3.connect("Employees.db")
    conn.row_factory = sqlite3.Row

    ds_nv = conn.execute('select * from EMPLOYEES')
    ds_nv = ds_nv.fetchall()
    for nhan_vien in ds_nv:
        ID = nhan_vien['ID']
        ten = nhan_vien['Ten']
        luong = nhan_vien['Luong']
        ngay_vao = nhan_vien['Ngay_vao_lam']
        ds_nhan_vien.append(NhanVien(ID, ten, luong, ngay_vao))
    return ds_nhan_vien


def GUI_in_nv():
    data = read_file_db()
    window = Tk()
    window.title('Danh sách các nhân viên')
    window.geometry("480x500")

    khung_chua = Frame(window)
    khung_chua.grid(row=0)
    scroll = Scrollbar(khung_chua, orient=VERTICAL)
    scroll.grid(row=0, column=4, sticky=N + S)
    # khung_con = Frame(khung_chua, yscroll=scroll.set)
    khung_con = Frame(khung_chua)
    khung_con.grid(row=0)

    x = y = 3
    title = ['ID', 'Tên', 'Lương', 'Ngày vào']
    for i in range(len(title)):
        Label(khung_con, text=title[i], relief=SUNKEN, fg="darkblue", font=(
            "Times", "11", "bold")).grid(row=0, column=i, sticky=W + E, padx=x, pady=y)

    r = 0
    for nhan_vien in data:
        r += 1
        Label(khung_con, text=nhan_vien.ID, relief=RAISED,
              width=5).grid(row=r, column=0, sticky=W + E, padx=x, pady=y)
        Label(khung_con, text=nhan_vien.ten, relief=RAISED, anchor=W,
              width=25).grid(row=r, column=1, sticky=W + E, padx=x, pady=y)
        Label(khung_con, text=nhan_vien.luong, relief=RAISED,
              width=15).grid(row=r, column=2, sticky=W + E, padx=x, pady=y)
        Label(khung_con, text=nhan_vien.ngay_lam, relief=RAISED,
              anchor=W, width=15).grid(row=r, column=3, sticky=W + E, padx=x, pady=y)

    # scroll.config(command=khung_con.yview)
    window, mainloop()


def check_file_exist():
    if os.path.isfile("Employees.db") == False:
        tao_file_db()


if __name__ == '__main__':
    check_file_exist()
    GUI_in_nv()
