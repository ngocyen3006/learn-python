from test_sort import Wrapper
from countingSort import countingSort


class TestCountingSort(Wrapper.TestSort):
    def sortMethod(self, arr):
        countingSort(arr)
