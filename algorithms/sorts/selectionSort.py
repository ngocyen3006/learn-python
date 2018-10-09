def selectionSort(a):
    for i in range(len(a)):
        minA = min(a[i:])
        indexM = a.index(minA, i)
        if a[i] != minA:
            a[indexM] = a[i]
            a[i] = minA
