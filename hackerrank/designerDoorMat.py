# https://www.hackerrank.com/challenges/designer-door-mat/problem

s = list(map(int, input().split()))
n = s[0]
m = s[1]

char = ".|."

# top door
for i in range(0, n // 2):
    print((char * i).rjust(m // 2 - 1, "-") +
          char + (char * i).ljust(m // 2 - 1, "-"))

# center line
print('WELCOME'.center(m, "-"))

# bottom door
for i in range(0, n // 2):
    print((char * ((n // 2) - i - 1)).rjust(m // 2 - 1, "-") +
          char + (char * ((n // 2) - i - 1)).ljust(m // 2 - 1, "-"))
