import sqlite3
from tkinter import *
from tkinter import messagebox


def Tra_tu(tu_tra):
    global txt_nghia_tra
    conn = sqlite3.connect("qltratu.db")
    sql = "SELECT nghia FROM TU_DIEN WHERE UPPER(tu)=?"
    cur = conn.execute(sql, (tu_tra.upper(),))
    nghia = cur.fetchone()
    if nghia != None:
        txt_nghia_tra.delete(0, END)
        txt_nghia_tra.insert(0, nghia[0])
    else:
        messagebox.showinfo("Thông báo", "Không tìm thấy từ này!")
    conn.close()


def XL_Tra_tu():
    tu_tra = txt_tu_tra.get()
    if tu_tra.strip() == "":
        messagebox.showinfo("Thông báo", "Bạn chưa nhập từ muốn tra!")
        return
    Tra_tu(tu_tra)


# main
if __name__ == "__main__":
    # tạo cửa sổ giao diện
    window = Tk()
    window.title("Tra từ")
    window.geometry("350x100")
    # tạo các điều khiển và định vị trí các điều khiển
    Label(window, text="Từ tra").grid(row=0, column=0, sticky=W)
    txt_tu_tra = Entry(window, width=40)
    txt_tu_tra.grid(row=0, column=1, sticky=W)

    Label(window, text="Nghĩa").grid(row=1, column=0, sticky=W)
    txt_nghia_tra = Entry(window, width=40)
    txt_nghia_tra.grid(row=1, column=1, sticky=W)

    khung_chuc_nang = Frame(window)
    Button(khung_chuc_nang, text="Tra từ", command=XL_Tra_tu).grid(
        row=0, column=0, padx=5)
    khung_chuc_nang.grid(row=2, column=1, padx=5, pady=5)

    #
    txt_tu_tra.focus()
    # mở cửa sổ giao diện
    window.mainloop()
