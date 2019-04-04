# https://leetcode.com/problems/add-binary/

def addBinary2(a, b):
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


def addBinary(a, b):
    if len(a) < len(b):
        a = '0' * (len(b) - len(a)) + a
    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b
    a = list(map(str, a[::-1]))
    b = list(map(str, b[::-1]))

    hold = '0'
    res = ''
    for i in range(len(a)):
        if hold == '1':
            t = addBin(b[i], hold)
            if t == '10':
                b[i] = '0'
                hold = '1'
            else:
                b[i] = t
                hold = '0'

        temp = addBin(a[i], b[i])
        if temp == '10':
            hold = '1'
            res = '0' + res
        else:
            res = temp[0] + res

    if hold == '1':
        res = hold + res
    return res


def addBin(a, b):
    if a == '1' and b == '1':
        return '10'
    if a == '0' and b == '0':
        return '0'
    return '1'


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

    a = '1011'
    b = '1011'
    print(addBinary(a, b))  # 10110
    print('-' * 10)

    a = '1111'
    b = '1011'
    print(addBinary(a, b))  # 11010
    print('-' * 10)
