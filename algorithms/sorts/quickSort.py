import random


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def sort(a, first, last):
    i = first
    j = last
    if i >= j:  # sort mang trong hoac mang co 1 phan tu
        pass
    elif j == i + 1:  # so sanh 2 vi tri lien ke sort(a,i,i+1)
        if a[i] > a[j]:
            swap(a, i, j)
    else:  # sort mang co nhieu hon 2 phan tu
        pivot = random.choice(a)  # pivot la so ngau nhien thuoc mang a
        loop = True
        while loop:
            # nhung phan tu be hon pivot dua ve ben trai mang
            while i <= j and a[i] < pivot:
                i = i + 1
            # phan tu lon hon hoac bang pivot dua ve ben phai mang
            while j >= i and a[j] >= pivot:
                j = j - 1
            if j < i:
                loop = False
            else:
                swap(a, i, j)
                i = i + 1
                j = j - 1
        sort(a, first, j)
        sort(a, i, last)
    pass


def quickSort(a):
    sort(a, 0, len(a) - 1)
    pass
