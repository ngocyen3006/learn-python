import xml.dom.minidom as xml

danh_sach = [
    {'Ten': 'Tieng chim hot trong bui man gai',
     'Nam_san_xuat': '1982',
     'The_loai': 'Tinh cam',
     'Dinh_dang': 'DVD'},
    {'Ten': 'Chien tranh va hoa binh',
     'Nam_san_xuat': '1981',
     'The_loai': 'Tinh cam, chien tranh',
     'Dinh_dang': 'DVD'},
    {'Ten': 'Nguoi dep va quai vat',
     'Nam_san_xuat': '1990',
     'The_loai': 'Tinh cam, hoat hinh',
     'Dinh_dang': 'VHS'},

]

Tai_lieu = xml.Document()
Nut_goc = Tai_lieu.createElement('DANH_SACH')
Tai_lieu.appendChild(Nut_goc)

for phim in danh_sach:
    # doc thong tin
    ten = phim['Ten']
    nam_san_xuat = phim['Nam_san_xuat']
    the_loai = phim['The_loai']
    dinh_dang = phim['Dinh_dang']

    # tao nut, tao cac thuoc tinh, tao van ban cho nut
    Nut_phim = Tai_lieu.createElement("PHIM")
    Nut_goc.appendChild(Nut_phim)
    Nut_phim.setAttribute("Ten", ten)
    Nut_phim.setAttribute("Nam_san_xuat", nam_san_xuat)

    NUt_the_loai = Tai_lieu.createElement('The_loai')
    Nut_phim.appendChild(NUt_the_loai)
    NUt_the_loai.appendChild(Tai_lieu.createTextNode(the_loai))

    Nut_dinh_dang = Tai_lieu.createElement('Dinh_dang')
    Nut_phim.appendChild(Nut_dinh_dang)
    Nut_dinh_dang.appendChild(Tai_lieu.createTextNode(dinh_dang))

f = open("phim1.xml", "w", encoding="utf-8")
Tai_lieu.writexml(f, newl="\n", indent="", addindent="  ", encoding="utf-8")
f.close()
