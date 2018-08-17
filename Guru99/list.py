print("-----------")
mylist = []
print(mylist)

mylist.append(4)
print(mylist)
print("-----------")


mylist.append(2)
print(mylist)
print("-----------")

mylist.append(3)
print(mylist)
print("-----------")


print(mylist[0])  # prints 1
print(mylist[1])  # prints 2
print(mylist[2])  # prints 3
print(mylist)

# prints out 1,2,3
for x in mylist:
    print(x)

print("----------------------")
mylist.remove(2)
print(mylist)

print("----------------------")
del mylist[0]
print(mylist)

print("----------------------")
arr = [1,2,3]
arr2 = [i ** 2 for i in arr]
print(arr2)