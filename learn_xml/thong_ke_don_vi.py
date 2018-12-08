from xml.dom.minidom import parse
from class_don_vi import DonVi, NhanVien


def danh_sach_dv(ds):
    xmlDoc = parse("donvi.xml")
    root_node = xmlDoc.documentElement

    listElement = root_node.getElementsByTagName("DON_VI")

    for node in listElement:
        id = node.getAttribute('ID')
        name = node.getAttribute('Ten')

        ds.append(DonVi(id, name))
    return ds


def ds_nv(ds):
    xmlDoc = parse("nhan_vien.xml")
    root_node = xmlDoc.documentElement

    listElement = root_node.getElementsByTagName("NHAN_VIEN")
    for node in listElement:
        id = node.getAttribute('ID')
        name = node.getAttribute('Ho_ten')
        cmnd = node.getAttribute('CMND')
        gt = node.getAttribute('Gioi_tinh')
        ns = node.getAttribute('Ngay_sinh')
        luong = node.getAttribute('Muc_luong')
        dc = node.getAttribute('Dia_chi')
        iddv = node.getAttribute('ID_DON_VI')

        ds.append(NhanVien(id, name, gt, ns, cmnd, luong, dc, iddv))
    return ds


def gioi_tinh(gt):
    if gt == "true":
        return 1
    return 0


def thong_ke_dv(iddv, dsnv):
    count = 0
    count_gt = 0
    for e in dsnv:
        if e.iddv == iddv:
            count += 1
            count_gt += gioi_tinh(e.gt)
            e.in_thong_tin()
    print(f"Tong NV: {count} - Trong do {count_gt} nam va {count - count_gt} nu")


def tim_kiem_nv(ten, dsnv):
    for e in dsnv:
        if ten in e.ten:
            e.in_thong_tin()


if __name__ == '__main__':
    print('--- Danh sach don vi ---')
    for dsdv in danh_sach_dv([]):
        print(dsdv)
    sdv = input('Ban muon xem thong ke don vi nao? (nhap so)')
    print('--- Ket qua thong ke ---')
    thong_ke_dv(sdv, ds_nv([]))
    print('------------------------------------------')
    ten = input('Nhap ten NV can tim:')
    print('--- Ket qua tim kiem ---')
    tim_kiem_nv(ten, ds_nv([]))
