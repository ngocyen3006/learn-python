# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/

def generate(numRows):
    if numRows < 1:
        return []
    if numRows == 1:
        return [[1]]
    result = [[1], [1, 1]]
    if numRows == 2:
        return result
    for i in range(1, numRows - 1):
        temp = [1]
        for j in range(0, i):
            temp.append(result[i][j] + result[i][j + 1])
        temp.append(1)
        result.append(temp)
    return result


def test():
    testcase = {
        1: [[1]],
        2: [[1], [1, 1]],
        3: [[1], [1, 1], [1, 2, 1]],
        4: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]],
        5: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    }
    for k in testcase.keys():
        print(generate(k))
        print(generate(k) == testcase[k])
        print('-' * 10)


if __name__ == '__main__':
    test()
