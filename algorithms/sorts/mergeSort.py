from runtimeFunction import timed


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


@timed
def mergeSort(a):
    if len(a) < 2:
        pass
    elif len(a) == 2:
        if a[0] > a[1]:
            swap(a, 0, 1)
    else:
        mid = len(a) // 2
        leftArr = a[:mid]
        rightArr = a[mid:]
        mergeSort(leftArr)
        mergeSort(rightArr)

        # merge leftArr and rightArr
        i = j = k = 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                a[k] = leftArr[i]
                i += 1
                k += 1
            else:
                a[k] = rightArr[j]
                j += 1
                k += 1

        # append vao mang mergeArr nhung phan tu con lai sau khi so sanh
        while i < len(leftArr):
            a[k] = leftArr[i]
            i += 1
            k += 1
        while j < len(rightArr):
            a[k] = rightArr[j]
            j += 1
            k += 1
    pass
