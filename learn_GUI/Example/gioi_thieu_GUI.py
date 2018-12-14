import tkinter
from tkinter.constants import RAISED
from tkinter import messagebox


def in_thong_bao():
    messagebox.showinfo("Chao", "Xin chao cac ban")


# tao cua so ung dung
top = tkinter.Tk()
top.title('Window')
top.geometry('250x250')

# resizable: cho nguoi dung thay doi kich thuoc,
# 0: False, 1: True
top.resizable(0, 0)

# tao button
# underline = vi tri chuoi (dung de lam shortcut)
# command = in_thong_bao (khi an vao nut "Hello" se hien ra messagebox cua ham in_thong_bao)
button1 = tkinter.Button(top, text='Hello', width=20,
                         borderwidth=2, height=2, underline=0, command=in_thong_bao)

# bg = mau nen, fg = mau chu cua button
# command = top.destroy de tat cua so ung dung
button2 = tkinter.Button(top, text='Quit', width=10,
                         borderwidth=2, height=2, underline=1, bg="blue", fg="green", command=top.destroy)

# tao label
# RAISED de hien khung, nhin giong button
# lbl = tkinter.Label(top, text="Ho ten", relief=RAISED)
lbl = tkinter.Label(top, text="Ho ten: ")  # text cu the

# neu text khong cu the, muon thay doi thi dung bien
# var = tkinter.StringVar()
# var.set("Ho ten: ")


button1.pack()  # dung hien button
button2.pack()
lbl.pack(side="left")  # side="left" canh trai

# top.bind('<Alt_L><h>', lambda e: click())
top.mainloop()  # dung hien thi cua so ung dung
