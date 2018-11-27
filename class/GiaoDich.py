class GiaoDich:
    def __init__(self, ma_giao_dich, ngay, so_luong, don_gia, loai):
        self.ma_giao_dich = ma_giao_dich
        self.ngay = ngay
        self.don_gia = don_gia
        self.so_luong = so_luong
        self.loai = loai

    def thanh_tien(self):
        return self.so_luong * self.don_gia

    def in_giao_dich(self, loai_giao_dich=''):
        print('In thong tin'.center(30, '-'))
        print(f"Ma GD {loai_giao_dich}: {self.ma_giao_dich}")
        print(f"Ngay: {self.ngay}")
        print(f"Loai: {self.loai}")
        print(f"So luong: {self.so_luong}")
        print(f"Don gia: {self.don_gia:,.0f}")
        print(f"Thanh tien: {self.thanh_tien():,.0f}")


class GiaoDichTienTe(GiaoDich):
    def __init__(self, ma_giao_dich, ngay, so_luong, ty_gia, loai_tien, mua_ban):
        GiaoDich.__init__(self, ma_giao_dich, ngay, so_luong, ty_gia, loai_tien)
        self.mua_ban = mua_ban

    def thanh_tien(self):
        if self.mua_ban:
            return GiaoDich.thanh_tien(self)
        return GiaoDich.thanh_tien(self) * 1.05

    def in_giao_dich(self):
        mua_ban = 'ban'
        if self.mua_ban == 1:
            mua_ban = 'mua'
        GiaoDich.in_giao_dich(self, mua_ban)


if __name__ == '__main__':
    print("Quan ly giao dich:".center(30, '-'))
    tong_luong_vang = 0
    tong_tien_vang = 0
    tong_luong_tien = 0
    tong_tien = 0
    loop = 1
    while loop > 0:
        ma_giao_dich = input("Nhap ma GD: ")
        ngay = input("Nhap ngay GD: ")
        so_luong = int(input('Nhap so luong: '))
        loai_GD = int(input("Chon loai GD: 1: Vang, 2: Tien te: "))
        if loai_GD == 1:
            loai_vang = input('Chon loai: 18k/ 24k/ 9999: ')
            don_gia = int(input('Nhap don gia: '))
            res = GiaoDich(ma_giao_dich, ngay, so_luong, don_gia, loai_vang)
            res.in_giao_dich()
            tong_luong_vang += so_luong
            print(f'Tong so luong: {tong_luong_vang}')
            tong_tien_vang += res.thanh_tien()
            print(f'Tong so tien: {tong_tien_vang:,.0f}')
        else:
            loai_tien = input('Chon loai: USD/ EUR/ AUD: ')
            ty_gia = int(input('Nhap ty gia: '))
            mua_ban = int(input('Ban mua hay ban? 1: mua, 0: ban: '))
            res = GiaoDichTienTe(ma_giao_dich, ngay, so_luong, ty_gia, loai_tien, mua_ban)
            res.in_giao_dich()
            tong_luong_tien += so_luong
            print(f'Tong so luong: {tong_luong_tien}')
            tong_tien += res.thanh_tien()
            print(f'Tong so tien: {tong_tien:,.0f}')

        print(''.center(30, '-'))
        loop = int(input('Ban muon tiep tuc giao dich? 1: Co, 0: Khong '))
