# Cau 1 Cau 2
import json
import datetime


class SINH_VIEN:
    def __init__(self, id, ho_ten, ngay_sinh, gioi_tinh, diem_trung_binh, ma_khoa):
        self.id = id
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.gioi_tinh = gioi_tinh
        self.diem_trung_binh = diem_trung_binh
        self.ma_khoa = ma_khoa

    def in_thong_tin(self):
        id = self.id
        ho_ten = self.ho_ten
        ngay_sinh = format_ngay_sinh(self.ngay_sinh)
        gioi_tinh = format_gioi_tinh(self.gioi_tinh)
        diem_tb = f"{self.diem_trung_binh:.1f}"
        khoa_hoc = khoa(self.ma_khoa)
        xep_loai = self.xep_loai_hoc_tap()

        chuoi = str(id).ljust(4) + "| " + ho_ten.ljust(25) + \
                "| " + ngay_sinh.ljust(15) + "| "
        chuoi += gioi_tinh.ljust(10) + "| " + str(diem_tb).ljust(10) + "| "
        chuoi += khoa_hoc.ljust(10) + "| " + xep_loai.ljust(10)
        print(chuoi)
        print("-" * 104)

    def tinh_tuoi(self):
        currentYear = datetime.date.today().year
        return currentYear - self.lay_nam_sinh()

    def xep_loai_hoc_tap(self):
        if self.diem_trung_binh >= 8.0:
            return "Giỏi"
        if self.diem_trung_binh >= 6.5:
            return "Khá"
        if self.diem_trung_binh >= 5.0:
            return "Trung Bình"
        return "Yếu"

    def lay_nam_sinh(self):
        return int(self.ngay_sinh.split("-")[0])


def in_tieu_de():
    chuoi = "ID".ljust(4) + "| " + "Họ tên".ljust(25) + \
            "| " + "Ngày sinh".ljust(15) + "| "
    chuoi += "Giới tính".ljust(10) + "| " + "Điểm TB".ljust(10) + "| "
    chuoi += "Mã khoa".ljust(10) + "| " + "Xếp loại".ljust(10)
    print(chuoi)
    print("-" * 104)


def format_gioi_tinh(gioi_tinh):
    if gioi_tinh == 1:
        return "Nam"
    if gioi_tinh == 0:
        return "Nữ"
    return "Khác"


def khoa(ma_khoa):
    if ma_khoa == "TO":
        return "Khoa Toán"
    return "Khoa Lý"


def format_ngay_sinh(ngay_sinh):
    ngay_sinh = ngay_sinh.split("-")
    return ngay_sinh[-1] + "/" + ngay_sinh[1] + "/" + ngay_sinh[0]


def khoi_tao_danh_sach_sinh_vien():
    danh_sach_sinh_vien = []
    f = open("SINH_VIEN.json", "r", encoding="utf-8")
    data = json.load(f)
    for sinh_vien in data:
        id = sinh_vien['id']
        ho_ten = sinh_vien['ho_ten']
        ngay_sinh = sinh_vien['ngay_sinh']
        gioi_tinh = sinh_vien['gioi_tinh']
        diem_trung_binh = sinh_vien['diem_trung_binh']
        ma_khoa = sinh_vien['ma_khoa']
        danh_sach_sinh_vien.append(
            SINH_VIEN(id, ho_ten, ngay_sinh, gioi_tinh, diem_trung_binh, ma_khoa))
    return danh_sach_sinh_vien


def in_danh_sach_sinh_vien_theo_khoa(ma_khoa):
    danh_sach_sinh_vien = khoi_tao_danh_sach_sinh_vien()
    kq = list(filter(lambda x: x.ma_khoa == ma_khoa, danh_sach_sinh_vien))
    khoa_hoc = khoa(ma_khoa)
    for sinh_vien in kq:
        sinh_vien.in_thong_tin()
    pass


def in_sinh_vien(id):
    danh_sach_sinh_vien = khoi_tao_danh_sach_sinh_vien()
    kq = list(filter(lambda x: x.id == id, danh_sach_sinh_vien))
    print("=" * 30)
    print(f"Sinh viên có {id} là: ")
    for sinh_vien in kq:
        sinh_vien.in_thong_tin()
    pass


if __name__ == '__main__':
    print('\n DANH SACH SINH VIEN')
    danh_sach_sinh_vien = khoi_tao_danh_sach_sinh_vien()
    in_tieu_de()
    for sinh_vien in danh_sach_sinh_vien:
        sinh_vien.in_thong_tin()

    print("\nDANH SACH SINH VIEN KHOA TOAN")
    in_tieu_de()
    in_danh_sach_sinh_vien_theo_khoa("TO")

    in_sinh_vien(1)
