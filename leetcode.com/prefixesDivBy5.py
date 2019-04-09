# https://leetcode.com/problems/binary-prefix-divisible-by-5/

def prefixesDivBy5(A):
    for i in range(1, len(A)):
        A[i] += A[i - 1] * 2 % 5
    return [a % 5 == 0 for a in A]


def test():
    print(prefixesDivBy5([0, 1, 1]))  # [true,false,false]
    print(prefixesDivBy5([1, 1, 1]))  # [false,false,false]
    print(prefixesDivBy5([0, 1, 1, 1, 1, 1]))  # [true,false,false,false,true,false]
    print(prefixesDivBy5([1, 1, 1, 0, 1]))  # [false,false,false,false,false]


if __name__ == '__main__':
    test()
