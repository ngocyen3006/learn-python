# Flip it!

def flip_vertical_axis(matrix):
    arr = [0] * len(matrix)
    for i in range(len(matrix)):
        arr[i] = list(reversed(matrix[i]))
    return arr


if __name__ == '__main__':
    arr = [[[1, 1], [0, 0]],
           [[1, 0, 0], [0, 0, 1]],
           [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    for i in arr:
        print(flip_vertical_axis(i))
