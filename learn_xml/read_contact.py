import xml.sax


class Student(xml.sax.ContentHandler):
    sl = 0

    def __init__(self):
        self.currentData = ""
        self.name = ""
        self.phone = ""

    def startElement(self, tag, attributes):
        self.currentData = tag

        if tag == "contact":
            name = attributes['name']
            phone = attributes['phone']
            print(f"{str(Student.sl).ljust(5)}|{name.ljust(15)}|{phone.ljust(12)}")
            print("-" * 5 + "|" + "-" * 15 + "|" + "-" * 12)
        Student.sl += 1


if __name__ == '__main__':
    print("List of contacts")
    print("STT".ljust(5) + "|" + "Name".ljust(15) + "|" + "Phone".ljust(12))
    print("-" * 5 + "|" + "-" * 15 + "|" + "-" * 12)

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    handler = Student()
    parser.setContentHandler(handler)

    parser.parse('contact.xml')
