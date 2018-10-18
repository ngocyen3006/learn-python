count = {}
with open("namesList.txt") as file:
    line = file.readline()
    while line:
        line = line.strip()
        count.setdefault(line, 0)
        count[line] += 1
        line = file.readline()
print(count)
