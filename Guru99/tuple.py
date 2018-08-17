n = int(input())
integer_list = list(map(int, input().split()))
    
tup = tuple(integer_list)
print(tup)
print(hash(tup))