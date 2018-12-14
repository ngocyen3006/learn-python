from tkinter import *


def Xu_ly_xac_nhan():
    chuoi = "Họ tên: "+txt_ho.get()+" "+txt_ten.get()
    lbl_thong_tin.configure(text=chuoi)


# tạo cửa sổ giao diện
window = Tk()
window.title("Thông tin nhân viên")
# tạo các điều khiển và định vị trí các điều khiển
Label(window, text="Họ").grid(row=0, column=0, sticky=W)
txt_ho = Entry(window, width=40)
txt_ho.grid(row=0, column=1, sticky=W)

Label(window, text="Tên").grid(row=1, column=0, sticky=W)
txt_ten = Entry(window, width=20)
txt_ten.grid(row=1, column=1, sticky=W)

khung_chuc_nang = Frame(window)
nut_xac_nhan = Button(khung_chuc_nang, text="Xác nhận", command=Xu_ly_xac_nhan)
nut_xac_nhan.grid(row=0, column=0, padx=5)
khung_chuc_nang.grid(row=2, column=1, padx=5, pady=5)

lbl_thong_tin = Label(window)
lbl_thong_tin.grid(row=3, column=0, columnspan=2, sticky=W)
#
txt_ho.focus()
# mở cửa sổ giao diện
window.mainloop()
