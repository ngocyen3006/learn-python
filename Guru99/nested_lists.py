if __name__ == '__main__':
    n = int(input())
    mylist = []

    for i in range(0, n):
        command = input()
        print("command: " + command)
        if command.star == "insert":
            number_i = int(input())
            number_element = int(input())
            mylist.insert(number_i, number_element)
        elif command == "print":
            print(mylist)
        elif command == "remove":
            number_remove = int(input())
            mylist.remove(number_remove)
        elif command == "append":
            number_append = int(input())
            mylist.append(number_append)
        elif command == "sort":
            mylist.sort()
        elif command == "reverse":
            mylist.reverse()
        else:
            mylist.pop()
