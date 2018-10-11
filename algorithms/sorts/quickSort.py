import random


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def sort(a, first, last):
    i = first
    j = last
    if i >= j:  # sort mang trong hoac mang co 1 phan tu
        return

    if j == i + 1:  # so sanh 2 vi tri lien ke sort(a,i,i+1)
        if a[i] > a[j]:
            swap(a, i, j)
        return

    # sort mang co nhieu hon 2 phan tu
    pivotIndex = random.randint(first, last)
    pivot = a[pivotIndex]  # pivot la so ngau nhien thuoc mang a
    while i < j:
        # nhung phan tu be hon pivot dua ve ben trai mang
        while i <= last and a[i] < pivot:
            i = i + 1
        # phan tu lon hon hoac bang pivot dua ve ben phai mang
        while j > i and a[j] >= pivot:
            j = j - 1
        if i < j:
            swap(a, i, j)
            i = i + 1
            j = j - 1

    # all element in this sub array are the same
    if j == -1 or i == last + 1:
        return

    sort(a, first, j)
    sort(a, i, last)


def quickSort(a):
    sort(a, 0, len(a) - 1)
    pass


# a = [28, 58, 26, 28, 59, 68, 90, 95]
# quickSort(a)
# print(a)
