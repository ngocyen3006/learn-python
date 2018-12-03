import json

danh_sach_sinh_vien = [
    {
        "Ma_so": "C01",
        "Ho_ten": "Mai Thanh Cần",
        "Gioi_tinh": True,
        "Ngay_sinh": "1965-12-24",
        "Hoc_bong": 120000
    },
    {
        "Ma_so": "C02",
        "Ho_ten": "Nguyễn Ngọc Thanh Thảo",
        "Gioi_tinh": False,
        "Ngay_sinh": "1989-12-01",
        "Hoc_bong": 150000
    },
    {
        "Ma_so": "C03",
        "Ho_ten": "Đặng Bình Phương",
        "Gioi_tinh": True,
        "Ngay_sinh": "1977-10-24",
        "Hoc_bong": 150000
    },
    {
        "Ma_so": "C04",
        "Ho_ten": "Chu Phạm Tiến Luật",
        "Gioi_tinh": True,
        "Ngay_sinh": "1988-03-15",
        "Hoc_bong": 100000
    }
]
# ghi
ten_tap_tin = "danh_sach_sinh_vien.json"
with open(ten_tap_tin, 'w', encoding="UTF-8") as f:
    json.dump(danh_sach_sinh_vien, f, indent=4)
