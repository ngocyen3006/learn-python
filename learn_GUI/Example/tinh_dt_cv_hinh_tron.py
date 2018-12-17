from tkinter import *


def Xu_ly_Tinh_toan():
    r = float(ban_kinh.get())
    chu_vi = 2*3.1416*r
    dien_tich = 3.1416*r*r
    kq_dien_tich.configure(text="Diện tích: %.4f" % (dien_tich))
    kq_chu_vi.configure(text="Chu vi: %.4f" % (chu_vi))


def thuc_hien():
    global ban_kinh, kq_dien_tich, kq_chu_vi
    # tạo cửa sổ giao diện
    window = Tk()
    window.title("Tính diện tích và chu vi hình tròn")
    window.geometry("300x100")
    # tạo các điều khiển
    nhac_1 = Label(window, text="Bán kính:")
    ban_kinh = Entry(window, width=20)
    kq_dien_tich = Label(window, fg="red")
    kq_chu_vi = Label(window, fg="red")
    tinh_toan = Button(window, text="Tính toán", command=Xu_ly_Tinh_toan)
    # định vị trí các điều khiển
    nhac_1.grid(row=0, column=0, sticky=W)
    ban_kinh.grid(row=0, column=1)
    kq_dien_tich.grid(row=1, column=0, columnspan=2, sticky=W)
    kq_chu_vi.grid(row=2, column=0, columnspan=2, sticky=W)
    tinh_toan.grid(row=3, column=1, sticky=E)
    #
    ban_kinh.focus()
    # mở cửa sổ giao diện
    window.mainloop()
