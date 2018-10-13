from test_sort import Wrapper
from radixSort import radixSort


class TestRadixSort(Wrapper.TestSort):
    def sortMethod(self, arr):
        radixSort(arr)
