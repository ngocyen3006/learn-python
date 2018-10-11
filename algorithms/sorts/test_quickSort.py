from test_sort import Wrapper
from quickSort import quickSort


class TestQuickSort(Wrapper.TestSort):
    def sortMethod(self, arr):
        quickSort(arr)
