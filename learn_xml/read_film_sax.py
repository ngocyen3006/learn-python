import xml.sax


class PhimHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.ten = ""
        self.nam_san_xuat = ""
        self.the_loai = ""
        self.dinh_dang = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        # attributes la dict
        self.CurrentData = tag
        if tag == "PHIM":
            print("* " * 30)
            self.ten = attributes["Ten"]
            self.nam_san_xuat = attributes["Nam_san_xuat"]
            print("Tên phim: %s - Năm sản xuất: %s" %
                  (self.ten, self.nam_san_xuat))

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "The_loai":
            print("Thể loại:", self.the_loai)
        elif self.CurrentData == "Dinh_dang":
            print("Định dạng:", self.dinh_dang)
            print("* " * 30)
            print("\n")
        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "The_loai":
            self.the_loai = content
        elif self.CurrentData == "Dinh_dang":
            self.dinh_dang = content


if (__name__ == "__main__"):
    # create an XMLReader
    parser = xml.sax.make_parser()
    # override the default ContextHandler
    Handler = PhimHandler()
    parser.setContentHandler(Handler)
    Ten_Tap_tin = "phim.xml"
    parser.parse(Ten_Tap_tin)
