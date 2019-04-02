# https://leetcode.com/problems/squares-of-a-sorted-array/
def sortedSquares(A):
    result = []
    n = len(A)
    i = 0
    j = n - 1
    while i != j:
        if A[i] ** 2 > A[j] ** 2:
            result.insert(0, A[i] ** 2)
            i += 1
        else:
            result.insert(0, A[j] ** 2)
            j -= 1
    if i == j:
        result.insert(0, A[i] ** 2)
    return result


def sortedSquares2(A):
    return sorted([i ** 2 for i in A])


if __name__ == '__main__':
    a = [-4, -1, 0, 3, 10]
    r_a = [0, 1, 9, 16, 100]

    b = [-7, -3, 2, 3, 11]
    r_b = [4, 9, 9, 49, 121]

    print(sortedSquares(a) == r_a)
    print(sortedSquares(b) == r_b)
