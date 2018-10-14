from runtimeFunction import timed


@timed
def selectionSort(a):
    for i in range(len(a) - 1):
        minIndex = i
        for j in range(i + 1, len(a)):
            if a[j] < a[minIndex]:
                minIndex = j
        if minIndex != i:
            temp = a[i]
            a[i] = a[minIndex]
            a[minIndex] = temp
