from runtimeFunction import timed
import random


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def sort(a, first, last):
    i = first
    j = last
    if i >= j:  # check len(arr) <= 1
        return

    if j == i + 1:  # check len(arr) = 2
        if a[i] > a[j]:
            swap(a, i, j)
        return

    # len(arr) > 2
    i += 1
    pivotIndex = random.randint(first, last)  # pivot is random number
    pivot = a[pivotIndex]

    swap(a, first, pivotIndex)
    while i <= j:
        # arr[element] < pivot
        while i <= last and a[i] < pivot:
            i += 1
        # arr[element] > pivot
        while j >= i and a[j] >= pivot:
            j -= 1
        if i < j:
            swap(a, i, j)
            i += 1
            j -= 1
    swap(a, j, first)

    sort(a, first, j - 1)
    sort(a, i, last)


@timed
def quickSort(a):
    sort(a, 0, len(a) - 1)
    pass
