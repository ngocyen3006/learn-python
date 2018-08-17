# 2 <= n <= 10
# -100 <= arr[i] <= 100
# tim gia tri lon thu 2 trong mang

n = int(input())
arr = list(map(int, input().split()))

max_1st = max(arr)

arr_without_max_1st = [x for x in arr if x < max_1st]
max_2nd = max(arr_without_max_1st)
# for i in range(1, n):
#     if(max_2nd < arr[i] and arr[i] != max_1st):
#         max_2nd = arr[i]


print(max_2nd)