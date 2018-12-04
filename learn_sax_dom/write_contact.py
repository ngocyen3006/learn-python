import xml.dom.minidom as xml

data_list = [{"Name": "Anh Thu", "Phone": "0989741258"},
             {"Name": "Thanh Thuy", "Phone": "0913258963"},
             {"Name": "Kim Cuong", "Phone": "0934369147"},
             {"Name": "Son Nam", "Phone": "0915654789"},
             {"Name": "Mai Quy", "Phone": "0982654123"},
             {"Name": "Tuan Thanh", "Phone": "0915369231"},
             {"Name": "Chu Van", "Phone": "0934852852"},
             {"Name": "Khang Khang", "Phone": "0907412365"},
             {"Name": "Mai Uyen", "Phone": "0909741147"},
             {"Name": "Thien Tuan", "Phone": "0989636363"}]

doc = xml.Document()
root = doc.createElement('contacts')
root.setAttribute("shelf", "Danh sach contact")

doc.appendChild(root)

for contact in data_list:
    name = contact['Name']
    phone = contact['Phone']

    contact_node = doc.createElement("contact")
    root.appendChild(contact_node)
    contact_node.setAttribute("phone", phone)
    contact_node.setAttribute("name", name)

f = open("contact.xml", "w", encoding="utf-8")
doc.writexml(f, newl="\n", indent="", addindent="  ", encoding="utf-8")
f.close()
