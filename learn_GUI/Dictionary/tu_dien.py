from tkinter import *
from tkinter import font
import sqlite3
from pprint import pprint


def read_db_file():
    conn = sqlite3.connect(r"qltratu.db")
    conn.row_factory = sqlite3.Row

    sql = "select * from TU_DIEN order by tu"
    cur = conn.execute(sql)
    row = cur.fetchall()
    dictionary = {}
    for item in row:
        dictionary.update({item['tu']: item['nghia']})

    conn.close()
    return dictionary


def create_window():
    window = Tk()

    window.title('Tu dien')

    Label(window, text="Tu", font=font.Font(
        size=11, weight='bold')).grid(row=0, column=0, sticky=W)
    Label(window, text="Nghia", font=font.Font(
        size=11, weight='bold')).grid(row=0, column=1, sticky=W)

    dictionary = read_db_file()

    i = 1
    for item in dictionary.keys():
        Label(window, text=item, fg='blue', font=(
            'Helvetica', 10)).grid(row=i, column=0, sticky=W)
        Label(window, text=dictionary[item]).grid(row=i, column=1, sticky=W)
        i += 1

    window.mainloop()


if __name__ == '__main__':
    create_window()
