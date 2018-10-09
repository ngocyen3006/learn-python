def selectionSort(a):
    for i in range(len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        if min != i:
            t = a[i]
            a[i] = a[min]
            a[min] = t
