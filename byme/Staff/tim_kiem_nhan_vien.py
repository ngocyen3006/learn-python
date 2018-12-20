from tkinter import *
import sqlite3
from tkinter import messagebox
from in_tat_ca_nv import *


def tim_nhan_vien(msnv, ms_nv, ho_ten, ngay_sinh, gt, luong, ma_phong_ban):
    conn = sqlite3.connect(r'ql_nhan_vien.db')
    cur = conn.execute("select * from NHAN_VIEN where ma_so=?", (msnv,))
    nhan_vien = cur.fetchone()
    if nhan_vien != None:
        ms = nhan_vien[0]
        ten = nhan_vien[1]
        ngay = format_date(nhan_vien[2])
        gioi_tinh = format_gt(nhan_vien[3])
        salary = format_currency(nhan_vien[4])
        ma_phong = nhan_vien[5]

        ms_nv.delete(0, END)
        ms_nv.insert(0, ms)

        ho_ten.delete(0, END)
        ho_ten.insert(0, ten)

        ngay_sinh.delete(0, END)
        ngay_sinh.insert(0, ngay)

        gt.delete(0, END)
        gt.insert(0, gioi_tinh)

        luong.delete(0, END)
        luong.insert(0, salary)

        ma_phong_ban.delete(0, END)
        ma_phong_ban.insert(0, ma_phong)
    else:
        messagebox.showinfo("Thông báo", "Không tìm thấy nhân viên này")
    conn.close()


def tim_nv():
    ma_so_nv = ma_so.get()
    tim_nhan_vien(ma_so_nv, ms_nv, ho_ten, ngay_sinh, gt, luong, ma_phong_ban)


def GUI_tim_kiem():
    global ms_nv, ngay_sinh, ho_ten, gt, luong, ma_phong_ban, ma_so
    window = Tk()
    window.title('Tìm nhân viên theo mã số')
    window.geometry("350x200")

    Label(window, text='Mã số muốn tìm', anchor=E).grid(row=0, column=1, sticky=W)
    ma_so = Entry(window, width=8)
    ma_so.grid(row=0, column=2, sticky=W, padx=3)
    tim = Button(window, text="Tìm", command=tim_nv)
    tim.grid(row=0, column=3, sticky=W)

    label = ['Mã số', 'Họ tên', 'Ngày sinh', 'Giới tính', 'Lương', 'Mã phòng']
    i = 1
    for j in label:
        Label(window, text=j).grid(row=i, column=0, sticky=W, padx=5)
        i += 1

    r = 1
    ms_nv = Entry(window, width=10)
    ms_nv.grid(row=r, column=1, sticky=W, columnspan=2, pady=2)

    r += 1
    ho_ten = Entry(window, width=30)
    ho_ten.grid(row=r, column=1, sticky=W, columnspan=2, pady=2)

    r += 1
    ngay_sinh = Entry(window, width=20)
    ngay_sinh.grid(row=r, column=1, sticky=W, columnspan=2, pady=2)

    r += 1
    gt = Entry(window, width=10)
    gt.grid(row=r, column=1, sticky=W, columnspan=2, pady=2)

    r += 1
    luong = Entry(window, width=20, justify='right')
    luong.grid(row=r, column=1, sticky=W, columnspan=2, pady=2)

    r += 1
    ma_phong_ban = Entry(window, width=20)
    ma_phong_ban.grid(row=r, column=1, sticky=W, columnspan=2, pady=2)

    ma_so.focus()
    window.mainloop()


if __name__ == '__main__':
    GUI_tim_kiem()
