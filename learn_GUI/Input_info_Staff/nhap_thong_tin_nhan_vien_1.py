from tkinter import *


def Xu_ly_xac_nhan():
    chuoi = "Họ tên: "+txt_ho.get()+" "+txt_ten.get()

    # Dung configure de in text trong label
    lbl_thong_tin.configure(text=chuoi)


# tạo cửa sổ giao diện
window = Tk()
window.title("Thông tin nhân viên")
window.geometry("400x200")

# tạo các điều khiển và định vị trí các điều khiển
# sticky = W (W: West canh huong Tay (dai dien ben trai) E: East (ben phai))
Label(window, text="Họ").grid(row=0, column=0, sticky=W)

txt_ho = Entry(window, width=30)
txt_ho.grid(row=0, column=1, sticky=W)

Label(window, text="Tên").grid(row=1, column=0, sticky=W)
txt_ten = Entry(window, width=20)
txt_ten.grid(row=1, column=1, sticky=W)

# Frame: nhom
khung_chuc_nang = Frame(window)
nut_xac_nhan = Button(khung_chuc_nang, text="Xác nhận", command=Xu_ly_xac_nhan)
nut_xac_nhan.grid(row=0, column=0, padx=5)
khung_chuc_nang.grid(row=2, column=1, padx=5, pady=5,
                     columnspan=2)


# columnspan: merge cot
lbl_thong_tin = Label(window)
lbl_thong_tin.grid(row=3, column=0, columnspan=2)
#
# .focus() de canh tro chuot tai txt_ho
txt_ho.focus()
# mở cửa sổ giao diện
window.mainloop()
