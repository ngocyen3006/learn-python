n = int(input())
mylist = []

for i in range(0, n):
    command_root = input()
    command = command_root.split(" ")
    if command[0] == "insert":
        mylist.insert(int(command[1]), int(command[2]))
    elif command[0] == "print":
        print(mylist)
    elif command[0] == "remove":
        mylist.remove(int(command[1]))
    elif command[0] == "append":
        mylist.append(int(command[1]))
    elif command[0] == "sort":
        mylist.sort()
    elif command[0] == "reverse":
        mylist.reverse()
    else:
        mylist.pop()
    
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print


