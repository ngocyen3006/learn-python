# Rotate Linear Array


def rotate_left(list_numbers, k):
    if len(list_numbers) < 1:
        return
    k = k % len(list_numbers)
    return list_numbers[k:] + list_numbers[:k]


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    k = 2
    r_a = [3, 4, 5, 1, 2]

    print(a)
    print(rotate_left(a, k) == r_a)
    print("-" * 25)

    a = list(range(1, 10))
    k = 14
    r_a = [6, 7, 8, 9, 1, 2, 3, 4, 5]

    print(a)
    print(rotate_left(a, k) == r_a)
    print("-" * 25)

    a = list(range(1, 10))
    k = 4
    r_a = [5, 6, 7, 8, 9, 1, 2, 3, 4]

    print(a)
    print(rotate_left(a, k) == r_a)
    print("-" * 25)

    a = list(range(1, 10))
    k = 10
    r_a = [2, 3, 4, 5, 6, 7, 8, 9, 1]

    print(a)
    print(rotate_left(a, k) == r_a)
    print("-" * 25)

    a = [1]
    k = 7
    r_a = [1]

    print(a)
    print(rotate_left(a, k) == r_a)
    print("-" * 25)

    a = []
    k = 7

    print(a)
    print(rotate_left(a, k))
    print("-" * 25)
