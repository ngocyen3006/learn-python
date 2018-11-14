def is_triangle(a, b, c):
    if c > a + b or a > b + c or b > a + c:
        return "No"
    return "Yes"


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    res = is_triangle(a, b, c)
    print(res)
