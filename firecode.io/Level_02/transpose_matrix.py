# Find the Transpose of a Square Matrix

def transpose_matrix(matrix):
    res = []
    for element in zip(*matrix):
        res.append(list(element))
    matrix[:] = res[:]
    return matrix


def transpose_matrix_2(m):
    m[:] = map(list, zip(*m))
    return m


if __name__ == '__main__':
    a = [[1, 0], [1, 0]]
    r_a = [[1, 1], [0, 0]]

    b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    r_b = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    c = [[1]]
    r_c = [[1]]

    d = [[1, 0, 1], [1, 0, 1], [1, 0, 1]]
    r_d = [[1, 1, 1], [0, 0, 0], [1, 1, 1]]

    i = 1
    print(f"Case {i}: {a}")
    print(transpose_matrix(a) == r_a)
    print("-" * 25)
    i += 1
    print(f"Case {i}: {b}")
    print(transpose_matrix(b) == r_b)
    print("-" * 25)
    i += 1
    print(f"Case {i}: {c}")
    print(transpose_matrix(c) == r_c)
    print("-" * 25)
    i += 1
    print(f"Case {i}: {d}")
    print(transpose_matrix(d) == r_d)
    print("-" * 25)
