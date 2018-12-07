import json
from ham_dinh_dang_nhan_vien import ngay, gt, so_tien

f = open("dang_3_phoi_hop_c.json", "r", encoding="utf-8")
du_lieu = json.load(f)

ma_khoa = du_lieu['Ma_khoa']
ten_khoa = du_lieu['Ten_khoa']
danh_sach = du_lieu['Danh_sach']

print("---------------------------")
print(f"{ten_khoa} - {ma_khoa}")
print("---------------------------")

for sinh_vien in danh_sach:
    ms = sinh_vien["Ma_so"]
    ten = sinh_vien["Ho_ten"]
    ns = ngay(sinh_vien["Ngay_sinh"])
    gioi_tinh = gt(sinh_vien["Gioi_tinh"])
    hoc_bong = so_tien(sinh_vien["Hoc_bong"])

    ds_dt = sinh_vien["Dien_thoai"]
    kq_ht = sinh_vien['Ket_qua_hoc_tap']

    print(f"\tSinh vien: {ms} --- {ten}")
    print(f"\t- Ngay sinh: {ns}")
    print(f"\t- Gioi tinh: {gioi_tinh}")
    print(f"\t- Hoc bong: {hoc_bong}")

    if ds_dt == []:
        print("\tSo dien thoai: Khong co")
    else:
        dt = "\tSo dien thoai: "
        for sdt in ds_dt:
            dt = dt + sdt + " - "
        print(dt[:(len(dt) - 2)])

    for kq in kq_ht:
        mon_hoc = kq["Ma_mon"]
        diem = kq['Diem']
        print(f"\tMon hoc: {mon_hoc} - Diem thi: {diem}")

    print('*-----' * 5)
