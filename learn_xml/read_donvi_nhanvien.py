from xml.dom.minidom import parse


def in_don_vi():
    print('--- Danh sach don vi ---')
    xmlDoc = parse("donvi.xml")
    root_node = xmlDoc.documentElement

    listElement = root_node.getElementsByTagName("DON_VI")

    for node in listElement:
        id = node.getAttribute('ID')
        name = node.getAttribute('Ten')
        print(f"{id} - {name}")


def dem_gioi_tinh(gt):
    if gt == "true":
        return 1
    return 0


def in_nhan_vien(ID_DV):
    print('--- Ket qua---')
    xmlDoc = parse("nhan_vien.xml")
    root_node = xmlDoc.documentElement

    listElement = root_node.getElementsByTagName("NHAN_VIEN")
    count = 0
    count_gt = 0
    for node in listElement:
        if int(node.getAttribute('ID_DON_VI')) == ID_DV:
            count_gt += dem_gioi_tinh(node.getAttribute('Gioi_tinh'))
            count += 1
            id = node.getAttribute('ID')
            name = node.getAttribute('Ho_ten')
            cmnd = node.getAttribute('CMND')
            print(f"{id} - {name} - {cmnd}")
    print(f"Tong so NV: {count}- Trong do {count_gt} nam va {count - count_gt} nu")


if __name__ == '__main__':
    in_don_vi()
    dv = int(input('Ban muon xem thong ke don vi nao? (nhap so)'))
    in_nhan_vien(dv)
