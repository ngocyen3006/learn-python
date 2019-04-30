# 728. Self Dividing Numbers
# https://leetcode.com/problems/self-dividing-numbers/

def selfDividingNumbers(left, right):
    res = []
    for i in range(left, right + 1):
        if isSelfDividingNum(i):
            res.append(i)
    return res


def isSelfDividingNum(num):
    if num in range(1, 10):
        return True

    digit = str(num)

    if '0' in digit:
        return False

    for d in digit:
        if d == '1':
            continue
        if num % int(d) != 0:
            return False
    return True


if __name__ == '__main__':
    left, right = 1, 2000
    output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    print(selfDividingNumbers(left, right))
