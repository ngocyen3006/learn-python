# Rotate a Square Image Counterclockwise

def rotate_square_image_ccw(matrix):
    res = []
    for i in zip(*matrix):
        res.append(list(i))
    matrix[:] = res[::-1]
    return matrix


if __name__ == '__main__':
    a = [[1, 0], [1, 0]]
    r_a = [[0, 0], [1, 1]]

    b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    r_b = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]

    print(rotate_square_image_ccw(a))
    print(rotate_square_image_ccw(a) == r_a)
    print("-" * 25)
    print(rotate_square_image_ccw(b))
    print(rotate_square_image_ccw(b) == r_b)
