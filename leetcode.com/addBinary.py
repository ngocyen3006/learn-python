# https://leetcode.com/problems/add-binary/

def addBinary(a, b):
    inta = reverseInt(a)
    intb = reverseInt(b)
    return bin(inta + intb)[2:]


def reverseInt(a):
    a = a[::-1]
    n = 0
    res = 0
    for e in a:
        res += int(e) * 2 ** n
        n += 1
    return res


if __name__ == '__main__':
    a = '11'
    b = '1'
    print(addBinary(a, b))  # 100
    print('-' * 10)

    a = '1010'
    b = '1011'
    print(addBinary(a, b))  # 10101
    print('-' * 10)

    a = '1'
    b = '0'
    print(addBinary(a, b))  # 1
    print('-' * 10)

    a = '0'
    b = '1'
    print(addBinary(a, b))  # 1
    print('-' * 10)

    a = '0'
    b = '0'
    print(addBinary(a, b))  # 0
    print('-' * 10)

    a = '1'
    b = '1'
    print(addBinary(a, b))  # 10
    print('-' * 10)
