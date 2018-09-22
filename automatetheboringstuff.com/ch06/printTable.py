# Table printer

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def maxWidths(tableData):
    colWidths = []
    for i in tableData:
        lenItems = []
        for j in i:
            lenItems = lenItems + [len(j)]
        colWidths = colWidths + [max(lenItems)]
    return colWidths


def printTable(tableData):
    colWidths = maxWidths(tableData)
    for i in zip(*tableData):
        print(end='\n')
        for j in range(len(i)):
            print(i[j].rjust(colWidths[j]), end=' ')


printTable(tableData)
