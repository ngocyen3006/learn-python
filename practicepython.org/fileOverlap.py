def fileToList(file):
    list = []
    with open(file) as filename:
        line = filename.readline()
        while line:
            list.append(int(line))
            line = filename.readline()
    return list


primeList = fileToList("primenumbers.txt")
happyList = fileToList("happynumbers.txt")

overlapList = [x for x in primeList if x in happyList]
print(overlapList)
