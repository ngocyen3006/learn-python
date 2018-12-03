import json

f = open("dang_1_doi_tuong.json", "r", encoding="utf-8")
sinh_vien = json.load(f)
ma_so = sinh_vien["Ma_so"]
ho_ten = sinh_vien["Ho_ten"]
print(ma_so)
print(ho_ten)
f.close()
