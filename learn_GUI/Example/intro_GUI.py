import tkinter
from tkinter.constants import LEFT, END, BOTTOM
from tkinter import messagebox


def welcome():
    name = 'Hello ' + E1.get()
    messagebox.showinfo('Hello', name)


root = tkinter.Tk()
root.title('What is your name?')
# root.geometry("300x100")

# padx, pady la do dan (khoang cach) chieu rong va chieu cao,
# cua label (entry va button dung duoc)
# side = LEFT (canh trai va nut hoac entry phia sau cung dong voi no)
L1 = tkinter.Label(root, text='Input Name: ')
L1.pack(side=LEFT, padx=10, pady=30)

E1 = tkinter.Entry(root, bd=0)
E1.pack(side=LEFT)
E1.insert(END, 'Input here')

B = tkinter.Button(root, text='Hello', command=welcome)
B.pack(side=LEFT)
# B.pack()

button2 = tkinter.Button(root, text='Quit', width=10,
                         borderwidth=2, height=2, underline=1, bg="blue", fg="green", command=root.destroy)
button2.pack(side=LEFT)

root.mainloop()
