from tkinter import *


def print_max():
    # ham eval(so_a.get()) chuyen kieu du lieu thanh so
    chuoi = 'So lon nhat la: ' + str(max(so_a.get(), so_b.get()))
    ket_qua.configure(text=chuoi)


root = Tk()
root.title('Tim so lon nhat')

Label(root, text='So a').grid(row=0, column=0, sticky=W)

so_a = Entry(root, justify="right")
so_a.grid(row=0, column=1, sticky=W)

Label(root, text='So b').grid(row=1, column=0, sticky=W)

so_b = Entry(root, justify="right")
so_b.grid(row=1, column=1, sticky=W)

khung_chuc_nang = Frame(root)
nut_xac_nhan = Button(khung_chuc_nang, text="Tim max", command=print_max)
nut_xac_nhan.grid(row=0, column=0, padx=5)
khung_chuc_nang.grid(row=2, column=1, padx=5, pady=5,
                     columnspan=2)

ket_qua = Label(root)
ket_qua.grid(row=3, column=0, columnspan=2)

so_a.focus()
root.mainloop()
