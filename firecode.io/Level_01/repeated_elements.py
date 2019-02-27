# Repeated Elements in Array

def duplicate_items(list_numbers):
    arr = set(list_numbers)
    count = []
    for i in arr:
        if list_numbers.count(i) > 1:
            count.append(i)
    return count


print(duplicate_items([1, 3, 4, 2, 1]))
print(duplicate_items([1, 3, 4, 2, 1, 2, 4]))
