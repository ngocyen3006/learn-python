from tkinter import *
from tkinter import messagebox
import sqlite3
import re
from SINH_VIEN import SINH_VIEN
from SINH_VIEN import format_gioi_tinh, format_ngay_sinh, khoa


def them_moi(ten, ns, gt, diem_tb, ma_khoa):
    ten = ten.strip()
    if ten == "":
        messagebox.showinfo("Thông báo", "Bạn chưa nhập họ tên!")
        return
    if re.match(r"\d\.\d", str(diem_tb)) == None:
        messagebox.showinfo("Thông báo", "Bạn nhập sai điểm trung bình!")
        return

    conn = sqlite3.connect(r"QLSinhVien.db")
    conn.execute("insert into SINH_VIEN(ho_ten,ngay_sinh,gioi_tinh,diem_trung_binh,ma_khoa) values(?,?,?,?,?)",
                 (ten, ns, gt, diem_tb, ma_khoa))
    conn.commit()
    conn.close()
    messagebox.showinfo("Thông báo", "Ghi thành công")


def them_sv():
    ten = ho_ten.get()
    ngay = ns.get()
    gioi_tinh = gt.get()
    diem_tb = diem_trung_binh.get()

    tuple_item = ma_khoa.curselection()
    khoa = ma_khoa.get(tuple_item)

    them_moi(ten, ngay, gioi_tinh, diem_tb, khoa)


def GUI_add_SV():
    global ho_ten, ns, gt, diem_trung_binh, ma_khoa

    window = Tk()
    window.title('Thêm sinh viên')
    window.geometry("400x200")

    label = ['Họ tên', 'Ngày sinh', 'Giới tính', 'Điểm TB', 'Mã Khoa']
    for i in range(len(label)):
        Label(window, text=label[i]).grid(row=i, column=0, sticky=W, padx=5)

    r = 0
    ho_ten = Entry(window, width=40)
    ho_ten.grid(row=r, column=1, sticky=W)

    r += 1
    ns = Entry(window, width=20)
    ns.grid(row=r, column=1, sticky=W)

    r += 1
    gt = IntVar()
    gt.set(1)
    khung_gt = Frame(window)
    gt_nam = Radiobutton(khung_gt, text='Nam', value=1, variable=gt)
    gt_nam.grid(row=0, column=0, sticky=W)

    gt_nu = Radiobutton(khung_gt, text='Nữ', value=0, variable=gt)
    gt_nu.grid(row=0, column=1, sticky=W)

    gt_khac = Radiobutton(khung_gt, text='Khác', value=2, variable=gt)
    gt_khac.grid(row=0, column=2, sticky=W)

    khung_gt.grid(row=r, column=1, sticky=W)

    r += 1
    diem_trung_binh = Entry(window, width=20)
    diem_trung_binh.grid(row=r, column=1, sticky=W)

    r += 1
    ds_ma_khoa = ["TO", "LY"]
    ma_khoa = Listbox(window, selectmode=SINGLE, height=len(ds_ma_khoa))
    for khoa in ds_ma_khoa:
        ma_khoa.insert(END, khoa)

    ma_khoa.grid(row=r, column=1, sticky=W)

    r += 1
    them_moi = Button(window, text="Ghi", command=them_sv)
    them_moi.grid(row=r, column=1, padx=60, sticky=W)

    window.mainloop()


def read_file_SV_db():
    data = []
    conn = sqlite3.connect("QLSinhVien.db")
    conn.row_factory = sqlite3.Row
    sinh_vien = conn.execute("SELECT * from SINH_VIEN")
    sinh_vien = sinh_vien.fetchall()
    for sv in sinh_vien:
        element = SINH_VIEN(sv['ID'], sv['ho_ten'], sv['ngay_sinh'], sv['gioi_tinh'],
                            sv['diem_trung_binh'], sv['ma_khoa'])
        data.append(element)
    conn.close()
    return data


def GUI_display_data():
    window = Tk()
    window.title('Danh sách sinh viên')
    window.geometry("700x500")

    title = ['ID', 'Họ tên', 'Ngày sinh', 'Giới tính', 'Điểm TB', 'Mã Khoa', 'Xếp loại']

    for i in range(len(title)):
        Label(window, text=title[i], font=("Helvetica", "12", "bold")).grid(row=0, column=i)

    danh_sach_sv = read_file_SV_db()
    x = 5
    y = 3
    r = 0

    for sv in danh_sach_sv:
        r += 1
        info_list = [sv.id, sv.ho_ten, format_ngay_sinh(sv.ngay_sinh), format_gioi_tinh(sv.gioi_tinh),
                     sv.diem_trung_binh, khoa(sv.ma_khoa), sv.xep_loai_hoc_tap()]
        width_list = [5, 20, 10, 8, 12, 10, 12]

        for c in range(len(width_list)):
            Label(window, text=info_list[c], relief=RAISED, anchor=W, width=width_list[c]).grid(row=r, column=c, padx=x,
                                                                                                pady=y, sticky=W + E)

    window.mainloop()


def menu():
    print('Bạn muốn thực hiện thao tác nào?')
    menu = ''' 1. Xem danh sách sinh viên 
    2. Thêm sinh viên mới '''
    menu = ''.join(menu.split('   '))
    print(menu)

    choice = int(input('>> '))
    return choice


if __name__ == '__main__':
    choose = menu()
    if choose == 1:
        GUI_display_data()
    elif choose == 2:
        GUI_add_SV()
    else:
        pass
