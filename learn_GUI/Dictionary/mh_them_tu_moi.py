import sqlite3
from tkinter import *
from tkinter import messagebox


def Them_tu_moi(tu_them, nghia_them):
    conn = sqlite3.connect("qltratu.db")
    sql = "SELECT * FROM TU_DIEN WHERE tu=?"
    cur = conn.execute(sql, (tu_them,))
    rows = cur.fetchall()
    if len(rows) == 0:
        sql = "INSERT INTO TU_DIEN VALUES(?,?)"
        conn.execute(sql, (tu_them, nghia_them))
        conn.commit()
        messagebox.showinfo("Thông báo", "Đã thêm thành công.")
    else:
        messagebox.showinfo("Thông báo", "Đã có từ này!")
    conn.close()


def XL_Them_tu_moi():
    tu_moi = txt_tu_moi.get()
    nghia_moi = txt_nghia_moi.get()
    if tu_moi.strip() == "":
        messagebox.showinfo("Thông báo", "Bạn chưa nhập từ muốn thêm!")
        return
    Them_tu_moi(tu_moi, nghia_moi)


if __name__ == "__main__":
    # tạo cửa sổ giao diện
    window = Tk()
    window.title("Thêm từ mới")
    window.geometry("350x100")
    # tạo các điều khiển và định vị trí các điều khiển
    Label(window, text="Từ mới").grid(row=0, column=0, sticky=W)
    txt_tu_moi = Entry(window, width=40)
    txt_tu_moi.grid(row=0, column=1, sticky=W)

    Label(window, text="Nghĩa mới").grid(row=1, column=0, sticky=W)
    txt_nghia_moi = Entry(window, width=40)
    txt_nghia_moi.grid(row=1, column=1, sticky=W)

    khung_chuc_nang = Frame(window)
    Button(khung_chuc_nang, text="Thêm mới", command=XL_Them_tu_moi).grid(
        row=0, column=0, padx=5)
    khung_chuc_nang.grid(row=2, column=1, padx=5, pady=5)
    #
    txt_tu_moi.focus()
    # mở cửa sổ giao diện
    window.mainloop()
