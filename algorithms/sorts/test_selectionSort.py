import test_sort
from selectionSort import selectionSort


class TestSelectionSort(test_sort.Wrapper.TestSort):
    def sortMethod(self, arr):
        selectionSort(arr)
