# Horizontal Flip

def flip_horizontal_axis(matrix):
    # Method 1
    # return list(reversed(matrix))

    # Method 2
    return matrix[::-1]

    # Method 3
    # arr = []
    # for i in range(len(matrix) - 1, -1, -1):
    #     arr.append(matrix[i])
    # return arr


if __name__ == '__main__':
    arr = [[[1, 1], [0, 0]],
           [[1, 0, 0], [0, 0, 1]],
           [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    for i in arr:
        print(flip_horizontal_axis(i))
