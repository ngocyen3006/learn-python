from tkinter import *
import sqlite3
from tkinter import messagebox
from in_tat_ca_nv import *
import tim_kiem_nhan_vien
import them_nhan_vien


def update_staff_sqlite(ho_ten, ngay_sinh, gioi_tinh, luong, ma_phong, ma_so):
    conn = sqlite3.connect(r'ql_nhan_vien.db')
    conn.row_factory = sqlite3.Row

    conn.execute('update NHAN_VIEN set ho_ten=?, ngay_sinh=?, gioi_tinh=?, luong=?, ma_phong=? where ma_so=?',
                 (ho_ten, ngay_sinh, gioi_tinh, luong, ma_phong, ma_so))

    conn.commit()
    messagebox.showinfo('Thông báo', 'Đã sửa thành công')
    conn.close()


def gioi_tinh_so(gt):
    if gt == 'Nam':
        return '1'
    return '0'


def update_staff():
    ma_so_nv = ms_nv.get()
    ten = ho_ten.get()
    ngay = ngay_sinh.get()
    ngay = them_nhan_vien.doi_ns(ngay)
    gioi_tinh = gt.get()
    gioi_tinh = gioi_tinh_so(gioi_tinh)
    l = luong.get()
    l = int("".join(l[:len(l) - 2].split(",")))
    ma_phong = ma_phong_ban.get()
    update_staff_sqlite(ten, ngay, gioi_tinh, l, ma_phong, ma_so_nv)


def tim_nv():
    ma_so_nv = ma_so.get()
    tim_kiem_nhan_vien.tim_nhan_vien(ma_so_nv, ms_nv, ho_ten, ngay_sinh, gt, luong, ma_phong_ban)


def GUI_update():
    global ms_nv, ngay_sinh, ho_ten, gt, luong, ma_phong_ban, ma_so
    window = Tk()
    window.title('Sửa nhân viên theo mã số')
    window.geometry("350x210")

    Label(window, text='Mã số muốn sửa', anchor=E).grid(row=0, column=1, sticky=W)
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

    Button(window, text="Cập nhật", command=update_staff).grid(column=1, pady=5)

    ma_so.focus()
    window.mainloop()


if __name__ == '__main__':
    GUI_update()
