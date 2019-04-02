# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

def repeatedNTimes(A):
    n = len(A) / 2 - 1
    sum_set_A = sum(set(A))
    return (sum(A) - sum_set_A) // n


if __name__ == '__main__':
    a = [1, 2, 3, 3]
    r_a = 3

    b = [2, 1, 2, 5, 3, 2]
    r_b = 2

    c = [5, 1, 5, 2, 5, 3, 5, 4]
    r_c = 5

    print(repeatedNTimes(a) == r_a)
    print(repeatedNTimes(b) == r_b)
    print(repeatedNTimes(c) == r_c)
