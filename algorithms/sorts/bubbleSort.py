def sort(arr):
    j = 1
    length = len(arr)
    while j < length:
        for i in range(length - j):
            if arr[i] > arr[i + 1]:
                t = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = t
            else:
                continue
        j = j + 1
    return arr
