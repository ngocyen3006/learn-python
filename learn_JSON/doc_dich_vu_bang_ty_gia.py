import requests
import json
import xu_ly_ty_gia

# đọc bảng tỷ giá từ dịch vụ
r = requests.get("http://dongabank.com.vn/exchange/export")
data = r.content  # dữ liệu thô nhị phân
chuoi = str(data)  # chuyển sang kiểu chuỗi

# lấy đúng dữ liệu chuỗi json
bat_dau = 3
ket_thuc = len(chuoi) - 1
chuoi_ty_gia = chuoi[bat_dau:ket_thuc - 1]
# chuyển kiểu chuỗi sang kiểu json
danh_sach_ty_gia = json.loads(chuoi_ty_gia)
danh_sach_ty_gia = danh_sach_ty_gia["items"]

# đọc biến danh sách để khởi tạo danh sách đối tượng (biến bang_ty_gia)
bang_ty_gia = []
for ty_gia in danh_sach_ty_gia:
    if (ty_gia["muatienmat"].strip() != ""):
        chuoi_thong_tin = ty_gia["type"]
        chuoi_thong_tin += ";" + ty_gia["muatienmat"]
        chuoi_thong_tin += ";" + ty_gia["bantienmat"]
        doi_tuong_ty_gia = xu_ly_ty_gia.XL_TY_GIA(chuoi_thong_tin)
        bang_ty_gia.append(doi_tuong_ty_gia)

# đọc danh sách đối tượng (biến bang_ty_gia) để in
# in tiêu đề
print("Ngoại tệ".ljust(10, " ") + "Mua vào".rjust(20, " ") + "Bán ra".rjust(20, " "))
for ty_gia in bang_ty_gia:
    print(ty_gia)
