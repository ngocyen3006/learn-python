import json
from ham_dinh_dang_nhan_vien import in_tieu_de, in_theo_cot

f = open("dang_3_phoi_hop_b.json", "r", encoding="utf-8")
du_lieu = json.load(f)

for khoa in du_lieu:
    ma_khoa = khoa['Ma_khoa']
    ten_khoa = khoa['Ten_khoa']
    danh_sach = khoa['Danh_sach']

    print(f"{ten_khoa} - {ma_khoa}")
    in_tieu_de()
    for sinh_vien in danh_sach:
        in_theo_cot(sinh_vien)
    print("\t---------------------\t")
