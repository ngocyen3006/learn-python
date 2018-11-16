import string

with open("example.txt") as file:
    line = file.readline()
    punc = string.punctuation
    while line:
        line = line.lower().strip()
        for i in punc:
            line = " ".join(line.split(i))
        line = "\n".join(line.split())
        print(line)
        line = file.readline()
file.close()
