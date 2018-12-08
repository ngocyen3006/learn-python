import xml.dom.minidom as xml

donvi = [{'Ten': 'Phi Quyet Nguyen', 'Gioi_tinh': True, 'Ngay_sinh': '31/08/1973', 'CMND': '060605210',
          'Muc_luong': '5200000', 'Dia_chi': '12 abc daf', 'ID_Donvi': '1'},
         {'Ten': 'Do Son Thuy Trang', 'Gioi_tinh': False, 'Ngay_sinh': '14/03/1979', 'CMND': '083239154',
          'Muc_luong': '8400000', 'Dia_chi': '1 hnj kjo', 'ID_Donvi': '2'},
         {'Ten': 'Trieu Thi Trang Dai', 'Gioi_tinh': False, 'Ngay_sinh': '26/04/1990', 'CMND': '005487440',
          'Muc_luong': '5000000', 'Dia_chi': '8 dfu oen', 'ID_Donvi': '1'},
         {'Ten': 'Bui Nam Quang Vien', 'Gioi_tinh': False, 'Ngay_sinh': '21/05/1993', 'CMND': '092700391',
          'Muc_luong': '5800000', 'Dia_chi': '21 hnr yfc', 'ID_Donvi': '3'},
         {'Ten': 'Tran Tien Quan', 'Gioi_tinh': True, 'Ngay_sinh': '18/02/1994', 'CMND': '011468433',
          'Muc_luong': '5600000', 'Dia_chi': '24 fvg hjk', 'ID_Donvi': '4'},
         {'Ten': 'Le Minh Khang', 'Gioi_tinh': True, 'Ngay_sinh': '28/12/1995', 'CMND': '052250493',
          'Muc_luong': '5200000', 'Dia_chi': '63 kgn cjd', 'ID_Donvi': '5'},
         {'Ten': 'Duong Thanh Binh', 'Gioi_tinh': True, 'Ngay_sinh': '25/04/1996', 'CMND': '013496480',
          'Muc_luong': '5100000', 'Dia_chi': '52 fhk heb', 'ID_Donvi': '4'},
         {'Ten': 'Truong Phuoc Thao Truc', 'Gioi_tinh': False, 'Ngay_sinh': '14/12/1996', 'CMND': '071576262',
          'Muc_luong': '5400000', 'Dia_chi': '54 klg uhn', 'ID_Donvi': '5'},
         {'Ten': 'Mai Dinh Duong', 'Gioi_tinh': True, 'Ngay_sinh': '31/07/1992', 'CMND': '077321551',
          'Muc_luong': '5500000', 'Dia_chi': '12 hnj gvf', 'ID_Donvi': '1'}]

doc = xml.Document()
root = doc.createElement('NHAN_VIEN_S')
root.setAttribute("shelf", "New Arrivals")

doc.appendChild(root)

id = 0
for d in donvi:
    id = id + 1
    ten = d['Ten']
    gt = d['Gioi_tinh']
    ngay_sinh = d['Ngay_sinh']
    cmnd = d['CMND']
    muc_luong = d['Muc_luong']
    dia_chi = d['Dia_chi']
    id_dv = d['ID_Donvi']

    d_node = doc.createElement("NHAN_VIEN")
    root.appendChild(d_node)
    d_node.setAttribute("ID", str(id))
    d_node.setAttribute("Ten", ten)
    d_node.setAttribute("Gioi_tinh", str(gt))
    d_node.setAttribute("Ngay_sinh", ngay_sinh)
    d_node.setAttribute("CMND", cmnd)
    d_node.setAttribute("Muc_luong", muc_luong)
    d_node.setAttribute("Dia_chi", dia_chi)
    d_node.setAttribute("ID_DON_VI", id_dv)

f = open("nhan_vien.xml", "w", encoding="UTF-8")
doc.writexml(f, newl="\n", indent="", addindent="  ", encoding="utf-8")
f.close()
