from random import randint
from bubbleSort import bubbleSort
from countingSort import countingSort
from insertionSort import insertionSort
from mergeSort import mergeSort
from quickSort import quickSort
from radixSort import radixSort
from selectionSort import selectionSort
import time

lowerbound = -2 ** 31
upperbound = 2 ** 31


def gen(n):
    '''
    Generate sorted array random number with n element
    '''
    return sorted([randint(lowerbound, upperbound) for i in range(n)])


# nTests = [100, 1000, 10000]
nTests = map(int, [1e5, 1e6, 1e7])

# sortFunctions = [bubbleSort, selectionSort, insertionSort,
#                  quickSort, mergeSort, countingSort, radixSort]

sortFunctions = [quickSort, mergeSort, countingSort, radixSort]
timeSort = {"bubbleSort": [], "selectionSort": [], "insertionSort": [],
            "quickSort": [], "mergeSort": [], "countingSort": [], "radixSort": []}
for n in nTests:
    print("----------------------------------------")
    print(f"Number of element: {n}")
    print("----------------------------------------")
    arr = gen(n)
    for i in sortFunctions:
        print(f"Testing sort method: {i.__name__}")
        temp = arr
        start = time.time()
        i(temp)
        end = time.time()
        run = round((end - start) * 1000, 4)
        timeSort[i.__name__].append(run)
    print(timeSort)
