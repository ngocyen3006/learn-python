import xml.sax


def formatDate(self):
    s = self.split("-")
    return s[2] + '/' + s[1] + '/' + s[0]


class LearningOutcomes(xml.sax.ContentHandler):
    def __init__(self):
        self.currentData = ""
        self.ho_ten = ""
        self.ngay_sinh = ""
        self.ma_mon = ""
        self.diem = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag

        if tag == "HOC_SINH":
            print("* " * 30)
            self.ho_ten = attributes["Ho_ten"]
            self.ngay_sinh = formatDate(attributes["Ngay_sinh"])
            print(f"Ho ten: {self.ho_ten}")
            print(f"Ngay sinh: {self.ngay_sinh}")

        if tag == "KET_QUA":
            self.ma_mon = " ".join(attributes["Ma_mon"].split("_"))
            self.diem = f"{float(attributes['Diem']):.1f}"
            print(f"{self.ma_mon}: {self.diem}")

    def endElement(self, tag):
        self.CurrentData = ""


if (__name__ == "__main__"):
    parser = xml.sax.make_parser()

    Handler = LearningOutcomes()
    parser.setContentHandler(Handler)
    parser.parse("ket_qua_hoc_tap.xml")
