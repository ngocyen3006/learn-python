def radixSort(arr):
    if len(arr) < 2:
        return
    maxArr = max(arr)
    digit = len(str(maxArr))
    temp = arr
    j = 0
    while j < digit:
        count = {0: [], 1: [], 2: [], 3: [], 4: [],
                 5: [], 6: [], 7: [], 8: [], 9: []}
        for i in temp:
            number = i // (10 ** j)
            modulo = number % 10
            count[modulo].append(i)
        temp = []
        for k in range(10):
            temp = temp + count[k]
        j += 1
    for i in range(len(arr)):
        arr[i] = temp[i]
