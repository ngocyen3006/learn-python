def countingSort(arr):
    if len(arr) < 1:
        return
    count = {}
    for number in arr:
        count.setdefault(number, 0)
        count[number] = count[number] + 1
    minArr = min(arr)
    maxArr = max(arr)
    j = 0
    while j < len(arr):
        for i in range(minArr, maxArr + 1):
            if i in count.keys():
                if count[i] > 1:
                    k = 0
                    while k < count[i] and j + k < len(arr):
                        arr[j + k] = i
                        k += 1
                    j = j + k
                else:
                    arr[j] = i
                    j = j + 1
    pass
