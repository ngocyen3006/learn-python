from tkinter import *


def Xu_ly_Tinh_tong():
    a = int(so_1.get())
    b = int(so_2.get())
    s = a + b
    so_tong.configure(text="Tổng là: "+str(s))


# tạo cửa sổ giao diện
window = Tk()
window.title("Tính tổng hai số")
window.geometry("300x100")
# tạo các điều khiển
nhac_1 = Label(window, text="Số thứ nhất:")
so_1 = Entry(window, width=20)
nhac_2 = Label(window, text="Số thứ hai:")
so_2 = Entry(window, width=20)
so_tong = Label(window, fg="red")
tinh_tong = Button(window, text="Tính tổng", command=Xu_ly_Tinh_tong)
# định vị trí các điều khiển
nhac_1.grid(row=0, column=0, sticky=W)
so_1.grid(row=0, column=1)
nhac_2.grid(row=1, column=0, sticky=W)
so_2.grid(row=1, column=1)
so_tong.grid(row=2, column=0, columnspan=2)
tinh_tong.grid(row=3, column=1, sticky=E)
#
so_1.focus()
# mở cửa sổ giao diện
window.mainloop()
