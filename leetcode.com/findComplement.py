# https://leetcode.com/problems/number-complement/

def findComplement(num):
    n = bin(num)[2:]
    res = ''
    for i in n:
        if i == '0':
            res += '1'
        else:
            res += '0'
    return int(res, 2)


if __name__ == '__main__':
    print(findComplement(5))
    print(findComplement(5) == 2)
    print('-' * 10)

    print(findComplement(1))
    print(findComplement(1) == 0)
