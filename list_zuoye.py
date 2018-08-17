# input x, y, z, n thuoc N
# 0 <= i <= x; 0 <= j <= y; 0 <= k <= z
# i + j + k != n
# tra ve ket qua [[i,j,k]]

x = int(input())
y = int(input())
z = int(input())
n = int(input())

arr = [[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1)
       for k in range(0, z + 1) if i + j + k != n]
print(arr)
