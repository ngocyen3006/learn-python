from tkinter import *
from tkinter.constants import BOTH, YES
from tkinter import font


def photo(year):
    list_hinh = ['than.gif', 'dau.gif', 'tuat.gif', 'hoi.gif', 'ti.gif', 'suu.gif', 'dan.gif', 'meo.gif', 'thin.gif',
                 'ty.gif', 'ngo.gif', 'mui.gif']
    return list_hinh[year % 12]


def can(year):
    list_can = ['Canh', 'Tan', 'Nham', 'Quy', 'Giap', 'At', 'Binh', 'Dinh', 'Mau', 'Ky']
    return list_can[year % 10]


def chi(year):
    list_chi = ['Than', 'Dau', 'Tuat', 'Hoi', 'Ty', 'Suu', 'Dan', 'Mao', 'Thin', 'Ty', 'Ngo', 'Mui']
    return list_chi[year % 12]


def can_chi():
    year = int(_year.get())
    canChi = can(year) + " " + chi(year)
    image = photo(year)

    lunarYear = Toplevel()

    # Title
    lunarYear.title('Calculate ' + str(year))

    # Size
    lunarYear.geometry("200x150")
    lunarYear.resizable(1, 1)

    # PhotoImage
    canvas = Canvas(lunarYear, width=64, height=64)
    canvas.pack(expand=YES, fill=BOTH)
    gif = PhotoImage(file=image)
    canvas.create_image(50, 70, image=gif, anchor=W)
    canvas.gif = gif

    # Label result
    result = Label(lunarYear, text=canChi, font=font.Font(size=14, weight='bold'))
    result.pack()


def makeGUI():
    global _year
    root = Tk()
    # Title
    root.title('Lunar year')

    # Size
    root.geometry("200x100")
    root.resizable(1, 1)

    # Label
    input_year = Label(root, text='Input Year')
    input_year.pack()

    # Entry
    _year = Entry(root)
    _year.pack()

    # Button
    Cal = Button(root, text='Tinh', command=can_chi)
    Cal.pack()

    root.mainloop()


if __name__ == '__main__':
    makeGUI()
