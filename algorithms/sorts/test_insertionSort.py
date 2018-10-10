from test_sort import Wrapper
from insertionSort import insertionSort


class TestInsertionSort(Wrapper.TestSort):
    def sortMethod(self, arr):
        insertionSort(arr)
