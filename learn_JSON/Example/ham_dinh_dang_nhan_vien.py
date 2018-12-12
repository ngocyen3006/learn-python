def in_theo_cot(sinh_vien):
    chuoi = sinh_vien["Ma_so"].ljust(10) + \
            sinh_vien["Ho_ten"].ljust(30) + \
            ngay(sinh_vien["Ngay_sinh"]).center(15) + \
            gt(sinh_vien["Gioi_tinh"]).ljust(10) + \
            so_tien(sinh_vien["Hoc_bong"]).rjust(10)
    print(chuoi)


def gt(gioi_tinh):
    s = "Nam"
    if gioi_tinh == False:
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


def in_theo_dong(sinh_vien):
    print(f'Ma so: {sinh_vien["Ma_so"]}')
    print(f'Ho ten: {sinh_vien["Ho_ten"]}')
    print(f'Ngay sinh: {ngay(sinh_vien["Ngay_sinh"])}')
    print(f'Gioi tinh: {gt(sinh_vien["Gioi_tinh"])}')
    print(f'Hoc bong: {so_tien(sinh_vien["Hoc_bong"])}')
    print('\n')
