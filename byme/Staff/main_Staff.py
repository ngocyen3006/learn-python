import in_tat_ca_nv
import them_phong_ban
import them_nhan_vien
import tim_kiem_nhan_vien
import sua_nhan_vien
from tkinter import *


def main():
    window = Tk()
    window.title('Menu')
    window.geometry("270x250")

    Label(window, text='Ấn vào chọn lựa bạn muốn thực hiện', font=("bold"), anchor=CENTER).grid(pady=5)

    menubar = Frame(window)
    list_chon = ['In danh sách nhân viên', 'Thêm phòng ban mới', 'Thêm nhân viên mới', 'Tìm kiếm nhân viên',
                 'Chỉnh sửa thông tin nhân viên', 'Thoát']
    list_xu_ly = [in_tat_ca_nv.makeGUI, them_phong_ban.makeGUI_addPB, them_nhan_vien.GUI_add_NV,
                  tim_kiem_nhan_vien.GUI_tim_kiem, sua_nhan_vien.GUI_update, window.quit]
    for i in range(6):
        Button(menubar, text=list_chon[i], command=list_xu_ly[i]).grid(row=i, sticky=W + E, pady=3)

    menubar.grid()

    window.config(menu=menubar)
    window.mainloop()


if __name__ == '__main__':
    main()
