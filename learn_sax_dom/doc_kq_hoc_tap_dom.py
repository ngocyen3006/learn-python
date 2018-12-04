from xml.dom.minidom import parse


def formatDate(self):
    s = self.split("-")
    return s[2] + '/' + s[1] + '/' + s[0]


xmlDoc = parse("ket_qua_hoc_tap.xml")
root_node = xmlDoc.documentElement

listElement = root_node.getElementsByTagName("HOC_SINH")

for node in listElement:
    print('*' * 30)
    ho_ten = node.getAttribute('Ho_ten')
    ngay_sinh = formatDate(node.getAttribute('Ngay_sinh'))
    print(f"Ho ten: {ho_ten}")
    print(f"Ngay sinh: {ngay_sinh}")

    ket_qua_thi = node.getElementsByTagName("KET_QUA_THI")[0]
    for i in range(4):
        ket_qua = ket_qua_thi.getElementsByTagName("KET_QUA")[i]
        ma_mon = " ".join(ket_qua.getAttribute('Ma_mon').split("_"))
        diem = ket_qua.getAttribute('Diem')
        print(f"{ma_mon}: {diem}")
