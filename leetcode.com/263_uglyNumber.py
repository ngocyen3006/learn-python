# 263. Ugly Number
# https://leetcode.com/problems/ugly-number/

# Runtime: 32ms (100.00%)
# Memory: 13.2 MB (5.15%)

def isUgly(num):
    for p in 2, 3, 5:
        while num % p == 0 < num:
            num /= p
    return num == 1


if __name__ == '__main__':
    testcase = {1: True,
                6: True,
                8: True,
                15: True,
                14: False,
                5 ** 10: True,
                2 ** 12: True,
                2 ** 5 * 3 ** 5 * 5 ** 2: True,
                2 ** 5 * 3 ** 5 * 5 ** 2 + 1: False}
    for k, v in testcase.items():
        print(isUgly(k) == v)
