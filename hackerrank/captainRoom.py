# https://www.hackerrank.com/challenges/py-the-captains-room/problem

# Method 1 not use set
K = int(input())
room = list(map(int, input().split()))
count = {}
for e in room:
    count.setdefault(e, 0)
    count[e] = count[e] + 1

for k, v in count.items():
    if v != K:
        print(k)

# Method 2
K = int(input())
room = list(map(int, input().split()))
r = set(room)
print((sum(r) * K - sum(room)) // (K - 1))
