class XL_TY_GIA:
    def __init__(self, chuoi_thong_tin):
        cac_thong_tin = chuoi_thong_tin.split(";")
        self.ma = cac_thong_tin[0]
        self.mua_vao = float(cac_thong_tin[1])
        self.ban_ra = float(cac_thong_tin[2])

    def __str__(self):
        ma = self.ma
        mua_vao = "{:,.0f}".format(self.mua_vao)
        ban_ra = "{:,.0f}".format(self.ban_ra)
        chuoi = ma.ljust(10, " ") + mua_vao.rjust(20, " ") + ban_ra.rjust(20, " ")
        return chuoi
