# https://leetcode.com/problems/sort-array-by-parity/

def sortArrayByParity(A):
    if len(A) < 2:
        return A
    i, j = 0, len(A) - 1
    while i <= j:
        if A[i] % 2 == 0:
            i += 1
            continue
        if A[j] % 2 == 1:
            j -= 1
            continue
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        i += 1
        j -= 1
    return A


if __name__ == '__main__':
    print(sortArrayByParity([3, 1, 2, 4]))
    print(sortArrayByParity([0, 1]))
