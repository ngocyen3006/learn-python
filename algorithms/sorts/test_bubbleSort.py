import test_sort
from bubbleSort import bubbleSort

class TestBubbleSort(test_sort.Wrapper.TestSort):
    def sortMethod(self, arr):
        bubbleSort(arr)