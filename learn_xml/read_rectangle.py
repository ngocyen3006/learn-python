import xml.sax


class HCNHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.ten = ""
        self.dai = 0
        self.rong = 0

    # Call when an element starts
    def startElement(self, tag, attributes):
        # attributes la dict
        self.CurrentData = tag
        if tag == "HCN":
            print("* " * 30)
            self.ten = attributes["Ten"]
            print("Tên: {}".format(self.ten))

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "Dai":
            print("Dai:", self.dai)
        elif self.CurrentData == "Rong":
            print("Rong:", self.rong)
            print("* " * 30)
            print("\n")
        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "Dai":
            self.dai = content
        elif self.CurrentData == "Rong":
            self.rong = content


if __name__ == "__main__":
    # create an XMLReader
    parser = xml.sax.make_parser()
    # override the default ContextHandler
    Handler = HCNHandler()
    parser.setContentHandler(Handler)
    Ten_Tap_tin = "cac_hinh_chu_nhat.xml"
    parser.parse(Ten_Tap_tin)
