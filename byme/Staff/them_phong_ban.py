from tkinter import *
from tkinter import messagebox
import sqlite3


class PhongBan:
    def __init__(self, ma_phong, ten_phong):
        self.ma_phong = ma_phong
        self.ten_phong = ten_phong


def read_phong_ban():
    data = []
    conn = sqlite3.connect(r"ql_nhan_vien.db")
    conn.row_factory = sqlite3.Row
    phong_ban = conn.execute("SELECT * from PHONG_BAN")
    phong_ban = phong_ban.fetchall()
    for i in phong_ban:
        element = PhongBan(i['ma_phong'], i['ten_phong'])
        data.append(element)
    conn.close()
    return data


def them_moi(ma_phong, ten_phong):
    conn = sqlite3.connect(r"ql_nhan_vien.db")
    phong_ban = conn.execute("SELECT * from PHONG_BAN where ma_phong=?", (ma_phong,))
    phong_ban = phong_ban.fetchall()
    if len(phong_ban) == 0:
        conn.execute("insert into PHONG_BAN values(?,?)", (ma_phong, ten_phong))
        conn.commit()
        messagebox.showinfo('Thông báo', 'Đã thêm thành công')
    else:
        messagebox.showinfo('Thông báo', 'Đã có phòng ban này trong danh sách')
    conn.close()


def them_PB():
    ma = ma_phong.get()
    ten = ten_phong.get()
    if ma.strip() == "" or ten.strip() == "":
        messagebox.showinfo("Thông báo", "Bạn chưa nhập đủ thông tin phòng ban")
        return
    them_moi(ma, ten)


def makeGUI_addPB():
    global ma_phong, ten_phong

    window = Tk()
    window.title('Thêm phòng ban')

    label = ['Mã phòng', 'Tên phòng']
    for i in range(2):
        Label(window, text=label[i]).grid(row=i, column=0)

    ma_phong = Entry(window, width=10)
    ma_phong.grid(row=0, column=1, padx=5, pady=3, sticky=W)

    ten_phong = Entry(window, width=20)
    ten_phong.grid(row=1, column=1, padx=5, pady=3, sticky=W)

    them_moi = Button(window, text="Thêm mới", command=them_PB)
    them_moi.grid(row=2, column=1)

    window.mainloop()


if __name__ == '__main__':
    makeGUI_addPB()
