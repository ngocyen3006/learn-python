# https://www.hackerrank.com/challenges/python-quest-1/problem

for i in range(1, int(input())):
    # print(i * str(i))
    print(int(i * (10 ** i - 1)/9))