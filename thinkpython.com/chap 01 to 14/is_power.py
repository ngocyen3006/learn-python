import random


def is_power(a, b):
    if b == 0 or a // b % b != 0:
        return False
    return True


testCase = [[9, 3], [8, 2], [1000, 10], [144, 12], [8, 3], [10, 4]]

for i in testCase:
    print(f"{i[0],i[1]} : {is_power(i[0], i[1])}")

a = random.randint(0, 100000)
b = random.randint(1, 10000)
print(f"{a,b} : {is_power(a,b)}")

c = random.randint(0, 10000)
n = random.randint(0, 30)
d = c ** n
print(f"{c,d,n} : {is_power(c,d)}")
