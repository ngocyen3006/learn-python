from tkinter import *


def Xu_ly_xac_nhan():
    chuoi = "Họ tên: "+txt_ho.get()+" "+txt_ten.get()
    chuoi_gioi_tinh = "Giới tính: "
    if chon_gioi_tinh.get() == 0:
        chuoi_gioi_tinh += "Nam"
    elif chon_gioi_tinh.get() == 1:
        chuoi_gioi_tinh += "Nữ"
    else:
        chuoi_gioi_tinh += "Khác"
    chuoi += "\n"+chuoi_gioi_tinh
    chuoi_ngoai_ngu = "Ngoại ngữ: "
    if chon_ngoai_ngu_1.get():
        chuoi_ngoai_ngu += chuoi_ngoai_ngu_1.get() + " "
    if chon_ngoai_ngu_2.get():
        chuoi_ngoai_ngu += chuoi_ngoai_ngu_2.get() + " "
    if chon_ngoai_ngu_3.get():
        chuoi_ngoai_ngu += chuoi_ngoai_ngu_3.get() + " "
    chuoi += "\n"+chuoi_ngoai_ngu

    lbl_thong_tin.configure(text=chuoi)


# tạo cửa sổ giao diện
window = Tk()
window.title("Thông tin nhân viên")
# tạo các điều khiển và định vị trí các điều khiển
d = 0
Label(window, text="Họ").grid(row=0, column=0, sticky=W)
txt_ho = Entry(window, width=40)
txt_ho.grid(row=d, column=1, sticky=W)
d += 1
Label(window, text="Tên").grid(row=1, column=0, sticky=W)
txt_ten = Entry(window, width=20)
txt_ten.grid(row=d, column=1, sticky=W)
d += 1
chon_gioi_tinh = IntVar()
chon_gioi_tinh.set(0)
khung_gioi_tinh = Frame(window)
rdo_nam = Radiobutton(khung_gioi_tinh, text='Nam',
                      value=0, variable=chon_gioi_tinh)
rdo_nu = Radiobutton(khung_gioi_tinh, text='Nữ',
                     value=1, variable=chon_gioi_tinh)
rdo_khac = Radiobutton(khung_gioi_tinh, text='Khác',
                       value=2, variable=chon_gioi_tinh)
rdo_nam.grid(column=0, row=0, sticky=W)
rdo_nu.grid(column=1, row=0, sticky=W)
rdo_khac.grid(column=2, row=0, sticky=W)
Label(window, text="Giới tính").grid(row=d, column=0, sticky=W)
khung_gioi_tinh.grid(row=d, column=1, sticky=W)
d += 1
chon_ngoai_ngu_1 = IntVar()
chon_ngoai_ngu_2 = IntVar()
chon_ngoai_ngu_3 = IntVar()
chuoi_ngoai_ngu_1 = StringVar()
chuoi_ngoai_ngu_2 = StringVar()
chuoi_ngoai_ngu_3 = StringVar()
chuoi_ngoai_ngu_1.set("Anh")
chuoi_ngoai_ngu_2.set("Pháp")
chuoi_ngoai_ngu_3.set("Đức")
khung_ngoai_ngu = Frame(window)
chk_ngoai_ngu_1 = Checkbutton(khung_ngoai_ngu, text=chuoi_ngoai_ngu_1.get(),
                              variable=chon_ngoai_ngu_1, onvalue=True, offvalue=False)
chk_ngoai_ngu_2 = Checkbutton(khung_ngoai_ngu, text=chuoi_ngoai_ngu_2.get(),
                              variable=chon_ngoai_ngu_2, onvalue=True, offvalue=False)
chk_ngoai_ngu_3 = Checkbutton(khung_ngoai_ngu, text=chuoi_ngoai_ngu_3.get(),
                              variable=chon_ngoai_ngu_3, onvalue=True, offvalue=False)
chk_ngoai_ngu_1.grid(column=0, row=0, sticky=W)
chk_ngoai_ngu_2.grid(column=1, row=0, sticky=W)
chk_ngoai_ngu_3.grid(column=2, row=0, sticky=W)
Label(window, text="Ngoại ngữ").grid(row=d, column=0, sticky=W)
khung_ngoai_ngu.grid(row=d, column=1, sticky=W)
d += 1
khung_chuc_nang = Frame(window)
nut_xac_nhan = Button(khung_chuc_nang, text="Xác nhận", command=Xu_ly_xac_nhan)
nut_xac_nhan.grid(row=0, column=0, padx=5)
khung_chuc_nang.grid(row=d, column=1, padx=5, pady=5)
d += 1
lbl_thong_tin = Label(window, justify=LEFT)
lbl_thong_tin.grid(row=d, column=0, columnspan=2, sticky=W)
#
txt_ho.focus()
# mở cửa sổ giao diện
window.mainloop()
