# https://www.hackerrank.com/challenges/designer-door-mat/problem

n, m = map(int, input().split())

char = ".|."

# top door
for i in range(1, n, 2):
    print((char * i).center(m, "-"))

# center line
print('WELCOME'.center(m, "-"))

# bottom door
for i in range(1, n, 2):
    print((char * (n - i - 1)).center(m, "-"))
