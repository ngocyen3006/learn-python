import sqlite3
from function_QLPhim import read_data, them_phim_moi, del_phim

if __name__ == '__main__':

    yeu_cau = 0

    while yeu_cau != 4:
        yeu_cau = int(input('''
Xin hay chon tac vu muon thuc hien:
    1. Xem danh sach phim
    2. Them phim moi
    3. Xoa phim theo ID
    4. Thoat
    '''))

        if yeu_cau == 1:
            read_data(r"QLPhim.db")

        elif yeu_cau == 2:
            ten = input("Nhap ten phim: ")
            nam_sx = input("Nhap nam san xuat: ")
            the_loai = input("Nhap the loai phim: ")
            thoi_luong = int(input("Nhap thoi luong phim: "))
            nuoc_sx = input("Nhap nuoc sx: ")

            them_phim_moi(ten, nam_sx, the_loai, thoi_luong, nuoc_sx)

        elif yeu_cau == 3:
            id = int(input("Ban muon xoa phim co ID nao? "))
            del_phim(id)
