import json
from ham_dinh_dang_nhan_vien import in_theo_cot, in_tieu_de

f = open("dang_2_danh_sach.json", "r", encoding="utf-8")
danh_sach = json.load(f)

in_tieu_de()
for sinh_vien in danh_sach:
    in_theo_cot(sinh_vien)

f.close()
