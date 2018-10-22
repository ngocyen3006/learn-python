import random

dict = {}

with open("ChineseDict.txt") as file:
    line = file.readline()
    while line:
        l = line.strip().split(": ")
        dict.update({l[0]: l[1]})
        line = file.readline()

n = int(input("Give me a number times you want to test: "))
i = 0
while i < n:
    k = random.choice(list(dict.keys()))
    print(k)
    user = input()

    while user != dict[k] and user.lower() != 'exit':
        print(k)
        user = input()

    if user.lower() == 'exit':
        print(dict[k])
        break
    i += 1
