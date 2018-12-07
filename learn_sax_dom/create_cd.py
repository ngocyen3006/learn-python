from xml.dom.minidom import Document

data_list = [{'ten': 'Happy new year',
              'casy': 'ABBA',
              'soluongbai': '10',
              'gia': '25000'}]

doc = Document()
root = doc.createElement('cds')

doc.appendChild(root)

for cd in data_list:
    ten = cd['ten']
    casy = cd['casy']
    soluong = cd['soluongbai']
    gia = cd['gia']

    cd_node = doc.createElement("cd")
    root.appendChild(cd_node)
    cd_node.setAttribute("ten", ten)

    singer = doc.createElement("ca_sy")
    cd_node.appendChild(singer)
    singer.appendChild(doc.createTextNode(casy))

    quan = doc.createElement("so_bai_hat")
    cd_node.appendChild(quan)
    quan.appendChild(doc.createTextNode(soluong))

    price = doc.createElement("gia_thanh")
    cd_node.appendChild(price)
    price.appendChild(doc.createTextNode(gia))

f = open("cd.xml", "w", encoding="utf-8")
doc.writexml(f, newl="\n", indent="", addindent="  ", encoding="utf-8")
f.close()
