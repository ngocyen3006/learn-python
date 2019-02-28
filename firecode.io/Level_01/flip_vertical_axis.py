# Flip it!

def flip_vertical_axis(matrix):
    res = [0] * len(matrix)
    for i in range(len(matrix)):
        row = len(matrix[i])
        arr = [0] * row
        for j in range(row - 1, -1, -1):
            arr[row - j - 1] = matrix[i][j]
        res[i] = arr
    return res


if __name__ == '__main__':
    arr = [[[1, 1], [0, 0]],
           [[1, 0, 0], [0, 0, 1]],
           [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    for i in arr:
        print(flip_vertical_axis(i))
