import json


def in_theo_cot(sinh_vien):
    chuoi = sinh_vien["Ma_so"].ljust(10) + \
            sinh_vien["Ho_ten"].ljust(30) + \
            ngay(sinh_vien["Ngay_sinh"]).center(15) + \
            gt(sinh_vien["Gioi_tinh"]).ljust(10) + \
            so_tien(sinh_vien["Hoc_bong"]).rjust(10)
    print(chuoi)


def gt(gioi_tinh):
    s = "Nam"
    if gioi_tinh == 'false':
        s = "Nu"
    return s


def so_tien(so):
    return "{:,.0f} VND".format(so)


def ngay(ngay_sinh):
    s = ngay_sinh.split("-")
    return s[2] + "/" + s[1] + "/" + s[0]


def in_tieu_de():
    chuoi = "Ma_so".ljust(10) + \
            "Ho_ten".ljust(30) + \
            "Ngay_sinh".center(15) + \
            "Gioi_tinh".ljust(10) + \
            "Hoc_bong".rjust(10)
    print(chuoi)


f = open("dang_3_phoi_hop_a.json", "r", encoding="utf-8")
du_lieu = json.load(f)
ma_khoa = du_lieu['Ma_khoa']
ten_khoa = du_lieu['Ten_khoa']
danh_sach = du_lieu['Danh_sach']

print(f"{ten_khoa} - {ma_khoa}")
in_tieu_de()
for sinh_vien in danh_sach:
    in_theo_cot(sinh_vien)
