import xml.sax


class RateHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentData = ""
        self.CurrencyCode = ""
        self.CurrencyName = ""
        self.Buy = ""
        self.Transfer = ""
        self.Sell = ""

    def startElement(self, tag, attributes):
        self.currentData = tag
        if tag == "Exrate":
            currencyCode = attributes['CurrencyCode']
            currencyName = attributes['CurrencyName']
            buy = f"{float(attributes['Buy']):,.2f}"
            transfer = f"{float(attributes['Transfer']):,.2f}"
            sell = f"{float(attributes['Sell']):,.2f}"
            print(f"{currencyCode.ljust(5)}{currencyName.ljust(20)}", end="")
            print(f"{buy.rjust(10)}{transfer.rjust(15)}{sell.rjust(15)}")

    def endElement(self, tag):
        self.currentData = ""

    # def characters(self,content)


if __name__ == '__main__':
    print("Code".ljust(5) + "Name".ljust(20) + "Buy".rjust(10) + "Transfer".rjust(15) + "Sell".rjust(15))
    parser = xml.sax.make_parser()
    handle = RateHandler()
    parser.setContentHandler(handle)
    parser.parse('bang_ty_gia.xml')
