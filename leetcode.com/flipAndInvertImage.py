# https://leetcode.com/problems/flipping-an-image/

def flipimagehorizontally(A):
    return [array[::-1] for array in A]


def invertImage(array):
    return [1 if i == 0 else 0 for i in array]


def flipAndInvertImage(A):
    flip_hor = flipimagehorizontally(A)
    return [invertImage(array) for array in flip_hor]


if __name__ == '__main__':
    a = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    r_a = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

    b = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    r_b = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]

    print(flipAndInvertImage(a))
    print(flipAndInvertImage(a) == r_a)
    print('-' * 15)

    print(flipAndInvertImage(b))
    print(flipAndInvertImage(b) == r_b)
