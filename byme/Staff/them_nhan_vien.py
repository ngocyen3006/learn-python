from tkinter import *
from tkinter import messagebox
import sqlite3
from them_phong_ban import read_phong_ban


def ds_pb():
    ds = []
    data = read_phong_ban()
    for i in data:
        ds.append(i.ma_phong)
    return ds


def doi_ns(ngay):
    ngay = ngay.split('/')
    return ngay[2] + '-' + ngay[1] + '-' + ngay[0]


def them_moi(ma, ten, ns, gt, luong, pb):
    conn = sqlite3.connect(r"ql_nhan_vien.db")
    nhan_vien = conn.execute("SELECT * from NHAN_VIEN where ma_so=?", (ma,))
    nhan_vien = nhan_vien.fetchall()
    if len(nhan_vien) == 0:
        conn.execute("insert into NHAN_VIEN values(?,?,?,?,?,?)", (ma, ten, doi_ns(ns), str(gt), luong, pb))
        conn.commit()
        messagebox.showinfo('Thông báo', 'Đã thêm thành công')
    else:
        messagebox.showinfo('Thông báo', 'Nhân viên này đã có trong danh sách')
    conn.close()


def them_nv():
    ma = ma_so.get()
    ten = ho_ten.get()
    ngay = ns.get()
    gioi_tinh = gt.get()
    l = luong.get()
    pb = phong_ban.get()

    them_moi(ma, ten, ngay, gioi_tinh, l, pb)


def GUI_add_NV():
    global ma_so, ho_ten, ns, gt, phong_ban, luong
    window = Tk()
    window.title('Thêm nhân viên')
    window.geometry("400x170")

    label = ['Mã số', 'Họ tên', 'Ngày sinh', 'Giới tính', 'Lương', 'Phòng ban']
    for i in range(len(label)):
        Label(window, text=label[i]).grid(row=i, column=0, sticky=W, padx=5)

    r = 0
    ma_so = Entry(window, width=10)
    ma_so.grid(row=r, column=1, sticky=W)

    r += 1
    ho_ten = Entry(window, width=40)
    ho_ten.grid(row=r, column=1, sticky=W)

    r += 1
    ns = Entry(window, width=20)
    ns.grid(row=r, column=1, sticky=W)

    r += 1
    gt = IntVar()
    gt.set(1)
    khung_gt = Frame(window)
    gt_nam = Radiobutton(khung_gt, text='Nam', value=1, variable=gt)
    gt_nam.grid(row=0, column=0, sticky=W)

    gt_nu = Radiobutton(khung_gt, text='Nữ', value=0, variable=gt)
    gt_nu.grid(row=0, column=1, sticky=W)

    khung_gt.grid(row=r, column=1, sticky=W)

    r += 1
    luong = Entry(window, width=20)
    luong.grid(row=r, column=1, sticky=W)

    r += 1
    ds_phong_ban = ds_pb()
    phong_ban = StringVar()
    phong_ban.set('KT')

    ds = OptionMenu(window, phong_ban, *ds_phong_ban)
    ds.grid(row=r, column=1, sticky=W)

    r += 1
    them_moi = Button(window, text="Thêm mới", command=them_nv)
    them_moi.grid(row=r, column=1, padx=60, sticky=W)

    window.mainloop()


if __name__ == '__main__':
    GUI_add_NV()
