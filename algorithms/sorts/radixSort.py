from copy import copy


def radixSort(arr):
    if len(arr) < 2:
        return
    maxArr = max(arr)
    digit = len(str(maxArr))
    j = 0
    while j < digit:
        count = {0: [], 1: [], 2: [], 3: [], 4: [],
                 5: [], 6: [], 7: [], 8: [], 9: []}
        for i in arr:
            number = i // (10 ** j)
            modulo = number % 10
            count[modulo].append(i)
        arr = []
        for k in range(10):
            arr = arr + count[k]
        j += 1
    return arr


a = [2, 3, 1, 6, 7, 5, 4, 8, 9, 10, 15, 14, 13, 12, 11]
print(radixSort(a))
# print(a)
