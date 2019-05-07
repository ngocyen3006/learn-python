# 202. Happy Number
# https://leetcode.com/problems/happy-number/

def isHappy(n):
    cycle = set()
    while n != 1 and n not in cycle:
        cycle.add(n)
        n = sum(int(i) ** 2 for i in str(n))
    return n == 1


if __name__ == '__main__':
    testcases = [1111111, 19, 1, 5, 16, 84]

    for test in testcases:
        print(test, isHappy(test))
