def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def mergeSort(a):
    if len(a) < 2:
        return

    if len(a) == 2:
        if a[0] > a[1]:
            return swap(a, 0, 1)

    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]
    mergeSort(left)
    mergeSort(right)

    # merge leftArr and rightArr
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
            k += 1
        else:
            a[k] = right[j]
            j += 1
            k += 1

    # append vao mang mergeArr nhung phan tu con lai sau khi so sanh
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1
    pass
