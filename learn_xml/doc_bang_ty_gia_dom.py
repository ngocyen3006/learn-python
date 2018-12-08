from xml.dom.minidom import parse

xmlDoc = parse("bang_ty_gia.xml")
root_node = xmlDoc.documentElement

listElement = root_node.getElementsByTagName("Exrate")
print("Code".ljust(5) + "Name".ljust(20) + "Buy".rjust(10) + "Transfer".rjust(15) + "Sell".rjust(15))

for node in listElement:
    currencyCode = node.getAttribute('CurrencyCode')
    currencyName = node.getAttribute('CurrencyName')
    buy = f"{float(node.getAttribute('Buy')):,.2f}"
    transfer = f"{float(node.getAttribute('Transfer')):,.2f}"
    sell = f"{float(node.getAttribute('Sell')):,.2f}"

    print(f"{currencyCode.ljust(5)}{currencyName.ljust(20)}", end="")
    print(f"{buy.rjust(10)}{transfer.rjust(15)}{sell.rjust(15)}")
