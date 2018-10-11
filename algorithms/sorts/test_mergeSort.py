from test_sort import Wrapper
from mergeSort import mergeSort


class TestMergeSort(Wrapper.TestSort):
    def sortMethod(self, arr):
        mergeSort(arr)
