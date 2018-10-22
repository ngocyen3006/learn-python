# https://www.hackerrank.com/challenges/symmetric-difference/problem

M = int(input())
mList = set(map(int, input().split()))
N = int(input())
nList = set(map(int, input().split()))

s = sorted(mList ^ nList)
print(*s, sep='\n')
