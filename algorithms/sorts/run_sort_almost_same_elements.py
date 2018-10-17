import random
from bubbleSort import bubbleSort
from countingSort import countingSort
from insertionSort import insertionSort
from mergeSort import mergeSort
from quickSort import quickSort
from radixSort import radixSort
from selectionSort import selectionSort
import time
import copy

lowerbound = -2 ** 31
upperbound = 2 ** 31


def gen(n):
    h = int(n * 95 / 100)
    k = n - h
    element = random.choice(range(lowerbound, upperbound))
    arr = [element for i in range(h)]
    l = random.sample(range(lowerbound, upperbound), k)
    m = arr + l
    return m


# nTests = [100, 1000, 10000]
nTests = map(int, [1e5, 1e6, 1e7])

# sortFunctions = [bubbleSort, selectionSort, insertionSort,
#                  quickSort, mergeSort, countingSort, radixSort]


# sortFunctions = [quickSort, mergeSort, countingSort, radixSort]
timeSort = {"bubbleSort": [], "selectionSort": [], "insertionSort": [],
            "quickSort": [], "mergeSort": [], "countingSort": [], "radixSort": []}
for n in nTests:
    print("----------------------------------------")
    print(f"Number of element: {n}")
    print("----------------------------------------")
    arr = gen(n)
    random.shuffle(arr)
    for i in sortFunctions:
        print(f"Testing sort method: {i.__name__}")
        temp = copy.copy(arr)
        start = time.time()
        i(temp)
        end = time.time()
        run = round((end - start) * 1000, 4)
        timeSort[i.__name__].append(run)
    print(timeSort)
