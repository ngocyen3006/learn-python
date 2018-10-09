def bubbleSort(arr):
    for j in range(1, len(arr)):
        for i in range(len(arr) - j):
            if arr[i] > arr[i + 1]:
                t = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = t
