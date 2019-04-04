# https://leetcode.com/problems/sqrtx/

import math


def mySqrt(x):
    if x < 0:
        return
    return int(math.sqrt(x))


if __name__ == '__main__':
    testcase = {4: 2,
                8: 2}

    for k, v in testcase.items():
        print(mySqrt(k) == v)
