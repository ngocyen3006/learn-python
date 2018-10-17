import copy
from random import randint
from bubbleSort import bubbleSort
from countingSort import countingSort
from insertionSort import insertionSort
from mergeSort import mergeSort
from quickSort import quickSort
from radixSort import radixSort
from selectionSort import selectionSort
import time
from functools import reduce

lowerbound = -2 ** 31
upperbound = 2 ** 31


def gen(n):
    '''
    Generate array random number with n element
    '''
    return [randint(lowerbound, upperbound) for i in range(n)]


def averageList(arr):
    '''
    return average of the list
    '''
    return reduce((lambda x, y: x + y), arr) / len(arr)


# nTests = [100, 1000, 10000]   # List contains number of elements
nTests = map(int, [1e5, 1e6, 1e7])

# sortFunctions = [bubbleSort, countingSort, insertionSort, quickSort, radixSort, selectionSort, mergeSort]
sortFunctions = [countingSort, quickSort, radixSort, mergeSort]

# A dictionary contains average of a list run 10 times with n elements
averageRunTime = {"bubbleSort": [], "countingSort": [], "insertionSort": [],
                  "quickSort": [], "radixSort": [], "selectionSort": [], "mergeSort": []}

for n in nTests:
    print("----------------------------------------")
    print(f"Number of element: {n}")
    print("----------------------------------------")
    timeSort = {"bubbleSort": [], "countingSort": [], "insertionSort": [],
                "quickSort": [], "radixSort": [], "selectionSort": [], "mergeSort": []}
    for times in range(10):  # run 10 times with every sort functions
        arr = gen(n)
        print(f"----------> Time: {times}")
        for i in sortFunctions:
            print(f"Testing sort method: {i.__name__}")
            temp = copy.copy(arr)
            start = time.time()
            i(temp)
            end = time.time()
            run = round((end - start) * 1000, 4)  # time run sort function
            timeSort[i.__name__].append(run)
    for k in sortFunctions:
        average = round(averageList(timeSort[k.__name__]), 4)
        averageRunTime[k.__name__].append(average)
print(averageRunTime)
