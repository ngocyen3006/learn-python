import xml.dom.minidom as xml

donvi = [{'Ten': 'Don vi A'},
         {'Ten': 'Don vi B'},
         {'Ten': 'Don vi C'},
         {'Ten': 'Don vi D'},
         {'Ten': 'Don vi E'}]

doc = xml.Document()
root = doc.createElement('DON_VI_S')
root.setAttribute("shelf", "Danh sach don vi")

doc.appendChild(root)

id = 0
for d in donvi:
    id = id + 1
    name = d['Ten']

    d_node = doc.createElement("DON_VI")
    root.appendChild(d_node)
    d_node.setAttribute("ID", str(id))
    d_node.setAttribute("Ten", name)

f = open("donvi.xml", "w", encoding="utf-8")
doc.writexml(f, newl="\n", indent="", addindent="  ", encoding="utf-8")
f.close()
