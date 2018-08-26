# The "copy" module's "copy()" and "deepcopy()" functions

import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42

print(spam)
print(cheese)

print("-----------------")

example = [0, 1, 2, 3, 4, 5]
ex = example
ex[1] = 'hello'

print(example)
print(ex)

print("--------------------")
arr = [[1, 2, 3], [4, 5]]
arr2 = copy.deepcopy(arr)
arr2[1][0] = 7

print(arr)
print(arr2)
