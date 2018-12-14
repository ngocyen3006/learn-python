from tkinter import *


def can(year):
    list_can = ['Canh', 'Tan', 'Nham', 'Quy', 'Giap', 'At', 'Binh', 'Dinh', 'Mau', 'Ky']
    return list_can[year % 10]


def chi(year):
    list_chi = ['Than', 'Dau', 'Tuat', 'Hoi', 'Ty', 'Suu', 'Dan', 'Mao', 'Thin', 'Ty', 'Ngo', 'Mui']
    return list_chi[year % 12]


def can_chi():
    year = int(_year.get())
    canChi = can(year) + " " + chi(year)

    lunarYear = Toplevel()

    # Title
    lunarYear.title('Calculate ' + str(year))

    # Size
    lunarYear.geometry("200x150")
    lunarYear.resizable(1, 1)

    # Label result
    result = Label(lunarYear, text=canChi)
    result.pack()


if __name__ == '__main__':
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
