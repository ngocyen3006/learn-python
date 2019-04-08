# https://leetcode.com/problems/sort-array-by-parity-ii/

def sortArrayByParityII(A):
    if len(A) < 2:
        return A
    i, j = 0, 1
    while i <= len(A) - 1 and j <= len(A) - 1:
        if A[i] % 2 == 0:
            i += 2
            continue
        if A[j] % 2 == 1:
            j += 2
            continue
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        i += 2
        j += 2
    return A


if __name__ == '__main__':
    print(sortArrayByParityII([3, 1, 2, 4]))
    print(sortArrayByParityII([0, 1]))
