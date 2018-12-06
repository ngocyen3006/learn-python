class DonVi:
    def __init__(self, iddv, ten):
        self.iddv = iddv
        self.ten = ten

    def __str__(self):
        return f"{self.iddv} - {self.ten}"


class NhanVien:
    def __init__(self, idnv, ten, gt, ns, cmnd, luong, dia_chi, iddv):
        self.idnv = idnv
        self.ten = ten
        self.gt = gt
        self.ns = ns
        self.cmnd = cmnd
        self.luong = luong
        self.dia_chi = dia_chi
        self.iddv = iddv

    def in_thong_tin(self):
        print(f"{self.idnv} - {self.ten} - {self.cmnd}")
