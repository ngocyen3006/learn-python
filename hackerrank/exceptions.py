# https://www.hackerrank.com/challenges/exceptions/problem

n = int(input())
for i in range(n):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error Code: {e}")
