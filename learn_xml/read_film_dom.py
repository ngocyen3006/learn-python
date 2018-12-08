from xml.dom.minidom import parse

xmlDoc = parse("phim.xml")
root_node = xmlDoc.documentElement

listElement = root_node.getElementsByTagName("PHIM")

for film_node in listElement:
    year = film_node.getAttribute('Nam_san_xuat')
    name = film_node.getAttribute('Ten')
    print(f"Name: {name} - Year: {year}")

    kind_node = film_node.getElementsByTagName('The_loai')[0]
    kind = kind_node.childNodes[0].data
    print(f"Movie genus: {kind}")

    LD_node = film_node.getElementsByTagName('Dinh_dang')[0]
    LD = LD_node.childNodes[0].data
    print(f'LD: {LD}')
    print('*************************************')
