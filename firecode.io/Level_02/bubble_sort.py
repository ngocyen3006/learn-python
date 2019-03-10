# Bubble Sort

from random import randint


def bubble_sort(a_list):
    n = len(a_list)
    for j in range(1, n):
        for i in range(n - j):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
    return a_list


if __name__ == '__main__':
    for _ in range(5):
        a = [randint(1, 50) for _ in range(15)]
        print(a)
        print(bubble_sort(a))
        print("-" * 30)
