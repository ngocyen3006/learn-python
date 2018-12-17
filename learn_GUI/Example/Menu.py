from tkinter import *
from tinh_dt_cv_hinh_tron import thuc_hien


def hcn():
    pass


def hinhTron():
    thuc_hien()


window = Tk()
window.title('Menu')
window.geometry('350x450')
#
menubar = Menu(window)
calMenu = Menu(menubar, tearoff=0)

calMenu.add_command(label='Tinh dien tich, chu vi hinh chu nhat', command=hcn)
calMenu.add_command(label='Tinh dien tich, chu vi hinh tron', command=hinhTron)

calMenu.add_separator()

calMenu.add_command(label="Thoat", command=window.quit)
menubar.add_cascade(label='Tinh toan', menu=calMenu)


#
window.config(menu=menubar)
window.mainloop()
