# Horizontal Flip

def flip_horizontal_axis(matrix):
    matrix[:] = matrix[::-1]
    return matrix


if __name__ == '__main__':
    arr = [[[1, 1], [0, 0]],
           [[1, 0, 0], [0, 0, 1]],
           [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    for i in arr:
        print(flip_horizontal_axis(i))
