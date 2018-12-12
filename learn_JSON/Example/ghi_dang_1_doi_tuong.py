import json

sinh_vien = {
    "Ma_so": "C01",
    "Ho_ten": "Mai Thanh Cần",
    "Gioi_tinh": True,
    "Ngay_sinh": "1965-12-24",
    "Hoc_bong": 120000
}
# ghi
ten_tap_tin = "sinh_vien.json"
with open(ten_tap_tin, 'w', encoding="UTF-8") as f:
    json.dump(sinh_vien, f, indent=4)
