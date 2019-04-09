# https://leetcode.com/problems/binary-prefix-divisible-by-5/

def prefixesDivBy5(A):
    res = []
    s = ''
    for b in A:
        s = s + str(b)
        res.append(int(s, 2) % 5 == 0)
    return res


def test():
    print(prefixesDivBy5([0, 1, 1]))  # [true,false,false]
    print(prefixesDivBy5([1, 1, 1]))  # [false,false,false]
    print(prefixesDivBy5([0, 1, 1, 1, 1, 1]))  # [true,false,false,false,true,false]
    print(prefixesDivBy5([1, 1, 1, 0, 1]))  # [false,false,false,false,false]


if __name__ == '__main__':
    test()
