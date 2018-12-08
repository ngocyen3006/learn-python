import xml.sax


class HINH_CHU_NHAT():
    def __init__(self, ten_hinh, dai, rong):
        self.ten_hinh = ten_hinh
        self.dai = dai
        self.rong = rong

    def tinh_chu_vi(self):
        return (self.dai + self.rong) * 2

    def tinh_dien_tich(self):
        return self.dai * self.rong

    def in_thuoc_tinh(self):
        chuoi = "\nDài: " + str(self.dai)
        chuoi += "\nRộng: " + str(self.rong)
        return chuoi

    def in_thong_tin(self):
        chuoi = "\nTên hình: " + self.ten_hinh
        chuoi += self.in_thuoc_tinh()
        chuoi += "\nChu vi: " + str(self.tinh_chu_vi())
        chuoi += "\nDiện tích: " + str(self.tinh_dien_tich())
        return chuoi


class HCNHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.ten = ""
        self.dai = 0
        self.rong = 0
        self.danh_sach = []

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "HCN":
            # print("* "*30)
            self.ten = attributes["Ten"]
            # print("Tên hình: %s" % (self.ten))

    # Call when an elements ends

    def endElement(self, tag):
        if self.CurrentData == "Dai":
            # print("Dài:", self.dai)
            pass
        elif self.CurrentData == "Rong":
            """"
            print("Rộng:", self.rong)
            print("* "*30)
            print("\n")
            """
            hinh_chu_nhat = HINH_CHU_NHAT(self.ten, float(self.dai),
                                          float(self.rong))
            self.danh_sach.append(hinh_chu_nhat)
        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "Dai":
            self.dai = content
        elif self.CurrentData == "Rong":
            self.rong = content


if (__name__ == "__main__"):
    # create an XMLReader
    parser = xml.sax.make_parser()
    # override the default ContextHandler
    Handler = HCNHandler()
    parser.setContentHandler(Handler)
    Ten_Tap_tin = "cac_hinh_chu_nhat.xml"
    parser.parse(Ten_Tap_tin)
    for hinh in Handler.danh_sach:
        print(hinh.in_thong_tin())
