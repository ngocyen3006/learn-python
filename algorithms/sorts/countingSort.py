def countingSort(arr):
    if len(arr) < 1:
        return
    count = {}
    maxArr = arr[0]
    minArr = arr[0]
    for i in range(len(arr)):
        number = arr[i]
        count.setdefault(number, 0)
        count[number] = count[number] + 1
        maxArr = max(maxArr, arr[i])
        minArr = min(minArr, arr[i])
    keys = sorted(count.keys())
    j = 0
    while j < len(arr):
        for i in keys:
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
