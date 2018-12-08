from xml.dom.minidom import Document
import xml.dom.minidom
import os.path


class CD:
    def __init__(self, ten, ca_sy, so_bai_hat, gia_thanh):
        self.ten = ten
        self.ca_sy = ca_sy
        self.so_bai_hat = so_bai_hat
        self.gia_thanh = gia_thanh


def make_xml(ten_file, cd):
    if os.path.isfile(ten_file):
        doc = xml.dom.minidom.parse(ten_file)
        root_xml = doc.documentElement
    else:
        doc = Document()
        root_xml = doc.createTextNode('cds')
        doc.appendChild(root_xml)

    child_node = doc.createElement('cd')
    child_node.setAttribute('ten', cd.ten)
    root_xml.appendChild(child_node)

    singer = doc.createElement("ca_sy")
    child_node.appendChild(singer)
    singer.appendChild(doc.createTextNode(cd.ca_sy))

    quan = doc.createElement("so_bai_hat")
    child_node.appendChild(quan)
    quan.appendChild(doc.createTextNode(cd.so_bai_hat))

    price = doc.createElement("gia_thanh")
    child_node.appendChild(price)
    price.appendChild(doc.createTextNode(cd.gia_thanh))

    return doc


def read_xml(ten_file):
    print('---- CD ----')
    DomTree = xml.dom.minidom.parse(ten_file)
    root_xml = DomTree.documentElement

    cds = root_xml.getElementsByTagName('cd')

    for cd in cds:
        if cd.hasAttribute('ten'):
            print(f"Ten cd: {cd.getAttribute('ten')}")

        ca_sy = cd.getElementsByTagName('ca_sy')[0]
        print(f"Ca sy: {ca_sy.childNodes[0].data}")

        so_bai_hat = cd.getElementsByTagName('so_bai_hat')[0]
        print(f"So bai hat: {so_bai_hat.childNodes[0].data}")

        gia_thanh = cd.getElementsByTagName('gia_thanh')[0]
        print(f"Gia: {gia_thanh.childNodes[0].data}")
        print('-----------------------')
    return


if __name__ == '__main__':
    loop = 1
    while loop == 1:
        i = int(input('Ban muon lam gi? 1: Them CD, 2: Xem danh sach CD  '))
        if i == 1:
            ten = input('Nhap ten CD:  ')
            ca_sy = input('Nhap ten ca sy:  ')
            so_bai_hat = input('Nhap so bai hat:  ')
            gia_thanh = input('Nhap gia thanh:  ')

            cd = CD(ten, ca_sy, so_bai_hat, gia_thanh)

            make_xml("cd.xml", cd).writexml(open("cd.xml", "w", encoding="utf=8"), newl="\n", indent="",
                                            addindent="\t", encoding="utf-8")
            print('Da them CD')
        else:
            read_xml("cd.xml")
        loop = int(input('Ban muon tiep tuc khong? Co: 1, Khong: 0  '))
